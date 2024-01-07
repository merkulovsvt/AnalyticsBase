## PostgreSQL

---

* **SQL** (Structured Query Language) - язык структурированных запросов.

* **Процедурное расширение SQL** - "диалект" (надбавка). PL/pgSQL в PostgreSQL, PL/SQL в Oracle.

* **База данных** (БД) - набор взаимосвязанных данных.

* **Система управления базами данных** (СУБД) - комплекс программных средств для управления данными.

* **СУБД** отвечает за: поддержку языка БД, механизмы хранения и извлечения данных, оптимизацию процессов извлечения.
  данных и тд.

* **Реляционные СУБД** - СУБД, управляющая реляционными базами данных.

* **Реляционная база данных** – это набор данных с предопределенными связями между ними.

---

* **Сущность** – например, клиенты, заказы, поставщики.

* **Таблица** – отношение.

* **Столбец** – атрибут.

* **Строка/запись** – кортеж.

* **Результирующий набор** – результат SQL-запроса.

---

* **string** в одинарных кавычках.

* Среда, где пишем код - **Query Tool**.

* Команды (операторы) по соглашению нужно прописывать с **заглавной** буквы, а названия таблиц, ... с **маленькой**.

* Для того, чтобы экранировать внутреннюю кавычку необходимо добавить перед ней ещё одну - **'something''wasd'**.

---

### Типы СУБД:

1. **Файл-серверные**: Microsoft Access.
2. **Клиент-серверные**: MySQL, PostgreSQL, Oracle, ...
3. **Встраиваемые**: SQLite.

---

### Типы SQL-запросов:

1. **DDL** (Data Definition Language) - работа с БД / таблицами.
    * `CREATE TABLE` table_name – создать таблицу.
    * `ALTER TABLE` table_name – изменить таблице.
        * `ADD COLUMN` column_name data_type.
        * `RENAME TO` new_table_name.
        * `RENAME` column_name `TO` new_column_name.
        * `ALTER COLUMN` column_name `SET DATA TYPE` data_type.
    * `DROP TABLE` table_name – удалить таблицу.
    * `TRUNCATE TABLE` table_name – удалить все данные и логи, но оставить структуру (нельзя резать таблицы, на которые
      есть
      ссылки, те внешний ключ, в других таблицах).


2. **DML** (Data Manipulation Language) - работа с данными.
    * `SELECT` – выборка данных.
    * `INSERT` – вставка новых данных.
    * `UPDATE` – обновление данных.
    * `DELETE` – удаление данных.
    * `MERGE` – слияние данных.


3. **TCL** (Transaction Control Language) - работа с транзакциями. `COMMIT`, `ROLLBACK`, `AVEPOINT`.
4. **DCL** (Data Control Language) - работа с разрешениями. `GRANT`, `REVOKE`, `DENY`.
5. **ANSI SQL-92** - единый стандарт для всех SQL языков. Благодаря ему большая часть запросов примерно одинаковая.

---

### [Основные типы данных](https://metanit.com/sql/postgresql/2.3.php)

---

### Базовые SQL-запросы

1. Создание БД:
   ```
   CREATE DATABASE db_name
       WITH ...
   ```
2. Удаление БД:
   ```
   DROP DATABASE [IF EXISTS] db_name
   ```
3. Создание таблицы (также можно создать напрямую через pgAdmin):
   ```
   CREATE TABLE table_name
   (
       data_id integer PRIMARY KEY,
       column1 varchar(128) [NOT NULL,...], ...
   )
   ```
4. Удаление таблицы:
   ```
   DROP TABLE [IF EXISTS] table_name
   ```
5. Вставка данных (n>=1) в таблицу:
   ```
   INSERT INTO table_name
   VALUES
   (data1, data2, ...),
   ```

* Также возможно запись вставки в одну строчку (n=1).  
  `INSERT INTO table_name VALUES (data1, data2, ...);`

---

### Отношение один ко многим (самое популярное)

* **Пример**: издатель - книги.

```
CREATE TABLE publisher
(
    publisher_id integer PRIMARY KEY,
    org_name varchar(128) NOT NULL,
    address text NOT NULL
);

CREATE TABLE book
(
   book_id integer PRIMARY KEY,
   title text NOT NULL,
   isbn varchar(32) NOT NULL
);
```

```
ALTER TABLE book
ADD COLUMN fk_publisher_id int FOREIGN KEY; - добавить в конец

ALTER TABLE book
ADD CONSTRAINT fk_publisher_id - добавить ограничение
FOREIGN KEY(fk_publisher_id) REFERENCES publisher(publisher_id);
```

Или можно задать зависимость при создании таблицы:

```
CREATE TABLE book
(
   book_id integer PRIMARY KEY,
   title text NOT NULL,
   isbn varchar(32) NOT NULL
   fk_publisher_id integer REFERENCES publisher(publisher_id) NOT NULL
);
```

---

### Отношение один к одному

