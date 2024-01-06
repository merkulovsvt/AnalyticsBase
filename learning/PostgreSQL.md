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
    * `TRUNCATE TABLE` table_name – удалить все данные, но оставить структуру (нельзя резать таблицы, на которые есть
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
    
    CONSTRAINT book_author_pkey PRIMARY KEY (book_id, author_id) - композитный ключ (состояющий из более чем одной колонки)
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
WHERE quantity > ALL (SELECT AVG(quantity)
   FROM order_details
   GROUP BY product_id
   )
```

---
