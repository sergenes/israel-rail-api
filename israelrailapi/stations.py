#!/usr/bin/env python
# -*- coding: utf-8 -*-

STATIONS = {'3700': {'Heb': 'תל אביב - סבידור מרכז', 'Eng': 'Tel Aviv-Savidor Center', 'Rus': 'Тель-Авив - Мерказ - Центральная', 'Arb': 'تل ابيب – ساڤيدور المركز'}, '3500': {'Heb': 'הרצליה', 'Eng': 'Hertsliya', 'Rus': 'Герцлия', 'Arb': 'هرتسليا'}, '3400': {'Heb': 'בית יהושע', 'Eng': "Bet Yehoshu'a", 'Rus': 'Бейт-Иегошуа ', 'Arb': 'بيت يهوشوع'}, '3300': {'Heb': 'נתניה', 'Eng': 'Netanya', 'Rus': 'Нетания', 'Arb': 'نتانيا'}, '3100': {'Heb': 'חדרה - מערב', 'Eng': 'Hadera-West', 'Rus': 'Хадера - Маарав', 'Arb': 'الخضيرة - غرب  '}, '2800': {'Heb': 'בנימינה', 'Eng': 'Binyamina', 'Rus': 'Биньямина', 'Arb': 'بنيامينا'}, '2820': {'Heb': 'קיסריה - פרדס חנה', 'Eng': 'Caesarea-Pardes Hana', 'Rus': 'Кейсария - Пардес-Хана', 'Arb': 'قيساريا - بارديس حنا'}, '2500': {'Heb': 'עתלית', 'Eng': 'Atlit', 'Rus': 'Атлит', 'Arb': 'عتليت'}, '2200': {'Heb': 'חיפה - בת גלים', 'Eng': 'Haifa-Bat Galim', 'Rus': 'Хайфа - Бат-Галим', 'Arb': 'حيفا - بات چاليم'}, '1300': {'Heb': 'חוצות המפרץ', 'Eng': 'Hutsot HaMifrats', 'Rus': 'Хоцот ха-Мифрац ', 'Arb': 'حوتسوت همفراتس'}, '700': {'Heb': 'קריית חיים', 'Eng': 'Kiryat Hayim', 'Rus': 'Кирьят-Хаим', 'Arb': 'كريات حاييم'}, '1400': {'Heb': 'קריית מוצקין', 'Eng': 'Kiryat Motzkin', 'Rus': 'Кирьят-Моцкин', 'Arb': 'كريات موتسكين'}, '1500': {'Heb': 'עכו', 'Eng': 'Ako', 'Rus': 'Акко ', 'Arb': 'عكا'}, '2300': {'Heb': "חיפה - חוף הכרמל (ש' רזיאל)", 'Eng': 'Haifa-Hof HaKarmel (Razi`el)', 'Rus': 'Хайфа Хоф ха-Кармель', 'Arb': 'حيفا - شاطئ الكرمل'}, '8700': {'Heb': "כפר סבא - נורדאו (א' קוסטיוק)", 'Eng': 'Kfar Sava-Nordau (A.Kostyuk)', 'Rus': 'Кфар-Саба – Нордау (А. Костюк)', 'Arb': 'كفار سابا - نورداو'}, '1600': {'Heb': 'נהריה', 'Eng': 'Nahariya', 'Rus': 'Нагария', 'Arb': 'نهاريا'}, '6500': {'Heb': 'ירושלים - גן החיות התנכי', 'Eng': 'Jerusalem-Biblical Zoo', 'Rus': 'Иерусалим – зоопарк', 'Arb': 'القدس - حديقة الحيوان التوراتية'}, '6300': {'Heb': 'בית שמש', 'Eng': 'Bet Shemesh', 'Rus': 'Бейт Шемеш', 'Arb': 'بيت شيمش'}, '7000': {'Heb': 'קריית גת', 'Eng': 'Kiryat Gat', 'Rus': 'Кирьят-Гат ', 'Arb': 'كريات چات'}, '5000': {'Heb': 'לוד', 'Eng': 'Lod', 'Rus': 'Лод', 'Arb': 'اللد'}, '7300': {'Heb': 'באר שבע- צפון/אוניברסיטה', 'Eng': "Be'er Sheva-North/University", 'Rus': 'Беер-Шева Цафон', 'Arb': 'بئر السبع - شمال/الجامعة'}, '4800': {'Heb': 'כפר חב"ד', 'Eng': 'Kfar Habad', 'Rus': 'Кфар ХАБАД', 'Arb': 'كفار حباد'}, '4600': {'Heb': 'תל אביב - השלום', 'Eng': 'Tel Aviv-HaShalom', 'Rus': 'Тель-Авив - ха-Шалом', 'Arb': 'تل أبيب - السلام'}, '2100': {'Heb': 'חיפה- מרכז השמונה', 'Eng': 'Haifa Center-HaShmona', 'Rus': 'Хайфа - Мерказ - Центральная', 'Arb': 'حيفا المركز - هشمونا'}, '5010': {'Heb': 'רמלה', 'Eng': 'Ramla', 'Rus': 'Рамле', 'Arb': 'الرملة'}, '8800': {'Heb': 'ראש העין - צפון', 'Eng': "Rosh Ha'Ayin-North", 'Rus': 'Рош ха-Айн Цафон', 'Arb': 'روش هعاين - شمال'}, '5300': {'Heb': 'באר יעקב', 'Eng': "Be'er Ya'akov", 'Rus': 'Беер-Яаков', 'Arb': 'بئير يعكوف'}, '5200': {'Heb': "רחובות (א' הדר) ", 'Eng': 'Rehovot (E. Hadar)', 'Rus': 'Реховот- им. А. Хадара', 'Arb': 'رحوڤوت'}, '5410': {'Heb': 'יבנה מזרח', 'Eng': 'Yavne-East', 'Rus': 'Явне-Восток', 'Arb': 'ياڤنه - شرق'}, '9100': {'Heb': 'ראשון לציון - הראשונים', 'Eng': 'Rishon LeTsiyon-HaRishonim', 'Rus': 'Ришон ле-Цион - Ха-Ришоним ', 'Arb': 'ريشون لتسيون - هريشونيم'}, '5800': {'Heb': "אשדוד עד הלום (מ' בר כוכבא)", 'Eng': 'Ashdod-Ad Halom (M.Bar Kochva)', 'Rus': 'Ашдод-ад-Халом (М. Бар Кохва)', 'Arb': 'أشدود - عاد هلوم'}, '4250': {'Heb': 'פתח תקווה - סגולה', 'Eng': 'Petah Tikva-Segula', 'Rus': 'Петах-Тиква - Сгула', 'Arb': 'بيتح تكڤا - سچوله'}, '4100': {'Heb': 'בני ברק', 'Eng': 'Bnei Brak', 'Rus': 'Бней-Брак', 'Arb': 'بني براك'}, '3600': {'Heb': 'תל אביב - אוניברסיטה', 'Eng': 'Tel Aviv-University', 'Rus': 'Тель-Авив - Университет', 'Arb': 'تل أبيب - الجامعة'}, '7320': {'Heb': 'באר שבע - מרכז', 'Eng': "Be'er Sheva-Center", 'Rus': 'Беер-Шева Мерказ', 'Arb': 'بئر السبع - المركز'}, '1220': {'Heb': 'מרכזית המפרץ (לב המפרץ)', 'Eng': 'HaMifrats Central Station', 'Rus': 'Центральная станция Ха-Мифрац', 'Arb': 'همفراتس المركزية'}, '4900': {'Heb': 'תל אביב - ההגנה', 'Eng': 'Tel Aviv-HaHagana', 'Rus': 'Тель-Авив - ха-Хагана ', 'Arb': 'تل أبيب - ههچناه'}, '8600': {'Heb': 'נמל תעופה בן גוריון', 'Eng': 'Ben Gurion Airport', 'Rus': 'Бен-Гурион Аэропорт', 'Arb': 'مطار بن چوريون'}, '6700': {'Heb': 'ירושלים - מלחה', 'Eng': 'Jerusalem-Malha', 'Rus': 'Иерусалим - Малха', 'Arb': 'القدس - المالحه'}, '5900': {'Heb': 'אשקלון', 'Eng': 'Ashkelon', 'Rus': 'Ашкелон ', 'Arb': 'أشكلون'}, '7500': {'Heb': 'דימונה', 'Eng': 'Dimona', 'Rus': 'Димона', 'Arb': 'ديمونا'}, '9200': {'Heb': 'הוד השרון - סוקולוב', 'Eng': 'Hod HaSharon-Sokolov', 'Rus': 'Ход Хашарон - Соколов', 'Arb': 'هود هشارون - سوكولوڤ'}, '4170': {'Heb': 'פתח תקווה  - קריית אריה', 'Eng': 'Petah Tikva-Kiryat Arye', 'Rus': 'Петах Тиква – Кирьят Арье', 'Arb': 'بيتح تكڤا - كريات أريه'}, '5150': {'Heb': 'לוד גני אביב', 'Eng': 'Lod-Gane Aviv', 'Rus': 'Лод - Ганей Авив', 'Arb': 'اللد - چاني أڤيڤ'}, '8550': {'Heb': 'להבים - רהט', 'Eng': 'Lehavim-Rahat', 'Rus': 'Леавим - Рахат', 'Arb': 'لهاڤيم - رهط'}, '300': {'Heb': 'פאתי מודיעין', 'Eng': "Pa'ate Modi'in", 'Rus': 'Патей Модиин', 'Arb': 'بأتي موديعين'}, '400': {'Heb': 'מודיעין - מרכז', 'Eng': "Modi'in-Center", 'Rus': 'Модиин центр ', 'Arb': 'موديعين - المركز'}, '4640': {'Heb': 'צומת חולון', 'Eng': 'Holon Junction', 'Rus': 'Холон - Развязка Холон', 'Arb': 'مفترق حولون'}, '4660': {'Heb': 'חולון - וולפסון', 'Eng': 'Holon-Wolfson', 'Rus': 'Холон - Вольфсон', 'Arb': 'حولون - ڤولفسون'}, '4680': {'Heb': 'בת ים - יוספטל', 'Eng': 'Bat Yam-Yoseftal', 'Rus': 'Бат Ям - Йосеф Таль', 'Arb': 'بات يام - يوسفطال'}, '4690': {'Heb': 'בת ים - קוממיות', 'Eng': 'Bat Yam-Komemiyut', 'Rus': 'Бат Ям - Комемуют', 'Arb': 'بات يام - كوميميوت'}, '9800': {'Heb': 'ראשון לציון-משה דיין', 'Eng': 'Rishon LeTsiyon-Moshe Dayan', 'Rus': 'Ришон-Ле-Цион станция им. Моше Даяна', 'Arb': 'ريشون لتسيون -موشي ديان'}, '9000': {'Heb': 'יבנה מערב', 'Eng': 'Yavne-West', 'Rus': 'Явне-Запад', 'Arb': 'ياڤني - غرب'}, '9600': {'Heb': 'שדרות', 'Eng': 'Sderot', 'Rus': 'Сдерот', 'Arb': 'سديروت'}, '9650': {'Heb': 'נתיבות', 'Eng': 'Netivot', 'Rus': 'Нетивот', 'Arb': 'نتيفوت'}, '9700': {'Heb': 'אופקים', 'Eng': 'Ofakim', 'Rus': 'Офаким', 'Arb': 'أوفاكيم'}, '3310': {'Heb': 'נתניה - ספיר', 'Eng': 'Netanya-Sapir', 'Rus': 'Нетания – Сапир', 'Arb': 'نتانيا - سبير'}, '1240': {'Heb': 'יקנעם - כפר יהושע', 'Eng': "Yokne'am-Kfar Yehoshu'a", 'Rus': 'Йокнеам – Кфар-Иегошуа', 'Arb': 'يوكنعام – كفار يهوشوع'}, '1250': {'Heb': 'מגדל העמק - כפר ברוך', 'Eng': "Migdal Ha'emek-Kfar Barukh", 'Rus': 'Мигдаль-Ха-Эмек – Кфар Барух', 'Arb': 'مجدال هعيمك – كفار باروخ'}, '1260': {'Heb': 'עפולה ר.איתן', 'Eng': 'Afula R.Eitan', 'Rus': 'Афула Р. Эйтан', 'Arb': 'العفولة  ر. ايتان'}, '1280': {'Heb': 'בית שאן', 'Eng': "Beit She'an", 'Rus': 'Бейт Шеан', 'Arb': 'بيت شآن'}, '1820': {'Heb': 'אחיהוד', 'Eng': 'Ahihud', 'Rus': 'Ахихуд', 'Arb': 'احيهود'}, '1840': {'Heb': 'כרמיאל', 'Eng': 'Karmiel', 'Rus': 'Кармиэль', 'Arb': 'كرميئيل'}, '2940': {'Heb': 'רעננה מערב', 'Eng': "Ra'anana West", 'Rus': 'Раанана-Вест', 'Arb': 'رعنانا ويست'}, '2960': {'Heb': 'רעננה דרום', 'Eng': "Ra'anana South", 'Rus': 'Раанана Южный', 'Arb': 'رعنانا الجنوبية'}, '6150': {'Heb': 'קרית מלאכי - יואב', 'Eng': 'Kiryat Malakhi – Yoav', 'Rus': 'Кирьят Малахи-Йоав', 'Arb': 'كريات ملاخي – يوآڤ'}, '680': {'Heb': 'ירושלים - יצחק נבון', 'Eng': 'Jerusalem - Yitzhak Navon', 'Rus': 'Иерусалим - Ицхак Навон', 'Arb': 'أورشليم – يتسحاق ناڤون'}, '6900': {'Heb': 'מזכרת בתיה', 'Eng': 'Mazkeret Batya', 'Rus': 'Мазкерет Батья', 'Arb': 'مزكيرت باتيا'}}
STATION_INDEX = {'תל אביב סבידור מרכז': '3700', 'tel aviv savidor center': '3700', 'тель авив мерказ центральная': '3700', 'تل ابيب – ساڤيدور المركز': '3700', 'הרצליה': '3500', 'hertsliya': '3500', 'герцлия': '3500', 'هرتسليا': '3500', 'בית יהושע': '3400', 'bet yehoshua': '3400', 'бейт иегошуа': '3400', 'بيت يهوشوع': '3400', 'נתניה': '3300', 'netanya': '3300', 'нетания': '3300', 'نتانيا': '3300', 'חדרה מערב': '3100', 'hadera west': '3100', 'хадера маарав': '3100', 'الخضيرة غرب': '3100', 'בנימינה': '2800', 'binyamina': '2800', 'биньямина': '2800', 'بنيامينا': '2800', 'קיסריה פרדס חנה': '2820', 'caesarea pardes hana': '2820', 'кейсария пардес хана': '2820', 'قيساريا بارديس حنا': '2820', 'עתלית': '2500', 'atlit': '2500', 'атлит': '2500', 'عتليت': '2500', 'חיפה בת גלים': '2200', 'haifa bat galim': '2200', 'хайфа бат галим': '2200', 'حيفا بات چاليم': '2200', 'חוצות המפרץ': '1300', 'hutsot hamifrats': '1300', 'хоцот ха мифрац': '1300', 'حوتسوت همفراتس': '1300', 'קריית חיים': '700', 'kiryat hayim': '700', 'кирьят хаим': '700', 'كريات حاييم': '700', 'קריית מוצקין': '1400', 'kiryat motzkin': '1400', 'кирьят моцкин': '1400', 'كريات موتسكين': '1400', 'עכו': '1500', 'ako': '1500', 'акко': '1500', 'عكا': '1500', 'חיפה חוף הכרמל (ש רזיאל)': '2300', 'haifa hof hakarmel (razi`el)': '2300', 'хайфа хоф ха кармель': '2300', 'حيفا شاطئ الكرمل': '2300', 'כפר סבא נורדאו (א קוסטיוק)': '8700', 'kfar sava nordau (a.kostyuk)': '8700', 'кфар саба – нордау (а. костюк)': '8700', 'كفار سابا نورداو': '8700', 'נהריה': '1600', 'nahariya': '1600', 'нагария': '1600', 'نهاريا': '1600', 'ירושלים גן החיות התנכי': '6500', 'jerusalem biblical zoo': '6500', 'иерусалим – зоопарк': '6500', 'القدس حديقة الحيوان التوراتية': '6500', 'בית שמש': '6300', 'bet shemesh': '6300', 'бейт шемеш': '6300', 'بيت شيمش': '6300', 'קריית גת': '7000', 'kiryat gat': '7000', 'кирьят гат': '7000', 'كريات چات': '7000', 'לוד': '5000', 'lod': '5000', 'лод': '5000', 'اللد': '5000', 'באר שבע צפון/אוניברסיטה': '7300', 'beer sheva north/university': '7300', 'беер шева цафон': '7300', 'بئر السبع شمال/الجامعة': '7300', 'כפר חב"ד': '4800', 'kfar habad': '4800', 'кфар хабад': '4800', 'كفار حباد': '4800', 'תל אביב השלום': '4600', 'tel aviv hashalom': '4600', 'тель авив ха шалом': '4600', 'تل أبيب السلام': '4600', 'חיפה מרכז השמונה': '2100', 'haifa center hashmona': '2100', 'хайфа мерказ центральная': '2100', 'حيفا المركز هشمونا': '2100', 'רמלה': '5010', 'ramla': '5010', 'рамле': '5010', 'الرملة': '5010', 'ראש העין צפון': '8800', 'rosh haayin north': '8800', 'рош ха айн цафон': '8800', 'روش هعاين شمال': '8800', 'באר יעקב': '5300', 'beer yaakov': '5300', 'беер яаков': '5300', 'بئير يعكوف': '5300', 'רחובות (א הדר)': '5200', 'rehovot (e. hadar)': '5200', 'реховот им. а. хадара': '5200', 'رحوڤوت': '5200', 'יבנה מזרח': '5410', 'yavne east': '5410', 'явне восток': '5410', 'ياڤنه شرق': '5410', 'ראשון לציון הראשונים': '9100', 'rishon letsiyon harishonim': '9100', 'ришон ле цион ха ришоним': '9100', 'ريشون لتسيون هريشونيم': '9100', 'אשדוד עד הלום (מ בר כוכבא)': '5800', 'ashdod ad halom (m.bar kochva)': '5800', 'ашдод ад халом (м. бар кохва)': '5800', 'أشدود عاد هلوم': '5800', 'פתח תקווה סגולה': '4250', 'petah tikva segula': '4250', 'петах тиква сгула': '4250', 'بيتح تكڤا سچوله': '4250', 'בני ברק': '4100', 'bnei brak': '4100', 'бней брак': '4100', 'بني براك': '4100', 'תל אביב אוניברסיטה': '3600', 'tel aviv university': '3600', 'тель авив университет': '3600', 'تل أبيب الجامعة': '3600', 'באר שבע מרכז': '7320', 'beer sheva center': '7320', 'беер шева мерказ': '7320', 'بئر السبع المركز': '7320', 'מרכזית המפרץ (לב המפרץ)': '1220', 'hamifrats central station': '1220', 'центральная станция ха мифрац': '1220', 'همفراتس المركزية': '1220', 'תל אביב ההגנה': '4900', 'tel aviv hahagana': '4900', 'тель авив ха хагана': '4900', 'تل أبيب ههچناه': '4900', 'נמל תעופה בן גוריון': '8600', 'ben gurion airport': '8600', 'бен гурион аэропорт': '8600', 'مطار بن چوريون': '8600', 'ירושלים מלחה': '6700', 'jerusalem malha': '6700', 'иерусалим малха': '6700', 'القدس المالحه': '6700', 'אשקלון': '5900', 'ashkelon': '5900', 'ашкелон': '5900', 'أشكلون': '5900', 'דימונה': '7500', 'dimona': '7500', 'димона': '7500', 'ديمونا': '7500', 'הוד השרון סוקולוב': '9200', 'hod hasharon sokolov': '9200', 'ход хашарон соколов': '9200', 'هود هشارون سوكولوڤ': '9200', 'פתח תקווה קריית אריה': '4170', 'petah tikva kiryat arye': '4170', 'петах тиква – кирьят арье': '4170', 'بيتح تكڤا كريات أريه': '4170', 'לוד גני אביב': '5150', 'lod gane aviv': '5150', 'лод ганей авив': '5150', 'اللد چاني أڤيڤ': '5150', 'להבים רהט': '8550', 'lehavim rahat': '8550', 'леавим рахат': '8550', 'لهاڤيم رهط': '8550', 'פאתי מודיעין': '300', 'paate modiin': '300', 'патей модиин': '300', 'بأتي موديعين': '300', 'מודיעין מרכז': '400', 'modiin center': '400', 'модиин центр': '400', 'موديعين المركز': '400', 'צומת חולון': '4640', 'holon junction': '4640', 'холон развязка холон': '4640', 'مفترق حولون': '4640', 'חולון וולפסון': '4660', 'holon wolfson': '4660', 'холон вольфсон': '4660', 'حولون ڤولفسون': '4660', 'בת ים יוספטל': '4680', 'bat yam yoseftal': '4680', 'бат ям йосеф таль': '4680', 'بات يام يوسفطال': '4680', 'בת ים קוממיות': '4690', 'bat yam komemiyut': '4690', 'бат ям комемуют': '4690', 'بات يام كوميميوت': '4690', 'ראשון לציון משה דיין': '9800', 'rishon letsiyon moshe dayan': '9800', 'ришон ле цион станция им. моше даяна': '9800', 'ريشون لتسيون موشي ديان': '9800', 'יבנה מערב': '9000', 'yavne west': '9000', 'явне запад': '9000', 'ياڤني غرب': '9000', 'שדרות': '9600', 'sderot': '9600', 'сдерот': '9600', 'سديروت': '9600', 'נתיבות': '9650', 'netivot': '9650', 'нетивот': '9650', 'نتيفوت': '9650', 'אופקים': '9700', 'ofakim': '9700', 'офаким': '9700', 'أوفاكيم': '9700', 'נתניה ספיר': '3310', 'netanya sapir': '3310', 'нетания – сапир': '3310', 'نتانيا سبير': '3310', 'יקנעם כפר יהושע': '1240', 'yokneam kfar yehoshua': '1240', 'йокнеам – кфар иегошуа': '1240', 'يوكنعام – كفار يهوشوع': '1240', 'מגדל העמק כפר ברוך': '1250', 'migdal haemek kfar barukh': '1250', 'мигдаль ха эмек – кфар барух': '1250', 'مجدال هعيمك – كفار باروخ': '1250', 'עפולה ר.איתן': '1260', 'afula r.eitan': '1260', 'афула р. эйтан': '1260', 'العفولة ر. ايتان': '1260', 'בית שאן': '1280', 'beit shean': '1280', 'бейт шеан': '1280', 'بيت شآن': '1280', 'אחיהוד': '1820', 'ahihud': '1820', 'ахихуд': '1820', 'احيهود': '1820', 'כרמיאל': '1840', 'karmiel': '1840', 'кармиэль': '1840', 'كرميئيل': '1840', 'רעננה מערב': '2940', 'raanana west': '2940', 'раанана вест': '2940', 'رعنانا ويست': '2940', 'רעננה דרום': '2960', 'raanana south': '2960', 'раанана южный': '2960', 'رعنانا الجنوبية': '2960', 'קרית מלאכי יואב': '6150', 'kiryat malakhi – yoav': '6150', 'кирьят малахи йоав': '6150', 'كريات ملاخي – يوآڤ': '6150', 'ירושלים יצחק נבון': '680', 'jerusalem yitzhak navon': '680', 'иерусалим ицхак навон': '680', 'أورشليم – يتسحاق ناڤون': '680', 'מזכרת בתיה': '6900', 'mazkeret batya': '6900', 'мазкерет батья': '6900', 'مزكيرت باتيا': '6900'}