* **Пример**: человек - паспорт.

```
CREATE TABLE person
(
    person_id int PRIMARY KEY,
    first_name varchar(64) NOT NUL,
    last_name varchar(64) NOT NULL
);

CREATE TABLE passport
(
    passport_id int PRIMARY KEY,
    serial_number int NOT NUL,
    fk_person_id int UNIQUE REFERENCES person(person_id) - UNIQUE гарантирует отсутствие дубликатов
);
```

---

### Отношение многие ко многим

* **Пример**: авторы статей - статьи.

```
CREATE TABLE book
(
    book_id int PRIMARY KEY
)

CREATE TABLE author
(
    author_id int PRIMARY KEY
)
```

```
CREATE TABLE book_author
(
    book_id int REFERENCES book(book_id),
    author_id int REFERENCES author(author_id),
    
    CONSTRAINT book_author_pkey PRIMARY KEY (book_id, author_id) - композитный ключ (состояющий из нескольких колонок) - плохо
)
```

* что **PRIMARY KEY**, что **FOREIGN KEY** являются ограничениями (**CONSTRAINT**).

---

### Базовые SELECT-запросы (выборки)

* **SELECT** работает после **FROM** и **WHERE**.

```
SELECT * - полная выборка (все колонки и все строки)
FROM table_name
```

**SELECT** получает строки из множества таблиц.

* `SELECT column1_name, column2_name, ...` - выборка из конкретных столбцов.


* `SELECT column1_name * column2_name` - выборка (столбец) из произведения элементов столбцов.

**DISTINCT** выводит только уникальные строки.

* `SELECT DISTINCT column1_name` - выводит только уникальные элементы.


* `SELECT DISTINCT column1_name, column2_name` - выводит только уникальные строки (сочетания).

**COUNT** выводит количество строк.

* `SELECT COUNT(*)` - посчитает общее количество строк.


* `SELECT COUNT(DISTINCT column1_name)` - посчитает количество уникальных строк в данном столбце.


* `SELECT column1_name || ' ' || column2_name` == `SELECT CONCAT(column1_name,' ',column2_name)` - выведет один столбец
  со значениями через пробел (объединение столбцов).

---

### Фильтрация WHERE

* Для работы с датами их необходимо заключать в одинарные кавычки `date > '1998-01-01'`.

```
SELECT *
FROM table_name
WHERE column1_name > 123 - условие
```

**WHERE** - оператор фильтрации.

* `WHERE condition1 {AND|OR} condition2`


* `WHERE column_name BETWEEN data1 and data2` - оператор предполагает включение (нестрого).


* `WHERE column_name == data1 OR column_name == data2 OR ...` == `WHERE column_name IN (data1, data2, ...)`


* `WHERE column_name NOT IN (data1, data2, ...)`


* `WHERE column_name IS [NOT] NULL`

---

### Сортировка ORDER BY

* Идёт после **FROM** или после **WHERE**.

```
SELECT *
FROM table_name
ORDER BY column1_name ASC, column2_name DESC, ...
```

**ORDER BY** - оператор сортировки вывода запроса.

* {**ASC**|**DESC**} (Ascending|Descending).
* По умолчанию стоит **ASC**, те по возрастанию.

---

### Агрегатные функции

```
SELECT MIN(column_name) - выведет минимальное из column_name
FROM table_name
```

**Агрегатные функции** вычисляют одно значение над некоторым набором строк.

* Ещё есть `MAX`, `AVG`, `SUM`, ...

---

### Оператор LIKE

**%** - placeholder (заполнитель) означающий 0, 1 и более символов.
**_** - ровно 1 любой символ.

```
SELECT column_name
FROM table_name
WHERE column_name LIKE '%a_'
```

**LIKE** - оператор, который используется для поиска строк, содержащих определённый шаблон символов.

* `LIKE 'U%'` - строки, начинающиеся с U.
* `LIKE '%U'` - строки, оканчивающиеся на U.

---

### Оператор LIMIT

* Идёт всегда последним.

```
SELECT column_name
FROM table_name
LIMIT 15 - выведет первые 15 элементов column_name
```

**LIMIT** - оператор, который выводит указанное число строк запроса.
---

### Группировка GROUP BY

* При наличии **WHERE** и **ORDER BY** стоит между ними.

*

```
SELECT column_name, COUNT(*) AS custom_name - псевдоним (кастомное название) столбца
FROM table_name
GROUP BY column_name
```

**GROUP BY** определяет то, как строки будут группироваться.

**Пример:**

```
SELECT category_id, supplier_id, AVG(unit_price) AS avg_price
FROM products
WHERE units_in_stock > 10
GROUP BY category_id, supplier_id - группировка по двум параметрам
ORDER BY category_id
LIMIT 5
```

---

### Постфильтрация HAVING

```
SELECT column1_name, MIN(column2_name)
FROM table_name
GROUP BY column1_name, column2_name, ... 
HAVING condition - постфильтрация
```

