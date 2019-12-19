import DOCTOR
import HOSPITAL
import os

Ap=os.sys.argv[1]
Hos=os.sys.argv[2]

HOS=HOSPITAL.Hospital(Hos,"lambayeque",56,500,2)
DOC=DOCTOR.Doctor("cardiologo",Ap,"UNPRG",HOS,57)

print(DOC.operar())