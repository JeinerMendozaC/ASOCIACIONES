import BILLETERA
import DINERO
import os
mat_bi=os.sys.argv[1]
vaL=os.sys.argv[2]
tip_bil=os.sys.argv[3]
sim=os.sys.argv[4]
BI1=BILLETERA.Billetera(mat_bi,5,40,"buena",tip_bil)
DIN1=DINERO.Dinero(sim,vaL,"peru",BI1,"2018")
#
print(DIN1.comprar())