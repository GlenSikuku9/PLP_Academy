## **Assignment Questions**

1. State and Explain the components of a DBMS(Database Management System)
  -A DBMS is a software that allows users to define, create and manage databases. The components are:
   -Database Schema: Defines the structure of the database, including tables, relationships, and constraints.
   -Data Manager: Manages the storage of data on disk and handles  transactions and concurrency.
   -Database Engine: Handles data storage, retrieval, and updates to the database.

2. What is a relational database? Give 4 examples.
  -A relational database is a type of database that stores data in structured tables with rows and columns. Relationships between tables are established using keys (e.g., primary and foreign keys). It uses SQL for querying and managing the data. Examples: MySQL, PostgreSQL, Oracle Database and Microsoft SQL Server.


3. State and Explain three classifications of SQL?
  -Data Definition Language (DDL): Used to define or modify database structures. Examples: CREATE, ALTER, DROP.
   Example: CREATE TABLE students (id INT, name VARCHAR(50));
  -Data Manipulation Language (DML): Used to manipulate data in the database. Examples: INSERT, UPDATE, DELETE, SELECT.
   Example: INSERT INTO students (id, name) VALUES (1, 'John');
  -Data Control Language (DCL): Used to control access to the database Examples: GRANT, REVOKE.
  Example: GRANT SELECT ON students TO user1;


4. What is the difference between a Primary Key and a Foreign Key?
  -Primary Key:
   .A unique identifier for a record in a table.
   .Cannot have NULL values.
   .Example: In a students table, student_id could be the primary key.

  -Foreign Key:
   .A column that establishes a relationship between two tables by  referencing the primary key of another table.
   .Can have duplicate values and NULL values.
   .Example: class_id in a students table referencing the id in a classes table.

5. What is an Entity-Relationship Diagram?
  -An Entity-Relationship Diagram (ERD) is a visual representation of the relationships between entities in a database. It uses shapes (e.g., rectangles for entities, diamonds for relationships, and ovals for attributes) to map out how data is structured and interconnected.




6. What are the advantages of relational databases?
 1)Data Integrity: Maintains accuracy and consistency of data through constraints.
 2)Flexibility: Easily adapts to changes in database structure.
 3)Efficient Data Retrieval: SQL allows powerful querying capabilities.
 4)Scalability: Can handle growing data volumes and user loads.
 5)Data Security: Supports robust access control mechanisms.

7. State four types of data type used to store data in tables?
  1)INT: Stores integers (e.g., 1, 2, -5).
  2)VARCHAR: Stores variable-length text strings (e.g., names, descriptions).
  3)DATE: Stores dates (e.g., 2024-11-26).
  4)FLOAT/DOUBLE: Stores floating-point numbers (e.g., 3.14, 2.718).

   
8. What is the purpose of a database management system (DBMS)?  
  -The primary purpose of a DBMS is to efficiently manage and organize data. Key purposes include:

   1)Data Storage and Retrieval: Provides a centralized system for storing and retrieving data.
   2)Data Security: Ensures authorized access to the database.
   3)Data Consistency: Maintains accuracy across the database with constraints and integrity rules.