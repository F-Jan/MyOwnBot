import os
import lightbulb
import commands


TOKEN = os.environ.get('DISCORD_TOKEN')

bot = lightbulb.BotApp(token=TOKEN)

commands.init_commands(bot)

bot.run()
