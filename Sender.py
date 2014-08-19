# -*- coding:utf-8 -*-
import random
from numpy import *


class Sender(object):
    """Класс имитирует передатчик и реализует атрибуты-методы,
    которые существуют в реальной системе

    """

    def __init__(self, FD_, FDD_, FC_, N_, SPEED_, A_NOISE_, A_SIGNAL_):

        # Открытые атрибуты-данные
        self.source_sequence = []                   # Исходная случайная последовательности символов длинной <N>
        self.source_signal = []                     # Исходный сигнал, полученный из <source_sequence> дительностью
                                                    # <time_signal>
        self.encoded_signal = []                    # Закодированная по алгоритму Хемминг(7,4,3) последовательность
        self.noise = []                             # Шумовой сигнал
        self.ASK = []                               # Амплитудно-манипулированный сигнал
        self.noise_ASK = []                         # Зашумленный АМ сигнал (имитация передачи)

        # Инициализация
        self.FD = FD_                               # Частота дискретизации аналогового несущего сигнала
        self.FDD = FDD_                             # Частота дискретизации цифрового исходного сигнала
        self.FC = FC_                               # Частота несущей
        self.N = N_                                 # Количество передающихся символов
        self.SPEED = SPEED_                         # Символьная скорость (частота символов)
        self.duration = 1 / self.SPEED              # Длительность импульса
        self.time_signal = self.N * self.duration   # Длительность исходного сигнала из <N> импульсов
        self.Wc = 2 * math.pi * self.FC             # Угловая частота несущей
        self.A_NOISE = A_NOISE_                     # Амплитуда шума
        self.A_SIGNAL = A_SIGNAL_                   # Амплитуда сигнала

    # Для хранения разрядов числа в списке используется прямой порядок 
    # (litle-endian order), т.е. A0,A1,A2,A3, в отличии от записи числа 
    # арабскими цифрами (big-endian), т.е A3,A2,A1,A0.
    def _coder_hamming(self, code):  # ПРИВАТНЫЙ АТРИБУТ-МЕТОД
        """Кодирование по алгоритму Хемминга(7,4,3), aX - информационные
        символы, cX - проверочные символы

        Принимаемые параметры:
            code - список из 4 элементов (блок символов)

        Возвращаемые параметры:
            encoded_sequence - закодированная последовательность,
                список из 7 элементов

        """
        encoded_sequence = [((code[0] + code[1]) % 2 + code[3]) % 2,    # c0
                            ((code[0] + code[2]) % 2 + code[3]) % 2,    # c1
                              code[0],                                  # a0
                            ((code[1] + code[2]) % 2 + code[3]) % 2,    # c2
                              code[1],                                  # a1
                              code[2],                                  # a2
                              code[3]]                                  # а3
        return encoded_sequence

    def generate_signal(self):
        """Формирование случайной последовательности символов
        длинной <N> и представление кждого символа в виде импульса длительностью <duration>

        """
        # Формируем исходную случайную последовательность символов
        self.source_sequence = [random.randint(0, 2) for x in range(0, self.N)]

        # Формируем список значений исходного сигнала
        self.source_signal = []
        for x in range(0, self.N):
            self.source_signal += [self.source_sequence[x] for y in arange(0, self.duration, (1.0 / self.FDD))]

    def encode_signal(self):
        """Формирование закодированной по алгоритму Хемминг(7,4,3) последовательности

        """
        # Исходную последовательность символов надо разбить на блоки по 4 разряда, 
        # если разрядов не хватает, то нужно дополнить последовательность 1-ми

        # Проверяем длину последовательности и дополняем единицами если необходимо
        if len(self.source_sequence) % 4 != 0:
            for x in xrange(len(self.source_sequence) - 4 * (len(self.source_sequence) / 4)):
                self.source_sequence += [1]

        # Кодируем
        for x in xrange(len(self.source_sequence) / 4):
            # На вход функции передаем блоки по 4 символа
            self.encoded_signal += self._coder_hamming(self.source_sequence[(x * 4): ((x + 1) * 4)])

    def genetare_noise(self):
        """Формируем шумовой сигнал в диапазоне [-1.0, 1.0] с 
        амплитудой <A_NOISE>

        """
        for x in xrange(0, len(self.encoded_signal)):
            self.noise += [self.A_NOISE * random.uniform(-1.0, 1.0) for x in arange(0, self.duration, (1.0 / self.FD))]

    def modulate_signal(self):
        """Формируем список значений амплитудно-манипулированного сигнала
        и производим на него наложение шума

        """
        for x in xrange(0, len(self.encoded_signal)):
            self.ASK += [self.A_SIGNAL * self.encoded_signal[x] * math.sin(self.Wc * t) for t in
                         arange(0, self.duration, (1.0 / self.FD))]

        # Зашумляем сигнал
        # Наложение шума предстовляет собой формирование списка среднеарифметических значений сигнала
        # и шума в дискреты времени. Возможны другие варинаты
        self.noise_ASK = [(self.noise[x] + self.ASK[x]) / 2 for x in
                          xrange(len(self.encoded_signal) * int(self.duration * self.FD))]