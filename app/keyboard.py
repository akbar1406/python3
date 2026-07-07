from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
ReplyKeyboardMarkup,KeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

first = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text='Каталог', )]
])
inline_catalog = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Купить',url='https://www.youtube.com')],
  [InlineKeyboardButton(text='Назад',callback_data='back')]
])

cars = ['Tesla','Mers','Bmw']
async def name_car():
  keybord = InlineKeyboardBuilder()
  for car in cars:
    keybord.add(InlineKeyboardButton(text=car,url='https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOKDnFvb5P89nUcqcX7fPZJg&index=11'))
  return keybord.adjust(2).as_markup() 
