import asyncio

from config import dp, bot, commands


async def bot_working():
    # register_admin_handlers()
    register_user_handlers()
    register_admin_handlers()
    dp.include_routers(user_)
   # dp.include_routers(admin_, user_)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

    finally:
        await bot.session.close()


async def main():
    bot_task = asyncio.create_task(bot_working())
    await asyncio.gather(bot_task)


if __name__ == '__main__':
    try:
        print('Bot went to work')
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot Stopped')
