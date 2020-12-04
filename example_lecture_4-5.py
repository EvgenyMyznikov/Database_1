import psycopg2
import sqlalchemy
from pprint import pprint

# создаем engine
# dialect+driver://username:password@host:port/database
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
# pprint(engine)

# установим соединение
connection = engine.connect()

# Посмотрим, какие таблицы есть
# pprint(engine.table_names())

# SELECT
# выбираем все поля из таблицы film и выводим первую строчку
sel = connection.execute('''SELECT * FROM film;
''').fetchone()
# pprint(sel)
# pprint(type(sel))

# Выберем столбец title таблицы film
sel2 = connection.execute('''SELECT title FROM film;
''').fetchmany(10)
# pprint(sel2)

# Выберем 2 столбца из таблицы film
sel3 = connection.execute('''SELECT title, release_year FROM film;
''').fetchmany(10)
# pprint(sel3)

# Выведем имена и фамилии актеров
sel4 = connection.execute('''SELECT first_name, last_name FROM actor;
''').fetchall()
# pprint(sel4)

# Как работает DISTINCT
# Выведем столбик rating из film
sel5 = connection.execute('''SELECT rating FROM film;
''').fetchmany(10)
# print(sel5)
# Найдем, какие уникальные рейтинги бывают с помощью DISTINCT
sel6 = connection.execute('''SELECT DISTINCT rating FROM film;
''').fetchall()
# print(sel6)

# Примеры с арифметикой
# Переведем цены в условные рубли. Попробуем умножить столбец amount на число
sel7 = connection.execute('''SELECT amount * 70 FROM payment;
''').fetchmany(10)
# pprint(sel7)

# Мы можем делать операции не только над числами, но и между столбцами
# Узнаем время аренды по позициям
sel8 = connection.execute('''SELECT rental_date - return_date FROM rental;
''').fetchmany(10)
# pprint(sel8)

# Оператор WHERE. Найдем фильмы, вышедшие после 2000 года
sel9 = connection.execute('''SELECT title, release_year FROM film
WHERE release_year >= 2000;
''').fetchall()
# pprint(sel9)

# Найдем сотрудников, которые сейчас работают. Внимание критерий отбора (в данном случае active
# не обязательно должен входить в выборку. И без этого все будет работать
sel10 = connection.execute('''SELECT first_name, last_name, active FROM staff
WHERE active = true;
''').fetchall()
# pprint(sel10)

# Найдем id, имена, фамилии актеров которых зовут JOE
sel11 = connection.execute('''SELECT actor_id, first_name, last_name FROM actor
WHERE first_name = 'JOE';
''').fetchmany(10)
# pprint(sel11)

# Найдем всех сотрудников, которые работают не во втором магазине
sel12 = connection.execute('''SELECT first_name, last_name FROM staff
WHERE store_id != 2;
''').fetchmany(10)
# pprint(sel12)

# Найдем только работающих сотрудников из всех магазинов кроме 1
sel13 = connection.execute('''SELECT first_name, last_name FROM staff
WHERE active = true AND NOT store_id = 1; 
''').fetchmany(10)  # тут равносильно можно было написать WHERE active = true AND store_id != 1;
# pprint(sel13)

# Найдем фильмы, цена проката которых меньше 0,99, а цена возмещения меньше 9,99
sel14 = connection.execute('''SELECT title, rental_rate, replacement_cost FROM film
WHERE rental_rate <= 0.99 AND replacement_cost <= 9.99; 
''').fetchmany(10)
# pprint(sel14)

# Найдем фильмы, аналогичные предыдущему примеру или продолжительностью менее 30 минут
sel15 = connection.execute('''SELECT title, length, rental_rate, replacement_cost FROM film
WHERE length <= 30 OR rental_rate <= 0.99 AND replacement_cost <= 9.99; 
''').fetchmany(10)
# pprint(sel15)

# IN. Найдем все фильмы с рейтингом R, NC-17
sel16 = connection.execute('''SELECT title, description, rating FROM film
WHERE rating IN ('R', 'NC-17'); 
''').fetchmany(10)
# pprint(sel16)

# NOT IN. Найдем фильмы недетского рейтинга, которых нет в 'G' и 'PG'
sel17 = connection.execute('''SELECT title, description, rating FROM film
WHERE rating NOT IN ('G', 'PG'); 
''').fetchmany(10)
# pprint(sel17)

# BETWEEN. Найдем фильмы с ценой проката между 0.99 и 2.99
sel18 = connection.execute('''SELECT title, rental_rate FROM film
WHERE rental_rate BETWEEN 0.99 AND 2.99; 
''').fetchmany(10)
# pprint(sel18)

# LIKE. Найдем фильмы, в описании которых есть слово 'Scientist'
sel19 = connection.execute('''SELECT title, description FROM film
WHERE description LIKE '%%Scientist%%'; 
''').fetchmany(10)
# pprint(sel19)

# Найдем id, имена, фамилии актеров, фамилия которых начинается с GEN
sel20 = connection.execute('''SELECT actor_id, first_name, last_name FROM actor
WHERE last_name LIKE '%%GEN%%'; 
''').fetchmany(10)
# pprint(sel20)

