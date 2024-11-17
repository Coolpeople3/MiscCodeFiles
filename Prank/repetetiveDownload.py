# Loop to create two text files

while 1<2:
    for i in range (2):
        # Create the filename
        filename = f'text_file_{i + 1}.txt'
    
        # Create the content for the text file
        content = f'This is text file number {i + 1}.'
    
        # Write the content to the file
        with open(filename, 'w') as file:
            file.write(content)
    
         # Print confirmation
        print(f'{filename} created.')
