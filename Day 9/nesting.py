capitals={
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a dictionary

travel_log={
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg", "Stuttgart"],
}

#Nesting dictionary in a dictionary

travel_log={
    "France": {"Paris":1,
    "Lille":2,
    "Dijon":3},

    "Germany": ["Berlin","Hamburg", "Stuttgart"],
}

#Nesting dictionary in a list

travel_log=[
    {
    "Key": ["a","b"],
    "Key2":  {"Dict1": 1}
    },
    {
    "Key3": "Value3",
    "Key4": "Value4",
    }
            ]