
# Mido

## 1.  Receiving and displaying midi messages
 
```
import mido

portname = "Digital Piano"

with mido.open_input(portname) as inport:
    for msg in inport:
        print(msg)
```
## 2.  Handling midi messages with a callback function

```

import mido
import time
def listen_input(message):
    if message.type == 'note_on':
        print('input:', message)
    # print (message.note)
inport = mido.open_input('Digital Piano', callback=listen_input)


while True:
    time.sleep(0.1)

```
