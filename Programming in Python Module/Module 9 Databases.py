"""
Databases

Entities relate through shared data called primary keys and foreign keys.
A primary key is a unique identifier for a record in a table, while a foreign key is a field in one table that refers to the primary key in another table.
A composite key is a combination of two or more columns that uniquely identify a record in a table.
This happens when no single column can uniquely identify a record. Example:
Employees with same ID but different department codes.
Candidate keys are columns or sets of columns that can uniquely identify a record in a table. A table can have multiple candidate keys, but only one primary key.

Types of databases:
1. Relational Databases: Use tables to store data and SQL for querying (e.g., MySQL, PostgreSQL).
2. NoSQL Databases: Use various data models like document, key-value, graph, or column-family (e.g., MongoDB, Cassandra).

NoSQL databases are better for handling unstructured data, scaling horizontally, and providing flexibility in data models.

SQL is the language used to manage and manipulate relational databases.
Database Management Systems (DBMS) then read and write data to the database based on SQL commands.

SQL SUBSETS:
- DDL (Data Definition Language): Commands that define the database structure (e.g., CREATE, ALTER, DROP).
- DML (Data Manipulation Language): Commands that manipulate data within the database (e.g., INSERT, UPDATE, DELETE).
- DQL (Data Query Language): Commands that query data from the database (e.g., SELECT).
- DCL (Data Control Language): Commands that control access to the database (e.g., GRANT, REVOKE).

DDL Commands:
- CREATE: Create a new database or table.
- ALTER: Modify an existing database or table.
- DROP: Delete a database or table.

DML Commands:
- SELECT: Retrieve data from a database.
- INSERT: Add new records to a table.
- UPDATE: Modify existing records in a table.
- DELETE: Remove records from a table.

DQL Commands:
- SELECT: Used to query and retrieve data from a database.

DCL Commands:
- GRANT: Give users access privileges to the database.
- REVOKE: Remove users' access privileges to the database.

SYNTAX EXAMPLES:
DDL:
    1. CREATE TABLE table_name (
        column1 datatype(size) PRIMARY KEY,
        column2 datatype(size) NOT NULL DEFAULT 'default_value',
        ...
    );
    2. DROP TABLE table_name;
    3. ALTER TABLE table_name ADD PRIMARY KEY (column_name);
    4. TRUNCATE TABLE table_name;

DQL:
    1. SELECT column1, column2 FROM table_name WHERE condition;

DML:
    1. INSERT INTO table_name (column1, column2) VALUES (value1, value2);
    2. UPDATE table_name SET column1 = value1 WHERE condition;
    3. DELETE FROM table_name WHERE condition;

DCL:
    1. GRANT ALL PRIVILEGES ON database_name TO 'username'@'host';
    2. REVOKE ALL PRIVILEGES ON database_name FROM 'username'@'host';

Las constraints son reglas aplicadas a las columnas de una tabla para asegurar la integridad de los datos. Algunos ejemplos comunes incluyen:
    Key constraints: ej PRIMARY KEY, FOREIGN KEY, aseguran que no haya filas duplicadas o que sean null
    Domain constraints: ej NOT NULL, UNIQUE, aseguran que los tipos de datos y valores sean correctos, ej: abc en una columna INT
    Referential integrity constraints: ej FOREIGN KEY con ON DELETE CASCADE, cohherencia entre tablas relacionadas. No puede haber un pedido con un cliente que no existe.

Datatypes:
    INT: Enteros
    FLOAT: Números de punto flotante
    CHAR(size): Cadena de caracteres de longitud fija
    VARCHAR(size): Cadena de caracteres de longitud variable
    DATE: Fecha
    DATETIME: Fecha y hora
    BOOLEAN: Valores verdadero/falso

SQL OPERATORS:
    Aritmeticos: +, -, *, /, %
    Comparacion: =, !=, <, >, <=, >=, !<, !>
    Logicos: AND, OR, NOT
    Bitwise: &, |, ^, ~, <<, >>

ORDER BY Clause:
    Se usa para ordenar los resultados de una consulta SQL en orden ascendente (ASC) o descendente (DESC).
    Por defecto, el orden es ascendente.
    Sintaxis:
    SELECT column1, column2 FROM table_name ORDER BY column1 ASC|DESC, column2 ASC|DESC;

Conexión a SQL:
    ABRO MYSQL SHELL
    \sql
    \connect root@localhost:3306  (osioso123450)
    control + c para salir para atras si le erro

BETWEEN Operator:
    Se usa para filtrar los resultados dentro de un rango especificado.
    Sintaxis:
    SELECT column1, column2 FROM table_name WHERE column1 BETWEEN value1 AND value2;

LIKE Operator:
    Se usa para buscar un patrón específico en una columna.
    Sintaxis:
    SELECT column1, column2 FROM table_name WHERE column1 LIKE pattern;
    - % representa cero o más caracteres
    - _ representa un solo carácter
    Ejemplo real usando % y _:
    SELECT * FROM Employees WHERE Name LIKE 'a%' AND City LIKE '_a%';
    Ejemplos:
    - 'a%' encuentra cualquier valor que comience con "a"
    - '%a' encuentra cualquier valor que termine con "a"
    - '%or%' encuentra cualquier valor que contenga "or"
    - '_r%' encuentra cualquier valor con "r" en la segunda posición
    - 'a_%_%' encuentra cualquier valor que comience con "a" y tenga al menos 3 caracteres

EXISTS Operator:
    Se usa para verificar la existencia de filas en una subconsulta.
    Sintaxis:
    SELECT column1, column2 FROM table_name WHERE EXISTS (subquery);
    Ejemplo:
    SELECT * FROM Employees E WHERE EXISTS (SELECT * FROM Orders O WHERE O.EmployeeID = E.EmployeeID);

IN Operator:
    Se usa para filtrar los resultados que coinciden con un conjunto específico de valores.
    Sintaxis:
    SELECT column1, column2 FROM table_name WHERE column1 IN (value1, value2, ...);
    Ejemplo:
    SELECT * FROM Employees WHERE Country IN ('USA', 'Canada', 'UK');

IS NULL Operator:
    Se usa para filtrar los resultados que tienen valores nulos en una columna.
    Sintaxis:
    SELECT column1, column2 FROM table_name WHERE column1 IS NULL;
    Ejemplo:
    SELECT * FROM Employees WHERE ManagerID IS NULL;

SELECT DISTINCT:
    Se usa para eliminar filas duplicadas en los resultados de una consulta SQL.
    Sintaxis:
    SELECT DISTINCT column1, column2 FROM table_name;
    Ejemplo:
    SELECT DISTINCT Country FROM Customers;

DATABASE SCHEMA: Es una forma de organizar los objetos de una base de datos Depende de que base de datos uses.
    MySQL: schema = base de datos. No hay diferencia práctica entre ambos; se usan como lo mismo.
    PostgreSQL: un schema es como una carpeta dentro de una base de datos, que sirve para ordenar tablas y otros objetos.
    Oracle: un schema está asociado a un usuario y contiene todos los objetos que ese usuario crea en la base de datos.


"""
