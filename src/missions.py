from src.bot import DinorpgApi

class MissionAccomplisher:
    """
        Make the dinoz teamcomplete action
    """
    def __init__(self, dinoIds):
        """
            DinoIds : Dinoz team with leader first
        """
        self.dinos = dinoIds
        self.bot = DinorpgApi()

    def profEugene(self):
        """
            Aller à l'université
            Combat d'escalade
            Combat pour la bouée
        """
        def escalade():
            for d in self.dinos:
                if not "fx_matesc" in self.bot.getItems(d):
                    sk = self.bot.getSK(self.dinos[0])
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/prof?sk={sk}")
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/prof?goto=talk;sk={sk}")
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/prof?goto=learn;sk={sk}")
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/prof?goto=fire;sk={sk}")
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/prof?goto=fire_fight;sk={sk}")
        
        
        def eau():
            for d in self.dinos:
                if not "fx_bouee" in self.bot.getItems(d):
                    sk = self.bot.getSK(self.dinos[0])
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/prof?sk={sk}")
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/prof?goto=talk;sk={sk}")
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/prof?goto=learn_water;sk={sk}")
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/prof?goto=water_fight;sk={sk}")
        
        self.bot.goTo(self.dinos, "univ")
        escalade()
        eau()

    def pelle(self):
        """
            Aller chercher la pelle aux mines de corail
        """

        if self.bot.hasItem(self.dinos, "fx_pelle"):
            return

        self.bot.goTo(self.dinos, "corail")
        for d in self.dinos:
            sk = self.bot.getSK(self.dinos[0])
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mine?sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mine?goto=yes;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/thanks?goto=yes;sk={sk}")
    
    def ingredients(self):
        """
            récupération de :
                - la boue
                - l'eau de jouvence
                - éclat de basalt
        """

        def repare():
            if self.bot.hasItem(self.dinos, "fx_pelle"):
                return

            self.bot.goTo(self.dinos, "corail")
            for d in self.dinos:
                    sk = self.bot.getSK(self.dinos[0])
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mine?sk={sk}")
                    self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mine?goto=repair;sk={sk}")

        def dig():
            for d in self.dinos:
                sk = self.bot.getSK(self.dinos[0])
                self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dig?sk={sk}")
        
        def hasGant(dinoId):
            return self.bot.hasItem([dinoId], "fx_rasca")
        

        if not self.bot.hasItem(self.dinos, "fx_marais", hasGant):
            repare()
            self.bot.goTo(self.dinos, "marais")
            dig()
        if not self.bot.hasItem(self.dinos, "fx_wpure"):
            repare()
            self.bot.goTo(self.dinos, "fountj")
            dig()
        if not self.bot.hasItem(self.dinos, "fx_basalt"):
            repare()
            self.bot.goTo(self.dinos, "bslt")
            dig()
    
    def domeAccess(self):
        """
            Récupère l'appeau à rascaphandre pour accéder au dôme sous la flotte
        """
        
        if self.bot.hasItem(self.dinos, "fx_rasca"):
            return

        self.bot.goTo(self.dinos, "chutes")

        # Parler Garde
        for d in self.dinos:
            sk = self.bot.getSK(self.dinos[0])
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome?sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome?goto=rasca;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome?goto=where;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome?goto=call;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome?goto=appeau;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome?goto=old;sk={sk}")

        self.bot.goTo(self.dinos, "port")

        # Parler Jovébozé
        for d in self.dinos:
            sk = self.bot.getSK(self.dinos[0])
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome__2?sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome__2?goto=sry;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome__2?goto=go;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/dome__2?goto=attack;sk={sk}")


    def zorc(self):
        """
            Récupération du gant de zorc
        """
        
        if self.bot.hasItem(self.dinos, "fx_gant"):
            return

        self.bot.goTo(self.dinos, "rasca")
        
        for d in self.dinos:
            sk = self.bot.getSK(self.dinos[0])
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mage?sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mage?goto=enigm;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mage?goto=next;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mage?goto=tresor;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mage?goto=quoi;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/mage?goto=show;sk={sk}")
    
    def getFeuille(self):
        """
            Récupération de la feuille
        """
        
        if self.bot.hasItem(self.dinos, "fx_nenuph"):
            return

        self.bot.goTo(self.dinos, "chutes")
        
        for d in self.dinos:
            sk = self.bot.getSK(self.dinos[0])
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/moine?sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/moine?goto=talk;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/moine?goto=act;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/moine?goto=gant;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/moine?goto=why;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/moine?goto=super;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/moine?goto=ok;sk={sk}")

    def getLanterne(self):
        """
            Getting the lantern object
        """
        
        if self.bot.hasItem(self.dinos, "fx_lantrn"):
            return

        self.bot.goTo(self.dinos, "collin")
        
        for d in self.dinos:
            sk = self.bot.getSK(self.dinos[0])
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/fou?sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/fou?goto=approach;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/fou?goto=ignore;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/fou?goto=intro;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/fou?goto=seenWhat;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/fou?goto=show;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/fou?goto=fight;sk={sk}")
        
    def congelation(self):
        """
            Go dans les gorges profondes
            Dissous le groupe
            Congèle un à un
        """

        self.bot.goTo(self.dinos, "stunel")

        self.bot.dissolvGroup(self.dinos[0])

        for d in self.dinos:
            sk = self.bot.getSK(d)
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/spelele?sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/spelele?goto=talk;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/spelele?goto=gla;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/spelele?goto=ok;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/spelele?goto=ok2;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/spelele?goto=ok3;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/spelele?goto=congel;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/spelele?goto=congel2;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/dialog/spelele?goto=thanks;sk={sk}")
            self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/congel?sk={sk}")

    def fromZero_toTheEnd(self):
        """
            dinoIds: dinos making it
            Making dinos go from any level to at least 25 and freezed
        """

        self.bot.goToLevel(self.dinos, 25)
                
        self.profEugene()
        self.pelle()
        self.ingredients()
        self.domeAccess()
        self.zorc()
        self.getFeuille()
        self.getLanterne()
        self.congelation()


    def PapyJoe(self):
        """
            Erreur sur le site pour le moment
        """
        def mission1():
            self.bot.goTo(self.dinos, "papy")
            # Accepting mission
            for d in self.dinos:
                self.bot.session.get(f"http://www.dinorpg.com/dino/{d}/act/mission/accept?m=fish;sk={self.bot.getSK(self.dinos[0])}")
            self.bot.goTo(self.dinos, "port")
            # Suite
            self.bot.goTo(self.dinos, "dnv")
            # Suite
            self.bot.goTo(self.dinos, "papy")
            # Valider la mission
        
        return {
            "Du poisson frais": mission1
        }