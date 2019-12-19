import COLEGIO
import ESTUDIANTE
import os

nom_al=os.sys.argv[1]
tip=os.sys.argv[2]
nom_col=os.sys.argv[3]
grad=os.sys.argv[4]

COL=COLEGIO.Colegio(nom_col,tip,1500,"PRIMARIO Y SECUNDARIO",25)
ALU=ESTUDIANTE.Estudiante(COL,grad,"A",16,18,nom_al)
#
print(ALU.aprender())