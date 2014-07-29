# -*- coding: UTF-8 -*-

import pylab		# Для графиков
import math			# Для sin(), cos()
import random
from numpy import *	# Для функции arange(), функция поддерживает тип float для аргументов

# ######### Входные данные ##############

Fd = 200.0 					# Частота дискретизации аналогового несущего сигнала
Fdd = 500.0 				# Частота дискретизации цифрового исходного сигнала
Fc = 20.0 					# Частота несущей
N = 30						# Количество передающихся символов
speed = 10.0 				# Символьная скорость (частота символов)
duration = 1 / speed		# Длительность импульса
time_signal = N * duration	# Длительность исходного сигнала из N импульсов
M = 2 						# Количество уровней модуляции

# Формируем исходную последовательность символов
source_sequence = [random.randint(0, M) for x in range(0, N)]

Wc = 2 * math.pi * Fc  		#Угловая частота несущей

# Формируем список значений исходного сигнала
source_signal = []
for x in range(0, N):
	source_signal += [source_sequence[x] for y in arange(0, duration, (1.0 / Fdd))]

# Формируем список значений модулированного сигнала
ASK = []
for x in xrange(0, N):
	ASK += [source_sequence[x] * math.sin(Wc * t) for t in arange(0, duration, (1.0 / Fd))]



#################  Демодулятор  #####################
# Выпрямитель, что бы среднее значение сигнала за длительность одного импульса отличалась от 0
rectified_ASK = []
for x in xrange(len(ASK)):
	rectified_ASK += [abs(ASK[x])] 



# Детектор
receive_sequence = []
temp = 0
# Считаем среднеарифметическое значение сигнала за время длительности одного импульса
# Если значение больше 0 - приняли 1
# РАБОТАЕТ ТОЛЬКО В ИДЕАЛЬНОМ СЛУЧАЕ
for x in xrange(0, N):

	for y in xrange(x*20, (x+1)*20):
		temp += rectified_ASK[y]

	if temp / (duration * Fd) > 0:
		receive_sequence += [1]
	else:
		receive_sequence += [0]

	temp = 0

print "Исходная последовательность  ",source_sequence
print "Полученная последовательность",receive_sequence



#################  Определение функции построения графиков  #####################

def plot_signal(x, y, title, labelx, labley, position):
	pylab.subplot(4, 1, position)
	pylab.plot(x, y)
	pylab.title(title)
	pylab.xlabel(labelx)
	pylab.ylabel(labley)
	pylab.grid(True)


plot_signal(arange(0, time_signal, (1.0 / Fdd)), source_signal, 'Digital sequence', 'time', '', 1)
plot_signal(arange(0, time_signal, (1.0 / Fd)), ASK, 'ASK', 'time', '', 2)
plot_signal(arange(0, time_signal, (1.0 / Fd)), rectified_ASK, 'rectified_ASK', 'time', '', 3)
# Отображение графиков
pylab.show()
