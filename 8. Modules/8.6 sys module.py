#sys module provides access to some variables used or maintained by interpreter.

import sys
for i in sys.path:
    print(i)
    
print(sys.version)