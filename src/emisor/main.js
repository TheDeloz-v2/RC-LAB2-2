import { solicitarMensaje, mostrarMensaje } from './application/application.js';
import { enviarInformacion } from './transmission/transmission.js';
import { codificarMensaje } from './presentation/presentation.js';
import { calcularIntegridad } from './link/link.js';
import { aplicarRuido } from './ruido/ruido.js';
import net from 'net';
import dotenv from 'dotenv';
import readline from 'readline';

async function main() {
    try {
        dotenv.config();
        const ip = process.env.SOCKET_IP || '127.0.0.1';
        const port = process.env.SOCKET_PORT || 3000;
        const noiseRate = process.env.NOISE_RATE || 0.1;

        const socket = new net.Socket();

        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        console.log('Awaiting server ' + ip + ':' + port);
        socket.connect(port, ip, async () => {
            console.log('Connected to server ' + ip + ':' + port);

            while (true) {
                const { mensaje, algoritmo } = await solicitarMensaje(rl);

                if (mensaje === 'EXIT') {
                    break;
                }

                // Codificar mensaje
                let mensajeBinario = codificarMensaje(mensaje);
                console.log('Mensaje codificado:', mensajeBinario);
                console.log('Longitud mensaje:', mensajeBinario.length);

                // Calcular integridad
                mensajeBinario = calcularIntegridad(mensajeBinario, algoritmo);
                console.log('Mensaje con integridad:', mensajeBinario);

                // Aplicar ruido
                if (algoritmo === 'Hamming') {
                    mensajeBinario = aplicarRuido(mensajeBinario[0], noiseRate);
                    console.log('Mensaje con ruido:', mensajeBinario);

                } else if (algoritmo === 'Fletcher') {
                    const mensajeBinarioRuido = aplicarRuido(mensajeBinario[0], noiseRate);
                    const checksum = mensajeBinario[1];
                    mensajeBinario = mensajeBinarioRuido+checksum;
                    console.log('Mensaje con ruido:', mensajeBinarioRuido);
                }

                // Enviar información
                enviarInformacion([algoritmo, mensajeBinario], socket);
            }

            socket.end();
            rl.close();
        });

        socket.on('error', (err) => {
            console.error('Error: ' + err);
        });

    } catch (err) {
        console.error('Error:', err);
    }
}

main();
