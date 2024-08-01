// transmission.js

export function enviarInformacion(mensajeBinario, socket) {
    const mensajeCompleto = mensajeBinario[0] + mensajeBinario[1];
    socket.write(mensajeCompleto);
}

