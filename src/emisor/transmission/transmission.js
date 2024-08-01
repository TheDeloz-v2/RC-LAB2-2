// transmission.js

export function enviarInformacion(mensajeBinario, socket) {
    socket.write(mensajeBinario[0]);
    socket.write(mensajeBinario[1]);
}

