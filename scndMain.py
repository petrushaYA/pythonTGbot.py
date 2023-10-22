import time
import config
from notifiers import get_notifier

file_id = open("C:/pythonTGbot/filesForTGbot/id.txt","r" , encoding="utf-8")
file = open("C:/pythonTGbot/filesForTGbot/message_for_bot.txt", encoding="utf-8")
id_read = file_id.read()
fr = file.read()
print("текст из файла:\n",fr)

def telegram_message():
    telegram = get_notifier('telegram')
    telegram.notify(token=config.TOKEN, chat_id=id_read, message=fr)
    time.sleep(1)
    file_id.close()

#await message.delete()
#user_full_name = message.from_user.full_name
#await message.answer(f"привет, {user_full_name}!")

# @dp.message_handler(commands=["start"])
# async def start(message: types.Message):
#     await bot.send_message(chat_id=config.CHAT_ID, text=fr)

# привет на вступление в группу
# @dp.message_handler(content_types=["new_chat_members"])
# async def new_chat(message: types.Message):
#     await message.answer("добро пожаловать!")


#удалить сообщение что человек ливнул
# @dp.message_handler(content_types=["left_chat_member"])
# async def left_message_delete(message: types.Message):
#     await message.delete()


#удалить стик
# @dp.message_handler(content_types=["sticker"])
# async def sticker_delete(message: types.Message):
#     await message.delete()


# написать после сообщения
#@dp.message_handler(content_types=['text'])
# async def handle_text_photo(message: types.Message):
#     for i in range(10):
#         await message.answer("kyky")
#         time.sleep(1)

if __name__ == '__main__':
    telegram_message()


