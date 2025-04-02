-- Avg daily temp for each city, entries are grouped by city, with an average temperature being calculated across each
-- group.
SELECT country_code, state_code, city_name,
  AvG(temp) AS average_daily_temp
FROM raw.daily_weather
WHERE date <= DATE(2024, 1, 7)
GROUP BY city_name, state_code, country_code
ORDER BY country_code, state_code