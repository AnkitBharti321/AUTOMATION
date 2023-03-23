import random


def for_the_memes():
    memes = {
        "rick_rolled": "https://pa1.narvii.com/6543/1cc43a342a90136e3c7da42fa7fac557b4c41738_128.gif",
        "you_tried": "https://media0.giphy.com/media/26ybwvTX4DTkwst6U/giphy.gif",
        "pretty_neat": "https://media3.giphy.com/media/n3p6JiIG0TzCU/giphy.gif",
        "dementors": "https://media4.giphy.com/media/aZeFIjI9hNcJ2/giphy.gif",
        "im_trying": "https://media1.tenor.com/images/8a7473b6b4aa49ae3fd108ca9e7c055f/tenor.gif",
        "this_is_fine": "https://media.tenor.com/images/3f4e7ecf480bda2915c82179023cf07f/tenor.gif",
        "creepy": "https://tenor.com/view/creepy-guy-behind-plant-hide-gif-11543382.gif"
    }
    return random.choice(list(memes.values()))
