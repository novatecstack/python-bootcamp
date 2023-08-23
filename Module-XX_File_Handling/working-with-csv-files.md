# Working with Files using Python

In this module, you will learn how you can perform below actions on a text file using Python:
  - Import .csv module
  - Open a .csv file
  - Read a .csv file
  - Write to a text file
  - Create a new text file

## [Import `.csv module`](https://docs.python.org/3/library/csv.html)
   
   ```
   import csv

   ```

## [Open a `.csv file` using Python](https://docs.python.org/3/library/functions.html?highlight=built%20functions#open)
   
   ```
   import csv

   # Opening a .csv file in read-only mode
   fileObj = open("samplefile.csv","r")

   ```

## [Read a `.csv file` using Python]()
   
   ```
   # Import the csv module
   import csv

   # Open a .csv file in read-only mode
   fileObj = open("samplefile.csv","r")


   # Reading a .csv file
   file_reader = csv.reader(fileObj, delimeter=",")

   for row in file_reader:
       print(row)
   
   ```

## [Close a `.csv file` using Python]()

   ```
   # Import the csv module
   import csv

   # Open a .csv file in read-only mode
   fileObj = open("samplefile.csv","r")

   # Close a .csv file
   fileObj.close()
   
   ```
## [Write to the .csv file]()
   
   ```
   # Import the csv module
   import csv

   # Define a new row contents to be added to the existing csv file
   newRow = ["200", "Bindesh", "Python", "C13453"]
   
   # Open an existing csv file to write into it
   fileObj = open("samplefile.csv","a")

   # Define the csv writer object
   wrt_obj = csv.writer(fileObj)

   # Write to csv file
   write_obj.writerow(newRow)

   # Close the csv file
   file.close()

   ```