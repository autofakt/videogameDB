SELECT * FROM games;
SELECT * FROM customer;
SELECT * FROM bank;
SELECT * FROM cart;
SELECT * FROM history;
DELETE FROM cart WHERE oid <> 0;
SELECT * FROM bank WHERE CID = '1';
INSERT INTO games (title,platform, price, quantity) VALUES ('FIFA 2021','PS4',5.99,3);
DELETE FROM games WHERE gid = 10;
DELETE FROM bank WHERE bid = 10;