import OBRA
import AUTOR
import os
tit_obra1=os.sys.argv[1]
tit_obra2=os.sys.argv[2]
nom_autor=os.sys.argv[3]
AUR=AUTOR.Autor(nom_autor,"Peruano",20,58,7)
OB1=OBRA.Obra(tit_obra1,300,"diciembre_1980",AUR,"obra literaria")
OB2=OBRA.Obra(tit_obra2,150,"enero 2000",AUR,"poesia")
#
print(OB1.leer())