from config import TOKEN
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.reply(f"Здравствуйте, это нофап бот)))", reply_markup=kb.main)


@router.message(Command("add"))
async def new_member(message: Message, command: CommandObject):
    data = command.args
    await message.reply(f" Ну скоро типа чето там {data}")
