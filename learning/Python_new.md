1. Pycharm
2. Типы данных
3. Функции + (*args, **kwargs)
4. lambda-функции
5. Декораторы
6. Исключения
7. Классы

Pipenv в pycharm:

* При создании нового проекта он автоматически добавится, как интерпретатор

* При клонировании из репозитория интерпретатор не добавляется, поэтому надо:

1. Зайти через `cmd` в папку проекта и запустить окружение `pipenv shell`

2. Далее добавить окружение, как обычно, через pycharm.


* Если надо поменять версию питона, то сначала необходимо удалить сохранение pipenv проекта в .virtualenvs