import AGUA
import TANQUE
import os

comp=os.sys.argv[1]
mat=os.sys.argv[2]
cap=os.sys.argv[3]

TAN=TANQUE.Tanque(mat,cap,"cilindrico",20,"madera")
AGU=AGUA.Agua(25,TAN,"1g/cmm3",comp,100)
#
print(AGU.tomar())
