import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="/q")
    await member.add_roles(role)

client.run("MTA1NzYyMTQ1MTY2ODIwOTc2Ng.GnHUX9.8KtDkcoRhKP-a4PuUC6K_Hwufso2MP2IcBXtWI")