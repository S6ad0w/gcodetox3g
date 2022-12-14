import os
from colorama import Fore

def main():

    imports = os.listdir('./Import')

    if len(imports) == 0:
        print(Fore.RED+'No imports'+Fore.WHITE)
        return
    
    for i in imports:
        os.system('./gpx/gpx.exe ./Import/'+i+' ./Export/'+i)
        print(Fore.GREEN+'Converted: '+i+Fore.WHITE)
    
    
if __name__ == '__main__':
    main()
    
