#Backup for Skynode Server
#To do:
#   - Implement google drive upload portion
#   - Allow login for skynode to open up SFTP server
#   - Cleanup for localpath logic
import pysftp
from ftplib import FTP
import time
import os
from var import *
import compression
#Google Drive FTP Adapter file
#adapterdir = "D:\\SkriptServer\\FTP\\google-drive-ftp-adapter-jar-with-dependencies.jar"

cnopts = pysftp.CnOpts
cnopts.compression = cnopts.hostkeys = cnopts.ciphers = None
cnopts.log = cnopts.compression = False


def sftp_get_skynode(remotepath, localpath): #Custom version for skynode
    for file in sftp.listdir(remotepath):
        filepath = remotepath + '/' + file
        if file in overwrite: #If a file needs to be overwritten
            os.remove(localpath + filepath) #Then delete the file
            print("[SFTP_GET]: Delete" + " " + localpath + filepath + " " + "for overwriting")
        if file in blacklist or file[-4:] in blacklist or os.path.isfile(localpath + filepath): #If the file already exists, or in the blacklist,
            print("[SFTP_GET]: Skipped" + " " + filepath)
            continue
        if sftp.isfile(filepath): #If file is a file
            sftp.get(filepath, localpath+filepath, preserve_mtime=True)
            print("[SFTP_GET]: Copied" + " " + filepath + " " + "to" + " " + localpath+filepath)
        else:
            if not os.path.exists(localpath + filepath + '/'): #If file is a folder
                os.mkdir(localpath + filepath + '/')
            sftp_get_skynode(filepath, localpath)

def sftp_get(remotepath, localpath): #Gets all files and folders recursively (and all files within each respective folder). pysftp required
    for file in sftp.listdir(remotepath):
        filepath = remotepath + '/' + file
        if sftp.isfile(filepath):
            sftp.get(filepath, localpath+filepath, preserve_mtime=True)
            print("[SFTP_GET]: Copied" + " " + filepath + " " + "to" + " " + localpath+filepath)
        else:
            os.mkdir(localpath + filepath + '/')
            sftp_get(filepath, localpath)

with pysftp.Connection(host=host, username=user, password=password, port=port, cnopts=cnopts) as sftp: #Get files
    for folder in remotedir:
        if not os.path.exists(localpath+folder):
            os.mkdir(localpath+folder)
        sftp_get_skynode(folder, localpath)


compression.zip(remotedir[-3::], "OUTPUT_World.7z") #Compresses files
compression.zip([remotedir[1]], "OUTPUT_PCONFIG.7z")




