import asyncio

from userge import userge, Message, Filters

chat_id = [
    -342245068, -455937686, -482461535, -459866909, -481555266,
    -462977547, -440401481, -495471654, -467412207, -329855110,
    -430184927, -326574146, -1001210989062, -467415507, -458524349,
    -497210523, -405343280, -477893875, -444763764, -432999610
]


@userge.on_filters(Filters.chat(chat_id) & Filters.user("HeXamonbot") & Filters.text)
async def test_loop(msg: Message):

        if msg.text.startswith("Hint:"):
            await msg.reply("~guess")