**HAVING** - оператор, который используется в паре с **GROUP BY** и является фильтром для групп.

**Пример:**

```
SELECT category_id, SUM(unit_price * units_in_stock)
FROM products
WHERE discontinued <> 1 - фильтр
GROUP BY category_id
HAVING SUM(unit_price * units_in_stock) > 5000 - постфильтр
ORDER BY SUM(unit_price * units_in_stock) DESC
```

---

### Операции на множествах

```
SELECT column11_name, column12_name - ориентируемся на эти столбцы
FROM table1_name
UNION
SELECT column21_name, column22_name - их количество должно совпадать
FROM table2_name
```

* **UNION** - объединение (удаляет дубликаты).

* **UNION ALL** - объединение (не удаляет дубликаты).


* **INTERSECT** - пересечение (удаляет дубликаты).
* **INTERSECT ALL** - пересечение (не удаляет дубликаты).


* **EXCEPT** - исключение (возвращает первую выборку без второй и удаляет дубликаты).
* **EXCEPT ALL** - **EXCEPT** + разница между количеством единых дубликатов выборок, если в первой их больше (10 в
  первой и 6 во второй, то в конечной будет 4 элемента) + не удаляет дубликаты.

**Пример:**

```
SELECT country
FROM customers
{UNION|INTERSECT|EXCEPT} [ALL]
SELECT country
FROM employees
```

---

### Соединения JOIN

* Если нет соответствия ставится NULL.

```
SELECT *
FROM table1_name
JOIN table2_name ON table1_name.column1_name = table2_name.column2_name
WHERE ...
```

* **INNER JOIN** - пересечение по ключу левой и правой таблицы.

* **LEFT (OUTER) JOIN** - из левой таблицы попадают абсолютно все записи (совместно с правой и без неё).

* **RIGHT (OUTER) JOIN** - из правой таблицы попадают абсолютно все записи (совместно с левой и без неё).

* **FULL (OUTER) JOIN** - объединение по ключу левой и правой таблицы (объединение LEFT JOIN и RIGHT JOIN).

* **CROSS JOIN** (декартово произведение) - каждому элементу из правой соответствует каждый из левой (NxM).

* **NATURAL JOIN** - INNER JOIN, но соединение происходит по всем столбцам с одинаковым названием.

* **SELF JOIN** (рекурсивный) - присоединить таблицу к самой себе (модель, не является отдельным оператором).

---

### INNER JOIN

* **INNER JOIN** == **JOIN**

**Пример:**

```
SELECT product_name, suppliers.company_name, units_in_stock
FROM products
INNER JOIN suppliers ON products.supplier_id = suppliers.supplier_id
```

---

### OUTER JOINS

* Если всем ключам есть соответствие, то **LEFT JOIN** == **INNER JOIN**.

**Пример:**

```
SELECT company_name, product_name
FROM suppliers
{LEFT|RIGHT|FULL} [OUTER] JOIN products ON suppliers.supplier_id = products.supplier_id
```

---

### CROSS JOIN

* При **CROSS JOIN** часть с **ON** опускается

```
SELECT column_name
FROM table1_name
CROSS JOIN table2_name
```

---

### NATURAL JOIN

* При **NATURAL JOIN** часть с **ON** опускается

```
SELECT column_name
FROM table1_name
NATURAL JOIN table2_name
```

* **Лучше не использовать**, а вместо этого прописывать все связи в ручную, чтобы избегать ошибок.

### SELF JOIN

* Чаще всего нужен для того, чтобы построить иерархию

**Пример:**

```
CREATE TABLE employee (
employee_id int PRIMARY KEY,
first_name varchar(256) NOT NULL,
last_name varchar(256) NOT NULL,
manager_id int,
FOREIGN KEY (manager_id) REFERENCES employee(employee_id); - указатель на то, что SELF JOIN возможен
);
```

```
INSERT INTO employee
(employee_id, first_name, last_name, manager_id)
VALUES
(1, 'Windy', 'Hays', NULL),
(2, 'Ava', 'Christensen', 1),
(3, 'Anna', 'Reeves', 2),
```

```
SELECT e.first_name || ' ' || e.last_name AS employee,
m.first_name || ' ' || m.last_name AS manager
FROM employee e
LEFT JOIN employee m ON m.employee_id = e.manager_id
ORDER BY manager;
```

Выведет слева ФИ сотрудника, а справа ФИ его менеджера.

---

### Оператор USING

```
SELECT column_name
FROM table1_name
JOIN table2_name ON table1_name.column_name = table2_name.column_name
```

Или можно написать **так**:

```
SELECT column_name
FROM table1_name
JOIN table2_name USING(column_name)
```

Те внутри ключевого слова **USING** мы пишем название столбца, по которому производим соединение. Он должен одинаково
называться в обеих таблицах.

---

### Псевдонимы Alias

* Псевдонимы используются для присвоения таблице или столбцу временного имени.

