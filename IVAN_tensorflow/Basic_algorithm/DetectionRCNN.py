import numpy as np
# from interface.Detection import detector
from interface import DLDetection


# call the interface to detect
def start_detect(frame, frame_num, model):
    results = DLDetection.detect(frame, model)
    # results = detector.detect(frame)
    blobs = np.zeros((int(len(results)/6), 8),int)
    for i in range(int(len(results)/6)):
        blobs[i][0] = frame_num                                       # frame number
        blobs[i][1] = -1                                              # car ID
        blobs[i][2] = results[(i - 1) * 6] * 100                      # detection score
        blobs[i][3] = results[(i - 1) * 6 + 1]                        # bbox x
        blobs[i][4] = results[(i - 1) * 6 + 2]                        # bbox y
        blobs[i][5] = results[(i - 1) * 6 + 3]                        # bbox x+w
        blobs[i][6] = results[(i - 1) * 6 + 4]                        # bbox y+h
        # if results[(i - 1) * 6 + 5] == 'minibus':                     # car class
        #     blobs[i][7] = 1
        # elif results[(i - 1) * 6 + 5] == 'bus':
        #     blobs[i][7]= 2
        # elif results[(i - 1) * 6 + 5] == 'smalltruck':
        #     blobs[i][7] = 3
        # elif results[(i - 1) * 6 + 5] == 'mediumtruck':
        #     blobs[i][7] = 4
        # elif results[(i - 1) * 6 + 5] == 'largetruck':
        #     blobs[i][7] = 5
        # elif results[(i - 1) * 6 + 5] == 'trailer':
        #     blobs[i][7] = 6
        # if results[(i - 1) * 6 + 5] == 'minibus_smalltruck':                     # car class
        #     blobs[i][7] = 1
        # elif results[(i - 1) * 6 + 5] == 'bus':
        #     blobs[i][7]= 2
        # elif results[(i - 1) * 6 + 5] == 'medium_large_truck_trailer':
        #     blobs[i][7] = 3
        if results[(i - 1) * 6 + 5] =='vehicle':
            blobs[i][7] = 1
    return blobs




