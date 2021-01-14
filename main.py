import discord
from util import read_json, write_json


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author.bot is False:
            try:
                prefix = str(read_json("data/prefix.json")[str(message.guild.id)])
                print("prefix: " + prefix)
            except KeyError:
                print("No saved prefix has been found")
                prefix = "!"

            print("message send by \"" + str(message.author) + "\" the message is \"" + str(message.content) +
                  "\" prefix for this user is \"" + str(prefix) + "\"")

            if message.content == prefix + 'user info':
                await message.channel.send(str(message))

            if message.content == prefix + "sex":
                await message.channel.send("Please enter me")

            elif message.content == prefix + "member id":
                await message.channel.send(str(message.author.id))

            elif message.content == prefix + "balance" or message.content == prefix + "bal" \
                    or message.content == prefix + "g" or message.content == prefix + "gold" \
                    or message.content == prefix + "money":
                try:
                    await message.channel.send("You have a balance of {} gold.".format(str(read_json("data/players.json")[str(message.author.id)]["Money"])))
                except KeyError:
                    temp_dict = read_json("data/players.json")
                    temp_dict[str(message.author.id)] = read_json("data/default_player.json")
                    await message.channel.send("Hello I see your new to the game. You start of with 1000 gold.")
                    write_json("data/players.json", temp_dict)
                    del temp_dict

            elif message.content == 'ping':
                await message.channel.send('pong')

            elif message.content.startswith(prefix + "change prefix "):
                prefix = str(message.content.removeprefix(prefix + "change prefix "))
                prefix_dict = read_json("data/prefix.json")
                prefix_dict[str(message.guild.id)] = prefix
                write_json("data/prefix.json", prefix_dict)
                del prefix_dict
                await message.channel.send("new prefix: " + prefix)
                print("new prefix \"" + prefix + "\" for server \"" + message.guild.name + "\"")

            elif "porn" in message.content:
                await message.channel.send("You really need pornhub.com or nhentai.net")

            if str(message.author.id) == "MY DISCORD ID":
                if message.content.startswith(prefix + "give money to"):
                    temp_dict = read_json("data/players.json")
                    temp_member_id = str(message.content.removeprefix(prefix + "give money to "))
                    try:
                        temp_dict[temp_member_id]["Money"] += 1000
                    except KeyError:
                        temp_dict[temp_member_id] = read_json("data/default_player.json")
                        temp_dict[temp_member_id]["Money"] += 1000
                    write_json("data/players.json", temp_dict)
                    await message.channel.send("You have given player {} 1000 gold".format(temp_member_id))
                    del temp_dict
                    del temp_member_id
                elif message.content == prefix + "who is the owner of this bot":
                    await message.channel.send("You are you dickhead.")


client = MyClient()
client.run('DISCORD BOT TOKEN')
