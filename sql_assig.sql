create database JOY;

use JOY;

CREATE TABLE SalesPeople(
    Snum INT,
	Sname VARCHAR(20) UNIQUE,
	City VARCHAR(20),
	Comm INT,
    PRIMARY KEY(Snum));
    
INSERT INTO SalesPeople(Snum,Sname,City,Comm)
values
(1001,"Peel","London",12),
(1002,"Serres","Sanjose",13),
(1004,"Motika","London",11),
(1007,"Rifkin","Barcelona",15),
(1003,"Axelrod","Newyork",10);

SELECT * FROM SalesPeople;

CREATE TABLE Customers(
    Cnum INT,
	Cname VARCHAR(20),
	City VARCHAR(20) NOT NULL,
	Snum INT,
    PRIMARY KEY(Cnum),
    FOREIGN KEY(Snum) REFERENCES SalesPeople(Snum));
    
INSERT INTO Customers(Cnum,Cname,City,Snum)
values
(2001,"Hoffman","London",1001),
(2002,"Giovanni","Rome",1003),
(2003,"Liu","Sanjose",1002),
(2004,"Grass","Berlin",1002),
(2006,"Clemens","London",1001),
(2008,"Cisneros","Sanjose",1007),
(2007,"Pereira","Rome",1004);

SELECT * FROM Customers;

CREATE TABLE Orders(
    Onum INT,
	Amt FLOAT,
	Odate DATE,
    Cnum INT,
    Snum INT,
    PRIMARY KEY(Onum),
    FOREIGN KEY(Cnum) REFERENCES Customers(Cnum),
    FOREIGN KEY(Snum) REFERENCES SalesPeople(Snum));
    
INSERT INTO Orders(Onum,Amt,Odate,Cnum,Snum)
values
(3001,18.69,"1990-10-3",2008,1007),
(3003,767.19,"1990-10-3",2001,1001),
(3002,1900.10,"1990-10-3",2007,1004),
(3005,5160.45,"1990-10-3",2003,1002),
(3006,1098.16,"1990-10-3",2008,1007),
(3009,1713.23,"1990-10-4",2002,1003),
(3007,75.75,"1990-10-4",2004,1002),
(3008,4273.00,"1990-10-5",2006,1001),
(3010,1309.95,"1990-10-6",2004,1002),
(3011,9891.88,"1990-10-6",2006,1001);

SELECT * FROM Orders;

/*
Count the number of Salesperson whose name begin with ‘a’/’A’.
*/
SELECT * FROM salespeople WHERE BINARY Sname LIKE "A%";
SELECT * FROM salespeople WHERE BINARY Sname LIKE "a%";
SELECT COUNT(Sname) FROM salespeople WHERE Sname LIKE "A%";   
SELECT COUNT(Sname) FROM salespeople WHERE BINARY Sname LIKE "a%"; 

/*
Display all the Salesperson whose all orders worth is more than Rs. 2000.
*/
SELECT salespeople.Sname,orders.Amt 
FROM salespeople 
INNER JOIN 
orders 
ON salespeople.Snum = orders.Snum 
WHERE Amt>2000;

/*
Count the number of Salesperson belonging to Newyork.
*/
SELECT * FROM salespeople WHERE City = "Newyork";
SELECT COUNT(City) AS City_Name FROM salespeople WHERE City = "Newyork";

/*
Display the number of Salespeople belonging to London and belonging to Paris.
*/
SELECT * FROM salespeople WHERE City IN ("London","Paris");

/*
Display the number of orders taken by each Salesperson and their date of orders.
*/
SELECT salespeople.Sname,COUNT(orders.Onum) AS "Numbers of Orders",orders.Odate FROM salespeople
INNER JOIN orders ON salespeople.Snum = orders.Snum GROUP BY salespeople.Sname;

SELECT salespeople.Sname,orders.Onum,orders.Odate FROM salespeople INNER JOIN orders ON salespeople.Snum = orders.Snum;