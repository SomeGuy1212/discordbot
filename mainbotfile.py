import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

block_words = ["peepee"]


@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('Hello'):
    await msg.channel.send('Hey There')


  if msg.author != client.user:
    for text in block_words:
      if "mod" not in str(msg.author.roles) and text in str(msg.content.lower()):
        await msg.delete()
        return

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1199787003596787712))
    print(f"Bot logged in as {client.user} We UP!")

@tree.command(
  name="newcommand",
  description="My first application Command",
  guild=discord.Object(id=1199787003596787712)
)

async def first_command(interaction):
  await interaction.response.send_message("Hello!")

@tree.command(
  name="ban",
  description="bans a user",
)

async def second_command(ctx, member: discord.Member, *, reason: str):
  if reason is None:
    reason = "This user was banned by" + ctx.message.author.name
  await member.ban(reason=reason)
  print('banned')
  return



@tree.command(
  name="kick",
  description="kicks a user",
)

async def kic(ctx, member: discord.Member, *, reason: str):
  if reason is None:
    reason = "This user was banned by" + ctx.message.author.name
  await member.kick(reason=reason)
  print('kicked')

async def reply(interaction):
  await interaction.response.send_message("kicked!")
  return


client.run('MTE5Nzg3NTYxOTM4NDU0NTM3MA.GnKrgp.iYA1MJ-8gs-C-3AVygIcrK1Z34vw2jxhF8mCI8')
