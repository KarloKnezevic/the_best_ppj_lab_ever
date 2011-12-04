'''nka model'''

from generator.dka import DKA

class NKA:
    
    def __init__( self, stanja, ulazni_znakovi, pocetno_stanje, prihvatljiva,
                prijelazi ):
        
        
        self.stanja             = set(stanja)           # skup LR1Stavki
        self.prihvatljiva       = set(prihvatljiva)     # skup LR1Stavki
        self.ulazni_znakovi     = set(ulazni_znakovi)   # skup stringova
        self.pocetno_stanje     = pocetno_stanje        # LR1Stavka
        self.prijelazi          = dict(prijelazi)       # rjecnik: kljuc = par (LR1Stavka, string)
                                                        # vrijednost = skup LR1Stavki
    
    
    def kreiraj_dka( self ):
        '''vraca instancu DKA
        generalno: knjiga utr, str 32
        MAK
        '''
        
<<<<<<< HEAD
        q0 = set ({self.pocetno_stanje})
        stanjaDKA = set (q0)        
=======
        q0 = frozenset ({self.pocetno_stanje})
        stanjaDKA = set (q0)
>>>>>>> 6d0c8cb303f1d480cb3588182568e75c73d01c3e
        
        postoji_neprihvatljivo = False
        obradjena = set()
        q1 = set()
        
        
        Q = set()
        for s in self.stanja:
            Q.add(frozenset({s}))
        
        prijelaziDKA = dict()
        
<<<<<<< HEAD
        
=======
>>>>>>> 6d0c8cb303f1d480cb3588182568e75c73d01c3e
        while len (Q) > len (obradjena):
            #print ("Sva stanja: " + str (Q))
            #print ("obradjena: " + str(obradjena))
            q1 = ((Q - obradjena).pop())
            
            #print ("Obradjujem stanje " + str (q1))
            
            obradjena.add(frozenset(q1))
            
            #input ()
            
            for z in self.ulazni_znakovi:
                
                new_q = set()
                
                for q in q1:
                  
<<<<<<< HEAD
                    new_q = new_q.union(frozenset ({self.prijelazi.get((q, z), {})}))
                    
                    
=======
                    new_q = new_q.union(frozenset (self.prijelazi.get((q, z), {})))
>>>>>>> 6d0c8cb303f1d480cb3588182568e75c73d01c3e
                
                if new_q:
                    stanjaDKA.add(frozenset(new_q))
                    prijelaziDKA[(frozenset(q1), z)] = new_q
                    
                else:
                    postoji_neprihvatljivo = True
                
            #input()
         
<<<<<<< HEAD
        F = stanjaDKA.copy()
        
        if postoji_neprihvatljivo:
            stanjaDKA.add(None)
            
=======
        F = stanjaDKA
        
        if postoji_neprihvatljivo:
            stanjaDKA.add(None)
>>>>>>> 6d0c8cb303f1d480cb3588182568e75c73d01c3e
        
        return DKA (stanjaDKA, self.ulazni_znakovi, q0, F, prijelaziDKA)