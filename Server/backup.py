import os
import zipfile
import datetime
import shutil
def main():
	
	#zipf = zipfile.ZipFile('~/backup/ODBackup-' + str(datetime.datetime.now()).replace(' ', '').replace(':' ,'-')+ '.zip', 'w')
	shutil.make_archive('~/backup/ODBackup-' + str(datetime.datetime.now()).replace(' ', '').replace(':' ,'-'), 'zip', '/home/ubuntu/OneDir/Files/') 


if __name__ == '__main__':
	main()
