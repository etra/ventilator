from ventilator.client import Client as ClientInterface
from discord import Client as DiscordClient, Intents, Message


class Client(ClientInterface):

    _client: DiscordClient = None

    def __init__(self, app):
        super(Client, self).__init__(app=app)

    @property
    def client(self) -> DiscordClient:
        if not self._client:
            intents = Intents.default()
            intents.message_content = True
            self._client = DiscordClient(intents=intents)
            self._client.event(self.on_message)
        return self._client

    def run(self):
        self.client.run(token=self.app.config.DISCORD_TOKEN)

    async def on_message(self, message: Message):
        return
        #todo: after message is cleared and it's clear what we need todo (send it to self.app.on_message(....)) resceived response will be used as message to send to channel

        # if message.author.bot:
        #     self.app.log.info(f'Ignoring bots')
        #     return
        #
        # if message.thread.id:
        #     self.app.log.info(f'Ignoring threads')
        #     return
        #
        # if self.user in message.mentions:
        #     await self.handle_mention(message)
        #
        # if message.guild is None:
        #     await self.handle_dm(message)
        # await message.channel.send("123")
        # response = self.app.on_message(....)
        # if response:
        #     await message.channel.send(response)

#
# if __name__ == '__main__':
#     intents = Intents.default()
#     intents.message_content = True
#
#     client = MyClient(intents=intents)
#     client.gpt = MyGPT()
#
#
#
#
#
#
#
#
#
#
#     client.run(token='')
#         return
#
# #
# class MyClient(Client):
#
#     gpt: MyGPT = None
#
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')
#
#     async def handle_mention(self, message: Message):
#         print('mentions')
#         print(message)
#         print(message.content)
#         print(message.id)
#         print(message.channel.id)
#         await message.create_thread(
#             name=f"Thread for: {message.content}"
#         )
#
#         return None
#
#     async def handle_dm(self, message: Message):
#         #todo: this do not support threads Do we whant to continue with implementation...
#         # await message.create_thread(name="ok")
#         await message.reply(f"You say: {message.content}")
#         print('dm')
#         # return None
#
#     async def on_message(self, message: Message):
#         if message.author.bot:
#             print(f'Ignoring bots')
#             return
#
#         if self.user in message.mentions:
#             await self.handle_mention(message)
#
#         if message.guild is None:
#             await self.handle_dm(message)


