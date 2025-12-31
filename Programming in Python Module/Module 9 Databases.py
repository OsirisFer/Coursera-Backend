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
    Key constraints: ej PRIMARY KEY, FOREIGN KEY
    Domain constraints: ej NOT NULL, UNIQUE
    Referential integrity constraints: ej FOREIGN KEY con ON DELETE CASCADE

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
    Comparacion: =, !=, <, >, <=, >=
    Logicos: AND, OR, NOT
    Bitwise: &, |, ^, ~, <<, >>

ORDER BY Clause:
    Se usa para ordenar los resultados de una consulta SQL en orden ascendente (ASC) o descendente (DESC).
    Sintaxis:
    SELECT column1, column2 FROM table_name ORDER BY column1 ASC|DESC;
    

"""
