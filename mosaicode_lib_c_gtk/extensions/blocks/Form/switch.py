#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Switch(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.label = "Switch"
        self.color = "250:150:150:150"
        self.group = "Form"
        self.ports = [{
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Click",
                "conn_type":"Output",
                "name":"click"
                }]

        self.properties = [{"name": "value_on",
                            "label": "Value On",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "value_off",
                            "label": "Value Off",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 0
                            }
                           ]

        self.codes["declaration"] = """
GtkWidget *switch_$id$;
typedef void (*switch_callback_$id$)(float value);
switch_callback_$id$ * $port[click]$;
int $port[click]$_size = 0;

void switch$id$_callback(GtkSwitch *toggle_button, gboolean state, void * data){
    float result = 0;
    if (state){
        result = $prop[value_on]$;
    }else{
        result = $prop[value_off]$;
    }
    for(int i = 0 ; i < $port[click]$_size ; i++){
        (*($port[click]$[i]))(result);
   }
}
"""

        self.codes["setup"] = """
    switch_$id$ = gtk_switch_new();
    $port[click]$ = (switch_callback_$id$ *)malloc(sizeof(switch_callback_$id$));
    g_signal_connect(
                G_OBJECT(switch_$id$),
                "state-set",
                G_CALLBACK(switch$id$_callback),
                NULL
                );
    gtk_container_add(GTK_CONTAINER(vbox), switch_$id$);
"""
