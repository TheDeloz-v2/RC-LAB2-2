from Hamming import hamming_decode
from ChecksumFletcher import checkReceiverChecksum
def recived_information(message_fletcher, fletcher, message_hamming):
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