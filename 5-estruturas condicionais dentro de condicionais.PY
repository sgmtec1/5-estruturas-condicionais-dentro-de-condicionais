# Estruturas condicionais dentro de condicionais
from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM6')

nota = int(input(lcd.escrever(board, 0, 0, 'DIGITE A NOTA')))


if nota >=9:
    lcd.escrever(board, 0, 0, 'PARABENS              ')
    lcd.escrever(board, 0, 1, 'QUADRO DE HONRA       ')
elif nota >= 7:
    lcd.escrever(board, 0, 0, 'APROVADO               ')
    lcd.escrever(board, 0, 1, '                       ')
elif nota >= 5:
    lcd.escrever(board, 0, 0, 'RECUPERACAO             ')
    lcd.escrever(board, 0, 1, '                        ')
else: 
    lcd.escrever(board, 0, 0, 'REPROVADO        ')
    lcd.escrever(board, 0, 1, '                 ')
time.sleep(100.0)
lcd.limpar(board)
board.exit()