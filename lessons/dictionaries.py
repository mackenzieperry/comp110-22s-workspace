"""Demonstrations of dictionaries capabilites."""

schools: dict[str, int]

schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print dictionary literal
print(schools)

# look up, access a key by its value
print(f"UNC has {schools['UNC']} students")

# remove a key vlaue pair from a dictionary by its key
schools.pop("Duke")

# Test for existance of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# update / reasssigne key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# empty dictionary literal
schools = {}

# Initialize key value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}

# Trying to access a key that does not exist
# gives you a keyError print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")