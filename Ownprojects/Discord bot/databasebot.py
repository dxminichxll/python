from discord.ext import commands
import sqlite3

client = commands.Bot(command_prefix='?')

db = sqlite3.connect("accounts.sqlite")


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def read(ctx, *, command="SELECT * FROM accounts"):
    print(command)
    try:
        for name, amount in db.execute(command):
            await ctx.send("{}: £{}0".format(name, amount/100))
    except ValueError:
        for time, name, amount in db.execute(command):
            await ctx.send("name: {}, amount: {}, time: {}".format(name, amount/100, time))
    except sqlite3.Error:
        await ctx.send("Invalid command")


@client.command()
async def insert(ctx, *, args):
    try:
        name, amount = args.split(' ')
        db.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, amount))
        db.commit()
        await ctx.send("Inserted {} into database".format(name))
    except ValueError:
        await ctx.send("Invalid command")
    except sqlite3.Error:
        await ctx.send("Invalid command")
        db.rollback()


@client.command()
async def execute(ctx, *, command):
    try:
        for row in db.execute(command):
            await ctx.send(row)
        db.commit()
        await ctx.send("Command executed")
    except sqlite3.Error:
        await ctx.send("Invalid command")


@client.command()
async def delete(ctx):
    db.execute("DELETE FROM accounts")
    db.execute("DELETE FROM history")
    db.commit()
    await ctx.send("Deleted whole database")


client.run('NjkyNzgxODQzNzI4MTcxMDA4.Xnzhiw.tKy_TqnnkVHJ-JE9RtoKbHQ_v5o')
db.close()
