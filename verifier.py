import urllib.request, json, os, sys, subprocess

def cls():
  os.system("clear")

def verify(filename):
  cls()
  input("Getting checksum from https://iksman.com/projects/md5/data.json...")
  response = urllib.request.urlopen("https://iksman.com/projects/md5/data.json")
  checksum = json.loads(response.read())["checksum"]
  input("Received checksum: '"  + checksum + "' >>")
  cls()

  print("Calculating checksum of file '" + filename + "'")
  checksum_file_subprocess = subprocess.run(["md5sum", filename], stdout=subprocess.PIPE)
  checksum_file = str(checksum_file_subprocess.stdout)[2:].split(" ")[0]
  input("Result: '" + checksum_file + "' >>")
  cls()

  input("Comparing two checksums:")
  print("Verified checksum from source: '" + checksum + "'") 
  input("Checksum from file '" + filename + "': '" + checksum_file + "' >>")
  if checksum == checksum_file:
    input("Verified!!")
    return 0
  else:
    input("Not verified!!")
    return 1


try:
  filename = sys.argv[1]
except:
  print("Please supply a file to verify")
  exit()

result = verify(filename)
if result == 0:
  cls()
  print("Content of file:")
  subprocess.call("./" + filename)
  print()  

