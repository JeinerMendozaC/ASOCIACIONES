import EMPRESA
import TRABAJADOR
import os

nom_em=os.sys.argv[1]
car=os.sys.argv[2]
hor=os.sys.argv[3]
sal=os.sys.argv[4]

EM=EMPRESA.Empresa(nom_em,"Los alpes",200,"privada",1000000)
TRA=TRABAJADOR.Trabajador(sal,45,hor,EM,car)

#
print(TRA.trabajar())
