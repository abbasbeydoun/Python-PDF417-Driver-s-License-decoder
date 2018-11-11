f = open('dlstring.txt', 'r')

dlstring = f.read()

f.close()

dlstringarray = dlstring.split('\n')
dlstringarray = dlstringarray[2:]
dlstringarray = [line.strip() for line in dlstringarray]

# remove 'ANSI' from first element (It's a fixed header)
dlstringarray[0] = dlstringarray[0][5:]

metadata = dlstringarray[0]

dlstringarray.remove(metadata)

decodedfile = open('dlstringdecoded.txt', 'w')

IIN = metadata[0:6]  # Issuer Identification Number
AAMVAV = metadata[6:8]  # AAMVA Version number
JV = metadata[8:10]  # Jurisdiction Version number
entries = metadata[10:12]  # Number of entries

DL = metadata[12:14]

offset = metadata[14:18]  # offset for this subfile
subfile_length = metadata[18:22]

DCA = metadata[27:]  # Jurisdiction specific vehicle class

decodedfile.write('Issuer Identification Number: ' + IIN + "\n")
decodedfile.write('AAMVA Version Number: ' + AAMVAV + "\n")
decodedfile.write('Jurisdiction Version Number: ' + JV + "\n")
decodedfile.write('Number of entries: ' + entries + "\n")
decodedfile.write('Type: ' + DL + "\n")
decodedfile.write('Offset for subfile: ' + offset + "\n")
decodedfile.write('Subfile length: ' + subfile_length + "\n")
decodedfile.write('Jurisdiction specific vehicle class : ' + DCA + "\n")

print(dlstringarray)

for field in dlstringarray:

    fieldID = field[0:3]
    fieldValue = field[3:]

    if fieldID == 'DCB':
        decodedfile.write('Jurisdiction specific restriction codes: ')
    elif fieldID == 'DCD':
        decodedfile.write('Jurisdiction specific endorsement codes: ')
    elif fieldID == 'DBA':
        decodedfile.write('Document Expiration date: ')
    elif fieldID == 'DCS':
        decodedfile.write('Customer Family Name: ')
    elif fieldID == 'DCT':
        decodedfile.write('Customer Given Name: ')
    elif fieldID == 'DBD':
        decodedfile.write('Document Issue Date: ')
    elif fieldID == 'DBB':
        decodedfile.write('Date of Birth: ')
    elif fieldID == 'DBC':
        decodedfile.write('Sex: ')  # 1 for male, 2 for female
    elif fieldID == 'DAY':
        decodedfile.write('Eye Color: ')
    elif fieldID == 'DAU':
        decodedfile.wriote('Height: ')
    elif fieldID == 'DAG':
        decodedfile.write('Address Line 1: ')
    elif fieldID == 'DAI':
        decodedfile.write('City: ')
    elif fieldID == 'DAJ':
        decodedfile.write('State: ')
    elif fieldID == 'DAK':
        decodedfile.write('Postal Code: ')
    elif fieldID == 'DAQ':
        decodedfile.write('Customer ID Number: ')
    elif fieldID == 'DCF':
        decodedfile.write('Document Discriminator: ')
    elif fieldID == 'DCG':
        decodedfile.write('Country Identification: ')
    elif fieldID == 'DCK':
        decodedfile.write('Inventory control number: ')

    decodedfile.write(fieldValue + "\n")