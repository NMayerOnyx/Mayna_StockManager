import random
from datetime import datetime

MasterList = []
LogToWrite = []
SelectedProduct = None

def LogWriteAdd (Type,string) :
    SetStr= "[{}][{} {}] {}".format(Type, datetime.today().strftime('%d-%m-%Y'),datetime.today().strftime('%H:%M:%S') ,string)
    LogToWrite.append(SetStr)

def LogPrint (loglist):
    for x in range(len(loglist)) :
        print(loglist[x])


LogWriteAdd("BOOT", "TEST")
LogWriteAdd("TEST", "Ceci est un test")
for x in range(6) :
    LogWriteAdd("WARNING", "Ceci est le test {}".format(x))
LogPrint(LogToWrite)


RandomNoms = [["Lotion", "Soin Peau"], ["Antiride", "Soin Peau"], ["Kératine", "Cheuveux"], ["Shampoing", "Cheuveux"], ["Colorant", "Cheuveux"], ["Déodorant", "Hygiène"], ["Mascara", "Maquillage"], ["Gloss", "Maquillage"], ["Fond de Teint", "Maquillage"], ["Rouge a lèvre", "Maquillage"]]

class Produit :

    #Classe représentant un produit
    
    def __init__ (self):
        self.ID = None
        self.NomProduit = ""
        self.QuantiteStock = 0
        self.TypeProduit = ""
        self.PrixProduit = 0

#Initialisation de quelques produits de test dans une liste
def Initialisation_Produits_Tests (Num) :
    ListeTestProduits = []
    for x in range(Num) :
        NbRand = random.randrange(10)
        Temp = RandomNoms[NbRand]
        Test = Produit()
        Test.ID = x+1
        Test.NomProduit = Temp[0]
        Test.QuantiteStock = random.randrange(1, 500)
        Test.TypeProduit = Temp[1]
        Test.PrixProduit = random.randrange(2, 200)
        ListeTestProduits.append(Test)
    LogWriteAdd("TEST", "Liste aléatoire de produits de {} élméments créée.".format(Num))
    return ListeTestProduits

def Affichage_Listes (Item) :
    for x in range(len(Item)) :
        Temp = Item[x]
        print("ID : ", Temp.ID)
        print( "Nom De Produit : ", Temp.NomProduit, "  --  Type de Produit : ", Temp.TypeProduit)
        print("Quantité en Stock : ", Temp.QuantiteStock, "  --  Prix du Produit : ", Temp.PrixProduit,"\n")
    LogWriteAdd("LOG", "Liste de produits affichée.")
    return


def MenuSelection() :
    global LogToWrite
    global MasterList
    global SelectedProduct
    print("Veuillez selectionner une action : \n0 - [TEST] - Générer une liste de produits temporaire.\n1 - Afficher la liste de produits.\n2 - Ajouter un nouveau produit.\n3 - Selectionner un produit par son identifiant.\n4 - Modifier un produit.\n5 - Supprimer un produit.\n6 - Afficher le registre actuel\n7 - Ajouter un message personalisé au registre.")
    if SelectedProduct == None :
        print ("Aucun produit selectionné.")
    else :
        print("Produit Selectionné = [Id = ", MasterList[SelectedProduct].ID, "] Nom = ", MasterList[SelectedProduct].NomProduit)
    select = (input())

    if select == "":
        print("Veuillez entrer une commande valide (Ne peut pas être vide)")
        LogWriteAdd("WARNING", "Commande Invalide (Commande Vide)")
        return -1
    else :
        select = int(select)

    if select > 7 or select < 0 :
        print("Veuillez entrer une commande valide (Ne peut pas être supérieure a 7 ou inférieure à 0)")
        LogWriteAdd("WARNING", "Commande Invalide (Commande hors des options)")
        return
    
    
    match((select)):
        case 0 :
            LogWriteAdd("DEBUG","Génération d'une liste par l'utilisateur")
            return select
        case 1 :
            Affichage_Listes(MasterList)
            LogWriteAdd("DEBUG", "Liste de produits affichée par l'utilsateur")
            return select
        case 2 :
            NouvProduit = Produit()
            NouvProduit.ID = MasterList[len(MasterList)-1].ID + 1
            NouvProduit.NomProduit = input("Entrez le nom du nouveau produit")
            NouvProduit.TypeProduit = input("Entrez le type du nouveau produit")
            NouvProduit.PrixProduit = int(input("Entrez le prix du nouveau produit"))
            NouvProduit.QuantiteStock = int(input("Entrez la quantité en stock du nouveau produit"))
            MasterList.append(NouvProduit)
            return select
        case 3 :
            IDSearch = (input("Entrez l'id du produit que vous souhaitez sélectionner"))
            IDSearch = int(IDSearch)
            for i in range(len(MasterList)):
                print("Debug Scan ", MasterList[i].NomProduit)
                if MasterList[i].ID == IDSearch :
                    SelectedProduct = i
                    print("Selectionné = ", MasterList[i].ID, MasterList[i].NomProduit )
            return select
        case 4 :
            None
            return select
        case 5 :
            None
            return select
        case 6 :
            LogPrint(LogToWrite)
            LogWriteAdd("LOG", "Registre affiché par l'utilisateur.")
            return select
        case 7 :
            None
            return select


ListeDeTest = Initialisation_Produits_Tests(5)

LogPrint(LogToWrite)

def main() :
    global MasterList
    global LogToWrite

    while 1 == 1 :
        MenuFeedback = MenuSelection()
        
        if MenuFeedback == 0 :
            MasterList = Initialisation_Produits_Tests(5)
            print("debug, généré")

Affichage_Listes(MasterList)


main()