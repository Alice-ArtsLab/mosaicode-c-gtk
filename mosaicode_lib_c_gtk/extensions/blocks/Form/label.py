#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Label(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.help = "Not to declare"
        self.label = "Label"
        self.color = "250:150:150:150"
        self.group = "Form"
        self.ports = [{
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "name": "float_value",
                "conn_type": "Input",
                "label": "Float Value"
                }]

        self.properties = [{"name": "label",
                            "label": "Label",
                            "type": MOSAICODE_STRING,
                            "value": "Label"
                            }
                           ]

        self.codes["declaration"] = """
GtkWidget *$label$_$id$;

void $port[float_value]$(float value){
    gchar *display;
    display = g_strdup_printf("$prop[label]$: %.1f", value);
    gtk_label_set_text(GTK_LABEL($label$_$id$), display);
    g_free(display);
}
"""

        self.codes["setup"] = """
   $label$_$id$ = gtk_label_new("$prop[label]$");
   gtk_container_add(GTK_CONTAINER(vbox), $label$_$id$);
"""

