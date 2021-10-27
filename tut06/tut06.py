import re
from os import name
import os.path
import shutil
def regex_renamer():

	# Taking input from the user
	dir = "corrected_srt"
	dirpath = os.path.join(dir)
	dirpath_wrong = os.path.join("wrong_srt")
	if os.path.isdir(dirpath)==False:
		os.mkdir("corrected_srt")

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))
	# ----------------------------------------------------------------------
	# For Breaking Bad
	# ----------------------------------------------------------------------
	if webseries_num == 1:
		webseries = "Breaking Bad"
		dir_corrected_srt = os.path.join(dirpath,webseries)
		dir_wrong_srt = os.path.join(dirpath_wrong,webseries)
		# Checking if the series folder is present in corrected_srt folder or not, if it is present then removing the folder and then copying the fresh series folder from wrong_srt to corrected_srt. 
		if os.path.isdir(dir_corrected_srt)==True:
			shutil.rmtree(dir_corrected_srt)
		shutil.copytree(dir_wrong_srt,dir_corrected_srt)
		# Breaking Bad s01e01 720p.BRrip.Sujaidr.mp4
		x = os.listdir(dir_corrected_srt)
		# Traversing in every file in the series folder
		for i in x:
			# Removing unwanted strings and storing file name parts in a list 
			clean = re.split(' 720p.BRrip.Sujaidr',i)
			pattern = re.compile('\d+')
			temp = re.findall(pattern,clean[0])
			season = int(temp[0])
			season = str(season)
			episode = int(temp[1])
			episode = str(episode)
			extension = clean[1]
			# print(season,episode)
			# print(len(season),len(episode))
			
			s_p = season_padding
			e_p = episode_padding
			# Applying padding to season and episode numbers
			while s_p>len(season):
				season = '0' + season 
			while e_p>len(episode):
				episode = '0' + episode
			# print('after padding')
			# print(season,episode)
			# print('Breaking Bad '+'Season '+season+' Episode '+episode+extension)
			new_name = 'Breaking Bad '+'Season '+season+' Episode '+episode+extension
			# Renaming new files
			os.rename(dir_corrected_srt+'/'+i,dir_corrected_srt+'/'+new_name)
	# ------------------------------------------------------------------------
	# For Game of Thrones
	# ------------------------------------------------------------------------
	if webseries_num == 2:
		webseries = "Game of Thrones"
		dir_corrected_srt = os.path.join(dirpath,webseries)
		dir_wrong_srt = os.path.join(dirpath_wrong,webseries)
		# Checking if the series folder is present in corrected_srt folder or not, if it is present then removing the folder and then copying the fresh series folder from wrong_srt to corrected_srt. 
		if os.path.isdir(dir_corrected_srt)==True:
			shutil.rmtree(dir_corrected_srt)
		shutil.copytree(dir_wrong_srt,dir_corrected_srt)
		# Game of Thrones - 8x01 - Winterfell.WEB.REPACK.MEMENTO.en.mp4
		x = os.listdir(dir_corrected_srt)
		# Traversing in every file in the series folder
		for i in x:
			# Removing unwanted strings and storing file name parts in a list
			clean = re.split('.WEB.REPACK.MEMENTO.en',i)
			# print(clean)
			pattern = re.compile('\d+')
			temp = re.findall(pattern,clean[0])
			season = int(temp[0])
			season = str(season)
			episode = int(temp[1])
			episode = str(episode)
			extension = clean[1]
			clean = re.split('Game of Thrones - ' + '\d+'+'x'+'\d+' + ' - ',clean[0])
			epi_name = clean[1]
			# print(season,episode)
			# print(len(season),len(episode))
			
			s_p = season_padding
			e_p = episode_padding
			# Applying padding to season and episode numbers
			while s_p>len(season):
				season = '0' + season 
			while e_p>len(episode):
				episode = '0' + episode
			# print('after padding')
			# print(season,episode)
			# print('Game of Thrones - '+'Season '+season+' Episode '+episode+' - '+epi_name+extension)
			new_name = 'Game of Thrones - '+'Season '+season+' Episode '+episode+' - '+epi_name+extension
			# Renaming new files
			os.rename(dir_corrected_srt+'/'+i,dir_corrected_srt+'/'+new_name)
	# ------------------------------------------------------------------------
	# For Lucifer
	# ------------------------------------------------------------------------
	if webseries_num == 3:
		webseries = "Lucifer"
		dir_corrected_srt = os.path.join(dirpath,webseries)
		dir_wrong_srt = os.path.join(dirpath_wrong,webseries)
		# Checking if the series folder is present in corrected_srt folder or not, if it is present then removing the folder and then copying the fresh series folder from wrong_srt to corrected_srt. 
		if os.path.isdir(dir_corrected_srt)==True:
			shutil.rmtree(dir_corrected_srt)
		shutil.copytree(dir_wrong_srt,dir_corrected_srt)
		# Lucifer - 6x01 - Nothing Ever Changes Around Here.HDTV.CAKES.en.mp4
		x = os.listdir(dir_corrected_srt)
		# Traversing in every file in the series folder
		for i in x:
			# Removing unwanted strings and storing file name parts in a list
			clean = re.split('.HDTV.CAKES.en',i)
			# print(clean)
			pattern = re.compile('\d+')
			temp = re.findall(pattern,clean[0])
			season = int(temp[0])
			season = str(season)
			episode = int(temp[1])
			episode = str(episode)
			extension = clean[1]
			clean = re.split('Lucifer - ' + '\d+'+'x'+'\d+' + ' - ',clean[0])
			epi_name = clean[1]
			# print(season,episode)
			# print(len(season),len(episode))
			
			s_p = season_padding
			e_p = episode_padding
			# Applying padding to season and episode numbers
			while s_p>len(season):
				season = '0' + season 
			while e_p>len(episode):
				episode = '0' + episode
			# print('after padding')
			# print(season,episode)
			# print('Game of Thrones - '+'Season '+season+' Episode '+episode+' - '+epi_name+extension)
			new_name = 'Lucifer - '+'Season '+season+' Episode '+episode+' - '+epi_name+extension
			# Renaming new files
			os.rename(dir_corrected_srt+'/'+i,dir_corrected_srt+'/'+new_name)
regex_renamer()