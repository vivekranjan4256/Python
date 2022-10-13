travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris","Lille","DIjon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin","Hamburg","Stuttgart"]
    },
]

def add_new_country(country,visits,list):
    new_country={"country":country,"visits": visits,"cities": list}
    travel_log.append(new_country)

add_new_country("Russia",2,["Moscow","Saint Petersburgh"])
print(travel_log)