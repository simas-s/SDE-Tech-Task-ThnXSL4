-- Avg daily temp for each city, entries are grouped by city, with an average temperature being calculated across each
-- group.
SELECT country_code, state_code, city_name,
  AvG(temp) AS average_daily_temp
FROM raw.daily_weather
WHERE date <= DATE(2024, 1, 7)
GROUP BY city_name, state_code, country_code
ORDER BY country_code, state_code


-- Avg daily humidity in each city
SELECT country_code, state_code, city_name,
  AVG(humidity) AS avg_daily_humidity
FROM raw.daily_weather
GROUP BY country_code, state_code, city_name
QUALIFY RANK() OVER (PARTITION BY state_code ORDER BY AVG(humidity) DESC) <=3

--Find the percentage of cities in each state experiencing "rain" as the weather condition.
SELECT country_code, state_code,
  SUM(CASE WHEN condition = "Rain" THEN 1 ELSE 0 END) * 100 / COUNT(*) AS cities_in_rain
FROM raw.daily_weather
GROUP BY country_code, state_code