## About project

This project is Discord bot. It's purpose is to handle requests sent to bot via Discord chat.
To initiate bot commands in discord you need to:
- mention bot @botname
- write dm to bot

For each mention or dm bot will respond by creating thread (private or public depending on where request was done dm or in channel). 
Using this thread bot will handle future communication by remembering the context of the conversation.



From discord we write to bot generate me a story:

Bot: if request is to generate a storey call function generate words and using this words it needs to generate a story
bot -> chat (understand what is the request) -> function generate_words -> call chat (generate words ) -> sent to user