# ORDER BY. Отсортируем фильмы по цене проката
sel21 = connection.execute('''SELECT title, rental_rate FROM film
ORDER BY rental_rate; 
''').fetchall()
# pprint(sel21)

# Все то же самое, только добавим DESC и просортируем по убыванию
sel22 = connection.execute('''SELECT title, rental_rate FROM film
ORDER BY rental_rate DESC; 
''').fetchall()
# pprint(sel22)

# Сортируем по нескольким столбцам. По продолжительности и по цене проката
# Там где продолжительность одинаковая, будем сортировать по цене проката
sel23 = connection.execute('''SELECT title, length, rental_rate FROM film
ORDER BY length DESC, rental_rate DESC; 
''').fetchall()
# pprint(sel23)

# Найдем id, имена, фамилии актеров, чья фамилия содержит 'LI', отсортируем в алфавитном
# порядке по фамилии, затем по имени
sel24 = connection.execute('''SELECT actor_id, first_name, last_name FROM actor
WHERE last_name LIKE '%%LI%%'
ORDER BY last_name, first_name; 
''').fetchall()
# pprint(sel24)

# LIMIT. Выведем первые 15 записей
sel25 = connection.execute('''SELECT title, length, rental_rate FROM film
WHERE rental_rate > 2.99
ORDER BY length DESC, rental_rate
LIMIT 15; 
''').fetchall()
# pprint(sel25)

# Insert. Сначала проверим, что у нас находится в таблице rental
sel26 = connection.execute('''SELECT * FROM rental
''').fetchmany(10)
# pprint(sel26)

# Insert. Добавим новый прокат
sel27 = connection.execute('''INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id)
    VALUES(NOW(), 1, 3, 2);
''')
# pprint(sel27)
# Проверим
sel28 = connection.execute('''SELECT * FROM rental
    WHERE staff_id = 2 AND inventory_id =1;
''').fetchall()
# pprint(sel28)

# UPDATE. Добавим возврат из проката
sel29 = connection.execute('''UPDATE rental
        SET return_date = NOW()
        WHERE rental_id = 16059;
''')
# pprint(sel29)
# Проверим
sel30 = connection.execute('''SELECT * FROM rental
    WHERE staff_id = 2 AND inventory_id =1;
''').fetchall()
# pprint(sel30)

# # INSERT можно комбнировать с SELECT, чтобы скопировать данные из одной таблицы в другую
# INSERT INTO table2
# SELECT * FROM table1
# WHERE condition;

# DELETE. Удалим данные
sel31 = connection.execute('''DELETE FROM rental
    WHERE rental_id = 16062;
''')
# pprint(sel31)
# Проверим
sel32 = connection.execute('''SELECT * FROM rental
    WHERE rental_id = 16062;
''').fetchall()
# pprint(sel32)


