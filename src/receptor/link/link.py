from Hamming import hamming_decode
from ChecksumFletcher import checkReceiverChecksum

def verificar_integridad(nombre, mensaje_binario, numero):
    mensaje_verificado = []
    if nombre == 'Hamming':
        # Ejecutar el algoritmo de Hamming para comprobar la integridad del mensaje
        print("\nHamming (7,4):")
        result = hamming_decode(mensaje_binario)
        mensaje_verificado.append(result[0])
        mensaje_verificado.append(result[1])
        mensaje_verificado.append(result[2])
    elif nombre == 'Fletcher':
        # Ejcuta el algoritmo de Fletcher 16 para comprobar la integridad del codigo
        print('\nFletcher Checksum 16:')
        corrected_message, status = checkReceiverChecksum(mensaje_binario, numero)
        if corrected_message:
            mensaje_verificado.append(corrected_message)
            mensaje_verificado.append(status)

        else:
            mensaje_verificado.append(corrected_message)
            mensaje_verificado.append(status)
    return mensaje_verificado

def corregir_mensaje(nombre, result):
    mensaje_corregido = []
    if nombre == 'Hamming':
        if result[1] == 'No se detectaron errores':
            mensaje_corregido.append(result[0])
            mensaje_corregido.append(result[1])
        elif result[1] == 'Se detectaron errores: el mensaje se descarta':
            mensaje_corregido.append(result[0])
            mensaje_corregido.append(result[1])
        else:
            result2 = hamming_decode(result[2])
            mensaje_corregido.append(result2[0])
            mensaje_corregido.append(result2[1])
    elif nombre == 'Fletcher':
        mensaje_corregido.append(result[0])
        mensaje_corregido.append(result[1])
    return mensaje_corregido