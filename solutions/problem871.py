class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        stations.append([target, 0])
        list_of_skipped_gas_stations = []
        fuel = startFuel
        station_counter = 0
        station_index = 0
        while station_index < len(stations):
            station = stations[station_index]
            station_position, fuel_station = station
            if fuel < station_position:
                if len(list_of_skipped_gas_stations) == 0:
                    return -1
                max_gas = max(list_of_skipped_gas_stations)
                fuel += max_gas
                station_counter += 1
                list_of_skipped_gas_stations.pop(list_of_skipped_gas_stations.index(max_gas))
            else:
                list_of_skipped_gas_stations.append(fuel_station)
                station_index += 1
        return station_counter
    
s = Solution()
print(s.minRefuelStops(target = 1, startFuel = 1, stations = []))