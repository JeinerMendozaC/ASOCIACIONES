import BURRO
import CARRETA
import os

RAZA=os.sys.argv[1]
FOR=os.sys.argv[2]
MAT=os.sys.argv[3]

CARR=CARRETA.Carreta(MAT,"2","cuero",25,FOR)
BURR=BURRO.Burro(580,RAZA,"800 kg","macho",CARR)
#
print(BURR.caminar())