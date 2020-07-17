import os
host= "http://49.235.92.12:8020"
os.environ["host"] = "http://49.235.92.12:8020"
print(os.environ["host"])