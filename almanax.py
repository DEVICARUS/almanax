import regex

from utility import getnsoup

def dofus():
    soup_almanax = getnsoup("http://www.krosmoz.com/en/almanax")

    soup_dofus = soup_almanax.find("div", "dofus")
    
    meridian = soup_dofus.find("p").string.replace("Quest: Offering for ", "")
    
    pattern = r"Find ([0-9]+) (.+) and take the offering to Antyklime Ax"
    offering = regex.match(pattern, soup_dofus.find("p", "fleft").string.strip()).groups()
    
    offering_link = "https://dofuswiki.fandom.com/wiki/" + offering[1].replace(" ", "_")
    
    soup_wiki = getnsoup(offering_link)
    offering_image_raw = soup_wiki.find("div", "floatnone").find_all("img")[0].get("src")
    pattern = r"(https://.+\.png).*"
    offering_image = regex.match(pattern, offering_image_raw).groups()[0]

    return {
        "meridian": meridian,
        "offering": {
            "name": offering[1],
            "quantity": offering[0],
            "image": offering_image, 
            "link": offering_link
        }
    }