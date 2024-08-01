from Hamming import hamming_decode
from ChecksumFletcher import checkReceiverChecksum

import re

def recived_information(conn):
    lista_mensaje = []
    while True: #en caso se envien mas de 1024 bytes
        #recibir 1024 bytes
        data = conn.recv(1024)
        if not data:
            break   #ya se recibio todo
        print(f"Mensaje recibido: \n {data}")
        data_str = data.decode('utf-8')  # Convertir de bytes a string
        nombre, mensaje_binario, numero = procesar_datos(data_str)
        return nombre, mensaje_binario, numero

def procesar_datos(data):
    # Usar regex para separar las partes
    match = re.match(r"([a-zA-Z]+)([01]+)(\w*)", data)
    if match:
        nombre = match.group(1)  # Parte de texto (nombre)
        mensaje_binario = match.group(2)  # Parte de binario
        numero = match.group(3)  # Parte de números y letras (puede estar vacía)
        return nombre, mensaje_binario, numero
    else:
        return None, None, None


def recived_info(message_fletcher, fletcher, message_hamming):
    result = hamming_decode(message_hamming)
    
    if result[1] == 'No se detectaron errores':
        print(f"Mensaje original: {result[0]}")
    elif result[1] == 'Se detectaron errores: el mensaje se descarta':
        print(result[1])
    else:
        print(f"{result[1]}")
        print(f"Mensaje corregido: {result[2]}")
        result2 = hamming_decode(result[2])
        print(f"Mensaje original: {result2[0]}")
    # Ejcuta el algoritmo de Fletcher 16 para comprobar la integridad del codigo
    print('\nFletcher Checksum 16:')
    corrected_message, status = checkReceiverChecksum(message_fletcher, fletcher)
    
    if corrected_message:
        print(status)
    else:
        print(status)