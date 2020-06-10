import discord
import importlib
import mysql.connector

from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        db = mysql.connector.connect(
        host="host",
        user="user",
        passwd="",
        database = "dante"
        )

        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM guilds WHERE guildid =" + str(message.guild.id))
        myresult = mycursor.fetchall()

        prefix = ""

        if not myresult:
            prefix = "!"
        for x in myresult:
            prefix = str(x[1])

        message.content = message.content.lower()
        mentions = message.mentions
        if len(mentions) > 3:
            if not message.author.bot:
                if message.content.startswith(prefix):
                    await message.delete()
                    await message.channel.send("<@" + str(message.author.id) + "> Too many mentions!")
                    return
        fun = __import__("fun")
        await fun.msg(str(message.content), message, prefix, self)
        info = __import__("info")
        await info.msg(str(message.content), message, prefix, self)
        mod = __import__("mod")
        await mod.msg(str(message.content), message, prefix, self)
        christmas = __import__("christmas")
        await christmas.msg(str(message.content), message, prefix, self)
        food = __import__("foodanddrink")
        await food.msg(str(message.content), message, prefix, self)
        nsfw = __import__("nsfw")
        await nsfw.msg(str(message.content), message, prefix, self)
        casino = __import__("casino")
        await casino.msg(str(message.content), message, prefix, self)
        if not message.author.bot:
            if message.content.startswith("!"):
                await message.delete()

client = MyClient()
client.run('YourToken')
