CREATE TABLE Table_India(
Name VARCHAR(255) NOT NULL,
Cust_I VARCHAR(18) NOT NULL PRIMARY KEY,
Open_Dt DATE NOT NULL,
Consul_Dt DATE,
VAC_ID CHAR(5),
DR_Name CHAR(255),
State CHAR(5),
Country CHAR(5),
DOB DATE,
FLAG CHAR(1)
);


f = open('file.txt', 'r')
while True:
    Dummy, 	Name, Cust_I, Open_Dt DATE, Consul_Dt, VAC_ID, DR_Name, State, Country, DOB, FLAG = list(map(str,f.readline().split('|')
	if name != 'H':
		INSERT INTO 
		(Name, Cust_I, Open_Dt DATE, Consul_Dt, VAC_ID, DR_Name, State, Country, DOB, FLAG)
		VALUES
		(Name, Cust_I, Open_Dt DATE, Consul_Dt, VAC_ID, DR_Name, State, Country, DOB, FLAG)
		);
f.close()