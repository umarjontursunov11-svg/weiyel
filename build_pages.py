#!/usr/bin/env python3
"""
Static SEO pages for the Weiyel O'zbekiston catalog.

Runs on Vercel as the build command (and locally for testing):
    python3 build_pages.py            -> writes ./public

For every product it writes /uz/p/<slug>.html and /ru/p/<slug>.html, plus
category pages, sitemaps and robots.txt, and copies the existing site files
(index.html, admin.html, products.js, d/, ...) next to them.

Admin-panel edits (Supabase sm_products / sm_settings) are pulled in at build
time when the network is reachable; pages also refresh price/hidden in the
browser, so an edit shows up before the next deploy.
"""
import html, json, os, re, shutil, sys, urllib.request
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
SB_URL = "https://fwuqtrfoenejodufnwyb.supabase.co"
SB_KEY = "sb_publishable_5nsgpaWXtJYY1gNY7jzDCA_KRJclQjr"
PROD = os.environ.get("VERCEL_PROJECT_PRODUCTION_URL") or "weiyel-uz.vercel.app"
BASE = os.environ.get("SITE_URL", "https://" + PROD).rstrip("/")
TODAY = date.today().isoformat()
PER_PAGE = 120  # products per category page

# ---------------------------------------------------------------- data
def load_js_json(path, prefix):
    s = open(path, encoding="utf-8").read()
    i = s.index(prefix) + len(prefix)
    if prefix.startswith("window.WY"):
        return json.loads(s[i:s.index(";\nwindow.dispatchEvent")])
    return json.loads(s[i:s.rindex(")")])

