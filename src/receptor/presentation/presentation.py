
def decodificar_mensaje(mensaje_binario):
    mensaje = ''
    for i in range(0, len(mensaje_binario), 8):
        byte = mensaje_binario[i:i+8]
        mensaje += chr(int(byte, 2))
    return mensaje