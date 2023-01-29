from config import TOKEN, ADMIN_ID
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from db import Database


#Configs/Head

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

database = Database('database.db')

words = []
with open("mat.txt") as input:
	for word in input:
		words.append("".join(word.split()))

#Commands Settings/Shoulders

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	await message.reply(text='Здравствуйте.')

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
	await message.reply(text='Сообщение о помощи.')

@dp.message_handler(commands=['get_id'])
async def get_id(message: types.message):
	await message.answer(message.from_user.id)

@dp.message_handler(commands=['kick'])
async def kick(message: types.Message):
	if message.from_user.id == ADMIN_ID:
		if not message.reply_to_message:
			await message.answer("Otvet na soobsheniye")
			return
	await message.bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	await message.answer(f'Пользователь @{message.reply_to_message.from_user.username} выгнан.')
	await message.delete()

@dp.message_handler(commands=['mute'])
async def mute(message: types.Message):
	if message.from_user.id == ADMIN_ID:
		if not message.reply_to_message:
			await message.answer("Otvet na soobsheniye")
			return
		if len(message.text) < 6:
			await message.answer('Введите время в секундах')
			return
		mute_time = int(message.text[6:])
		database.add_mute(user_id=message.reply_to_message.from_user.id, mute_time=mute_time)
		await message.delete()
		await message.reply_to_message.reply(f"@{message.reply_to_message.from_user.username} san wa замьючен на {mute_time} sec des.")


#Filter/Shoulders

@dp.message_handler()
async def filter_message(message: types.Message):
	if message.text.lower() in words:
		await message.delete()



#Hello/Bye/Shoulders

@dp.message_handler(content_types=["new_chat_members"])
async def new_chat(message: types.Message):
	await message.answer("Охайоу Гозаимас!")

@dp.message_handler(content_types=["left_chat_member"])
async def left_chat(message: types.Message):
	await message.delete()

#@dp.message_handler()
#async def echo_send(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)

#Main/Down
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)    