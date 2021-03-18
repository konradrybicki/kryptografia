create database service;

use service;

create table users(
  Login varchar(10) primary key,
  PasswordHash varchar(64) unique not null,
  PasswordSalt varchar(64) unique not null
);