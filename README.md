Radiotech_part2
===============

Репозиторий второго семестра курса радиотехники.

Общие сведения
--------------

В корне репозитория находится пример выполнения задания. Построенна приемо-передающая система, использующая амплитудную манипуляцию и алгоритм Хемминга(7,4,3)

В файле example.py находится класс главного окна программы с логикой работы приложения

В файле Sender.py находится класс, который позволяет имитировать фунции передатчика (генератор, кодер, модулятор)

В файле Receiver.py находится класс, который позволяет имитировать фунции приемника (демодулятор, декодер)

В файле Plot.py находится функция для построений графиков

Приложение осуществляет вывод информации в консоль и лог-файл log.txt, который создается в корне папки с программой

Запуск и сборка
---------------

```python ./example.py```

Скриншоты
----------

Пример работы программы

![alt-текст](https://github.com/dep403mai/Radiotech_part2/blob/master/ScreenshotMainWindow.png "Пример работы программы")

Пример построения графиков
![alt-текст](https://github.com/dep403mai/Radiotech_part2/blob/master/ScreenshotPlot.png "Пример построения графиков")

Пример вывода в консоль
![alt-текст](https://github.com/dep403mai/Radiotech_part2/blob/master/ScreenshotConsole.png "Пример вывода в консоль")

Порядок работы с репозиторием
------------------------------
- Необходимо создать форк репозитория, клонируйте репозиторий к себе на рабочую машину. Все необходимые инструкции можно найти [здесь]
[здесь]:https://help.github.com/articles/fork-a-repo
- Все изменения производить в вашей (форкнутой) версии репозитория
- В процессе работы над вашим проектом, нужно будет делать локальные коммиты в Git, затем делать push изменений в ваш форк на GitHub. (Существуют много методик коммитов, старайтесь коммитить законченные куски кода)
- После внесения необходимых изменений, нужно отправить pull-request в [центральный репозиторий]
[центральный репозиторий]:https://github.com/dep403mai/Radiotech_part2
- Преподаватели будут проводить code-review перед тем, как слить (мержить) ваш код в центральный репозиторий
- Если после отправки pull-request вы внесли новые изменения в код, отправлять новый pull-request не нужно, все изменения автоматически попадут в прошлый запрос. 
- Если будут замечания к вашему коду, вы также можете просто добавлять коммиты в свою ветку master, и пулл-реквест будет автоматически обновляться.
- Ваш код должен быть помещен в папку /номер_группы/номер_варианта/. Вся документация должна храниться в папке /номер_группы/номер_варианта/doc/
- 
