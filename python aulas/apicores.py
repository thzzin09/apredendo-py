#=============================
#PROGRAMA DE CORES DO THZZIN==
#=============================
cores = {
    'limpar' : '\033[m',
    'branco' : '\033[30m',
    'vermelho' : '\033[31m',
    'verde' : '\033[32m',
    'amarelo' : '\033[33m',
    'azul' : '\033[34m',
    'roxo' : '\033[35m',
    'ciano' : '\033[36m',
    'branco' : '\033[37m'
}


#============================================
#=====PROGRAMA DE CORES DO THZZIN (2.0) =====
#============================================
cores = {
    'limpar'    : '\033[m',
    
    # --- CORES DAS LETRAS (Fore) ------------
    'branco'    : '\033[37m',
    'vermelho'  : '\033[31m',
    'verde'     : '\033[32m',
    'amarelo'   : '\033[33m',
    'azul'      : '\033[34m',
    'roxo'      : '\033[35m',
    'ciano'     : '\033[36m',
    'preto'     : '\033[30m',
    
    # --- CORES DE FUNDO (Back) --------------
    'f_branco'  : '\033[47m',
    'f_vermelho': '\033[41m',
    'f_verde'   : '\033[42m',
    'f_amarelo' : '\033[43m',
    'f_azul'    : '\033[44m',
    'f_roxo'    : '\033[45m',
    'f_ciano'   : '\033[46m',
    'f_preto'   : '\033[40m',
    
    # --- ESTILOS EXTRA ----------------------
    'negrito'   : '\033[1m',
    'sublinhado': '\033[4m',
    'inverter'  : '\033[7m'
}
#=============================================

# EXEMPLO DE COMO USAR OS DOIS JUNTOS:
print(f"{cores['f_azul']}{cores['branco']} TEXTO BRANCO COM FUNDO AZUL {cores['limpar']}")
print(f"{cores['f_vermelho']}{cores['negrito']} ALERTA MÁXIMO! {cores['limpar']}")