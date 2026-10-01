/* STANDART VA METROLOGIYA — sayt ma'lumotlari.
   Sayt (index.html) va admin panel (admin.html) shu fayldan foydalanadi. */

/* Supabase ulanishi (publishable kalit — ochiq bo'lishi mumkin, himoya RLS qoidalarida) */
window.SB = {
  url: "https://fwuqtrfoenejodufnwyb.supabase.co",
  key: "sb_publishable_5nsgpaWXtJYY1gNY7jzDCA_KRJclQjr"
};

/* ---------- DILER MA'LUMOTLARI (standart qiymatlar) ----------
   Admin panelda saqlangan qiymatlar shularning ustidan yoziladi. */
window.DEALER = {
  name:  "STANDART VA METROLOGIYA MCHJ",
  phones: ["+998 90 939-71-83", "+998 98 361-71-83"],
  whatsapp: "+998 33 078-98-89",
  telegram: "standartgsouz",        // t.me/ dan keyingi qism
  email: "standartvametrologiya@gmail.com",
  instagram: "",                    // masalan: "https://instagram.com/sahifa_nomi"
  facebook: "",                     // masalan: "https://facebook.com/sahifa_nomi"
  address: {
    uz:"Toshkent sh., Yakkasaroy tumani, Yakkasaroy ko‘chasi, 5-uy, 12-xona",
    ru:"г. Ташкент, Яккасарайский район, ул. Яккасарай, дом 5, офис 12"
  }
};