#!/usr/bin/env python
# coding: utf-8
​
# In[1]:
​
​
​
​
# In[2]:
​
​
# создаем engine
engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/postgres')
engine
​
​
# In[3]:
​
​
con = engine.connect()
​
​
# Агрегирующие функции
​
# In[4]:
​
​
# найдем максимальную стоимость проката
con.execute("""
SELECT MAX(rental_rate) FROM film
""").fetchall()
​
​
# In[5]:
​
​
# посчитаем среднюю продолжительность фильма
con.execute("""
SELECT AVG(length) FROM film
""").fetchall()
​
​
# In[6]:
​
​
# сколько уникальных имен актеров?
con.execute("""
SELECT COUNT(DISTINCT first_name) FROM actor
""").fetchall()
​
​
# In[7]:
​
​
# посчитаем сумму продаж и среднюю продажу по конкретному продавцу
con.execute("""
SELECT SUM(amount), AVG(amount) FROM payment
WHERE staff_id = 1;
""").fetchall()
​
​
# In[ ]:
​
​
​
​
​
# Вложенные запросы
​
# In[8]:
​
​
# найдем все фильмы с продолжительностью ваше среднего
​
# так работать не будет
con.execute("""
SELECT title, length  FROM film
WHERE length >= AVG(length)
""").fetchall()
​
​
# In[9]:
​
​
con.execute("""
SELECT title, length FROM film
WHERE length >= (
    SELECT AVG(length) FROM film)
""").fetchall()
​
​
# In[10]:
​
​
# найдем названия фильмов, стоимость проката которых не максимальная
con.execute("""SELECT title, rental_rate FROM film
WHERE rental_rate < (SELECT MAX(rental_rate) FROM film)
ORDER BY rental_rate DESC
""").fetchall()
​
​
# Группировки
​
# In[11]:
​
​
# посчитаем количество актеров в разрезе фамилий (найдем однофамильцев)
con.execute("""
SELECT last_name, COUNT(*) FROM actor
GROUP BY last_name;
""").fetchall()
​
​
# In[12]:
​
​
# посчитаем количество фильмов в разрезе рейтингов (распределение рейтингов)
con.execute("""
SELECT rating, COUNT(title) FROM film
GROUP BY rating;
""").fetchall()
​
​
# In[13]:
​
​
# найдем максимальные продажи в разрезе продавцов
con.execute("""
SELECT staff_id, MAX(amount) FROM payment
GROUP BY staff_id;
""").fetchall()
​
​
# In[14]:
​
​
# найдем минимальные продажи каждого продавца каждому покупателю
con.execute("""
SELECT staff_id, customer_id, MIN(amount) FROM payment
GROUP BY staff_id, customer_id;
""").fetchall()
​
​
# In[15]:
​
​
# найдем среднюю продолжительность фильма в разрезе рейтингов в 2006 году
con.execute("""
SELECT rating, AVG(length) FROM film
WHERE release_year = 2006
GROUP BY rating;
""").fetchall()
​
​
# Оператор HAVING
​
# In[16]:
​
​
# отберем только фамилий актеров, которые не повторяются
con.execute("""
SELECT last_name FROM actor
GROUP BY last_name
HAVING COUNT(last_name) = 1;
""").fetchall()
​
​
# In[17]:
​
​
# отберем и посчитаем только фамилии актеров, которые повторяются
con.execute("""
SELECT last_name, COUNT(last_name) FROM actor
GROUP BY last_name
HAVING count(last_name) > 1;
""").fetchall()
​
​
# In[18]:
​
​
# найдем фильмы, у которых есть SUPER в названии и они сдавались в прокат суммарно более, чем на 5 дней
con.execute("""
SELECT title, SUM(rental_duration) FROM film
WHERE title LIKE '%%SUPER%%'
GROUP BY title
HAVING SUM(rental_duration) > 5;
""").fetchall()
​
​
# ALIAS
​
# In[19]:
​
​
# Предыдущий запрос с псевдонимами
con.execute("""
SELECT title t, SUM(rental_duration) sum_t FROM film f
WHERE title LIKE '%%SUPER%%'
GROUP BY t
HAVING SUM(rental_duration) > 5;
""").fetchall()
​
​
# Объединение таблиц
​
# In[20]:
​
​
# выведем имена, фамилии и адреса всех сотрудников
con.execute("""
SELECT first_name, last_name, address FROM staff s
LEFT JOIN address a ON s.address_id = a.address_id;
""").fetchall()
​
​
# In[21]:
​
​
# определим количество продаж каждого продавца
con.execute("""
SELECT p.staff_id, COUNT(amount) FROM payment p
LEFT JOIN staff s ON p.staff_id = s.staff_id
GROUP BY p.staff_id;
""").fetchall()
​
​
# In[22]:
​
​
# посчитаем, сколько актеров играло в каждом фильме
con.execute("""
SELECT title, COUNT(actor_id) FROM film f
JOIN film_actor a ON f.film_id = a.film_id
GROUP BY f.title;
""").fetchall()
​
​
# In[ ]:
​
​
​
​
​
# In[ ]:
​
​
​
​
​
# In[23]:
​
​
# сколько копии фильмов со словом SUPER в названии есть в наличии
con.execute("""
SELECT title, COUNT(inventory_id) FROM film f
JOIN inventory i ON f.film_id = i.film_id
WHERE f.title LIKE '%%SUPER%%'
GROUP BY title;
""").fetchall()
​
​
# In[24]:
​
​
# выведем список покупателем с количеством их покупок в алфивитной порядке
con.execute("""
SELECT c.last_name, COUNT(p.amount) amount FROM customer c
LEFT JOIN payment p ON c.customer_id = p.customer_id
GROUP BY  c.last_name;
""").fetchall()
​
​
# In[25]:
​
​
# выведем имена и почтовые адреса всех покупателей из России
con.execute("""
SELECT c.last_name, c.first_name, c.email FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ON a.city_id = city.city_id
JOIN country co ON city.country_id = co.country_id
WHERE country = 'Russian Federation';
""").fetchall()
​
​
# In[26]:
​
​
# фильмы, которые берут в прокат чаще всего
con.execute("""
SELECT f.title, COUNT(r.inventory_id) count FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY  f.title
ORDER BY  count DESC;
""").fetchall()
​
​
# In[27]:
​
​
# суммарные доходы магазинов
con.execute("""
SELECT s.store_id, SUM(p.amount) sales FROM store s 
JOIN staff st ON s.store_id = st.store_id
JOIN payment p ON st.staff_id = p.staff_id
GROUP BY s.store_id;
""").fetchall()
​
​
# In[28]:
​
​
# найдем города и страны каждого магазина
con.execute("""
SELECT store_id, city, country FROM store s 
JOIN address a ON s.address_id = a.address_id
JOIN city ON a.city_id = city.city_id
JOIN country c ON city.country_id = c.country_id;
""").fetchall()
​
​
# In[29]:
​
​
# выведем топ-5 жанров по доходу
con.execute("""
SELECT c.name, SUM(p.amount) revenue FROM category c 
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY  revenue DESC 
LIMIT 5;
""").fetchall()
​
​
# In[ ]:
​
