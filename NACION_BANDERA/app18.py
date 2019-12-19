import BANDERA
import NACION
import os

cols=os.sys.argv[1]
na=os.sys.argv[2]

NA=NACION.Nacion(na,12345666,"martin vizcarra","america","lima")
BA=BANDERA.Bandera(NA,3,"escudo",cols,"28-07-1824")
#
print(BA.representar())