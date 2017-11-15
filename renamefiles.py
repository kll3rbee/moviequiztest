import os
def rename_files():
	# show files
	file_list = os.listdir('/Users/dondave/Documents/codes/moviequiztest/prank')
	# print file_list
	dirpath = os.getcwd()
	# print (dirpath)
	os.chdir('/Users/dondave/Documents/codes/moviequiztest/prank')
	# rename files
	for files in file_list:
		os.rename(files, files.translate(None, '0123456789'))
	os.chdir(dirpath)

rename_files()