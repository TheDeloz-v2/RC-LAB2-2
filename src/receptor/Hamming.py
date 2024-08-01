def hamming_decode_block(block):
    """
    Decodifica un mensaje utilizando el código de Hamming y verifica la integridad del mensaje.
    
    Parámetros:
    received_message (str): Un mensaje binario concatenado con la información generada por el emisor.
    
    Retorna:
    tuple: Una tupla que contiene:
           - El mensaje original sin la información generada por el emisor si no se detectaron errores.
           - Un estado indicando si no se detectaron errores, si el mensaje se descarta por errores,
             o si se corrigieron errores, junto con la posición de los bits corregidos y el mensaje corregido.
    """
    def calculate_parity_positions(data_length):
        
        # Calcula las posiciones de los bits de paridad en el mensaje de longitud data_length
        parity_positions = []
        i = 0
        while (2**i) <= data_length:
            parity_positions.append(2**i)
            i += 1
        return parity_positions

    def calculate_parity_bits(data, parity_positions):
        # Calcula los bits de paridad para los datos dados
        parity_bits = [0] * len(parity_positions)
        for i in range(1, len(data) + 1):
            if data[i - 1] == '1':
                for j in range(len(parity_positions)):
                    if i & parity_positions[j]:
                        parity_bits[j] ^= 1
        return parity_bits

    def find_error_position(parity_bits):
        # Encuentra la posición del error en el mensaje usando los bits de paridad calculados
        error_position = 0
        for i in range(len(parity_bits)):
            if parity_bits[i] == 1:
                error_position += 2**i
        return error_position
    

    # Paso 1: Solicitar mensaje en binario concatenado con la información generada por el emisor
    data = block
    
    # Calcular las posiciones de los bits de paridad
    parity_positions = calculate_parity_positions(len(data))
    
    # Calcular los bits de paridad en el mensaje recibido
    received_parity_bits = calculate_parity_bits(data, parity_positions)
    
    # Encontrar la posición del error si existe
    error_position = find_error_position(received_parity_bits)

    if error_position == 0:
        # No se detectaron errores
        original_message = ''.join([data[i-1] for i in range(1, len(data) + 1) if i not in parity_positions])
        return original_message, 'No se detectaron errores', block
    else:
        # Se detectaron errores, corregir el bit en la posición del error
        error_position -= 1  # Ajustar la posición del error para el índice de la lista
        corrected_data = list(data)
        corrected_data[error_position] = '0' if data[error_position] == '1' else '1'
        corrected_message = ''.join(corrected_data)
        
        # Verificar nuevamente los bits de paridad para asegurarse de que la corrección fue exitosa
        corrected_parity_bits = calculate_parity_bits(corrected_message, parity_positions)
        if sum(corrected_parity_bits) == 0:
            # Se corrigieron errores
            original_message = ''.join([corrected_message[i-1] for i in range(1, len(corrected_message) + 1) if i not in parity_positions])
            return original_message, f'Se detectaron y corrigieron errores en la posición {error_position + 1}', corrected_message
        else:
            # No se pudieron corregir todos los errores
            return None, 'Se detectaron errores: el mensaje se descarta', None

def hamming_decode(received_message):

    if len(received_message) % 7 != 0:
        return None, "Error de longitud: el mensaje debe ser múltiplo de 7 bits."

    blocks = [received_message[i:i+7] for i in range(0, len(received_message), 7)]
    original_message = ""
    corrected_message = ""
    errors_detected = False
    errors_corrected = False
    corrected_positions = []

    for block in blocks:
        block_message, status, corrected_block = hamming_decode_block(block)
        if status == 'No se detectaron errores':
            original_message += block_message
            corrected_message += block
        elif status == 'Se detectaron errores: el mensaje se descarta':
            return None, 'Se detectaron errores: el mensaje se descarta'
        else:
            errors_corrected = True
            corrected_positions.append((blocks.index(block) * 7) + int(status.split()[-1]) - 1)
            original_message += block_message
            corrected_message += corrected_block

    if errors_corrected:
        return original_message, f'Se detectaron y corrigieron errores en las posiciones {corrected_positions}', corrected_message
    else:
        return original_message, 'No se detectaron errores', received_message
