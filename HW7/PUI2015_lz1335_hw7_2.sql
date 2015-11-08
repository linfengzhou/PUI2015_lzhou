SELECT start_station_id, start_station_name,  CDB_TransformToWebmercator(CDB_LatLng(
  start_station_latitude, 
  start_station_longitude)) 
as the_geom_webmercator, 
SUM(tripduration) AS trip_count 

FROM citibike

WHERE ST_Dwithin(CDB_LatLng(
  start_station_latitude,
  start_station_longitude
)::geography,
       CDB_LatLng(40.7307602,-73.9974086)::geography,
           1000)

GROUP BY
start_station_id,
start_station_name,
start_station_latitude,
start_station_longitude;