```
SELECT column1_name [AS] new_col1, COUNT(DISTINCT column2_name) [AS] new_col2
FROM table1_name [AS] new_tb1
JOIN table2_name [AS] new_tb2 ON new_tb1.id = new_tb2.id
```

Работа в **SELECT**:

* Нельзя использовать в **WHERE** и **HAVING** (работают до **SELECT**).

* Можно использовать в **GROUP BY** и **ORDER BY** (работают после **SELECT**) и при использовании **подзапросов**.

---

### Подзапросы

**Зачем они нужны?**

* Запросы бывают логически сложными.
* Реализовать запрос в лоб может быть сложно => подзапросы могут помочь.
* Есть задачи, которые без подзапросов не решить.

Выведем все компании, которые находятся там же, где и клиенты:

```
SELECT company_name
FROM suppliers
WHERE country IS IN (SELECT DISTINCT country FROM customers) - это подзапрос
	             
```

Можно заменить **JOIN**ом:

```
SELECT company_name
FROM suppliers
JOIN customers USING(country)
```

НО так работает не всегда. Проще говоря надо смотреть по ситуации - когда-то удобнее **JOIN**, когда-то **подзапрос**.

---

### Оператор EXISTS

**WHERE EXISTS** с подзапросом внутри возвращает **true**, если в подзапросе была возвращена хотя бы одна строка.

```
SELECT company_name, contact_name
FROM costumers
WHERE [NOT] EXISTS (SELECT customer_id FROM orders
              WHERE customer_id = customers.customer_id 
              AND freight BETWEEN 50 AND 100)
```

---

### Операторы ANY | ALL

* Операторы **ANY** и **ALL** используются с фильтрациями **WHERE** и **HAVING**.

* Оператор **ANY** возвращает **true**, если какое-либо из значений подзапроса соответствует условию.

* Оператор **ALL** возвращает **true**, если все значения подзапроса удовлетворяют условию.

```
SELECT DISTINCT company_name
FROM customers
WHERE customer_id = ANY(
   SELECT customer_id
   FROM orders
   JOIN order_details USING(order_id)
   WHERE quantity > 40
   )
```

```
SELECT DISTINCT product_name
FROM products
JOIN order_details USING(product_id)
WHERE quantity > ALL(SELECT AVG(quantity)
   FROM order_details
   GROUP BY product_id
   )
```

---

### DDL (Data Definition Language)

* `CREATE TABLE` table_name – создать таблицу.
* `ALTER TABLE` table_name – изменить таблице.
* `ADD COLUMN` column_name data_type.
* `RENAME TO` new_table_name.
* `RENAME` column_name `TO` new_column_name.
* `ALTER COLUMN` column_name `SET DATA TYPE` data_type.
* `DROP TABLE` table_name – удалить таблицу.
* `TRUNCATE TABLE` table_name – удалить все данные и логи, но оставить структуру (нельзя резать таблицы, на которые есть
  ссылки, те внешний ключ, в других таблицах).

**DDL** (язык описания данных) отвечает за работу с **БД** | **таблицами**.

* Создание таблицы:

```
CREATE TABLE student(
student_id serial NOT NULL,
first_name varchar(128),
last_name varchar(128)
);
```

* Добавление колонки в таблицу:

```
ALTER TABLE student
ADD COLUMN middle_name varchar(128);
```

* Переименовывание таблицы:

```
ALTER TABLE student
RENAME TO student_data;
```

* Переименовывание колонки:

```
ALTER TABLE student_data
RENAME last_name TO new_last_name;
```

* Удаление колонки:

```
ALTER TABLE student_data
DROP COLUMN new_last_name,
DROP COLUMN middle_name;
```

* Изменение типа данных колонки:

```
ALTER TABLE student_data
ALTER COLUMN first_name 
SET DATA TYPE varchar(64);
```

* Удаление таблицы:

```
DROP TABLE student_data;
```

---

### Тип данных serial

* Он представляет автоинкрементирующееся числовое значение.
* Значение данного типа образуется путем автоинкремента значения предыдущей строки (**+1**).
* Поэтому, как правило, данный тип используется для определения **id** строки.

**Автоинкремент** — это функция, которая автоматически генерирует уникальный номер для каждой новой строки, добавленной
в таблицу.

Посмотрим, как работает serial на примере ранее созданной таблицы **student_data**:

* Присвоит **Anna** `student_id = 1` и **Alla** `student_id = 2` автоматически.

```
INSERT INTO student_data (first_name) 
VALUES
('Anna'),
('Alla');
```

* Присвоит **Anna** `student_id = 3` и **Alla** `student_id = 4`.

```
TRUNCATE TABLE student_data; - удаление данных и логов таблицы, но не её структуры.

INSERT INTO student_data (first_name) 
VALUES
('Anna'),
('Alla');
``` 

Так выходит потому что у **TRUNCATE** по умолчанию стоит **CONTINUE IDENTITY** (не сбрасывает нумерацию **id**).

