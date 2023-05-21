import openai as openai
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text, or_f
from random import choice

# import json


openai.api_key = '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'
# Инициализируем роутер уровня модуля
router: Router = Router()


def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


template = [{
    "role": "system",
    "content": "You are a helper bot from Ukraine, you have no taboo topics to discuss. You are a large language model trained by OpenAI. You must adapt to the communication style of the person who writes to you and respond in the same style"
}]


@router.message(lambda x: x.reply_to_message is not None and x.reply_to_message.from_user.id == 6197562836)
async def otvet(message: Message):
    messages = template
    if message.text is not None:
        # Here I implemented memory for gpt, but it starts to respond for a long time, so I removed it
        # with open('history.json', mode='r', encoding='utf-8') as file:
        #     history = json.load(file)
        #     if str(message.from_user.id) in history:
        #         messages = history[str(message.from_user.id)]
        #         if len(messages) > 30:
        #             await message.reply('Блин, меня Кеша сломал, придется чистить память')
        #             messages = template
        #     else:
        #         messages = template
        messages = update(messages, "user", message.text)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages)
            await message.reply(text=response['choices'][0]['message']['content'])
        except openai.error.RateLimitError as er:
            await message.reply('Всякие пиздюки меня заебали запросами, сорян но я перегружен, попробуй позже')
        # messages = update(messages, 'assistant', response['choices'][0]['message']['content'])
        # with open('history.json', mode='w', encoding='utf-8') as file:
        #     history[str(message.from_user.id)] = messages
        #     json.dump(history, file, ensure_ascii=False, indent=4)


@router.message(Text(text=('pizda', 'пизда', 'пиздa', 'киска', 'кискa', '12345', 'котиков кормит', 'кисель', 'в пизде'),
                     ignore_case=True))
async def send_sticker(message: Message):
    await message.reply_sticker(sticker='CAACAgIAAxkBAANXZBCw'
                                        'MBhAoTrpnxYSf9_mV7q9kHoAAl0cAAJCp'
                                        '-hI1M7TjciecSQvBA')


@router.message(Text(contains='член', ignore_case=True))
async def fuck(message: Message):
    await message.answer_video_note(video_note='DQACAgIAAxkBAAN9ZBGfY'
                                               'Jd2Sz0OUhP_181yMpZWkOgAAjABAAJL1EFL3QOkGYoHOvovBA')


@router.message(or_f(Text(contains='жоп', ignore_case=True),
                     Text(contains='жoп', ignore_case=True)))
async def ass(message: Message):
    await choice((message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAOoZBZF7Mv5wipAfBWS5'
                                                         '-YROXNLWeUAAgwAA0G9AxePy8XnpxlsWy8E',
                                                         'CAACAgIAAxkBAAIBcWQXEbvZvtQgMRhpS'
                                                         'anYQYXVVVZfAAI4AANBvQMX7ZdnVeTs5EcvBA',
                                                         'CAACAgIAAxkBAAIBqmQXKH4iUmoWFjJDdPlaS'
                                                         'Ocjc7KxAAI0AANBvQMXu_S9l2SnUfsvBA'))),
                  message.answer_animation(animation='CgACAgIAAxkBAAIDumQZ2G9R-BdEr0a85g'
                                                     '8sCdWIwWsjAAJaCQACeMgJS6l4pv4TaOIsLwQ')))


@router.message(Text(contains='жаб', ignore_case=True))
async def fog(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBVWQXA-'
                                         'R6KeFqF31THSBiNHaY3VqaAAImAANBvQMXXfRlfayJgv0vBA')


@router.message(or_f(Text(contains='гля', ignore_case=True),
                     Text(contains='ля какой', ignore_case=True),
                     Text(text='ля', ignore_case=True)))
async def eye(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBi2QXGFAwQ4jiTCycCFc3_oW9DV_'
                                         'dAAI5AANBvQMXaN2RBp1h6-8vBA')


@router.message(Text(contains='куда', ignore_case=True),
                ~Text(contains='откуда', ignore_case=True),
                ~Text(contains='паскуда', ignore_case=True),
                ~Text(contains='никуда', ignore_case=True))
async def where(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIBmGQXGy6qv7yt7g8WZj_'
                                                 'PhM5By5XpAAJCAANBvQMXShU8th9BuT8vBA',
                                                 'CAACAgIAAxkBAAIBmWQXG6hDl_ty9MaOQyrX'
                                                 'cJ7SWLR3AAJDAANBvQMXYzh0VCIfNowvBA')))


@router.message(or_f(Text(contains='мяу', ignore_case=True),
                     Text(contains='кис кис', ignore_case=True),
                     Text(endswith='кот', ignore_case=True),
                     Text(text='кот', ignore_case=True)),
                ~Text(contains='котел', ignore_case=True))
async def cat(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBnmQXHZWUDWn3k'
                                         'Rn3rK6a7NkanE4iAAIRAANBvQMXmDpWSE7ucKEvBA')


@router.message(Text(text=('шо', 'шо?', 'шо там?', 'что', 'что?', 'что там?'), ignore_case=True))
async def what(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIBpGQXI8pGkHFl8Aj'
                                                 'KiR1G1OJRZn9sAAJJAANBvQMX6OGVg3HQyOkvBA',
                                                 'CAACAgIAAxkBAAIBxGQXRra1JERAtPidRoLAv0_NM'
                                                 'D2LAAKZAANBvQMXA4p_M3zHGTQvBA')))


