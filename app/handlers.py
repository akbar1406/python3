from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
from aiogram import F, Router
import app.keyboard as kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class Reg(StatesGroup):
  name = State()
  age = State()
  number = State()


@router.message(CommandStart())
async def cmd_srt(message: Message):
   await message.answer('Welcome',
                        reply_markup=kb.first)
@router.message(Command('car'))
async def cars(message: Message):
  await message.answer('cars',
                       reply_markup=await kb.name_car())
@router.message(F.text == 'Каталог')
async def msg1(message: Message):
  await message.answer('Выберите далее',
                       reply_markup=kb.inline_catalog)
@router.message(F.photo)
async def cmd_photo(message: Message):
  await message.answer(f'ID фото {message.photo[-1].file_id} ')

@router.message(Command('get_photo'))
async def cmd_pht(message:Message):
  await message.answer_photo(photo='AgACAgIAAxkBAAPWakp5osbhTj0okguvLPG3SpcU8tEAAhEdaxvpu1BKmSsfVBClsM8BAAMCAAN5AAM8BA'
                             ,caption='logo')
  
@router.callback_query(F.data == 'back')
async def clb_back(callback:CallbackQuery):
  await callback.message.edit_text('hello',
                                   reply_markup=kb.inline_catalog)
  

@router.message(Command('reg'))
async def eee(message:Message,state:FSMContext):
  await state.set_state(Reg.name)
  await message.answer('Введите ваше имя')
@router.message(Reg.name)
async def www(message:Message,state:FSMContext):
  await state.update_data(name=message.text)
  await state.set_state(Reg.age)
  await message.answer('Сколько вам лет ?')
@router.message(Reg.age)
async def rrr(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Reg.number)
    # Создаем кнопку для отправки контакта
    contact_button = KeyboardButton(text='📱Отправить контакт', request_contact=True)
    keyboard = ReplyKeyboardMarkup(keyboard=[[contact_button]],
                                   resize_keyboard=True,
                                   one_time_keyboard=True)
    await message.answer('Нажмите кнопку, чтобы отправить номер телефона, или введите его вручную:',
                         reply_markup=keyboard)
@router.message(Reg.number)
async def ttt(message:Message,state:FSMContext):
  if message.contact:
    phone_number = message.contact.phone_number
  else:
    phone_number = message.text
  await state.update_data(number=phone_number)
  data = await state.get_data()
  await message.answer(f'Имя :{data["name"]} Возраст :{data["age"]} Контакты {data["number"]}')
  await state.clear()
