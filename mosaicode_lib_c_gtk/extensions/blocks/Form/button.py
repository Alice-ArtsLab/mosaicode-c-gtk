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

        self.properties = [{"name": "value",
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
GtkWidget *$label$_$id$;
typedef void (*button_callback_$id$)(float value);
button_callback_$id$ * $port[click]$;
int $port[click]$_size = 0;

void $label$$id$_callback(void * data){
   for(int i = 0 ; i < $port[click]$_size ; i++){
        // Call the stored functions
        (*($port[click]$[i]))($prop[value]$);
   }
}
"""

        self.codes["setup"] = """
    $label$_$id$ = gtk_button_new_with_label("$prop[label]$");
    $port[click]$ = (button_callback_$id$ *)malloc(sizeof(button_callback_$id$));
    g_signal_connect(
                G_OBJECT($label$_$id$),
                "clicked",
                G_CALLBACK($label$$id$_callback),
                NULL
                );
    gtk_container_add(GTK_CONTAINER(vbox), $label$_$id$);
"""
