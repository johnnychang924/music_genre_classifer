import os
import subprocess

if __name__ == "__main__":
    folder_address = "./music/鄉村"
    for folder in os.listdir(folder_address):
        #if folder.endswith(".mp4"):
        path = folder_address + "/" + folder
        path = path[:-1]
        print(path)
        ret = subprocess.run(f'ffmpeg -i "{path}4" "{path}3"',shell=True, capture_output=False)
        print(ret.returncode)
