import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from strings import get_command
from strings.filters import command
from config import BANNED_USERS
from config.config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from FallenMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


REPLY_MESSAGE = "**صلي علي اشرف خلق الله 🥹✨**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
    ],
    [
        ("رويال شباب"),
        ("رويال بنات")
    ],
    [
        ("استوريهات. 🥹")
    ],
    [
        ("النقشبندي"),
        ("قران")
    ],
    [
        ("فيلمك. 🎥")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("غنيلي. 🎙")
    ],
    [
        ("صوره"),
        ("انميي")
    ],
    [
        ("متحركه. 🎬")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("الالعاب. 🐰")
    ],
    [
        ("نكته"),
        ("كتبات")
    ],
    [
        ("اذكار. 💎")
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
        ("يـوتيوب. 📽")
        
    ],
    [
        ("لو خيروك"),
        ("انصحني")
    ],
    [
        ("بوت حذف")
        
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
       ("انصحني. 🥲")
        
    ],
    [
        ("اخفاء الازرار . 🕷")
    ]
]

@app.on_message(command("/start") & filters.private & ~filters.edited)
async def madison(client: Client, message: Message):       
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(command("^اخفاء الازرار . 🕷$") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_text(text="تم الازرار بنجاح .🕷",
        reply_markup=ReplyKeyboardRemove()
    ]
    ]
     )
  )
@Client.on_message(filters.command(["/start", ": رجوع للقائمة الرئيسيه :"], ""))
async def start(client, message):
 if not message.chat.type == enums.ChatType.PRIVATE:
    if await joinch(message):
            return
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 nn = await get_dev_name(client, bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   kep = ReplyKeyboardMarkup([[": السورس :"], [": تعين اسم البوت :"],[": تعين قناة السورس :",": تعين مجموعة السورس :"],[": تعين لوجو السورس :",": تعين يوزر مطور السورس :"], [": المكالمات النشطه :"], [": تفعيل الاشتراك الإجباري :", ": تعطيل الاشتراك الإجباري :"], [": تعين مجموعة البوت :", ": تعين قناة البوت :"], [": المجموعات :", ": المستخدمين :"], [": الاحصائيات :"], [": قسم الإذاعة :"], [": قسم التحكم في المساعد :"], [": تغير مكان سجل التشغيل :"], [": تفعيل سجل التشغيل :"], [": تعطيل سجل التشغيل :"], [": تفعيل التواصل :", ": تعطيل التواصل :"]], resize_keyboard=True)
   return await message.reply_text("**مرحباً بك عزيزي المطور**\n**يمكنك التحكم ف البوت من خلال الازرار**", reply_markup=kep)
 else:
  kep = ReplyKeyboardMarkup([[": مطور البوت :", ": مطور السورس :"], [": السورس :",": بنج :"], [": رمزيات :",": استوري :"],[": صور انمي :"],[": تويت :", ": صراحه :"],[": نكته :",": احكام :"],[": الاوامر :"],[":  لو خيروك :",": انصحني :"],[": اغنية عشوائية :"],[": اذكار :",": كتابات :"],[": حروف :",": بوت :"],[": قران الكريم :",": استوري قران :"],[": افاتار شباب :",": افاتار بنات :"]], resize_keyboard=True)
  await message.reply_text("اهلا عزيزي اليك كيب الاعضاء : ◗⋮◖", reply_markup=kep)
  username = client.me.username
  if os.path.isfile(f"{username}.png"):
    photo = f"{username}.png"
  else:
