import CAMARA
import CELULAR
import os

sis=os.sys.argv[1]
res=os.sys.argv[2]
efec=os.sys.argv[3]


CEL=CELULAR.Celular(sis,"Redmi",0.2,"8 RAM","4500 mA")
CAM=CAMARA.Camara(res,"compacta",CEL,efec,"1,6um")

#
print(CAM.tomar_fotos())