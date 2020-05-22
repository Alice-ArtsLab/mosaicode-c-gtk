#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Scale(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.label = "Scale"
        self.color = "250:150:150:150"
        self.group = "Form"
        self.ports = [
                {
                "type": "mosaicode_lib_c_base.extensions.ports.float",
                "name": "float_value",
                "conn_type": "Input",
                "label": "Float Value"
                },{
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
                            {"name": "orientation",
                            "label": "Orientation",
                            "type": MOSAICODE_COMBO,
                            "values": ["GTK_ORIENTATION_HORIZONTAL","GTK_ORIENTATION_VERTICAL"],
                            "value": "GTK_ORIENTATION_HORIZONTAL"
                            },
                            {"name": "value",
                            "label": "Value",
                            "type": MOSAICODE_FLOAT,
                            "value": "0"
                            },
                            {"name": "min",
                            "label": "Min",
                            "type": MOSAICODE_FLOAT,
                            "value": "0"
                            },
                            {"name": "max",
                            "label": "Max",
                            "type": MOSAICODE_FLOAT,
                            "value": "100"
                            },
                            {"name": "step",
                            "label": "Step",
                            "type": MOSAICODE_FLOAT,
                            "value": "1"
                            },
                            {"name": "digits",
                            "label": "Digits",
                            "type": MOSAICODE_FLOAT,
                            "value": "2"
                            }
                           ]

        self.codes["declaration"] = """
GtkWidget * scale_$id$;
float_callback * $port[click]$;
int $port[click]$_size = 0;

void $port[float_value]$(float value){
    gtk_range_set_value(GTK_RANGE(scale_$id$), value);
}

static void scale$id$_value_changed_callback(
                    GtkRange *range,
                    gpointer user_data){
    float value = gtk_range_get_value(range);
    for(int i = 0 ; i < $port[click]$_size ; i++){
        // Call the stored functions
        (*($port[click]$[i]))(value);
   }
}

"""

        self.codes["setup"] = """
    scale_$id$ = gtk_scale_new_with_range(
                $prop[orientation]$,
                $prop[min]$,
                $prop[max]$,
                $prop[step]$
                );
    gtk_range_set_value(GTK_RANGE(scale_$id$), $prop[value]$);
    gtk_scale_set_digits(GTK_SCALE(scale_$id$), $prop[digits]$);
    g_signal_connect(
                G_OBJECT(scale_$id$),
                "value-changed",
                G_CALLBACK(scale$id$_value_changed_callback),
                NULL);
    gtk_fixed_put(GTK_FIXED(fixed_layout), scale_$id$, $prop[x]$, $prop[y]$);
"""
