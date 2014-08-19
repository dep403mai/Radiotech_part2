# -*- coding:utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

from Sender import *
from Receiver import *

from Plot import *
from Form import *
class MainWindowClass(QtGui.QMainWindow):
    """Класс главного окна программы. 
    Наследуется от QMainWindow, содержит в себе класс 
    интерфейса Ui_MainWindow. Класс Ui_MainWindow сгенерирован
    при помощи команды <pyuic4> из файла form.ui. Описание формы form.ui
    сгенерировано через Designer, идущего в составе PyQt4

    """
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Сигналы и слоты
        self.connect(self.ui.CONDUCT_EXPERIMENT, QtCore.SIGNAL('clicked()'),self.conduct_experiment) # Проведение эксперимента
        self.connect(self.ui.PLOT_GRAPH, QtCore.SIGNAL('clicked()'),self.plot_graph)                 # Построение графиков

        # Дескриптор файла, в котором храниться лог
        self.file = open("log.txt", 'w')

    def __del__(self):
    	self.file.close()
    
    def conduct_experiment(self):
        """Провести эксперимент по имитации приемо-передачи. 
        Эксперимент проводится count раз, затем вычисляется
        мат.ожидание и дисперсия битовой ошибки

        """
        self.file.write("\n\n============ New imitation ===========")
        print "\n\n============ New imitation ==========="
        
        # Входные данные
        # Проводим инициализацию открытых атрибутов-данных класса данными из формы
        # Все данные из формы в формате Qstring переводим в питоновский string, а затем в float
        self.FD = int(str(self.ui.FD.text()))                   # Частота дискретизации аналогового несущего сигнала         
        self.FDD = int(str(self.ui.FDD.text()))                 # Частота дискретизации цифрового исходного сигнала         
        self.FC = int(str(self.ui.FC.text()))                   # Частота несущей                   
        self.N = int(str(self.ui.N.text()))                     # Количество передающихся символов                   
        self.SPEED = float(str(self.ui.SPEED.text()))           # Символьная скорость (частота символов)
        self.duration = 1 / self.SPEED                          # Длительность импульса
        self.time_signal = self.N * self.duration               # Длительность исходного сигнала из <N импульсов
        self.A_NOISE = float(str(self.ui.A_NOISE.text()))       # Амплитуда шума                   
        self.A_SIGNAL = float(str(self.ui.A_SIGNAL.text()))     # Амплитуда сигнала                   
        self.DETECTION_THRESHOLD = float(str(self.ui.DETECTION_THRESHOLD.value())) # Порог детектирования   
        
        # Локальные переменные
        count = self.ui.EXPER_COUNT.value()     # Необходимое количество экспериментов
        bit_error = []                          # В списке храниться апостериорной вероятность битовой ошибки при каждом эксперименте

        # Проводим эксперимент <count> раз и вичисляем апостериорной вероятность битовой ошибки при каждом эксперименте
        for x in xrange(count):
            self.file.write("\n\nExperiment #" + str(x))
            print "\nExperiment #", x
            
            # Конструируем объекты приемника и передатчика
            self.sender_obj = Sender(self.FD,
                                self.FDD,
                                self.FC,
                                self.N,
                                self.SPEED,
                                self.A_NOISE,
                                self.A_SIGNAL)

            self.receiver_obj = Receiver(self.FD,
                                    self.N,
                                    self.SPEED,
                                    self.DETECTION_THRESHOLD,
                                    self.file)
            # Имитируем передатчик
            self.sender_obj.generate_signal()
            self.sender_obj.encode_signal()
            self.sender_obj.genetare_noise()
            self.sender_obj.modulate_signal()

            # Имитируем приемник
            self.receiver_obj.demodulate_signal(self.sender_obj.noise_ASK)
            self.receiver_obj.decode_signal()

            # Сравниваем декодированную последовательность и исходную.
            # Считаем количество ошибочных битов
            error = 0.0 # Количество ошибочных битов
            for x in xrange(len(self.receiver_obj.decode_code)):
                if self.receiver_obj.decode_code[x] != self.sender_obj.source_sequence[x]:
                    error += 1
            
            print "Decode sequence: ", self.receiver_obj.decode_code
            self.file.write("\nDecode sequence: " + str(self.receiver_obj.decode_code))
            print "Source sequence: ", self.sender_obj.source_sequence
            self.file.write("\nSource sequence: " + str(self.sender_obj.source_sequence))

            # Вычисление апостериорной вероятности появления битовой ошибки в эксперименте.
            # Вычисляется как отношение количества ошибочных битов к длине последовательности.
            # Вычисленная вероятноть заноситься в список <bit_error> при каждом эксперименте 
            # для формирования выборки
            if error != 0:
                bit_error.append(error/len(self.receiver_obj.decode_code))
                print "Sequences are not matched"
                self.file.write("\nSequences are not matched")
            else:
                bit_error.append(0)

        # Вычисление мат. ожидания вероятности появления битовой ошибки
        # Считаем как среднеарифметическое значение
        expected_value = 0.0    # Мат.ожидание
        for x in xrange(count):
            expected_value += bit_error[x]
        expected_value /= float(count)

        self.ui.EXPECTED_VALUE.setText(str(expected_value))
        self.file.write("\n\nExpected value: " + str(expected_value))
        print "\nExpected value: ", expected_value

        # Вычисление дисперсии вероятности появления битовой ошибки
        # Дисперсия вычисляется по формуле: (sum(Xi^2) - sum(Xi)^2 / n) / n - 1
        sum_of_squares = 0.0 
        for x in xrange(count):
            sum_of_squares += bit_error[x] ** 2

        square_of_the_sum = 0.0
        for x in xrange(count):
            square_of_the_sum += bit_error[x]
        square_of_the_sum *= square_of_the_sum

        dispersion = (sum_of_squares - square_of_the_sum / count) / (count - 1)

        self.ui.DISPERSION.setText(str(dispersion))
        self.file.write("\nDispersion:     " + str(dispersion))
        print "Dispersion: ", dispersion
    
    def plot_graph(self):
        """Построить графики

        """
        # plot_signal(x, y, title, (list)labelx, (list)labley, position)
        plot_signal(arange(0, self.time_signal, (1.0 / self.FDD)), self.sender_obj.source_signal, 'Random source sequence', 'time', '', 1)
        plot_signal(arange(0, len(self.sender_obj.encoded_signal) * self.duration, (1.0 / self.FD)), self.sender_obj.noise_ASK, 'Noised ASK', 'time', '', 3)
        plot_signal(arange(0, len(self.receiver_obj.receive_sequence) * self.duration, (1.0 / self.FD)), self.receiver_obj.rectified_ASK, 'Rectified ASK', 'time', '', 5)

        # Для того, что бы отобразить декодированную последователоность символов, представим их в виде импульсов
        # длительности <duration>
        decode_signal = []
        for x in range(0, len(self.receiver_obj.decode_code)):
            decode_signal += [self.receiver_obj.decode_code[x] for y in arange(0, self.duration, (1.0 / self.FDD))]

        plot_signal(arange(0, len(self.receiver_obj.decode_code) * self.duration, (1.0 / self.FDD)), decode_signal, 'Decode sequence', 'time', '', 7)

        # Отображение графиков
        pylab.show()

app = QtGui.QApplication(sys.argv) # Cоздать основной объект приложения
windows = MainWindowClass()        # Создать объект класса MainWindowClass()
windows.show()                     # Показать главное окно приложения
sys.exit(app.exec_())