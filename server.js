import net from 'net';

const server = net.createServer((socket) => {
    console.log('Cliente conectado');

    socket.on('data', (data) => {
        console.log('Mensaje recibido: ' + data);
        socket.write('Mensaje recibido: ' + data);
    });

    socket.on('end', () => {
        console.log('Cliente desconectado');
    });

    socket.on('error', (err) => {
        console.error('Error en el socket: ' + err.message);
    });
});

server.listen(3000, '127.0.0.1', () => {
    console.log('Servidor escuchando en 127.0.0.1:3000');
});

