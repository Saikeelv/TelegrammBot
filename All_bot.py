import telebot
from telebot import types # для указание типов
bot = telebot.TeleBot('5855454149:AAEvWYINNxXHSIrVnV27LjIQ0JxTfO8PBKc') 

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет, хочу")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, хочешь поговорить?".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):   
    if(message.text == "Привет, хочу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери персонажа для беседы", reply_markup=markup)
#############################################################################################
#2D tyan  
      
    if(message.text == "2D тяночка"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_cinema = types.KeyboardButton("Кино")
        btn_mus = types.KeyboardButton("Музыка")
        btn_anime = types.KeyboardButton("Аниме")
        markup.add(btn_cinema, btn_anime, btn_mus) 
        bot.send_message(message.chat.id, text="Классно, о чем хочешь поговорить?", reply_markup=markup)
    ''' '''
    if(message.text == "Кино"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_triller = types.KeyboardButton("триллер")
        btn_fantastic = types.KeyboardButton("фантастика")
        btn_dramma = types.KeyboardButton("драмма")
        btn_romantic = types.KeyboardButton("романтика")
        markup.add(btn_dramma, btn_fantastic, btn_romantic, btn_triller) 
        bot.send_message(message.chat.id, text="Круто, какие жанры предпочитиешь?", reply_markup=markup)
        
    if (message.text == "триллер" or message.text == "драмма" or message.text == "фантастика" or message.text == "романтика"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_Yes = types.KeyboardButton("Конечно хочу")
        btn_No = types.KeyboardButton("Не очень")
        markup.add(btn_Yes, btn_No) 
        bot.send_message(message.chat.id, text="А у тебя хороший вкус)\n Хочешь узнать какой у меня любимый фильм?", reply_markup=markup)
    if(message.text == "Конечно хочу"):
        markup = types.InlineKeyboardMarkup()
        btn_url = types.InlineKeyboardButton("Вот он", url='https://www.youtube.com/watch?v=F2i1se1MwP0')
        markup.add(btn_url)
        bot.send_message(message.chat.id, "Обожаю этот фильм", reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
        
    if(message.text == "Не очень"):
        bot.send_message(message.chat.id, text="Ну и ладно, ищи себе другую 2д девушку....")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
   
    ''' '''
    if(message.text == "Музыка"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_kpop = types.KeyboardButton("k-pop")
        btn_rock = types.KeyboardButton("рок")
        btn_rep = types.KeyboardButton("рэп")
        btn_hiphop = types.KeyboardButton("хип-хоп")
        markup.add(btn_kpop, btn_rock, btn_rep, btn_hiphop) 
        bot.send_message(message.chat.id, text="люблю говорить о музыке)\nкакие жанры тебе нравятся?", reply_markup=markup)
        
    if(message.text == "k-pop" or message.text == "рок" or message.text == "рэп" or message.text == "хип-хоп"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_No = types.KeyboardButton("Нет")
        markup.add(btn_No) 
        bot.send_message(message.chat.id, text="Круто, скажшь название группы?(напиши текстом в чат)", reply_markup=markup)
    if(message.text == "Metallica"):
        bot.send_message(message.chat.id, text="Ты не поверишь, но oна мне тоже очень нравится)\n Но моя самая любимая группа - SOAD")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
        
    if(message.text == "Нет"):
        bot.send_message(message.chat.id, text="Ну и ладно, не очень то и интересно. Я тоже не скажу свою любимую группу")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
       
    ''' '''
     
    if(message.text == "Аниме"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_Yes = types.KeyboardButton("Конечно смотрел")
        btn_No = types.KeyboardButton("Неа")
        markup.add(btn_Yes, btn_No)
        bot.send_message(message.chat.id, text="Ах тыж маленький любитель японской анимации?\nСмотрел евангелион?", reply_markup=markup)
        
    if(message.text == "Конечно смотрел"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_Yes = types.KeyboardButton("Конечно)")
        btn_No = types.KeyboardButton("Не")
        markup.add(btn_Yes, btn_No)
        bot.send_photo(message.chat.id, 'http://pm1.narvii.com/7969/35cd9f7688731554722d45fced64ed00824aa7d2r1-960-540v2_uhq.jpg');
        bot.send_message(message.chat.id, text="Хочешь ещё мемчик?)", reply_markup=markup );
    if(message.text == "Конечно)"):
        bot.send_photo(message.chat.id, 'http://pm1.narvii.com/6986/fcb1d0560f50adada25582dbcea4df8020d827a1r1-1024-686v2_uhq.jpg');
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
           
    if(message.text == "Неа"):
         markup = types.InlineKeyboardMarkup()
         btn_url = types.InlineKeyboardButton("Вот тебе ссылочка", url='https://animego.org/anime/evangelion-863')
         markup.add(btn_url)
         bot.send_message(message.chat.id, text="Очень советую посмотреть", reply_markup=markup)
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn_boy = types.KeyboardButton("Пай - мальчик")
         btn_2d = types.KeyboardButton("2D тяночка")
         btn_hait = types.KeyboardButton("Хейтер")
         markup.add(btn_boy, btn_2d, btn_hait) 
         bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
    if(message.text == "Не"):
         bot.send_message(message.chat.id, text="ах, не буду тебе больше мемы скидывыать...")  
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn_boy = types.KeyboardButton("Пай - мальчик")
         btn_2d = types.KeyboardButton("2D тяночка")
         btn_hait = types.KeyboardButton("Хейтер")
         markup.add(btn_boy, btn_2d, btn_hait) 
         bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
##########################################################################################################
#haiter
    if (message.text == "Хейтер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Лучше, чем у тебя!")
        markup.add(btn1)
        bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}! Как дела?".format(message.from_user), reply_markup=markup)
    if (message.text == "Лучше, чем у тебя!"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что за наезд?")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Где твое уважение?", reply_markup=markup)

    if (message.text == "Что за наезд?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Низкая самооценка")
        btn2 = types.KeyboardButton("Неудачи по жизни")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Эй-эй, давай о чем-нибудь тогда поговорим!", reply_markup=markup)
        bot.send_message(message.chat.id, text="Что хочешь обсудить?", reply_markup=markup)

    if (message.text == "Низкая самооценка"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Под стулом")
        btn2 = types.KeyboardButton("Ниже плинтуса")
        btn3 = types.KeyboardButton("В Бикини Боттом")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выбери уровни?", reply_markup=markup)

    if (message.text == "Под стулом"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Дыа")
        btn2 = types.KeyboardButton("Нетт")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Ты уверен в своем выборе?", reply_markup=markup)

    if (message.text == "Дыа"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Лайк")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Это стул в доме Патрика", reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://yandex.ru/images/search?text=дом%20патрика%20мем&from=tabbar&pos=11&img_url=http%3A%2F%2Fimg.buzzfeed.com%2Fbuzzfeed-static%2Fstatic%2F2020-01%2F2%2F17%2Fasset%2F6b104667e1d1%2Fsub-buzz-405-1577985785-9.png&rpt=simage&lr=120836')
###
    if (message.text == "Лайк"):
        bot.send_message(message.chat.id, text="Еще увидимся")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)

    if (message.text == "Нетт"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Еще ниже?")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="А где она?", reply_markup=markup)

    if (message.text == "Еще ниже?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Лайкос")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Погнали в гости к Патрику", reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://yandex.ru/images/search?from=tabbar&text=патрик%20мем&pos=29&img_url=http%3A%2F%2Fcartoonbucket.com%2Fwp-content%2Fuploads%2F2015%2F12%2FPatrick-Star-Smiling-eq245.gif&rpt=simage&lr=120836')
###
    if (message.text == "Лайкос"):
        bot.send_message(message.chat.id, text="До встречи!")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)

    if (message.text == "Ниже плинтуса"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Ок, допустим")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Нужно выбирать еще ниже", reply_markup=markup)

    if (message.text == "Ок, допустим"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Зачет")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Добро пожаловать в Бикини Боттом, сегодня скидки на крабсбургеры", reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://yandex.ru/images/search?text=бикини%20боттом&from=tabbar&p=2&pos=68&rpt=simage&img_url=http%3A%2F%2Fwhitegames.net%2Fuploads%2Fposts%2F2020-08%2F15965308797_440-h620.jpg&lr=120836')
###
    if (message.text == "Зачет"):
        bot.send_message(message.chat.id, text="До скорой!")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)

    if (message.text == "В Бикини Боттом"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Класс")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Добро пожаловать! В Красти Краб сегодня скидочки!", reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://yandex.ru/images/search?text=красти%20крабс%20мем&from=tabbar&pos=17&img_url=http%3A%2F%2Fi.ytimg.com%2Fvi%2FQyKTtXgWfGA%2Fmaxresdefault.jpg&rpt=simage&lr=120836')
###
    if (message.text == "Класс"):
        bot.send_message(message.chat.id, text="Пошел за крабсбургером")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)

    if (message.text == "Неудачи по жизни"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Рождение")
        btn2 = types.KeyboardButton("У меня нет друзей")
        btn3 = types.KeyboardButton("Все стабильно")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выбери какую?", reply_markup=markup)

    if(message.text == "Рождение"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("В окне")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Выход есть и он?", reply_markup=markup)
###
    if (message.text == "В окне"):
        bot.send_message(message.chat.id, text="Номер психологической помощи: 84232227665")
        bot.send_photo(message.chat.id, photo='https://yandex.ru/images/search?from=tabbar&text=номер%20психологической%20помощи%20мем&pos=20&img_url=http%3A%2F%2Frisovach.ru%2Fupload%2F2014%2F01%2Fmem%2Ftoni-stark_40740970_big_.jpeg&rpt=simage&lr=120836')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)

    if (message.text == "У меня нет друзей"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Не хочу")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Давай дружить!", reply_markup=markup)
###
    if (message.text == "Не хочу"):
        bot.send_message(message.chat.id, text="Ищи других слушателей")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)

    if (message.text == "Все стабильно"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Себя")
        btn2 = types.KeyboardButton("Меня")
        btn3 = types.KeyboardButton("Родителей")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Кого ты обманываешь?", reply_markup=markup)
###
    if (message.text == "Себя"):
        bot.send_message(message.chat.id, text="Номер психологической помощи")
        bot.send_photo(message.chat.id, photo= 'https://yandex.ru/images/search?from=tabbar&text=номер%20психологической%20помощи%20мем&pos=20&img_url=http%3A%2F%2Frisovach.ru%2Fupload%2F2014%2F01%2Fmem%2Ftoni-stark_40740970_big_.jpeg&rpt=simage&lr=120836');
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
###
    if (message.text == "Меня"):
        bot.send_message(message.chat.id, text="Все х**yня, давай по новой!")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
###
    if (message.text == "Родителей"):
        bot.send_message(message.chat.id, text="Тебе нужно больше стараться!")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_boy = types.KeyboardButton("Пай - мальчик")
        btn_2d = types.KeyboardButton("2D тяночка")
        btn_hait = types.KeyboardButton("Хейтер")
        markup.add(btn_boy, btn_2d, btn_hait) 
        bot.send_message(message.chat.id, text="Выбери нового персонажа для беседы", reply_markup=markup)
            
    
        
    
   
    
   
    





        
        
        
bot.polling(none_stop=True)