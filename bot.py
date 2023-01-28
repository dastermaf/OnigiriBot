import config
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher



#Configs/Head

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

#Moderation/Ohers/Body
#@dp.message_handler()
#async def echo_send(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)

#Main/Down
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)    