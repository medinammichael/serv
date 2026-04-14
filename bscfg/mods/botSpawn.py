import bs
import bsGame
import bsInternal
from bsGame import *

def onBegin(self):
    bs.Activity.onBegin(self)
    s = self.getSession()
    try:
        self._bots = bs.BotSet()
        self.botTypes = [
            bs.BomberBot, bs.BomberBotPro, bs.BomberBotProShielded,
            bs.ToughGuyBot, bs.ToughGuyBotPro, bs.ToughGuyBotProShielded,
            bs.ChickBot, bs.ChickBotPro, bs.ChickBotProShielded, bs.NinjaBot,
            bs.MelBot, bs.PirateBot
        ]

        def btspawn():
            if len(self.players) == 1:
                try:
                    if not self._bots.haveLivingBots():
                        pt = (self.players[0].actor.node.position[0],
                              self.players[0].actor.node.position[1] + 2,
                              self.players[0].actor.node.position[2])
                        self._bots.spawnBot(random.choice(self.botTypes),
                                            pos=pt,
                                            spawnTime=500)
                except:
                    pass
            else:
                self.botTimer = None

        self.botTimer = bs.gameTimer(1000,btspawn,True)
        if isinstance(s, bs.CoopSession):
            import bsUI
            bsInternal._setAnalyticsScreen(
                'Coop Game: '+s._campaign.getName()
                +' '+s._campaign.getLevel(bsUI.gCoopSessionArgs['level'])
                .getName())
            bsInternal._incrementAnalyticsCount('Co-op round start')
            if len(self.players) == 1:
                bsInternal._incrementAnalyticsCount(
                    'Co-op round start 1 human player')
            elif len(self.players) == 2:
                bsInternal._incrementAnalyticsCount(
                    'Co-op round start 2 human players')
            elif len(self.players) == 3:
                bsInternal._incrementAnalyticsCount(
                    'Co-op round start 3 human players')
            elif len(self.players) >= 4:
                bsInternal._incrementAnalyticsCount(
                    'Co-op round start 4+ human players')
        elif isinstance(s, bs.TeamsSession):
            bsInternal._setAnalyticsScreen('Teams Game: '+self.getName())
            bsInternal._incrementAnalyticsCount('Teams round start')
            if len(self.players) == 1:
                bsInternal._incrementAnalyticsCount(
                    'Teams round start 1 human player')
            elif len(self.players) > 1 and len(self.players) < 8:
                bsInternal._incrementAnalyticsCount(
                    'Teams round start ' + str(len(self.players)) +
                    ' human players')
            elif len(self.players) >= 8:
                bsInternal._incrementAnalyticsCount(
                    'Teams round start 8+ human players')
        elif isinstance(s, bs.FreeForAllSession):
            bsInternal._setAnalyticsScreen(
                'FreeForAll Game: '+self.getName())
            bsInternal._incrementAnalyticsCount('Free-for-all round start')
            if len(self.players) == 1:
                bsInternal._incrementAnalyticsCount(
                    'Free-for-all round start 1 human player')
            elif len(self.players) > 1 and len(self.players) < 8:
                bsInternal._incrementAnalyticsCount(
                    'Free-for-all round start ' + str(len(self.players)) +
                    ' human players')
            elif len(self.players) >= 8:
                bsInternal._incrementAnalyticsCount(
                    'Free-for-all round start 8+ human players')
    except Exception:
        bs.printException("error setting analytics screen")

    # for some analytics tracking on the c layer..
    bsInternal._resetGameActivityTracking()

    # we dont do this in onTransitionIn because it may depend on
    # players/teams which arent available until now
    bs.gameTimer(1, bs.WeakCall(self.showScoreBoardInfo))
    bs.gameTimer(1000, bs.WeakCall(self.showInfo))
    bs.gameTimer(2500, bs.WeakCall(self._showTip))

    # store some basic info about players present at start time
    self.initialPlayerInfo = [
        {'name': p.getName(full=True),
         'character': p.character} for p in self.players]

    # sort this by name so high score lists/etc will be consistent
    # regardless of player join order..
    self.initialPlayerInfo.sort(key=lambda x: x['name'])

    # if this is a tournament, query info about it such as how much
    # time is left
    try:
        tournamentID = self.getSession()._tournamentID
    except Exception:
        tournamentID = None

    if tournamentID is not None:
        bsInternal._tournamentQuery(
            args={'tournamentIDs': [tournamentID],
                  'source': 'in-game time remaining query'},
            callback=bs.WeakCall(self._onTournamentQueryResponse))



bsGame.GameActivity.onBegin = onBegin