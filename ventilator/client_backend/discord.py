from ventilator.client import Client as ClientInterface
from discord import Client as DiscordClient, Intents, Message, Thread
from datetime import datetime

class TextPart:
    def __init__(self, text: str, split_type: str = None):
        self.text = text
        self.split_type = split_type

    split_type = None
    text = None

def split_response(response: str):
    if len(response) < 2000:
        yield TextPart(response, '')
    else:
        paragraphs = response.split("\n")
        for paragraph in paragraphs:
            if len(paragraph) > 2000:
                sentences = paragraph.split(".")
                for sentence in sentences:
                    if len(sentence) > 2000:
                        words = sentence.split(" ")
                        for word in words:
                            if len(word) > 2000:
                                raise Exception("Word is too long")
                            else:
                                yield TextPart(word, ' ')
                    else:
                        yield TextPart(sentence, '.')
            else:
                yield TextPart(paragraph, '\n')

def combine_chunks(text):
    response_chunk = []
    chunk = ''
    for part in split_response(text):
        if len(chunk) + len(part.text) < 2000:
            chunk += part.split_type + part.text
        else:
            response_chunk.append(chunk)
            chunk = part.split_type + part.text

    response_chunk.append(chunk)
    return response_chunk

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

    #we need to chunk response to 2000 charecters and sent it one by one to discord thread and it should split message by paragraphs or sentences or words. (what ever is possible)
    def split_response(self, response: str):
        if len(response) < 2000:
            return [response]

        paragraphs = response.split("\n")
        for paragraph in paragraphs:
            if len(paragraph) > 2000:
                sentences = paragraph.split(".")
                for sentence in sentences:
                    if len(sentence) > 2000:
                        words = sentence.split(" ")
                        for word in words:
                            if len(word) > 2000:
                                raise Exception("Word is too long")
                    else:
                        yield sentence



        return response

    async def on_message(self, message: Message):
        if message.author.bot:
            self.app.log.info(f'Ignoring bots')
            return

        if message.guild is None:
            await message.channel.send(f"Hi {message.author.name}, I do not support DM's in Discord yet!")
            return

        #this is mention
        if self.client.user in message.mentions \
                or (isinstance(message.channel, Thread) and message.channel.owner.id == self.client.user.id):

            thread = None
            if isinstance(message.channel, Thread):
                thread = message.channel

            if thread is None:
                thread = await message.create_thread(name=f"Thread for: {message.author} {datetime.now()}")

            if thread is None:
                raise Exception("Thread is None")

            #todo clean content of @mentioons
            conversation_id = thread.id
            response = self.app.on_message(conversation_id, message.content)

            for chunk in combine_chunks(response):
                await thread.send(chunk)

        return

