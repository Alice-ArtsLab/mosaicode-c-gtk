#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Entry(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.label = "Entry"
        self.color = "250:150:150:150"
        self.group = "Form"
        self.ports = [{
                "type":"mosaicode_lib_c_base.extensions.ports.string",
                "label":"Enter",
                "conn_type":"Output",
                "name":"enter"
                },{
                "type": "mosaicode_lib_c_base.extensions.ports.string",
                "name": "text_value",
                "conn_type": "Input",
                "label": "Text Value"
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
                            "type": MOSAICODE_STRING,
                            "value": ""
                            }
                           ]

        self.codes["declaration"] = """
GtkWidget *entry_$id$;
string_callback * $port[enter]$;
int $port[enter]$_size = 0;

void $port[text_value]$(const char * value){
    gtk_entry_set_text(GTK_ENTRY(entry_$id$), value);
    // Should it propagate the received value?
    //for(int i = 0 ; i < $port[enter]$_size ; i++){
    //    (*($port[enter]$[i]))(value);
    //}
}

void entry$id$_callback(GtkEntry * widget, void * data){
    const gchar * value = gtk_entry_get_text(GTK_ENTRY(widget));
    for(int i = 0 ; i < $port[enter]$_size ; i++){
        (*($port[enter]$[i]))(value);
    }
}
"""

        self.codes["setup"] = """
    entry_$id$ = gtk_entry_new();
    gtk_entry_set_text(GTK_ENTRY(entry_$id$), "$prop[value]$");
    g_signal_connect(
                G_OBJECT(entry_$id$),
                "activate",
                G_CALLBACK(entry$id$_callback),
                NULL
                );
   gtk_fixed_put(GTK_FIXED(fixed_layout), entry_$id$, $prop[x]$, $prop[y]$);
"""