WY = load_js_json(os.path.join(ROOT, "products.js"), "window.WY=")
ROWS, SUBS, NAMES, IP, CS = WY["rows"], WY["subs"], WY["names"], WY["ip"], WY["cs"]
DET = {}
for k in range((len(ROWS) + CS - 1) // CS):
    p = os.path.join(ROOT, "d", f"{k}.js")
    if os.path.exists(p):
        s = open(p, encoding="utf-8").read()
        DET.update(json.loads(s[s.index(",") + 1:s.rindex(")")]))

def sb_get(path):
    try:
        req = urllib.request.Request(f"{SB_URL}/rest/v1/{path}", headers={"apikey": SB_KEY, "Authorization": "Bearer " + SB_KEY})
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print("supabase skipped:", e)
        return []

OVR = {r["catno"]: r.get("data") or {} for r in sb_get("sm_products?select=catno,data")}
SETTINGS = {r["key"]: r.get("value") for r in sb_get("sm_settings?select=key,value")}

DEALER = {
    "name": "STANDART VA METROLOGIYA MCHJ",
    "phones": ["+998 90 939-71-83", "+998 98 361-71-83"],
    "whatsapp": "+998 33 078-98-89",
    "telegram": "standartgsouz",
    "email": "standartvametrologiya@gmail.com",
    "address": {"uz": "Toshkent sh., Yakkasaroy tumani, Yakkasaroy ko‘chasi, 5-uy, 12-xona",
                "ru": "г. Ташкент, Яккасарайский район, ул. Яккасарай, дом 5, офис 12"},
}
if isinstance(SETTINGS.get("dealer"), dict):
    DEALER.update({k: v for k, v in SETTINGS["dealer"].items() if v not in (None, "")})

def img_url(code):
    if not code: return ""
    return code if code.startswith("http") else IP.get(code[0], "") + code[1:]

# apply admin overrides: edits, hidden, new products, price
IDX = {r[0]: i for i, r in enumerate(ROWS)}
PRODUCTS = []
for r in ROWS:
    PRODUCTS.append({"no": r[0], "name": r[1], "cas": r[2], "spec": r[3], "sub": SUBS[r[4]],
                     "img": img_url(r[5]), "price": "", "det": DET.get(r[0], {})})
for no, d in OVR.items():
    if no in IDX:
        p = PRODUCTS[IDX[no]]
    else:
        if d.get("hidden") or not d.get("name") or d.get("sub") not in NAMES: continue
        p = {"no": no, "name": d["name"], "cas": "", "spec": "", "sub": d["sub"], "img": "", "price": "", "det": {}}
        PRODUCTS.insert(0, p)
    for k in ("name", "cas", "spec", "img", "price"):
        if d.get(k): p[k] = d[k]
    if d.get("sub") in NAMES: p["sub"] = d["sub"]
    if d.get("details"): p["det"] = d["details"]
    p["hidden"] = bool(d.get("hidden"))
PRODUCTS = [p for p in PRODUCTS if not p.get("hidden")]

# ---------------------------------------------------------------- text
MAIN = {
    "1": ("Oziq-ovqat", "Пищевые продукты"),
    "2": ("Ekologiya", "Экология"),
    "3": ("Po‘lat va rangli metallar", "Сталь и цветные металлы"),
    "4": ("Kimyoviy mahsulotlar", "Химическая продукция"),
    "5": ("Minerallar, ko‘mir, neft", "Минералы, уголь, нефть"),
    "6": ("Klinik dori vositalari", "Клинические препараты"),
    "7": ("Sanoat va iste’mol mollari", "Промышленные товары"),
    "8": ("Fizik-texnik xossalar", "Физико-технические свойства"),
    "9": ("Biologik sifat nazorati", "Биологический контроль качества"),
}
L = {
    "uz": dict(i=0, html="uz", og="uz_UZ", other="ru", home="Bosh sahifa", catalog="Katalog", all="Barcha yo‘nalishlar",
               catno="Katalog №", spec_h="Texnik xususiyatlari", packs="Qadoq hajmi", comp="Tarkibi va attestatsiya qiymatlari",
               comp_h=["Modda", "Attestatsiya qiymati", "Noaniqlik (k=2)", "CAS"], volume="Hajmi", price="Narxi",
               ask="Narx so‘rash", add="So‘rovga qo‘shish", related="Shu bo‘limdagi boshqa mahsulotlar",
               dealer="Weiyel’ning O‘zbekistondagi yagona rasmiy dileri", noimg="Rasm mavjud emas", mol="Molekula tuzilishi",
               products="ta mahsulot", page="Sahifa", prev="← Oldingi", next="Keyingi →", hidden="Bu mahsulot hozircha mavjud emas.",
               cert="Har bir namuna sertifikati bilan yetkaziladi", contact="Aloqa", wa="WhatsApp", tg="Telegram",
               std="standart namuna", stds="Standart namunalar", nodata="Batafsil ma’lumot va sertifikatni so‘rov orqali yuboramiz.",
               t_suffix="standart namuna — Weiyel O‘zbekiston",
               d_tpl="{name}{cas} — Weiyel sertifikatlangan standart namunasi. {spec}O‘zbekistonda rasmiy diler STANDART VA METROLOGIYA: sertifikat bilan yetkazib berish, narx so‘rov bo‘yicha.",
               lbl={"Form": "Shakli", "Term of validit": "Yaroqlilik muddati", "Term of validity": "Yaroqlilik muddati",
                    "Molecular Formula": "Molekulyar formula", "Stroma": "Matritsa", "Packing": "Qadoq", "Save conditions": "Saqlash sharoiti",
                    "Storage conditions": "Saqlash sharoiti", "Concentration": "Konsentratsiya", "Solvent": "Erituvchi", "Purity": "Tozaligi",
                    "Subculture": "Ozuqa muhiti", "Subculturing": "Qo‘llash tartibi", "Growth conditions": "O‘stirish sharoiti",
                    "Safety level": "Xavfsizlik darajasi", "Application": "Qo‘llanilishi", "Transportation conditions": "Tashish sharoiti",
                    "Specification": "Hajmi", "Traceability": "Kuzatiluvchanlik", "Usage": "Foydalanish", "Remark": "Izoh", "Remarks": "Izoh"},
               v={"Liquid State": "Suyuq", "Solid State": "Qattiq", "Solid-Liquid Coexistence": "Qattiq-suyuq", "Pure": "Toza modda", "Water": "Suv",
                  "Methanol": "Metanol", "Acetonitrile": "Atsetonitril", "Ethanol": "Etanol", "Acetone": "Aseton", "Hexane": "Geksan",
                  "n-Hexane": "n-Geksan", "Toluene": "Toluol", "Soil": "Tuproq", "Filter Paper": "Filtr qog‘oz", "Activated carbon": "Faollashtirilgan ko‘mir",
                  "Petroleum": "Neft", "Fertilizer": "O‘g‘it", "Standard": "Standart", "Brown ampoule": "Jigarrang ampula", "Plastic bottle": "Plastik shisha",
                  "Brown glass bottle": "Jigarrang shisha idish", "Ampoule bottle": "Ampula", "Brown vial": "Jigarrang flakon", "Plastic box": "Plastik quti",
                  "White plastic bottle": "Oq plastik idish", "Activated carbon tube": "Ko‘mirli naycha", "box": "Quti", "Box": "Quti", "Vial": "Flakon",
                  "Brown plastic bottle": "Jigarrang plastik idish", "Aluminum foil bag": "Alyumin folga paket", "Glass bottle": "Shisha idish"},
               months="oy",
               temp={"at 2-8 ℃": "2–8 ℃ haroratda", "Room temperature": "Xona haroratida", "in cool": "Salqin joyda", "at -20 ℃": "-20 ℃ haroratda", "at -18 ℃": "-18 ℃ haroratda"},
               std_txt="germetik va yorug‘likdan himoyalangan joyda saqlang. Ishlatishdan oldin (20±3) ℃ gacha keltirib, yaxshilab chayqating. Ochilgandan so‘ng darhol ishlating, ifloslanishdan saqlang."),
    "ru": dict(i=1, html="ru", og="ru_RU", other="uz", home="Главная", catalog="Каталог", all="Все направления",
               catno="Кат. №", spec_h="Технические характеристики", packs="Фасовка", comp="Состав и аттестованные значения",
               comp_h=["Компонент", "Аттестованное значение", "Неопределённость (k=2)", "CAS"], volume="Фасовка", price="Цена",
               ask="Запросить цену", add="В запрос", related="Другие позиции раздела",
               dealer="Единственный официальный дилер Weiyel в Узбекистане", noimg="Нет изображения", mol="Структура молекулы",
               products="позиций", page="Страница", prev="← Назад", next="Далее →", hidden="Эта позиция временно недоступна.",
               cert="Каждый образец поставляется с сертификатом", contact="Контакты", wa="WhatsApp", tg="Telegram",
               std="стандартный образец", stds="Стандартные образцы", nodata="Подробные характеристики и сертификат отправим по запросу.",
               t_suffix="стандартный образец — Weiyel Узбекистан",
               d_tpl="{name}{cas} — сертифицированный стандартный образец Weiyel. {spec}Официальный дилер в Узбекистане STANDART VA METROLOGIYA: поставка с сертификатом, цена по запросу.",
               lbl={"Form": "Форма", "Term of validit": "Срок годности", "Term of validity": "Срок годности", "Molecular Formula": "Молекулярная формула",
                    "Stroma": "Матрица", "Packing": "Упаковка", "Save conditions": "Условия хранения", "Storage conditions": "Условия хранения",
                    "Concentration": "Концентрация", "Solvent": "Растворитель", "Purity": "Чистота", "Subculture": "Питательная среда",
                    "Subculturing": "Порядок применения", "Growth conditions": "Условия культивирования", "Safety level": "Уровень биобезопасности",
                    "Application": "Применение", "Transportation conditions": "Условия транспортировки", "Specification": "Фасовка",
                    "Traceability": "Прослеживаемость", "Usage": "Применение", "Remark": "Примечание", "Remarks": "Примечание"},
               v={"Liquid State": "Жидкость", "Solid State": "Твёрдое вещество", "Solid-Liquid Coexistence": "Твёрдое/жидкое", "Pure": "Чистое вещество",
                  "Water": "Вода", "Methanol": "Метанол", "Acetonitrile": "Ацетонитрил", "Ethanol": "Этанол", "Acetone": "Ацетон", "Hexane": "Гексан",
                  "n-Hexane": "н-Гексан", "Toluene": "Толуол", "Soil": "Почва", "Filter Paper": "Фильтровальная бумага", "Activated carbon": "Активированный уголь",
                  "Petroleum": "Нефть", "Fertilizer": "Удобрение", "Standard": "Стандарт", "Brown ampoule": "Ампула тёмного стекла",
                  "Plastic bottle": "Пластиковый флакон", "Brown glass bottle": "Флакон тёмного стекла", "Ampoule bottle": "Ампула",
                  "Brown vial": "Виала тёмного стекла", "Plastic box": "Пластиковая коробка", "White plastic bottle": "Белый пластиковый флакон",
                  "Activated carbon tube": "Угольная трубка", "box": "Коробка", "Box": "Коробка", "Vial": "Виала", "Brown plastic bottle": "Тёмный пластиковый флакон",
                  "Aluminum foil bag": "Пакет из алюминиевой фольги", "Glass bottle": "Стеклянный флакон"},
               months="мес.",
               temp={"at 2-8 ℃": "При 2–8 ℃", "Room temperature": "При комнатной температуре", "in cool": "В прохладном месте", "at -20 ℃": "При −20 ℃", "at -18 ℃": "При −18 ℃"},
               std_txt="хранить герметично, в защищённом от света месте. Перед использованием выдержать до (20±3) ℃ и перемешать. После вскрытия использовать сразу, избегать загрязнения."),
}
STD_EN = "Store airtight and away from light place."

def e(s): return html.escape(str(s or ""), quote=True)
def sub_html(s): return re.sub(r"&lt;(/?)sub&gt;", r"<\1sub>", e(s))
def plain(s): return re.sub(r"</?sub>", "", str(s or ""))

def tv(T, k, v):
    if v in T["v"]: return e(T["v"][v])
    m = re.match(r"^([\d.]+)\s*Months?$", v, re.I)
    if m: return f"{m.group(1)} {T['months']}"
    if k in ("Save conditions", "Storage conditions") and STD_EN in v:
        pre = v.split(STD_EN)[0].strip()
        if pre in T["temp"]: return e(T["temp"][pre] + ", " + T["std_txt"])
    return sub_html(v)

def slugify(no, name):
    s = re.sub(r"[^a-z0-9]+", "-", (no + " " + plain(name)).lower()).strip("-")
    return s[:90].rstrip("-") or re.sub(r"[^a-z0-9]+", "-", no.lower())

seen = set()
for p in PRODUCTS:
    s = slugify(p["no"], p["name"]); base = s; n = 2
    while s in seen: s = f"{base}-{n}"; n += 1
    seen.add(s); p["slug"] = s

BY_SUB = {}
for p in PRODUCTS: BY_SUB.setdefault(p["sub"], []).append(p)
SUB_ORDER = [k for k in NAMES if k in BY_SUB]

def main_of(k): return k.split("_")[0]
def sub_name(k, T): return NAMES[k][T["i"]]
def main_name(m, T): return MAIN[m][T["i"]]
def url_p(lang, p): return f"/{lang}/p/{p['slug']}.html"
def url_sub(lang, k, page=1): return f"/{lang}/k/{k}.html" if page == 1 else f"/{lang}/k/{k}-{page}.html"
def url_main(lang, m): return f"/{lang}/k/{m}.html"

# ---------------------------------------------------------------- layout
CSS = """:root{--bg:#f6f8fb;--surface:#fff;--ink:#0f1b2d;--muted:#5b6778;--line:#e3e8ef;--brand:#0a6cff;--brand2:#00b4a6;--soft:#e8f1ff;--dark:#0b1626}
*{box-sizing:border-box;margin:0;padding:0}[hidden]{display:none!important}
body{font:500 15px/1.6 Manrope,system-ui,-apple-system,"Segoe UI",sans-serif;background:var(--bg);color:var(--ink)}
a{color:var(--brand);text-decoration:none}a:hover{text-decoration:underline}
.w{width:min(1120px,100% - 32px);margin-inline:auto}
header{background:var(--dark);color:#fff;position:sticky;top:0;z-index:5}
.hb{display:flex;align-items:center;justify-content:space-between;gap:12px;height:64px}
.logo{display:flex;align-items:center;gap:10px;color:#fff;font-weight:800;font-size:19px}.logo:hover{text-decoration:none}
.logo i{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,var(--brand),var(--brand2));display:grid;place-items:center}
.hn{display:flex;gap:18px;align-items:center;font-weight:700;font-size:14px}.hn a{color:#cfd9e8}.hn a:hover{color:#fff;text-decoration:none}
.lg{border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:5px 12px;color:#fff!important}
.bc{font-size:13px;color:var(--muted);padding:18px 0 6px;display:flex;flex-wrap:wrap;gap:6px}.bc a{color:var(--muted)}.bc span{opacity:.5}
main{padding-bottom:56px}
h1{font-size:clamp(24px,3.4vw,36px);line-height:1.2;letter-spacing:-.01em;margin:6px 0 10px;text-wrap:balance;overflow-wrap:anywhere}
.lead{color:var(--muted);max-width:70ch;margin-bottom:18px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:18px}
.pg{display:grid;grid-template-columns:360px 1fr;gap:28px;padding:26px;margin-top:10px}
.media{display:grid;gap:12px;align-content:start}
.img{aspect-ratio:1/1;max-width:100%;border:1px solid var(--line);border-radius:14px;background:#fff;display:grid;place-items:center;overflow:hidden;color:#9fb3cf;font-weight:700;font-size:13px;text-align:center}
.img img{width:100%;height:100%;object-fit:contain}
.mol{border:1px solid var(--line);border-radius:14px;background:#fff;padding:10px;text-align:center;color:var(--muted);font-size:12px;font-weight:700}
.mol img{max-width:100%;max-height:150px;object-fit:contain;display:block;margin:0 auto 4px}
.cat{color:var(--brand);font-weight:800;font-size:12px;letter-spacing:.1em;text-transform:uppercase}
.ids{display:flex;flex-wrap:wrap;gap:8px;margin:4px 0 18px}
.ids span{background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:7px 12px;font-size:13px;font-weight:600}
.ids b{color:var(--muted);margin-right:4px}.ids .pr{background:#e6fbf5;border-color:#b5ecd9;color:#067a5f;font-weight:800}
h2{font-size:17px;margin:22px 0 10px}
table{width:100%;border-collapse:collapse;font-size:14px}
.sp th,.sp td{padding:10px 12px;border-top:1px solid var(--line);text-align:left;vertical-align:top}
.sp th{width:38%;color:var(--muted);background:var(--bg);font-weight:700}.sp td{overflow-wrap:anywhere}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:12px}.tw table{min-width:480px}
.tw th{background:var(--bg);color:var(--muted);text-align:left;padding:10px 12px;font-size:12px}.tw td{padding:10px 12px;border-top:1px solid var(--line)}
.packs{display:flex;flex-wrap:wrap;gap:8px}.packs span{border:1px solid #cfe0ff;background:var(--soft);color:#0a4fc2;border-radius:999px;padding:6px 14px;font-weight:700;font-size:13px}
.acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:999px;font-weight:800;font-size:14px;border:1px solid var(--line);background:#fff;color:var(--ink)}
.btn:hover{text-decoration:none;border-color:var(--brand);color:var(--brand)}
.btn.p{background:linear-gradient(135deg,var(--brand),var(--brand2));color:#fff;border:0}.btn.p:hover{color:#fff;filter:brightness(1.05)}
.note{background:var(--bg);border-radius:12px;padding:14px 16px;color:var(--muted)}
.warn{background:#fff4e0;color:#9a5b00;border-radius:12px;padding:12px 16px;font-weight:700;margin-top:12px}
.rel{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.rel a,.lst a{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px;color:var(--ink);font-weight:700;font-size:14px}
.rel a:hover,.lst a:hover{border-color:var(--brand);text-decoration:none}
.rel small,.lst small{display:block;color:var(--muted);font-weight:600;font-size:12px;font-family:ui-monospace,Consolas,monospace}
.lst{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-top:14px}
.subs{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px}
.subs a{display:flex;justify-content:space-between;gap:10px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;color:var(--ink);font-weight:700}
.subs a:hover{border-color:var(--brand);text-decoration:none}.subs b{color:var(--muted);font-variant-numeric:tabular-nums}
.pager{display:flex;gap:8px;flex-wrap:wrap;margin-top:18px;align-items:center}
.pager a,.pager span{padding:8px 14px;border-radius:10px;border:1px solid var(--line);background:#fff;font-weight:700;font-size:14px}.pager span.on{background:var(--brand);color:#fff;border-color:var(--brand)}
footer{background:var(--dark);color:#aab6c8;padding:34px 0;font-size:14px}
.fg{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:24px}footer h3{color:#fff;font-size:15px;margin-bottom:10px}footer a{color:#cfd9e8}
footer ul{list-style:none;display:grid;gap:6px;overflow-wrap:anywhere}
@media(max-width:860px){.pg{grid-template-columns:1fr;padding:18px}.media{grid-template-columns:1fr 1fr}.rel,.subs{grid-template-columns:1fr 1fr}.hn a:not(.lg){display:none}.fg{grid-template-columns:1fr}}
@media(max-width:540px){.rel,.subs,.lst{grid-template-columns:1fr}.media{grid-template-columns:1fr}}
"""
FLASK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"><path d="M9 3h6M10 3v6L4.5 18.5A2 2 0 0 0 6.2 21.5h11.6a2 2 0 0 0 1.7-3L14 9V3"/></svg>'
FAVICON_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#0a6cff"/><path d="M12 6h8M13.5 6v7L8 23a2.5 2.5 0 0 0 2.2 3.7h11.6A2.5 2.5 0 0 0 24 23l-5.5-10V6" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230a6cff'/%3E%3Cpath d='M12 6h8M13.5 6v7L8 23a2.5 2.5 0 0 0 2.2 3.7h11.6A2.5 2.5 0 0 0 24 23l-5.5-10V6' fill='none' stroke='%23fff' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"

def digits(s): return re.sub(r"\D", "", s or "")

def page(lang, title, desc, path, alt_path, body, jsonld=None, crumbs=None, extra_head="", no=None):
    T = L[lang]; o = T["other"]
    bc = ""
    if crumbs:
        bc = '<nav class="bc w" aria-label="breadcrumb">' + '<span>›</span>'.join(
            (f'<a href="{e(u)}">{e(n)}</a>' if u else f'<span style="opacity:1">{e(n)}</span>') for n, u in crumbs) + "</nav>"
        jl = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, **({"item": BASE + u} if u else {})} for i, (n, u) in enumerate(crumbs)]}
        jsonld = (jsonld or []) + [jl]
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    tel = DEALER["phones"][0] if DEALER.get("phones") else ""
    addr = (DEALER.get("address") or {}).get(lang, "")
    return f"""<!DOCTYPE html>
<html lang="{T['html']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{BASE}{path}">
<link rel="alternate" hreflang="{lang}" href="{BASE}{path}">
<link rel="alternate" hreflang="{o}" href="{BASE}{alt_path}">
<link rel="alternate" hreflang="x-default" href="{BASE}{path if lang == 'uz' else alt_path}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{BASE}{path}"><meta property="og:locale" content="{T['og']}"><meta property="og:site_name" content="Weiyel O‘zbekiston">
{extra_head}<meta name="theme-color" content="#0b1626">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/assets/p.css">
{ld}
</head>
<body{f' data-no="{e(no)}"' if no else ''}>
<header><div class="w hb">
  <a class="logo" href="/"><i>{FLASK}</i>Weiyel</a>
  <nav class="hn"><a href="/">{e(T['home'])}</a><a href="/{lang}/k/">{e(T['catalog'])}</a><a href="/#contact">{e(T['contact'])}</a><a class="lg" href="{e(alt_path)}" hreflang="{o}">{o.upper()}</a></nav>
</div></header>
{bc}
<main class="w">
{body}
</main>
<footer><div class="w fg">
  <div><h3>{e(DEALER.get('name',''))}</h3><p>{e(T['dealer'])}. {e(T['cert'])}.</p></div>
  <div><h3>{e(T['contact'])}</h3><ul>{''.join(f'<li><a href="tel:+{digits(x)}">{e(x)}</a></li>' for x in DEALER.get('phones', []))}
    {f'<li>{e(T["wa"])}: <a href="https://wa.me/{digits(DEALER["whatsapp"])}" rel="noopener">{e(DEALER["whatsapp"])}</a></li>' if DEALER.get('whatsapp') else ''}
    {f'<li>{e(T["tg"])}: <a href="https://t.me/{e(DEALER["telegram"])}" rel="noopener">@{e(DEALER["telegram"])}</a></li>' if DEALER.get('telegram') else ''}
    {f'<li><a href="mailto:{e(DEALER["email"])}">{e(DEALER["email"])}</a></li>' if DEALER.get('email') else ''}</ul></div>
  <div><h3>{e(T['catalog'])}</h3><ul>{''.join(f'<li><a href="{url_main(lang, m)}">{e(main_name(m, T))}</a></li>' for m in MAIN if any(main_of(k) == m for k in SUB_ORDER))}</ul>{f'<p style="margin-top:10px">{e(addr)}</p>' if addr else ''}</div>
</div></footer>
{'<script src="/assets/p.js" defer></script>' if no else ''}
</body>
</html>
"""

