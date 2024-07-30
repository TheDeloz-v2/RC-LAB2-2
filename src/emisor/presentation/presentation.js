// presentation.js

export function codificarMensaje(mensaje) {
    return mensaje.split('').map(char => char.charCodeAt(0).toString(2).padStart(8, '0')).join('');
}

export function decodificarMensaje(mensajeBinario) {
    let mensaje = '';
    for (let i = 0; i < mensajeBinario.length; i += 8) {
        const byte = mensajeBinario.slice(i, i + 8);
        mensaje += String.fromCharCode(parseInt(byte, 2));
    }
    return mensaje;
}
