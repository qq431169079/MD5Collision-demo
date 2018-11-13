import urllib.request

input("Installing file 'evil' from 'https://iksman.com/projects/md5' >>")
urllib.request.urlretrieve("https://iksman.com/projects/md5/evil" , "evil")
print("Succesfully installed file 'evil' to folder")

