from discord.ext import commands,menus
import discord
import collections
import aiohttp
import matplotlib.pyplot as plt
import os
import asyncpg
async def connect():
    bot.pg_con = await asyncpg.connect(host='aws.cqnrr2qkkpix.us-east-2.rds.amazonaws.com',database='dagbot',user='postgres',password='ARnav123#')
async def cogcache():
    bot.cogdata = await bot.pg_con.fetch("""
SELECT * FROM cogcheck;""")
cmdhelp = {'clapify':'*inert slow clap*','monospace':'adds a black box around text to make it fancy','under':'__underlines text__','blue':'makes text blue in color','orange':'makes text orange in color','yellow':'makes text yellow color','green':'makes text green in color','cyan':'makes text cyan in color','red':'makes text red','spoiler':'text in a black box to click','box':'puts text in a BBB','bold':'**makes text bold**','italics':'*puts text in italics*','striked':'~~strikes the text~~','emojify':'every letter is replaced by an emoji','ping':"SHows the bot's latency",'test':'testing.....testing..123','dadjoke':'A joke only a dad would tell','yomama':'insult yo mama','cn':'I <3 chcuk norris','joke':'Random joke to make you :kek:','highfive':'initiate the high5','udef':'gets an urban dictionary definiton','bacon':'play the oracle of bacon sand get the bacon number of an actor','gif':'get a gif menu for a query','cf':'geta fun fact about a cat','nou':'UNO REVERSE CARD','wrongopinion':'bruh','f':'f in the chat for thing','hug':'give a user a big hug','advice':'get advice from dagbot','slap':'give a user a big slap','rate':'Have me rate someone **everything final**','dog':'get a cute doggo','cat':'cute catpic','rps':'rock-paper-Scissors-shoot','russianroulette':'lets dance with death','trivia':'MCQ trivia','jeopardy':'Fun game','hangman':'Use hangman help','numgame':'fun number guessing game','google':'get a google search result','weather':'get live weather of a city','randomint':'random integer is generated','taco':'random taco recipe','wikipedia':'get wikipedia results','youtube':'get a you tube result for a query','define':'get a dictionary define for word','quote':'famous quote from database','hp':'use hp help for harry potter','fact':'get a kickass fact','numfact':'get a random number fact','numsearch':'get a number fact for a particluar number','pokedex':'get pokedex info for pokemon','poem':'get a poem from a title'
,'meme':'r/meme','dankmeme':'r/dankmemes','thought':'r/Showerthoughts','askreddit':'r/AskReddit','greentext':'from r/greentext','rip':'f in the chat for thing','catfact':'Get a fact on a cat','panda':'get a cude panda pic','fox':'get a swett fox pic','racoon':'racoon pic?','reverse':'!poow ,ffuts esreveR','reaction':'get your slow ass reaction time','yoda':'Yoda speak, you will get','oeis':'Online Encyclopedia of Integer Sequences','aww':'r/aww','dex':'r/DankExchange','pun':'r/puns', 'starwarsmeme':'r/PrequelMemes','discord':'r/Discordmemes','comic':'r/comics','copypasta':'r/copypasta'}

