from PIL import Image
import numpy as np
import math
import sys

def Pixelize(inputImage, outputImage, rowCount, columnCount):
    try:
        print("INFO: Start")

        rowCount = rowCount
        columnCount = columnCount

        im = Image.open(inputImage)
        npArr = np.array(im)
        accum = []
        npArrX = 0
        npArrY = 0

        imSize = im.size
        print("INFO: Input Image Size:", imSize[0], imSize[1])

        rowSize = int(round(im.size[0] / rowCount))
        columnSize = int(round(im.size[1] / columnCount))
        print("INFO: RowSize in Pixels:", rowSize, "ColumnSize in Pixels:", columnSize)
        print("INFO: Output Image Pixels:", rowCount, columnCount)

        for iter in range(rowCount * columnCount):
            accum = [0, 0, 0]
            for x in range(rowSize):
                for y in range(columnSize):
                    if(x + (rowSize * (iter % rowCount)) >= imSize[0]):
                        npArrX = imSize[0] - 1
                    else:
                        npArrX = x + (rowSize * (iter % rowCount))
                    if(y + (columnSize * (math.floor(iter / rowCount))) >= imSize[1]):
                        npArrY = imSize[1] - 1
                    else:
                        npArrY = y + (columnSize * (math.floor(iter / rowCount)))
                    accum = npArr[npArrY, npArrX] + accum
            accum = accum / (rowSize * columnSize)

            for x in range(rowSize):
                for y in range(columnSize):
                    if (x + (rowSize * (iter % rowCount)) >= imSize[0]):
                        npArrX = imSize[0] - 1
                    else:
                        npArrX = x + (rowSize * (iter % rowCount))
                    if (y + (columnSize * (math.floor(iter / rowCount))) >= imSize[1]):
                        npArrY = imSize[1] - 1
                    else:
                        npArrY = y + (columnSize * (math.floor(iter / rowCount)))
                    npArr[npArrY, npArrX] = accum

            log = "INFO: Processing " + str(round((100 * iter) / (rowCount * columnCount), 0)) + "%"
            sys.stdout.write("\r" + log)

        Image.fromarray(npArr).save(outputImage)

        print("\nINFO: Finished Successfully")

    except TypeError:
        im = Image.open(inputImage)
        imSize = im.size
        print("ERROR: Max RowCount must be", imSize[0], "Max ColumnCount must be", imSize[1])

    print("INFO: End")

    return