* Для сброса необходимо добавить **RESTART IDENTITY** - `TRUNCATE TABLE student_data RESTART IDENTITY;`.

---

### Ограничение CONSTRAINT

* **CONSTRAINT** используются для (указания правил) ограничения типа данных, которые могут быть помещены в таблицу. Это
  обеспечивает точность и достоверность данных в таблице.

* Если существует какое-либо нарушение между ограничением и действием данных, действие
  прерывается.

* Ограничения могут быть на уровне столбцов и таблиц.

В SQL обычно используются следующие ограничения:

* `NOT NULL` - гарантирует, что столбец не может иметь нулевое значение.
* `UNIQUE` - гарантирует, что все значения в столбце будут разными.
* `PRIMARY KEY` - комбинация NOT NULL и UNIQUE. Уникально идентифицирует каждую строку в таблице.
* `FOREIGN KEY` - однозначно идентифицирует строку/запись в другой таблице.
* `CHECK` - гарантирует, что все значения в столбце удовлетворяют определенному условию.
* `DEFAULT` - задает значение по умолчанию для столбца, если значение не указано.
* `INDEX` - используется для быстрого создания и извлечения данных из базы данных.

Задать ограничение можно при создании и изменении таблицы.

* Способ вывести все ограничения по столбцу `chair_id`:

```
SELECT constraint_name
FROM information_schema.key_column_usage
WHERE table_name = 'chair'
AND table_schema = 'public'
AND column_name = 'chair_id';
```

* Способ удалить ограничение:

```
ALTER TABLE chair
DROP CONSTRAINT chair_chair_id_key - название ограничения.
```

---

### PRIMARY KEY

* Уникально идентифицирует каждую строку в таблице.

В таблице **PK** может быть только один столбец или комбинация столбцов (**композитный ключ**) - **плохо**, в отличие от
**UNIQUE NOT NULL**.

* Задание **PK** при создании:

```
CREATE TABLE chair
(
chair_id serial [CONSTRAINT PK_char_chair_id] PRIMARY KEY, - название ограничения задано автоматически 'chair_chair_id_key'
chair_name varchar
);
```

```
CREATE TABLE chair
(
chair_id serial,
chair_name varchar,

CONSTRAINT PK_char_chair_id PRIMARY KEY(chair_id) - мы сами задали название ограничения 'PK_char_chair_id'
);
```

* Задание **PK** при изменении:

```
ALTER TABLE chair
ADD PRIMARY KEY(chair_id);
```

```
ALTER TABLE chair
ADD CONSTRAINT PK_char_chair_id PRIMARY KEY(chair_id)
```

---

### FOREIGN KEY

* Используется для связи между таблицами.

* Внешний ключ устанавливается для столбца из зависимой таблицы, и указывает на один из столбцов из главной таблицы.

Как правило, внешний ключ указывает на первичный ключ из связанной главной таблицы.

* Задание **FK** при создании:

```
CREATE TABLE book
(
book_id serial PRIMARY KEY,
publisher_id serial [CONSTRAINT FK_books_publisher] REFERENCES publisher(publisher_id)
);
```

```
CREATE TABLE book
(
book_id serial PRIMARY KEY,
publisher_id serial,

CONSTRAINT FK_books_publisher FOREIGN KEY(publisher_id) REFERENCES publisher(publisher_id)
);
```

* Задание **FK** при изменении:

```
ALTER TABLE book
ADD CONSTRAINT FK_books_publisher FOREIGN KEY(publisher_id) REFERENCES publisher(publisher_id);
```

Если при **INSERT** в `book` передать в `publisher_id` не существующий **id**, то будет ошибка.

* Общий синтаксис установки внешнего ключа:

```
REFERENCES ref_table_name(ref_table_column_name)
    [ON DELETE {CASCADE|RESTRICT|...}]
    [ON UPDATE {CASCADE|RESTRICT|...}]
```

* С помощью выражений **ON DELETE** и **ON UPDATE** можно установить действия, которые выполняются соответственно при
  **удалении** и **изменении** связанной строки из главной таблицы.

Для установки подобного действия можно использовать следующие опции:

* **CASCADE**: автоматически удаляет или изменяет строки из зависимой таблицы при удалении или изменении связанных строк
  в главной таблице.

* **RESTRICT**: предотвращает какие-либо действия в зависимой таблице при удалении или изменении связанных строк в
  главной таблице. То есть фактически какие-либо действия отсутствуют.

* **NO ACTION**: действие по умолчанию, предотвращает какие-либо действия в зависимой таблице при удалении или изменении
  связанных строк в главной таблице. И генерирует ошибку. В отличие от **RESTRICT** выполняет проверку на связанность
  между таблицами в конце транзакции.

* **SET NULL**: при удалении связанной строки из главной таблицы устанавливает для столбца внешнего ключа значение
  **NULL**.

