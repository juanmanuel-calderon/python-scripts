import discord
import asyncio
import random
import sys
import os
from gtts import gTTS

client = discord.Client()
token = sys.argv[1]
client_id = sys.argv[2]

init = ['Tengo que ir a', 
        'Voy a']

polloverb = [' bañarme', 
             ' cagar', 
             ' salir con mi flaca', 
             ' hacerm★ la comida', 
             ' trabajar', 
             ' jugar Rocket League', 
             ' pedir McDonalds', 
             ' comprar regalo', 
             ' ver lucha libre', 
             ' garchar', 
             ' dormir', 
             ' comprar Coca-Cola', 
             ' llamar a Sancho',
             ' ir a la jato de mi enamorada']

time = ['', 
        ' en seis días', 
        ' mañana por la mañana', 
        ' dentro de dos horas', 
        ' la próxima semana', 
        ' en la noche', 
        ' a las ocho y media', 
        ' el sábado']

@client.event
async def on_ready():
    print('Everything went ok!')

@client.event
async def on_message(message):
    if message.content.startswith('!pollo'):
        phrase = random.choice(init) + random.choice(polloverb) + random.choice(time) + '.'
        
        tts = gTTS(text=phrase, lang='es-us')
        tts.save('tts.mp3')
        
        voice = await client.join_voice_channel(client.get_channel(client_id))
        player = voice.create_ffmpeg_player('tts.mp3')
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await voice.disconnect()  
        await client.send_message(message.channel, phrase)
        os.remove('tts.mp3')

client.run(token)