#!E:\users\lenovo\PycharmProjects\untitled\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: '3color-Press==0.2.1','console_scripts','3color'
__requires__ = '3color-Press==0.2.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('3color-Press==0.2.1', 'console_scripts', '3color')()
    )
