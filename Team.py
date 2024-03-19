class Team:
    def __init__(self, teamName):
        self.teamName = teamName
        self.seed = None
        self.kpRank = None
        self.conf = None
        self.record = None
        self.eff = None
        self.confChamp = False
        self.regSeasonChamp = False
        
        self.offEff = None
        self.offEffRk = None
        self.defEff = None
        self.defEffRk = None
        self.tempo = None
        self.tempoRk = None
        self.luck = None
        self.luckRk = None
        self.oppEff = None
        self.oppEffRk = None
        self.oppOffEff = None
        self.oppOffEffRk = None
        self.oppDefEff = None
        self.oppDefEffRk = None
        self.nonConOppEff = None
        self.nonConOppEffRk = None