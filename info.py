import discord
from datetime import datetime
from discord.utils import get
import mysql.connector
async def msg(message, x, p, self):
    msg = x
    #Check if the message was sent by ourselves:
    if msg.author == self.user:
        print('Not a user message.')
        return
    #If not, we can execute commands, such as this simple ping!

    cmd = message.split()
    validcommands = [p+ "info", p+ "help", p+ "invite", p+ "s", p+ "u", p+"prefix"]

    if not cmd[0].lower() in validcommands:
        return

    #Connect to database
    db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "dante"
)

    if message.startswith(p + "prefix"):
        if not msg.guild.owner_id == msg.author.id:
            embed = discord.Embed(title = "No Permission!", description = "You do not have permission to change the prefix in " + str(msg.guild.name) , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
            return
        try:
            sql = "INSERT INTO guilds (guildid, prefix) VALUES (%s, %s)"
            val = (msg.guild.id, str(cmd[1]))
            mycursor = db.cursor()
            mycursor.execute(sql, val)
            db.commit()
            print(mycursor.rowcount, "record inserted.")
        except:
            sql = "UPDATE guilds SET prefix = %s WHERE guildid = %s"
            val = (str(cmd[1]), msg.guild.id)
            mycursor = db.cursor()
            mycursor.execute(sql, val)
            db.commit()
            print(mycursor.rowcount, "record updated")

    if message == p + "info":
        embed = discord.Embed(title = "Info", description = 'Made by: Darkmane Arweinyd \nWith help by: Alex Malebogh \n\nBeta testers: Kyrpto the superdog, Tyler Furrison, Alex Malebogh, Jessa, The Floof Hotel Staff Team & Users\n\nPing: ___Took {0}'.format(round(self.latency, 1)) + "ms___" , color=0x00ff00)
        await msg.channel.send(embed = embed)

    if message == p + "help":
            embed = discord.Embed(title = "Info", description = 'Commands: https://github.com/dantefurrybot/dantev4/blob/beta/help.md\nMade by: Darkmane Arweinyd \nWith help by: Alex Malebogh \n\nPing: ___Took {0}'.format(round(self.latency, 1)) + "ms___" , color=0x00ff00)
            await msg.channel.send(embed = embed)

    if message == p + "invite":
            embed = discord.Embed(title = "Invite", description = 'Invite: https://discordapp.com/oauth2/authorize?client_id=548269826020343809&scope=bot&permissions=93190\nMade by: Darkmane Arweinyd \nWith help by: Alex Malebogh \n\nPing: ___Took {0}'.format(round(self.latency, 1)) + "ms___" , color=0x00ff00)
            await msg.channel.send(embed = embed)

    if message == p + "s":
        embed = discord.Embed(title=msg.guild.name, color=0x00ff00)
        embed.add_field(name="Owner", value=msg.guild.owner, inline=False)
        embed.add_field(name="Date of creation", value=msg.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.add_field(name="Region", value=msg.guild.region, inline=False)
        embed.set_thumbnail(url = msg.guild.icon_url)
        await msg.channel.send(embed=embed)

    if message.startswith(p + "u"):
        for user in x.mentions:
                embed = discord.Embed(description = str(user.name) + "#" +str(user.discriminator) , color = 0x00ff00)
                embed.set_thumbnail(url = user.avatar_url)
                embed.add_field(name = "Name:", value = user.display_name, inline = True)
                embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = True)
                embed.add_field(name = "Date Joined:", value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = True)
                await msg.channel.send(embed = embed)
