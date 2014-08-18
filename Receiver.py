# -*- coding:utf-8 -*-
import pylab  # Для графиков
from numpy import * 

class Receiver(object):
    """Класс имитирует приемник и реализует атрибуты-методы,
    которые существуют в реальной системе"""
    def __init__(self, FD_, N_, SPEED_, DETECTION_THRESHOLD_):
        self.HAMMING_LENGTH = 7          # Длина последовательности после кодирования по Хеммингу(7,4,3)
        self.rectified_ASK = []
        self.receive_sequence = []
        self.decode_code = []

        self.FD = FD_                  # Частота дискретизации аналогового несущего сигнала
        self.SPEED = SPEED_                # Символьная скорость (частота символов)
        self.DETECTION_THRESHOLD = DETECTION_THRESHOLD_   # Порог детектирования
        
        self.encoded_signal_length = self.HAMMING_LENGTH * N_ / 4
        self.duration = 1 / self.SPEED        # Длительность импульса
        

    ###########################    Декодер   ###########################
    def _decoder_hamming(self, count, code):
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

    def demodulate_signal(self, signal):
        for x in xrange(len(signal)):
            self.rectified_ASK += [abs(signal[x])]

        # Детектор
        
        temp = 0

        # Считаем среднеарифметическое значение сигнала за время длительности одного импульса
        for x in xrange(0, self.encoded_signal_length):

            # Суммируем значение сигнала за время длительности одного импульса
            for y in xrange(x * len(self.rectified_ASK) / self.encoded_signal_length,
                           (x + 1) * len(self.rectified_ASK) / self.encoded_signal_length):
                
                temp += self.rectified_ASK[y]
            # Сравниваем среднеарифметическое значение сигнала с порогом детектирования
            if (temp / (self.duration * self.FD) - self.DETECTION_THRESHOLD) > 0:
                self.receive_sequence += [1]
            else:
                self.receive_sequence += [0]
            temp = 0

    def decode_signal(self):
        for x in xrange(len(self.receive_sequence) / self.HAMMING_LENGTH):
            self.decode_code += self._decoder_hamming(x, self.receive_sequence[(x * self.HAMMING_LENGTH): ((x + 1) * self.HAMMING_LENGTH)])