# shared by every product page (/assets/p.js): applies admin-panel price / hidden / name edits
LIVE_JS = """(function(){var no=document.body.getAttribute('data-no');if(!no||!window.fetch)return;
fetch('%s/rest/v1/sm_products?select=data&catno=eq.'+encodeURIComponent(no),{headers:{apikey:'%s',Authorization:'Bearer %s'}}).then(function(r){return r.ok?r.json():[]}).then(function(a){var d=a&&a[0]&&a[0].data;if(!d)return;
if(d.hidden)document.getElementById('hid').hidden=false;
var pr=document.getElementById('pr');if(d.price){pr.hidden=false;pr.querySelector('i').textContent=d.price;}else pr.hidden=true;
if(d.name)document.querySelector('h1').textContent=d.name;}).catch(function(){});})();
""" % (SB_URL, SB_KEY, SB_KEY)

def product_page(p, lang):
    T = L[lang]; o = T["other"]; det = p["det"] or {}
    m = main_of(p["sub"]); sn = sub_name(p["sub"], T); mn = main_name(m, T)
    name = plain(p["name"])
    cas_ok = bool(re.match(r"^\d+-\d+-\d$", p["cas"] or ""))
    title = f"{name} ({p['no']}){', CAS ' + p['cas'] if cas_ok else ''} — {T['t_suffix']}"
    desc = T["d_tpl"].format(name=name, cas=f" (CAS {p['cas']})" if cas_ok else "",
                             spec=(f"{T['volume']}: {p['spec']}. " if p["spec"] else "")).strip()[:300]
    photo = p["img"] or ""
    mol = f"https://weiyeglobal.oss-accelerate.aliyuncs.com/molecularPng/{p['cas']}.png" if cas_ok else ""
    main_img = photo or mol
    rows = [(k, v) for k, v in (det.get("b") or []) if v and v != "/" and k not in ("number", "Sharing mode")]
    spec = ""
    if rows:
        spec = f'<h2>{e(T["spec_h"])}</h2><table class="sp"><tbody>' + "".join(
            f'<tr><th>{e(T["lbl"].get(k, k))}</th><td>{tv(T, k, v)}</td></tr>' for k, v in rows) + "</tbody></table>"
    if det.get("p"):
        spec += f'<h2>{e(T["packs"])}</h2><div class="packs">' + "".join(f"<span>{e(x)}</span>" for x in det["p"]) + "</div>"
    if det.get("m"):
        spec += (f'<h2>{e(T["comp"])}</h2><div class="tw"><table><thead><tr>' + "".join(f"<th>{e(h)}</th>" for h in T["comp_h"]) +
                 "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{sub_html(r[i] if i < len(r) else '')}</td>" for i in range(4)) + "</tr>" for r in det["m"]) +
                 "</tbody></table></div>")
    if not spec:
        spec = f'<p class="note" style="margin-top:14px">{e(T["nodata"])}</p>'
    sibs = BY_SUB.get(p["sub"], [])
    i = sibs.index(p) if p in sibs else 0
    rel = [x for x in (sibs[i + 1:i + 7] + sibs[max(0, i - 6):i]) if x is not p][:6]
    rel_html = ""
    if rel:
        rel_html = f'<h2 style="margin-top:34px">{e(T["related"])}</h2><div class="rel">' + "".join(
            f'<a href="{url_p(lang, x)}">{e(plain(x["name"]))}<small>{e(x["no"])}</small></a>' for x in rel) + "</div>"
    ask = f'/index.html?add={urllib.request.quote(p["no"])}#contact'
    wa = f'https://wa.me/{digits(DEALER.get("whatsapp",""))}?text=' + urllib.request.quote(f'{T["ask"]}: {p["no"]} — {name}') if DEALER.get("whatsapp") else ""
    body = f"""<article class="card pg" itemscope itemtype="https://schema.org/Product">
  <div class="media">
    <div class="img">{f'<img src="{e(main_img)}" alt="{e(name)}" referrerpolicy="no-referrer" loading="eager" onerror="this.replaceWith(document.createTextNode(\'{e(T["noimg"])}\'))">' if main_img else e(T["noimg"])}</div>
    {f'<div class="mol"><img src="{e(mol)}" alt="" referrerpolicy="no-referrer" loading="lazy" onerror="this.parentNode.remove()">{e(T["mol"])}</div>' if mol and photo else ''}
  </div>
  <div>
    <div class="cat"><a href="{url_main(lang, m)}">{e(mn)}</a> · <a href="{url_sub(lang, p['sub'])}">{e(sn)}</a></div>
    <h1 itemprop="name">{e(name)}</h1>
    <div class="ids"><span><b>{e(T['catno'])}</b><span itemprop="sku" style="all:unset">{e(p['no'])}</span></span>{f'<span><b>CAS</b>{e(p["cas"])}</span>' if p['cas'] else ''}{f'<span><b>{e(T["volume"])}</b>{e(p["spec"])}</span>' if p['spec'] else ''}<span class="pr" id="pr"{'' if p['price'] else ' hidden'}><b>{e(T['price'])}</b><i style="font-style:normal">{e(p['price'])}</i></span></div>
    <meta itemprop="brand" content="Weiyel">
    <div class="warn" id="hid" hidden>{e(T['hidden'])}</div>
    {spec}
    <div class="acts"><a class="btn p" href="{e(ask)}">{e(T['ask'])}</a>{f'<a class="btn" href="{e(wa)}" rel="noopener">WhatsApp</a>' if wa else ''}{f'<a class="btn" href="https://t.me/{e(DEALER["telegram"])}" rel="noopener">Telegram</a>' if DEALER.get('telegram') else ''}</div>
  </div>
</article>
{rel_html}
"""
    ld = {"@context": "https://schema.org", "@type": "Product", "name": name, "sku": p["no"], "mpn": p["no"],
          "brand": {"@type": "Brand", "name": "Weiyel"}, "category": f"{mn} / {sn}", "description": desc,
          "url": BASE + url_p(lang, p)}
    if main_img: ld["image"] = main_img
    if cas_ok: ld["additionalProperty"] = [{"@type": "PropertyValue", "name": "CAS", "value": p["cas"]}]
    crumbs = [(T["home"], "/"), (T["catalog"], f"/{lang}/k/"), (mn, url_main(lang, m)), (sn, url_sub(lang, p["sub"])), (name, None)]
    return page(lang, title, desc, url_p(lang, p), url_p(o, p), body, [ld], crumbs,
                extra_head=f'<meta property="og:image" content="{e(main_img)}">\n' if main_img else "", no=p["no"])