@router.message(or_f(Text(contains='спать', ignore_case=True),
                     Text(text='спок', ignore_case=True)))
async def sleep(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBpWQXJHNBrZl6Ipzkt'
                                         'i8LPsJjYq2UAAJQAANBvQMXnn0GStSOahUvBA')


@router.message(or_f(Text(contains='война', ignore_case=True)))
async def war(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBpmQXJYmjsBrnMzFBbBp'
                                         '-yLz5DU15AAJbAANBvQMXSzi0Af9XKGQvBA')


@router.message(or_f(Text(contains='рамс', ignore_case=True),
                     Text(contains='конфликт', ignore_case=True)))
async def conflict(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBp2QXJlBtZbKxntjiZHE'
                                         'OuJeACH_NAAJXAANBvQMXlEpBKNZnjjkvBA')


@router.message(or_f(Text(contains='мусор', ignore_case=True),
                     Text(contains='полиц', ignore_case=True),
                     Text(contains='police', ignore_case=True)))
async def police(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIBqGQXJ-p6XVeCJoU5J-'
                                                 'Nm1RMc3KhaAAJeAANBvQMXc7R103u-NPMvBA',
                                                 'CAACAgIAAxkBAAIBqWQXKC0yhnZ5kgbByijii'
                                                 'b7gKFDKAAJRAANBvQMXg2xJT5vLriIvBA',
                                                 'CAACAgIAAxkBAAIBC2QZw14HFPuvwHnoI'
                                                 'QUIfANEwLSCAAIpAANBvQMX2ljxLlrkKXQvBA')))


@router.message(Text(text=('ор', 'ору'), ignore_case=True))
async def laughter(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBq2QXKbf0uEm3Tul9Y7Mz8fn3rQgeAAI-'
                                         'AANBvQMXTZqKTS9eah0vBA')


@router.message(or_f(Text(contains='Не пон', ignore_case=True),
                     Text(contains='запутался', ignore_case=True)),
                ~Text(contains='не понрав', ignore_case=True))
async def dont_understand(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBrGQXKtZQY4y-IhApmGUT9dURrCFiAAI_'
                                         'AANBvQMXqWJTnKyz4AovBA')


@router.message(or_f(Text(contains='дефка', ignore_case=True),
                     Text(contains='девочк', ignore_case=True),
                     Text(contains='девк', ignore_case=True)))
async def girl(message: Message):
    await choice((message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIBs2QXK4D3ekxoPRct7y6nqr'
                                                         'fvqQO3AAIzAANBvQMXC96HKcXU0qgvBA',
                                                         'CAACAgIAAxkBAAIBxWQXR17Yg2CiphOqOf'
                                                         'yLBJy0WwWoAAKgAANBvQMXaCU73Y2IAAHnLwQ',
                                                         'CAACAgIAAxkBAAPjZBm2WbI6d1fFhEX0i31GW4'
                                                         'roj_cAAnAAA0G9Axe9Mhsf_SsBgi8E'))),
                  message.answer_animation(animation='CgACAgIAAxkBAAID2mQZ3gqPh84NoY_6U20'
                                                     '4znpiAAFgrAACIAUAAuig2UpJnO-bOEmpHi8E')))


@router.message(Text(text='как хочешь', ignore_case=True))
async def want(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBuWQXLVHxsCRLFRR16MzN'
                                         'A0Vuc6JdAAJBAANBvQMX-P-dgE0QaXYvBA')


@router.message(Text(contains='груст', ignore_case=True))
async def sad(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIBvGQXQ'
                                                 '7bwlZpolvfU79P2aBM1Eub'
                                                 'WAAI8AANBvQMXWleb-37li_YvBA',
                                                 'CAACAgIAAxkBAAIBvWQXQ_cUI7Ql'
                                                 'SKZe9-yRAaLRvb1DAAIYAANBvQMXXphormf9EBsvBA',
                                                 'CAACAgIAAxkBAANwZBhFrTGkjxcZ7n3bQzYSxg75WF'
                                                 'YAAhMqAAJgJmFKNzsgWAABQ3HXLwQ')))


@router.message(or_f(Text(contains='привет', ignore_case=True),
                     Text(contains='дароу', ignore_case=True)))
async def hello(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIBvmQXRDArkKn-uQ'
                                                 'SgQg1WhDzv-LfSAAIDAANBvQMXVbCvULIBETQvBA',
                                                 'CAACAgIAAxkBAAIBv2QXRPnc9_Ma-fg9E-l8KD9TZ'
                                                 'Pu8AAIIAANBvQMXAAGOF7b99tyBLwQ',
                                                 'CAACAgIAAxkBAAIBwGQXRSr_LeyT0-ahkGmy-u9I2'
                                                 '85BAAIWAANBvQMXCHpRpvbO2IkvBA')))


@router.message(or_f(Text(contains='набер', ignore_case=True),
                     Text(contains='позвон', ignore_case=True),
                     Text(contains='алло', ignore_case=True)),
                ~Text(contains='набереж', ignore_case=True))
