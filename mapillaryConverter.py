import os
import sys
import json

def writeDataYaml(outputFolderName):
    dataYaml = open(f"{outputFolderName}/data.yaml", "w")
    dataYaml.write("names:\n")
    dataYaml.write("- sign\n")
    dataYaml.write("nc: 1\n")
    dataYaml.write(f"test: {outputFolderName}/test/images\n")
    dataYaml.write(f"train: {outputFolderName}/train/images\n")
    dataYaml.write(f"val: {outputFolderName}/valid/images\n")

# specify input folder, output folder, and number of images to move
if(len(sys.argv) >= 3):

    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])

    inputFolderName = sys.argv[1]
    outputFolderName = sys.argv[2]

    if not os.path.isdir(outputFolderName):
        os.makedirs(outputFolderName)

    writeDataYaml(outputFolderName)
    os.makedirs(f"{outputFolderName}/test/images")
    os.makedirs(f"{outputFolderName}/test/labels")
    os.makedirs(f"{outputFolderName}/train/images")
    os.makedirs(f"{outputFolderName}/train/labels")
    os.makedirs(f"{outputFolderName}/valid/images")
    os.makedirs(f"{outputFolderName}/valid/labels")
    
    # train
    trainFile = open(f"{inputFolderName}/splits/train.txt", "r")
    trainList = map(lambda x: x.strip(), trainFile.readlines())

    for fileName in trainList:
        jsonFile = open(f"{inputFolderName}/annotations/{fileName}.json", "r")
        data = json.load(jsonFile)

        box = None
        width = data["width"]
        height = data["height"]
        objects = data["objects"]

        labelsFile = open(f"{outputFolderName}/train/labels/{fileName}.txt", "w")

        for i in range(1, len(objects)):
            obj = objects[i]
            box = obj["bbox"]

            ymin = box["ymin"] / height
            ymax = box["ymax"] / height
            xmin = box["xmin"] / width
            xmax = box["xmax"] / width
            bwidth = xmax - xmin
            bheight = ymax - ymin

            # 1 is only class
            labelsFile.write(f"1 {xmin} {ymin} {bwidth} {bheight}\n")

        # find the folder it lives in
        if os.path.isfile(f"{inputFolderName}/train0/{fileName}.jpg"):
            os.replace(f"{inputFolderName}/train0/{fileName}.jpg", f"{outputFolderName}/train/images/{fileName}.jpg")
        elif os.path.isfile(f"{inputFolderName}/train1/{fileName}.jpg"):
            os.replace(f"{inputFolderName}/train1/{fileName}.jpg", f"{outputFolderName}/train/images/{fileName}.jpg")
        elif os.path.isfile(f"{inputFolderName}/train2/{fileName}.jpg"):
            os.replace(f"{inputFolderName}/train2/{fileName}.jpg", f"{outputFolderName}/train/images/{fileName}.jpg")

    # val
    valFile = open(f"{inputFolderName}/splits/val.txt", "r")
    valList =  map(lambda x: x.strip(), valFile.readlines())

    for fileName in valList:
        jsonFile = open(f"{inputFolderName}/annotations/{fileName}.json", "r")
        data = json.load(jsonFile)

        box = None
        width = data["width"]
        height = data["height"]
        objects = data["objects"]

        labelsFile = open(f"{outputFolderName}/valid/labels/{fileName}.txt", "w")

        for i in range(1, len(objects)):
            obj = objects[i]
            box = obj["bbox"]

            ymin = box["ymin"] / height
            ymax = box["ymax"] / height
            xmin = box["xmin"] / width
            xmax = box["xmax"] / width
            bwidth = xmax - xmin
            bheight = ymax - ymin

            # 1 is only class
            labelsFile.write(f"1 {xmin} {ymin} {bwidth} {bheight}\n")

        os.replace(f"{inputFolderName}/val/{fileName}.jpg", f"{outputFolderName}/valid/images/{fileName}.jpg")