def sub_pages(k, lang):
    T = L[lang]; o = T["other"]; items = BY_SUB[k]; m = main_of(k)
    pages = max(1, (len(items) + PER_PAGE - 1) // PER_PAGE); out = []
    for pg in range(1, pages + 1):
        chunk = items[(pg - 1) * PER_PAGE:pg * PER_PAGE]
        sn, mn = sub_name(k, T), main_name(m, T)
        title = f"{sn} — {T['stds']} Weiyel{(' · ' + T['page'] + ' ' + str(pg)) if pg > 1 else ''} | Weiyel O‘zbekiston"
        desc = f"{sn} ({mn}): {len(items)} {T['products']}. {T['dealer']}. {T['cert']}."
        pager = ""
        if pages > 1:
            pager = '<nav class="pager">' + (f'<a href="{url_sub(lang, k, pg - 1)}">{e(T["prev"])}</a>' if pg > 1 else "") + "".join(
                f'<span class="on">{n}</span>' if n == pg else f'<a href="{url_sub(lang, k, n)}">{n}</a>' for n in range(1, pages + 1)) + (
                f'<a href="{url_sub(lang, k, pg + 1)}">{e(T["next"])}</a>' if pg < pages else "") + "</nav>"
        body = (f'<h1>{e(sn)}</h1><p class="lead">{e(mn)} · {len(items)} {e(T["products"])}. {e(T["cert"])}.</p>'
                f'<div class="lst">' + "".join(f'<a href="{url_p(lang, x)}">{e(plain(x["name"]))}<small>{e(x["no"])}{" · CAS " + e(x["cas"]) if x["cas"] else ""}{" · " + e(x["spec"]) if x["spec"] else ""}</small></a>' for x in chunk) + "</div>" + pager)
        crumbs = [(T["home"], "/"), (T["catalog"], f"/{lang}/k/"), (mn, url_main(lang, m)), (sn, None)]
        out.append((url_sub(lang, k, pg), page(lang, title, desc, url_sub(lang, k, pg), url_sub(o, k, pg), body, None, crumbs)))
    return out

def main_page(m, lang):
    T = L[lang]; o = T["other"]; mn = main_name(m, T)
    subs = [k for k in SUB_ORDER if main_of(k) == m]; total = sum(len(BY_SUB[k]) for k in subs)
    body = (f'<h1>{e(mn)}</h1><p class="lead">{total} {e(T["products"])}. {e(T["dealer"])}. {e(T["cert"])}.</p><div class="subs">' +
            "".join(f'<a href="{url_sub(lang, k)}">{e(sub_name(k, T))}<b>{len(BY_SUB[k])}</b></a>' for k in subs) + "</div>")
    return page(lang, f"{mn} — {T['stds']} Weiyel | Weiyel O‘zbekiston", f"{mn}: {total} {T['products']}. {T['dealer']}.",
                url_main(lang, m), url_main(o, m), body, None, [(T["home"], "/"), (T["catalog"], f"/{lang}/k/"), (mn, None)])

def catalog_root(lang):
    T = L[lang]; o = T["other"]
    mains = [m for m in MAIN if any(main_of(k) == m for k in SUB_ORDER)]
    body = (f'<h1>{e(T["stds"])} Weiyel</h1><p class="lead">{len(PRODUCTS)} {e(T["products"])}. {e(T["dealer"])}.</p><div class="subs">' +
            "".join(f'<a href="{url_main(lang, m)}">{e(main_name(m, T))}<b>{sum(len(BY_SUB[k]) for k in SUB_ORDER if main_of(k) == m)}</b></a>' for m in mains) + "</div>")
    return page(lang, f"{T['catalog']}: {T['stds']} Weiyel | Weiyel O‘zbekiston", f"{len(PRODUCTS)} {T['products']}. {T['dealer']}.",
                f"/{lang}/k/", f"/{o}/k/", body, None, [(T["home"], "/"), (T["catalog"], None)])

# ---------------------------------------------------------------- write
def write(rel, content):
    path = os.path.join(OUT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f: f.write(content)

def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):  # empty it in place (the folder itself may be held open)
        p = os.path.join(OUT, name)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    # existing site
    for name in os.listdir(ROOT):
        if name in ("public", ".git", ".vercel", "build_pages.py", "vercel.json", "__pycache__") or name.startswith("."):
            if name != ".htaccess": continue
        src = os.path.join(ROOT, name)
        (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, os.path.join(OUT, name))
    write("/assets/p.css", CSS)
    write("/assets/p.js", LIVE_JS)
    write("/favicon.svg", FAVICON_SVG)
    urls = {"uz": [], "ru": []}
    for lang in ("uz", "ru"):
        write(f"/{lang}/k/index.html", catalog_root(lang)); urls[lang].append((f"/{lang}/k/", "0.6"))
        for m in MAIN:
            if any(main_of(k) == m for k in SUB_ORDER):
                write(url_main(lang, m), main_page(m, lang)); urls[lang].append((url_main(lang, m), "0.6"))
        for k in SUB_ORDER:
            for u, h in sub_pages(k, lang):
                write(u, h); urls[lang].append((u, "0.5"))
        for p in PRODUCTS:
            u = url_p(lang, p); write(u, product_page(p, lang)); urls[lang].append((u, "0.8"))
    # sitemaps
    for lang in ("uz", "ru"):
        o = L[lang]["other"]
        body = "".join(
            f'<url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority>'
            f'<xhtml:link rel="alternate" hreflang="{lang}" href="{BASE}{u}"/><xhtml:link rel="alternate" hreflang="{o}" href="{BASE}{u.replace("/" + lang + "/", "/" + o + "/", 1)}"/></url>'
            for u, pr in urls[lang])
        write(f"/sitemap-{lang}.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
              f'<url><loc>{BASE}/</loc><lastmod>{TODAY}</lastmod><priority>1.0</priority></url>' + body + "</urlset>\n")
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
          "".join(f"<sitemap><loc>{BASE}/sitemap-{l}.xml</loc><lastmod>{TODAY}</lastmod></sitemap>" for l in ("uz", "ru")) + "</sitemapindex>\n")
    write("/robots.txt", f"User-agent: *\nAllow: /\nDisallow: /admin.html\n\nSitemap: {BASE}/sitemap.xml\n")
    n = sum(len(v) for v in urls.values())
    print(f"base={BASE} products={len(PRODUCTS)} overrides={len(OVR)} pages={n} subs={len(SUB_ORDER)}")

if __name__ == "__main__":
    main()
