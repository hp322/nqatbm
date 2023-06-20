from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

# -ل

tembm.start()



c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5299626487]




@tembm.on(events.NewMessage)
async def join_channel(event):
    try:
        await tembm(JoinChannelRequest("@tembm"))
    except BaseException:
        pass
        
@tembm.on(events.NewMessage)
async def join_channel(event):
    try:
        await tembm(JoinChannelRequest("@tembm"))
    except BaseException:
        pass
      

@tembm.on(events.NewMessage)
async def join_channel(event):
    try:
        await tembm(JoinChannelRequest("@tembm"))
    except BaseException:
        pass  
        
        
        
        
        
        
@tembm.on(events.NewMessage(outgoing=False, pattern='/bmm'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**السورس كاعد يشتغل️**')


@tembm.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**اوامر الاسـتخدام 

- @ZMMBOT - `/bm1`
- @A_MAN9300BOT - `/bm2`
- @MARKTEBOT - `/bm3`
- @XNSEX21BOT - `/bm4`
ارسـل - `/bm`
للمغادرة - `/llbm`
للتحويل - `/trabm`
للمعلومات - `/infbm`
للانضمام - `/jobm`**""")





@tembm.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")



@tembm.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**سيتم الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
tembm
''')
async def _(event):
    await event.reply("**سيتم تجميع النقاط**")
    await event.edit("**سيتم تجميع النقاط**")
    joinu = await tembm(JoinChannelRequest('tembm'))
    channel_entity = await tembm.get_entity(bot_username)
    await tembm.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await tembm.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tembm.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tembm(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await tembm.send_message(event.chat_id, f"**تم تجميع نقـاط...! **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tembm(JoinChannelRequest(url))
            except:
                bott = url.split('/bm1')[-1]
                await tembm(ImportChatInviteRequest(bott))
            msg2 = await tembm.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tembm.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tembm.send_message(event.chat_id, "**تم تجميع نقـاط...! **")

@tembm.on(events.NewMessage(outgoing=False, pattern='/bm2'))
async def _(event):
    await event.reply("**سيتم تجميع النقاط**")
    await event.edit("**سيتم تجميع النقاط**")
    joinu = await tembm(JoinChannelRequest('tembm'))
    channel_entity = await tembm.get_entity(bot_usernamee)
    await tembm.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await tembm.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tembm.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tembm(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await tembm.send_message(event.chat_id, f"**تم تجميع نقـاط...! **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tembm(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tembm(ImportChatInviteRequest(bott))
            msg2 = await tembm.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tembm.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tembm.send_message(event.chat_id, "**تم تجميع نقـاط...! **")


@tembm.on(events.NewMessage(outgoing=False, pattern='/bm3'))
async def _(event):
    await event.reply("**سيتم تجميع النقاط**")
    await event.edit("**سيتم تجميع النقاط**")
    joinu = await tembm(JoinChannelRequest('tembm'))
    channel_entity = await tembm.get_entity(bot_usernameee)
    await tembm.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await tembm.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tembm.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tembm(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await tembm.send_message(event.chat_id, f"**تم تجميع نقـاط...! **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tembm(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tembm(ImportChatInviteRequest(bott))
            msg2 = await tembm.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tembm.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tembm.send_message(event.chat_id, "**تم تجميع نقـاط...! **")


@tembm.on(events.NewMessage(outgoing=False, pattern='/bm4'))
async def _(event):
    await event.reply("**سيتم تجميع النقاط**")
    await event.edit("**سيتم تجميع النقاط**")
    joinu = await tembm(JoinChannelRequest('tembm'))
    channel_entity = await tembm.get_entity(bot_usernameeee)
    await tembm.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await tembm.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tembm.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tembm(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await tembm.send_message(event.chat_id, f"**تم تجميع نقـاط...! **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tembm(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tembm(ImportChatInviteRequest(bott))
            msg2 = await tembm.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tembm.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tembm.send_message(event.chat_id, "**تم تجميع نقـاط...! **")

@tembm.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**سيتم تجميع النقاط**")
    joinu = await tembm(JoinChannelRequest('tembm'))
    channel_entity = await tembm.get_entity(bot_username)
    await tembm.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await tembm.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tembm.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tembm(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await tembm.send_message(event.chat_id, f"**تم تجميع نقـاط...! **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tembm(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tembm(ImportChatInviteRequest(bott))
            msg2 = await tembm.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tembm.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tembm.send_message(event.chat_id, "**تم تجميع نقـاط...! **")
    
    
    
@tembm.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**سيتم تجميع النقاط**")
    joinu = await tembm(JoinChannelRequest('tembm'))
    channel_entity = await tembm.get_entity(bot_usernamee)
    await tembm.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await tembm.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tembm.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tembm(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await tembm.send_message(event.chat_id, f"**تم تجميع نقـاط...! **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tembm(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tembm(ImportChatInviteRequest(bott))
            msg2 = await tembm.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tembm.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tembm.send_message(event.chat_id, "**تم تجميع نقـاط...! **")

@tembm.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**سيتم تجميع النقاط**")
    joinu = await tembm(JoinChannelRequest('tembm'))
    channel_entity = await tembm.get_entity(bot_usernameee)
    await tembm.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await tembm.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tembm.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tembm(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await tembm.send_message(event.chat_id, f"**تم تجميع نقـاط...! **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tembm(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tembm(ImportChatInviteRequest(bott))
            msg2 = await tembm.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tembm.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tembm.send_message(event.chat_id, "**تم تجميع نقـاط...! **")


@tembm.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**سيتم تجميع النقاط**")
    joinu = await tembm(JoinChannelRequest('tembm'))
    channel_entity = await tembm.get_entity(bot_usernameeee)
    await tembm.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await tembm.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tembm.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tembm(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await tembm.send_message(event.chat_id, f"**تم تجميع نقـاط...! **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tembm(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tembm(ImportChatInviteRequest(bott))
            msg2 = await tembm.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tembm.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tembm.send_message(event.chat_id, "**تم تجميع نقـاط...! **")


##########################################




@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/bbm1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tembm.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await tembm.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await tembm.send_message(bot_username, pt)
    sleep(4)
    msg = await tembm.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/bbm2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tembm.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await tembm.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await tembm.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await tembm.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/bbm3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tembm.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await tembm.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await tembm.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await tembm.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/bbm4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tembm.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await tembm.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await tembm.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await tembm.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'/nbm1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tembm.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await tembm.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await tembm.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'/bm2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tembm.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await tembm.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await tembm.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@tembm.on(events.NewMessage(outgoing=False, pattern=r'/nbm3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tembm.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await tembm.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await tembm.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'/nbm4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tembm.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await tembm.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await tembm.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@tembm.on(events.NewMessage(outgoing=False, pattern=r'/llbm'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await tembm.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await tembm(LeaveChannelRequest(dialog.entity))
                await event.respond(f"** غادرت گل القنوات **")
                




@tembm.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await tembm.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    

@tembm.on(events.NewMessage(outgoing=False, pattern='/trabm'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""** قسم تحويل النقاط
        
• @ZMMBOT - `/bbm1 + عدد النقاط `
• @A_MAN9300BOT - `/bbm2 + عدد النقاط`
• @MARKTEBOT - `/bbm3 + عدد النقاط `
• @XNSEX21BOT - `/bbm4 + عدد النقاط`**""")



@tembm.on(events.NewMessage(outgoing=False, pattern='/infbm'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""** قسم معلومات البوتات
• @ZMMBOT - `/nbm1`
• @A_MAN9300BOT - `/nbm2`
• @MARKTEBOT - `/nbm3`
• @XNSEX21BOT - `/nbm4`**""")


@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tembm.send_message(userbt, '/start')
     sleep(2)
    msg1 = await tembm.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await tembm.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@tembm.on(events.NewMessage(outgoing=False, pattern='/jobm'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await tembm.send_message(event.chat_id, "** اوكف راح انضم ب جميع قنوات البوتات **")
        joinq = await tembm(JoinChannelRequest('d3boot_7'))
        joinw = await tembm(JoinChannelRequest('Fvvvv'))
        joine = await tembm(JoinChannelRequest('DzDDDD'))
        joinr = await tembm(JoinChannelRequest('botbillion'))
        joint = await tembm(JoinChannelRequest('zzzzzz1'))
        joiny = await tembm(JoinChannelRequest('zzzzzz'))
        joini = await tembm(JoinChannelRequest('zz_MX'))
        joino = await tembm(JoinChannelRequest('tembm'))
        joinp = await tembm(JoinChannelRequest('KTTTT'))
        joina = await tembm(JoinChannelRequest('RRXFR'))
        sendd = await tembm.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
        


print("")
tembm.run_until_disconnected()
