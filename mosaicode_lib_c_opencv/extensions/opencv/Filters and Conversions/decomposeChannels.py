#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Decompose Channels class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class DecomposeChannels(BlockModel):
    """
    This class contains methods related the DecomposeChannels class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)
        
        self.language = "c"
        self.framework = "opencv"
        self.label = "Decompose Channels"
        self.color = "230:0:50:245"
        self.group = "Filters and Conversions"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image1",
                       "label":"Output 1",
                       "conn_type":"Output"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image2",
                       "label":"Output 2",
                       "conn_type":"Output"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image3",
                       "label":"Output 3",
                       "conn_type":"Output"}]

# ------------------C/OpenCv code--------------------------------------
        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat tmp_$id$[3];
    Mat $port[output_image1]$;
    Mat $port[output_image2]$;
    Mat $port[output_image3]$;
"""    
        
        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        split($port[input_image]$, tmp_$id$);
        $port[output_image1]$ = tmp_$id$[0];
        $port[output_image2]$ = tmp_$id$[1];
        $port[output_image3]$ = tmp_$id$[2];
    }
"""    

        self.codes["deallocation"] = \
"""        
    tmp_$id$[0].release();
    tmp_$id$[1].release();
    tmp_$id$[2].release();
    $port[output_image1]$.release();
    $port[output_image2]$.release();
    $port[output_image3]$.release();
    $port[input_image]$.release();
"""            

# -----------------------------------------------------------------------------
