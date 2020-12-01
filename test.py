"""
print("Hello World")
array = [37, 7, -45, 38, 174, -28, -21, -37, 22, 25, 53, -25, 28, -22, -37, 28, -29, -38, 7, -48, -14, 34, 84, -33, -40, -44, 45, 3, 99, 7]
i = 0
for elements in array:
	if i == 2:
		print(str(elements)+ ",")
	if i == 2:
		i = 0
	else:
		i+=1
"""

"""
import string
array = " "
array += string.ascii_letters[0:26]
print(array)
wordstuff = "python language"
for i in wordstuff:
	for j in array:
		if(i==j):
			print(array.index(j))

"""
"""
vowels = ['a', 'e', 'i', 'o', 'u']

# index of'p' is vowels
index = vowels.index('e')
print('The index of p:', index)
"""
import os
import time
while True: 
	for i in range(17):
		print("Check point 1")
		print(i)
		if i >= 10: 
			KernelPath = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/Demonte/Downloads/Yuno\ Gif/frame_"+str(i)+"_delay-0.1s.gif"
		else: 
			KernelPath = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/Demonte/Downloads/Yuno\ Gif/frame_0"+str(i)+"_delay-0.1s.gif"
		time.sleep(.5)
		os.system(KernelPath)