import os

import requests
from faker import Faker
from faker.providers import internet
from telethon import events

from FallenRobot.modules.helper_funcs.chat_status import is_user_admin
from FallenRobot import telethn, SUPPORT_CHAT


@telethn.on(events.NewMessage(pattern="/fgen$"))
async def hi(event):
    if event.fwd_from:
        return
    if (
        event.is_group
        and not await is_user_admin(event, event.message.sender_id)
    ):
        await event.reply("`You Should Be Admin To Do This!`")
        return
    fake = Faker()
    print("FAKE DETAILS GENERATED\n")
    name = str(fake.name())
    fake.add_provider(internet)
    address = str(fake.address())
    ip = fake.ipv4_private()
    cc = fake.credit_card_full()
    email = fake.ascii_free_email()
    job = fake.job()
    android = fake.android_platform_token()
    pc = fake.chrome()
    await event.reply(
        f"<b><u> Fake Information Generated</b></u>\n<b>Name :-</b><code>{name}</code>\n\n<b>Address:-</b><code>{address}</code>\n\n<b>IP ADDRESS:-</b><code>{ip}</code>\n\n<b>credit card:-</b><code>{cc}</code>\n\n<b>Email Id:-</b><code>{email}</code>\n\n<b>Job:-</b><code>{job}</code>\n\n<b>Android User Agent:-</b><code>{android}</code>\n\n<b>PC User Agent:-</b><code>{pc}</code>",
        parse_mode="HTML",
    )


@telethn.on(events.NewMessage(pattern="/picgen$"))
async def _(event):
    if event.fwd_from:
        return
    if await is_user_admin(event, event.message.sender_id):
        url = "https://thispersondoesnotexist.com/image"
        response = requests.get(url)
        if response.status_code == 200:
            with open("Anonymous.jpg", "wb") as f:
                f.write(response.content)

        captin = f"Fake Image powered by @{SUPPORT_CHAT}."
        fole = "Anonymous.jpg"
        await telethn.send_file(event.chat_id, fole, caption=captin)
        await event.delete()
        os.system("rm ./Anonymous.jpg ")
