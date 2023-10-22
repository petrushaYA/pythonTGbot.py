import config
from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

file_id = open("C:/pythonTGbot/filesForTGbot/id.txt","w", encoding="utf-8")
@dp.message_handler(commands=["start"])
async def def_start(message: types.Message):
    chat_id = str(message.chat.id)
    print(chat_id)
    file_id.write(chat_id)
    file_id.close()
    with open("config.py", "w") as config_file:
        config_file.write(f"TOKEN = '{config.TOKEN}'\n")
        config_file.write(f"CHAT_ID = '{chat_id}'")
    return()

if __name__ == '__main__':
    executor.start_polling(dp)