emojilist = {'text':'\U0001f1f9','games':'\U0001f3b2','reddit':'\U0001f534','image':'\U0001f5bc','util':'\U0001f5a5','smart':'\U0001f9e0','fun':'\U0001f973','animals':'\U0001f436','Help':'\U00002753','tags':'\U0001f4c1','meta':'\U0001f6e0','memes':'\U0001f58d','Jishaku':'\U000026a0','ai':'\U0001f916'}
bot = commands.Bot(command_prefix = commands.when_mentioned_or('..'))
extensions = ['text','fun','imag','redditscrap','games','util','whysomart','animals','memes','ai']
class MyHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        ctx = self.context
        guild = ctx.guild
        pre = '.'
        embed = discord.Embed(
            color=guild.me.color,
            title=f"DAGBOT HELP",
            description=f"You can use {pre}help <command>/<category> for help with specific commands."
        )

        for cog in ctx.bot.cogs.values():
            emj = emojilist[f'{cog.qualified_name}']
            embed.add_field(name=f'{emj}  **{cog.qualified_name}**',value=f"`{cog.__doc__}`",inline=True)
        embed.add_field(name='FURTHER INFO',value='''
        `COMMAND PREFIX:` `{}`
        `prefix help` To get info about orefix related commands
        `tag help`: Tags a very large commands griup with a help menu'''.format('gay'))
        await ctx.send(embed=embed)

    async def send_cog_help(self, cog):
        ctx = self.context
        sp = 15
        cog_commands = cog.get_commands()
        cmlist = ''
        if len(cog_commands) == 0:
            return await ctx.send("This cog doesn't have any commands for some reason.")
        #command.clean_params
        pre = '.'
        if cog.qualified_name == 'image':
            addi = 'TRY THEM AND SEE, CANNOT EXPLAIN'
        else:
            addi = ''
        embed = discord.Embed(
            color=0x7289DA,
            title=f"{cog.qualified_name} help\n{addi}",
        )
        for command in cog_commands:
            my_ord_dict = (command.clean_params)
            param = ''
            for key,value in my_ord_dict.items():
                p = str(value)
                if '=' in p:
                    param = param + ' '+f'<{key}>'
                else:
                    param = param +' '+ f'[{key}]'
            try:
                file = cmdhelp[f'{command}']
            except:
                if cog.qualified_name == 'image':
                    des = ''
                else:
                    des = "My lazy ass owner didn't add help to this command."
            else:
                print(file)
                des = file
            print(param)
            toadd = f'`{command.name} {param}`'
            sp = 20-len(toadd)
            spc = (sp*' ')
            cmlist = cmlist+toadd+f'{spc}{des}'
            if isinstance(command, commands.Group):
                cmlist += "\u200b 🞵\n"
            else:
                cmlist += "\n"

        embed.description = cmlist
        embed.set_footer(text=f"🞵 means that the command listed is a Group. Use {ctx.prefix}help <group> for help with its subcommands.")
        await ctx.send(embed=embed)

    async def send_command_help(self, command):
        ctx = self.context
        guild = ctx.guild
        embed = discord.Embed(
            color=guild.me.color,
        )
        my_ord_dict = (command.clean_params)
        param = ''
        for key,value in my_ord_dict.items():
            p = str(value)
            if '=' in p:
                param = param + ' '+f'<{key}>'
            else:
                param = param +' '+ f'[{key}]'
        embed.title = f'{command.name}{param}'
        try:
            embed.description = cmdhelp[f'{command}']
        except:
            embed.description = "My lazy ass owner didn't add help to this command."
        alis = command.aliases
        if len(alis)==0:
            alis = 'none'
        embed.add_field(name='Aliases',value=str(alis))
        embed.add_field(name='Command Group',value = command.cog_name)


        return await ctx.send(embed=embed)


async def getkeydict():
    wedit = (bot.cogs)
    keylist = []
    for key in wedit.keys():
       keylist.append(key)
    bot.coglist = keylist

@bot.command()
async def rejectsuggestion(ctx,id,*,reason):
    if str(ctx.author.id) == '491174779278065689':
        channel = bot.get_channel(676031268009410570)
        y = await channel.fetch_message(id)
        oldemb = y.embeds[0]
        descrip = str(oldemb.description)
        oldtit = oldemb.title
        print(descrip)
        print(oldtit)
        newemb = discord.Embed(title=f'SUGGESTION REJECTED',description=descrip)
        newemb.add_field(name='Reason', value=reason)
        await y.edit(embed=newemb)
    else:
        await ctx.send('Only Daggy1234 has this ability, sorry')
@bot.event
async def on_message(message):
    channel = message.channel
    #id = message.guild.id
    #for e in bot.prefdict:
    #        if e['server_id'] == str(id):
    #            prefix  = (e['command_prefix'])
    #            break
    prefix = '.'
    ctx = await bot.get_context(message)
    if not ctx.valid:
        if bot.user.mentioned_in(message):
            embed = discord.Embed(title='You hit me up?',description=f'''
    My Prefix for this server is: `{prefix}`

    Use the help command to get smart enough to use me: `{prefix}help` ''',color=message.guild.me.color)
            embed.add_field(name='Support Server',value='[Invite Link](https://discord.gg/grGkdeS)')
            embed.add_field(name='Invite Link',value='[Click me](https://discordapp.com/api/oauth2/authorize?client_id=675589737372975124&permissions=378944&scope=bot)')
            await channel.send(embed=embed)
    await bot.process_commands(message)


@bot.command()
async def approvesuggestion(ctx,id):
    if str(ctx.author.id) == '491174779278065689':
        channel = bot.get_channel(676031268009410570)
        y = await channel.fetch_message(id)
        oldemb = y.embeds[0]
        descrip = str(oldemb.description)
        oldtit = oldemb.title
        print(descrip)
        print(oldtit)
        newemb = discord.Embed(title=f'SUGGESTION APPROVED',description=descrip)
        await y.edit(embed=newemb)
    else:
        await ctx.send('Only Daggy1234 has this ability, sorry')
