import PUNTO
import VECTOR
import os

coor=os.sys.argv[1]
tip=os.sys.argv[2]
ang=os.sys.argv[3]

VEC=VECTOR.Vector(tip,5,ang,"4/3","X-Y")
PUN=PUNTO.Punto(coor,VEC,"I",4,1)

print(PUN.ubicar())