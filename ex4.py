import csv

try:
    # open csv file and make a reader object
# iterate over the reader object and print cols that contain name and address 
    with open("staff_details.csv", newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        for col in reader:
            if col[0] == "":
                raise Exception() 
            else:
                print(col[1], ",", col[3])

except FileNotFoundError:
    print("The specified file does not exist")

except Exception:
    print("Staff ID is missing in record")      
       