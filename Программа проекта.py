import telebot
from telebot import types


bot = telebot.TeleBot('id')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton('ОГЭ')
    item3 = types.KeyboardButton('ЕГЭ')
    markup.add(item2, item3)
    bot.send_message(message.chat.id, f'Привет. \nЧем займешься сегодня?'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'ОГЭ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Задание 01')
        item2 = types.KeyboardButton('Задание 02')
        item3 = types.KeyboardButton('Задание 03')
        item4 = types.KeyboardButton('Задание 04')
        item5 = types.KeyboardButton('Задание 05')
        back = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3, item4, item5, back)
        bot.send_message(message.chat.id, f'Выбери номер задания ОГЭ'.format(message.from_user),reply_markup=markup)

    elif message.text == 'ЕГЭ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Задание 1-3')
        item4 = types.KeyboardButton('Задание 4')
        item5 = types.KeyboardButton('Задание 5')
        item6 = types.KeyboardButton('Задание 6')
        item7 = types.KeyboardButton('Задание 7')
        item8 = types.KeyboardButton('Задание 8')
        item9 = types.KeyboardButton('Задание 9')
        item10 = types.KeyboardButton('Задание 10')
        item11 = types.KeyboardButton('Задание 11')
        item12 = types.KeyboardButton('Задание 12')
        item13 = types.KeyboardButton('Задание 13')
        item14 = types.KeyboardButton('Задание 14')
        item16 = types.KeyboardButton('Задание 16-21')
        back= types.KeyboardButton('Назад')
        markup.add(item1, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item16, back)

        bot.send_message(message.chat.id, f'Выбери номер задания ЕГЭ'.format(message.from_user),reply_markup=markup)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton('ОГЭ')
        item3 = types.KeyboardButton('ЕГЭ')
        markup.add(item2, item3)
        bot.send_message(message.chat.id, 'Назад'.format(message.from_user), reply_markup=markup)

    elif message.text == 'Задание 1-3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton('1')
        item3 = types.KeyboardButton('2-3')
        markup.add(item2, item3)
        bot.send_message(message.chat.id, '1-3'.format(message.from_user), reply_markup=markup)

    elif message.text == 'Задание 4':
        bot.send_message(message.chat.id, "см Орфоэпический словарь")
    elif message.text == '1':
        bot.send_message(message.chat.id, "1е Задание ЕГЭ")
        b1 = open("image_2023-05-10_01-04-19.png", "rb")
        bot.send_photo(message.chat.id, b1)
        b2 = open("image_2023-05-10_01-04-38.png", "rb")
        bot.send_photo(message.chat.id, b2)
        b3 = open("image_2023-05-10_01-05-00.png", "rb")
        bot.send_photo(message.chat.id, b3)
    elif message.text == '2-3':
        bot.send_message(message.chat.id, "2е-3е Задания ЕГЭ")
        b4 = open("image_2023-05-10_01-05-24.png", "rb")
        bot.send_photo(message.chat.id, b4)
        b5 = open("image_2023-05-10_01-05-50.png", "rb")
        bot.send_photo(message.chat.id, b5)
        b6 = open("image_2023-05-10_01-06-10.png", "rb")
        bot.send_photo(message.chat.id, b6)
        b7 = open("image_2023-05-10_01-06-27.png", "rb")
        bot.send_photo(message.chat.id, b7)
        b8 = open("image_2023-05-10_01-06-43.png", "rb")
        bot.send_photo(message.chat.id, b8)
        b9 = open("image_2023-05-10_01-06-58.png", "rb")
        bot.send_photo(message.chat.id, b9)
    elif message.text == '3':
        bot.send_message(message.chat.id, "Смотри")

    elif message.text == 'Задание 01':
        bot.send_message(message.chat.id, '☆Сжатое изложение:')
        bot.send_message(message.chat.id, '✿Необходимо написать все микротемы текста.')
        bot.send_message(message.chat.id, '\nМикротема – это главная мысль абзаца.\nВ изложении бывает 3-4 абзаца.')
        bot.send_message(message.chat.id, '✿Cпособы сжатия текста: ')
        bot.send_message(message.chat.id, '•Исключение\nЧто можно и нужно исключить:')
        bot.send_message(message.chat.id, 'повторы\nсинонимы\nнесущественную информацию\nописания\nОЧП')
        bot.send_message(message.chat.id, '•Обобщение ')
        bot.send_message(message.chat.id, 'ОЧП обобщающим словом\nчасти предложения синонимами, местоимением')
        bot.send_message(message.chat.id, '•Упрощение')
        bot.send_message(message.chat.id, 'соединение нескольких предложений в одно\nзамена прямой речи косвенной')

    elif message.text == 'Задание 02':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Общие сведения")
        item2 = types.KeyboardButton("Подлежащее")
        item3 = types.KeyboardButton("Сказуемое")
        item4 = types.KeyboardButton("Второстепенные члены предложения")
        item5 = types.KeyboardButton("Предложения бывают:")
        item6 = types.KeyboardButton("Передача речи")
        item7 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.chat.id, '2е задание ОГЭ'.format(message.from_user), reply_markup=markup)

    elif message.text == 'Общие сведения':
        bot.send_message(message.chat.id, 'Грамматическая основа – это главные члены предложения.')
        bot.send_message(message.chat.id, """
        Грамматическая основа состоит из подлежащего и сказуемого (или только одного из главных членов предложения).
        \nПодлежащее – то, о чем говорится в предложении.\nСказуемое – это что говорится о подлежащем в предложении.
        Подежащее и сказуемое могут быть выражены любой частью речи.""")
    elif message.text == 'Подлежащее':
        bot.send_message(message.chat.id,
                         """Подлежащее\nПодлежащее должно стоять в И.п.
                         Слова МНЕ, ТЕБЕ, ЕМУ, ЕЙ, НАМ, ВАМ, ИМ не могут быть подлежащим.
                         В придаточной части СПП в роли подлежащего могут выступать союзные слова КОТОРЫЙ, ЧТО, КТО.
                         Подлежащее может быть выражено одним словом (любой частью речи) или словосочетанием.
                         Подлежащее = словосочетание
                         1. Сущ. в И.п. + С + сущ в Т.п.(кто с кем)2. Числ(сущ.) + сущ. в Р.п.(кол-во деятелей)
                         Слова много, мало, несколько, большинство входят в подлежащее.
                         3. Слово в И.п. + ИЗ +слово в Р.п. (кто-то из кого-то, что-то из чего-то; часть целого)
                         4. Начало, середина,конец + сущ. (значение фазы)
                         5. Фразеологизм (устойчивое неделимое словосочетание) или метафора.
                         6. Неопределенное местоимение от …кто …что +имя Пример: Что-то неприятное было в егооблике.""")
    elif message.text == 'Сказуемое':
        bot.send_message(message.chat.id,
                         """Сказуемое\nСказуемое бывает:\n""")
        z1 = open("msg1204733824-86260.png", "rb")
        bot.send_photo(message.chat.id, z1)
    elif message.text == 'Второстепенные члены предложения':
        bot.send_message(message.chat.id,
                         """Второстепенные члены предложения""")
        z2 = open("image_2023-04-23_11-30-23.png", "rb")
        bot.send_photo(message.chat.id, z2)
    elif message.text == 'Предложения бывают:':
        bot.send_message(message.chat.id, "Двусоставные и односоставные предложения")
        bot.send_message(message.chat.id, "Типы односоставных предложений")
        z3 = open("image_2023-04-24_18-30-57.png", "rb")
        bot.send_photo(message.chat.id, z3)
        bot.send_message(message.chat.id, "Сложное предложение")
        z4 = open("image_2023-04-24_18-35-10.png", "rb")
        bot.send_photo(message.chat.id, z4)
    elif message.text == 'Передача речи':
        bot.send_message(message.chat.id, "Способы выражения чужой речи")
        z5 = open("image_2023-04-24_18-36-55.png", "rb")
        bot.send_photo(message.chat.id, z5)

    elif message.text == 'Задание 03':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        item1 = types.KeyboardButton("Знаки препинания в ССП")
        item2 = types.KeyboardButton("Знаки препинания в предложениях с ОЧ")
        item3 = types.KeyboardButton("Обособленные члены предложения")
        item4 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, '3е задание ОГЭ'.format(message.from_user), reply_markup=markup)

    elif message.text == 'Знаки препинания в ССП':
        bot.send_message(message.chat.id,
                         """Запятая в ССП не ставится:
                         1.Когда есть общий второстепенный член предложения
                         2.Когда есть общая придаточная часть
                         3.Когда есть общее вводное слово
                         4.Когда соединяются 2 вопросительных, 2 восклицательных, 2 побудительных и 2 назывных предложения""")
        bot.send_message(message.chat.id,
                         """Знаки препинания в СПП.
Придаточная часть может находиться абсолютно в любой
части предложения.\nВажно помнить, что нужно обязательно находить границу
между предложениями, а не ставить запятую перед союзами.\n
Придаточная часть всегда отделяется от главной запятой
(исключение составляют однородные придаточные,
соединенные союзом И)""")

    elif message.text == 'Знаки препинания в предложениях с ОЧ':
        bot.send_message(message.chat.id,
                         """Знаки препинания в предложениях с ОЧ (однородными членами)""")
        bot.send_message(message.chat.id,
                         """1.Запятая ставится, если
 ОЧ не соединены никакими союзами.\n2.Запятая не ставится, если ОЧ соединены сочинительными союзами.\n
 3.Запятая ставится, если ОЧ соединены противительными союзами (но, а, да (=но))\n
 4.Если в предложении мы видим повторяющиеся союзы, то запятая ставится перед вторым и последующими.\n
 НО: если перед первым союзом есть такой же ОЧ, то запятая ставится перед первым и последующими союзами.\n
 5.Если ОЧ соединеныдвойными сопоставительными союзами, то запятая ставится перед второй частью
 союза.\n6.Нужно помнить об обобщающих словах при ОЧ. Если обобщающее слово стоит перед рядом ОЧ, то ставим :
 Если же обобщающее
 слово стоит после ряда
 ОЧ, то ставим -""")
    elif message.text == 'Обособленные члены предложения':
        bot.send_message(message.chat.id,
                         """Обособленные члены предложения.""")
        bot.send_message(message.chat.id,
                         """Причастный оборот – это причастие с зависимыми словами.
Отвечает на вопросы Какой? Какая? Какие? Является
определением. Всегда относится к какому-то слову
(существительному или местоимению), которое может стоять
либо впереди него, либо после. Именно от этого зависят
случаи обособления.""")
        bot.send_message(message.chat.id,
                         """Обособленное определение, выраженно причастным
оборотом, выделяется запятыми, когда:\n
1.Стоит после определяемого слова\n
2.Относится к личному местоимению (в этом случае оборот
обособляется в любой позиции)""")
        bot.send_message(message.chat.id,
                         """Не обособляется такой оборот, когда:\n
                         1.Определяемое слово стоит после оборота\n
2.НО: если при этом оборот имеет добавочное
обстоятельственное значение (можно заменить на СПП с
обстоятельственным значением), то все равно обособляетс.""")
        bot.send_message(message.chat.id,
                         """Деепричастный оборот – это деепричастие с зависимыми
словами. Отвечает на вопрос Что делая? Что сделав? Как?
Является обстоятельством в предложении. Относится к
глаголу. Обособляется во всех случаях.\n Два или несколько одиночных деепричастий или
деепричастных оборотов являются ОЧ и между собой
обособляются по правилу ОЧ""")
    elif message.text == 'Задание 04':
        bot.send_message(message.chat.id, "Типы связи в словосочетании")
        z6 = open("image_2023-04-24_19-28-10.png", "rb")
        bot.send_photo(message.chat.id, z6)
    elif message.text == 'Задание 05':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        item1 = types.KeyboardButton("Корни с чередованием")
        item2 = types.KeyboardButton("Приставки")
        item4 = types.KeyboardButton("Личные окончания глаголов")
        item5 = types.KeyboardButton("НЕ с различными частями речи")
        item6 = types.KeyboardButton("Н и НН")
        item7 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item4, item5, item6, item7)
        bot.send_message(message.chat.id, '5е задание ОГЭ'.format(message.from_user), reply_markup=markup)
    elif message.text == 'Корни с чередованием':
        bot.send_message(message.chat.id,
                         """Корни с чередованием""")
        z7 = open("image_2023-04-25_09-40-05.png", "rb")
        bot.send_photo(message.chat.id, z7)
    elif message.text == 'Приставки':
        bot.send_message(message.chat.id, "Приставки")
        z8 = open("image_2023-04-25_09-44-09.png", "rb")
        bot.send_photo(message.chat.id, z8)
    elif message.text == 'Личные окончания глаголов':
        bot.send_message(message.chat.id, "Личные окончания глаголов")
        z9 = open("image_2023-04-25_09-46-51.png", "rb")
        bot.send_photo(message.chat.id, z9)
    elif message.text == 'НЕ с различными частями речи':
        bot.send_message(message.chat.id,"НЕ с различными частями речи")
        z10 = open("image_2023-04-25_09-52-22.png", "rb")
        bot.send_photo(message.chat.id, z10)
    elif message.text == 'Н и НН':
        bot.send_message(message.chat.id,"Н и НН")
        z11 = open("image_2023-04-25_09-51-53.png", "rb")
        bot.send_photo(message.chat.id, z11)

    elif message.text == 'Задание 7':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        item1 = types.KeyboardButton("Прилагательные")
        item2 = types.KeyboardButton("Числительные")
        item3 = types.KeyboardButton("Местоимения")
        item4 = types.KeyboardButton("Глаголы")
        item7 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4, item7)
        bot.send_message(message.chat.id, '7е задание ЕГЭ'.format(message.from_user), reply_markup=markup)
    elif message.text == 'Прилагательные':
        bot.send_message(message.chat.id, "Прилагательные")
        z12 = open("image_2023-05-02_10-43-42.png", "rb")
        bot.send_photo(message.chat.id, z12)

    elif message.text == 'Числительные':
        bot.send_message(message.chat.id, "Числительные")
        z13 = open("image_2023-05-02_10-44-19.png", "rb")
        bot.send_photo(message.chat.id, z13)
    elif message.text == 'Местоимения':
        bot.send_message(message.chat.id, "Местоимения")
        z14 = open("image_2023-05-02_10-44-43.png", "rb")
        bot.send_photo(message.chat.id, z14)
    elif message.text == 'Глаголы':
        bot.send_message(message.chat.id, "Глаголы")
        z15 = open("image_2023-05-02_10-45-15.png", "rb")
        bot.send_photo(message.chat.id, z15)
    elif message.text == 'Задание 8':
        bot.send_message(message.chat.id,"Виды ошибок")
        z16 = open("image_2023-05-02_10-47-10.png", "rb")
        bot.send_photo(message.chat.id, z16)
        z17 = open("image_2023-05-02_10-47-24.png", "rb")
        bot.send_photo(message.chat.id, z17)
    elif message.text == 'Задание 9':
        bot.send_message(message.chat.id, "Корни с чередованием")
        z18 = open("image_2023-05-02_10-50-19.png", "rb")
        bot.send_photo(message.chat.id, z18)
    elif message.text == 'Задание 10':
        bot.send_message(message.chat.id, "Приставки")
        z19 = open("image_2023-05-02_10-51-36.png", "rb")
        bot.send_photo(message.chat.id, z19)
        z20 = open("image_2023-05-02_10-51-59.png", "rb")
        bot.send_photo(message.chat.id, z20)

    elif message.text == 'Задание 11':
        bot.send_message(message.chat.id, "Суффиксы")
        z21 = open("image_2023-05-02_10-53-54.png", "rb")
        bot.send_photo(message.chat.id, z21)
        z22 = open("image_2023-05-02_10-54-09.png", "rb")
        bot.send_photo(message.chat.id, z22)
        z23 = open("image_2023-05-02_10-54-28.png", "rb")
        bot.send_photo(message.chat.id, z23)
    elif message.text == 'Задание 12':
        bot.send_message(message.chat.id, "Глаголы и причастия")
        z24 = open("image_2023-05-02_10-58-43.png", "rb")
        bot.send_photo(message.chat.id, z24)
        z25 = open("image_2023-05-02_10-59-02.png", "rb")
        bot.send_photo(message.chat.id, z25)
    elif message.text == 'Задание 13':
        bot.send_message(message.chat.id,
                         """НЕ НИ""")
        z26 = open("2023-05-09_17-49-37.png", "rb")
        bot.send_photo(message.chat.id, z26)
        z27 = open("2023-05-09_17-49-52.png", "rb")
        bot.send_photo(message.chat.id, z27)
    elif message.text == 'Задание 14':
        bot.send_message(message.chat.id, "Написание слов")
        z29 = open("2023-05-09_17-51-08.png", "rb")
        bot.send_photo(message.chat.id, z29)
        z30 = open("2023-05-09_17-51-24.png", "rb")
        bot.send_photo(message.chat.id, z30)
    elif message.text == 'Задание 16-21':
        bot.send_message(message.chat.id,"Знаки припинания")
        z31 = open("2023-05-09_17-58-07.png", "rb")
        bot.send_photo(message.chat.id, z31)
        z32 = open("2023-05-09_17-58-16.png", "rb")
        bot.send_photo(message.chat.id, z32)
        z33 = open("2023-05-09_17-58-29.png", "rb")
        bot.send_photo(message.chat.id, z33)
        z34 = open("2023-05-09_17-58-37.png", "rb")
        bot.send_photo(message.chat.id, z34)
        z35 = open("2023-05-09_17-58-46.png", "rb")
        bot.send_photo(message.chat.id, z35)






bot.polling(none_stop=True, interval=0)
