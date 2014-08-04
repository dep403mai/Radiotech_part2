# -*- coding:utf-8 -*-

import pylab  # Для графиков
from numpy import * 

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

###########################   Кодер   ###########################

# Для хранения разрядов числа в списке используется прямой порядок 
# (litle-endian order), т.е. A0,A1,A2,A3, в отличии от записи числа 
# арабскими цифрами (big-endian), т.е A3,A2,A1,A0.
def coder_hamming(code):
    """Кодирование по алгоритму Хемминга(7,4,3), aX - информационные
    символы, cX - проверочные символы

    Принимаемые параметры:
    code - список из 4 элементов (блок символов)

    Возвращаемые параметры:
    encoded_sequence - закодированная последовательность,
    список из 7 элементов

    """
    encoded_sequence = [((code[0] + code[1]) % 2 + code[3]) % 2,  # c0
                        ((code[0] + code[2]) % 2 + code[3]) % 2,  # c1
                        code[0],  # a0
                        ((code[1] + code[2]) % 2 + code[3]) % 2,  # c2
                        code[1],  # a1
                        code[2],  # a2
                        code[3]]  # а3
    return encoded_sequence

###########################    Декодер   ###########################
def decoder_hamming(count, code):
    """Декодирование по алгоритму Хемминга(7,4,3)

    Принимаемые параметры:
    count -  номер текущего блока для декодирования
    code - список из 7 элементов (блок символов)

    Возвращаемые параметры:
    encoded_sequence - декодированная последовательность
    из 4 элементов

    """
    # Генерируем контрольные символы
    c0 = ((code[2] + code[4]) % 2 + code[6]) % 2
    c1 = ((code[2] + code[5]) % 2 + code[6]) % 2
    c2 = ((code[4] + code[5]) % 2 + code[6]) % 2

    # Для определения позиции искаженного символа суммируем веса искаженных проверочных символов
    w1 = w2 = w3 = 0

    # Проверяем контрольные символы
    if c0 != code[0] or c1 != code[1] or c2 != code[3]:
        if c0 != code[0]:
            w1 = 1
        if c1 != code[1]:
            w2 = 2
        if c2 != code[3]:
            w3 = 4

        # Код Хемминга(7,4,3) может сам исправлять ошибки
        # первой кратности, т.к. кодовое расстояние такого кода d=3
        # При ошибках большей кратности последовательность восстановленна
        # не будет, нужно применять дополнительные меры для обеспечения 
        # помехоустойчивости 
        # 
        # Нумерация элементов в списке начинается с 0, вычитаем 1
        syndrome = w1 + w2 + w3 - 1
        print "Block", count, ": Error in", syndrome, "bit"

        # Заменяем ошибочный символ на противоположный
        code[syndrome] ^= code[syndrome]

    return [code[2], code[4], code[5], code[6]]


##########################################################
#
#          Входные данные
#
##########################################################

FD = 200.0                  # Частота дискретизации аналогового несущего сигнала
FDD = 500.0                 # Частота дискретизации цифрового исходного сигнала
FC = 10.0                   # Частота несущей
N = 32                      # Количество передающихся символов
SPEED = 10.0                # Символьная скорость (частота символов)
duration = 1 / SPEED        # Длительность импульса
time_signal = N * duration  # Длительность исходного сигнала из N импульсов
Wc = 2 * math.pi * FC       # Угловая частота несущей
A_NOISE = 1                 # Амплитуда шума
A_SIGNAL = 1.25             # Амплитуда сигнала
DETECTION_THRESHOLD = 0.3   # Порог детектирования
HAMMING_LENGTH = 7          # Длина последовательности после кодирования по Хеммингу(7,4,3)


##########################################################
#
#          Генерирование исходной последовательности
#
##########################################################

# Формируем исходную последовательность символов
source_sequence = [random.randint(0, 2) for x in range(0, N)]

# Формируем список значений исходного сигнала
source_signal = []
for x in range(0, N):
    source_signal += [source_sequence[x] for y in arange(0, duration, (1.0 / FDD))]