window.T = {
uz:{
  title:"Weiyel — Sertifikatlangan standart namunalar",
  nav_home:"Bosh sahifa",nav_catalog:"Katalog",nav_bio:"Biologik nazorat",nav_about:"Biz haqimizda",nav_contact:"Aloqa",
  hero_badge:"Weiyel’ning O‘zbekistondagi yagona rasmiy dileri",
  dl_eyebrow:"Rasmiy diler",dl_title:"Weiyel’ning O‘zbekistondagi yagona rasmiy dileri",
  dl_text:"Biz Weiyel kompaniyasi bilan rasmiy dilerlik shartnomasiga va dilerlik sertifikatiga egamiz. Siz original mahsulotni to‘g‘ridan-to‘g‘ri va kafolat bilan olasiz — chet elga murojaat qilish shart emas.",
  dl_ribbon:"Rasmiy diler",dl_cert:"DILERLIK SERTIFIKATI",dl_cert_sub:"O‘zbekiston Respublikasi",dl_footer:"Weiyel’ning O‘zbekistondagi rasmiy dileri",
  dl:[["shield","Original mahsulot","Faqat ishlab chiqaruvchidan, sertifikati bilan."],["chat","O‘zbek va rus tilida","Mahalliy menejer savollaringizga tez javob beradi."],["box","Shartnoma va hujjatlar","Rasmiy shartnoma va barcha kerakli hujjatlar."],["plane","Bojxona bizdan","Olib kelish va rasmiylashtirishni o‘zimiz hal qilamiz."]],
  c_phone_l:"Telefon",c_addr_l:"Manzil",nav_dealer:"Rasmiy diler",nav_products:"Mahsulotlar",
  pc_eyebrow:"Katalog",pc_title:"Mahsulotlar katalogi",pc_back:"Orqaga",pc_home:"Bosh sahifa",pc_cart:"So‘rovga o‘tish",pc_sub:"Nomi, katalog raqami yoki CAS raqami bo‘yicha qidiring. Keraklilarini “So‘rovga qo‘shish” tugmasi bilan tanlang.",pc_search:"Qidiruv",pc_ph:"Masalan: Vitamin B2, BWJ4322 yoki 83-88-5",pc_all:"Barcha yo‘nalishlar",pc_allsub:"Barcha bo‘limlar",pc_found:"Topildi:",pc_reset:"Filtrni tozalash",pc_more:"Yana ko‘rsatish",pc_loading:"Katalog yuklanmoqda…",pc_order:"Bu yo‘nalish mahsulotlari buyurtma asosida yetkaziladi. Kerakli namunani yozib yuboring — narx va muddatini aytamiz.",pc_none:"Hech narsa topilmadi. Boshqa so‘z bilan qidirib ko‘ring yoki bizga yozing — topib beramiz.",pc_err:"Katalogni yuklab bo‘lmadi. Sahifani yangilang.",pc_h:["Katalog №","Nomi","CAS","Hajmi",""],pc_add:"So‘rovga qo‘shish",pc_added:"✓ Qo‘shildi",pc_msg:"Quyidagi mahsulotlar kerak:",pc_details:"Batafsil",pd_spec:"Texnik xususiyatlari",pd_packs:"Qadoq hajmi",pd_comp:"Tarkibi va attestatsiya qiymatlari",pd_comp_h:["Modda","Attestatsiya qiymati","Noaniqlik (k=2)","CAS"],pd_mol:"Molekula tuzilishi",pd_noimg:"Rasm mavjud emas",pd_nodata:"Bu mahsulot bo‘yicha batafsil ma’lumot va sertifikatni so‘rov orqali yuboramiz.",pd_ask:"Narx so‘rash",pd_close:"Yopish",pd_catno:"Katalog №",pd_price:"Narxi",pd_page:"Alohida sahifada ochish ↗",lbl:{"Form":"Shakli","Term of validit":"Yaroqlilik muddati","Term of validity":"Yaroqlilik muddati","Molecular Formula":"Molekulyar formula","Stroma":"Matritsa","Packing":"Qadoq","Save conditions":"Saqlash sharoiti","Storage conditions":"Saqlash sharoiti","Concentration":"Konsentratsiya","Solvent":"Erituvchi","Purity":"Tozaligi","Subculture":"Ozuqa muhiti","Subculturing":"Qo‘llash tartibi","Growth conditions":"O‘stirish sharoiti","Safety level":"Xavfsizlik darajasi","Application":"Qo‘llanilishi","Transportation conditions":"Tashish sharoiti","Specification":"Hajmi","Traceability":"Kuzatiluvchanlik","Usage":"Foydalanish","Remark":"Izoh","Remarks":"Izoh"},
  hero_t1:"Laboratoriyangiz uchun",hero_t2:"ishonchli standart namunalar",
  hero_lead:"12 900 dan ortiq sertifikatlangan standart namunalar (CRM): oziq-ovqat, ekologiya, metallar, kimyo, dori vositalari va boshqa sohalar uchun. Xalqaro standartlarga to‘liq muvofiq.",
  hero_btn1:"Katalogni ko‘rish",hero_btn2:"Narx so‘rash",
  mini1:"Ishlab chiqaruvchi",mini2:"Sifat tizimi",mini3:"Akkreditatsiya",mini4:"Akkreditatsiya",
  st1:"standart namunalar",st2:"mamlakatga yetkazamiz",st3:"mahsulot omborda tayyor",st4:"yillik tajriba",
  cat_eyebrow:"Katalog",cat_title:"Mahsulot yo‘nalishlari",cat_sub:"Kerakli yo‘nalishni tanlang — biz sizga mos namunani topib beramiz.",
  more:"Batafsil",
  cats:[
    ["food","#f08a24","Oziq-ovqat","Fizik-kimyoviy ko‘rsatkichlar, pestitsid va veterinariya dori qoldiqlari, toksinlar, qo‘shimchalar."],
    ["env","#1aa56b","Ekologiya","Suv sifati, havo ifloslantiruvchilari, metallar, organik birikmalar, gaz standartlari."],
    ["metal","#6b7a90","Po‘lat va rangli metallar","Oddiy, nodir, yengil, og‘ir, qimmatbaho va noyob yer metallari, qotishmalar."],
    ["chem","#7c4dff","Kimyoviy mahsulotlar","Organik va noorganik standartlar, reagentlar, tabiiy va dorivor xomashyo."],
    ["mineral","#b5651d","Minerallar, ko‘mir, neft","Tuproq, tog‘ jinslari, qurilish materiallari, cho‘kindilar, neft mahsulotlari."],
    ["drug","#e0457b","Klinik dori vositalari","Farmakopeya standartlari, klinik materiallar, diagnostika reagentlari."],
    ["industry","#0a6cff","Sanoat va iste’mol mollari","To‘qimachilik, kosmetika, elektr mahsulotlari, asbob sarf materiallari."],
    ["physics","#00a3b4","Fizik-texnik xossalar","Zarracha o‘lchami, pH, qovushqoqlik, issiqlik va boshqa fizik standartlar."]
  ],
  bio_eyebrow:"Yangi yo‘nalish",bio_title:"Biologik sifat nazorati",
  bio_text:"Klinik va tadqiqot laboratoriyalari uchun nuklein kislota, oqsil va immunologik nazorat materiallari. Natijalaringiz aniq va takrorlanuvchan bo‘lishi uchun.",
  bio_btn:"Maslahat olish",
  bio:["Nuklein kislota namunalari (zamburug‘lar, viruslar)","Nuklein kislota standartlari","Oqsil sifat nazorati","Immunologiya mahsulotlari","Suyuq ichki sifat nazorati"],
  why_eyebrow:"Nega biz",why_title:"Weiyel — ishonchli hamkoringiz",why_sub:"Oddiy, tez va kafolatli. Biz bilan ishlash qulay.",
  why:[
    ["box","Omborda mavjud","Dunyo bo‘ylab omborlarimizda mahsulotlarning 90% dan ortig‘i doim tayyor."],
    ["shield","Sifat kafolati","Har bir standart namuna sertifikat bilan birga yetkaziladi."],
    ["plane","Global logistika","FedEx va SF Express bilan hamkorlik — 50+ mamlakatga xavfsiz yetkazish."],
    ["chat","Tezkor xizmat","Navbatsiz, bir necha soniyada javob beruvchi shaxsiy menejer."]
  ],
  steps_eyebrow:"Qanday ishlaymiz",steps_title:"Buyurtma — 4 oddiy qadam",
  steps:[["So‘rov yuboring","Kerakli namunani yozing yoki WhatsApp orqali murojaat qiling."],["Taklif oling","Narx, mavjudlik va muddat bo‘yicha tez javob beramiz."],["Tasdiqlang","Buyurtmani tasdiqlang — hujjatlarni tayyorlaymiz."],["Qabul qiling","Sertifikat bilan birga eshigingizgacha yetkazamiz."]],
  about_eyebrow:"Biz haqimizda",about_title:"20 yillik tajribaga ega yetkazib beruvchi",
  about_p1:"Weiyel — sertifikatlangan standart namunalarni ishlab chiqaruvchi va yetkazib beruvchi kompaniya. Biz butun dunyodagi laboratoriyalar va sinov markazlariga xizmat ko‘rsatamiz.",
  about_p2:"Mahsulotlarimiz xalqaro standartlarga kuzatiluvchan (traceability) va nufuzli akkreditatsiyalarga ega.",
  checks:["ISO 17034:2016 va ISO 9001:2015 sertifikatlari","ANAB va CNAS akkreditatsiyasi","Xalqaro standartlarga kuzatiluvchanlik","50+ mamlakatda mijozlar"],
  about_btn:"Biz bilan bog‘laning",orbit2:"50+ mamlakat",years:"yillik tajriba",
  faq_title:"Ko‘p beriladigan savollar",
  faq:[
    ["Standart namuna (CRM) nima?","Bu tarkibi yoki xossalari aniq o‘lchangan va sertifikat bilan tasdiqlangan material. Laboratoriyalar undan asboblarni kalibrlash va natijalarni tekshirish uchun foydalanadi."],
    ["Yetkazib berish qancha vaqt oladi?","Mahsulotlarning ko‘pchiligi omborda mavjud, shuning uchun yetkazish odatda tez amalga oshiriladi. Aniq muddatni so‘rovingizga javob sifatida aytamiz."],
    ["Sertifikat beriladimi?","Ha, har bir namuna bilan birga uning sertifikati (analiz sertifikati) beriladi."],
    ["Siz haqiqatan rasmiy dilermisiz?","Ha. Bizda Weiyel bilan tuzilgan dilerlik shartnomasi va dilerlik sertifikati bor. So‘rasangiz, nusxasini ko‘rsatamiz."],
    ["Qanday bog‘lansam bo‘ladi?","Telefon, Telegram, WhatsApp yoki ushbu sahifadagi forma orqali — qaysi biri qulay bo‘lsa."]
  ],
  c_title:"Narx so‘rash",c_sub:"Kerakli namunani yozing — O‘zbekistondagi menejerimiz tez orada javob beradi.",
  c_hours_l:"Ish vaqti",c_hours:"Du–Sh, 09:00–18:00",
  f_name:"Ismingiz",f_company:"Kompaniya",f_phone:"Telefon",f_cat:"Yo‘nalish",f_msg:"Xabar (namuna nomi, miqdori)",f_send:"Yuborish",
  f_ok:"Rahmat! So‘rovingiz qabul qilindi. Tez orada siz bilan bog‘lanamiz.",f_err:"Xabar yuborilmadi. Iltimos, telefon yoki Telegram orqali bog‘laning.",
  f_about:"Weiyel’ning O‘zbekistondagi yagona rasmiy dileri. Laboratoriyalar va sinov markazlari uchun sertifikatlangan standart namunalar.",
  ft_cat:"Yo‘nalishlar",ft_links:"Sahifalar",rights:"Barcha huquqlar himoyalangan.",
  certs:["Sertifikatlangan namunalar","Omborda mavjud","Tez yetkazish","Sifat sertifikati"]
},
ru:{
  title:"Weiyel — Сертифицированные стандартные образцы",
  nav_home:"Главная",nav_catalog:"Каталог",nav_bio:"Биоконтроль",nav_about:"О нас",nav_contact:"Контакты",
  hero_badge:"Единственный официальный дилер Weiyel в Узбекистане",
  dl_eyebrow:"Официальный дилер",dl_title:"Единственный официальный дилер Weiyel в Узбекистане",
  dl_text:"У нас есть официальный дилерский договор и дилерский сертификат компании Weiyel. Вы получаете оригинальную продукцию напрямую и с гарантией — без обращения за рубеж.",
  dl_ribbon:"Официальный дилер",dl_cert:"ДИЛЕРСКИЙ СЕРТИФИКАТ",dl_cert_sub:"Республика Узбекистан",dl_footer:"официальный дилер Weiyel в Узбекистане",
  dl:[["shield","Оригинальная продукция","Только от производителя, с сертификатом."],["chat","На узбекском и русском","Местный менеджер быстро ответит на ваши вопросы."],["box","Договор и документы","Официальный договор и все необходимые документы."],["plane","Таможня — на нас","Доставку и оформление берём на себя."]],
  c_phone_l:"Телефон",c_addr_l:"Адрес",nav_dealer:"Официальный дилер",nav_products:"Продукция",
  pc_eyebrow:"Каталог",pc_title:"Каталог продукции",pc_back:"Назад",pc_home:"Главная",pc_cart:"Перейти к запросу",pc_sub:"Ищите по названию, каталожному номеру или номеру CAS. Нужные позиции отметьте кнопкой «В запрос».",pc_search:"Поиск",pc_ph:"Например: Vitamin B2, BWJ4322 или 83-88-5",pc_all:"Все направления",pc_allsub:"Все разделы",pc_found:"Найдено:",pc_reset:"Сбросить фильтр",pc_more:"Показать ещё",pc_loading:"Загрузка каталога…",pc_order:"Продукция этого направления поставляется под заказ. Напишите, какой образец нужен — сообщим цену и срок.",pc_none:"Ничего не найдено. Попробуйте другой запрос или напишите нам — мы найдём.",pc_err:"Не удалось загрузить каталог. Обновите страницу.",pc_h:["Кат. №","Название","CAS","Фасовка",""],pc_add:"В запрос",pc_added:"✓ Добавлено",pc_msg:"Нужны следующие позиции:",pc_details:"Подробнее",pd_spec:"Технические характеристики",pd_packs:"Фасовка",pd_comp:"Состав и аттестованные значения",pd_comp_h:["Компонент","Аттестованное значение","Неопределённость (k=2)","CAS"],pd_mol:"Структура молекулы",pd_noimg:"Нет изображения",pd_nodata:"Подробные характеристики и сертификат на этот образец отправим по запросу.",pd_ask:"Запросить цену",pd_close:"Закрыть",pd_catno:"Кат. №",pd_price:"Цена",pd_page:"Открыть страницу товара ↗",lbl:{"Form":"Форма","Term of validit":"Срок годности","Term of validity":"Срок годности","Molecular Formula":"Молекулярная формула","Stroma":"Матрица","Packing":"Упаковка","Save conditions":"Условия хранения","Storage conditions":"Условия хранения","Concentration":"Концентрация","Solvent":"Растворитель","Purity":"Чистота","Subculture":"Питательная среда","Subculturing":"Порядок применения","Growth conditions":"Условия культивирования","Safety level":"Уровень биобезопасности","Application":"Применение","Transportation conditions":"Условия транспортировки","Specification":"Фасовка","Traceability":"Прослеживаемость","Usage":"Применение","Remark":"Примечание","Remarks":"Примечание"},
  hero_t1:"Для вашей лаборатории —",hero_t2:"надёжные стандартные образцы",
  hero_lead:"Более 12 900 сертифицированных стандартных образцов (CRM) для пищевой промышленности, экологии, металлургии, химии, фармацевтики и других отраслей. Полное соответствие международным стандартам.",
  hero_btn1:"Смотреть каталог",hero_btn2:"Запросить цену",
  mini1:"Производитель",mini2:"Система качества",mini3:"Аккредитация",mini4:"Аккредитация",
  st1:"стандартных образцов",st2:"стран доставки",st3:"товаров в наличии",st4:"лет опыта",
  cat_eyebrow:"Каталог",cat_title:"Направления продукции",cat_sub:"Выберите нужное направление — мы подберём подходящий образец.",
  more:"Подробнее",
  cats:[
    ["food","#f08a24","Пищевые продукты","Физико-химические показатели, остатки пестицидов и ветпрепаратов, токсины, добавки."],
    ["env","#1aa56b","Экология","Качество воды, загрязнители воздуха, металлы, органические соединения, газовые смеси."],
    ["metal","#6b7a90","Сталь и цветные металлы","Обычные, редкие, лёгкие, тяжёлые, драгоценные и редкоземельные металлы, сплавы."],
    ["chem","#7c4dff","Химическая продукция","Органические и неорганические стандарты, реактивы, натуральное и лекарственное сырьё."],
    ["mineral","#b5651d","Минералы, уголь, нефть","Почвы, горные породы, стройматериалы, донные отложения, нефтепродукты."],
    ["drug","#e0457b","Клинические препараты","Фармакопейные стандарты, клинические материалы, диагностические реагенты."],
    ["industry","#0a6cff","Промышленные товары","Текстиль, косметика, электротовары, расходные материалы для приборов."],
    ["physics","#00a3b4","Физико-технические свойства","Размер частиц, pH, вязкость, теплофизические и другие стандарты."]
  ],
  bio_eyebrow:"Новое направление",bio_title:"Биологический контроль качества",
  bio_text:"Материалы для контроля нуклеиновых кислот, белков и иммунологических исследований для клинических и научных лабораторий. Чтобы ваши результаты были точными и воспроизводимыми.",
  bio_btn:"Получить консультацию",
  bio:["Образцы нуклеиновых кислот (грибы, вирусы)","Стандарты нуклеиновых кислот","Контроль качества белков","Продукция для иммунологии","Жидкий внутрилабораторный контроль"],
  why_eyebrow:"Почему мы",why_title:"Weiyel — ваш надёжный партнёр",why_sub:"Просто, быстро и с гарантией. С нами удобно работать.",
  why:[
    ["box","Всё в наличии","Более 90% продукции всегда есть на наших складах по всему миру."],
    ["shield","Гарантия качества","Каждый стандартный образец поставляется с сертификатом."],
    ["plane","Мировая логистика","Партнёрство с FedEx и SF Express — надёжная доставка в 50+ стран."],
    ["chat","Быстрый сервис","Персональный менеджер отвечает за секунды, без очереди."]
  ],
  steps_eyebrow:"Как мы работаем",steps_title:"Заказ — 4 простых шага",
  steps:[["Отправьте запрос","Напишите, какой образец нужен, или свяжитесь через WhatsApp."],["Получите предложение","Быстро сообщим цену, наличие и сроки."],["Подтвердите","Подтвердите заказ — мы подготовим документы."],["Получите заказ","Доставим до двери вместе с сертификатом."]],
  about_eyebrow:"О нас",about_title:"Поставщик с 20-летним опытом",
  about_p1:"Weiyel — производитель и поставщик сертифицированных стандартных образцов. Мы обслуживаем лаборатории и испытательные центры по всему миру.",
  about_p2:"Наша продукция прослеживаема к международным эталонам и имеет авторитетные аккредитации.",
  checks:["Сертификаты ISO 17034:2016 и ISO 9001:2015","Аккредитация ANAB и CNAS","Прослеживаемость к международным стандартам","Клиенты в 50+ странах"],
  about_btn:"Связаться с нами",orbit2:"50+ стран",years:"лет опыта",
  faq_title:"Частые вопросы",
  faq:[
    ["Что такое стандартный образец (CRM)?","Это материал с точно измеренным составом или свойствами, подтверждёнными сертификатом. Лаборатории используют его для калибровки приборов и проверки результатов."],
    ["Сколько времени занимает доставка?","Большинство товаров есть на складе, поэтому доставка обычно быстрая. Точный срок сообщим в ответ на ваш запрос."],
    ["Предоставляется ли сертификат?","Да, каждый образец поставляется вместе с сертификатом анализа."],
    ["Вы действительно официальный дилер?","Да. У нас есть дилерский договор с Weiyel и дилерский сертификат. По запросу покажем копию."],
    ["Как с вами связаться?","По телефону, в Telegram, WhatsApp или через форму на этой странице — как вам удобнее."]
  ],
  c_title:"Запросить цену",c_sub:"Напишите, какой образец вам нужен — наш менеджер в Узбекистане скоро ответит.",
  c_hours_l:"Время работы",c_hours:"Пн–Сб, 09:00–18:00",
  f_name:"Ваше имя",f_company:"Компания",f_phone:"Телефон",f_cat:"Направление",f_msg:"Сообщение (название образца, количество)",f_send:"Отправить",
  f_ok:"Спасибо! Ваш запрос принят. Мы скоро свяжемся с вами.",f_err:"Не удалось отправить. Пожалуйста, позвоните или напишите в Telegram.",
  f_about:"Единственный официальный дилер Weiyel в Узбекистане. Сертифицированные стандартные образцы для лабораторий и испытательных центров.",
  ft_cat:"Направления",ft_links:"Разделы",rights:"Все права защищены.",
  certs:["Сертифицированные образцы","В наличии на складе","Быстрая доставка","Сертификат качества"]
}};