* **SET DEFAULT**: при удалении связанной строки из главной таблицы устанавливает для столбца внешнего ключа значение по
  умолчанию, которое задается с помощью атрибуты **DEFAULT**. Если для столбца не задано значение по умолчанию, то в
  качестве него применяется значение **NULL**.

---

### CHECK

* Используется для ограничения диапазона значений, которые могут быть помещены в столбец.


* Задание **CHECK** при создании:

```
CREATE TABLE book
(
book_id serial PRIMARY KEY,
price decimal [CONSTRAINT CHK_book_price] CHECK (price >= 0)
);
```

```
CREATE TABLE book
(
book_id serial PRIMARY KEY,
price decimal,
    
CONSTRAINT CHK_book_price CHECK (price >= 0)
);
```

* Задание **CHECK** при изменении:

```
ALTER TABLE book
ADD CONSTRAINT CHK_book_price CHECK (price >= 0); - сервер не даст записать данные, если не будет выполнено условие
```

* Внутри скобок может быть любое условие

---

### DEFAULT

* Используется для задания значения по умолчанию столбца.

Никаких **CONSTRAINT** для **DEFAULT** не нужно.

* Задание **DEFAULT** при создании:

```
CREATE TABLE customer
(
customer_id serial,
full_name text,
status char DEFAULT 'r',

CONSTRAINT PK_customer_customer_id PRIMARY KEY(customer_id),
CONSTRAINT CHK_customer_status CHECK(status = 'r' OR status = 'p')
)
```

* Задание **DEFAULT** при изменении:

```
ALTER TABLE customer
ALTER COLUMN status 
SET DEFAULT 'r';
```

* Удаление **DEFAULT** при изменении:

```
ALTER TABLE customer
ALTER COLUMN status 
DROP DEFAULT;
```

---

### Генератор последовательностей SEQUENCE

* Создание последовательности (счетчика):

```
CREATE SEQUENCE seq;
```

* Функции последовательностей:

```
SELECT nextval('seq'); - сначала запускает счетчик со значением старта, а далее делает следующие шаги и возвращает соответствующие значение последовательности.
SELECT currval('seq'); - возвращает текущее значение последовательности.
SELECT lastval(); - не принимает аргумент и возвращает последнее значение, сгенерованное какой-либо из последовательностей данной сессии.
SELECT setval('seq', 16, {true|false}) - устанавливает для последовательности заданное значение поля.
```

При **true** (по умолчанию) - `nextval('seq')` будет следующее число относительно заданного в `setval`.  
При **false** - `nextval('seq')` будет число заданное в `setval`.

* Основные параметры при создании последовательности:

```
CREATE SEQUENCE IF NOT EXISTS giga_seq
INCREMENT 16 - шаг 16
MINVALUE 0 - минимум 0 (при переходе выводит ошибку)
MAXVALUE 160 - максимум 160 (при переходе выводит ошибку)
START WITH 2 - начинает с 2 (по умолчанию стоит 0)
```

* Переименование последовательности:

```
ALTER SEQUENCE seq
RENAME TO new_seq; 
```

* Сброс последовательности:

```
ALTER SEQUENCE seq
RESTART [WITH num];
```

* Удаление последовательности:

```
DROP SEQUENCE seq;
```

---

### Последовательности и таблицы

* Делаем **serial** в домашних условиях:

```
CREATE TABLE book
(
book_id int NOT NULL,
title text NOT NULL,
isbn varchar(32) NOT NULL,
publisher_id int NOT NULL,

CONSTRAINT PK_book_book_id PRIMARY KEY(book_id)
);
```

```
CREATE SEQUENCE IF NOT EXISTS book_book_id_seq
START WITH 1 OWNED BY book.book_id;
```

```
ALTER TABLE book
ALTER COLUMN book_id 
SET DEFAULT nextval('book_book_id_seq'); - установить значения по умолчанию, иначе будет ошикба при INSERT.
```

Но всё не так красочно, ведь тут <u>так же как и у оригинального</u> **serial** существует проблема с ручной добавкой
**book_id**.

В какой-то момент будет ошибка - последовательность упрётся в номер, который мы добавили, тк **PK** по определению
**UNIQUE**.  
Проще говоря, нет синхронизации с реальностью.

* Делаем **serial++**:

```
CREATE TABLE book
(
book_id int GENERATED {ALWAYS или BY DEFAULT} AS IDENTITY (START WITH 1 INCREMENT BY 1 ...) NOT NULL,
title text NOT NULL,
isbn varchar(32) NOT NULL,
publisher_id int NOT NULL,

CONSTRAINT PK_book_book_id PRIMARY KEY(book_id)
);
```

```
INSERT INTO book (title, isbn, publisher_id)
VALUES
('data','data', 1);
```

В данном случае мы просто не сможем добавить в таблицу строку при указывании **book_id** вручную.

* Работает на версиях PostgreSQL >= 10.
* Другие СУБД поддерживают подобный синтаксис.

