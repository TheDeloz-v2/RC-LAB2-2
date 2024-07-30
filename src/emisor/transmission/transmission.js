// transmission.js

import net from 'net';

export function enviarInformacion(mensaje) {
    const client = new net.Socket();
    client.connect(1337, '127.0.0.1', function() {
        console.log('Conectado al servidor');
        client.write(mensaje);
        client.end();
    });

    client.on('error', (err) => {
        console.error('Error en la conexión:', err.message);
    });
}

export function recibirInformacion() {
    return new Promise((resolve, reject) => {
        const server = net.createServer(function(socket) {
            socket.on('data', function(data) {
                resolve(data.toString());
                server.close();
            });

            socket.on('error', (err) => {
                reject('Error en la conexión: ' + err.message);
            });
        });

        server.listen(1337, '127.0.0.1', () => {
            console.log('Esperando datos en el puerto 1337...');
        });
    });
}
