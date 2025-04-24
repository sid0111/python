
try:
    with open("sid", "r") as file:
        content = file.read()

# except FileNotFoundError:
#     print("File not found!")

except Exception as e:
    print("Unknown exception ",e)

else: #executes only when there is no error
    print("file read sucessfully!")
    print(f"File content : \n{content}")

finally: # always executed
    print("EOP")