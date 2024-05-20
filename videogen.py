import discord
import random
import requests
from discord.ext import commands
from discord import app_commands
import json

class videogencmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    def parse(text):
    try:
        return json.loads(text)
    except ValueError as e:
        await inter.response.send_message('invalid code: %s' % e ephemeral=True)
        return None # or: raise




    @app_commands(name="permcode")
    async def title(self, inter: discord.Interaction):
    	print("[Logs] Generating a 1 day code for someone")
    	code1 = random.randomint(10,1000)
    	code2 = random.randomint(10,1000)
    	code3 = random.randomint(10,1000)
    	code4 = random.randomint(10,1000)
    	await inter.response.followup(f"You code is {code1}{code2}{code3}{code4}")
    	print("[Logs] Code Sucsessfully Generated, and sent to the command user"ephemeral=True)
		data = "perm"
		with open(f'{code1}{code2}{code3}{code4}', 'w', encoding='utf-8') as f:
    		json.dump(data, f, ensure_ascii=False, indent=4)
    @app_commands(name="redeem")
    async def redeem(self, inter: discord.Interaction, code: int):
    	text = int
    	parse()
    	if json.loads == "perm":
    		print("[Logs] Someone is Redeeming a  code")
    		    member = inter.author
    		 = get(member.server.roles, name="perm")
    			await bot.add_roles(member, role)















async def setup(bot):
    await bot.add_cog(videogencmds(bot))