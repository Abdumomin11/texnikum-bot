import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# BotFather'dan olgan tokeningiz
API_TOKEN = "8513885783:AAGdQoXXrfxHgpuy658CAQK1xn7TbnENjh4"

# Ochgan kanalingizning ID raqami
CHANNEL_ID = -1004437903961 

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Murojaat va So'rovnoma uchun holatlar (States)
class MurojatState(StatesGroup):
    ism = State()
    telefon = State()
    matn = State()

class SorovnomaState(StatesGroup):
    s1 = State()
    s2 = State()
    s3 = State()
    s4 = State()
    s5 = State()
    s6 = State()
    s7 = State()
    s8 = State()
    s9 = State()
    s10 = State()
    s11 = State()
    s12 = State()
    s13 = State()
    s14 = State()
    s15 = State()
    s16 = State()
    s17 = State()
    s18 = State()
    s19 = State()
    s20 = State()

# Asosiy menyu tugmalari
def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏛 Texnikum haqida"), KeyboardButton(text="📚 Yo'nalishlar")],
            [KeyboardButton(text="🌐 Bizning ijtimoiy tarmoqlar"), KeyboardButton(text="✍️ Murojaat yuborish")],
            [KeyboardButton(text="📊 So'rovnoma")]
        ],
        resize_keyboard=True
    )

# /start buyrug'i
@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Assalomu alaykum! Texnikumimizning rasmiy botiga xush kelibsiz.\n"
        "Kerakli bo'limni tanlang:",
        reply_markup=get_main_menu()
    )

# 1. Texnikum haqida
@dp.message(F.text == "🏛 Texnikum haqida")
async def info_texnikum(message: types.Message):
    text = (
        "🏛 **Texnikumimiz haqida qisqacha:**\n\n"
        "Bizning texnikum zamonaviy kasb-hunar va mutaxassisliklarni o'rgatishga ixtisoslashgan. "
        "Talabalarimiz uchun barcha qulayliklar, malakali ustozlar va amaliyot o'tash maskanlari mavjud."
    )
    await message.answer(text, parse_mode="Markdown")

# 2. Yo'nalishlar
@dp.message(F.text == "📚 Yo'nalishlar")
async def info_yonalishlar(message: types.Message):
    text = (
        "📚 **Texnikumimizda mavjud yo'nalishlar:**\n\n"
        "🔹 **9-sinf baza negizidagi yo'nalishlar:**\n"
        "1. Raqamli axborotlarni qayta ishlash\n"
        "2. Bank nazoratchisi\n"
        "3. Avtomobil ustasi\n"
        "4. Turarjoy infratuzilmasi\n"
        "5. Grafika va dizayn operatori\n"
        "6. Sotuvchi nazoratchi kassir\n\n"
        "🔹 **11-sinf baza negizidagi yo'nalishlar:**\n" 
        "1. Moliya\n"
        "2. Kompyuter injiniringi\n"
        "3. Bank ishi\n"
        "4. Buxgalteriya hisobi va audit\n"
        "5. Menejment\n"
        "6. Axborot xavfsizligi"
    )
    await message.answer(text, parse_mode="Markdown")

# 3. Ijtimoiy tarmoqlar
@dp.message(F.text == "🌐 Bizning ijtimoiy tarmoqlar")
async def info_tarmoqlar(message: types.Message):
    text = (
        "🌐 **Bizni ijtimoiy tarmoqlarda kuzating:**\n\n"
        "• Telegram kanal: t.me/oltinkol__3__son\n"
        "• Instagram sahifamiz: instagram.com/texnikum\n"
        "• Rasmiy veb-sayt: https://3texedu.uz/"
    )
    await message.answer(text, parse_mode="Markdown")


# ==================== SO'ROVNOMA (20 TA SAVOL) ====================

