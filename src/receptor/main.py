from application.application import mostrar_mensaje
from transmission.transmission import recived_information
from presentation.presentation import decodificar_mensaje
from link.link import verificar_integridad, corregir_mensaje
from Hamming import hamming_decode
from ChecksumFletcher import checkReceiverChecksum
from Receptor import connection


def main():
    data = connection()
    recived_information(data[0],data[1],data[2])
    # Ejecutar el algoritmo de Hamming para comprobar la integridad del mensaje
    print("\nHamming (7,4):")
    received_message = input("Ingrese el mensaje codificado: ")
    result = hamming_decode(received_message)
    
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
    corrected_message, status = checkReceiverChecksum()
    
    if corrected_message:
        print(status)
    else:
        print(status)
if __name__ == "__main__":
    main()