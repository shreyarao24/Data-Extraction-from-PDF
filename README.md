# Data Extraction from PDFs using Python

## Introduction

This project involved extracting data from multiple PDF files and converting them to CSV files for easier use and manipulation. Using a combination of these 3 custom algorithms, data was extracted from 11 different PDF files.

The PDF files contained information on students from 11 different schools. To ensure their privacy is protected, all file names have been replaced with generic placeholders and any visible information in the screenshots of the PDFs (provided for context) has been blacked out.

## Premilinary Extraction

First, the PDFs were converted into text files using XpdfReader. XpdfReader (https://www.xpdfreader.com/) has multiple applications that can be accessed through the command prompt. 

1. Download XpdfReader and unzip the file. The doc folder contains all documentation for the different XpdfReader applications, and the bin32 folder contains all the applications.
2. Create a new folder called 'test' and copy the pdftotext application from the bin32 folder to the test folder. This folder should contain nothing but the pdftotext application and the PDF file you wish to convert.
3. Using the command prompt, navigate to your test folder and use the pdftotext application to convert your PDF file to a text file. There are many different options to choose from to decide the layout of your text file (which are outlined in the documentation). I used the 'table' option so that all the columns in my PDF file are aligned in my text file.

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



## Algorithm #1
