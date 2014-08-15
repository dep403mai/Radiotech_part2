import pylab  # Для графиков
from numpy import * 

#################  Определение функции построения графиков  #####################

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
