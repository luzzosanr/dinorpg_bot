from ..basic.verification import verification
from ..basic.simpleActions import simpleActions
from .destinations import pathFinder

class pathActions:
    def traject(path, dinoIds):
        """
            dinoIds : array integer iding the dinos in party, first is leader (on element if alone)
            path : destination the dino will go through
        """

        for d in path:
            while not verification.checks(dinoIds):
                pass
            simpleActions.move(d, dinoIds[0])
            
    def goTo(dinoIds, dest):
        """
            dinoIds : array integer iding the dinos in party, first is leader (on element if alone)
            dest : destination in code
            Go to a destination in group
        """

    
        path = pathFinder().findPath(dest, verification.getPlace(dinoIds[0]))
        pathActions.traject(path, dinoIds)
