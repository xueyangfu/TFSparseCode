import matplotlib
matplotlib.use('Agg')
from dataObj.image import imageNetObj
from tf.ista_time import ISTA_Time
#from plot.roc import makeRocCurve
import pdb

trainImageLists =  "/shared/imageNet/vid2015_128x64/imageNetVID_2015_list.txt"
randImageSeed = None
#Get object from which tensorflow will pull data from
trainDataObj = imageNetObj(trainImageLists, resizeMethod="crop", shuffle=True, seed=randImageSeed)

#ISTA params
params = {
    #Base output directory
    'outDir':          "/home/sheng/mountData/tfLCA/",
    #Inner run directory
    'runDir':          "/imagenetTime_demo/",
    'tfDir':           "/tfout",
    #Save parameters
    'ckptDir':         "/checkpoints/",
    'saveFile':        "/save-model",
    'savePeriod':      100, #In terms of displayPeriod
    #output plots directory
    'plotDir':         "plots/",
    'plotPeriod':      100, #With respect to displayPeriod
    #Progress step
    'progress':        10,
    #Controls how often to write out to tensorboard
    'writeStep':       10, #300,
    #Threshold
    'zeroThresh':      1e-4,
    #Flag for loading weights from checkpoint
    'load':            True,
    'loadFile':        "/home/sheng/mountData/tfLCA/saved/imagenet_spacetime.ckpt",
    #Device to run on
    'device':          '/gpu:0',
    #####ISTA PARAMS######
    #Num iterations
    'numIterations':   10, #1000000,
    'displayPeriod':   1000, #300,
    #Batch size
    'batchSize':       1,
    #Learning rate for optimizer
    'learningRateA':   1e-4,
    'learningRateW':   1e-4,
    #Lambda in energy function
    'thresh':          .03,
    #Number of features in V1
    'numV':            1536,
    #Time dimension
    'nT':              7,
    #Stride of V1
    'VStrideT':        1,
    'VStrideY':        4,
    'VStrideX':        4,
    #Patch size
    'patchSizeT':      4,
    'patchSizeY':      16,
    'patchSizeX':      16,
}

#Allocate tensorflow object
#This will build the graph
tfObj = ISTA_Time(params, trainDataObj)

print "Done init"
tfObj.runModel()
print "Done run"

tfObj.closeSess()

