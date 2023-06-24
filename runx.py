import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://www.facebook.com/profile.php?id=100057149474543')

bit = platform.architecture()[0]
if bit == '64bit':
    import Darkai
elif bit == '32bit':
    import Darkai