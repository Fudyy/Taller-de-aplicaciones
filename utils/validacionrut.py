def validacion_rut(rut: str):
    rut_separado = rut.split('-')
    if len(rut_separado) != 2:
        return False

    rut_numero = rut_separado[0]
    rut_dv = rut_separado[1]

    if not rut_numero.isdigit():
        return False

    # Verificar que el dígito verificador sea válido
    if len(rut_dv) != 1:
        return False

    if not rut_dv.isdigit():
        if rut_dv != 'K' and rut_dv != 'k':
            return False

    # Calcular el dígito verificador esperado
    factor = 2
    suma = 0
    for digito in reversed(rut_numero):
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    dv_esperado = 11 - (suma % 11)
    if dv_esperado == 11:
        dv_esperado = '0'
    elif dv_esperado == 10:
        dv_esperado = 'K'
    else:
        dv_esperado = str(dv_esperado)

    # Comparar el dígito verificador calculado con el ingresado
    if rut_dv.upper() != dv_esperado:
        return False

    return True