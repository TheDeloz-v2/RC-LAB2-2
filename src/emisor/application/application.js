// application.js

import readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

export function solicitarMensaje() {
    return new Promise((resolve) => {
        rl.question('Ingrese el mensaje a enviar: ', (mensaje) => {
            rl.question('Ingrese el algoritmo a utilizar (Fletcher/Hamming): ', (algoritmo) => {
                rl.close();
                resolve({ mensaje, algoritmo });
            });
        });
    });
}

export function mostrarMensaje(mensaje) {
    console.log('Mensaje recibido: ', mensaje);
}
