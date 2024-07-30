// Hamming.js

// Function to calculate the parity bit for a given position
function calculateParityBit(encodedMessage, parityPosition) {
    let parityBit = 0;
    for (let i = 0; i < encodedMessage.length; i++) {
        // Check if the current position has the parity bit in its binary representation
        if ((i + 1) & parityPosition) {
            parityBit ^= encodedMessage[i];
        }
    }
    return parityBit;
}

// Function to encode a message using Hamming code
function encodeMessage(data) {

    let lines = data.match(/.{1,4}/g);
    console.log(lines);

    let encodedMessage = [];  

    for (let line of lines) {
        line = line.split('').map(Number);
        const n = line.length;
        const m = Math.ceil(Math.log2(n + 1));

        if (n === 0) {
            throw new Error('The data is empty');
        } 

        if (n % 4 !== 0) {
            throw new Error('The length of the data must be a multiple of 4');
        }

        if (n / 4 >= 1) {
            const vueltas = n / 4;

            for (let i = 0; i < vueltas; i++) {
                let dataChunk = line.slice(i * 4, (i + 1) * 4);
                let encodedChunk = encodeChunk(dataChunk);
                encodedMessage.push(...encodedChunk);
            }
            
        }
    }
    
    return encodedMessage.join('');
}


function encodeChunk(data) {
    const n = data.length;
    const m = Math.ceil(Math.log2(n + 1));
    const totalLength = n + m;
    const encodedMessage = new Array(totalLength).fill(0);

    // Insert data bits into the encodedMessage leaving space for parity bits
    let dataIdx = 0;
    for (let i = 1; i <= totalLength; i++) {
        if ((i & (i - 1)) === 0) {
            // Position is a power of two, reserve for parity bit
            continue;
        }
        encodedMessage[i - 1] = data[dataIdx++];
    }

    // Calculate the parity bits and insert them
    for (let i = 0; i < m; i++) {
        const parityPosition = 1 << i;
        encodedMessage[parityPosition - 1] = calculateParityBit(encodedMessage, parityPosition);
    }

    let encodedMessageString = encodedMessage.join('');

    return encodedMessageString;
} 

// Function to decode a message encoded using Hamming code
function decodeMessage(encodedMessage) {
    const totalLength = encodedMessage.length;
    const m = Math.ceil(Math.log2(totalLength));
    const n = totalLength - m;
    const data = new Array(n);

    // Copy the data bits from the encodedMessage
    let dataIdx = 0;
    for (let i = 1; i <= totalLength; i++) {
        if ((i & (i - 1)) === 0) {
            // Position is a power of two, skip parity bit
            continue;
        }
        data[dataIdx++] = encodedMessage[i - 1];
    }

    // Verify the parity bits
    for (let i = 0; i < m; i++) {
        const parityPosition = 1 << i;
        const parityBit = calculateParityBit(encodedMessage, parityPosition);
        if (encodedMessage[parityPosition - 1] !== parityBit) {
            throw new Error('Error decoding the message');
        }
    }

    return data;
}

export { encodeMessage, decodeMessage };

 
