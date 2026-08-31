import os
import discord
from discord.ext import commands
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in Railway Variables")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def auth(ctx):
    url = "https://animalcompany.us-east1.nakamacloud.io/"

    payload = {
  "tid": "6c0d31d7-83cf-4cf7-80fb-6e767c7a73de",
  "uid": "e2205f6c-7d06-449c-90df-8d6f217cad2a",
  "usn": "uAMyng4XNexqRWyL",
  "vrs": {
    "authID": "86b24019d46e43e98151ad1d67fe2313",
    "clientUserAgent": "SteamVR 1.88.1.3421_a3df6ce5",
    "deviceID": "6e966ac701018e17cdc3f60884880618066128bf"
  },
  "exp": 1788311304,
  "iat": 1787706274,
}

    response = requests.post(
        url,
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    print("API status:", response.status_code)
    print("API response:", response.text)

    if response.ok:
        await ctx.send("Authentication request succeeded.")
    else:
        await ctx.send(f"API request failed: `{response.status_code}`")

bot.run(BOT_TOKEN)
