import sys
import rrdtool
from  Notify import send_alert_attached
import time

ultima_lectura = int(rrdtool.last("rendimiento.rrd"))
tiempo_final = ultima_lectura
tiempo_inicial = tiempo_final - 7200


def graficaCPU():
    ret = rrdtool.graphv("monitoreoCPU.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=Cpu load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        "--title=Uso del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",

                        "DEF:cargaCPU=rendimiento.rrd:CPUload:AVERAGE",

                         "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                         "VDEF:cargaMIN=cargaCPU,MINIMUM",
                         "VDEF:cargaAVG=cargaCPU,AVERAGE",
                         "VDEF:cargaSTDEV=cargaCPU,STDEV",
                         "VDEF:cargaLAST=cargaCPU,LAST",

                         "CDEF:umbral24=cargaCPU,24,LT,0,cargaCPU,IF",
                         "CDEF:umbral45=cargaCPU,45,LT,0,cargaCPU,IF",
                         "CDEF:umbral55=cargaCPU,55,LT,0,cargaCPU,IF",
                         "AREA:cargaCPU#00FF00:Carga del CPU",
                         "AREA:umbral24#0000FF:Carga CPU mayor que 24",
                         "AREA:umbral45#FFFF00:Carga CPU mayor que 45",
                         "AREA:umbral55#FF0000:Carga CPU mayor que 55",
                         "HRULE:24#0000FF:Umbral 1 - 24%",
                         "HRULE:45#FFFF00:Umbral 25 - 45%",
                         "HRULE:55#FF0000:Umbral 46 - 55%",

                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaMAX:%6.2lf %SMAX",
                         "GPRINT:cargaAVG:%6.2lf %SAVG",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST" )
    #print (ret)

    ultimo_valor=float(ret['print[0]'])
    print("Ultimo valor: " + str(ultimo_valor))
    if ultimo_valor>55:
        send_alert_attached("CPU ESTADO GO", "monitoreoCPU.png")
        print("CPU sobrepasa Umbral línea base ESTADO GO")
    elif ultimo_valor>45:
        send_alert_attached("CPU ESTADO SET", "monitoreoCPU.png")
        print("CPU sobrepasa Umbral línea base ESTADO SET")
    elif ultimo_valor>24:
        send_alert_attached("CPU ESTADO READY", "monitoreoCPU.png")
        print("CPU sobrepasa Umbral línea base ESTADO READY")
    
def graficaRAM():
    ret = rrdtool.graphv("monitoreoRAM.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=RAM load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        "--title=Uso de la RAM del agente Usando SNMP y RRDtools \n Detección de umbrales",

                        "DEF:cargaRAM=rendimiento.rrd:RAMload:AVERAGE",

                         "VDEF:cargaMAX=cargaRAM,MAXIMUM",
                         "VDEF:cargaMIN=cargaRAM,MINIMUM",
                         "VDEF:cargaAVG=cargaRAM,AVERAGE",
                         "VDEF:cargaSTDEV=cargaRAM,STDEV",
                         "VDEF:cargaLAST=cargaRAM,LAST",

                         "CDEF:umbral74=cargaRAM,74,LT,0,cargaRAM,IF",
                         "CDEF:umbral89=cargaRAM,89,LT,0,cargaRAM,IF",
                         "CDEF:umbral94=cargaRAM,94,LT,0,cargaRAM,IF",
                         "AREA:cargaRAM#00FF00:Carga de la RAM",
                         "AREA:umbral74#0000FF:Carga RAM mayor que 74",
                         "AREA:umbral89#FFFF00:Carga RAM mayor que 89",
                         "AREA:umbral94#FF0000:Carga RAM mayor que 94",
                         "HRULE:74#0000FF:Umbral 1 - 74%",
                         "HRULE:89#FFFF00:Umbral 75 - 89%",
                         "HRULE:94#FF0000:Umbral 90 - 94%",

                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaMAX:%6.2lf %SMAX",
                         "GPRINT:cargaAVG:%6.2lf %SAVG",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST" )

    ultimo_valor=float(ret['print[0]'])
    print("Ultimo valor: " + str(ultimo_valor))
    if ultimo_valor>94:
        send_alert_attached("RAM ESTADO GO", "monitoreoRAM.png")
        print("RAM sobrepasa Umbral línea base ESTADO GO")
    elif ultimo_valor>89:
        send_alert_attached("RAM ESTADO SET", "monitoreoRAM.png")
        print("RAM sobrepasa Umbral línea base ESTADO SET")
    elif ultimo_valor>74:
        send_alert_attached("RAM ESTADO READY", "monitoreoRAM.png")
        print("RAM sobrepasa Umbral línea base ESTADO READY")
        
def graficaSTR():
    ret = rrdtool.graphv("monitoreoSTR.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=STR load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        "--title=Uso de la unidad de almacenamiento del agente Usando SNMP y RRDtools \n Detección de umbrales",

                        "DEF:cargaSTR=rendimiento.rrd:STRload:AVERAGE",

                         "VDEF:cargaMAX=cargaSTR,MAXIMUM",
                         "VDEF:cargaMIN=cargaSTR,MINIMUM",
                         "VDEF:cargaAVG=cargaSTR,AVERAGE",
                         "VDEF:cargaSTDEV=cargaSTR,STDEV",
                         "VDEF:cargaLAST=cargaSTR,LAST",

                         "CDEF:umbral53=cargaSTR,53,LT,0,cargaSTR,IF",
                         "CDEF:umbral68=cargaSTR,68,LT,0,cargaSTR,IF",
                         "CDEF:umbral83=cargaSTR,83,LT,0,cargaSTR,IF",
                         "AREA:cargaSTR#00FF00:Carga de la Unidad",
                         "AREA:umbral53#0000FF:Carga de la Unidad mayor que 53",
                         "AREA:umbral68#FFFF00:Carga de la Unidad mayor que 68",
                         "AREA:umbral83#FF0000:Carga de la Unidad mayor que 83",
                         "HRULE:53#0000FF:Umbral 1 - 53%",
                         "HRULE:68#FFFF00:Umbral 54 - 68%",
                         "HRULE:83#FF0000:Umbral 69 - 83%",

                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaMAX:%6.2lf %SMAX",
                         "GPRINT:cargaAVG:%6.2lf %SAVG",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST" )

    ultimo_valor=float(ret['print[0]'])
    print("Ultimo valor: " + str(ultimo_valor))
    if ultimo_valor>83:
        send_alert_attached("Unidad de almacenamiento ESTADO GO", "monitoreoSTR.png")
        print("STR sobrepasa Umbral línea base ESTADO GO")
    elif ultimo_valor>68:
        send_alert_attached("Unidad de almacenamiento ESTADO SET", "monitoreoSTR.png")
        print("STR sobrepasa Umbral línea base ESTADO SET")
    elif ultimo_valor>53:
        send_alert_attached("Unidad de almacenamiento ESTADO READY", "monitoreoSTR.png")
        print("STR sobrepasa Umbral línea base ESTADO READY")

while(1):
    graficaCPU()
    graficaRAM()
    graficaSTR()
    time.sleep(300)
