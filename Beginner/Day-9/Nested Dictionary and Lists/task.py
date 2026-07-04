capitals = {"France": "Paris", "Germany": "Berlin"}

# nested lists in dictionaries:

# travel_vlog={
#     "France":["Paris","Monaco","Lille"],
#     "Germany":["Berlin","Munich","Frankfurt"]
# }

# print Lille
# print(travel_vlog["France"][2])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
print(nested_list[2][0])

# dictionary inside a dictionary

travel_vlog = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Nice", "Lyon", "Lille"],
    },
    "Germany": {"cities_visited": ["Berlin", "Munich", "Frankfurt"], "total_visits": 5},
}

print(travel_vlog["Germany"]["cities_visited"][2])
