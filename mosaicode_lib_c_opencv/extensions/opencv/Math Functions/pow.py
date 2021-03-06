#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Pow class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Pow(BlockModel):
    """
    This class contains methods related the Pow class.
    """

    def __init__(self):
        BlockModel.__init__(self)
        
        self.language = "c"
        self.framework = "opencv"
        self.label = "Pow"
        self.color = "179:255:25:245"
        self.group = "Math Functions"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.properties = [{"label": "Exponent",
                            "name": "exponent",
                            "value":1,
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 10,
                            "step": 1
                            }
                           ]

# --------------------------- C/OpenCv Code------------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
"""

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
        pow($port[input_image]$, $prop[exponent]$, $port[output_image]$);
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""

# -----------------------------------------------------------------------------
