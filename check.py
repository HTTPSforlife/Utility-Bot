import discord
OWNER_IDS=[1241784498635538654]


def is_owner(ctx):
    return ctx.message.author.id in OWNER_IDS