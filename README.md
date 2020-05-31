# tcp-port-scanner

Версия 1

Автор: Макаров Егор, КН-202

### Описание

Сканер открытых портов TCP

### Как работать с программой

Запустите `scanner.py` с номером порта начала диапазона и номером порта конца диапазона. Если ввести номер одного порта, то программа просканирует только его

`-h`, `--help` — вызов справки

### Примеры запуска

```
>python scanner.py 0 3000
127.0.0.1:135    OPENED
127.0.0.1:445    OPENED
127.0.0.1:2869   OPENED
127.0.0.1:3000   OPENED
Scanning completed
```

```
>python scanner.py 2869
127.0.0.1:2869   OPENED
Scanning completed
```