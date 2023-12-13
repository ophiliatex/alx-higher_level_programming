-- display max temperature for every state in of order by name
SELECT state,
    MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
