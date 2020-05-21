#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Spin(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.label = "Spin"
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
                            {"name": "lower",
                            "label": "Lower",
                            "type": MOSAICODE_FLOAT,
                            "lower": -20000,
                            "upper": 20000,
                            "step": 1,
                            "value": 0
                            },
                            {"name": "upper",
                            "label": "Upper",
                            "type": MOSAICODE_FLOAT,
                            "lower": -20000,
                            "upper": 20000,
                            "step": 1,
                            "value": 200000
                            },
                            {"name": "climb_rate",
                            "label": "Climb Rate",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "digits",
                            "label": "Digits",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            }
                           ]

        self.codes["declaration"] = """
GtkWidget *spin_$id$;
GtkAdjustment *spin_$id$_adjustment;
typedef void (*spin_callback_$id$)(float value);
spin_callback_$id$ * $port[click]$;
int $port[click]$_size = 0;

void spin$id$_callback(GtkSpinButton *widget, gboolean state, void * data){
    float result = (float)gtk_spin_button_get_value(widget);
    for(int i = 0 ; i < $port[click]$_size ; i++){
        (*($port[click]$[i]))(result);
   }
}
"""

        self.codes["setup"] = """
    spin_$id$_adjustment = gtk_adjustment_new (
                $prop[lower]$,
                0.0, // page increment
                10.0, // page size
                1.0, //step icnrement
                $prop[upper]$,
                $prop[value]$);
    spin_$id$ = gtk_spin_button_new(
                spin_$id$_adjustment,
                $prop[climb_rate]$,
                $prop[digits]$);
    $port[click]$ = (spin_callback_$id$ *)malloc(sizeof(spin_callback_$id$));
    g_signal_connect(
                G_OBJECT(spin_$id$),
                "value-changed",
                G_CALLBACK(spin$id$_callback),
                NULL
                );
    gtk_container_add(GTK_CONTAINER(vbox), spin_$id$);
"""