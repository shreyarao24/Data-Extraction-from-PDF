import pandas

f = pandas.read_csv('C:/Users/Shreya/Desktop/file-name.csv', header = None)

final = pandas.DataFrame(columns = ['Sr No.', 'Name', 'Student ID', 'Gender', 'Grade'])

for i in range(0, len(f), 2):
    r1 = f.iat[i, 0].split(' ')
    while r1.count('') > 0:
        r1.remove('')
    
    r2 = f.iat[i+1, 0].split(' ')
    while r2.count('') > 0:
        r2.remove('')
        
    r = r1 + r2

    sr_no = r[0]
    
    if r[9].isnumeric():
        sid = '*' + r[1] + r[2] + r[9]
    else:
        sid = '*' + r[1] + r[2] + r[10]
    
    name = r[3] + ' ' + r[4]
    
    if 'BOY' in r:
        gender = 'BOY'
    else:
        gender = 'GIRL'
        
    if r[7].isnumeric():
        grade = r[7]
    else:
        grade = r[8]
    
    l = [sr_no, name, sid, gender, grade]
    final.loc[len(final)] = l
    
final.to_csv('C:/Users/Shreya/Desktop/files/file-name.csv')