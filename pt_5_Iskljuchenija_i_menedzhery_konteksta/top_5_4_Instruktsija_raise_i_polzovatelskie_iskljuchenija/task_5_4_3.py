Подвиг
3.
Имеется
следующий
фрагмент
программы:


class LimitException(Exception):
    """Превышение лимита"""


class ServerLimitException(LimitException):
    """Превышение нагрузки на сервер"""


try:
    raise ServerLimitException('превышение серверной нагрузки')
except LimitException:
    print("LimitException")
except ServerLimitException:
    print("ServerLimitException")

Выберите
все
верные
утверждения, относящиеся
к
этой
программе.

при
выполнении
этой
программы
на
экране
будет
отображена
строка
"ServerLimitException"
после
выполнения
оператора
raise программа
перейдет
в
первый
блок except
программа
ни
при
каких
типах
исключений
не
перейдет
во
второй
блок except
при
выполнении
этой
программы
на
экране
будет
отображена
строка
"LimitException"
после
выполнения
оператора
raise программа
перейдет
во
второй
блок except
