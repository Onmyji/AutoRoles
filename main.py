import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="The name of the role you want to give to new users")
    await member.add_roles(role)

client.run("YOUR_TOKEN")
