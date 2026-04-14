# MadeBySobyDamn
import bs
from bsMap import *
import bsMap
import bsInternal
import json
import cmdsetg
import logger

num = 0

def __init__(self, vrOverlayCenterOffset=None):
    """
    Instantiate a map.
    """
    import bsInternal
    bs.Actor.__init__(self)
    self.preloadData = self.preload(onDemand=True)

    def text():
        # bySoby
        t = bs.newNode('text',
                       attrs={'text': u'\ue043|TRONOS SUPER SMASH FFA|\ue043\n',
                              'scale': 1.0,
                              'maxWidth': 0,
                              'position': (7, 600),
                              'shadow': 1.5,
                              'flatness': 1.2,
                              'color': ((0.5+random.random()*1.0), (0.5+random.random()*1.0), (0.5+random.random()*1.0)),
                              'hAlign': 'center',
                              'hAttach': 'center',
                              'vAttach': 'top'})
        #bs.animate(t, 'opacity', {0: 0.0, 500: 1.0, 6500: 1.0, 7000: 0.0})
        #bs.gameTimer(7000, t.delete)
        ##
        t = bs.newNode('text',
                       attrs={'text': u'',
                              'scale': 1.0,
                              'maxWidth': 0,
                              'position': (7, 600),
                              'shadow': 1.5,
                              'flatness': 0.0,
                              'color': ((0+random.random()*1.0), (0+random.random()*1.0), (0+random.random()*1.0)),
                              'hAlign': 'center',
                              'vAttach': 'top'})
        #bs.animate(t, 'opacity', {0: 0.0, 500: 1.0, 6500: 1.0, 7000: 0.0})
        #bs.gameTimer(15000, t.delete)
        # bySoby
        t = bs.newNode('text',
                       attrs={
                       'text': u'\ue029   |----VENTA DE ROLES----| \ue029\n'
                               '-----------------------------------------\n'
                               u'    \ue043OWNER\ue043 ---> 7$\n'
                               '-----------------------------------------\n'
                               u'   \ue049ADMIN\ue049  ---> 5$\n'
                               '-----------------------------------------\n'
                               u'     \ue048VIP\ue048   ----> 3$\n'
                               '-----------------------------------------\n'
                               u'\ue062discord.gg/4jApufsnCm\ue062',
                              'scale': 0.7,
                              'maxWidth': 0,
                              'position': (65, 190),
                              'shadow': 1,
                              'color': ((0.5+random.random()*1.0), (0.5+random.random()*1.0), (0.5+random.random()*1.0)),
                              'hAlign': 'left',
                              'hAttach': 'left',
                              'vAttach': 'bottom'})
        #bs.animate(t, 'opacity', {0: 0.0, 500: 1.0, 6500: 1.0, 7000: 0.0})
        #bs.gameTimer(25000, t.delete)
        # bySoby..............................Dont Edit This
        t = bs.newNode('text',
                       attrs={'text': u'\ue043MICHAEL\ue043',
                              'scale': 0.8,
                              'maxWidth': 0,
                              'position': (-50, 0),
                              'shadow': 1.0,
                              'color': ((0+random.random()*1.0), (0+random.random()*1.0), (0+random.random()*1.0)),
                              'flatness': 1.0,
                              'hAlign': 'right',
                              'hAttach': 'right',
                              'vAttach': 'bottom'})
        #bs.animate(t, 'opacity', {0: 0.0, 20: 1.0, 60: 1.0, 70: 0.0})
        #bs.gameTimer(340, t.delete)
        t = bs.newNode('text',
                       attrs={'text': u'',
                              'scale': 0.8,
                              'maxWidth': 0,
                              'position': (0, 138),
                              'shadow': 0.5,
                              'flatness': 1.0,
                              'color': ((0+random.random()*1.0), (0+random.random()*1.0), (0+random.random()*1.0)),
                              'hAlign': 'center',
                              'vAttach': 'bottom'})
        bs.animate(t, 'opacity', {36000: 0.0,
                   36500: 1.0, 42500: 1.0, 43000: 0.0})
        bs.gameTimer(43000, t.delete)
        ##
        t = bs.newNode('text',
                       attrs={'text': u'',
                              'scale': 1,
                              'maxWidth': 0,
                              'position': (0, 138),
                              'shadow': 0.5,
                              'flatness': 1.0,
                              'color': ((0+random.random()*1.0), (0+random.random()*1.0), (0+random.random()*1.0)),
                              'hAlign': 'center',
                              'vAttach': 'bottom'})
        bs.animate(t, 'opacity', {45000: 0.0,
                   45500: 1.0, 50500: 1.0, 51000: 0.0})
        bs.gameTimer(51000, t.delete)
    bs.gameTimer(3500, bs.Call(text))
    bs.gameTimer(56000, bs.Call(text), repeat=True)

    def stats_shower():
        px=-110
        offset=str(7*" ")
        #separator ="--"*len(columnas)
        tabla= ""+ "       Name"+offset + "         Kills\n" 
        t = bs.newNode('text',
                        attrs={ 'text':str(tabla),
                                'scale': 0.6,
                                'maxWidth': 0,
                                'position': (400, -90),
                                'shadow': 0,
                                'flatness': 1.0,
                                'color': (0.7,0.7,0.7),
                                'hAlign': 'left',
                                'vAttach': 'top'})
        """ print "  Nombre: {}".format(name)
            print "  Puntaje: {}".format(stats['scores'])
            print "  Eliminaciones: {}".format(stats['kills'])
            print "  Muertes: {}".format(stats['deaths'])
            print "  Juegos jugados: {}".format(sta
                                'position': (-100,ts['games'])
            print
        """
        f = open(logger.stats, "r")
        stats = json.loads(f.read())

        #print(stats)
        # Ordenar por la metrica deseada (ejemplo: puntaje 'scores')
        # Convertimos los valores de 'scores' a enteros para que se ordenen correctamente.
        jugadores_ordenados = sorted(
            stats.items(),
            key=lambda item: int(item[1]['scores']),
            reverse=True # Orden descendente
        )

        # Imprimir los top 5 (o menos si no hay suficientes jugadores)
        top_5 = jugadores_ordenados[:5]  # Obtener solo los primeros 5
        for i, (id_jugador, stats) in enumerate(top_5, start=1):
            name = stats['name_html'].split(">")[-1]  # Extraer el nombre del jugador
            nameident=len(name)
            name=name.capitalize()
            name=name[:15]

            t = bs.newNode('text',
                        attrs={'text':u" {} | ".format(i)+u" {}".format(name),
                                'scale': 0.5,
                                'maxWidth': 0,
                                'position': (400, px),
                                'shadow': 1,
                                'flatness': 1.0,
                                'color': (1,1,1),
                                'hAlign': 'left',
                                'vAttach': 'top'})
            t = bs.newNode('text',
                        attrs={'text':"  "*19+"{}".format(stats['kills']),
                                'scale': 0.5,
                                'maxWidth': 0,
                                'position': (400, px),
                                'shadow': 1,
                                'flatness': 1.0,
                                'color': (1,1,1),
                                'hAlign': 'left',
                                'vAttach': 'top'})
            px=px-20
        """ print "  Nombre: {}".format(name)
            print "  Puntaje: {}".format(stats['scores'])
            print "  Eliminaciones: {}".format(stats['kills'])
            print "  Muertes: {}".format(stats['deaths'])
            print "  Juegos jugados: {}".format(sta
                                'position': (-100,ts['games'])
            print
        """
    stats_shower()

    # set some defaults
    bsGlobals = bs.getSharedObject('globals')
    # area-of-interest bounds
    aoiBounds = self.getDefBoundBox("areaOfInterestBounds")
    if aoiBounds is None:
        print 'WARNING: no "aoiBounds" found for map:', self.getName()
        aoiBounds = (-1, -1, -1, 1, 1, 1)
    bsGlobals.areaOfInterestBounds = aoiBounds
    # map bounds
    mapBounds = self.getDefBoundBox("levelBounds")
    if mapBounds is None:
        print 'WARNING: no "levelBounds" found for map:', self.getName()
        mapBounds = (-30, -10, -30, 30, 100, 30)
    bsInternal._setMapBounds(mapBounds)
    # shadow ranges
    try:
        bsGlobals.shadowRange = [
            self.defs.points[v][1] for v in
            ['shadowLowerBottom', 'shadowLowerTop',
             'shadowUpperBottom', 'shadowUpperTop']]
    except Exception:
        pass
    # in vr, set a fixed point in space for the overlay to show up at..
    # by default we use the bounds center but allow the map to override it
    center = ((aoiBounds[0]+aoiBounds[3])*0.5,
              (aoiBounds[1]+aoiBounds[4])*0.5,
              (aoiBounds[2]+aoiBounds[5])*0.5)
    if vrOverlayCenterOffset is not None:
        center = (center[0]+vrOverlayCenterOffset[0],
                  center[1]+vrOverlayCenterOffset[1],
                  center[2]+vrOverlayCenterOffset[2])
    bsGlobals.vrOverlayCenter = center
    bsGlobals.vrOverlayCenterEnabled = True
    self.spawnPoints = self.getDefPoints("spawn") or [(0, 0, 0, 0, 0, 0)]
    self.ffaSpawnPoints = self.getDefPoints("ffaSpawn") or [(0, 0, 0, 0, 0, 0)]
    self.spawnByFlagPoints = (self.getDefPoints("spawnByFlag")
                              or [(0, 0, 0, 0, 0, 0)])
    self.flagPoints = self.getDefPoints("flag") or [(0, 0, 0)]
    self.flagPoints = [p[:3] for p in self.flagPoints]  # just want points
    self.flagPointDefault = self.getDefPoint("flagDefault") or (0, 1, 0)
    self.powerupSpawnPoints = self.getDefPoints("powerupSpawn") or [(0, 0, 0)]
    self.powerupSpawnPoints = \
        [p[:3] for p in self.powerupSpawnPoints]  # just want points
    self.tntPoints = self.getDefPoints("tnt") or []
    self.tntPoints = [p[:3] for p in self.tntPoints]  # just want points
    self.isHockey = False
    self.isFlying = False
    self._nextFFAStartIndex = 0


bsMap.Map.__init__ = __init__
