SELECT 
start_station_id, 
start_station_name,
end_station_id,
end_station_name, 
SUM(tripduration) AS trip_count

FROM citibike

GROUP BY 
start_station_id,
start_station_name,
end_station_id,
end_station_name;