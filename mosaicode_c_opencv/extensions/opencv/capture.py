#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Capture class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import os
from glob import glob


class Capture(BlockModel):
    """
    This class contains methods related the Capture class.
    """
    # ------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        self.help = "Realiza a aquisição de uma imagem " + \
            "a partir de algum dispositivo," + \
            " seja este uma mídia ou um dispositivo " + \
            "de aquisição de imagens (câmera, scanner)."
        self.label = "Capture"
        self.color = "50:100:200:150"
        self.out_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "label":"Input Image"}
                          ]
        self.group = "Image Source"
        self.language = "c"
        self.framework = "opencv"
        self.properties = [{"name": "camera",
                 "label": "Camera",
                 "type": MOSAICODE_INT,
                 "value":"0",
                 "lower": 0,
                 "upper": 4}]

        self.codes["declaration"] = \
            'IplImage * block$id$_img_o0 = NULL; //Capture\n' + \
            'CvCapture* block$id$_capture = NULL; \n' + \
            'IplImage* block$id$_frame = NULL; \n' + \
            'int counter$id$ = 0;\n'

        self.codes["execution"] = \
            'if (counter$id$ == 0){\n' + \
            'block$id$_capture = cvCaptureFromCAM($camera$); \n' + \
            'if( !cvGrabFrame( block$id$_capture ))' + \
            '{ printf("Cannot Grab Image from camera $camera$"); }\n' + \
            'block$id$_frame = cvRetrieveFrame( block$id$_capture ); \n' + \
            'block$id$_img_o0 = cvCloneImage( block$id$_frame );\n' + \
            'counter$id$++;\n' + \
            '}\n'
        self.codes["deallocation"] = "cvReleaseImage(&block$id$_img_o0);\n"
# -----------------------------------------------------------------------------
