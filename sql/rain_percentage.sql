--Find the percentage of cities in each state experiencing "rain" as the weather condition.
SELECT country_code, state_code,
  SUM(CASE WHEN condition = "Rain" THEN 1 ELSE 0 END) * 100 / COUNT(*) AS cities_in_rain
FROM raw.daily_weather
WHERE date <= DATE(2024, 1, 7)
GROUP BY country_code, state_code