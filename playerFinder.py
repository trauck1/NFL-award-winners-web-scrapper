from bs4 import BeautifulSoup
import requests

#condenses the name to fit the criteria of the url
def nameCondenser(name):
    nameList = name.split()
    if len(nameList) < 2:
        print("Not a valid name")
        return
    firstName = nameList[0]
    lastName = nameList[1]
    
    #first name(condenses to the first 2 letters)
    if(len(firstName) >=2):
        firstName = firstName[0]+firstName[1]
    else:
        print("invalid first name")
    
    #last name(condenses to the first 4 letters)
    if('-' in lastName):
        afterHyphen = lastName.split('-')
        if(len(afterHyphen) >=4):
            lastName = afterHypen[0]+afterHypen[1]+afterHypen[2]+afterHypen[3]
    elif(len(lastName) >=4):
        lastName = lastName[0]+lastName[1]+lastName[2]+lastName[3]
    #special case for Bo Nix(only player with a 3 letter last name)
    elif(len(lastName) == 3):
        lastName = lastName[0]+lastName[1]+lastName[2]+lastName[2]
    else:
        print("invalid last name")
        return
    
    #make sure the first letter of the first and last name is uppercase is uppercase
    firstNameList = list(firstName)
    firstNameList[0] = firstNameList[0].upper()
    firstName = "".join(firstNameList)

    lastNameList = list(lastName)
    lastNameList[0] = lastNameList[0].upper()
    lastName = "".join(lastNameList)

    return lastName+firstName

#returns all the urls that could be a match for the given name    
def urlFinder(condensedName, fullName):
    counter = 0
    urlNotFound = False
    url = ''
    urlList = []
    initial = condensedName[0]
    while not urlNotFound:
        urlEnding = initial+"/"+condensedName+"0"+str(counter)+".htm"
        url = "https://www.pro-football-reference.com/players/"+urlEnding
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        h1_tag = soup.find('h1')
        h1_text = h1_tag.get_text().strip()
        if "Page Not Found" in h1_text:
            urlNotFound = True
        else:
            urlList.append(url)
            counter+= 1
    return urlList

def urlChecker(urlList, fullName):
    nameList = fullName.split()
    firstName = nameList[0]
    lastName = nameList[1]
    print("Possible Matches found:")
    for url in urlList:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        strongTag = soup.find('strong')
        name = strongTag.get_text().strip()
        #for names with periods ex. D.K. Metcalf
        name = name.replace(".", "")
        if(firstName in name and lastName in name):
            print(name,':')
            playerInfo = soup.find('strong', string='Draft')
            if playerInfo:
                # Get the parent paragraph to get all the text
                draft_info = playerInfo.parent.get_text().strip()
                print(draft_info)
            else:
                print("Undrafted")
            


if __name__ == "__main__":
    fullName = input("Enter any NFL player name! ")
    condensedName = nameCondenser(fullName)
    if(condensedName):
        urlList = urlFinder(condensedName, fullName)
        if(len(urlList) == 0):
            print("No matches found.")
        else:
            urlChecker(urlList, fullName)



    



