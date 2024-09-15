import os
import sys
import random

# specify input folder, output folder, and number of images to move
if(len(sys.argv) >= 3):

    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])

    inputFolderName = sys.argv[1]
    outputFolderName = sys.argv[2]

    for i in range(int(sys.argv[3])):
        imgFiles = os.listdir(f"{inputFolderName}/images")
        labelFiles = os.listdir(f"{inputFolderName}/labels")
        rand = random.randint(0, len(imgFiles) - 1)
        filename = imgFiles[rand]
        os.replace(f"{inputFolderName}/images/{filename}", f"{outputFolderName}/images/{filename}")

        labelFileName = f"{filename.split('.jpg')[0]}.txt"
        os.replace(f"{inputFolderName}/labels/{labelFileName}", f"{outputFolderName}/labels/{labelFileName}")

        print(f"Moved {filename} and {labelFileName} from {inputFolderName} to {outputFolderName}")
