Radiotech_part2
===============

Репозиторий второго семестра курса радиотехники.

Задание
-------
Текст задания находится в репозитории [Radiotech_book], pdf доступен по [ссылке]
[Radiotech_book]:https://github.com/dep403mai/Radiotech_book
[ссылке]:https://github.com/dep403mai/Radiotech_book/raw/master/Radiotech.pdf

Общие сведения
--------------

В корне репозитория находится пример выполнения задания. Построенна приемо-передающая система, использующая амплитудную манипуляцию и алгоритм Хемминга(7,4,3)

В файле `example.py` находится класс главного окна программы с логикой работы приложения

В файле `Sender.py` находится класс, который позволяет имитировать фунции передатчика (генератор, кодер, модулятор)

В файле `Receiver.py` находится класс, который позволяет имитировать фунции приемника (демодулятор, декодер)

В файле `Plot.py` находится функция для построений графиков

Приложение осуществляет вывод информации в консоль и лог-файл `log.txt`, который создается в корне папки с программой

Запуск и сборка
---------------

```python ./example.py```

Для генерирования класса с формой из файл описания запустить скрипт `BuldForm.sh (.bat)`

`./BuldForm.sh`

Скриншоты
----------

Пример работы программы

![alt-текст](https://github.com/dep403mai/Radiotech_part2/blob/master/ScreenshotMainWindow.png "Пример работы программы")

Пример построения графиков

![alt-текст](https://github.com/dep403mai/Radiotech_part2/blob/master/ScreenshotPlot.png "Пример построения графиков")

Пример вывода в консоль

![alt-текст](https://github.com/dep403mai/Radiotech_part2/blob/master/ScreenshotConsole.png "Пример вывода в консоль")

Пример документации
------------------
Исходные и [скомпилированные] файлы документации находятся в каталоге `doc`.
[скомпилированные]:https://github.com/dep403mai/Radiotech_part2/raw/master/doc/Documentation.pdf

Порядок работы с репозиторием
------------------------------
- Необходимо создать форк репозитория, затем клонируйте репозиторий к себе на рабочую машину. Все необходимые инструкции можно найти [здесь]
[здесь]:https://help.github.com/articles/fork-a-repo
- Все изменения производить в вашей (форкнутой) версии репозитория
- В процессе работы над вашим проектом, нужно будет делать локальные коммиты в Git, затем делать push изменений в ваш форк на GitHub. (Существуют много методик коммитов, старайтесь коммитить законченные куски кода)
- После внесения необходимых изменений, нужно отправить pull-request в [центральный репозиторий]
[центральный репозиторий]:https://github.com/dep403mai/Radiotech_part2
- Преподаватели будут проводить code-review перед тем, как слить (мержить) ваш код в центральный репозиторий
- Если после отправки pull-request вы внесли новые изменения в код, отправлять новый pull-request не нужно, все изменения автоматически попадут в прошлый запрос. 
- Если будут замечания к вашему коду, вы также можете просто добавлять коммиты в свою ветку master, и пулл-реквест будет автоматически обновляться.
- Ваш код должен быть помещен в папку `/номер_группы/номер_варианта/`. Вся документация должна храниться в папке `/номер_группы/номер_варианта/doc/`

Литература и ссылки
-------------------
- [Работа с Git репозиториями]
[Работа с Git репозиториями]:http://dev.call2ru.com/vs/%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%81%20Git.pdf
- [Шпаргалки. Работа с github]
[Шпаргалки. Работа с github]:http://iklmn.net/blog/shpargalki-rabota-s-github.html
- [Эндрю Хант, Дэвид Томас. Программист-прагматик. Путь от подмастерья к мастеру]
[Эндрю Хант, Дэвид Томас. Программист-прагматик. Путь от подмастерья к мастеру]:http://www.ozon.ru/context/detail/id/1657382/
- [PEP8]
[PEP8]:https://docs.google.com/file/d/0B7cDWj1-Z0r0MmYwZjJhZWEtMjk1Zi00NWE5LWEzNTQtOTFjNjcwYjdhMGRl/edit?ddrp=1&pli=1&hl=ru
- [А.В.Столяров. Оформление программного кода. Методическое пособие]
[А.В.Столяров. Оформление программного кода. Методическое пособие]:http://www.stolyarov.info/books/codestyle
- [Сверстай диплом красиво: LaTeX за три дня]
[Сверстай диплом красиво: LaTeX за три дня]:http://www.stolyarov.info/books/latex3days
- [A Byte of Python (Russian)]
[A Byte of Python (Russian)]:http://wombat.org.ua/AByteOfPython/AByteofPythonRussian-2.01.pdf
- [Введениев среду PyQt4]
[Введениев среду PyQt4]:http://wiki.python.su/%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%D0%92%D0%A1%D1%80%D0%B5%D0%B4%D1%83PyQt4
- [PyQt Class Reference]
[PyQt Class Reference]:http://pyqt.sourceforge.net/Docs/PyQt4/classes.html
- [PyQt: unpythonic GUI]
[PyQt: unpythonic GUI]:http://pyobject.ru/blog/2008/05/07/pyqt-unpythonic-gui/
