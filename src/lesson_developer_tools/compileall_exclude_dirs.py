import compileall
import re

compileall.compile_dir(
    'examples',
    rx=re.compile(r'/subdir'),
)

