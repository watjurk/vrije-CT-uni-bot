BOT_PREFIX = "Bot:"  # The bot name every time it generates a reply
USER_PREFIX = "You: "  # The name of the user every time it inputs/answers for the bot


def bot_format(x: str) -> str:  # define it as a string
    return f"{BOT_PREFIX} {x}"  # returns the string 
