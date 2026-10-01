# Convertisseur de bases — version "moteur" (sans input()/print())

def convertion_dec_bin(nbre: int,etat_actuelle_nbre: str)-> str:
    tab=[]
    nbre=int(nbre)
    
    if etat_actuelle_nbre=="d":
        
        q=nbre
        while q!=0:
            r=q%2
            q=q//2
            tab.append(r)
            
        tab.reverse()
        nbre_convertit="".join(map(str,tab))
        return nbre_convertit
    
        
def convertion_oct_bin(nbre: int,etat_actuelle_nbre: str)-> str:
    tab=[]
    if etat_actuelle_nbre=="o":
        nbre=str(nbre)
        for i in nbre:
            valeur=int(i)
            if 0<=valeur<8:
                bin_of_valeur=convertion_dec_bin(valeur,"d")
                
                #On augmente la valeur convertit de 4-len(iter)*"0" a droite si sa longueur est inferieur à 4
                if len(bin_of_valeur)<3:
                    bin_of_valeur="0"*(3-len(bin_of_valeur))+bin_of_valeur
        
                tab.append(bin_of_valeur)
                nbre_convertit="".join(map(str,tab))
        return nbre_convertit
    
    
def convertion_hex_bin(nbre: str,etat_actuelle: str)-> str:
    tab=[] 
    if etat_actuelle=="h":
        nbre=str(nbre)
        for i in nbre:
            #fonction qui transforme l'entrée utilisateur en nombre convertissable
            def to_hex_digit(r):
               table={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
               return table.get(r,str(r))#renvoi la valeur si elle existe sinon le nombre lui mm en format str
           
            valeur=int(to_hex_digit(i))
            if 0<=valeur<16: 
                bin_of_valeur=convertion_dec_bin(valeur,"d")
                #On augmente la valeur convertit de 4-len(iter)*"0" a droite si sa longueur est inferieur à 4
                if len(bin_of_valeur)<4:
                    bin_of_valeur="0"*(4-len(bin_of_valeur))+bin_of_valeur
        
                tab.append(bin_of_valeur)
                nbre_convertit="".join(map(str,tab))
        return nbre_convertit
        
            
def convertion_bin_dec(nbre: str,etat_nbre: str):
    etat_nbre=etat_nbre.lower()
    compteur=0
    nbre_convertit=0
    if etat_nbre=="b":
        for elmt in nbre:
            elmt=int(elmt)
            compteur+=1
            if elmt in{0,1}:
                nbre_convertit+=elmt*2**(len(nbre)-compteur)
        return nbre_convertit    
    
    
def convertion_dec_oct(nbre: str,etat_nbre: str):
    etat_nbre=etat_nbre.lower()
    tab=[]
    nbre=int(nbre)
    if etat_nbre=="d":
        q=nbre
        while q!=0:
            r=q%8
            q=q//8
            tab.append(r)
            
        tab.reverse()
        nbre_convertit="".join(map(str,tab))
        return nbre_convertit
      
def convertion_dec_hex(nbre: str,etat_nbre: str):
    etat_nbre=etat_nbre.lower()
    tab=[]
    if etat_nbre=="d":
        nbre=int(nbre)
        r=nbre%16
        
        def to_digit_hex(r):
            table={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
            return table.get(r,str(r))#renvoi la valeur si elle existe sinon le nombre lui mm en format str
        
        valeur_hex=to_digit_hex(r)
                       
        q=nbre//16
        tab.append(valeur_hex)
        while q!=0:
            r=q%16
            
            valeur_hex=to_digit_hex(r)
            
            q=q//16
            tab.append(valeur_hex)
        tab.reverse()
    nbre_convertit="".join(map(str,tab))#On transforme tout les elmts de la liste en str avant la jointure
    return nbre_convertit

# Fonction "moteur" 
#Elle reçoit les données et RETOURNE un dict :
#{"resultat": "..."}  ou  {"erreur": "..."} selon le traitement

def convertir(nbre: str, base_depart: str, base_arrivee: str) -> dict:
    nbre = str(nbre).upper().strip().replace(" ","")
    base_depart = base_depart.lower().strip()
    base_arrivee = base_arrivee.lower().strip()

    if base_depart not in {"d", "b", "o", "h"}:
        return {"erreur": "Base de départ invalide. Choisir d, b, o ou h."}
    if base_arrivee not in {"d", "b", "o", "h"}:
        return {"erreur": "Base d'arrivée invalide. Choisir d, b, o ou h."}

    # validation générale des caractères (chiffres ou A-F)
    if not nbre or not all(c.isdigit() or c in "ABCDEF" for c in nbre):
        return {"erreur": "Le nombre contient des caractères invalides."}

    # validation spécifique à la base de départ annoncée
    chiffres_valides = {
        "b": set("01"),
        "o": set("01234567"),
        "d": set("0123456789"),
        "h": set("0123456789ABCDEF"),
    }
    if not all(c in chiffres_valides[base_depart] for c in nbre):
        return {"erreur": f"Le nombre {nbre} n'est pas valide en base '{base_depart}'."}

    try:
        match base_arrivee:
            case "b":
                match base_depart:
                    case "d":
                        resultat = convertion_dec_bin(nbre, base_depart)
                    case "b":
                        resultat = nbre
                    case "o":
                        resultat = convertion_oct_bin(nbre, base_depart)
                    case "h":
                        resultat = convertion_hex_bin(nbre, base_depart)

            case "d":
                match base_depart:
                    case "d":
                        resultat = nbre
                    case "b":
                        resultat = convertion_bin_dec(nbre, base_depart)
                    case "o":
                        resultat = convertion_bin_dec(convertion_oct_bin(nbre, base_depart), "b")
                    case "h":
                        resultat = convertion_bin_dec(convertion_hex_bin(nbre, base_depart), "b")

            case "o":
                match base_depart:
                    case "d":
                        resultat = convertion_dec_oct(nbre, base_depart)
                    case "b":
                        resultat = convertion_dec_oct(convertion_bin_dec(nbre, base_depart), "d")
                    case "o":
                        resultat = nbre
                    case "h":
                        resultat = convertion_dec_oct(
                            convertion_bin_dec(convertion_hex_bin(nbre, base_depart), "b"), "d"
                        )

            case "h":
                match base_depart:
                    case "d":
                        resultat = convertion_dec_hex(nbre, base_depart)
                    case "b":
                        resultat = convertion_dec_hex(convertion_bin_dec(nbre, base_depart), "d")
                    case "o":
                        resultat = convertion_dec_hex(
                            convertion_bin_dec(convertion_oct_bin(nbre, base_depart), "b"), "d"
                        )
                    case "h":
                        resultat = nbre

        return {"resultat": str(resultat)}

    except Exception as e:
        return {"erreur": f"Erreur interne pendant la conversion : {e}"}
    
print(convertir("e8af","h","d"))

