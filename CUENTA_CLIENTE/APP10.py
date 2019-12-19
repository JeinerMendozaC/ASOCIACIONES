import CLIENTE
import CUENTA
import os

nom=os.sys.argv[1]
tip=os.sys.argv[2]
age=os.sys.argv[3]

CUEN=CUENTA.Cuenta("12/01/2019","20/02/2020",tip,1200,"copia de dni")
CLI=CLIENTE.Cliente(nom,678907654,CUEN,"San juan de lurigancho",age)

#
print(CLI.ahorrar())