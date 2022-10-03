import discord
import os
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def rollDice(num, dice, mod):
  print("num: ", num)
  print("dice: ", dice)
  print("mod: ", mod)
  res = 0  
  for i in range(num):
      n = random.randint(1, dice)
      print("roll: ", n)
      res += n

  res += mod
  print("res: ", res)
  
  return res

@client.event
async def on_ready():
  print('DiceBot is live')
  
@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return

  if msg.startswith('!ping'):
    await message.channel.send('pong')
  
  elif msg.startswith('!roll '):
    str = msg.split('!roll ')
    res = None
    mod = 0
    
    try:
      roll = str[1].split('d')
      num = int(roll[0])
      try:
        d = roll[1].split(' ')
        dice = int(d[0])
        mod = int(d[1])
      except:
        dice = int(roll[1])
      res = rollDice(num, dice, mod)
    except:
      res = None

    if res == None:
      await message.channel.send('Oops')
    else:
      await message.channel.send(f'{res}')
    
  else:
    await message.channel.send('Oops')
    
client.run(os.environ['TOKEN'])