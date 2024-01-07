from fileInteraction import WriteFile
import pprint
from PopulateDictionary import PopulateClassDictionary, PopulateTextDictionary
from dbStuff import WriteClassDictionaryToDb

# TODO:
# fix git
# - copy everything to a new folder 
# - delete repo
# - delete original folder
# unit tests
# allow artists and composers
# - brendel != beethoven
# start getting data from wikipedia and discogs:
# - get nationality/ies
# - gender/s
# - birth/death years
# - album release years
# introduce timing how long it takes to run scripts and how many artists etc were processed

pp = pprint.PrettyPrinter(indent=4)

def printClassDictionary(classDictionary):
    for artistName in classDictionary:
        print(artistName)
        for albumName in classDictionary[artistName].albums:
            print("   - ",albumName)
            pp.pprint(classDictionary[artistName].albums[albumName].tracks)

def main():
    classDictionary = PopulateClassDictionary()

    # printClassDictionary(classDictionary)    

    # textDictionary = PopulateTextDictionary(classDictionary)

    # pp.pprint(textDictionary)

    # WriteFile(textDictionary)

    WriteClassDictionaryToDb(classDictionary)

main()



