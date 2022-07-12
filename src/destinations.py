class pathFinder:

    def __init__(self):
        self.gorgesFromLanterne = ["chemin", "auree", "gochut", "marais", "ilewkk", "goport", "fountj", "dnv", "univ", "colesc", "gogtc", "forges", "fosslv", "tunel", "stunel"]
    
    def getDestinations(self, place):
        """
            place : from to start
            return : possible destinations within the zone
        """
        
        if (place == "dnv"):
            return ["univ", "fountj"]
        if (place == "fountj"):
            return ['papy', 'frcbrt', 'port', 'dnv']
        if (place == "papy"):
            return ['univ', 'frcbrt']
        if (place == "univ"):
            return ['papy', 'dnv', 'colesc']
        if (place == "colesc" or place == "gocol"):
            return ['univ', 'gogtc']
        if (place == "frcbrt"):
            return ['marche', 'fountj', 'papy']
        if (place == "marche"):
            return ['frcbrt']
        if (place == "port" or place == "goport"):
            return ['fountj', 'goiles']
        if (place == "ilewkk" or place == "goiles"):
            return ['goport', 'corail', 'marais']
        if (place == "corail"):
            return ['ilewkk', 'marais']
        if (place == "marais"):
            return ['ilewkk', 'corail', 'chutes']
        if (place == "chutes" or place == "gochut"):
            return ['baobob', 'marais', 'rasca', 'gogrum']
        if (place == "baobob"):
            return ['chutes']
        if (place == "dome" or place == 'rasca'):
            return ['chutes']
        if (place == "bslt" or place == "gogtc"):
            return ['forges', 'gocol']
        if (place == "forges"):
            return ['vener', 'bslt', 'rashpk', 'fosslv']
        if (place == "rashpk"):
            return ['forges']
        if (place == "fosslv"):
            return ['forges', 'tunel']
        if (place == "vener"):
            return ['forges']
        if (place == "tunel"):
            return ['fosslv', 'stunel']
        if (place == "gorges" or place == "stunel"):
            return ['tunel']
        if (place == "auree" or place == "gogrum"):
            return ['chemin', 'gochut']
        if (place == "chemin"):
            return ['fleuve', 'collin', 'auree']
        if (place == "collin"):
            return ['fleuve', 'chemin']
        if (place == "fleuve"):
            return ['collin', 'chemin']
        if (place == "camp"):
            return ['gogorg']
        if (place == "jungle"):
            return ['garde', 'fleuve']
        if (place == "garde"):
            return ['jungle']
        
    
    def goTo(self, dest, init):
        """
            dest : destination aimed
            init : start place
            return : the path to use to go to the place
        """

        if (dest == init):
            return []
        
        paths = [[i] for i in self.getDestinations(init)]
        while (not dest in [i[-1] for i in paths]):
            paths = [p + [a] for p in paths for a in self.getDestinations(p[-1]) if not a in p]
            if paths == []:
                return [init]
        
        for p in paths:
            if p[-1] == dest:
                return p
    
    def fullNameToCode(self, name):
        """
            name : full name of the place
            return : the code to be use to move
        """

        if (name == "La Fontaine de Jouvence"):
            return "fountj"
        if (name == "Forcebrut"):
            return "frcbrt"
        if (name == "Place du Marché"):
            return "marche"
        if (name == "Port de Prêche"):
            return "port"
        if (name == "Dinoville"):
            return "dnv"
        if (name == "Chez Papy Joe"):
            return "papy"
        if (name == "L'Université"):
            return "univ"
        if (name == "Collines Escarpées"):
            return "colesc"
        if (name == "Pentes de Basalte"):
            return "bslt"
        if (name == "Forges du Grand Tout Chaud"):
            return "forges"
        if (name == "Ruines Ashpouk"):
            return "rashpk"
        if (name == "Fosselave"):
            return "fsslv"
        if (name == "Repaire du Vénérable"):
            return "vener"
        if (name == "Tunnel sous la Branche"):
            return "tunel"
        if (name == "Gorges Profondes"):
            return "gorges"
        if (name == "Tour de Karinbao"):
            return "tourbt"
        if (name == "L'Ile Waïkiki"):
            return "ilewkk"
        if (name == "Mines de Corail"):
            return "corail"
        if (name == "Marais Collant"):
            return "marais"
        if (name == "Chutes Mutantes"):
            return "chutes"
        if (name == "Chez M. Bao Bob"):
            return "baobob"
        if (name == "Dôme Soulaflotte"):
            return "dome"
        if (name == "L'Orée de la Forêt"):
            return "auree"
        if (name == "Chemin Glauque"):
            return "chemin"
        if (name == "Collines hantées"):
            return "collin"
        if (name == "Fleuve Jumin"):
            return "fleuve"
        if (name == "Camp Korgon"):
            return "camp"
        if (name == "Jungle Sauvage"):
            return "jungle"
        if (name == "Porte de Sylvenoire"):
            return "garde"


#traject = ["gorges", "chemin", "tunel", "fosslv", "forges", "bslt", "gocol", "univ", "dnv", "fountj", "port", "goiles", "marais", "chutes", "gogrum", "chemin", "collin"]
#traject = ["univ", "dnv", "fountj", "port", "goiles", "marais", "chutes", "gogrum", "chemin", "collin"]