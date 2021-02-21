import pandas
import re

f = pandas.read_csv('C:/Users/Shreya/Desktop/file-name.csv')

# creating a new dataframe to store all extracted data
final = pandas.DataFrame(columns = ['Sr No.', 'Name', 'Student ID', 'Gender', 'Grade'])

# looping through each row in the dataframe
for row in f.itertuples():
    #splitting the information, which was stored as a string, into a list
    r = row[1].split(' ')
    
    # removing any empty strings in the list
    while r.count('') > 0:
        r.remove('')
    
    # extracting required information
    sr_no = r[0]
    sid = '*' + r[1] + r[2] + r[3]
    grade = r[4]
    
    if len(re.sub('[^a-zA-Z]+', '', r[5])) <= 2:
        name = re.sub('[^a-zA-Z]+', '', r[5]) + ' ' + re.sub('[^a-zA-Z]+', '', r[6])
    else:
        name = re.sub('[^a-zA-Z]+', '', r[5])
        
    if 'BOY' in r:
        gender = 'BOY'
    else:
        gender = 'GIRL'
        
    l = [sr_no, name, sid, gender, grade]
    # adding the final data to our new dataframe
    final.loc[len(final)] = l
    
# converting our pandas dataframe to a .csv file
final.to_csv('C:/Users/Shreya/Desktop/files/file-name.csv')
