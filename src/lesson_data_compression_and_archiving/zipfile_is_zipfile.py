import zipfile

for filename in ['README.txt', 'example.zip',
                 'bad_example.zip', 'notthere.zip']:
    print('{:>15}  {}'.format(
        filename, zipfile.is_zipfile(filename)))
