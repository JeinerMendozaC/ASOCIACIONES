import DOCENTE
import UNIVERSIDAD
import os

nomd=os.sys.argv[1]
tip=os.sys.argv[2]
nU=os.sys.argv[3]

UNI=UNIVERSIDAD.Universidad(tip,nU,1400,"Lambayeque",12)
DO=DOCENTE.Docente("Matematica",nomd,UNI,45,"doctor")

print(DO.instruir())