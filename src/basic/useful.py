from bs4 import BeautifulSoup
from ..connection.session import account

class utilities:
    def getDinoz():
        """
            Return the list of available dinoz of the account (unfrozened dinoz)
        """
        
        list = BeautifulSoup(account().run().content, "html.parser").find(id = "dinozList").find_all("a")
        dinoz = [i.get_attribute_list("href")[0][6:] for i in list if i.get_attribute_list("href")[0][:6] == '/dino/']

        # Removing overview and missions (unlocked later)
        if "overview" in dinoz:
            dinoz.remove("overview")
        if "missions" in dinoz:
            dinoz.remove("missions")

        return dinoz