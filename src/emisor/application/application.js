// application.js

export function solicitarMensaje(rl) {
    return new Promise((resolve) => {
        rl.question('Ingrese el mensaje a enviar: ', (mensaje) => {
            rl.question('Ingrese el algoritmo a utilizar (Fletcher/Hamming): ', (algoritmo) => {
                resolve({ mensaje, algoritmo });
            });
        });
    });
}

export function mostrarMensaje(mensaje) {
    console.log('Mensaje recibido: ', mensaje);
}