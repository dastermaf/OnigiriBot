import config
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from db import Database


#Configs/Head
db = Database("database.dp")
bot = Bot(token=config.token)
dp = Dispatcher(bot)

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

@dp.message_handler(commands=['mute'])
async def mute(message: types.Message):
	if str(message.from_user.id) == config.ADMIN_ID:
		if not message.reply_to_message:
			await message.reply("Чигаи. Должен быть ответом на сообщение.")
		return
	mute_sec = int(meaage.text[6:])
	db.add_mute(message.reply_to_message.from_user.id, mute_sec)
	await message_reply_to_message.reply(f"Пользователь забанен на {mute_sec} секунд")

#Filter/Shoulders
@dp.message_handler()
async def filter_message(message: types.Message):
	if message.text.lower() in words:
		await message.delete()

	if not db.examination(message.from_user.id):
		db.add(message.from_user.id)
	if not db.mute(message.from_user.id):
		print ("/")
	else:
		await message.delete()


#Hello/Bye/Shoulders
@dp.message_handler(content_types=["new_chat_members"])
async def new_chat(message: types.Message):
	await message.answer("Охайоу Гозаимас!")

@dp.message_handler(content_types=["left_chat_member"])
async def left_chat(message: types.Message):
	await message.delete()

#Moderation/Ohers/Body
#@dp.message_handler()
#async def echo_send(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)

#Main/Down
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)    