# -*- coding:utf-8 -*-

from Sender import *
from Receiver import *
from Plot import *
from form import *

from PyQt4 import QtCore, QtGui
import sys

class MainWindowClass(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.test)
        
        self.FD = 0                     # Частота дискретизации аналогового несущего сигнала
        self.FDD = 0                    # Частота дискретизации цифрового исходного сигнала
        self.FC = 0                     # Частота несущей
        self.N = 0                      # Количество передающихся символов
        self.SPEED = 0                  # Символьная скорость (частота символов)
        self.A_NOISE = 0                # Амплитуда шума
        self.A_SIGNAL = 0               # Амплитуда сигнала
        self.DETECTION_THRESHOLD = 0    # Порог детектирования
        self.HAMMING_LENGTH = 7         # Длина последовательности после кодирования по Хеммингу(7,4,3)
    
    def conduct_experiment(count):
        ##########################################################
        #
        #          Входные данные
        #
        ##########################################################
        self.FD = 200.0                                                 
        self.FDD = 500.0                                                
        self.FC = self.ui.FC.text()                                     
        self.N = self.ui.N.text()                                       
        self.SPEED = self.ui.SPEED.text()                               
        self.duration = 1 / SPEED                                       # Длительность импульса
        self.time_signal = N * duration                                 # Длительность исходного сигнала из N импульсов
        self.Wc = 2 * math.pi * FC                                      # Угловая частота несущей
        self.A_NOISE = self.ui.A_NOISE.text()                           
        self.A_SIGNAL = self.ui.A_SIGNAL.text()                         
        self.DETECTION_THRESHOLD = self.ui.DETECTION_THRESHOLD.value    
        
        self.error = []
        for x in xrange(count):
            # Конструируем объекты приемника и передатчика

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
    
    def plot():
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


app = QtGui.QApplication(sys.argv)
windows = MainWindowClass()
windows.show()
sys.exit(app.exec_())