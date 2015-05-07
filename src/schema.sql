create database monitor;
GRANT ALL PRIVILEGES ON monitor.* to 'user'@'localhost';
FLUSH PRIVILEGES;

create table bw_internet ( timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, rx bigint unsigned DEFAULT 0, tx bigINT unsigned DEFAULT 0, PRIMARY KEY (timestamp) );
