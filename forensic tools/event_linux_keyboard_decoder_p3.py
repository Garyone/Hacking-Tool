import struct 
import evdev

file = input("stream to decode?")
f = open(file, "rb" ); 
datax= []
try: 
  while True:
    data = f.read(24)
    (tv_sec, tv_usec, type, code, value, x, y) = struct.unpack('4IHHI',data)
    datax.append(evdev.ecodes.KEY[x])

except Exception:
    print("finished")

finally:
    final = ''
    for i in range(len(datax)):
       final = datax[i] + ' '+final    
    print("Stream : ",final)