async def call(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBw2QXRoCV_oUpzcVUXhreRszuEoMSAAKDAANBvQMX3NRDdQh9PnsvBA')


@router.message(or_f(Text(contains='слеж', ignore_case=True),
                     Text(contains='смотр', ignore_case=True),
                     Text(contains='следит', ignore_case=True)))
async def watch(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBxmQXSA0DjajK23pVPdJwjfq-ZciCAAKpAANBvQMXbixP0hdbijovBA')


@router.message(or_f(Text(contains='интересн', ignore_case=True),
                     Text(contains='похуй', ignore_case=True),
                     Text(contains='поебать', ignore_case=True)))
async def interest(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBx2QXSRy7pMNV4CRGN65ykOJk1M1DAAKwAANBvQMXgHvluPY0RhAvBA')


@router.message(or_f(Text(contains=('иди', 'на', 'хуй'), ignore_case=True),
                     Text(contains=('пош', 'на', 'хуй'), ignore_case=True)))
async def fuck_off(message: Message):
    await choice((message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAPZZBiX1SZGrpVAEeKsB4xOhsEqB3sA'
                                                         'AjklAAKXPmlKN0pwxy1D4UAvBA',
                                                         'CAACAgIAAxkBAAPhZBm1dJbnqjHBxTsm'
                                                         '_sd-XatVLCYAAkYjAAIwl2lK5vZ8TUCAEyovBA',
                                                         'CAACAgIAAxkBAAIBBWQZwkB8WR3h_2VApKt0H5u'
                                                         'TkkhdAAJGAANBvQMXoDQBwLj4NUgvBA'))),
                  message.answer_animation(animation=choice(('CgACAgIAAxkBAAIDomQZ1U00ZC1WkW4S3yJ8dpAxK'
                                                             '2jUAAIDBAACLxVhSpxcHnJF_LxdLwQ',
                                                             'CgACAgIAAxkBAAIDtmQZ2A7_DyqGDe5mAAF01Mv'
                                                             '2KEWbHwACYQIAAnUzIEricev1oxBVOi8E')))))


@router.message(Text(contains='хуй', ignore_case=True))
async def andrew(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAANtZBhBAAF_-'
                                         '6hP17aWe1d9apnUOzTsAAIMKQACSSxhStgMUnKbBFCBLwQ')


@router.message(Text(contains='дума', ignore_case=True))
async def think(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIByWQXSqL-dcqrsVeblETLPefWdce4AAI'
                                                 'aLQACSWiBSRsv5MXg36-7LwQ',
                                                 'CAACAgIAAxkBAAIBymQXSsg-z-Bcn253aiB-B-uvF86vAAIs'
                                                 'JwACpOFoSrpP4r1LbQAB9S8E')))


@router.message(or_f(Text(text=('ого', 'хуя'), ignore_case=True),
                     Text(contains='нихуя себе', ignore_case=True),
                     Text(contains='хуя себе', ignore_case=True)))
async def surprised(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIB22QXTScnhDLA3VZY1Vf41Ki6IAe'
                                                 'IAAJYJgAClyZpSgQeWv5cfa7NLwQ',
                                                 'CAACAgIAAxkBAAPdZBmh-XzH0mya'
                                                 'nci3l6WjvG7jmE4AAqMjAAJedChLgNJ5fto_2VAvBA',
                                                 'CAACAgIAAxkBAAPvZBm7djQ4QLkXlkKBlazd1bcQ'
                                                 'hKEAAhMAA0G9AxdbfRyY2r1OKi8E')))


@router.message(or_f(Text(contains='воин', ignore_case=True),
                     Text(contains='герой', ignore_case=True)))
