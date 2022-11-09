class pathFinder:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(pathFinder, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.paths = {}
        self.dictionnaryCreation()
        self.syno = {}
        self.placeSynonymes()
        self.nameToId = {}
        self.fullNameToCodeCreation()
    
    def dictionnaryCreation(self):
        self.paths["dnv"] = ["univ", "fountj"]
        self.paths["fountj"] = ['papy', 'frcbrt', 'port', 'dnv']
        self.paths["papy"] = ['univ', 'frcbrt']
        self.paths["univ"] = ['papy', 'dnv', 'colesc']
        self.paths["colesc"] = ['univ', 'gogtc']
        self.paths["frcbrt"] = ['marche', 'fountj', 'papy']
        self.paths["marche"] = ['frcbrt']
        self.paths["port"] = ['fountj', 'goiles']
        self.paths["ilewkk"] = ['goport', 'corail', 'marais']
        self.paths["corail"] = ['ilewkk', 'marais']
        self.paths["marais"] = ['ilewkk', 'corail', 'chutes']
        self.paths["chutes"] = ['baobob', 'marais', 'rasca', 'gogrum']
        self.paths["baobob"] = ['chutes']
        self.paths["dome"] = ['chutes']
        self.paths["bslt"] = ['forges', 'gocol']
        self.paths["forges"] = ['vener', 'bslt', 'rashpk', 'fosslv']
        self.paths["rashpk"] = ['forges']
        self.paths["fosslv"] = ['forges', 'tunel']
        self.paths["vener"] = ['forges']
        self.paths["tunel"] = ['fosslv', 'stunel']
        self.paths["gorges"] = ['tunel', 'gocamp']
        self.paths["auree"] = ['chemin', 'gochut']
        self.paths["chemin"] = ['fleuve', 'collin', 'auree']
        self.paths["collin"] = ['fleuve', 'chemin']
        self.paths["fleuve"] = ['collin', 'chemin']
        self.paths["camp"] = ['gogorg']
        self.paths["jungle"] = ['garde', 'fleuve']
        self.paths["garde"] = ['jungle']

    def placeSynonymes(self):
        """
            For places that have synonymes like goto...
        """

        self.syno["gochut"] = "chutes"
        self.syno["gocol"] = "colesc"
        self.syno["goiles"] = "ilewkk"
        self.syno["goport"] = "port"
        self.syno["rasca"] = "dome"
        self.syno["gogtc"] = "bslt"
        self.syno["stunel"] = "gorges"
        self.syno["gogrum"] = "auree"
        self.syno["gocamp"] = "camp"
        self.syno["gogorg"] = "gorges"
        
    
    def findPath(self, dest, init):
        """
            dest : destination aimed in code
            init : start place
            return : the path to use to go to the place
        """

        # Main name of the object
        def main(place):
            if place in self.syno.keys():
                return self.syno[place]
            return place

        if (dest == init):
            return []
        
        paths = [[i] for i in self.paths[init]]

        while (not dest in [main(i[-1]) for i in paths]):
            paths = [p + [a] for p in paths for a in self.paths[main(p[-1])] if not a in p]
            if paths == []:
                return [init]
        
        for p in paths:
            if main(p[-1]) == dest:
                return p
    
    def fullNameToCodeCreation(self):
        self.nameToId["La Fontaine de Jouvence"] = "fountj"
        self.nameToId["Forcebrut"] = "frcbrt"
        self.nameToId["Place du Marché"] = "marche"
        self.nameToId["Port de Prêche"] = "port"
        self.nameToId["Dinoville"] = "dnv"
        self.nameToId["Chez Papy Joe"] = "papy"
        self.nameToId["L'Université"] = "univ"
        self.nameToId["Collines Escarpées"] = "colesc"
        self.nameToId["Pentes de Basalte"] = "bslt"
        self.nameToId["Forges du Grand Tout Chaud"] = "forges"
        self.nameToId["Ruines Ashpouk"] = "rashpk"
        self.nameToId["Fosselave"] = "fsslv"
        self.nameToId["Repaire du Vénérable"] = "vener"
        self.nameToId["Tunnel sous la Branche"] = "tunel"
        self.nameToId["Gorges Profondes"] = "gorges"
        self.nameToId["Tour de Karinbao"] = "tourbt"
        self.nameToId["L'Ile Waïkiki"] = "ilewkk"
        self.nameToId["Mines de Corail"] = "corail"
        self.nameToId["Marais Collant"] = "marais"
        self.nameToId["Chutes Mutantes"] = "chutes"
        self.nameToId["Chez M. Bao Bob"] = "baobob"
        self.nameToId["Dôme Soulaflotte"] = "dome"
        self.nameToId["L'Orée de la Forêt"] = "auree"
        self.nameToId["Chemin Glauque"] = "chemin"
        self.nameToId["Collines hantées"] = "collin"
        self.nameToId["Fleuve Jumin"] = "fleuve"
        self.nameToId["Camp Korgon"] = "camp"
        self.nameToId["Jungle Sauvage"] = "jungle"
        self.nameToId["Porte de Sylvenoire"] = "garde"


#traject = ["gorges", "chemin", "tunel", "fosslv", "forges", "bslt", "gocol", "univ", "dnv", "fountj", "port", "goiles", "marais", "chutes", "gogrum", "chemin", "collin"]
#traject = ["univ", "dnv", "fountj", "port", "goiles", "marais", "chutes", "gogrum", "chemin", "collin"]