@dp.message(F.text == "📊 So'rovnoma")
async def start_sorovnoma(message: types.Message, state: FSMContext):
    await message.answer(
        "📊 **Talabalar uchun umumiy so'rovnoma boshlandi.**\n"
        "Iltimos, har bir savolga o'z fikringizni yozib qoldiring (1-savol/20):\n\n"
        "1. Ism va familiyangizni kiriting:",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(SorovnomaState.s1)

@dp.message(SorovnomaState.s1)
async def q2(message: types.Message, state: FSMContext):
    await state.update_data(s1=message.text)
    await message.answer("2. Qaysi kursda o'qiysiz? (masalan: 1-kurs, 2-kurs)")
    await state.set_state(SorovnomaState.s2)

@dp.message(SorovnomaState.s2)
async def q3(message: types.Message, state: FSMContext):
    await state.update_data(s2=message.text)
    await message.answer("3. Qaysi yo'nalishda tahsil olasiz?")
    await state.set_state(SorovnomaState.s3)

@dp.message(SorovnomaState.s3)
async def q4(message: types.Message, state: FSMContext):
    await state.update_data(s3=message.text)
    await message.answer("4. Texnikumdagi dars jarayonlari va muhitidan qoniqasizmi? (Ha/Yo'q/Qisman)")
    await state.set_state(SorovnomaState.s4)

@dp.message(SorovnomaState.s4)
async def q5(message: types.Message, state: FSMContext):
    await state.update_data(s4=message.text)
    await message.answer("5. O'qituvchilarning dars tushuntirish malakasini 5 ballik tizimda baholang:")
    await state.set_state(SorovnomaState.s5)

@dp.message(SorovnomaState.s5)
async def q6(message: types.Message, state: FSMContext):
    await state.update_data(s5=message.text)
    await message.answer("6. Texnikumdagi axborot texnologiyalari (kompyuter xonalari) holati sizni qoniqtiradimi?")
    await state.set_state(SorovnomaState.s6)

@dp.message(SorovnomaState.s6)
async def q7(message: types.Message, state: FSMContext):
    await state.update_data(s6=message.text)
    await message.answer("7. Kutubxona va o'quv adabiyotlari bilan ta'minlanganlik darajasi qanday?")
    await state.set_state(SorovnomaState.s7)

@dp.message(SorovnomaState.s7)
async def q8(message: types.Message, state: FSMContext):
    await state.update_data(s7=message.text)
    await message.answer("8. Amaliy mashg'ulotlar yetarlicha tashkil etilyaptimi?")
    await state.set_state(SorovnomaState.s8)

@dp.message(SorovnomaState.s8)
async def q9(message: types.Message, state: FSMContext):
    await state.update_data(s8=message.text)
    await message.answer("9. Guruhingizdagi muhit va o'rtog'ingiz bilan munosabatlaringiz qanday?")
    await state.set_state(SorovnomaState.s9)

@dp.message(SorovnomaState.s9)
async def q10(message: types.Message, state: FSMContext):
    await state.update_data(s9=message.text)
    await message.answer("10. Texnikumda o'tkaziladigan madaniy-ma'rifiy tadbirlarda qatnashasizmi?")
    await state.set_state(SorovnomaState.s10)

@dp.message(SorovnomaState.s10)
async def q11(message: types.Message, state: FSMContext):
    await state.update_data(s10=message.text)
    await message.answer("11. Oshxona (bufet)dagi narxlar va tozalik qoniqarlimi?")
    await state.set_state(SorovnomaState.s11)

@dp.message(SorovnomaState.s11)
async def q12(message: types.Message, state: FSMContext):
    await state.update_data(s11=message.text)
    await message.answer("12. Dars jadvali siz uchun qulaymi?")
    await state.set_state(SorovnomaState.s12)

@dp.message(SorovnomaState.s12)
async def q13(message: types.Message, state: FSMContext):
    await state.update_data(s12=message.text)
    await message.answer("13. Texnikumdagi tozalik va sanitariya sharoitlarini qanday baholaysiz?")
    await state.set_state(SorovnomaState.s13)

@dp.message(SorovnomaState.s13)
async def q14(message: types.Message, state: FSMContext):
    await state.update_data(s13=message.text)
    await message.answer("14. Rahbariyat va tutorlar bilan bog'lanish yoki murojaat qilish qiyinmi?")
    await state.set_state(SorovnomaState.s14)

@dp.message(SorovnomaState.s14)
async def q15(message: types.Message, state: FSMContext):
    await state.update_data(s14=message.text)
    await message.answer("15. Kelgusida o'z yo'nalishingiz bo'yicha mutaxassis bo'lib ishlay olasizmi?")
    await state.set_state(SorovnomaState.s15)

@dp.message(SorovnomaState.s15)
async def q16(message: types.Message, state: FSMContext):
    await state.update_data(s15=message.text)
    await message.answer("16. Texnikumda qo'shimcha to'garaklar (sport, tillar) tashkil etilishini xohlarmidingiz?")
    await state.set_state(SorovnomaState.s16)

@dp.message(SorovnomaState.s16)
async def q17(message: types.Message, state: FSMContext):
    await state.update_data(s16=message.text)
    await message.answer("17. Masofaviy ta'lim elementlaridan foydalanasizmi?")
    await state.set_state(SorovnomaState.s17)

@dp.message(SorovnomaState.s17)
async def q18(message: types.Message, state: FSMContext):
    await state.update_data(s17=message.text)
    await message.answer("18. Texnikum faoliyatini yaxshilash bo'yicha qanday taklifingiz bor?")
    await state.set_state(SorovnomaState.s18)

@dp.message(SorovnomaState.s18)
async def q19(message: types.Message, state: FSMContext):
    await state.update_data(s18=message.text)
    await message.answer("19. Joriy ta'lim yilidan umumiy olganda ko'nglingiz to'ldimi?")
    await state.set_state(SorovnomaState.s19)

@dp.message(SorovnomaState.s19)
async def q20(message: types.Message, state: FSMContext):
    await state.update_data(s19=message.text)
    await message.answer("20. So'nggi savol: Botimiz faoliyati yoki texnikum haqida oxirgi tilak va e'tirozlaringizni yozing:")
    await state.set_state(SorovnomaState.s20)

@dp.message(SorovnomaState.s20)
async def finish_sorovnoma(message: types.Message, state: FSMContext):
    await state.update_data(s20=message.text)
    data = await state.get_data()
    
    # Barcha javoblarni kanalga yuborish uchun yig'amiz
    report = (
        f"📊 **Yangi so'rovnoma natijasi!**\n\n"
        f"1. F.I.Sh: {data.get('s1')}\n"
        f"2. Kurs: {data.get('s2')}\n"
        f"3. Yo'nalish: {data.get('s3')}\n"
        f"4. Muhitdan qoniqish: {data.get('s4')}\n"
        f"5. Ustozlar bahosi: {data.get('s5')}\n"
        f"6. IT xonalari: {data.get('s6')}\n"
        f"7. Kutubxona: {data.get('s7')}\n"
        f"8. Amaliyot: {data.get('s8')}\n"
        f"9. Guruh muhiti: {data.get('s9')}\n"
        f"10. Tadbirlar: {data.get('s10')}\n"
        f"11. Oshxona: {data.get('s11')}\n"
        f"12. Dars jadvali: {data.get('s12')}\n"
        f"13. Tozalik: {data.get('s13')}\n"
        f"14. Rahbariyat/Tutor: {data.get('s14')}\n"
        f"15. Kelajakda ishlash: {data.get('s15')}\n"
        f"16. To'garaklar: {data.get('s16')}\n"
        f"17. Masofaviy ta'lim: {data.get('s17')}\n"
        f"18. Takliflar: {data.get('s18')}\n"
        f"19. Yildan ko'ngil to'qmi: {data.get('s19')}\n"
        f"20. Oxirgi tilak: {data.get('s20')}"
    )
    
    try:
        await bot.send_message(CHANNEL_ID, report, parse_mode="Markdown")
        await message.answer(
            "✅ So'rovnomada faol qatnashganingiz uchun rahmat! Javoblarimiz mas'ullarga yuborildi.",
            reply_markup=get_main_menu()
        )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi.", reply_markup=get_main_menu())
        print(e)
        
    await state.clear()


# ==================== MUROJAAT YUBORISH QISMI ====================

@dp.message(F.text == "✍️ Murojaat yuborish")
async def start_murojat(message: types.Message, state: FSMContext):
    await message.answer(
        "Iltimos, murojaatingiz uchun **ism va familiyangizni** kiriting:",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(MurojatState.ism)

@dp.message(MurojatState.ism)
async def process_ism(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text)
    kontakt_tugma = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📞 Telefon raqamni yuborish", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Rahmat! Endi telefon raqamingizni yuboring:", reply_markup=kontakt_tugma)
    await state.set_state(MurojatState.telefon)

@dp.message(MurojatState.telefon)
async def process_telefon(message: types.Message, state: FSMContext):
    telefon = message.contact.phone_number if message.contact else message.text
    await state.update_data(telefon=telefon)
    await message.answer("Murojaatingiz matnini yozib yuboring:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(MurojatState.matn)

@dp.message(MurojatState.matn)
async def process_matn(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ism, telefon, murojat = data.get("ism"), data.get("telefon"), message.text
    user_id = message.from_user.id
    username = f"@{message.from_user.username}" if message.from_user.username else "Mavjud emas"
    
    kanal_text = (
        f"📩 **Yangi murojaat!**\n\n"
        f"👤 F.I.Sh: {ism}\n"
        f"📞 Telefon: {telefon}\n"
        f"🔗 Username: {username}\n"
        f"🆔 ID: {user_id}\n\n"
        f"📝 Matn: {murojat}"
    )
    
    await bot.send_message(CHANNEL_ID, kanal_text, parse_mode="Markdown")
    await message.answer("✅ Murojaatingiz qabul qilindi!", reply_markup=get_main_menu())
    await state.clear()

# Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())