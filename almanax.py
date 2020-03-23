import regex

from utility import getnsoup

def meridian(soup_almanax):
    soup_meridian = soup_almanax.find("div", id="almanax_boss")
    
    pattern = r"<span\sclass=\"title\">(.+)</span><br/?>\n\s*(.*?)\s*</div>"
    meridian = regex.search(pattern, str(soup_meridian)).groups()
    
    return {
        "name": meridian[0],
        "description": meridian[1]
    }

def dofus(soup_almanax):
    soup_dofus = soup_almanax.find("div", "dofus")
    
    meridian = soup_dofus.find("p").string.replace("Quest: Offering for ", "")
    
    pattern = r"Bonus:\s(.*?)\s*<div\sclass=\"more\">\n\s*(.*?)\s*<div\sclass=\"more-infos\">"
    bonus_raw = regex.search(pattern, str(soup_dofus)).groups()
    bonus_name = bonus_raw[0]
    bonus_description = regex.sub(r"<.*?>", "", bonus_raw[1])
    
    pattern = r"Find ([0-9]+) (.+) and take the offering to Antyklime Ax"
    offering = regex.match(pattern, soup_dofus.find("p", "fleft").string.strip()).groups()
    
    offering_link = "https://dofuswiki.fandom.com/wiki/" + offering[1].replace(" ", "_")
    
    soup_wiki = getnsoup(offering_link)
    offering_image_raw = soup_wiki.find("div", "floatnone").find_all("img")[0].get("src")
    pattern = r"(https://.+\.png).*"
    offering_image = regex.match(pattern, offering_image_raw).groups()[0]

    return {
        "meridian": meridian,
        "bonus": {
            "name": bonus_name,
            "description": bonus_description
        },
        "offering": {
            "name": offering[1],
            "quantity": int(offering[0]),
            "image": offering_image, 
            "link": offering_link
        }
    }