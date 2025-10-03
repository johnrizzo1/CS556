drop table public.employee;

CREATE TABLE public.employee (
	fname varchar NULL,
	minit varchar NULL,
	lname varchar NULL,
	ssn varchar NOT NULL,
	bdate date null,
	address varchar NULL,
	sex bpchar(1) NULL,
	salary numeric NULL,
	superssn varchar NULL,
	dno varchar NULL,
	CONSTRAINT ssn PRIMARY KEY (ssn)
);

insert into public.employee (fname, minit, lname, ssn, bdate, address, sex, salary, superssn, dno) 
	values ('John', 'B', 'Smith', '123456789', '1965-01-09', '731 Fondren, Houston, TX', 'M', 30000, 333445555, 5);	
insert into public.employee (fname, minit, lname, ssn, bdate, address, sex, salary, superssn, dno) 
	values ('Franklin', 'T', 'Wong', '333445555', '1955-12-08', '638 Voss, Houston, TX', 'M', 40000, 888665555, 5);
insert into public.employee (fname, minit, lname, ssn, bdate, address, sex, salary, superssn, dno) 
	values ('Alicia', 'J', 'Zelaya', '999887777', '1968-07-19', '3321 Castle, Spring, TX', 'F', 25000, 987654321, 4);
insert into public.employee (fname, minit, lname, ssn, bdate, address, sex, salary, superssn, dno) 
	values ('Jennifer', 'S', 'Wallace', '987654321', '1941-06-20', '291 Berry, Bellaire, TX', 'F', 43000, 888665555, 4);
insert into public.employee (fname, minit, lname, ssn, bdate, address, sex, salary, superssn, dno) 
	values ('Ramesh', 'K', 'Narayan', '666884444', '1962-09-15', '975 Fire Oak, Humble, TX', 'M', 38000, 333445555, 5);
insert into public.employee (fname, minit, lname, ssn, bdate, address, sex, salary, superssn, dno) 
	values ('Joyce', 'A', 'English', '453453453', '1972-07-31', '5631 Rice, Houston, TX', 'F', 25000, 333445555, 5);
insert into public.employee (fname, minit, lname, ssn, bdate, address, sex, salary, superssn, dno) 
	values ('Ahmad', 'V', 'Jabbar', '987987987', '1969-03-29', '980 Dallas, Houston, TX', 'M', 25000, 987654321, 4);
insert into public.employee (fname, minit, lname, ssn, bdate, address, sex, salary, superssn, dno) 
	values ('James', 'E', 'Borg', '888665555', '1937-11-10', '450 Stone Houston, TX', 'M', 55000, null, 1);

drop table public.department;
create table public.department (
	dname varchar not null,
	mgrssn varchar null,
	mgrstartdate date null,
	dnumber integer not null,
	constraint dnumber primary key (dnumber)
);

insert into public.department (dname, dnumber, mgrssn, mgrstartdate) values ('Research', 5, 333445555, '1988-05-22');
insert into public.department (dname, dnumber, mgrssn, mgrstartdate) values ('Administration', 4, 987654321, '1995-01-01');
insert into public.department (dname, dnumber, mgrssn, mgrstartdate) values ('Headquarters', 1, 888665555, '1981-06-19');

-- 
-- Department Locations
drop table public.dept_locations ;
create table public.dept_locations (
	dlocation varchar not null,
	dnumber integer not null,
	primary key (dnumber, dlocation)
);

insert into public.dept_locations (dnumber, dlocation) values (1, 'Houston');
insert into public.dept_locations (dnumber, dlocation) values (4, 'Stafford');
insert into public.dept_locations (dnumber, dlocation) values (5, 'Bellaire');
insert into public.dept_locations (dnumber, dlocation) values (5, 'Sugarland');
insert into public.dept_locations (dnumber, dlocation) values (5, 'Houston');

--
-- Project
drop table public.project;
create table public.project (
	pname varchar null,
	pnumber integer not null,
	plocation varchar null,
	dnum integer null,
	primary key (pnumber)
);
insert into public.project (pname, pnumber, plocation, dnum) values ('ProductX', 1, 'Bellaire', 5);
insert into public.project (pname, pnumber, plocation, dnum) values ('ProductY', 2, 'Sugarland', 5);
insert into public.project (pname, pnumber, plocation, dnum) values ('ProductZ', 3, 'Houston', 5);
insert into public.project (pname, pnumber, plocation, dnum) values ('Computerization', 10, 'Stafford', 4);
insert into public.project (pname, pnumber, plocation, dnum) values ('Reorganization', 20, 'Houston', 1);
insert into public.project (pname, pnumber, plocation, dnum) values ('Newbenefits', 30, 'Stafford', 4);

