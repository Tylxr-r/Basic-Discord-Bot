import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
        await self.change_presence(
            activity=discord.Game(name="$help for commands")
        )

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        if message.author == self.user:
            return
        
        content = message.content.lower()
        content_send = message.channel.send

        if content == "$help":
            embed = discord.Embed(
                title="List of commands",
                description="$help\n$cm1\ncm2\ncm3",
                color=0XFFFFFF
            )
            await message.channel.send(embed=embed)

        elif content == ("$cm1"):
            await content_send("content")

        elif content == ("$cm2"):
            await content_send("content")

        elif content == ("cm3"):
            await content_send("content")

intents = discord.Intents.default()
intents.message_content = True

with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

client = MyClient(intents=intents)

client.run(TOKEN)
