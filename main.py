import discord
from keep_alive import keep_alive
class MyClient(discord.Client):

    async def on_ready(self):
        print('bot is online now', self.user)

    async def on_message(self, message):
        word_list = ['black','enter the black listed words']


        if message.author == self.user:
            return

        messageContent = message.content
        if len(messageContent) > 0:
            for word in word_list:
                if word in messageContent:
                    await message.delete()
                    await message.channel.send('Do not say that!')

     

keep_alive()
client = MyClient()
client.run('you_bot_token')