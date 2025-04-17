-- step 1: create database
create database ordermanagementsystem;

-- step 2: use the created database
use ordermanagementsystem

-- create tables

-- users table
create table users (
    userid int primary key identity(1,1),
    username varchar(100),
    password varchar(100),
    role varchar(50)
)
-- products table
create table products (
    productid int primary key identity(1,1),
    productname varchar(100),
    description text,
    price decimal(10, 2),
    quantityinstock int,
    type varchar(50)
)

-- electronics table
create table electronics (
    productid int primary key,
    brand varchar(100),
    warrantyperiod int,
    foreign key (productid) references products(productid)
)

-- clothing table
create table clothing (
    productid int primary key,
    size varchar(10),
    color varchar(50),
    foreign key (productid) references products(productid)
)

-- orders table
create table orders (
    orderid int primary key identity(1,1),
    userid int,
    foreign key (userid) references users(userid)
)

-- order details table
create table order_details (
    orderdetailid int primary key identity(1,1),
    orderid int,
    productid int,
    quantity int,
    foreign key (orderid) references orders(orderid),
    foreign key (productid) references products(productid)
)

-- insert users (harry potter characters)
insert into users (username, password, role) values
('harry_potter', 'expelliarmus', 'user'),
('hermione_granger', 'leviosa123', 'user'),
('ron_weasley', 'chessmaster', 'user'),
('albus_dumbledore', 'elderwand', 'admin'),
('severus_snape', 'always', 'admin'),
('draco_malfoy', 'slytherin', 'user'),
('luna_lovegood', 'wrackspurt', 'user'),
('neville_longbottom', 'herbology', 'user'),
('ginny_weasley', 'batbogey', 'user'),
('sirius_black', 'padfoot', 'admin')

-- insert products (electronics + clothing)
insert into products (productname, description, price, quantityinstock, type) values
('laptop', 'dell inspiron 15', 55000.0, 100, 'electronics'),
('t-shirt', 'gryffindor cotton t-shirt, size m', 500.0, 200, 'clothing'),
('smartphone', 'iphone 13', 80000.0, 50, 'electronics'),
('jeans', 'blue denim, size 32', 1200.0, 150, 'clothing'),
('tablet', 'samsung galaxy tab', 30000.0, 60, 'electronics'),
('jacket', 'black leather jacket, size l', 3500.0, 90, 'clothing'),
('headphones', 'sony wh-1000xm4', 20000.0, 80, 'electronics'),
('sweater', 'woolen sweater, size m', 1500.0, 120, 'clothing'),
('monitor', 'hp 24-inch monitor', 10000.0, 70, 'electronics'),
('hoodie', 'hogwarts hoodie, size l', 1800.0, 110, 'clothing')

-- insert electronics details
insert into electronics (productid, brand, warrantyperiod) values
(1, 'dell', 2),
(3, 'apple', 1),
(5, 'samsung', 2),
(7, 'sony', 1),
(9, 'hp', 2)
-- insert clothing details
insert into clothing (productid, size, color) values
(2, 'm', 'red'),
(4, '32', 'blue'),
(6, 'l', 'black'),
(8, 'm', 'grey'),
(10, 'l', 'maroon')

-- insert orders
insert into orders (userid) values (1)
insert into orders (userid) values (2)
insert into orders (userid) values (3)
insert into orders (userid) values (4)
insert into orders (userid) values (5)
insert into orders (userid) values (6)
insert into orders (userid) values (7)
insert into orders (userid) values (8)
insert into orders (userid) values (9)
insert into orders (userid) values (10)

-- insert order details
insert into order_details (orderid, productid, quantity) values
(1, 1, 2),
(1, 2, 1),
(2, 3, 1),
(3, 4, 2),
(4, 5, 1),
(5, 6, 3),
(6, 7, 1),
(7, 8, 2),
(8, 9, 1),
(9, 10, 2)

-- view data
select * from users
select * from products
select * from electronics
select * from clothing
select * from orders
select * from order_details
