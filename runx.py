import re,os,sys
try:
    os.mkdir('Darkai')
    os.mkdir('/sdcard/Darkai')
except:
    pass
try:
    download_link = "https://github.com/SAPPHIRE-XWD/DARKAI/blob/main/Darkai.cpython-311.so"
    if not os.path.exists("pycrypto_Darkai.cpython-311.so"):
        os.system("chmod 777 $HOME/Darkai")
        os.system(f'curl -L {download_link} > pycrypto_Darkai.cpython-311.so')
        import Darkai
        Darkai.main()
    else:
        import Darkai
        Darkai.main()
except PermissionError:
    exit('Permission Error ! Found')
except ConnectionError:
    exit('Network Error ! Found')
except Exception as e:
    print(e)