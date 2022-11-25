import cv2 as cv
import imutils
import numpy as np
from CropTemplate import TemplateCropping, Crop
from TemplateMatching import MatchTemplate
from HSVConvertion import SplitHSV

def FindCrowns(region, template, threshold):

    template90 = imutils.rotate(template, angle=90)
    template180 = imutils.rotate(template, angle=180)
    template270 = imutils.rotate(template, angle=270)

    output1, matchCount1 = MatchTemplate(region, template, threshold)
    output2, matchCount2 = MatchTemplate(output1, template90, threshold)
    output3, matchCount3 = MatchTemplate(output2, template180, threshold)
    outputFinal, matchCount4 = MatchTemplate(output3, template270, threshold)
    matchCountFinal = matchCount1 + matchCount2 + matchCount3 + matchCount4

    return matchCountFinal

