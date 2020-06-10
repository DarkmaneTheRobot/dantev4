import discord
import mysql.connector
async def msg(message, x, p, self):
    msg = x

    #Check if the message was sent by ourselves:
    if msg.author == self.user:
        print('Not a user message.')
        return
    #If not, we can execute commands, such as this simple ping!

    #Connect to database
    db = mysql.connector.connect(
  host="host",
  user="user",
  passwd="",
  database = "dante"
)

    if "owo" in message:
        if message == "!owo":
            print("Command")
        else:
            print("What's this?")
            try:
                sql = "INSERT INTO owo (userid, owocount) VALUES (%s, %s)"
                val = (msg.author.id, 1)
                mycursor = db.cursor()
                mycursor.execute(sql, val)
                db.commit()
                print(mycursor.rowcount, "record inserted.")
            except:
                sql = "UPDATE owo SET owocount = owocount +1 WHERE userid =" + str(msg.author.id)
                mycursor.execute(sql)
                db.commit()
                print(mycursor.rowcount, "record updated")

    cmd = message.split()
    validcommands = [p + "owo", p+ "bal"]

    if not cmd[0].lower() in validcommands:
        return

    if message == p+ "bal":
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM currency WHERE userid = '" + str(msg.author.id) + "' and guildid = '" + str(msg.guild.id) + "'")
        myresult = mycursor.fetchall()

        if not myresult:
            sql = "INSERT INTO currency (userid, guildid) VALUES (%s, %s)"
            val = (msg.author.id, msg.guild.id)
            mycursor = db.cursor()
            mycursor.execute(sql, val)
            db.commit()
            print(mycursor.rowcount, "record inserted.")
            embed = discord.Embed(title = "Your cash!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> You currently have £100" + " in the bank"
            embed.set_thumbnail(url = "https://1gb82h2px4rr3s7tp94g0nt1-wpengine.netdna-ssl.com/wp-content/uploads/2018/01/DividendInvesting.jpg")
            await msg.channel.send(embed = embed)

        for x in myresult:
            embed = discord.Embed(title = "Your cash!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> You currently have £" + str(x[2]) + " in the bank"
            embed.set_thumbnail(url = "https://1gb82h2px4rr3s7tp94g0nt1-wpengine.netdna-ssl.com/wp-content/uploads/2018/01/DividendInvesting.jpg")
            await msg.channel.send(embed = embed)

    if message == p+ "owo":
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM owo WHERE userid =" + str(msg.author.id))
        myresult = mycursor.fetchall()
        if not myresult:
            embed = discord.Embed(title = "OwO!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> You have not yet said OwO"
            embed.set_thumbnail(url = "https://i.imgur.com/YzifUxe.png")
            await msg.channel.send(embed = embed)
        for x in myresult:
            embed = discord.Embed(title = "OwO!", color=0x00ff00)
            if int(x[1]) == 1:
                embed.description = "<@" + str(msg.author.id) + "> You have said OwO 1 time."
                embed.set_thumbnail(url = "https://i.imgur.com/YzifUxe.png")
                await msg.channel.send(embed = embed)
            elif int(x[1]) > 1:
                embed.description = "<@" + str(msg.author.id) + "> You have said OwO " +  str(x[1]) + " times."
                embed.set_thumbnail(url = "https://i.imgur.com/YzifUxe.png")
                await msg.channel.send(embed = embed)
