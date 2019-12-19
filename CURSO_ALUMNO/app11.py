import ALUMNO
import CURSO
import os

nom_cur=os.sys.argv[1]
Nom_al=os.sys.argv[2]
tip_INS=os.sys.argv[3]

CUR=CURSO.Curso(nom_cur,4,"programacion I"," 3 ciclos",tip_INS)
AL=ALUMNO.Alumno(Nom_al,"123488I",CUR,"Universitario",16.3)

#
print(AL.matricular())
