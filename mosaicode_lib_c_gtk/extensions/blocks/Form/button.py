#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Button(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.label = "Button"
        self.color = "250:150:150:150"
        self.group = "Form"
        self.ports = [{
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Click",
                "conn_type":"Output",
                "name":"click"
                }]

        self.properties = [{"name": "x",
                            "label": "X",
                            "type": MOSAICODE_INT,
                            "value": "0"
                            },
                            {"name": "y",
                            "label": "Y",
                            "type": MOSAICODE_INT,
                            "value": "0"
                            },
                            {"name": "value",
                            "label": "Value",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "label",
                            "label": "Label",
                            "type": MOSAICODE_STRING,
                            "value": "Label"
                            }
                           ]

        self.codes["declaration"] = """
GtkWidget *button_$id$;
float_callback * $port[click]$;
int $port[click]$_size = 0;

void button$id$_callback(void * data){
   for(int i = 0 ; i < $port[click]$_size ; i++){
        // Call the stored functions
        (*($port[click]$[i]))($prop[value]$);
   }
}
"""

        self.codes["setup"] = """
    button_$id$ = gtk_button_new_with_label("$prop[label]$");
    g_signal_connect(
                G_OBJECT(button_$id$),
                "clicked",
                G_CALLBACK(button$id$_callback),
                NULL
                );
    gtk_fixed_put(GTK_FIXED(fixed_layout), button_$id$, $prop[x]$, $prop[y]$);
"""
