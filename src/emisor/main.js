import { solicitarMensaje, mostrarMensaje } from './application/application.js';
import { enviarInformacion, recibirInformacion } from './transmission/transmission.js';
import { codificarMensaje, decodificarMensaje } from './presentation/presentation.js';
import { calcularIntegridad, verificarIntegridad } from './link/link.js';
import { aplicarRuido } from './ruido/ruido.js';

async function main() {
    const { mensaje, algoritmo } = await solicitarMensaje();
    
    // Codificar mensaje
    let mensajeBinario = codificarMensaje(mensaje);
    
    // Calcular integridad
    mensajeBinario = calcularIntegridad(mensajeBinario, algoritmo);
    console.log(mensajeBinario);

    // Aplicar ruido
    const tasaError = 0.01;
    mensajeBinario = aplicarRuido(mensajeBinario, tasaError);
    
    // Enviar informacion
    enviarInformacion(mensajeBinario);
    
    // Recibir informacion
    let mensajeRecibido = await recibirInformacion();
    
    // Verificar integridad
    let errorDetectado = verificarIntegridad(mensajeRecibido, algoritmo);
    
    // Decodificar mensaje
    let mensajeDecodificado;
    if (!errorDetectado) {
        mensajeDecodificado = decodificarMensaje(mensajeRecibido);
        mostrarMensaje(mensajeDecodificado);
    } else {
        mostrarMensaje('Error: No fue posible corregir los errores.');
    }
}

main();

