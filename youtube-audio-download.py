import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system('clear')

try:
    input = input(bcolors.FAIL + bcolors.BOLD + 'Have you added urls to file videos-to-download.txt? ')
    if input.lower() == 'y':
        with open('videos-to-download.txt', 'r') as f:
            videos = f.readlines()
            
        if len(videos) != 0:
            print(bcolors.OKBLUE + 'downloading the following videos (total '+ str(len(videos)) + '): ')
            for url in videos:
                print(url)

            for idx,url in enumerate(videos):
                print(bcolors.OKGREEN)
                print('\nDownloading item #' + str(idx + 1) + ' of ' + str(len(videos)) + ' total items')
                print(url)
                os.system('youtube-dl -o \'%(title)s.%(ext)s\' -x --audio-format mp3 ' + url)
                
            print(bcolors.WARNING + '\nItems downloaded successfully')
        else:
            print(bcolors.FAIL + '\nPlease add your video urls first...')
    else: 
        print(bcolors.FAIL + '\nPlease add your video urls first...')
except KeyboardInterrupt:
    sys.exit(0) # or 1, or whatever
finally:
    print(bcolors.ENDC)