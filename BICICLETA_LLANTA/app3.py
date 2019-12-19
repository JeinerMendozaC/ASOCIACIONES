import BICICLETA
import LLANTA
import os
mat_llanta=os.sys.argv[1]
rayos=os.sys.argv[2]
tipobic=os.sys.argv[3]
BIC=BICICLETA.Bicicleta(tipobic,500,8,"Cuero",160)
LL=LLANTA.Llanta(mat_llanta,2,BIC,50,"aluminio")
print(LL.rodar())