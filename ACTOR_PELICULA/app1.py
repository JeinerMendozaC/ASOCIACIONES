import ACTOR
import PELICULA
import os
nom_actor1=os.sys.argv[1]
nom_actor2=os.sys.argv[2]
nom_pelicula=os.sys.argv[3]
AC1=ACTOR.Actor(nom_actor1,"16/06/1980","masculino",40,12)
AC2=ACTOR.Actor(nom_actor2,"02/07/1990","femenino",30,10)
PELI=PELICULA.Pelicula(nom_pelicula,AC1,"2 horas",10,"Pablo Orlando")
NOM=AC2.getNombre()
print(PELI.observar(),"y",NOM)
