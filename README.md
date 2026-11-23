# export_dbviewer

Script em Python que automatiza a exportação de uma tabela aberta no DBF Viewer, em blocos de 50 registros, usando [PyAutoGUI](https://pyautogui.readthedocs.io/).

Fiz para exportar uma tabela com mais de mil registros sem repetir o processo na mão. O script repete o fluxo de salvar e preencher o intervalo de registros até chegar ao fim da tabela.

## Requisitos

- Windows, com o DBF Viewer instalado
- Python 3.10 ou superior
- Tela em 1920x1080, porque o script clica em uma posição fixa da caixa de diálogo

## Instalação

```bash
git clone https://github.com/femanix/export_dbviewer.git
cd export_dbviewer
pip install -r requirements.txt
```

## Uso

1. Abra a tabela no DBF Viewer e deixe a pasta de destino já selecionada na caixa de salvar.
2. Ajuste no topo do `main.py` o registro inicial (`inicio`), o tamanho de cada bloco (`intervalo`) e o total de registros (`fim`).
3. Rode o script e, nos 3 segundos seguintes, coloque a janela do DBF Viewer em primeiro plano:

```bash
python main.py
```

Cada bloco é salvo com o nome `alunos_export [inicio] - [fim]`.

Para interromper, leve o mouse ao canto superior esquerdo da tela. É a trava de segurança padrão do PyAutoGUI.
