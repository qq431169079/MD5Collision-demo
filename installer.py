import urllib.request

input("Installing file 'good' from 'https://iksman.com/projects/md5' >>")
urllib.request.urlretrieve("https://iksman.com/projects/md5/good" , "good")
print("Succesfully installed file 'good' to folder")

