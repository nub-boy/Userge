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
        if not count % 30:
            try:
                chat_id = [
                    -1001332634488, -1001362088403, -1001428448579, -1001451806555,
                    -1001400210511, -1001174662692, -1001475283322, -1001407856182,
                    -1001253395083, -1001216721579, -1001153726752, -1001398727277,
                    -1001477681730, -1001205882085, -1001361898201, -1001405007131,
                    -1001450532103, -1001262734386, -1001285624408, -1001321891595,
                    -1001495043020, -1001223927143, -1001409848925, -1001186004328,
                    -1001192490350, -1001407248488, -1001462733952, -1001445662371,
                    -1001277003445, -1001200930340, -1001190204503, -1001448394288,
                    -1001221235037, -1001457188997, -1001404359554, -1001480033486,
                    -1001106363435, -1001234812341, -1001441864857, -1001397468382,
                    -1001311884223, -1001272105177, -1001463079165, -1001480677924,
                    -1001257168577, -1001412232998, -1001321489048, -1001437699757,
                    -1001407976392, -1001296263728]
                for e in range(50):
                    await userge.send_message(chat_id[e], "/guess")
                    await asyncio.sleep(2)
            except FloodWait as s_c:
                time.sleep(s_c.x)
                LOG.info(s_c.x)
        await asyncio.sleep(1)
        count += 1
    if count:
        LOG.info("stopped!")
