import requests

def MusicAPI(arstist_name):
    api_adress = "https://www.theaudiodb.com/api/v1/json/2/search.php?s="

    #artist = input("Enter the Artsist name : ")

    url = api_adress + arstist_name

    json_data = requests.get(url).json()

    data=json_data['artists'][0]

    print("Here is some information about ", data['strArtist']," : ", "\n", data['strBiographyEN'])

    return data