-- 
-- works_on
drop table public.works_on;
create table public.works_on (
	essn varchar not null,
	pno integer not null,
	hours decimal,
	primary key (essn, pno)
);
insert into public.works_on (essn, pno, hours) values (123456789, 1, 32.5);
insert into public.works_on (essn, pno, hours) values (123456789, 2, 7.5);
insert into public.works_on (essn, pno, hours) values (666884444, 3, 40.0);
insert into public.works_on (essn, pno, hours) values (453453453, 1, 20.0);
insert into public.works_on (essn, pno, hours) values (453453453, 2, 20.0);
insert into public.works_on (essn, pno, hours) values (333445555, 2, 10.0);
insert into public.works_on (essn, pno, hours) values (333445555, 3, 10.0);
insert into public.works_on (essn, pno, hours) values (333445555, 10, 10.0);
insert into public.works_on (essn, pno, hours) values (333445555, 20, 10.0);
insert into public.works_on (essn, pno, hours) values (999887777, 30, 30.0);
insert into public.works_on (essn, pno, hours) values (999887777, 10, 10.0);
insert into public.works_on (essn, pno, hours) values (987987987, 10, 35.0);
insert into public.works_on (essn, pno, hours) values (987987987, 30, 5.0);
insert into public.works_on (essn, pno, hours) values (987654321, 30, 20.0);
insert into public.works_on (essn, pno, hours) values (987654321, 20, 15.0);
insert into public.works_on (essn, pno, hours) values (888665555, 20, null);

--
-- Dependent
drop table public.dependent;
create table public.dependent (
	essn varchar not null,
	dependent_name varchar not null,
	sex char,
	bdate date,
	relationship varchar,
	primary key (essn, dependent_name)
);
insert into public.dependent (essn, dependent_name, sex, bdate, relationship) values (333445555, 'Alice', 'F', '1986-04-05', 'Daughter');
insert into public.dependent (essn, dependent_name, sex, bdate, relationship) values (333445555, 'Theodore', 'M', '1983-10-25', 'Son');
insert into public.dependent (essn, dependent_name, sex, bdate, relationship) values (333445555, 'Joy', 'F', '1958-05-03', 'Spouse');
insert into public.dependent (essn, dependent_name, sex, bdate, relationship) values (987654321, 'Abner', 'M', '1942-02-28', 'Spouse');
insert into public.dependent (essn, dependent_name, sex, bdate, relationship) values (123456789, 'Michael', 'M', '1988-01-04', 'Son');
insert into public.dependent (essn, dependent_name, sex, bdate, relationship) values (123456789, 'Alice', 'F', '1988-12-30', 'Daughter');
insert into public.dependent (essn, dependent_name, sex, bdate, relationship) values (123456789, 'Elizabeth', 'F', '1967-05-05', 'Spouse');

--
-- Solutions

-- 1) Find every department that has a location in Chicago
select	department.dnumber
from	department, dept_locations
where 	department.dnumber = dept_locations.dnumber
	and dept_locations.dlocation = 'Houston'

-- 2) Find every project managed by a department with a location in Chicago
select 	project.pnumber
from 	department, dept_locations, project
where	department.dnumber = dept_locations.dnumber
	and project.dnum = dept_locations.dnumber
	and	project.plocation = 'Bellaire'

-- 3) Find every department whose manager works on a project 
--	  managed by a department with a location in Chicago
select 	department.dnumber
from 	department, works_on, project
where 	department.mgrssn = works_on.essn
	and works_on.pno = project.pnumber
	and project.plocation = 'Bellaire'
	
-- 4) Find every department that doesn't have a location in Chicago
select	department.dnumber, dept_locations.dlocation 
from	department, dept_locations
where	department.dnumber = dept_locations.dnumber 
	and dept_locations.dlocation != 'Bellaire'
	
-- 5) Find every department that manages at least two projects
-- 6) Find every employee who manages at least three departments
-- 7) Find every employee who neither has any supervisees, nor manages any department
-- 8) Find every employee who either has not supervisees or manages no department (or both)
-- 9) Find every employee who supervisees exactly two other employees