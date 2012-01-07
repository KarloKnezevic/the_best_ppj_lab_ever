'''klasa kao tablica znakova za zadani djelokrug programa'''

class Djelokrug:
    
    def __init__( self, nad_djelokrug ):
        
        self.nad_djelokrug = nad_djelokrug
        
        self.tablica = {}   # k: ime, v: tip
    
    
    def dodaj( self, ime, tip ):
        '''dodavanje identifikatora'''
        self.tablica[ ime ] = tip
    
    
    def provjeri_funkciju( self, ime, tip ):
        '''ako postoji deklaracija ovog imena u ovom (globalnom) djelokrugu onda
        je pripadni tip te deklaracije tip
        
        vraca true ako u OVOM djelokrugu postoji deklarirana FUNKCIJA s ovim
        imenom i ISTIM tipom (za tip funkcija postoji __eq__())
        '''
        # TODO
        return True
    
    
