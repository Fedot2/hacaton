from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import telebot
import constants, os, re
import emoji
import xlrd
import random
import requests
from bs4 import BeautifulSoup

TOKEN = "5377787832:AAFQTODZ1oFd_QPcUxeU8x8vAuvvsVnfH2E"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["/start", "/help"]
keyboard.add(*buttons)
data=[]

#_______________________Болтовня___________________
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["ДА!", "Ехехе... Пока ещё нет..."]
    keyboard.add(*buttons)
    await message.answer("Приветствую тебя, молодой студент! Я - такой же как и ты, студент Евлампий.\nЯ так понимаю, у тебя есть проблема? Я помогу!\nДля начала ответь, ты уже сдал ЕГЭ?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "ДА!")
async def Cpp_m(message: types.Message):
    data.append(1)
    await message.reply(
        "Ого, ну ты и умница!",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["100-150", "150-200", "200-250", "250-300", "1000-7"]
    keyboard.add(*buttons)
    await message.answer("Замечательно! Расскажи, насколько баллов ты сдал ЕГЭ?", reply_markup=keyboard)

#________________________Технический отрывок_______________________
@dp.message_handler(lambda message: message.text == "100-150")
async def Cpp_m(message: types.Message):
    data.append(1)
    await message.reply(
        "Мда... Сочувствую, но это не беда!",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да"]
    keyboard.add(*buttons)
    await message.answer("Для таких баллов тоже ВУЗов полно. Готов?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "150-200")
async def Cpp_m(message: types.Message):
    data.append(2)
    await message.reply(
        "Немного ниже среднего, конечно, однако тоже неплохо!",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да"]
    keyboard.add(*buttons)
    await message.answer("Ладно, посмотрим что можно найти. Готов?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "200-250")
async def Cpp_m(message: types.Message):
    data.append(3)
    await message.reply(
        "Не дурно! С такими баллами можно много куда поступить.)",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да"]
    keyboard.add(*buttons)
    await message.answer("Ну что-же, пойдём смотреть куда поступать?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "250-300")
async def Cpp_m(message: types.Message):
    data.append(4)
    await message.reply(
        "Очень даже хорошо! С такими баллами открыто много дорог!\n Если не все...\n\n(-_-)",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да"]
    keyboard.add(*buttons)
    await message.answer("Ну что-же, пойдём смотреть куда поступать?)", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "1000-7")
async def Cpp_m(message: types.Message):
    data.append(0)
    await message.reply(
        "(╯°□°）╯︵ ┻━┻",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да"]
    keyboard.add(*buttons)
    await message.answer("Ладно... Не важно... Давай уже перейдём к делу.\n\n(-_-)", reply_markup=keyboard)
#________________________Сново болтовня_______________________
@dp.message_handler(lambda message: message.text == "Ехехе... Пока ещё нет...")
async def Cpp_m(message: types.Message):
    data.append(0)
    await message.reply(
        "Что же... Думаю что это не так страшно, ведь у тебя ещё есть время подумать.",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Всё верно.", "Нет, я просто мимо проходил."]
    keyboard.add(*buttons)
    await message.answer("Я так понял, что ты собираешься куда либо поступать, не так ли?", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Нет, я просто мимо проходил.")
async def Cpp_m(message: types.Message):
    await message.reply(
        "Ну... Тогда проходи дальше и не задерживайся.",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Прощай!", "Э! Погоди, я передумал."]
    keyboard.add(*buttons)
    await message.answer("Твой путь только начался. Я буду молиться за тебя.", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Э! Погоди, я передумал.")
async def Cpp_m(message: types.Message):
    await message.reply(
        "О, у тебя есть что-то на уме? Решил на ВУЗы посмотреть?",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да"]
    keyboard.add(*buttons)
    await message.answer("Ну так что? Мы будем выбирать ВУЗ?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Да")
async def Cpp_m(message: types.Message):
    await message.reply(
        "Что же... Приступим.",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пока ещё нет.", "Да, я уже выбрал."]
    keyboard.add(*buttons)
    await message.answer("Ты уже определился с факультетом?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Пока ещё нет.")
async def Cpp_m(message: types.Message):
    await message.reply(
        "Эммм... Ну ладно...",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["IT", "Технический", "Хим-био", "Экономика"]
    keyboard.add(*buttons)
    await message.answer("Тогда я предложу тебе направления, а ты подумай и реши, что тебе по душе.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Да, я уже выбрал.")
async def Cpp_m(message: types.Message):
    await message.reply(
        "Моё уважение)",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["IT", "Технический", "Хим-био", "Экономика"]
    keyboard.add(*buttons)
    await message.answer("Тогда, для начала, укажи своё направление.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Всё верно.")
async def Cpp_m(message: types.Message):
    await message.reply(
        "(✷‿✷)",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["IT", "Технический", "Хим-био", "Экономика"]
    keyboard.add(*buttons)
    await message.answer("Тогда, для начала, укажи своё направление.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "IT")
async def Cpp_m(message: types.Message):
    await message.reply(
        "Крутой (⌐■_■)",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Прикладная математика и информатика", "Математика и компьютерные науки", "Информационная безопасность", "Бизнес-информатика", "Программная инженерия"]
    keyboard.add(*buttons)
    await message.answer("Теперь выбери факультет, на который ты хотел бы поступить.", reply_markup=keyboard)

#________________________________________________1/1_________________________________________
@dp.message_handler(lambda message: message.text == "Прикладная математика и информатика")
async def with_puree(message: types.Message):
    # await message.reply(text="Прости, курсы для этого языка ещё не добавлены.\nВыбери другой язык.\n\n(ಥ﹏ಥ)")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Следующий.", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 2 or data[0] == 3 or data[0] == 4 or data[0]==1:
        await message.reply(
            "Это новый университет, но у него большие перспективы.\nДанный уневерситет не имеет военной кафедры, но зато у него есть общежитие.\n"
            "https://rosnou.ru/"
            , reply_markup=keyboard)
    else:
        await message.reply(
            "Это новый уневерситет, но у него большие перспективы.\nДанный уневерситет не имеет военной уафедры, но зато у него есть общежитие.\n"
            "https://rosnou.ru/ \n\n"
            "Вряд ли ты его потянешь."
            , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Следующий.")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Следующий", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 2 or data[0] == 3 or data[0] == 4 or data[0]==1:
        await message.reply(
            "Московский политехнический университет... Звучит круто)\n"
            "https://mospolytech.ru/"
            , reply_markup=keyboard)
    else:
        await message.reply(
            "Московский политехнический университет... Звучит круто)\n"
            "https://mospolytech.ru/ \n\n"
            "Вряд ли ты его потянешь."
            , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Следующий")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Далее", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 2 or data[0] == 3 or data[0] == 4 or data[0]==1:
        await message.reply("Бауманка, она и в Африке Бауманка)))\n"
                            "https://www.bmstu.ru/"
                            , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Далее")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Дальше", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 2 or data[0] == 3 or data[0] == 4 or data[0] == 1:
        await message.reply("Если ты думаешь, что в МАИ тебя могут научить только летать, то ты сильно заблуждаешься.\n"
                            "https://mai.ru/"
                            , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Дальше")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Ещё один", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 2 or data[0] == 3 or data[0] == 4 or data[0] == 1:
        await message.reply(
            "Высшая школа экономики... Неожиданно, не так ли?)\n"
            "https://www.hse.ru/"
            , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Ещё один")
async def without_puree4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 2 or data[0] == 3 or data[0] == 4 or data[0] == 1:
        await message.reply(
            "МИРЭА - Российский технологический университет. Название говорит само за себя.\n"
            "https://www.mirea.ru/"
            , reply_markup=keyboard)

#________________________________________________1/2_________________________________________
@dp.message_handler(lambda message: message.text == "Математика и компьютерные науки")
async def with_puree(message: types.Message):
    # await message.reply(text="Прости, курсы для этого языка ещё не добавлены.\nВыбери другой язык.\n\n(ಥ﹏ಥ)")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Другой.", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 3 or data[0] == 4:
        await message.reply(
            "Санкт-Петербургский государственный университет\n"
            "https://spbu.ru/"
            , reply_markup=keyboard)
    else:
        await message.reply(
            "Санкт-Петербургский государственный университет\n"
            "https://spbu.ru/ \n\n"
            "Вряд ли ты его потянешь."
            , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Другой.")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Хочу другой", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 3 or data[0] == 4:
        await message.reply(
            "МГТУ имени Н.Э. Баумана... Ну!?\n"
            "https://www.bmstu.ru/"
            , reply_markup=keyboard)
    else:
        await message.reply(
            "МГТУ имени Н.Э. Баумана... Ну!?\n"
            "https://www.bmstu.ru/ \n\n"
            "Вряд ли ты его потянешь."
            , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Хочу другой")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Я сказал(а) хочу другой", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 3 or data[0] == 4:
        await message.reply("Национальный исследовательский Томский государственный университет\n"
                            "https://www.tsu.ru/"
                            , reply_markup=keyboard)
    else:
        await message.reply("Национальный исследовательский Томский государственный университет\n"
                            "https://www.tsu.ru/ \n\n"
                            "Вряд ли ты его потянешь."
                            , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Я сказал(а) хочу другой")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["...", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 3 or data[0] == 4:
        await message.reply("Российский университет дружбы народов?\n"
                            "https://www.rudn.ru/"
                            , reply_markup=keyboard)
    else:
        await message.reply("Российский университет дружбы народов?\n"
                            "https://www.rudn.ru/ \n\n"
                            "Вряд ли ты его потянешь."
                            , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "...")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    if data[0] == 0 or data[0] == 3 or data[0] == 4:
        await message.reply(
            "Санкт-Петербургский политехнический университет Петра Великого. Больше мне нечего предложить...\n"
            "https://www.spbstu.ru/"
            , reply_markup=keyboard)
    else:
        await message.reply(
            "Санкт-Петербургский политехнический университет Петра Великого. Больше мне нечего предложить...\n"
            "https://www.spbstu.ru/ \n\n"
            "Вряд ли ты его потянешь."
            , reply_markup=keyboard)

#________________________________________________1/3_________________________________________
@dp.message_handler(lambda message: message.text == "Информационная безопасность")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Не этот", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Национальный исследовательский университет 'Высшая школа экономики'\n"
        "https://www.hse.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Не этот")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["И не этот", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Национальный исследовательский ядерный университет. Что скажешь?\n"
        "https://mephi.ru/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "И не этот")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Опять мимо", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Московский политехнический университет\n"
                        "https://mospolytech.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Опять мимо")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Всё ещё нет", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Национа́льный иссле́довательский университе́т\n"
                        "https://www.miet.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Всё ещё нет")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский технический университет связи и информатики. Больше мне нечего предложить...\n"
        "https://mtuci.ru/"
        , reply_markup=keyboard)

#________________________________________________1/4_________________________________________
@dp.message_handler(lambda message: message.text == "Бизнес-информатика")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Nope...", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Very good! Так сказать)))\n"
        "https://misis.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Nope...")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["NOPE.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "РГУ нефти и газа (НИУ) имени И.М. Губкина\n"
        "https://www.gubkin.ru/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "NOPE.")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["NOPE!", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("МГТУ им. Н.Э. Баумана\n"
                        "https://www.bmstu.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "NOPE!")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["NO!", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Московский политехнический университет\n"
                        "https://mospolytech.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "NO!")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский технический университет связи и информатики. Больше мне нечего предложить...\n"
        "https://mtuci.ru/"
        , reply_markup=keyboard)

#________________________________________________1/5_________________________________________
@dp.message_handler(lambda message: message.text == "Программная инженерия")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Неть", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский авиационный институт\n"
        "https://mai.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Неть")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Нееть", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Российский государственный социальный университет\n"
        "https://rgsu.net/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Нееть")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["НЕЕЕЕТЬ!", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("МГТУ им. Н.Э. Баумана\n"
                        "https://www.bmstu.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "НЕЕЕЕТЬ!")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["АААААААААА", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Московский государственный технологический университет «СТАНКИН»\n"
                        "https://stankin.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "АААААААААА")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "МИРЭА - Российский технологический университет. Больше мне нечего предложить...\n"
        "https://www.mirea.ru/"
        , reply_markup=keyboard)

#__________________________Хим-био____________________
@dp.message_handler(lambda message: message.text == "Хим-био")
async def Cpp_m(message: types.Message):
    await message.reply(
        "Ха-ха! Ботан ʕ•ᴥ•ʔ",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Химическая технология", "Материаловедение и технологии материалов", "Биотехнология", "Биоинженерия и биоинформатика", "Врачебное дело"]
    keyboard.add(*buttons)
    await message.answer("Теперь выбери факультет, на который ты хотел бы поступить.", reply_markup=keyboard)

#________________________________________________2/1_________________________________________
@dp.message_handler(lambda message: message.text == "Материаловедение и технологии материалов")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Предложи что-то другое", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Национальный исследовательский технологический университет «МИСиС»\n"
        "https://misis.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Предложи что-то другое")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский Политехнический. Больше мне нечего предложить...\n"
        "https://mospolytech.ru/"
        , reply_markup=keyboard)


#________________________________________________2/2_________________________________________
@dp.message_handler(lambda message: message.text == "Химическая технология")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский политехнический университет\n"
        "https://mospolytech.ru/"
        , reply_markup=keyboard)


#________________________________________________2/3_________________________________________
@dp.message_handler(lambda message: message.text == "Биотехнология")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не нравится, давай дальше.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский политехнический университет\n"
        "https://mospolytech.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Мне не нравится, давай дальше.")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Национальный исследовательский технологический университет «МИСиС»\n"
        "https://misis.ru/"
        , reply_markup=keyboard)


#________________________________________________2/4_________________________________________
@dp.message_handler(lambda message: message.text == "Биоинженерия и биоинформатика")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский государственный университет имени М.В.Ломоносова\n"
        "https://conf.msu.ru/rus/event/7500/"
        , reply_markup=keyboard)

#________________________________________________2/5_________________________________________
@dp.message_handler(lambda message: message.text == "Врачебное дело")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не нравится, давай дальше.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Российский национальный исследовательский медицинский университет имени Н. И. Пирогова\n"
        "https://rsmu.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Мне не нравится, давай дальше.")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Национальный исследовательский технологический университет «МИСиС»\n"
        "https://misis.ru/"
        , reply_markup=keyboard)

#______________________Технический_____________________
@dp.message_handler(lambda message: message.text == "Технический")
async def Cpp_m(message: types.Message):
    await message.reply(
        "Ух ты! ジ",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Бизнес-информатика", "Информатика и вычислительная техника", "Автоматизация технологических процессов и производств", "Информационная безопасность"]
    keyboard.add(*buttons)
    await message.answer("Теперь выбери факультет, на который ты хотел бы поступить.", reply_markup=keyboard)

#______________________3\1_____________________________
@dp.message_handler(lambda message: message.text == "Автоматизация технологических процессов и производств")
async def with_puree(message: types.Message):
    # await message.reply(text="Прости, курсы для этого языка ещё не добавлены.\nВыбери другой язык.\n\n(ಥ﹏ಥ)")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Другой.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Санкт-Петербургский государственный университет\n"
        "https://spbu.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Другой.")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Хочу другой", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "МГТУ имени Н.Э. Баумана... Ну!?\n"
        "https://www.bmstu.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Хочу другой")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Я сказал(а) хочу другой", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Национальный исследовательский Томский государственный университет\n"
                        "https://www.tsu.ru/"
                        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Я сказал(а) хочу другой")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["...", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Российский университет дружбы народов?\n"
                        "https://www.rudn.ru/"
                        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "...")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Санкт-Петербургский политехнический университет Петра Великого. Больше мне нечего предложить...\n"
        "https://www.spbstu.ru/"
        , reply_markup=keyboard)

#________________________________________________3/2_________________________________________
@dp.message_handler(lambda message: message.text == "Информатика и вычислительная техника")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Не этот", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Национальный исследовательский университет 'Высшая школа экономики'\n"
        "https://www.hse.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Не этот")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["И не этот", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Национальный исследовательский ядерный университет. Что скажешь?\n"
        "https://mephi.ru/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "И не этот")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Опять мимо", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Московский политехнический университет\n"
                        "https://mospolytech.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Опять мимо")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Всё ещё нет", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Национа́льный иссле́довательский университе́т\n"
                        "https://www.miet.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Всё ещё нет")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский технический университет связи и информатики. Больше мне нечего предложить...\n"
        "https://mtuci.ru/"
        , reply_markup=keyboard)

#________________________________________________3/3_________________________________________
@dp.message_handler(lambda message: message.text == "Бизнес-информатика")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Nope...", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Very good! Так сказать)))\n"
        "https://misis.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Nope...")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["NOPE.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "РГУ нефти и газа (НИУ) имени И.М. Губкина\n"
        "https://www.gubkin.ru/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "NOPE.")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["NOPE!", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("МГТУ им. Н.Э. Баумана\n"
                        "https://www.bmstu.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "NOPE!")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["NO!", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Московский политехнический университет\n"
                        "https://mospolytech.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "NO!")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский технический университет связи и информатики. Больше мне нечего предложить...\n"
        "https://mtuci.ru/"
        , reply_markup=keyboard)

#________________________________________________3/4_________________________________________
@dp.message_handler(lambda message: message.text == "Информационная безопасность")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Неть", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский авиационный институт\n"
        "https://mai.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Неть")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Нееть", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Российский государственный социальный университет\n"
        "https://rgsu.net/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Нееть")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["НЕЕЕЕТЬ!", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("МГТУ им. Н.Э. Баумана\n"
                        "https://www.bmstu.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "НЕЕЕЕТЬ!")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["АААААААААА", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Московский государственный технологический университет «СТАНКИН»\n"
                        "https://stankin.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "АААААААААА")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "МИРЭА - Российский технологический университет. Больше мне нечего предложить...\n"
        "https://www.mirea.ru/"
        , reply_markup=keyboard)


#______________________Экономика_____________________
@dp.message_handler(lambda message: message.text == "Экономика")
async def Cpp_m(message: types.Message):
    await message.reply(
        "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]",
        reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Менеджмент", "Управление персоналом", "Бизнес-информатика", "Государственное и муниципальное управление"]
    keyboard.add(*buttons)
    await message.answer("Теперь выбери факультет, на который ты хотел бы поступить.", reply_markup=keyboard)

#________________________________________________4/1_________________________________________
@dp.message_handler(lambda message: message.text == "Бизнес-информатика")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Nope...", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Very good! Так сказать)))\n"
        "https://misis.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Nope...")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["NOPE.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "РГУ нефти и газа (НИУ) имени И.М. Губкина\n"
        "https://www.gubkin.ru/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "NOPE.")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["NOPE!", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("МГТУ им. Н.Э. Баумана\n"
                        "https://www.bmstu.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "NOPE!")
async def without_puree2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["NO!", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Московский политехнический университет\n"
                        "https://mospolytech.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "NO!")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский технический университет связи и информатики. Больше мне нечего предложить...\n"
        "https://mtuci.ru/"
        , reply_markup=keyboard)

#________________________________________________4/2_________________________________________
@dp.message_handler(lambda message: message.text == "Менеджмент")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Давай дальше смотреть", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский университет им. С.Ю. Витте\n"
        "https://www.muiv.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Давай дальше смотреть")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Продолжай, ещё есть предложения?", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский гуманитарно-экономический университет\n"
        "https://mgei.ru/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Продолжай, не задерживайся")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Ну... Что-то не очень... Давай другой.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Российская академия народного хозяйства и государственной службы\n"
                        "https://www.ranepa.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Ну... Что-то не очень... Давай другой.")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский архитектурно-строительный институт. Больше мне нечего предложить...\n"
        "https://masi.ru/"
        , reply_markup=keyboard)

#________________________________________________4/3_________________________________________
@dp.message_handler(lambda message: message.text == "Управление персоналом")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Нет, мне не нравится...", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Это новый уневерситет, но у него большие перспективы.\nДанный уневерситет не имеет военной уафедры, но зато у него есть общежитие.\n"
        "https://rosnou.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Нет, мне не нравится...")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне всё ещё не нравится", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский университет им. С.Ю. Витте\n"
        "https://www.muiv.ru/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Мне всё ещё не нравится")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["НЕТ, МНЕ НЕ НРАВИТСЯ", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("РГУ им. Косыгина\n"
                        "https://kosygin-rgu.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "НЕТ, МНЕ НЕ НРАВИТСЯ")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Финансовый университет при Правительстве Российской Федерации\n"
        "http://www.fa.ru/Pages/Home.aspx"
        , reply_markup=keyboard)

#________________________________________________4/4_________________________________________
@dp.message_handler(lambda message: message.text == "Государственное и муниципальное управление")
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Нет, мне не хочется в этот институт", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "МИРЭА - Российский технологический университет. Название говорит само за себя.\n"
        "https://www.mirea.ru/"
        , reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Нет, мне не хочется в этот институт")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Ну уж нет!", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский архитектурно-строительный институт. Больше мне нечего предложить...\n"
        "https://masi.ru/"
        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Ну уж нет!")
async def without_puree1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Нет, мне не подходит, он не такой как я хочу", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply("Институт мировых цивилизаций\n"
                        "http://imc-i.ru/"
                        , reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Нет, мне не подходит, он не такой как я хочу")
async def without_puree3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Мне не подошли эти вузы.", "Мне нравится!"]
    keyboard.add(*buttons)
    await message.reply(
        "Московский университет им. С.Ю. Витте\n"
        "https://www.muiv.ru/"
        , reply_markup=keyboard)

#__________________________end_____________________
@dp.message_handler(lambda message: message.text == "Мне не подошли эти вузы.")
async def without_puree(message: types.Message):
    await message.answer(
        "Прости, но это всё что я могу. Возможно, в будущем я стану получше...\n")
@dp.message_handler(lambda message: message.text == "Мне нравится!")
async def without_puree(message: types.Message):
    await message.answer(
        "Замечательно!.\n Я безумно рад. (｡◕‿◕｡) \n\nЧто-же, теперь ты можешь идти дальше и жить как тебе подсказывает сердце, а на этом моя работа закончена.\nПрощай. \n\n(づ｡◕‿‿◕｡)づ")


@dp.message_handler(commands=['help'])
async def send_welcome(msg: types.Message):
    await msg.answer('Боюсь вас огорчить, но помощи не будет, пока что...')


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    await msg.answer('Не понимаю, что это значит. ¯\_(ツ)_/¯ ')


if __name__ == '__main__':
    executor.start_polling(dp)
