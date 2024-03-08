from search import search

# Create a FileSearch object with quiet=False (not suppressing output) and find the string "SomeString" in the current directory
fs = search.FileSearch(quiet=False).FindString("/home/evil_rc/Desktop", "SomexString")

# Print the return code of the search (True if found, False otherwise)
print(f"Search return code: {fs}")

# Check if the search was successful
if fs:
    print("Found successfully.")
else:
    print("Not Found.")
