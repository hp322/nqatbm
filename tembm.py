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
DEVS = [5159123009]




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
        
        
        
        
        
        
@tembm.on(events.NewMessage(outgoing=False, pattern='/bm'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**السورس كاعد يشتغل️**')


@tembm.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @ZMMBOT - `/point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`
• SEND - `/bm`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")





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
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 bm⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  bm    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯bm 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@tembm.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
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
            await tembm.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

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
    await tembm.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@tembm.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
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
            await tembm.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

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
    await tembm.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@tembm.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
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
            await tembm.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

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
    await tembm.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@tembm.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
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
            await tembm.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

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
    await tembm.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@tembm.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
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
            await tembm.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

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
    await tembm.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@tembm.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
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
            await tembm.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

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
    await tembm.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@tembm.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
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
            await tembm.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

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
    await tembm.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@tembm.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
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
            await tembm.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

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
    await tembm.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


##########################################




@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
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
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
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

@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
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
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
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
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
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
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
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
 
@tembm.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
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
    
@tembm.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
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
    

@tembm.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await tembm.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await tembm(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                




@tembm.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await tembm.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    

@tembm.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")



@tembm.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


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
        
@tembm.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await tembm.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await tembm(JoinChannelRequest('d3boot_7'))
        joinw = await tembm(JoinChannelRequest('Fvvvv'))
        joine = await tembm(JoinChannelRequest('DzDDDD'))
        joinr = await tembm(JoinChannelRequest('botbillion'))
        joint = await tembm(JoinChannelRequest('zzzzzz1'))
        joiny = await tembm(JoinChannelRequest('zzzzzz'))
        joini = await tembm(JoinChannelRequest('zz_MX'))
        joino = await tembm(JoinChannelRequest('zd_e6'))
        joinp = await tembm(JoinChannelRequest('KTTTT'))
        joina = await tembm(JoinChannelRequest('RRXFR'))
        sendd = await tembm.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
        


print("💠 Sbmmmt 💠")
tembm.run_until_disconnected()


#code skip accumulate points by t.me.zzzzl1l thank you my bro