Ограничение можно обойти так:

```
INSERT INTO book
OVERRIDING SYSTEM VALUE
VALUES (3, 'data', 'data', 1)
```

---

### Оператор INSERT

* Вставляем во все столбцы таблицы.

```
INSERT INTO table_name
VALUES
(data1), 
(data2); - можно вставлять больше 1 строчки данных за раз
```

* Вставляем в конкретные столбцы таблицы.

```
INSERT INTO table_name (column1_name, ...)
VALUES ();
```

* Cоздаём новую таблицу `best_authors` с данными из `author` при условии `rating > 4`.

```
SELECT *
INTO best_authors
FROM author
WHERE rating > 4
```

* Вставляем данные из `author` в `best_authors` при условии `rating < 4`.

```
INSERT INTO best_authors 
SELECT *
FROM author
WHERE rating < 4
```

---

### Операторы UPDATE, DELETE, RETURNING

* **UPDATE** - обновляет данные таблицы.

```
UPDATE author
SET full_name = 'Big Man', rating = 5 - изменил значения full_name и rating в строке, где author_id = 3.
WHERE author_id = 3;
```

* **DELETE** - удаляет данные из таблицы, но сохраняет логи.

```
DELETE FROM author
WHERE rating < 4.5; - удалили все строки, где rating < 4.5.
```

```
DELETE FROM author; - удалит все строки.
```

* **RETURNING** - выводит данные, с которыми мы работали (вставили, обновили, удалили).

```
INSERT INTO book
VALUES ('data')
RETURNING *; - выведет всё, что мы вставили.
```

```
INSERT INTO book (book_id)
VALUES ('data')
RETURNING book_id; - выведет все book_id, что мы вставили.
```

```
UPDATE author
SET full_name = 'Big Man', rating = 5
WHERE author_id = 3
RETURNING *; - выведет всё, что мы обновили.
```

```
DELETE FROM author
WHERE author_id = 3
RETURNING *; - выведет всё, что мы удалили.
```

---

### Нормализация

* **Нормальная Форма** - свойство отношения, характеризующее его с точки зрения избыточности.

* **Нормализация** - процесс минимизации избыточности отношения (приведение к НФ).

**1 Нормальная форма**

* Нет строк-дубликатов.
* Все поля (атрибуты) простых типов данных (int, varchar, ...). Не массивы.
* Все значения скалярные (одно значение в поле). Не массивы.

**2 Нормальная форма**

* Удовлетворяет **1НФ**.
* Есть первичный ключ (может быть композитным).
* Все поля (атрибуты) описывают первичный ключ целиком, а не лишь его часть:

Таблица `(author_id, book_id, author_name, book_title)` - не подходит, тк `author_name` описывает только
ключ `author_id`, а `book_title` только `book_id`.  
Поэтому надо разбить данную таблицу на 3, `(author_id, author_name)`, `(book_id, book_title)`, `(author_id, book_id)`.

**3 Нормальная форма**

* Удовлетворяет **2НФ**
* Нет зависимостей одних неключевых атрибутов от других (все атрибуты зависят только от первичного или внешнего ключа)

Таблица `(book_id, book_title, publisher_title, publisher_contact)` - не подходит, тк `publisher_title` зависит
от `publisher_contact` и они оба не являются ключевыми.  
Поэтому надо разбить данную таблицу на 2, `(book_id, book_title, publisher_id)`, `(publisher_id, title, contact)`.


---

### Представления VIEW

* **VIEW** - сохранённый запрос (подзапрос) в виде объекта БД (виртуальная таблица).
* Так как **VIEW** объект, то его можно увидеть в Schemas - Public - Views.
* К **VIEW** можно делать обычный **SELECT**.
* **VIEW** можно соединять и тд (**JOIN**,...).
* Производительность такая же, как и у обычной таблицы.
* Позволять делать кеширование с помощью материализации.
* Позволяет сокращать сложные запросы.
* Позволяет подменить реальную таблицы.
* Позволяет создавать виртуальные таблицы, соединяющие несколько таблиц.
* Позволяет скрыть логику агрегации данных при работе через **ORM**.
* Позволяет скрыть информацию(строки/столбцы) от групп пользователей.

**Виды**:

* Временные. +
* Обновляемые. +
* Рекурсивные. -
* Материализуемые. -

```
CREATE VIEW view_name AS
SELECT select_statement - обычный запрос
```

Изменение (`REPLACE`) **VIEW**:

* Можно только добавлять в конец новые столбцы:
    * нельзя удалять существующие
    * нельзя поменять имена столбцов
    * нельзя поменять порядок следования столбцов

```
CREATE OR REPLACE VIEW view_name AS
SELECT select_statement;
```

* Можно переименовать **VIEW**:

```
ALTER VIEW view_name 
RENAME TO new_view_name;
```

* Можно удалить **VIEW**:

```
DROP VIEW [IF EXISTS] view_name;
```

