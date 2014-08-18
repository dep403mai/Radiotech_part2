# -*- coding:utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

from Sender import *
from Receiver import *
from Plot import *
from form import *

class MainWindowClass(QtGui.QMainWindow):
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
        self.file.write("\n\n============ Новый эксперимент ===========")
        print "\n\n============ Новый эксперимент ==========="
        
        # Входные данные
        # Проводим инициализацию открытых атрибутов-данных класса данными из формы
        # Все данные из формы в формате Qstring переводим в питоновский string, а затем в float
        self.FD = 200.0                                                 
        self.FDD = 500.0                                                
        self.FC = int(str(self.ui.FC.text()))                                     
        self.N = int(str(self.ui.N.text()))                                       
        self.SPEED = float(str(self.ui.SPEED.text()))
        self.duration = 1 / self.SPEED           # Длительность импульса
        self.time_signal = self.N * self.duration          # Длительность исходного сигнала из N импульсов
        self.A_NOISE = float(str(self.ui.A_NOISE.text()))                           
        self.A_SIGNAL = float(str(self.ui.A_SIGNAL.text()))                         
        self.DETECTION_THRESHOLD = float(str(self.ui.DETECTION_THRESHOLD.value()))    
        
        # Локальные переменные
        count = self.ui.EXPER_COUNT.value()
        bit_error = []                          # В списке храниться апостериорной вероятность битовой ошибки при каждом эксперименте

        # Проводим эксперимент <count> раз и вичисляем апостериорной вероятность битовой ошибки при каждом эксперименте
        for x in xrange(count):
            self.file.write("\n\nЭксперимент #" + str(x))
            print "\nЭксперимент #", x
            
            # Конструируем объекты приемника и передатчика
            sender_obj = Sender(self.FD,
                                self.FDD,
                                self.FC,
                                self.N,
                                self.SPEED,
                                self.A_NOISE,
                                self.A_SIGNAL)

            receiver_obj = Receiver(self.FD,
                                    self.N,
                                    self.SPEED,
                                    self.DETECTION_THRESHOLD,
                                    self.file)
            # Передатчик
            sender_obj.generate_signal()
            sender_obj.encode_signal()
            sender_obj.genetare_noise()
            sender_obj.modulate_signal()
            noise_ASK = sender_obj.noise_ASK
            code_signal = sender_obj.encoded_signal

            # Приемник
            receiver_obj.demodulate_signal(noise_ASK)
            receiver_obj.decode_signal()

            # Сравниваем декодированную последовательность и исходную
            error = 0.0
            for x in xrange(len(receiver_obj.decode_code)):
                if receiver_obj.decode_code[x] != sender_obj.source_sequence[x]:
                    error += 1
            print "Decode sequence: ", receiver_obj.decode_code
            self.file.write("\nDecode sequence: " + str(receiver_obj.decode_code))
            print "Source sequence: ", sender_obj.source_sequence
            self.file.write("\nSource sequence: " + str(sender_obj.source_sequence))

            # Вычисление апостериорной вероятности появления битовой ошибки в эксперименте
            if error != 0:
                bit_error.append(error/len(receiver_obj.decode_code))
                print "Sequences are not matched"
                self.file.write("\nSequences are not matched")
            else:
                bit_error.append(0)

        # Вычисление мат. ожидания вероятности появления битовой ошибки
        expected_value = 0.0
        for x in xrange(count):
            expected_value += bit_error[x]
        expected_value /= float(count)
        self.ui.EXPECTED_VALUE.setText(str(expected_value))
        self.file.write("\n\nМат. ожидание: " + str(expected_value))

        # Вычисление дисперсии вероятности появления битовой ошибки
        temp = 0.0
        for x in xrange(count):
            temp += bit_error[x] ** 2
        dispersion = (temp - temp / count) / (count - 1)
        self.ui.DISPERSION.setText(str(dispersion))
        self.file.write("\nДисперсия:     " + str(dispersion))
    
    def plot_graph(self): # !!!ТУТ НАДО ВСЕ ПЕРЕДЕЛАТЬ!!!
        plot_signal(arange(0, time_signal, (1.0 / FDD)), source_signal, 'Digital sequence', 'time', '', 1)
        plot_signal(arange(0, len(code_signal) * duration, (1.0 / FD)), noise_ASK, 'ASK', 'time', '', 3)
        plot_signal(arange(0, len(receive_sequence) * duration, (1.0 / FD)), rectified_ASK, 'rectified_ASK', 'time', '', 5)

        decode_signal = []
        for x in range(0, len(decode_code)):
            decode_signal += [decode_code[x] for y in arange(0, duration, (1.0 / FDD))]

        plot_signal(arange(0, len(decode_code) * duration, (1.0 / FDD)), decode_signal, 'Decode sequence', 'time', '', 7)

        # Отображение графиков
        pylab.show()

    
    def test(self):
        self.ui.label_9.setText(self.FC)


app = QtGui.QApplication(sys.argv) # Cоздать основной объект приложения
windows = MainWindowClass()        # Создать объект класса MainWindowClass()
windows.show()                     # Показать главное окно приложения
sys.exit(app.exec_())