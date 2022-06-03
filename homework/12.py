from tkinter import*
import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

win = Tk()
win.title('Официальный курс некоторых валют на данный момент')
win.geometry('350x200')
win['bg'] = '#DDF983'
us = round(data['Valute']['USD']['Value'],2)
eu = round(data['Valute']['EUR']['Value'],2)
def usd():
    lebl = Label(win, text = f'1 USD = {us} руб',font = ('Arial bold',22),bg = '#99FF99')
    lebl.pack()
def eur():
    lebl = Label(win, text = f'1 EUR = {eu} руб',font = ('Arial bold',22),bg = '#99CCFF')
    lebl.pack()
btn_eur = Button(win,font =('Arial bold',22),text ='Курс Евро',bg ='#99CCFF', command = eur)     
btn_usd = Button(win,font =('Arial bold',22),text ='Курс доллара США',bg ='#99FF99', command = usd)
    
btn_usd.pack()
btn_eur.pack()
win.mainloop()