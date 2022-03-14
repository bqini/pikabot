import nextcord
from discord.ext import commands

bot = commands.Bot(activity=nextcord.Game(name='prefix }'),command_prefix="}", case_insensitive=True)

@bot.event
async def on_ready():
    print("sex isnt cool virginity is awesome")



@bot.command(name="hi")
async def example_command(context):
    await context.send("Hey all, Scott here and im back!")


@bot.command(name="nsfw")
async def my_nsfw_command(context):
        await context.send("https://tenor.com/view/vorzek-vorzneck-oglg-og-lol-gang-gif-24901093")
@bot.command(name="stupid")
async def example_command(context):
    await context.send("sex")

@bot.command(name="mumei")
async def example_command(context):
    await context.send("fine https://media.discordapp.net/attachments/836441425151393816/920917864297410630/lzzkck3sq3s71.png?width=381&height=670")

@bot.command(name="onisaur")
async def example_command(context):
    await context.send("https://cdn.discordapp.com/attachments/836441425151393816/920921046411014175/image_2021-11-06_023708.jpg")

@bot.command(name="amongus?")
async def idk_man(context):
    await context.send("https://c.tenor.com/PNPcRrIeLkwAAAAC/youtooz-among-us.gif")


@bot.command(name="freegames.com")
async def never_gonna_let_you_pirate(context):
    await context.send("https://media.discordapp.net/attachments/744791642636156928/757077633933770862/image0.gif")

@bot.command(name="day")
async def monado_monday_people(context):
    await context.send("https://tenor.com/view/monado-monday-monday-shulk-xenoblade-xenoblade-chronicles-gif-22809686")

@bot.command(name="time")
async def its_always_reyn_time(context):
    await context.send("https://preview.redd.it/1a0zn2rphz051.jpg?width=640&crop=smart&auto=webp&s=e6b1a736c163dd6dce61261a947e4993a1421708")

@bot.command(name="rex_smug")
async def rex_smug(context):
    await context.send("https://media.discordapp.net/attachments/948620463192551467/952001380304953425/processed-b97745ad-d975-4856-8869-05cf6d823c0e_GmKfzaD7.jpeg")

@bot.command(name="updates")
async def wanna_see_changes(context):
    await context.send("3/12/22 10:36 added america command. 3/12/22 20:20 added everyone command. 3/12/22 20:21 added jesse_gay command. 3/12/22 23:00 added ping and blow_phone_now command. 3/13/22 16:9 removed jesse_gay command replaced with no_maidens? command.")

@bot.command(name="america")
async def guns_are_very_america(context):
    await context.send(":gun:")

@bot.command(name="everyone")
async def mario_rabbis_pretty_cool(context):
    await context.send("@everyone gamers I got mario + rabbids and bug fables")

@bot.command(name="rex_scream")
async def AHHHHHHHHHHHH(context):
    await context.send("https://cdn.discordapp.com/attachments/949673515139858475/952389309573501008/Y2Mate.is_-_Rexs_Scream-bCoLf76dVMA-48k-1647137633838_1.mp3")

@bot.command(name="ping")
async def sussy_amogus(context):
    await context.send("@everyone")


@bot.command(name="blow_phone_now")
async def blow_the_phone_like_its_C4(context):
    await context.send("@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone")

@bot.command(name="no_maidens?")
async def no_maidens(context):
    await context.send("https://cdn.discordapp.com/attachments/512014380179783691/952662939825999932/20220226_000059.jpg")

@bot.command(name="britan_sucks")
async def you_mean_football(context):
    await context.send("https://media.discordapp.net/attachments/948620463192551467/952662738381996073/meme.png")

bot.run("feel free to use my code put your bots token here and make sure to remove it when you post it")
