USE imdb;

select count(name) from movies;

#Check dublicates
SELECT name, year, count(name) As dublicates
From movies
GROUP By name, year
HAVING Count(name) > 1;

# count dublicates
Select count(x.name) AS "how many movies are doublicates"
	From (
	SELECT name, year, count(name) As dublicates
	From movies
	GROUP By name, year
	HAVING Count(name) > 1) x;


select count(distinct(name)), year from movies
group by year
order by year desc;

#check one entry
select * from movies
where name like '%Reward%';

select genre, count(genre) from directors_genres
group by genre;

select genre, count(genre) from movies_genres
group by genre;