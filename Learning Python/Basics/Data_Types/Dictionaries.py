# Examples of dictionaries

# Create
user = {"first_name":"Ada"}
print(user)

# Read
user = {"first_name":"Ada"}
print(user["first_name"])

# Update
user["family_name"] = "Byron"
print(user)

user["family_name"] = "Lovelace"
print(user)

# Delete
del user["family_name"]
print(user)


