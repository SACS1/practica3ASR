import time
import rrdtool
from getSNMP import consultaSNMP
#rrdpath = '/home/tani/PycharmProjects/Introduccion_SNMP/5-AdministraciónDeRendimiento/RRD/'
carga_CPU = 0
totalRAM = 2028056 #kb
totalSTR = 25639140 #kb

def obtenerRAMUse():
    porcentaje_RAM = 0
    uso_RAM = 0
    uso_RAM = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.25.2.3.1.6.1'))
    porcentaje_RAM = (uso_RAM*100)/totalRAM
    return porcentaje_RAM
    
def obtenerSTRUse():
    porcentaje_STR = 0
    uso_STR = 0
    uso_STR = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.25.2.3.1.6.36'))
    uso_STR = uso_STR*4 #cantidad de KB por bloque
    porcentaje_STR = (uso_STR*100)/totalSTR
    return porcentaje_STR


while 1:
    carga_CPU = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.25.3.3.1.2.196608'))
    carga_RAM = int(obtenerRAMUse())
    carga_STR = int(obtenerSTRUse())
    valor = "N:" + str(carga_CPU) + ":" + str(carga_RAM) + ":" + str(carga_STR)
    print(valor)
    rrdtool.update('rendimiento.rrd', valor)
    #rrdtool.dump('rendimiento.rrd','rendimiento.xml')
    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
