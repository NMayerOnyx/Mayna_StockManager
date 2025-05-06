import random


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

    return ListeTestProduits

def Affichage_Listes (Item) :
    for x in range(len(Item)) :
        Temp = Item[x]
        print("ID : ", Temp.ID)
        print( "Nom De Produit : ", Temp.NomProduit, "  --  Type de Produit : ", Temp.TypeProduit)
        print("Quantité en Stock : ", Temp.QuantiteStock, "  --  Prix du Produit : ", Temp.PrixProduit,"\n")
    return

ListeDeTest = Initialisation_Produits_Tests(5)
Affichage_Listes(ListeDeTest)