import compileall
import glob


def show(title):
    print(title)
    for filename in glob.glob('examples/**',
                              recursive=True):
        print('  {}'.format(filename))
    print()


show('Before')

compileall.compile_dir('examples')

show('\nAfter')
