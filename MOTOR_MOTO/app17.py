import MOTO
import MOTOR
import os

tip=os.sys.argv[1]
cab=os.sys.argv[2]
com=os.sys.argv[3]

MOT=MOTOR.Motor(3,cab,com,4,"2T")
MO=MOTO.Moto(tip,3,200,"China",MOT)
#
print(MO.avanzar())