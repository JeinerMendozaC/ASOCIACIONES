import CASA
import HABITACION
import os
ubi=os.sys.argv[1]
AF=os.sys.argv[2]
MA=os.sys.argv[3]

CAS=CASA.Casa(ubi,"60 m","cemento",3,10)
HAB=HABITACION.Habitacion("al lado de la cocina",2,CAS,MA,AF)
#
print(HAB.getAforo())