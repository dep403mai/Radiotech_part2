# -*- coding:utf-8 -*-

import pylab		# Для графиков
import math			# Для sin(), cos()
import random
from numpy import *	# Для функции arange(), функция поддерживает тип float для аргументов

#################   Кодер   #####################
def Coder_Hamming(source_sequence):
	code_sequence = [((source_sequence[0] + source_sequence[1]) % 2 + source_sequence[3]) % 2, 	# c0
					 ((source_sequence[0] + source_sequence[2]) % 2 + source_sequence[3]) % 2, 	# c1
					 source_sequence[0], 														# a0
					 ((source_sequence[1] + source_sequence[2]) % 2 + source_sequence[3]) % 2, 	# c2
					 source_sequence[1], 														# a1
					 source_sequence[2], 														# a2
					 source_sequence[3]]														# а3
	# Бит проверки четности
	# count = 0
	# for x in xrange(7):
	# 	if code_sequence[x] == 1:
	# 		count += 1

	# if count % 2 == 0:
	# 	code_sequence += [0]
	# else:
	# 	code_sequence += [1]

	return code_sequence

#################   Декодер   #####################
def Decoder_Hamming(code):
	c0 = ((code[2] + code[4]) % 2 + code[6]) % 2
	#print 'C0 ', c0
	c1 = ((code[2] + code[5]) % 2 + code[6]) % 2
	#print 'C1 ', c1
	c2 = ((code[4] + code[5]) % 2 + code[6]) % 2
	#print 'C2 ', c2

	# Для определения позиции искаженного символа суммируем веса искаженных проверочных символов
	w1 = w2 = w3 = 0

	if c0 != code[0] or c1 != code[1] or c2 != code[3]:
		if c0 != code[0]:
			w1 = 1
		if c1 != code[1]:
			w2 = 2
		if c2 != code[3]:
			w3 = 4

			# Нумерация элементов в списке начинается с 0, вычитаем 1
			syndrome = w1 + w2 + w3 - 1
			print 'Error in' , syndrome, 'bit'

			if code[syndrome] == 1:
				code[syndrome] = 0
			else:
				code[syndrome] = 1
	return [code[2], code[4], code[5], code[6]]

########## Входные данные ##############

Fd = 200.0 					# Частота дискретизации аналогового несущего сигнала
Fdd = 500.0 				# Частота дискретизации цифрового исходного сигнала
Fc = 10.0 					# Частота несущей
N = 30 						# Количество передающихся символов
speed = 10.0 				# Символьная скорость (частота символов)
duration = 1 / speed 		# Длительность импульса
time_signal = N * duration 	# Длительность исходного сигнала из N импульсов
Wc = 2 * math.pi * Fc  		# Угловая частота несущей

# Формируем исходную последовательность символов
source_sequence = [random.randint(0, 2) for x in range(0, N)]

# Формируем список значений исходного сигнала
source_signal = []
for x in range(0, N):
	source_signal += [source_sequence[x] for y in arange(0, duration, (1.0 / Fdd))]

#################  Сжатие  #####################

#################  Кодирование  #####################
# Хемминг 8,4,4 с дополнительным битом проверки на четность
# Надо разбить на блоки по 4 разряда, если не хватает, то дополнить 1-ми

# Дополняем еденицами, что бы можно было разделить на блоки по 4 бита
for x in xrange(len(source_sequence) - 4 * (len(source_sequence) / 4)):
	source_sequence += [1]

code_signal=[]
for x in xrange(len(source_sequence)/4):
	code_signal += Coder_Hamming(source_sequence[(x * 4): ((x + 1) * 4)])

#################  Модулятор  #####################

# Формируем список значений модулированного сигнала
ASK = []
for x in xrange(0, len(code_signal)):
	ASK += [1.25*code_signal[x] * math.sin(Wc * t) for t in arange(0, duration, (1.0 / Fd))]
# Формируем шум
noise = []
for x in xrange(0, len(code_signal)):
	noise += [random.uniform(-1.0, 1.0) for x in arange(0, duration, (1.0 / Fd))]

# Зашумляем сигнал
noise_ASK = [(noise[x] + ASK[x])/2 for x in xrange(len(code_signal) * int(duration * Fd))]





#################  Демодулятор  #####################
# Выпрямитель, что бы среднее значение сигнала за длительность одного импульса отличалась от 0
rectified_ASK = []
for x in xrange(len(ASK)):
	rectified_ASK += [abs(noise_ASK[x])] 

# Детектор
receive_sequence = []
temp = 0
# Считаем среднеарифметическое значение сигнала за время длительности одного импульса
# Если значение больше 0 - приняли 1
# РАБОТАЕТ ТОЛЬКО В ИДЕАЛЬНОМ СЛУЧАЕ
for x in xrange(0, len(code_signal)):

	for y in xrange(x*20, (x+1)*20):
		temp += rectified_ASK[y]

	if (temp / (duration * Fd) - 0.3) > 0: # 0,35 - порог детектирования
		receive_sequence += [1]
	else:
		receive_sequence += [0]
	temp = 0

#################  Декодируем  #####################
print "Decoding......"
decode_code = []
for x in xrange(len(receive_sequence)/7):
	decode_code += Decoder_Hamming(receive_sequence[(x * 7): ((x + 1) * 7)])
print " 	Done"
print "Source sequence  ", source_sequence
print "Decode code      ", decode_code

error = 0
for x in xrange(len(decode_code)):
	if decode_code[x] != source_sequence[x]:
		error += 1
if error != 0:
	print "\n 	Found ", error, " error(s)\n"
else:
	print "\n 	Not found any error or all errors were corrected\n"

#################  Определени е функции построения графиков  #####################

def plot_signal(x, y, title, labelx, labley, position):
	pylab.subplot(4, 1, position)
	pylab.plot(x, y)
	pylab.title(title)
	pylab.xlabel(labelx)
	pylab.ylabel(labley)
	pylab.grid(True)

plot_signal(arange(0, time_signal, (1.0 / Fdd)), source_signal, 'Digital sequence', 'time', '', 1)
plot_signal(arange(0, 56 * duration, (1.0 / Fd)), noise_ASK, 'ASK', 'time', '', 2)
plot_signal(arange(0, 56 * duration, (1.0 / Fd)), rectified_ASK, 'rectified_ASK', 'time', '', 3)
# Отображение графиков
#pylab.show()
