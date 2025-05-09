import random
from datetime import datetime

import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Gestionnaire de Produits")
root.geometry("1200x800")

# Frame for buttons on the left
button_frame = tk.Frame(root, width=200, bg="lightgray")
button_frame.pack(side="left", fill="y")

# Add 8 buttons to the left frame
for i in range(1, 9):
    button = tk.Button(button_frame, text=f"Button {i}", width=20, height=2)
    button.pack(pady=15)

# Frame for the product list on the right
list_frame = tk.Frame(root)
list_frame.pack(side="right", fill="both", expand=True)

# Label for the product list
list_label = tk.Label(list_frame, text="Liste de Produits", font=("Arial", 14))
list_label.pack(pady=10)

# Treeview widget for displaying products and their characteristics
columns = ("Id", "Nom", "Type", "Stock", "Prix")
product_list = ttk.Treeview(list_frame, columns=columns, show="headings")
product_list.heading("Id", text="Id")
product_list.heading("Nom", text="Nom")
product_list.heading("Type", text="Type")
product_list.heading("Stock", text="Stock")
product_list.heading("Prix", text="Prix")
product_list.pack(fill="both", expand=True)

#Initialisation de la liste de produits
#MasterList est la liste de produits, qui sera affichée dans le Treeview

def LoadListToTreeview (Item) :
    #Fonction affichant une liste de produits donnée, avec les caractéristiques de chaque produit.
    for x in range(len(Item)) :
        Temp = Item[x]
        product_list.insert("", "end", values=(Temp.ID, Temp.NomProduit, Temp.TypeProduit, Temp.QuantiteStock, Temp.PrixProduit))
    LogWriteAdd("LOG", "Liste de produits chargée dans Treeview.")
    return




#MasterList est la liste complète (Temporaire et pour test) des produits.
MasterList = []
#LogToWrite est le registre actuellement en mémoire, sous forme de liste
LogToWrite = []
#SelectedProduct est le produit de MasterList actuellement selectionné pour modifications.
SelectedProduct = None
GenAmount = None

def LogWriteAdd (Type,string) :
    #Fonction ajoutant un élément dans la liste LogToWrite(Le registre), avec la date et l'heure actuelle, un flag(Type) et un texte donnés.
    SetStr= "[{}][{} {}] {}".format(Type, datetime.today().strftime('%d-%m-%Y'),datetime.today().strftime('%H:%M:%S') ,string)
    LogToWrite.append(SetStr)

def LogPrint (loglist):
    #Fonction affichant le registre en mémoire
    for x in range(len(loglist)) :
        print(loglist[x])


#Test basique de LogWriteAdd et LogPrint
LogWriteAdd("BOOT", "TEST")
LogWriteAdd("TEST", "Ceci est un test")
for x in range(6) :
    LogWriteAdd("WARNING", "Ceci est le test {}".format(x))
LogPrint(LogToWrite)


def InputNumberCheck(entry, min, max) :
    #Fonction vérifiant si le nombre entré par l'utilisateur se trouve dans une plage determinée, et retourne 1 si oui, 0 sinon.

    if entry == "":
        print("Veuillez entrer une commande valide (Ne peut pas être vide)")
        LogWriteAdd("WARNING", "Commande Invalide (Commande Vide)")
        return 0
    else :
        entry = int(entry)

    if entry > max or entry < min :
        print("Veuillez entrer une commande valide (Ne peut pas être supérieure a", max, " ou inférieure à ",min, ")")
        LogWriteAdd("WARNING", "Commande Invalide (Commande hors des options)")
        return 0
    
    return 1
    

RandomNoms = [["Lotion", "Soin Peau"], ["Antiride", "Soin Peau"], ["Kératine", "Cheuveux"], ["Shampoing", "Cheuveux"], ["Colorant", "Cheuveux"], ["Déodorant", "Hygiène"], ["Mascara", "Maquillage"], ["Gloss", "Maquillage"], ["Fond de Teint", "Maquillage"], ["Rouge a lèvre", "Maquillage"]]