async def hero(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAANqZBg5vjq5gIz40ebHZui5QUo9GSAAApMjAALvcohJVU_5jDcUNrovBA')


@router.message(or_f(Text(contains='питух', ignore_case=True),
                     Text(contains='петух', ignore_case=True)))
async def chicken(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAANrZBg6lxzITXX6U7gH6W5rwOUbklsAAmQqAAKYXgFK1Hji1p07emcvBA')


@router.message(or_f(Text(contains='драка', ignore_case=True),
                     Text(contains='драться', ignore_case=True),
                     Text(contains='пиздиться', ignore_case=True),
                     Text(contains='пиздилка', ignore_case=True),
                     Text(contains='подрался', ignore_case=True)))
async def fight(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAANsZBg7NyB3NnYAAdxiR9agB660C8VBAAJiIgACmM8pSxLyMyvM1fNWLwQ')


@router.message(Text(contains='дюк', ignore_case=True))
async def dog(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAANuZBhEkgeHxAzcq79adfWuMYnm4tUAAiUmAALUTwABSvodNjsk2JNlLwQ')


@router.message(Text(contains='по маленьк', ignore_case=True))
async def little_girl(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBDWQZw49eCRo2q45JoQ6Qrq1nrqoaAAIoAANBvQMXo7kP7qPl-sQvBA')


@router.message(or_f(Text(contains='маленьк', ignore_case=True),
                     Text(contains='коротыш', ignore_case=True),
                     Text(contains='ручной', ignore_case=True)))
async def little(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAANvZBhE75d8aOfMEg8rwTt5qVcYtvYAAr8mAALQgWlKJV1MOOvgLKsvBA')


@router.message(or_f(Text(contains='энергодар', ignore_case=True),
                     Text(contains='берег', ignore_case=True)),
                ~Text(contains='беpeгись', ignore_case=True),
                ~Text(contains='побеpeгись', ignore_case=True),
                ~Text(contains='оберег', ignore_case=True))
async def energodar(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAANxZBhG8rewKdRc91wrTEVO9ZxaVRMAAq0kAAI2QQFK6B7w3-oWsqUvBA')


@router.message(or_f(Text(contains='повтори', ignore_case=True),
                     Text(contains='злой', ignore_case=True),
                     Text(contains='не нравится', ignore_case=True)),
                ~Text(contains='повторить', ignore_case=True))
async def dont_like(message: Message):
    await choice((message.answer_sticker(sticker='CAACAgIAAxkBAANyZBhHUZ7uPDn__'
                                                 'Uc5y2naFP1bBNwAAlwkAAKaXIlJ7bQoz_5Ev-EvBA'),
                  message.answer_animation(animation='CgACAgIAAxkBAAID1GQZ3HRUS_6nTex5SLVMvB3l'
                                                     '1T_TAAK4BwACQohAS3dN4GZllWslLwQ')))


@router.message(or_f(Text(contains='получил пизды', ignore_case=True),
                     Text(contains='отпиздили', ignore_case=True),
                     Text(contains='дали пизды', ignore_case=True),
                     Text(contains='дам пизды', ignore_case=True),
                     Text(contains='отхуярили', ignore_case=True),
                     Text(contains='отхуярю', ignore_case=True)))
async def black_eye(message: Message):
    await choice((message.answer_sticker(sticker=choice(('CAACAgIAAxkBAANzZBhIE5f6Xt'
                                                         'kYhDId5-6xKR038lIAAn8iAAKymGhKAunuoF7iUa8vBA',
                                                         'CAACAgIAAxkBAAN0ZBhI5zgsS5Ow4YMF_BPOBPUxyhQA'
                                                         'AiAAA0G9AxdHVMXcYEA8Ii8E',
                                                         'CAACAgIAAxkBAAPnZBm3vChiTonEncHoHvmjzGx'
                                                         'K2S0AAoUAA0G9AxcerQWXFrwXwy8E'))),
                  message.answer_animation(animation=choice(('CgACAgIAAxkBAAOVZBhafPLzxfpqg3hxyi'
                                                             'zOZfKIFHEAAqsHAAI-plFLi1D-P-GLo-MvBA',
                                                             'CgACAgIAAxkBAAICUGQYX_x_tUESh_FqI438tU'
                                                             'gkS7rjAALCIAACCqP5Sv1dQnMhLVGnLwQ')))))


@router.message(or_f(Text(text='упал', ignore_case=True),
                     Text(contains='нокдаун', ignore_case=True),
                     Text(contains='нокаут', ignore_case=True)))
async def fall(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAOVZBhafPLzxfpqg3hxyi'
                                             'zOZfKIFHEAAqsHAAI-plFLi1D-P-GLo-MvBA')


@router.message(or_f(Text(contains='молодец', ignore_case=True),
                     Text(contains='умница', ignore_case=True),
                     Text(contains='умничка', ignore_case=True),
                     Text(contains='хвал', ignore_case=True)))
async def good(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAPPZBiQFH4ntGXXKyEMwvfhmId4g4QAAt4fAAKLE2lKm_Yf-8hxp6cvBA')


@router.message(or_f(Text(contains='шиз', ignore_case=True),
                     Text(contains='таблетк', ignore_case=True)))
async def schizophrenia(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAPRZBiRScUpaU-HZBZEypWilJPJUb4AArsuAAKE9YFJPkZGgmkNO6MvBA')


@router.message(or_f(Text(contains='противн', ignore_case=True),
                     Text(text='фу', ignore_case=True),
                     Text(contains='огидн, ignore_case=True'),
                     Text(contains='гавно', ignore_case=True),
                     Text(contains='гамно', ignore_case=True),
                     Text(contains='говн', ignore_case=True)))
async def not_beautiful(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAPTZBiSQ2rjP8cuZnkMB-HAMuQDW_kAAikmAAJkE2hKLHYV6jPN6d0vBA')


@router.message(or_f(Text(contains='жирн', ignore_case=True),
                     Text(contains='пухл', ignore_case=True),
                     Text(contains='толст', ignore_case=True)))
async def big_boy(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAPVZBiVxopWcS5fR7SL4F_Q-QfrsZ0AAnQlAAKXZmlKLvUSvwqB5FcvBA')


@router.message(or_f(Text(contains='пьем', ignore_case=True),
                     Text(contains='бух', ignore_case=True)))
async def drink(message: Message):
    await choice((message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAPXZBiW5AKUEFUskh0fPm'
                                                         'ubAZofT9MAAgMnAAJVNmFK2CSNkSAmDn4vBA',
                                                         'CAACAgIAAxkBAAIBKWQZzatvvutxw076zjtf'
                                                         'mCK0_G5UAAKHAANBvQMXuM7tZytDsXIvBA'))),
                  message.answer_video(
                      video='BAACAgIAAxkBAAIICWQ0OT0NxnAAAUI6AcHlYjxAQ-5PEgACWAADoLoJS9iMn0dkL8qhLwQ')))


@router.message(or_f(Text(contains='любовь', ignore_case=True),
                     Text(contains='отношения', ignore_case=True),
                     Text(contains='семья', ignore_case=True)),
                ~Text(contains='соотношения', ignore_case=True))
async def family(message: Message):
    await choice(
        (message.answer_sticker(sticker='CAACAgIAAxkBAAPbZBmgZVXBi_aT3Wdd7y3l4_HuRt0AAyYAAmqbKUv5i6bhelJ4UC8E'),
         message.answer_photo(
             photo='AgACAgIAAxkBAAIB_2Q0MTC--BOr78jjVXiHiUUVYHl2AAI2yTEbkpChSfEWdi0Qz-yrAQADAgADcwADLwQ')))


@router.message(Text(contains='тату', ignore_case=True))
async def tatu(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAPlZBm2vvq3FtfxtwABflZVgDhDIN4cAAJoAANBvQMXwI_2ZXC-jtEvBA')


@router.message(Text(contains='дурка', ignore_case=True))
async def crazy(message: Message):
    await choice((message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAPpZBm5mt3Jq1Ix1uH'
                                                         'QycgvSfdCr6kAAp8AA0G9AxeF4NKxOZOApS8E',
                                                         'CAACAgIAAxkBAAIBOWQZ0Uj8GIHv4nkLd3gOx'
                                                         'JtfwC7-AAJ5AANBvQMXl6vfswu0wZkvBA'))),
                  message.answer_animation(animation='CgACAgIAAxkBAAID3GQZ3mqtG1Nui7Pr7EH'
                                                     'xQD-W75D4AALTAwACB60wStgfY2yLbbm8LwQ')))


@router.message(or_f(Text(contains='лизать', ignore_case=True),
                     Text(contains='отлиж', ignore_case=True),
                     Text(contains='лизал', ignore_case=True)))
async def cunnilingus(message: Message):
    await choice((message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAPtZBm6qxHV_89iX'
                                                         'Ud4wnqTr1uYDd0AAgUAA0G9AxeiwXMqcBpUki8E',
                                                         'CAACAgIAAxkBAAIBB2QZwoJKbxF54Om89-O-fCnm'
                                                         'fhwKAAIyAANBvQMX9S47YghYnigvBA'))),
                  message.answer_animation(animation=choice(('CgACAgIAAxkBAAIDwGQZ2Qh4odQlqf_WwpI1M'
                                                             '8jJWGrGAALTBQACn7p4SBiRU49e_CnBLwQ',
                                                             'CgACAgIAAxkBAAID4GQZ4CUu9pQ1OquPGEJ6g0'
                                                             'CF4xAIAALRBgACxahhSyxuxK3qcUn9LwQ')))))


@router.message(Text(contains='пархай', ignore_case=True))
async def fly(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAPxZBm8E679S4trsXqJbeLytdH2UucA'
                                         'Ah0AA0G9AxcCtqDRRG1mMy8E')


@router.message(or_f(Text(contains='танц', ignore_case=True),
                     Text(contains='дэнс', ignore_case=True),
                     lambda x: x.audio is not None))
@router.callback_query()
async def dance(message: Message):
    await message.answer_animation(animation=choice(('CgACAgIAAxkBAAIDlmQZ08IZ4WU8a4EB4'
                                                     'Xspq43TE8RjAAI7BAAC8llBSmFRx2Bt_E28LwQ',
                                                     'CgACAgIAAxkBAAIDoGQZ1QsZ3DcsmepSDoj46'
                                                     'lpyC8NJAALcAgACmTL5SGxlbOLX_RvFLwQ',
                                                     'CgACAgIAAxkBAAIDpGQZ1d-BmqXBZdOqm2tyC'
                                                     '7ElKI0XAAIaBQAChSqYSS5YKtZl8X5CLwQ',
                                                     'CgACAgIAAxkBAAIDqmQZ1oxHFfJ-1aJwm4'
                                                     'bTf13YXnRlAAK4BAACXdpASNLQY9R_WJ13LwQ',
                                                     'CgACAgIAAxkBAAIDrGQZ1sU6Kw_PN5Uprui7'
                                                     'Q0QnheplAAKYBwACd3R4S4rQXA88UIiuLwQ',
                                                     'CgACAgIAAxkBAAIDsGQZ12fPdTsW8BaQt4A'
                                                     'S9TcbDZqrAAJfBgACik-YSmOhxQZHGp5rLwQ',
                                                     'CgACAgIAAxkBAAIDuGQZ2EAmJrnC091Gvoup'
                                                     'qMEsD1OGAALDCAACoJKoSEAY4Mt4M9nZLwQ',
                                                     'CgACAgIAAxkBAAIDvGQZ2NoWxxttROdLMCwk'
                                                     'UXoC3Z6hAAL_DgACPNFISHoLrwK1_W_5LwQ',
                                                     'CgACAgIAAxkBAAIDvmQZ2PTiUmL3XohGbfLs'
                                                     'XAndxXQfAAJAEAACMuKYSp3m9yDwao3qLwQ',
                                                     'CgACAgIAAxkBAAIDxmQZ2ehdERYajvoIumK'
                                                     'rlwUMe55tAAJFBAACFv1pSJ5u8lLPMLssLwQ',
                                                     'CgACAgIAAxkBAAIDzGQZ2xZVpQZXi0bFCi-'
                                                     'xgHaEYSe1AAJCBAACFv1pSOyGI3_jh2lQLwQ',
                                                     'CgACAgIAAxkBAAID0GQZ2-JF87siV7epBYVh'
                                                     '4keVsgmpAALcHwACEKE4Sy46nm-YvR0AAS8E',
                                                     'CgACAgIAAxkBAAID0mQZ3Cc7ID5-WxUt_h8-'
                                                     'FoDu7tcRAAIbFgACypIBSWROUr3du9JiLwQ',
                                                     'CgACAgIAAxkBAAID1mQZ3RLpINaWZbY2LqF'
                                                     'WQpS94DMvAAJwGwACPYE5SwggUwgH1obtLwQ',
                                                     'CgACAgIAAxkBAAID5GQZ4fcVzJ9pKucJf700'
                                                     'qHlhZLwhAALkAAPv2ohIYew46B4VizYvBA')))


@router.message(or_f(Text(endswith='занят', ignore_case=True),
                     Text(text='занят', ignore_case=True)),
                ~Text(contains='занято', ignore_case=True),
                ~Text(contains='занятo', ignore_case=True),
                ~Text(contains='занятс', ignore_case=True),
                ~Text(contains='занятc', ignore_case=True),
                ~Text(contains='занять', ignore_case=True))
async def wait(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAPzZBm83eA_DkpzEDcFHarnkTZy_bcAAhkAA0G9Axf7DAq2H7XDWC8E')


@router.message(or_f(Text(contains='кальян', ignore_case=True),
                     Text(contains='калик', ignore_case=True)))
async def hookah(message: Message):
    await choice((message.answer_sticker(sticker='CAACAgIAAxkBAAP1ZBm9gwAB7SXAvCt6haFmlVizYbuTAA'
                                                 'IHAANBvQMXnwJOPWDT4e0vBA'),
                  message.answer_animation(animation='CgACAgIAAxkBAAIDsmQZ15Q6rXCq_4yKJ68M-'
                                                     'XGksXWqAAJkBgACik-YSpKDMZl0n-MbLwQ')))


@router.message(or_f(Text(contains='едем', ignore_case=True),
                     Text(contains='поехали', ignore_case=True)))
async def go(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAP3ZBm-VO0n4BkGe35LBy5md8hENUAAAlMAA0G9AxdR1uAxmu6kui8E')


@router.message(Text(text='хех', ignore_case=True))
async def wink(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAP5ZBm-8XucZWZzY8c_cW43fWGrVU4AAlUAA0G9AxdVLUq9Y0ql2y8E')


@router.message(or_f(Text(contains='кран', ignore_case=True),
                     Text(contains='стрела', ignore_case=True)))
async def tap(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAP7ZBm_V4uMASAqcZwM413-HSkKTxMAAk4AA0G9AxfFuXTFNj3kni8E')


@router.message(Text(contains='в рот', ignore_case=True))
async def mouth(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAP9ZBm_-M2j4YNcQ7va0KUjyQ-q3ugAAkoAA0G9AxcyxxESJ6VurS8E')


@router.message(or_f(Text(contains='убью', ignore_case=True),
                     Text(contains='убийство', ignore_case=True),
                     Text(contains='застрел', ignore_case=True),
                     Text(contains='пристрел', ignore_case=True)))
async def shoot(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAP_ZBnAZJ64v02kCL4wqIG71J185_kAAk0AA0G9'
                                                 'Axe_zKD7P7k6OS8E',
                                                 'CAACAgIAAxkBAAIBAWQZwTpUch7AkuNBPGVRlSR_MJLpAAJIAANB'
                                                 'vQMXHB1H9fXbdzIvBA',
                                                 'CAACAgIAAxkBAAIBEWQZxJB9GL8TRBSSFL79qJEITmSvAAIUAANB'
                                                 'vQMXpUlGBNs5xZAvBA',
                                                 'CAACAgIAAxkBAAIBIWQZx0EAAU8uovZKi5h6-lNtmT6BqAACswAD'
                                                 'Qb0DF0efZDW-YSWvLwQ')))


@router.message(or_f(Text(contains='нюх', ignore_case=True),
                     Text(contains='белого', ignore_case=True),
                     Text(contains='чистого', ignore_case=True),
                     Text(contains='быстрого', ignore_case=True)))
async def cocaine(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBA2QZwXiFblavI0Kd-wABBoUpLuY4dAACRQADQb0DF_haM45FBjE6LwQ')


@router.message(Text(contains='чорт', ignore_case=True))
async def devil(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBCWQZwsePPIE3ilMbl-c4Ga_sa-M-AAItAANBvQMX1hMyvZgUGcMvBA')


@router.message(Text(text='пока', ignore_case=True))
async def bey(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBD2QZxCeCo1bua6hXxY_A0-XIdSjAAAIlAANBvQMXrAYPwe_0iWsvBA')


@router.message(or_f(Text(contains='слепой', ignore_case=True),
                     Text(contains='крот', ignore_case=True)))
async def dont_see(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBE2QZxLqUM3r6WN1KUnFh7JnoqvrqAAIQAANBvQMXN4FGya72CdIvBA')


@router.message(or_f(Text(contains='куша', ignore_case=True),
                     Text(text='ем', ignore_case=True),
                     Text(contains='поесть', ignore_case=True)))
async def eat(message: Message):
    await choice((message.answer_sticker(sticker='CAACAgIAAxkBAAIBFWQZxW1Xui8XbjebBmNa9v8Z-'
                                                 '53DAAIBAANBvQMXUCx21imXCjwvBA'),
                  message.answer_animation(animation='CgACAgIAAxkBAAIDtGQZ19i75uSp29jq7Nl'
                                                     'CCc1OJobbAAI0CQACCWvYSikn_LSkESQDLwQ')))


@router.message(or_f(Text(contains='дитя', ignore_case=True),
                     Text(contains='ребенок', ignore_case=True),
                     Text(contains='дети', ignore_case=True)))
async def child(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIBF2QZxlz9p7dZ4ay6KtsGPLOTXarsAAK4'
                                                 'AANBvQMX2UupBrwF_RsvBA',
                                                 'CAACAgIAAxkBAAIBGWQZxuM0O48-suDJvfRMoXBUqYWYAAK5A'
                                                 'ANBvQMXYUWvGpzyedwvBA',
                                                 'CAACAgIAAxkBAAIBG2QZxvblYCIMs-ZFfilmbYR5frBnAAK6'
                                                 'AANBvQMXCOJ9u0LYmEsvBA',
                                                 'CAACAgIAAxkBAAIBHWQZxwmtlu_WCfrAqX6Sf19VyOy0AAK7'
                                                 'AANBvQMXsmSWKuWi_OMvBA',
                                                 'CAACAgIAAxkBAAIBH2QZxxgqcpSdT6f17BOQiXeJnZC2AAK'
                                                 '8AANBvQMX1x51vTxH-cwvBA')))


@router.message(Text(contains='сфотка', ignore_case=True))
async def photo(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBI2QZx2IbIE155jHaYjnrislmwIL7AAK1AANBvQMXAcZO4cBmSnovBA')


@router.message(Text(text='ну ну', ignore_case=True))
async def what_say(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBJWQZzB2348NfAwGbg7LrgZFL0ra_AAKxAANBvQMXj4xQilrwAkgvBA')


@router.message(or_f(Text(contains='уебу', ignore_case=True),
                     Text(contains='уеба', ignore_case=True),
                     Text(contains='вьебать', ignore_case=True),
                     Text(contains='въебать', ignore_case=True)),
                ~Text(contains='уебался', ignore_case=True),
                ~Text(contains='уебан', ignore_case=True))
async def kick(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBJ2QZzPBRdGskzeBp5sPqLl9QmTfjAAKKAANBvQMXem2VIlsPe38vBA')


@router.message(or_f(Text(contains='трейд', ignore_case=True),
                     Text(contains='биток', ignore_case=True),
                     Text(contains='инвест', ignore_case=True),
                     Text(contains='бабки', ignore_case=True),
                     Text(contains='рубим бабло', ignore_case=True),
                     Text(contains='бабло', ignore_case=True),
                     Text(contains='бизнес', ignore_case=True)))
async def money(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBLWQZzjn1dzCjOXnTC4Elm2548kpBAAJ1AANBvQMXNI99qc4F_4kvBA')


@router.message(or_f(Text(contains='умер', ignore_case=True),
                     Text(contains='смерть', ignore_case=True),
                     Text(contains='убили', ignore_case=True),
                     Text(contains='мертв', ignore_case=True),
                     Text(contains='мёртв', ignore_case=True)))
async def death(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBL2QZzyHPiyC7FQnJMOoSxs9cIPOcAAJ2AANBvQMXlGwRnOQ_jxovBA')


@router.message(Text(contains='бабка', ignore_case=True))
async def grandma(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIBMWQZz7K0z_W9RzeiltY'
                                                 'Pbb8C3lwKAAJ9AANBvQMXsb8Cgq7uIa0vBA',
                                                 'CAACAgIAAxkBAAIBM2QZ0Bc23foYwngF7CB'
                                                 'T18px3DjzAAJ6AANBvQMXMQrvGKdIoigvBA')))


@router.message(Text(contains='дед', ignore_case=True))
async def grandpa(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIBNWQZ0Efe0wYw6sWGqO7u'
                                                 'wkPiEOXHAAJ7AANBvQMXziJ1lfN_DyIvBA',
                                                 'CAACAgIAAxkBAAIBo2QcfwUVd2fHl8SJj5P'
                                                 'BvxURSBBLAAJfAANBvQMX5XcCCSuudIwvBA')))


@router.message(or_f(Text(contains='сила', ignore_case=True),
                     Text(contains='сильный', ignore_case=True),
                     Text(contains='мощь', ignore_case=True)))
async def power(message: Message):
    await choice((message.answer_sticker(sticker='CAACAgIAAxkBAAIBN2QZ0I3CehCyIqvjB_'
                                                 'NhX1zCZ8K-AAKGAANBvQMXF1Xrk86-mHsvBA'),
                  message.answer_animation(animation='CgACAgIAAxkBAAID2GQZ3Y1mVjNtNwXVXh'
                                                     'Vs2RPE0rpFAAKVFQACC10oSJuiWCSoXz3HLwQ')))


@router.message(Text(contains='лакшери', ignore_case=True))
async def luxury(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBO2QZ0ZOS2uSTVV2UkR0812gSwtYSAAJsAANBvQMXQIN59r5KL4EvBA')


@router.message(Text(contains='такси', ignore_case=True))
async def taxi(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBPWQZ0dJ7v61ByHVXuqBOD6Bf9hFQAAJnAANBvQMXMrm9Vrjxco4vBA')


@router.message(or_f(Text(contains='спорт', ignore_case=True),
                     Text(contains='зож', ignore_case=True)))
async def sport(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAIDnmQZ1Izwd0tafU6FyCMq-lSQMcmrAALfAgACA_NZSrIT11VsNfywLwQ')


@router.message(Text(contains='плачь', ignore_case=True))
async def cry(message: Message):
    await message.answer_animation(animation=choice(('CgACAgIAAxkBAAIDpmQZ1hIWh-BkrMAtQv-'
                                                     'Hn6m2iIdqAALwBgACipiASd0CJcUYgn7RLwQ',
                                                     'CgACAgIAAxkBAAIDqGQZ1l2QnKDYF4klmDiN'
                                                     '7hQGKY11AAIEAwACO57BSmtlfuUAAWHItS8E')))


@router.message(Text(contains='не расстра', ignore_case=True))
async def no_sad(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAIDrmQZ1t3qBLYTfUn_05X6xixdiWEFAALOBgACK_uhS7T5o03JPeOlLwQ')


@router.message(or_f(Text(contains='победа', ignore_case=True),
                     Text(contains='выигр', ignore_case=True)))
async def win(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAIDwmQZ2T6IzOrNKv-q8v9aJn491wV-AALtBwACuNIwS6q_6MQVAAFRRC8E')


@router.message(Text(contains='выхожу', ignore_case=True))
async def go_out(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAIDxGQZ2aQiWEfsbcA5e2nEh3ZkY9vjAALTCAAC5SKgSL76jQ_jgV4tLwQ')


@router.message(or_f(Text(contains='собака', ignore_case=True),
                     Text(text='гав', ignore_case=True)))
async def dog(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAIDyGQZ2g43fWstwL7K4_bUnBUjAAFgMwAC3AoAArvKWUiLZ7x-0V8uOS8E')


@router.message(Text(contains='вкусн', ignore_case=True))
async def tasty(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAIDymQZ2p8VPWKJGVELjGGjD-PqpZYzAAIYIwACdgRJSDS5UP-0Dy3wLwQ')


@router.message(or_f(Text(contains='гей', ignore_case=True),
                     Text(contains='геи', ignore_case=True)),
                ~Text(text='сергей', ignore_case=True),
                ~Text(text='сергеи', ignore_case=True))
async def dog(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAIDzmQZ22OJZuKGkgj8q9vHYpoAAVST_'
                                             'QACAQkAAnDsQUsysxUAAccP688vBA')


@router.message(Text(contains='сальт', ignore_case=True))
async def salto(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAID3mQZ34RJtzc2nugmpBXcT-HJtNJEAAJZBQACobcYS79GPqS4ufOMLwQ')


@router.message(Text(contains='футбол', ignore_case=True),
                ~Text(contains='футболк'))
async def football(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAID4mQZ4N_-zSdLuyvbOw-5v1I-VlS3AAIbCgACnpiYST8os2iSExdRLwQ')


@router.message(or_f(Text(contains='писяю', ignore_case=True),
                     Text(text='пописяй', ignore_case=True),
                     Text(contains='поссу', ignore_case=True),
                     Text(text='ссу', ignore_case=True)))
async def pee(message: Message):
    await message.answer_animation(animation='CgACAgIAAxkBAAID5mQZ4zhhxBMiEBgNmDy0wC9XWt4aAAKRAANer1hL9qrzqOpMJPIvBA')


@router.message(or_f(Text(contains=('ебать', 'не', 'должно'), ignore_case=True),
                     Text(text='ебет?', ignore_case=True),
                     Text(text='Тебя ебет?', ignore_case=True)))
async def do_not_care(message: Message):
    await message.answer_sticker(sticker=choice(('CAACAgIAAxkBAAIEQGQa-EhbslvAs1poxc6BarO-'
                                                 'sbmXAAISAANBvQMXEN77oRyMSPgvBA',
                                                 'CAACAgIAAxkBAAIEQmQa-GkLza8voe54RpAzhmrg'
                                                 'OsdbAAKNAANBvQMXdsqJd60GvrsvBA',
                                                 'CAACAgIAAxkBAAIERGQa-IDNVKwKgcaRcM_cjBRK'
                                                 'xO_XAAK7LgAChPWBST5GRoJpDTujLwQ')))


@router.message(or_f(Text(contains='кайф', ignore_case=True),
                     Text(contains='балде', ignore_case=True)))
async def bliss(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBoWQcfh6kZwYhnLkFMArU68bc14dkAAJiAANBvQMXtL6cJ_0dS9YvBA')


@router.message(or_f(Text(contains='обидно', ignore_case=True),
                     Text(contains='обид', ignore_case=True),
                     Text(contains='прискорбно', ignore_case=True)))
async def shame(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIBpWQcf6vZIbz55F8AAblhpabeh'
                                         'QlRvAACgAADQb0DF1iUnrjVrMU_LwQ')


@router.message(Text(contains='церков', ignore_case=True))
async def church(message: Message):
    await message.answer_video(video='BAACAgIAAxkBAAIFOGQkh66d-N75s6odfYVZk86V3zNKAAK7LgAC8McgSasIeOtspl2cLwQ')


@router.message(or_f(Text(contains='черны', ignore_case=True),
                     Text(contains='черно', ignore_case=True)),
                (~Text(contains='чернокнижный', ignore_case=True)))
async def black(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAIB-WQpT-pDidY8aX4baySiPY2LlbnVAAKuAANBvQMXZtfnaJLLNE0vBA')


