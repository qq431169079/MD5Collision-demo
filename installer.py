import urllib.request, subprocess

input("Installing file 'good' from 'https://iksman.com/projects/md5' >>")
urllib.request.urlretrieve("https://iksman.com/projects/md5/good" , "good")
subprocess.run(["chmod","+x","good"])
print("Succesfully installed file 'good' to folder")

