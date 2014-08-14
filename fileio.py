"""Operations having to do with files."""

def get_reader(filename):
    """returns a reader"""



def get_writer(filename, headers=False):
    """takes a filename and returns a writer for that file type"""

def combine_data(*filenames):
    """Takes a list of filenames, with the last file being the newly combined file, and combines the files into one file."""
    newfilename = filenames[-1]
    oldfilenames = filenames[0:-1]

    i = 0
    newfile = open(newfilename,'w')
    for filename in oldfilenames:
        #Loop through each file and append the results to the new file
        with open(filename, 'r') as oldfile:
            #reader
            reader = get_reader(oldfile)
            
            #
            writer = get_writer(newfile, headers)
            if(i==0): writer.writeheader()

            # Write the data for each row to the file
            for row in reader:
                try:
                    writer.writerow(row)
                except:
                    print("ROW NOT WRITTEN: "+str(row))
                    pass
        i+=1
