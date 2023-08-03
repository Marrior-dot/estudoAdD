CREATE TABLE EmployeeDemographics(
EmployeeId int,
FirstName varchar(50),
LastName varchar(50),
Age int,
Gender varchar(50)
)

CREATE TABLE EmployeeSalary(
EmployeeId int,
JobTitle varchar(50),
Salary int
)

-- Query 1
INSERT INTO EmployeeDemographics(EmployeeId, FirstName, LastName, Age, Gender)
VALUES (1, 'John', 'Doe', 28, 'Male');

-- Query 2
INSERT INTO EmployeeDemographics(EmployeeId, FirstName, LastName, Age, Gender)
VALUES (2, 'Jane', 'Smith', 35, 'Female');

-- Query 3
INSERT INTO EmployeeDemographics(EmployeeId, FirstName, LastName, Age, Gender)
VALUES (3, 'Michael', 'Johnson', 42, 'Male');

-- Query 4
INSERT INTO EmployeeDemographics(EmployeeId, FirstName, LastName, Age, Gender)
VALUES (4, 'Emily', 'Williams', 31, 'Female');

-- Query 5
INSERT INTO EmployeeDemographics(EmployeeId, FirstName, LastName, Age, Gender)
VALUES (5, 'Daniel', 'Brown', 25, 'Male');

-- Query 6
INSERT INTO EmployeeDemographics(EmployeeId, FirstName, LastName, Age, Gender)
VALUES (6, 'Sarah', 'Jones', 29, 'Female');

-- Query 7
INSERT INTO EmployeeDemographics(EmployeeId, FirstName, LastName, Age, Gender)
VALUES (7, 'Christopher', 'Davis', 38, 'Male');

-- Query 8
INSERT INTO EmployeeDemographics(EmployeeId, FirstName, LastName, Age, Gender)
VALUES (8, 'Jessica', 'Miller', 27, 'Female');

-- Query 1
INSERT INTO EmployeeSalary(EmployeeId, JobTitle, Salary)
VALUES (1, 'Software Engineer', 75000);

-- Query 2
INSERT INTO EmployeeSalary(EmployeeId, JobTitle, Salary)
VALUES (2, 'Marketing Specialist', 60000);

-- Query 3
INSERT INTO EmployeeSalary(EmployeeId, JobTitle, Salary)
VALUES (3, 'Project Manager', 90000);

-- Query 4
INSERT INTO EmployeeSalary(EmployeeId, JobTitle, Salary)
VALUES (4, 'Data Analyst', 65000);

-- Query 5
INSERT INTO EmployeeSalary(EmployeeId, JobTitle, Salary)
VALUES (5, 'UI/UX Designer', 70000);

-- Query 6
INSERT INTO EmployeeSalary(EmployeeId, JobTitle, Salary)
VALUES (6, 'Sales Representative', 55000);

-- Query 7
INSERT INTO EmployeeSalary(EmployeeId, JobTitle, Salary)
VALUES (7, 'Financial Analyst', 80000);

-- Query 8
INSERT INTO EmployeeSalary(EmployeeId, JobTitle, Salary)
VALUES (8, 'HR Manager', 72000);

-- Query 9
INSERT INTO EmployeeSalary(EmployeeId, JobTitle, Salary)
VALUES (9, 'Systems Administrator', 68000);
