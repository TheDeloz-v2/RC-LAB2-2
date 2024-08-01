// link.js

import { fletcher16, verificarChecksumFletcher } from '../ChecksumFletcher.js';
import { encodeMessage, decodeMessage } from '../Hamming.js';

export function calcularIntegridad(mensajeBinario, algoritmo) {
    if (algoritmo === 'Fletcher') {
        const checksum = fletcher16(mensajeBinario);
        return [mensajeBinario, checksum];
    } else if (algoritmo === 'Hamming') {
        const encodedMessage = encodeMessage(mensajeBinario);
        return [encodedMessage, ''];
    } else {
        throw new Error('Algoritmo no soportado');
    }
}

export function verificarIntegridad(mensajeBinario, algoritmo) {
    if (algoritmo === 'Fletcher') {
        return !verificarChecksumFletcher(mensajeBinario);
    } else if (algoritmo === 'Hamming') {
        try {
            decodeMessage(mensajeBinario);
            return false;
        } catch (error) {
            return true;
        }
    } else {
        throw new Error('Algoritmo no soportado');
    }
}

