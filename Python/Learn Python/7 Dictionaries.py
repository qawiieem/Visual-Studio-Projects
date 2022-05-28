monthConversions = {                #remember the format for dictionaries
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sept" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConversions["Mar"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Luv", "Not a valid key"))
print(monthConversions.get("Hye"))
