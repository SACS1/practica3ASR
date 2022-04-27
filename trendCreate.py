import rrdtool
ret = rrdtool.create("rendimiento.rrd",
                     "--start",'N',
                     "--step",'300',
                     "DS:CPUload:GAUGE:300:0:100",
                     "DS:RAMload:GAUGE:300:0:100",
                     "DS:STRload:GAUGE:300:0:100",
                     "RRA:AVERAGE:0.5:1:50")
if ret:
    print (rrdtool.error())
