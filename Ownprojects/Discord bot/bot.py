import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('Bot is ready')


@client.event
async def on_member_join(member):
    print(member, "has joined the server")


@client.event
async def on_member_remove(member):
    print(member, "has left the server")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    print("Ping executed")


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    print("8ball executed")

@client.command()
async def clear(ctx, amount=1):
    amount += 1
    await ctx.channel.purge(limit=amount)
    print("Clear executed")


@client.command()
async def bee(ctx):
    await ctx.send("""
    According to all known :speaking_head: laws :hammer: :writing_hand: of aviation :airplane:, there is no :x: way that a bee :bee: should be able :heavy_check_mark: to fly :butterfly: :bee: . Its wings :wind_blowing_face: are too small :white_small_square: to get its fat :busts_in_silhouette: little body :boy: off the ground :beach_umbrella: . The bee :bee: , of course, flies :wind_blowing_face: anyway. Because bees :bee: don’t :x: care :no_good: what humans :couple: think is impossible :no_entry_sign: .” SEQ. 75 - “INTRO TO BARRY” INT. BENSON HOUSE - DAY ANGLE ON: Sneakers :athletic_shoe: on the ground :earth_americas: :beach_umbrella: . Camera :movie_camera: PANS UP :arrow_up: to reveal :hushed: BARRY BENSON’S BEDROOM :bed: ANGLE ON: Barry’s hand :hand_splayed: flipping :middle_finger: through different sweaters :shirt: in his closet:closed_umbrella: . BARRY Yellow :yellow_heart: black :black_heart: , yellow :yellow_heart: black :black_heart: yellow :yellow_heart: black :black_heart: yellow :yellow_heart: black :black_heart: yellow :yellow_heart: black :black_heart:, yellow :yellow_heart: black :black_heart: ...oohh, black :black_heart: and yellow :yellow_heart:... ANGLE ON: Barry wearing the sweater :shirt: he picked :thinking: , looking :eyes: in the mirror . BARRY (CONT’D) Yeah :white_check_mark: , let’s shake :handshake: it up :arrow_up_small: a little :white_small_square: . He picks :eye: the black :black_heart: and yellow :yellow_heart: one :one: . He then goes :walking: to the sink :potable_water: , takes the top :top: off :mobile_phone_off: a CONTAINER :wastebasket: OF HONEY :honey_pot: , and puts some honey :honey_pot: into his hair :haircut: . He squirts :sweat_drops: some in his mouth :lips: and gargles :anger_right: . Then he takes :head_bandage: the lid :level_slider: off the bottle :champagne: , and rolls :newspaper2: some on like deodorant :snowflake: . CUT :scissors: TO :two: : INT. BENSON HOUSE :house
    """)


@client.command()
async def loop(ctx):
    while True:
        await ctx.send("epstein didn't kill himself | " * 10)


client.run('NjkyNzgxODQzNzI4MTcxMDA4.Xnzhiw.tKy_TqnnkVHJ-JE9RtoKbHQ_v5o')
