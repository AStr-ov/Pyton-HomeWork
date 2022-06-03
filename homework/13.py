import telebot
bot= telebot.TeleBot('5421160068:AAEhHEUK5n8WsUmLitx2UaLAKes1mV1QBtU')

@bot.message_handler(commands=['start'])
def pusk(m):
    bot.send_message(m.chat.id, 'Привет. Если хочешь подсчитать выражение, пожалуйста, вводи все через пробел!')

#@bot.message_handler(commands=['calc'])
@bot.message_handler(content_types=['text']) 

def calc(mes):   
    nums=mes.text.split()    
    x=int(nums[0])
    y=int(nums[2])
    if nums[1]=='+':
        bot.send_message(mes.chat.id, f'{x} + {y} = {x+y} ')
    elif nums[1]=='-':
        bot.send_message(mes.chat.id, f'{x} - {y} = {x-y} ')
    elif nums[1]=='*':
        bot.send_message(mes.chat.id, f'{x} * {y} = {x*y} ')
    elif nums[1]=='/':
        bot.send_message(mes.chat.id, f'{x} / {y} = {x/y} ')

    
bot.polling(none_stop=True, interval=0)