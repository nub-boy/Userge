import time
import asyncio

from pyrogram.errors import FloodWait

from userge import userge, Message, Config, get_collection

SAVED_SETTINGS = get_collection("CONFIGS")
UPDATE_ = False

LOG = userge.getLogger(__name__)


async def _init() -> None:
    global UPDATE_  # pylint: disable=global-statement
    data = await SAVED_SETTINGS.find_one({'_id': 'UPDATE_'})
    if data:
        UPDATE_ = data['on']


@userge.on_cmd(
    "auto", about={
        'header': "set profile picture",
        'usage': "{tr}autopic\n{tr}autopic [image path]\nset timeout using {tr}sapicto"},
    allow_channels=False, allow_via_bot=False)
async def auto(message: Message):
    global UPDATE_  # pylint: disable=global-statement
    await message.edit('`processing...`')
    if UPDATE_:
        if isinstance(UPDATE_, asyncio.Task):
            UPDATE_.cancel()
        UPDATE_ = False
        SAVED_SETTINGS.update_one({'_id': 'UPDATE_'},
                                  {"$set": {'on': False}}, upsert=True)
        await asyncio.sleep(1)
        await message.edit('**stopped**',
                           del_in=5, log=__name__)
        return
    data_dict = {'on': True}
    SAVED_SETTINGS.update_one({'_id': 'UPDATE_'},
                              {"$set": data_dict}, upsert=True)
    await message.edit(
        '**started**', del_in=3, log=__name__)
    UPDATE_ = asyncio.get_event_loop().create_task(_worker())


@userge.add_task
async def _worker():
    count = 0
    while UPDATE_:
        if not count % 20:
            try:
                chat_id = [-342245068, -455937686, -482461535, -459866909,
                           -481555266, -462977547, -440401481, -495471654,
                           -467412207, -329855110, -430184927, -326574146,
                           -1001210989062, -467415507, -458524349, -497210523,
                           -405343280, -477893875, -444763764, -432999610]
                for e in range(20):
                    await userge.send_message(chat_id[e], "/guess")
                    await asyncio.sleep(2)
            except FloodWait as s_c:
                time.sleep(s_c.x)
                LOG.info(s_c.x)
        await asyncio.sleep(1)
        count += 1
    if count:
        LOG.info("stopped!")
