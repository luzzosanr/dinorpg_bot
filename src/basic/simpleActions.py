from bs4 import BeautifulSoup

from ..basic.inventory import inventory
from ..connection.session import account

class simpleActions:
    """
        Dinoz are identified by ID
    """
    def fight(dino):
        """
            Make a dino fight
        """

        account().run(f"dino/{dino}/act/fight?sk={account().getSk()}")    
    
    def revive(dino):
        """
            Reviving a dino, throw an error if not dead
        """

        # Reloading potions
        if (not inventory.isStock("item_1")):
            inventory.reloadItem("1", "12")
        
        # Resurrection
        r = account().run(f"dino/{dino}/act/resurrect?angel=1;sk={account().getSk()}")
        account().sk = BeautifulSoup(r.content, "html.parser").find(id = "act_resurrect").find().get_attribute_list("onclick")[0].split("=")[-1][:-2]

        # Stop resting
        account().run(f"dino/{dino}/act/stop_heal?sk={account().getSk()};ajax=1")
    
    def move(dest, dinoId):
        """
            dinoId : integer iding the dino in links
            dest : destination the dino is moving to
        """
        
        account().run(f"dino/{dinoId}/act/move?sk={account().getSk()};to={dest}")

    def dissolvGroup(dinoId):
        """
            dinoId : id of the chef of the group needed to be dissolve
        """

        account().run(f"dino/{dinoId}/act/dissolve_group?sk={account().getSk()}")
        
    def follow(leader, follower):
        """
            leader : id of the dino being the future/current leader
            followers : id of the dinoz following the leader
            Make the followers follow the leader
        """

        account().run(f"dino/{follower}/act/follow?f={leader};sk={account().getSk()}")
    
    