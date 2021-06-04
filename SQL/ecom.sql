CREATE TABLE `User` (Id int(10) NOT NULL auto_increment, Username varchar(255), Pass varchar(255), Role varchar(255), PRIMARY KEY (Id));
CREATE TABLE Staff (Id int(10) NOT NULL auto_increment, User_id int(10) NOT NULL, Gender int(10) NOT NULL, Brithday varchar(255), Address varchar(255), Phone varchar(255), Name varchar(255), Salary int(10) NOT NULL, Email varchar(255), PRIMARY KEY (Id));
CREATE TABLE Cart (Id int(10) NOT NULL auto_increment, Person_id int(10) NOT NULL, PRIMARY KEY (Id));
CREATE TABLE CartItem (Id int(10) NOT NULL auto_increment, Cart_id int(10) NOT NULL, Product_id int(10) NOT NULL, Quantity int(10) NOT NULL, PRIMARY KEY (Id));
CREATE TABLE `Order` (Id int(10) NOT NULL auto_increment, Person_id int(10) NOT NULL, Cart_id int(10) NOT NULL, Payment_id int(10) NOT NULL, Shipment_id int(10) NOT NULL, Bank_id int(10) NOT NULL, Created_time varchar(255), Status int(10) NOT NULL, Method int(10) NOT NULL, PRIMARY KEY (Id));
CREATE TABLE Payment (Id int(10) NOT NULL auto_increment, Shipment_id int(10) NOT NULL, Total int(10) NOT NULL, PRIMARY KEY (Id));
CREATE TABLE Shipment (Id int(10) NOT NULL auto_increment, ShipFee int(10) NOT NULL, Address varchar(255), Phone varchar(255), Name varchar(255), PRIMARY KEY (Id));
CREATE TABLE Invoice (Id int(10) NOT NULL auto_increment, Order_id int(10) NOT NULL, Bank_id int(10) NOT NULL, Created_time varchar(255), Price int(10) NOT NULL, Status int(10) NOT NULL, PRIMARY KEY (Id));
CREATE TABLE Bank (Id int(10) NOT NULL auto_increment, Name varchar(255), Account varchar(255), Number varchar(255), PRIMARY KEY (Id));
CREATE TABLE Inventory (Id int(10) NOT NULL auto_increment, Book_id int(10), Elector_id int(10), Clothes_id int(10), Type int(10) NOT NULL, Price int(10) NOT NULL, Quantity int(10) NOT NULL, Created_time varchar(255), PRIMARY KEY (Id));
CREATE TABLE Product (Id int(10) NOT NULL auto_increment, Inventory_id int(10) NOT NULL, Type int(10) NOT NULL, Sale int(10) NOT NULL, Price int(10) NOT NULL, Quantity int(10) NOT NULL, Created_time varchar(255), Description varchar(255), PRIMARY KEY (Id));
CREATE TABLE Person (Id int(10) NOT NULL auto_increment, User_id int(10) NOT NULL, Gender int(10) NOT NULL, Birthday varchar(255), Address varchar(255), Phone varchar(255), Name varchar(255), Email varchar(255), PRIMARY KEY (Id));
CREATE TABLE Book (Id int(10) NOT NULL auto_increment, Supplier_id int(10) NOT NULL, Category_id int(10) NOT NULL, Name varchar(255), Author varchar(255), Publisher varchar(255), Category varchar(255), PRIMARY KEY (Id));
CREATE TABLE Electro (Id int(10) NOT NULL auto_increment, Supplier_id int(10) NOT NULL, Name varchar(255), Width varchar(255), Height varchar(255), Weight varchar(255), Branch varchar(255), PRIMARY KEY (Id));
CREATE TABLE Clothes (Id int(10) NOT NULL auto_increment, Supplier_id int(10) NOT NULL, FashionCategory_id int(10) NOT NULL, Name varchar(255), `Size` varchar(255), FashionCategory_name varchar(255), Branch varchar(255), Color varchar(255), PRIMARY KEY (Id));
CREATE TABLE Supplier (Id int(10) NOT NULL auto_increment, Name int(10) NOT NULL, Address int(10) NOT NULL, PRIMARY KEY (Id));
CREATE TABLE category (Id int(10) NOT NULL auto_increment, Name varchar(255), PRIMARY KEY (Id));
CREATE TABLE FashionCategory (Id int(10) NOT NULL auto_increment, Name varchar(255), PRIMARY KEY (Id));
ALTER TABLE Cart ADD CONSTRAINT FKCart401932 FOREIGN KEY (Person_id) REFERENCES Person (Id);
ALTER TABLE Person ADD CONSTRAINT FKPerson681017 FOREIGN KEY (User_id) REFERENCES `User` (Id);
ALTER TABLE Staff ADD CONSTRAINT FKStaff374805 FOREIGN KEY (User_id) REFERENCES `User` (Id);
ALTER TABLE `Order` ADD CONSTRAINT FKOrder762820 FOREIGN KEY (Person_id) REFERENCES Person (Id);
ALTER TABLE `Order` ADD CONSTRAINT FKOrder118433 FOREIGN KEY (Bank_id) REFERENCES Bank (Id);
ALTER TABLE `Order` ADD CONSTRAINT FKOrder814380 FOREIGN KEY (Payment_id) REFERENCES Payment (Id);
ALTER TABLE `Order` ADD CONSTRAINT FKOrder465057 FOREIGN KEY (Shipment_id) REFERENCES Shipment (Id);
ALTER TABLE Invoice ADD CONSTRAINT FKInvoice290755 FOREIGN KEY (Order_id) REFERENCES `Order` (Id);
ALTER TABLE `Order` ADD CONSTRAINT FKOrder356458 FOREIGN KEY (Cart_id) REFERENCES Cart (Id);
ALTER TABLE Invoice ADD CONSTRAINT FKInvoice548949 FOREIGN KEY (Bank_id) REFERENCES Bank (Id);
ALTER TABLE Payment ADD CONSTRAINT FKPayment54008 FOREIGN KEY (Shipment_id) REFERENCES Shipment (Id);
ALTER TABLE CartItem ADD CONSTRAINT FKCartItem949738 FOREIGN KEY (Cart_id) REFERENCES Cart (Id);
ALTER TABLE CartItem ADD CONSTRAINT FKCartItem549173 FOREIGN KEY (Product_id) REFERENCES Product (Id);
ALTER TABLE Product ADD CONSTRAINT FKProduct894604 FOREIGN KEY (Inventory_id) REFERENCES Inventory (Id);
ALTER TABLE Inventory ADD CONSTRAINT FKInventory778691 FOREIGN KEY (Book_id) REFERENCES Book (Id);
ALTER TABLE Inventory ADD CONSTRAINT FKInventory462384 FOREIGN KEY (Elector_id) REFERENCES Electro (Id);
ALTER TABLE Inventory ADD CONSTRAINT FKInventory572660 FOREIGN KEY (Clothes_id) REFERENCES Clothes (Id);
ALTER TABLE Book ADD CONSTRAINT FKBook164516 FOREIGN KEY (Supplier_id) REFERENCES Supplier (Id);
ALTER TABLE Electro ADD CONSTRAINT FKElectro708033 FOREIGN KEY (Supplier_id) REFERENCES Supplier (Id);
ALTER TABLE Clothes ADD CONSTRAINT FKClothes984155 FOREIGN KEY (Supplier_id) REFERENCES Supplier (Id);
ALTER TABLE Clothes ADD CONSTRAINT FKClothes638580 FOREIGN KEY (FashionCategory_id) REFERENCES FashionCategory (Id);
ALTER TABLE Book ADD CONSTRAINT FKBook729070 FOREIGN KEY (Category_id) REFERENCES category (Id);
ALTER TABLE supplier MODIFY name varchar(255);  
ALTER TABLE supplier MODIFY address varchar(255);  
ALTER TABLE inventory MODIFY Book_id int(10);  
ALTER TABLE inventory MODIFY Elector_id int(10);  
ALTER TABLE inventory MODIFY Clothes_id int(10);  
ALTER TABLE `Order` MODIFY payment_id int(10);  
ALTER TABLE `Order` MODIFY shipment_id int(10);  
ALTER TABLE `Order` MODIFY bank_id int(10); 
ALTER TABLE `Order` add total int(10); 

ALTER TABLE cart add is_used varchar(255);

select * from user;
insert into User (Username, Pass, Role) values ("warehouse", "123", "warehouse_staff");
insert into User (Username, Pass, Role) values ("sale", "123", "sale_staff");
insert into User (Username, Pass, Role) values ("business", "123", "business_staff");
insert into Bank (name, account, number) values ("Asia Commercial Bank (ACB)", "2131231231", "123123123123");


select * from person;
select * from category;
select * from FashionCategory;
select * from supplier;
select * from book;
select * from electro;
select * from inventory;
select * from product;
select * from cart;
select * from cartitem;
select * from `order`;

SET SQL_SAFE_UPDATES = 0;
delete from book;
delete from person;
delete from User where Role = 'Customer';
delete from product;
delete from product where id = 5;
delete from cartitem;
delete from `order`;


-- alter table
