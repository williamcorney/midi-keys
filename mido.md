
# Mido

## 1.  Receiving and displaying midi messages
 
```
import mido

portname = "Digital Piano"

with mido.open_input(portname) as inport:
    for msg in inport:
        print(msg)
```
