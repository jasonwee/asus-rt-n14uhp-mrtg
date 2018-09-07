import compileall
import re

compileall.compile_dir(
    'examples',
    maxlevels=0,
)

