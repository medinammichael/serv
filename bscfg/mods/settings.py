import bs
import bsGame
from terminal import Colors
from datetime import datetime
date = datetime.now().strftime('%d')


# Add New Prefix Commands:
prefixComand = ('/', '.', '-', '*', ',', '#', '!', '?', ';')
cmdlogs = True

enableTop5effects = True
enableTop5commands = False
enableCoinSystem = True

enableStats = True

# More Settings On setchat.py
spamProtection = True
shieldBomb = False
shieldBomb = False  # shield on bomb
bombLights = False
bombLights = False  # light on bomb

bombName = False # name on bomb

bigBomb = False  # hehe extra

k_msg = False  # Killing Message

k_pop = False  # Killing Message PopUp
nightMode = True
nightMode = True

enableChatFilter = True

showTextsInBottom = False

gameTexts = ['Welcome To Blitz Server', 'Use "/shop commands" to see commands available to buy.', 'Use "/shop effects" to see effects available and their price.', 'Use "/me" or "/stats" to see your '+bs.getSpecialChar(
    'ticket')+' and your stats in this server', 'Use "/buy" to buy effects that you like', 'Use "/donate" to give some of your tickets to other players', 'Use "/scoretocash" to convert some of your score to '+bs.getSpecialChar('ticket')+'\nCurrent Rate: 5scores = '+bs.getSpecialChar('ticket')+'1']

questionDelay = 120  # 60 #seconds
questionsList = {u'Que se consigue en el grupo de Discord?': 'billetes', 'Que puedes comprar en el server con Billetes?': 'comandos', 'Con O Sin?': 'con', 'Quien es el creador de este Servidor?': 'michael', 'Adentro o Afuera?': 'adentro', 'Eres Team Carne o Sangre?': 'sangre', 'Adentro  o Afuera?': 'afuera', 'Cuantos billetes se pueden ganar en el grupo de Discord?': 'muchos', 'Con o Sin?': 'sin', 'Eres Team Carne O Sangre?': 'carne',
                 'add': None,
                 'multiply': None}

availableCommands = {'nv': 10,
                     'gm': 1000,
                     'emote': 0,
                     'box': 30,
                     'boxall': 100,
                     'spaz': 50,
                     'spazall': 100,
                     'inv': 40,
                     'invall': 200,
                     'tex': 10,
                     'texall': 40,
                     'freeze': 100,
                     'freezeall': 300,
                     'sleep': 100,
                     'sleepall': 300,
                     'thaw': 50,
                     'thawall': 70,
                     'kill': 100,
                     'killall': 300,
                     'end': 100,
                     'hug': 60,
                     'hugall': 100,
                     'remove': 200,
                     'md': 600,
                     'fly': 100,
                     'flyall': 200,
                     'heal': 50,
                     'healall': 70,
                     'spawn': 100,
                     'dbomb': 5,
                     'zoe': 10,
                     'gp': 100}

availableEffects = {'ice': 50,
                    'sweat': 50,
                    'scorch': 50,
                    'glow': 40,
                    'distortion': 50,
                    'slime': 50,
                    'metal': 50,
                    'surrounder': 200,
                    'tag': 50,
                    'footprint': 50}

nameOnPowerUps = False  # Whether or not to show the powerup's name on top of powerups

shieldOnPowerUps = False  # Whether or not to add shield on powerups

# Whether or not to show disco lights on powerup's location
discoLightsOnPowerUps = False

FlyMaps = False  # Whether or not to enable the 3D flying maps in games playlist


# Powerup distribution
dist = (('tripleBombs', 2),
        ('iceBombs', 2),
        ('punch', 0),
        ('impactBombs', 2),
        ('landMines', 2),
        ('stickyBombs', 2),
        ('shield', 0),
        ('health', 2),
        ('curse', 0),
        ('Troll', 0),
        ('Bot', 0),
        ('Rchar', 0),
        ('Bunny', 0),
        ('Tunner', 0))


def return_yielded_game_texts():
    for text in gameTexts:
        yield text


def return_players_yielded(bs):
    for player in bs.getSession().players:
        yield player

# ** TERMINAL **

# STATS
print Colors.LIGHT_CYAN+ 'Enable Stats : '+ Colors.END+ Colors.LIGHT_GREEN+ 'ON'+ Colors.END if enableStats else Colors.RED+ 'OFF'+ Colors.END
# COIN SYSTEM
print Colors.LIGHT_CYAN+ 'CoinSystem : '+ Colors.END+ Colors.LIGHT_GREEN+ 'ON'+ Colors.END if enableCoinSystem else Colors.RED+ 'OFF'+ Colors.END
# NIGHT MODE
print Colors.LIGHT_CYAN+ 'Modo Noche Activado!'+ Colors.END if nightMode else 'Modo Noche Desactivado'
# TOPS
print Colors.LIGHT_CYAN+ 'Top Effects : '+ Colors.END+ Colors.LIGHT_GREEN+ 'ON'+ Colors.END if enableTop5effects else Colors.RED+ 'OFF'+ Colors.END
