import zmq
from config import PORT

context = zmq.Context()
socket = context.socket(zmq.REQ)  # Use REQ socket for requester in request-reply pattern
socket.connect(f"tcp://localhost:{PORT}")  # Connect socket for communication (set PORT in config, default 5555)


def send_request(is_english, message, socket):
    """
    Example request-sending function for Morse encoder/decoder microservice.
    :param is_english: True if input is English and desired response is Morse, False for the opposite.
    :param message: The message to send (string)
    :param socket: The zmq.context.socket object connected to correct port
    :return: Response from service as a string.
    """
    # 0x01 is used to signify the subsequent bytestring is English (to be encoded as Morse)
    if is_english:
        control = b'\x01'
    # 0x02 is used to signify the subsequent bytestring is Morse (to be encoded as English)
    else:
        control = b'\x02'
    # Send the request with the format control_byte + bytestring_message
    socket.send(control + message.encode())
    response = socket.recv_string()
    return response


if __name__ == "__main__":
    text = "Hello world"
    print(f"Original:          {text}")
    morse = send_request(True, text, socket)
    print(f"Morse:             {morse}")
    translated = send_request(False, morse, socket)
    print(f"Back to English:   {translated}")
