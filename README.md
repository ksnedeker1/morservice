# morservice

A Morse-English translator microservice using ZeroMQ for OSU's CS361.

## Requesting Data

### Connection

Include the below code snippet to establish the connection. Default port is 5555.

```python
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)           # Use REQ socket for requester in request-reply pattern
socket.connect(f"tcp://localhost:5555")    # Service process uses port 5555, change in config.py if necessary
```

### Formatting Data

Valid English characters include A-Z, a-z, 0-9, symbols in [,.?;:/-'"_()=+], and space ' '. Morse is represented using '.' for short signals
and '-' for long signals, with a single space between letters and three spaces between words.

### Sending Data

The request format is a bytestring with a front control byte representing whether the message to be translated is in English or Morse. 
0x01 is used for messages to be translated from English to Morse, 0x02 for the opposite. Send this using socket.send(). See 
examples/examplerequester.py for an a more functional example.

```python
# For English to Morse
socket.send("\x01Hello World".encode())
# For English to Morse
socket.send("\x02.... . ._.. ._.. ___   .__ ___ ._. ._.. _..".encode())
```

## Receiving data
The service responds with a bytestring containing the translated message which can be automatically converted to a string using socket.recv_string(), 
or manually with socket.recv().decode().

```python
# Morse message sent
socket.send("\x02.... . ._.. ._.. ___   .__ ___ ._. ._.. _..".encode())
# English message received
response = socket.recv_string()
print(response)  # 'HELLO WORLD'
```

## UML Sequence Diagram

![UML Sequence Diagram](https://github.com/ksnedeker1/morservice/blob/master/img/umldiagram.png)
