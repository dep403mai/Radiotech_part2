# -*- coding:utf-8 -*-

import pylab  # Для графиков
from numpy import * 
from Sender import *
from Receiver import *

# ################  Определение функции построения графиков  #####################

def plot_signal(x, y, title, labelx, labley, position):
    """Построение графика сигнала

    Принимаемые параметры:
    x - список значений аргументов
    y - список значений функции (Внимание: len(x) == len(y))
    title - название графика
    labelx - подпись оси X
    labley - подпись оси Y
    position - позиция графика в поле окна. Что бы графики не накладывались
    друг на друга, оставляется между графиками простанство, передвая в качестве
    аргумента <position> нечетные значения: 1, 3, 5. Измените значение константы
    TOTAL_QUANTITY, которая отвечает за максимальное количество графиков:
    (TOTAL_QUANTITY >= <position>)

    """
    TOTAL_QUANTITY = 7
    pylab.subplot(TOTAL_QUANTITY, 1, position)
    pylab.plot(x, y)
    pylab.title(title)
    pylab.xlabel(labelx)
    pylab.ylabel(labley)
    pylab.grid(True)

##########################################################
#
#          Передатчик
#
##########################################################
sender_obj = Sender()

sender_obj.generate_signal()
sender_obj.encode_signal()
sender_obj.genetare_noise()
sender_obj.modulate_signal()
noise_ASK = sender_obj.noise_ASK
code_signal = sender_obj.encoded_signal

##########################################################
#
#          Приемник
#
##########################################################
receiver_obj = Receiver(len(code_signal))
receiver_obj.demodulate_signal(noise_ASK)
receiver_obj.decode_signal()


print "     Done"
print "Source sequence  ", sender_obj.source_sequence
print "Decode code      ", receiver_obj.decode_code


##########################################################
#
#     Сравниваем декодированную последовательность и исходную
#
##########################################################
error = 0
for x in xrange(len(receiver_obj.decode_code)):
    if receiver_obj.decode_code[x] != sender_obj.source_sequence[x]:
        error += 1
if error != 0:
    print "\n   Found ", error, " error(s)\n"
else:
    print "\n   Not found any error or all errors were corrected\n"


##########################################################
#
#    Построение графиков
#
##########################################################
# plot_signal(arange(0, time_signal, (1.0 / FDD)), source_signal, 'Digital sequence', 'time', '', 1)
# plot_signal(arange(0, len(code_signal) * duration, (1.0 / FD)), noise_ASK, 'ASK', 'time', '', 3)
# plot_signal(arange(0, len(receive_sequence) * duration, (1.0 / FD)), rectified_ASK, 'rectified_ASK', 'time', '', 5)

# decode_signal = []
# for x in range(0, len(decode_code)):
#     decode_signal += [decode_code[x] for y in arange(0, duration, (1.0 / FDD))]

# plot_signal(arange(0, len(decode_code) * duration, (1.0 / FDD)), decode_signal, 'Decode sequence', 'time', '', 7)

# # Отображение графиков
# pylab.show()