class Produit :

    #Classe représentant un produit avec plusieurs caracteristiques
    
    def __init__ (self):
        self.ID = None
        self.NomProduit = ""
        self.QuantiteStock = 0
        self.TypeProduit = ""
        self.PrixProduit = 0


def Initialisation_Produits_Tests (Num) :
    #Fonction retournant une liste de produit aléatoire depuis une liste faite au préalable, avec un nombre d'entrées donné. Fonction de test!
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
    #Fonction affichant une liste de produits donnée, avec les caractéristiques de chaque produit.
    for x in range(len(Item)) :
        Temp = Item[x]
        print("ID : ", Temp.ID)
        print( "Nom De Produit : ", Temp.NomProduit, "  --  Type de Produit : ", Temp.TypeProduit)
        print("Quantité en Stock : ", Temp.QuantiteStock, "  --  Prix du Produit : ", Temp.PrixProduit,"\n")
    LogWriteAdd("LOG", "Liste de produits affichée.")
    return


def MenuSelection() :
    #Programme de menu pour sélectionner une action en tapant un numéro. Sera remplacé par une interface TKinter.
    global LogToWrite
    global MasterList
    global SelectedProduct
    global GenAmount
    print("=========================================================================================================================")
    print("Veuillez selectionner une action : \n0 - [TEST] - Générer une liste de produits temporaire.\n1 - Afficher la liste de produits.\n2 - Ajouter un nouveau produit.\n3 - Selectionner un produit par son identifiant.\n4 - Modifier un produit.\n5 - Supprimer un produit.\n6 - Afficher le registre actuel\n7 - Ajouter un message personalisé au registre.")
    print("=========================================================================================================================")
    
   #Affichage du produit actuellement selectionné
    if SelectedProduct == None :
        print ("Aucun produit selectionné.")
    else :
        print("Produit Selectionné = [Id = ", MasterList[SelectedProduct].ID, "] Nom = ", MasterList[SelectedProduct].NomProduit)
    Select = (input("Entrez une commande : "))

    #Verification de l'entrée
    InputCheck = InputNumberCheck(Select, 0, 7)
    if InputCheck == 0 :
        return
    Select = int(Select)

    
    #Si l'entrée est dans la plage demandée, alors lancer le programme en accordance.
    match((Select)):
        case 0 :
            #Demande un nombre de produits a générer pour MasterList, ce qui sera fait post MenuSelection (Test)
            GenAmount = input("Entrez le nombre de Produits a générer : ")
            LogWriteAdd("DEBUG","Génération d'une liste par l'utilisateur")
            return Select
        
        case 1 :
            #Affichage de la liste des produits, tout simplemenjt
            Affichage_Listes(MasterList)
            LogWriteAdd("DEBUG", "Liste de produits affichée par l'utilsateur")
            return Select
        
        case 2 :
            #Création et ajout d'un nouveau produit dans la liste. L'ID s'incrémente toujours selon le dernier produit de la liste (l'id le plus élevé)
            NouvProduit = Produit()
            NouvProduit.ID = MasterList[len(MasterList)-1].ID + 1
            NouvProduit.NomProduit = input("Entrez le nom du nouveau produit : ")
            NouvProduit.TypeProduit = input("Entrez le type du nouveau produit : ")
            NouvProduit.PrixProduit = int(input("Entrez le prix du nouveau produit : "))
            NouvProduit.QuantiteStock = int(input("Entrez la quantité en stock du nouveau produit : "))
            MasterList.append(NouvProduit)
            TempString = "Ajout d'un produit : [ID : {}] Nom : {}.".format(NouvProduit.ID, NouvProduit.NomProduit)
            LogWriteAdd("LOG", TempString)
            return Select   
        
        case 3 :
            #Selection d'un produit par son ID, si il existe. Lorsque selectionné, il pourra etre modifié ou supprimé.
            ProduitVerif = 0

            IDSearch = (input("Entrez l'id du produit que vous souhaitez sélectionner : "))
            IDSearch = int(IDSearch)
            for i in range(len(MasterList)):
                if MasterList[i].ID == IDSearch :
                    SelectedProduct = i
                    print("Selectionné = ", MasterList[i].ID, MasterList[i].NomProduit)
                    ProduitVerif = 1
            if ProduitVerif == 0 :
                print("Aucun produit de cet ID n'a été trouvé!")
                LogWriteAdd("LOG", "Recherche infructueuse.")
                return Select
            TempString = "Selection du produit [ID : {}] Nom : {}.".format(MasterList[i].ID, MasterList[i].NomProduit)
            LogWriteAdd("LOG", TempString)
            return Select
        
        case 4 :
            #Verification de la selection, puis modification de stock, direct, ou par changement, ainsi que modif directe du prix 
            if SelectedProduct == None :
                print("Aucun produit selectioné!!!")
                LogWriteAdd("ERROR", "Tentative de modifications sans produit selectionné.")
                return Select
            TempString = ""

            print("Veuillez selectionner une action : \n1 - Modifier la quantité en stock.\n2 - Modifier le prix.")
            Select2 = input()

            InputCheck = InputNumberCheck(Select2, 1, 2)
            if InputCheck == 0 :
                return
            Select2 = int(Select2)
            
            match Select2 :
                case 1 :
                    print("Veuillez selectionner une action : \n1 - Réduire le stock.\n2 - Augmenter le stock\n3 - Directement modifier le stock")
                    print("Stock actuel de", MasterList[SelectedProduct].NomProduit ," : ",MasterList[SelectedProduct].QuantiteStock)
                    Select3 = input()
                    LogWriteAdd("LOG", "Tentative de modification de stock de [ID : {}] Nom : {}.".format(MasterList[SelectedProduct].ID, MasterList[SelectedProduct].NomProduit))
                    
                    InputCheck = InputNumberCheck(Select3, 1, 3)
                    if InputCheck == 0 :
                        return
                    Select3 = int(Select3)

                    match Select3 :

                        case 1 :
                            StockMod = int(input("Entrez la quantité de stock retirée : "))
                            MasterList[SelectedProduct].QuantiteStock -= StockMod

                            if MasterList[SelectedProduct].QuantiteStock < 0 :
                                print("Le stock est négatif! Cette opération sera annulée!!")
                                MasterList[SelectedProduct].QuantiteStock += StockMod
                                LogWriteAdd("ERROR","Tentative de modification de stock résultant en un stock négatif.")
                            else:
                                print("Le stock de ",MasterList[SelectedProduct].NomProduit ," est désormais à : ", MasterList[SelectedProduct].QuantiteStock)
                            
                            LogWriteAdd("LOG", "Modification de stock de [ID : {}] Nom : {}. Stock modifié de {} à {}".format(MasterList[SelectedProduct].ID, MasterList[SelectedProduct].NomProduit, MasterList[SelectedProduct].QuantiteStock + StockMod, MasterList[SelectedProduct].QuantiteStock))
                            

                        case 2 :
                            StockMod = int(input("Entrez la quantité de stock ajoutée : "))
                            MasterList[SelectedProduct].QuantiteStock += StockMod
                            print("Le stock de ",MasterList[SelectedProduct].NomProduit ," est désormais à : ", MasterList[SelectedProduct].QuantiteStock)
                            LogWriteAdd("LOG", "Modification de stock de [ID : {}] Nom : {}. Stock modifié de {} à {}".format(MasterList[SelectedProduct].ID, MasterList[SelectedProduct].NomProduit, MasterList[SelectedProduct].QuantiteStock - StockMod, MasterList[SelectedProduct].QuantiteStock))

                        case 3 :
                            StockMod = int(input("Entrez la quantité de stock à appliquer : "))
                            TempStock = MasterList[SelectedProduct].QuantiteStock
                            MasterList[SelectedProduct].QuantiteStock = StockMod

                            if MasterList[SelectedProduct].QuantiteStock < 0 :
                                print("Le stock est négatif! Cette opération sera annulée!!")
                                MasterList[SelectedProduct].QuantiteStock = TempStock
                                LogWriteAdd("ERROR","Tentative de modification de stock résultant en un stock négatif.")
                            else:
                                print("Le stock de ",MasterList[SelectedProduct].NomProduit ," est désormais à : ", MasterList[SelectedProduct].QuantiteStock)
                            LogWriteAdd("LOG", "Modification de stock de [ID : {}] Nom : {}. Stock modifié de {} à {}".format(MasterList[SelectedProduct].ID, MasterList[SelectedProduct].NomProduit, TempStock, MasterList[SelectedProduct].QuantiteStock))

                case 2 :
                    PriceMod = int(input("Entrez le nouveau prix a appliquer : "))
                    print("Prix actuel de", MasterList[SelectedProduct].NomProduit ," : ",MasterList[SelectedProduct].PrixProduit)
                    TempPrice = MasterList[SelectedProduct].PrixProduit
                    MasterList[SelectedProduct].PrixProduit = PriceMod
                    LogWriteAdd("LOG", "Tentative de modification du prix de [ID : {}] Nom : {}.".format(MasterList[SelectedProduct].ID, MasterList[SelectedProduct].NomProduit))

                    if MasterList[SelectedProduct].PrixProduit < 0 :
                        print("Le prix est négatif! Cette opération sera annulée!!")
                        MasterList[SelectedProduct].PrixProduit = TempPrice
                        LogWriteAdd("ERROR","Tentative de modification de prix résultant en un prix négatif.")
                    else:
                        print("Le prix de ",MasterList[SelectedProduct].NomProduit ," est désormais à : ", MasterList[SelectedProduct].PrixProduit)
                        LogWriteAdd("LOG", "Modification de prix de [ID : {}] Nom : {}. Stock modifié de {} à {}".format(MasterList[SelectedProduct].ID, MasterList[SelectedProduct].NomProduit, TempPrice, MasterList[SelectedProduct].PrixProduit))

            return Select
        case 5 :
            #Verif de la selection puis demande de suppression, necessite d'écrire supprimer afin d'éviter les suppressions accidentelles
            if SelectedProduct == None :
                print("Aucun produit selectioné!!!")
                LogWriteAdd("ERROR", "Tentative de SUPPRESSION sans produit selectionné.")
                return Select
            
            LogWriteAdd("LOG", "Tentative de SUPPRESSION de [ID : {}] Nom : {}.".format(MasterList[SelectedProduct].ID, MasterList[SelectedProduct].NomProduit))
            print("Voulez-vous vraiment supprimer ce produit définitivement? : [Id = ", MasterList[SelectedProduct].ID, "] Nom = ", MasterList[SelectedProduct].NomProduit, "\n Si oui, écrivez 'supprimer', sinon tappez autre chose et pressez entree.")
            Select4 = input()
            
            if Select4 == "supprimer" :
                LogWriteAdd("LOG", "SUPPRESSION DEFINITIVE de [ID : {}] Nom : {}.".format(MasterList[SelectedProduct].ID, MasterList[SelectedProduct].NomProduit))
                del MasterList[SelectedProduct]
                SelectedProduct = None
                print("Produit ",MasterList[SelectedProduct].NomProduit ," supprimé.")
                

            return Select
        case 6 :
            #Affichage du registre d'application
            LogWriteAdd("LOG", "Registre affiché par l'utilisateur.")
            print("=========================================================================================================================")
            LogPrint(LogToWrite)
            print("=========================================================================================================================")
            return Select
        case 7 :
            #Ajout d'une entrée de registre personalisée.
            LogString = input("Veuillez entrer le texte a ajouter au registre : ")
            LogWriteAdd("MANUAL",LogString)
            return Select




def main() :
    global MasterList
    global LogToWrite
    global GenAmount

    while 1 == 1 :
        MenuFeedback = MenuSelection()
        
        if MenuFeedback == 0 :
            GenAmount = int(GenAmount)
            MasterList = Initialisation_Produits_Tests(GenAmount)
            print("DEBUG - Liste de ", GenAmount, " éléments générée")

Affichage_Listes(MasterList)


MasterList = Initialisation_Produits_Tests(20)
LoadListToTreeview(MasterList)

main()
