import pandas

f = pandas.read_csv('C:/Users/Shreya/Desktop/file-name.csv', header = None)

# dropping duplicate rows - since headers were repeated on every new page of the pdf
f.drop_duplicates(keep = 'first', inplace = True)

# creating a new dataframe
final = pandas.DataFrame(columns = ['Sr No.', 'Name', 'Student ID', 'Gender'])

for row in f.itertuples():
    r = str(row[1]).split(' ')
    
    while r.count('') > 0:
        r.remove('')
      
    if r[0].isnumeric() and len(r) > 1:
        sr_no = r[0]
        
        for i in range(0, len(r)):
            if len(r[i]) == 3 and r[i].isnumeric() and len(r[i+1]) == 3 and r[i+1].isnumeric():
                sid = '*' + r[i] + r[i+1] + r[i+2]
                break

    
        name = r[1]
        if r[2].isalpha():
            name = name + ' ' + r[2]
        
        if 'BOY' in r:
            gender = 'BOY'
        else:
            gender = 'GIRL'
        
        l = [sr_no, name, sid, gender]
        final.loc[len(final)] = l
        
final.to_csv('C:/Users/Shreya/Desktop/files/file-name.csv')