import os

folder = input('Enter folder name: ')
# check for valid folder name
if os.path.isdir(folder):
    filename = input('Enter file name: ') # read file name
    file = folder + "\\" + filename # create the fully qualified file name
    name = input('Enter user name: ') # read name
    address = input('Enter address: ') # read address
    phone = input('Enter phone number: ') # read phone
    # code to write the data to the file
    outfile = open(file, 'w')
    print(f'{name},{address},{phone}', file=outfile)
    outfile.close()
    # code to read the data to the file
    infile = open(file, 'r')
    data = infile.readline().strip().split(',')
    # display the file contents to the user for validation purposes.
    print(f'Your name: {data[0]}')
    print(f'Your address: {data[1]}')
    print(f'Your phone: {data[2]}')
    infile.close()

else:
    print(f'Error: {folder} do not exist.')