#!C:\Users\apple\PycharmProjects\����\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'wxpy==0.3.9.8','console_scripts','wxpy'
__requires__ = 'wxpy==0.3.9.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('wxpy==0.3.9.8', 'console_scripts', 'wxpy')()
    )
