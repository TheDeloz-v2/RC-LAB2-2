def fletcher16(data):
    """
    Calcula el checksum Fletcher-16 para los datos proporcionados.
    
    El checksum Fletcher-16 es un algoritmo de verificación que suma los valores de los bits de entrada
    de forma acumulativa y modular, para detectar errores en la transmisión de datos.
    
    Parámetros:
    data (str): Una cadena de bits binarios.
    
    Retorna:
    int: El checksum Fletcher-16 de los datos como un valor hexadecimal.
    """
    sum1 = 0
    sum2 = 0
    # Procesamos los datos en bytes (8 bits cada uno)
    for i in range(0, len(data), 8):
        byte = data[i:i+8]
        if len(byte) < 8:
            # Rellenar con ceros si el byte es menor a 8 bits
            byte = byte.ljust(8, '0')
        sum1 = (sum1 + int(byte, 2)) % 255
        sum2 = (sum2 + sum1) % 255
    fletch = (sum2 << 8) | sum1
    return f'{fletch:04x}'

def checkReceiverChecksum(ReceivedMessage, Fletcher):
    """
    Verifica la integridad de un mensaje binario utilizando checksum y bit de paridad.
    
    Esta función solicita al usuario un mensaje binario que incluye datos y un bit de paridad.
    Luego, calcula el checksum de los datos y su bit de paridad, y lo compara con el bit de paridad
    recibido para determinar si hay errores en el mensaje.
    
    Retorna:
    tuple: Una tupla que contiene los datos del mensaje y un estado indicando si se detectaron errores.
           Si no se detectaron errores, retorna (data, 'No se detectaron errores').
           Si se detectaron errores, retorna (None, 'Se detectaron errores: el mensaje se descarta').
    """
    # Solicitar mensaje con checksum
    ReceivedMessage = ReceivedMessage.replace(" ", "")

    #Calculamos el checksum para los primeros 4 bits
    calculated_checksum = fletcher16(ReceivedMessage)

    if Fletcher == calculated_checksum:
        return ReceivedMessage, 'No se detectaron errores'
    else:
        return None, 'Se detectaron errores: el mensaje se descarta'


def main():

    # Verificar la integridad del mensaje
    corrected_message, status = checkReceiverChecksum()
    
    if corrected_message:
        print(status)
    else:
        print(status)

if __name__ == "__main__":
    main()