##########################################################
#
#          Кодирование
#
##########################################################
# Хемминг(7,4,3)
# Исходную последовательность символов надо разбить на блоки по 4 разряда, 
# если разрядов не хватает, то нужно дополнить последовательность 1-ми

# Проверяем длину последовательности и дополняем единицами если необходимо
if len(source_sequence) % 4 != 0:
    for x in xrange(len(source_sequence) - 4 * (len(source_sequence) / 4)):
        source_sequence += [1]

# Кодируем
code_signal = []
for x in xrange(len(source_sequence) / 4):
    # На вход функции передаем блоки по 4 символа
    code_signal += coder_hamming(source_sequence[(x * 4): ((x + 1) * 4)])


##########################################################
#
#          Модулятор
#
##########################################################
# Формируем список значений модулированного сигнала
ASK = []
for x in xrange(0, len(code_signal)):
    ASK += [A_SIGNAL * code_signal[x] * math.sin(Wc * t) for t in arange(0, duration, (1.0 / FD))]

# Формируем шум
noise = []
for x in xrange(0, len(code_signal)):
    noise += [A_NOISE * random.uniform(-1.0, 1.0) for x in arange(0, duration, (1.0 / FD))]

# Зашумляем сигнал
# Наложение шума предстовляет собой формирование списка среднеарифметических значений сигнала
# и шума в дискреты времени
noise_ASK = [(noise[x] + ASK[x]) / 2 for x in xrange(len(code_signal) * int(duration * FD))]


##########################################################
#
#          Демодулятор
#
##########################################################
# Выпрямитель, что бы среднее значение сигнала за длительность одного импульса отличалась от 0
rectified_ASK = []
for x in xrange(len(ASK)):
    rectified_ASK += [abs(noise_ASK[x])]

# Детектор
receive_sequence = []
temp = 0

# Считаем среднеарифметическое значение сигнала за время длительности одного импульса
for x in xrange(0, len(code_signal)):

    # Суммируем значение сигнала за время длительности одного импульса
    for y in xrange(x * len(rectified_ASK) / len(code_signal),
                    (x + 1) * len(rectified_ASK) / len(code_signal)):
        temp += rectified_ASK[y]

    # Сравниваем среднеарифметическое значение сигнала с порогом детектирования
    if (temp / (duration * FD) - DETECTION_THRESHOLD) > 0:
        receive_sequence += [1]
    else:
        receive_sequence += [0]
    temp = 0


##########################################################
#
#          Декодируем
#
##########################################################
print "Decoding......"
decode_code = []

# Разбиваем демодулированную последовательность на блоки длиной HAMMING_LENGTH и декодируем
for x in xrange(len(receive_sequence) / HAMMING_LENGTH):
    decode_code += decoder_hamming(x, receive_sequence[(x * HAMMING_LENGTH): ((x + 1) * HAMMING_LENGTH)])

print "     Done"
print "Source sequence  ", source_sequence
print "Decode code      ", decode_code


##########################################################
#
#     Сравниваем декодированную последовательность и исходную
#
##########################################################
error = 0
for x in xrange(len(decode_code)):
    if decode_code[x] != source_sequence[x]:
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
plot_signal(arange(0, time_signal, (1.0 / FDD)), source_signal, 'Digital sequence', 'time', '', 1)
plot_signal(arange(0, 56 * duration, (1.0 / FD)), noise_ASK, 'ASK', 'time', '', 3)
plot_signal(arange(0, 56 * duration, (1.0 / FD)), rectified_ASK, 'rectified_ASK', 'time', '', 5)

decode_signal = []
for x in range(0, len(decode_code)):
    decode_signal += [decode_code[x] for y in arange(0, duration, (1.0 / FDD))]

plot_signal(arange(0, len(decode_code) * duration, (1.0 / FDD)), decode_signal, 'Decode sequence', 'time', '', 7)

# Отображение графиков
pylab.show()