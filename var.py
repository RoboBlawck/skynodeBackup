#Global variables
host = "fna1.skynode.pro"
user = "shingsurvival.42bc0ab7"
port = 2022
password = input("Enter password: ") #Don't log passwords
remotedir = ['logs','plugins','MAIN_world', 'MAIN_world_nether', 'MAIN_world_the_end'] #remotedir[:-3] last 3, remotedir[2]
localpath = "C:/Users/New_Shing/Desktop/SkyNode_Temp/"
blacklist = ['.jar']
overwrite = ['latest.log']
conf = "a -t7z -m0=LZMA2 -mx=9 -mfb=64 -md=64m -ms=on" #compression settings
exe = "C:/Users/New_Shing/Desktop/7-Zip/7z.exe" #7z exe path



#Use from var import *