-- Top 3 city humidities per state
SELECT country_code, state_code, city_name,
  AVG(humidity) AS avg_daily_humidity
FROM raw.daily_weather
WHERE date <= DATE(2024, 1, 7)
GROUP BY country_code, state_code, city_name
QUALIFY RANK() OVER (PARTITION BY state_code ORDER BY AVG(humidity) DESC) <=3