// ruido.js

export function aplicarRuido(mensajeBinario, tasaError) {
    let mensajeConRuido = '';
    for (let i = 0; i < mensajeBinario.length; i++) {
        if (Math.random() < tasaError) {
            mensajeConRuido += mensajeBinario[i] === '0' ? '1' : '0';
        } else {
            mensajeConRuido += mensajeBinario[i];
        }
    }
    return mensajeConRuido;
}
