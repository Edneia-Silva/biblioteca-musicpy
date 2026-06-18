from musicpy import *
import random
import os

notas = ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']

sequencia = ','.join(random.choice(notas) for _ in range(20))

melodia = chord(sequencia)

melodia.interval = [0.25] * 20

write(melodia, name='musica.mid')

os.startfile('musica.mid')