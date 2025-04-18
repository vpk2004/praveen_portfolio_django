use portfolio_database;
create database portfolio_database;


CREATE TABLE pf_details(
s_no INT PRIMARY KEY AUTO_INCREMENT,
full_name VARCHAR(20),
ph_no VARCHAR(12),
e_mail VARCHAR(40),
e_mail_subject VARCHAR(100),
visiter_msg VARCHAR(300)
);


SELECT * FROM pf_details;
