SELECT 
start_station_id, 
start_station_name,
end_station_id,
end_station_name, 
COUNT(tripduration) AS trip_count

FROM citibike

GROUP BY 
start_station_id,
start_station_name,
end_station_id,
end_station_name

ORDER BY 
trip_count DESC

LIMIT 5

