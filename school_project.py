import config
import telebot 
from telebot import types 


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['go', 'start']) 
def start(message):
    q_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Меню📱")
    q_markup.add(item1)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!" 
                     "\n \nЯ - <b>{1.first_name}</b>, бот помогающий ученикам 7-9 классов лучше запомнить физику! "
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=q_markup)
    

@bot.message_handler(commands=['stop'])
def stop(message):
    w_markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "Досвидания, {0.first_name}!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=w_markup)
    

@bot.message_handler(content_types=["text"])
def go_send_messages(message):
    if message.chat.type == 'private':
        if message.text == 'Меню📱':
            two_markup = types.InlineKeyboardMarkup()
            but1 = types.InlineKeyboardButton(text='Начать✅', callback_data='sta')
            but2 = types.InlineKeyboardButton(text='Контакты🌎', callback_data='kon')
            two_markup.add(but1,but2)
            bot.send_message(message.chat.id,"Меню📱".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=two_markup)


            @bot.callback_query_handler(func=lambda call: call.data in ['sta','kon'])   
            def callback_one(call):
                try:
                    if call.message:
                        if call.data == 'sta':
                            keyboard = types.InlineKeyboardMarkup()
                            ite0 = types.InlineKeyboardButton(text='7', callback_data='zero')
                            ite1 = types.InlineKeyboardButton(text='8', callback_data='one')
                            ite2 = types.InlineKeyboardButton(text='9', callback_data='two')
                            keyboard.add(ite0, ite1, ite2)
                            bot.send_message(message.chat.id,"Какой класс тебя интересует?".format(message.from_user),reply_markup=keyboard)
                        elif call.data == 'kon':
                            one_markup = types.InlineKeyboardMarkup(row_width=1)
                            ite5 = types.InlineKeyboardButton(text="Почта📫", callback_data="five")
                            ite6 = types.InlineKeyboardButton(text="Ватсап💬", callback_data="six")
                            one_markup.add(ite5, ite6)
                            bot.send_message(message.chat.id, "{0.first_name},выберите способ связи".format(message.from_user), parse_mode="html", reply_markup=one_markup)
                except Exception as e:
                    print(repr(e))


            @bot.callback_query_handler(func=lambda call: call.data in ['zero','one','two','three','four'])   
            def callback_two(call):
                try:
                    if call.message:
                        if call.data == 'zero':
                            e_markup = types.InlineKeyboardMarkup()
                            ite7 = types.InlineKeyboardButton(text='1️⃣', callback_data='1')
                            ite8 = types.InlineKeyboardButton(text='2️⃣', callback_data='2')
                            ite9 = types.InlineKeyboardButton(text='3️⃣', callback_data='3')
                            ite10 = types.InlineKeyboardButton(text='4️⃣', callback_data='4')
                            ite11 = types.InlineKeyboardButton(text='5️⃣', callback_data='5')
                            e_markup.add(ite7,ite8,ite9,ite10,ite11)
                            bot.send_message(message.chat.id,"{0.first_name}, вот основные разделы 7 класса, выбери нужный"
                                                 '\n\n1)  Физика и её роль в познании окружающего мира🌏'
                                                 '\n2)  Первоначальные сведения о строении вещества🧬'
                                                 '\n3)  Взаимодействия тел.Масса⛓️‍💥'
                                                 '\n4)  Давление твердых тел, жидкостей и газов🫗'
                                                 '\n5)  Работа и мощность. Энергия💡'.format(message.from_user),reply_markup=e_markup)
                        elif call.data == 'one':
                            r_markup = types.InlineKeyboardMarkup()
                            ite12 = types.InlineKeyboardButton(text='1️⃣', callback_data='6')
                            ite13 = types.InlineKeyboardButton(text='2️⃣', callback_data='7')
                            ite14 = types.InlineKeyboardButton(text='3️⃣', callback_data='8')
                            ite15 = types.InlineKeyboardButton(text='4️⃣', callback_data='9')
                            ite16 = types.InlineKeyboardButton(text='5️⃣', callback_data='10')
                            r_markup.add(ite12,ite13,ite14,ite15,ite16)
                            bot.send_message(message.chat.id,"{0.first_name}, вот основные разделы 8 класса, выбери нужный"
                                             '\n\n1)  Тепловые явления🔅'
                                             '\n2)  Изменение агрегатных состояний вещества💧'
                                             '\n3)  Электрические явления⚡'
                                             '\n4)  Световые явления🔦'
                                             '\n5)  Магнитные явления🧲'.format(message.from_user), reply_markup=r_markup)
                        elif call.data == 'two':
                            t_markup = types.InlineKeyboardMarkup()
                            ite17 = types.InlineKeyboardButton(text='1️⃣', callback_data='11')
                            ite18 = types.InlineKeyboardButton(text='2️⃣', callback_data='13')
                            ite19 = types.InlineKeyboardButton(text='3️⃣', callback_data='14')
                            ite20 = types.InlineKeyboardButton(text='4️⃣', callback_data='15')
                            t_markup.add(ite17,ite18,ite19,ite20)
                            bot.send_message(message.chat.id,"{0.first_name}, вот основные разделы 9 класса, выбери нужный"
                                             '\n\n1)  Законы движения и механика⚙️'
                                             '\n2)  Электричество и магнетизм⚡'
                                             '\n3)  Оптические явления и природа света🌈'
                                             '\n4)  Механические волны ⚗️'.format(message.from_user), reply_markup=t_markup)
                except Exception as e:
                    print(repr(e))


            @bot.callback_query_handler(func=lambda call: call.data in ['1','2','3','4','5',
                                                                        '6','7','8','9','10',
                                                                        '11','12','13','14','15'])
               
            def callback_four(call):
                try:
                    if call.message:
                        if call.data == '1':
                            bot.send_media_group(message.chat.id, [                                                                                       #начало 7 класса
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img3.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img10.jpg','rb'))  ])
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img11.jpg','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img12.jpg','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img13.jpg','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img14.jpg','rb'))
                        elif call.data == '2':
                            bot.send_media_group(message.chat.id, [       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1a.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2a.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img3a.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4a.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5a.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6a.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7a.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8a.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9a.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img10a.png','rb'))  ])
                        elif call.data == '3':
                            bot.send_media_group(message.chat.id, [       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1b.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2b.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img3b.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4b.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5b.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6b.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7b.png','rb'))  ])
                        elif call.data == '4':
                            bot.send_media_group(message.chat.id, [       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1c.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2c.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img3c.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4c.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5c.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6c.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7c.jpg','rb')),  
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8c.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9c.jpg','rb'))  ])
                        elif call.data == '5':
                            bot.send_media_group(message.chat.id, [
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1d.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2d.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img3d.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4d.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5d.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6d.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7d.jpg','rb')),  
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8d.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9d.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img10d.jpg','rb'))  ])
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img11d.jpg','rb')) #конец 7 класс
                        
                        
                        
                        
                        
                        elif call.data == '6':
                            bot.send_media_group(message.chat.id, [                                                                                               #начало 8 класс
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1e.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2e.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img3e.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4e.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5e.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6e.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7e.jpg','rb')),  
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8e.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9e.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img10e.jpg','rb'))  ])
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img11e.jpg','rb'))
                        elif call.data == '7':
                            bot.send_media_group(message.chat.id, [
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1f.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2f.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4f.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5f.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6f.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7f.png','rb')),  
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8f.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9f.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img10f.png','rb'))  ])
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img11f.png','rb'))
                        elif call.data == '8':
                            bot.send_media_group(message.chat.id, [
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1g.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2g.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4g.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5g.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6g.jpg','rb')),   ])
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7g.jpg','rb'))
                        elif call.data == '9':
                            bot.send_media_group(message.chat.id, [
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1h.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2h.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4h.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5h.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6h.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7h.jpg','rb')),  
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8h.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9h.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img10h.jpg','rb'))  ])
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img11h.jpg','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img12h.jpg','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img13h.jpg','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img14h.jpg','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img15h.jpg','rb'))
                        elif call.data == '10':
                            bot.send_media_group(message.chat.id, [
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1i.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2i.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4i.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5i.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6i.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7i.png','rb')),  
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8i.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9i.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img10i.png','rb'))  ])
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img11i.png','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img12i.png','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img13i.png','rb'))      #конец 8 класса




                        
                        elif call.data == '11':
                            bot.send_media_group(message.chat.id, [                                                                                        #начало 9 класс
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1j.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2j.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4j.png','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5j.png','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6j.png','rb'))  ])
                        elif call.data == '13':
                            bot.send_media_group(message.chat.id, [                                                                                        
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1k.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2k.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4k.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5k.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6k.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7k.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8k.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9k.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img10k.jpg','rb'))  ])
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img11k.jpg','rb'))
                            bot.send_photo(message.chat.id,open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img12k.jpg','rb'))
                        elif call.data == '14':
                            bot.send_media_group(message.chat.id, [                                                                                        
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1l.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2l.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4l.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5l.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6l.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7l.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8l.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9l.jpg','rb'))  ])
                        elif call.data == '15':
                            bot.send_media_group(message.chat.id, [                                                                                        
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img1m.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img2m.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img4m.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img5m.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img6m.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img7m.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img8m.jpg','rb')),       
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img9m.jpg','rb')),
                            telebot.types.InputMediaPhoto(open(r'C:\Users\misha\Desktop\telegram-bot\photo1\img10m.jpg','rb'))  ])      #конец 9 класса
                
                
                except Exception as e:
                    print(repr(e))

            @bot.callback_query_handler(func=lambda call: call.data in ['five','six']) 
            def get_user_photo(call):
                try:
                    if call.message:
                        if call.data == 'five':  
                            bot.send_message(call.message.chat.id,"Почта для связи📫\n**********@mail.ru")
                        elif call.data == 'six':
                            bot.send_message(call.message.chat.id,"Ватсап💬\n+7(925)-***-**-**")

                except Exception as e:
                    print(repr(e))
    

if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print('Ошибка соединения: ', e)
    except Exception as r:
        print("Ошибка в коде: ", r)
    finally:
        print("Бот выключен")