import IMPRESORA
import LAPTOP
import os

res=os.sys.argv[1]
mod=os.sys.argv[2]

LAP=LAPTOP.Laptop(mod,"8 RAM","WINDOWS 10",3,"A1TB")
IMP=IMPRESORA.Impresora("400 lines/min","windows",LAP,res,10)

#
print(IMP.imprimir())