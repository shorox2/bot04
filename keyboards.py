from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('Random photo')
b4 = KeyboardButton('/location')
b5 = KeyboardButton('/vote')
kb.add(b1, b2).add(b3, b4)
rkb = ReplyKeyboardRemove()

kpb = ReplyKeyboardMarkup(resize_keyboard=True)
kp1 = ('Рандoм')
kp2 = ('Назад')
kpb.add(kp1, kp2)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='👍', callback_data= "like")
ib2 = InlineKeyboardButton(text='👎', callback_data= "dislike")
ib3 = InlineKeyboardButton(text='➡️', callback_data='next')
ib4 = InlineKeyboardButton(text = 'go back', callback_data="back")
ikb.add(ib1, ib2).add(ib3).add(ib4)

