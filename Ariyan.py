import os, sys

try:

    __import__("CY_enc").main()

except Exception as e:

    exit(str(e))

 
