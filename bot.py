import discord
from discord.ext import commands
from bot_token import TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_message_delete(message):
    embed = discord.Embed(title="{} deleted a message".format(message.author.name),
                          description="", color=0xFF0000)
    embed.add_field(name=message.content, value="This is the message that they have deleted",
                    inline=True)
    channel = bot.get_channel() #put channel id here
    await channel.send(embed=embed)


@bot.event
async def on_message_edit(message_before, message_after):
    embed = discord.Embed(title="{} edited a message".format(message_before.author.name),
                          description="", color=0xFF0000)
    embed.add_field(name=message_before.content, value="before any edit",
                    inline=True)
    embed.add_field(name=message_after.content, value="after the edit",
                    inline=True)
    channel = bot.get_channel() #put channel id here
    await channel.send(embed=embed)

bot.run(token=TOKEN)