# python-scripts
Some random python scripts I made.

Currenty contains two scripts:

- yugioh.py:

  Defines a Microsoft Excel macro (to be used with ExcelPython) that queries the yugiohprices.com API and gets the average price of a card.
  
  - Usage:
  
    With cells [LOB] and [001], it queries for 'LOB-001' (Blue-Eyes White Dragon).
    
    In case of failure in when asking the API, it returns '-'.
    
- pollobot.py

  Creates a Discord bot that generates a random excuse (in Spanish, but easily modifiable). 
  
  The bot connectes to the Discord voice channel and reads the generated excuse using gTTS (Google Text-to-Speech).
  
  - Usage:
  
    python pollobot.py [discord_token] [voice_channel_id]