@bot.command(aliases=['sugg','idea'])
async def suggest(ctx,*,suggest):
    guild = ctx.guild
    fro = guild.name
    auth = ctx.author.display_name
    embed = discord.Embed(title='DAGBOT SUGGESTION ADDED',description=f'```yaml\n{suggest}\n```\n**FROM:***{auth}\n**SERVER:**{fro}',color=ctx.guild.me.color)
    embed.add_field(name='SENT', value="Your SUGGESTION has been added to the Support server")
    embed.add_field(name='Support Server',value='[Join Now](https://discord.gg/5Y2ryNq)')
    channel = bot.get_channel(676031268009410570)
    msg = await channel.send(embed=embed)
    await ctx.send(embed=embed)
    await msg.add_reaction('\U00002705')
    await msg.add_reaction('\U0000274c')
class meta(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.group(invoke_without_command=True)
    async def cog(self,ctx):
        await ctx.send('Please use cog help to get started!')
    @cog.command()
    @commands.cooldown(1,10,commands.BucketType.guild)
    async def enable(self,ctx,*,cog):
        if str(cog) in bot.coglist:
                id = str(ctx.guild.id)
                await bot.pg_con.execute("""
            UPDATE cogcheck
            SET {}='y'
            WHERE serverid = '{}';""".format(str(cog),id))
                await cogcache()
                await ctx.send(f'We have enabled the cog {cog}')

        else:
            await ctx.send('The cog you have entered does not exist')
    @cog.command()
    @commands.cooldown(1,10,commands.BucketType.guild)
    async def disable(self,ctx,*,cog):
        if str(cog) in bot.coglist:
                id = str(ctx.guild.id)
                await bot.pg_con.execute("""
            UPDATE cogcheck
            SET {}='n'
            WHERE serverid = '{}';""".format(str(cog),id))
                await cogcache()
                await ctx.send(f'We have disabled the cog {cog}')

        else:
            await ctx.send('The cog you have entered does not exist')
    @cog.command()
    async def status(self,ctx):
        id = ctx.guild.id
        embed = discord.Embed(title='COG STATUS FOR THIS SERVER',color = ctx.guild.me.color)
        mstr = ''
        for c in bot.cogdata:
            if str(c['serverid']) == str(id):
                for e in bot.coglist:
                    if c[e]:
                        kwrd = ': Enabled'
                    else:
                        kwrd = ': Disabled'
                    mstr = mstr+'\n'+f'{e}:{kwrd}'
        embed.description = mstr
        await ctx.send(embed=embed)
    @cog.command()
    async def help(self,ctx):
        await ctx.send('''`
        Cog Commands:
        A cog is a command category, you can enable or disable cogs and all of the commands inside them. Use the help menu to see all the available cogs. NOTE Meta and Help cogs cannot be disabled.
        cog enable <cog> : enables the cog to be used
        cog disable <cog> : disabled the cog
        cog status <cog>: shows teh status on wether a cog is enabled or disabled`''')
class Help(commands.Cog):
    """YOU ARE ALDREADY HERE"""
    def __init__(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self
    @commands.command()
    async def helpdm(self,ctx):
        await ctx.trigger_typing()
        channel = ctx.channel
        guild = ctx.guild
        id = ctx.guild.id
        sender = ctx.author
        embed = discord.Embed(title="DAGBOT - HELP", color=guild.me.color)
        embed.add_field(name="HELP COMMANDS-fun",value='''
    `help` shows this message
    `test` checks wether bot functions correctly
    `ping` checks the ping of bot
    `dadjoke` shares dad joke from online
    `peace` bot opinion on peace
    `yomama` outputs yomama joke
    `slap <user>` slaps them
    `rate <thing>` rates it
    `advice ` get advice from DAGBOT
    `cn` get chuck norris joke
    `cat` gets a cute cat pic''',inline=True)
        embed.add_field(name="HELP COMMANDS-fun",value='''
    `joke` gets a random joke
    `bacon <actor>` gets info from the oracle of bacon
    `war` bot opinion on war
    `highfive` bot high-fives you
    `udef <word>` shares definition from urban dictionary
    `define <word>` shares definition of word from dictionary
    `hug <user>` hugs them
    `gif <query>` finds top 3 gifs with search
    `cf/catfact` get a random ctafact
    `f <thing>` get an f for thing and see hoe people react
    `dog` gets a cute dogpic''',inline=True)
        await sender.send(embed=embed)
        embed = discord.Embed(title="DAGBOT - HELP-REDDIT", color=0xfa780e)
        embed.add_field(name='Commands', value='''
        `meme` gets a meme from r/meme
        `dankmeme` gets a meme from r/dankmeme
        `thought` gets a thought from r/shower thought
        `topic` gets a topic from r/AskReddit
        `greentext` gets a 4chan post via r/greentext''',inline=False)
        await sender.send(embed=embed)
        embed = discord.Embed(title="DAGBOT - HELP-SMART/GEEK", color=0xf5ea12)
        embed.add_field(name='Commands', value='''
    `quote` shares a quote
    `numfact` gets a random fact about number
    `numsearch <number>` gets a fact about a particluar number
    `fact` shares a random fact
    `pokedex <pokemon name/id>` get the data for a pokemon or id
    `hp help ` gives more information on the harry potter command library''',inline = True)
        await sender.send(embed=embed)
        embed = discord.Embed(title="DAGBOT - HELP - GAMES", color=0xfd40f4)
        embed.add_field(name='Commands', value='''
    `jeopardy` play JEOPARDY
    `yoda <text>` turns input text into yodish
    `numgame` play a fun number game
    `rr <number of slots (default is 6)>` play russian roulette
    `rps` play rock paper Scissors''',inline = True)
        await sender.send(embed=embed)
        embed = discord.Embed(title="DAGBOT - UTILITIES",color=0x33d360)
        embed.add_field(name='UTILITIES', value='''
    `weather <city>` get the real time weather
    `google <query>` get the top 5 search results in a cool menu
    `random <start> <end>`get a random integer within range
    `taco` gets a random taco with recipe
    `tag help` to use tags! a nifty feature and 13 subcommand''')
        await sender.send(embed=embed)
        embed = discord.Embed(title='DAGBOT - Text Manipulation',color=0x230cfb)
        embed.add_field(name='Commands',value='''
    `bold <text>` makes text bold
    `italics <text> ` makes text italics
    `box <text>` puts the text in a infobox
    `clapify <text>` you know
    `emojify <text>` makes the text using emojis
    `strike <text>` strikes the Text
    `spolier <text>` turns text into a spolier
    `monospace <text>` makes text monospace''')
        await sender.send(embed=embed)

        embed = discord.Embed(name='DAGBOT Config/Info',color=0x00ffff)
        embed.add_field(name='Commands',value='''
        `COMMAND PREFIX:` `{}`
        `prefix help` To get info about orefix related commands
        `enablespam` To enable Dagbot replying to messages with no commands
        `disablespam` To disable dagbot replying to non-COMMANDS'''.format('.'))
        await ctx.send('Help command sent')
    def cog_unload(self):
        self.bot.help_command = self._original_help_command





       

@bot.command()
@commands.cooldown(1,10,commands.BucketType.user)
async def dexuv(ctx,*,pid):
    url = f'https://uz9t4q6y9j.execute-api.eu-west-1.amazonaws.com/prod/{pid}'
    print(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            js = await r.json()

            try:
                it = len(js['x'])-1
            except:
                await ctx.send('No data, please enter a valid post id from r/DankExchange')
            else:
                plt.xlabel('Time in Minutes')
                plt.ylabel('Upvotes')
                x = js['x']
                y = js['y']
                plt.plot(y,color='black', marker='o', linestyle='dashed',linewidth=1, markersize=6)
                plt.savefig(f'{pid}graph.png')
                plt.close()
                file = discord.File(f'{pid}graph.png',filename='graph.png')
                embed = discord.Embed(title=f'Upvote Graph for {pid}')
                embed.set_image(url="attachment://graph.png")
                embed.set_footer(text='Powered by C🅰ri🅱🅾s🅰urus#0834 Dank Exchange API')
                await ctx.send(file=file,embed=embed)
                os.remove(f'{pid}graph.png')
        
@bot.event
async def on_ready():
    #bot.add_cog(gettingdb(bot))
    bot.add_cog(Help(bot))
    bot.add_cog(meta(bot))
    
    print('bot online')
if __name__ == '__main__':
    bot.load_extension("jishaku")
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print(f'{extension} cannot be loaded due to {error}')
        else:
            print(f'loaded extension {extension}')
bot.loop.run_until_complete(connect())
bot.loop.run_until_complete(cogcache())
bot.loop.run_until_complete(getkeydict())
print(bot.cogdata)
bot.run('Njc1OTM3NzQyNjM4ODA5MDg5.XlvdUw.Ru5H8y0sVGb9758ZdNSJY5TX0aM')
