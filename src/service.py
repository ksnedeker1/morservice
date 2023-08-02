import zmq
from config import PORT
from src.conversions import english_to_morse, morse_to_english


context = zmq.Context()


def start_service(port=PORT):
    """
    Start the Morse-English translation microservice.

    This uses ZeroMQ's request-reply pattern to receive requests and send back the translated message. The
    communication format is a bytestring with the first byte serving as a control character to signify whether
    the request message is in English or Morse (response is translated to opposite).

        Control Characters:
            - 0x01: Request in English, response in Morse
            - 0x02: Request in Morse, response in English

        Valid Message Characters:
            - English: A-Z, a-z, 0-9, symbols in [,.?;:/-'"_()=+], and space ' '.
            - Morse: Standard combinations of '.' and '-' representing short and long signals corresponding
                     with the above defined valid English characters. Each character should be separated by
                     a space, and word should be separated by three spaces.

    :param port: The port number the service will listen for requests. Default set in src.config.PORT
    """
    socket = context.socket(zmq.REP)  # REP socket for request-reply pattern
    socket.bind(f"tcp://*:{port}")
    while True:  # socket.recv() is blocking
        data = socket.recv()
        # Unpack request for control char and message to translate
        control, message = data[0], data[1:].decode()
        try:
            # 0x01 implies request was an English string, convert to Morse
            if control == 0x01:
                translated = english_to_morse(message)
            # 0x02 implies request was a Morse string, convert to English
            elif control == 0x02:
                translated = morse_to_english(message)
            else:
                raise ValueError("Unknown or missing control character")
            # Send translated string as response
            socket.send(translated.encode())
        except Exception as e:
            socket.send(f"Error: {str(e)}".encode())
