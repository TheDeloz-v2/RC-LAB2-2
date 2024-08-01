from application.application import mostrar_mensaje
from transmission.transmission import recived_information
from presentation.presentation import decodificar_mensaje
from link.link import verificar_integridad, corregir_mensaje
import socket

def main():

    HOST = "127.0.0.1"  # IP, capa de Red. 127.0.0.1 es localhost
    PORT = 3000       # Puerto, capa de Transporte

    # AF_INET especifica IPv4,
    #   tambien hay AF_INET6
    # SOCK_STREAM especifica TCP,
    #   tambien hay SOCK_DGRAM para UDP y otros...
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #bind reserva/asigna tal socket a una IP:puerto especifica
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}")
        while True:
            #accept() bloquea y deja esperando
            conn, addr = s.accept()
            with conn:
                nombre, mensaje_binario, numero = recived_information(conn)
                #recived_information(data[0],data[1],data[2])
                mensaje_verificado = verificar_integridad(nombre, mensaje_binario, numero)
                print("Estado del mensaje verificado: " + mensaje_verificado[1])
                mensaje_corregido = corregir_mensaje(nombre, mensaje_verificado)
                if mensaje_corregido[1] != 'Se detectaron errores: el mensaje se descarta':
                    print("Mensaje corregido: " + mensaje_corregido[0])
                    mensaje_final = decodificar_mensaje(mensaje_corregido[0])
                    mostrar_mensaje(mensaje_final)
                mostrar_mensaje(mensaje_corregido[1])
if __name__ == "__main__":
    main()