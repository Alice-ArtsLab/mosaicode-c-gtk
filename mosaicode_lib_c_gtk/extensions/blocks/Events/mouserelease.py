#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MouseRelease(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.label = "Mouse Release"
        self.color = "250:150:150:150"
        self.group = "Event"
        self.ports = [
                {
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Release x",
                "conn_type":"Output",
                "name":"release_x"
                },
                {
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Release Y",
                "conn_type":"Output",
                "name":"release_y"
                },
                {
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Button",
                "conn_type":"Output",
                "name":"release_button"
                }
                ]

        self.properties = []

        self.codes["declaration"] = """
float_callback * $port[release_x]$;
float_callback * $port[release_y]$;
float_callback * $port[release_button]$;
int $port[release_x]$_size = 0;
int $port[release_y]$_size = 0;
int $port[release_button]$_size = 0;

void mouse_release_$id$_callback_release(
                        GtkWidget *widget,
                        GdkEventButton *event,
                        gpointer data){
   for(int i = 0 ; i < $port[release_x]$_size ; i++){
        // Call the stored functions
        (*($port[release_x]$[i]))(event->x);
   }
   for(int i = 0 ; i < $port[release_y]$_size ; i++){
        // Call the stored functions
        (*($port[release_y]$[i]))(event->y);
   }
   for(int i = 0 ; i < $port[release_button]$_size ; i++){
        // Call the stored functions
        (*($port[release_button]$[i]))(event->button);
   }
}
"""

        self.codes["setup"] = """
    g_signal_connect(
                G_OBJECT(window),
                "button_release_event",
                G_CALLBACK(mouse_release_$id$_callback_release),
                NULL
                );
"""