Модифицировать данные (вставлять, удалять, ...) через **VIEW** можно, если:

* Данные только из одной таблицы в **SELECT**.
* Нет **DISTINCT**, **GROUP BY**, **HAVING**, **UNION**, **INTERSECT**, **EXCEPT**, **LIMIT**.
* Нет агрегатных функций **MIN**, **MAX**, **SUM**, **COUNT**, **AVG**, ...
* **WHERE** не под запретом.

```
CREATE VIEW products_suppliers_categories AS
SELECT product_name, quantity_per_unit, unit_price, units_in_stock, 
company_name, contact_name, phone, 
category_name, description
FROM products
JOIN suppliers USING (supplier_id)
JOIN categories USING (category_id);
```

Выведет все строки, где unit_price > 20:

```
SELECT *
FROM products_suppliers_categories
WHERE unit_price > 20;
```

---

### Обновляемые представления

Оригинальная таблица:

```
CREATE OR REPLACE VIEW heavy_orders AS
SELECT order_id, freight
FROM orders
WHERE freight > 50;
```

После выполнения данного кода в `heavy_orders` произойдёт изменение `freight > 100` без каких-либо ошибок:

```
CREATE OR REPLACE VIEW heavy_orders AS
SELECT order_id, freight
FROM orders
WHERE freight > 100;
```

В таком случае будет ошибка:

```
CREATE OR REPLACE VIEW heavy_orders AS
SELECT order_id, ship_via, freight
FROM orders
WHERE freight > 50;
```

Два запроса снизу смогут "обмануть" систему, но придётся **DROP**ать `new_view`:

```
ALTER VIEW heavy_orders RENAME TO new_view;
```

```
CREATE OR REPLACE VIEW heavy_orders AS
SELECT order_id, ship_via, freight
FROM orders
WHERE freight > 50;
```

Можно делать **INSERT** через **VIEW** (вставится в оригинальные таблицы):

```
INSERT INTO heavy_orders
VALUES (1, 1, 50);
```

Можно удалять строки, что есть во **VIEW** (они также удаляются из оригинала):

```
DELETE FROM heavy_orders 
WHERE freight < 100.25;
```

---

### CHECK во VIEW

```
CREATE OR REPLACE VIEW heavy_orders AS
SELECT *
FROM orders
WHERE freight > 100;
```

У нас получится вставить эти неподходящие под фильтр `freight > 100` данные через `heavy_orders`.   
Они попадут в оригинальную таблицу, но в `heavy_orders` их не будет.

```
INSERT INTO heavy_orders
VALUES
(11900, 'FOLIG', 1, '2000-01-01', '2000-01-05', '2000-01-04', 1, 80, 'Folies gourmandes', '184, 
chaussee de Tournai', 'Lille', NULL, 59000, 'FRANCE'); - в данном случае freight = 80
```

Можно модифицировать **VIEW** так, чтобы фильтр во **VIEW** учитывался при вставке:

```
CREATE OR REPLACE VIEW heavy_orders AS
SELECT *
FROM orders
WHERE freight > 100
WITH {LOCAL|CASCADE} CHECK OPTION;
```

* **LOCAL** - сервер будет проверять соответствие вставляемых данных фильтру **VIEW**.

* **CASCADE** - **LOCAL** + проверка будет и для подлежащих **VIEW** (детей).

---

### Условное выражение CASE

* Представляет собой общее условное выражение, напоминающее операторы **if/else** в других языках программирования:

```
CASE WHEN condition_1 THEN result_1 - if
     WHEN condition_2 THEN result_2 - elif
     [WHEN...]
     [ELSE result_n]
END
```

* **condition** - условие, возвращающее **bool**.
* **result** - результат или действие в случае с **PL**\**pgSQL**.

В данном случае будет дополнительный столбец `amount` со значениями, соответствующими условиям:

```
SELECT product_name, unit_price, units_in_stock,
    CASE WHEN units_in_stock >= 100 THEN 'lots of'
         WHEN units_in_stock >= 50 THEN 'average'
         WHEN units_in_stock < 50 THEN 'low number'
         ELSE 'unknown'
    END AS amount
FROM products;
```

---

### Условные выражения COALESCE и NULLIF

* **COALESCE**(`arg1`, `arg2`, ...); - принимает N аргументов и возвращает первый **!=NULL элемент**.   
  В случае, если все аргументы **NULL**, вернёт **NULL**.

```
SELECT order_id, order_date, COALESCE(ship_region, 'unknown') AS ship_region - если ship_region == NULL, будет выведено 'unknown'.
FROM orders
LIMIT 10;
```

* **NULLIF**(`arg1`, `arg2`) - сравнивает 2 аргумента и если они равны возвращает **NULL**.
  В случае, если они не равны, то вернёт `arg1`.

```
SELECT contact_name, COALESCE(NULLIF(city, ''), 'Unknown') as city - Если city == '', то будет 'Unknown', иначе будет city.
FROM customers;
```