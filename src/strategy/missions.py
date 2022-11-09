from ..connection.session import account
from ..path.action import pathActions
from ..basic.verification import verification
from ..basic.simpleActions import simpleActions
from ..strategy.basic import basicStrategy

class missionAccomplisher:
    """
        Make the dinoz teamcomplete action
    """
    def __init__(self, dinoIds):
        """
            DinoIds : Dinoz team with leader first
        """
        self.dinos = dinoIds

    def profEugene(self):
        """
            Aller à l'université
            Combat d'escalade
            Combat pour la bouée
        """
        def escalade():
            for d in self.dinos:
                if not "fx_matesc" in verification.getItems(d):
                    sk = account().getSk()
                    account().run(f"dino/{d}/act/dialog/prof?sk={sk}")
                    account().run(f"dino/{d}/act/dialog/prof?goto=talk;sk={sk}")
                    account().run(f"dino/{d}/act/dialog/prof?goto=learn;sk={sk}")
                    account().run(f"dino/{d}/act/dialog/prof?goto=fire;sk={sk}")
                    account().run(f"dino/{d}/act/dialog/prof?goto=fire_fight;sk={sk}")
        
        
        def eau():
            for d in self.dinos:
                if not "fx_bouee" in verification.getItems(d):
                    sk = account().getSk()
                    account().run(f"dino/{d}/act/dialog/prof?sk={sk}")
                    account().run(f"dino/{d}/act/dialog/prof?goto=talk;sk={sk}")
                    account().run(f"dino/{d}/act/dialog/prof?goto=learn_water;sk={sk}")
                    account().run(f"dino/{d}/act/dialog/prof?goto=water_fight;sk={sk}")
        
        pathActions.goTo(self.dinos, "univ")
        escalade()
        eau()

    def pelle(self):
        """
            Aller chercher la pelle aux mines de corail
        """

        if verification.hasItem(self.dinos, "fx_pelle"):
            return

        pathActions.goTo(self.dinos, "corail")
        for d in self.dinos:
            sk = account().getSk()
            account().run(f"dino/{d}/act/dialog/mine?sk={sk}")
            account().run(f"dino/{d}/act/dialog/mine?goto=yes;sk={sk}")
            account().run(f"dino/{d}/act/dialog/thanks?goto=yes;sk={sk}")
    
    def ingredients(self):
        """
            récupération de :
                - la boue
                - l'eau de jouvence
                - éclat de basalt
        """

        def repare():
            if verification.hasItem(self.dinos, "fx_pelle"):
                return

            pathActions.goTo(self.dinos, "corail")
            for d in self.dinos:
                    sk = account().getSk()
                    account().run(f"dino/{d}/act/dialog/mine?sk={sk}")
                    account().run(f"dino/{d}/act/dialog/mine?goto=repair;sk={sk}")

        def dig():
            for d in self.dinos:
                sk = account().getSk()
                account().run(f"dino/{d}/act/dig?sk={sk}")
        
        def hasGant(dinoId):
            return verification.hasItem([dinoId], "fx_gant")
        

        if not verification.hasItem(self.dinos, "fx_marais", hasGant):
            repare()
            pathActions.goTo(self.dinos, "marais")
            dig()
        if not verification.hasItem(self.dinos, "fx_wpure", hasGant):
            repare()
            pathActions.goTo(self.dinos, "fountj")
            dig()
        if not verification.hasItem(self.dinos, "fx_basalt", hasGant):
            repare()
            pathActions.goTo(self.dinos, "bslt")
            dig()
    
    def domeAccess(self):
        """
            Récupère l'appeau à rascaphandre pour accéder au dôme sous la flotte
        """
        
        if verification.hasItem(self.dinos, "fx_rasca"):
            return

        pathActions.goTo(self.dinos, "chutes")

        # Parler Garde
        for d in self.dinos:
            sk = account().getSk()
            account().run(f"dino/{d}/act/dialog/dome?sk={sk}")
            account().run(f"dino/{d}/act/dialog/dome?goto=rasca;sk={sk}")
            account().run(f"dino/{d}/act/dialog/dome?goto=where;sk={sk}")
            account().run(f"dino/{d}/act/dialog/dome?goto=call;sk={sk}")
            account().run(f"dino/{d}/act/dialog/dome?goto=appeau;sk={sk}")
            account().run(f"dino/{d}/act/dialog/dome?goto=old;sk={sk}")

        pathActions.goTo(self.dinos, "port")

        # Parler Jovébozé
        for d in self.dinos:
            sk = account().getSk()
            account().run(f"dino/{d}/act/dialog/dome__2?sk={sk}")
            account().run(f"dino/{d}/act/dialog/dome__2?goto=sry;sk={sk}")
            account().run(f"dino/{d}/act/dialog/dome__2?goto=go;sk={sk}")
            account().run(f"dino/{d}/act/dialog/dome__2?goto=attack;sk={sk}")


    def zorc(self):
        """
            Récupération du gant de zorc
        """
        
        if verification.hasItem(self.dinos, "fx_gant"):
            return

        pathActions.goTo(self.dinos, "rasca")
        
        for d in self.dinos:
            sk = account().getSk()
            account().run(f"dino/{d}/act/dialog/mage?sk={sk}")
            account().run(f"dino/{d}/act/dialog/mage?goto=enigm;sk={sk}")
            account().run(f"dino/{d}/act/dialog/mage?goto=next;sk={sk}")
            account().run(f"dino/{d}/act/dialog/mage?goto=tresor;sk={sk}")
            account().run(f"dino/{d}/act/dialog/mage?goto=quoi;sk={sk}")
            account().run(f"dino/{d}/act/dialog/mage?goto=show;sk={sk}")
    
    def getFeuille(self):
        """
            Récupération de la feuille
        """
        
        if verification.hasItem(self.dinos, "fx_nenuph"):
            return

        pathActions.goTo(self.dinos, "chutes")
        
        for d in self.dinos:
            sk = account().getSk()
            account().run(f"dino/{d}/act/dialog/moine?sk={sk}")
            account().run(f"dino/{d}/act/dialog/moine?goto=talk;sk={sk}")
            account().run(f"dino/{d}/act/dialog/moine?goto=act;sk={sk}")
            account().run(f"dino/{d}/act/dialog/moine?goto=gant;sk={sk}")
            account().run(f"dino/{d}/act/dialog/moine?goto=why;sk={sk}")
            account().run(f"dino/{d}/act/dialog/moine?goto=super;sk={sk}")
            account().run(f"dino/{d}/act/dialog/moine?goto=ok;sk={sk}")

    def getLanterne(self):
        """
            Getting the lantern object
        """
        
        if verification.hasItem(self.dinos, "fx_lantrn"):
            return

        pathActions.goTo(self.dinos, "collin")
        
        for d in self.dinos:
            sk = account().getSk()
            account().run(f"dino/{d}/act/dialog/fou?sk={sk}")
            account().run(f"dino/{d}/act/dialog/fou?goto=approach;sk={sk}")
            account().run(f"dino/{d}/act/dialog/fou?goto=ignore;sk={sk}")
            account().run(f"dino/{d}/act/dialog/fou?goto=intro;sk={sk}")
            account().run(f"dino/{d}/act/dialog/fou?goto=seenWhat;sk={sk}")
            account().run(f"dino/{d}/act/dialog/fou?goto=show;sk={sk}")
            account().run(f"dino/{d}/act/dialog/fou?goto=fight;sk={sk}")
        
    def congelation(self):
        """
            Go dans les gorges profondes
            Dissous le groupe
            Congèle un à un
        """

        pathActions.goTo(self.dinos, "stunel")

        simpleActions.dissolvGroup(self.dinos[0])

        for d in self.dinos:
            sk = account().getSk()
            account().run(f"dino/{d}/act/dialog/spelele?sk={sk}")
            account().run(f"dino/{d}/act/dialog/spelele?goto=talk;sk={sk}")
            account().run(f"dino/{d}/act/dialog/spelele?goto=gla;sk={sk}")
            account().run(f"dino/{d}/act/dialog/spelele?goto=ok;sk={sk}")
            account().run(f"dino/{d}/act/dialog/spelele?goto=ok2;sk={sk}")
            account().run(f"dino/{d}/act/dialog/spelele?goto=ok3;sk={sk}")
            account().run(f"dino/{d}/act/dialog/spelele?goto=congel;sk={sk}")
            account().run(f"dino/{d}/act/dialog/spelele?goto=congel2;sk={sk}")
            account().run(f"dino/{d}/act/dialog/spelele?goto=thanks;sk={sk}")
            account().run(f"dino/{d}/act/congel?sk={sk}")

    def fromZero_toTheEnd(self):
        """
            dinoIds: dinos making it
            Making dinos go from any level to at least 19 and freezed
        """

        basicStrategy.goToLevel(self.dinos, 19)
                
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
            pathActions.goTo(self.dinos, "papy")
            # Accepting mission
            for d in self.dinos:
                account().run(f"dino/{d}/act/mission/accept?m=fish;sk={account().getSk()}")
            pathActions.goTo(self.dinos, "port")
            # Suite
            pathActions.goTo(self.dinos, "dnv")
            # Suite
            pathActions.goTo(self.dinos, "papy")
            # Valider la mission
        
        return {
            "Du poisson frais": mission1
        }