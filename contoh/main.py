from persegi import Persegi    
from persegi_controller import persegiController    
from persegi_view import PersegiView 

persegi = Persegi(2)
penghitung_persegi = PersegiController()
penampil_persegi = Persegiview()  

penampil_persegi.show_luas(persegi, penghitung_persegi)
penampil_persegi.show_keliling(persegi, penghitung_persegi)
