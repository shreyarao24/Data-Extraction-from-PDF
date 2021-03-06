# Data Extraction from PDFs using Python

## Introduction

This project involved extracting data from multiple PDF files and converting them to CSV files for easier use and manipulation. Using a combination of these 3 custom algorithms, data was extracted from 11 different PDF files.

The PDF files contained information on students from 11 different schools. To ensure their privacy is protected, all file names have been replaced with generic placeholders and any visible information in the screenshots of the PDFs (provided for context) has been blacked out.

## Premilinary Extraction

First, the PDFs were converted into text files using XpdfReader. XpdfReader (https://www.xpdfreader.com/) has multiple applications that can be accessed through the command prompt. 

1. Download XpdfReader and unzip the file. The doc folder contains all documentation for the different XpdfReader applications, and the bin32 folder contains all the applications.
2. Create a new folder called 'test' and copy the pdftotext application from the bin32 folder to the test folder. This folder should contain nothing but the pdftotext application and the PDF file you wish to convert.
3. Using the command prompt, navigate to your test folder and use the pdftotext application to convert your PDF file to a text file. There are many different options to choose from to decide the layout of your text file (which are outlined in the documentation). I used the 'table' option so that when created, all the columns in my text file would be aligned.

```
C:\Users\Shreya>cd Desktop/test

C:\Users\Shreya\Desktop\test>pdftotext -table pdf-file.pdf text-file.txt
```
4. The new text file is created and stored within your test folder.

After getting the text file, I used OpenRefine to convert my text file into a CSV file. 

1. Download OpenRefine (https://openrefine.org/) and open the application. It should open in your browser.
2. Upload your newly created text file, and customize as you wish. I chose to save it with comma seperated values, and did not store any blank rows. 
3. Use the facet tool to filter out any specific rows. Since all of my PDF files were rather small (400-500 rows of data), I was able to manually check for empty rows and flag them. Then, I faceted all flagged rows and removed them. 
4. Export your cleaned text file as a .csv file.

Although the data has now been successfully converted into a .csv file, it is still very messy. Although our text file had the data organized into columns, when exported by OpenRefine, each row of data was compressed into a single column. 

<img src="images/Screenshot 2021-02-21 130526.png">

Furthermore, the data was not present on a single line either - in many cases, the data for each student was stored on 2 rows, or even 4 rows. 

To extract data from the raw CSV file, I used the pandas module in Python 3. I had to create 3 different algorithms based on the structure of the PDF file.

## Algorithm #1

The first PDF was orgnaized like this - 

<img src="Screenshot 2021-02-23 175644">

The data for each student was present on only a single row, so it was easy to extract the required data, which was - the serial number, the name, the student ID, the gender, and the grade. 


To access rows one at a time, I looped through the dataframe using **pandas.DataFrame.itertuples()**, and then split each row into a list. The serial number was the first element in each row, so we had to access only the firt element:

```
sr_no = r[0]
```

The student ID was separated into 3 parts, since the 





