import tarfile

with tarfile.open('example.tar', 'r') as t:
    print(t.getnames())

