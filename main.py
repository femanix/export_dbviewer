import pyautogui
import time
'''
Resolução da tela: 1920x1080 
Já deixar antes mapeado a pasta onde irá salvar na cx de diálogo 
'''
# Função para salvar e nomear o arquivo
def salvar_arquivo(inicio, fim):
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.write(f'alunos_export [{inicio}] - [{fim}]')
    pyautogui.hotkey('alt', 's')
    time.sleep(0.5)

# Função para preencher o diálogo de salvar
def preencher_dialogo(inicio, fim):
    pyautogui.hotkey('alt', 'd')
    pyautogui.click(948, 558)
    pyautogui.write(str(inicio))
    pyautogui.press('tab')
    pyautogui.write(str(fim))
    pyautogui.hotkey('alt', 'o')
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'n')
    time.sleep(1)

# Configurações
inicio = 1
intervalo = 49
fim = 1310 # Quantidade de itens na tabela

# Espera inicial
time.sleep(3)

# Loop para criar os arquivos
while inicio < fim + 50:
    fim = inicio + intervalo
    salvar_arquivo( inicio, fim)
    preencher_dialogo(inicio, fim)
    inicio = fim + 1
