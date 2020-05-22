#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MouseClick(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.label = "Mouse Click"
        self.color = "250:150:150:150"
        self.group = "Event"
        self.ports = [
                {
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Click x",
                "conn_type":"Output",
                "name":"click_x"
                },
                {
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Click Y",
                "conn_type":"Output",
                "name":"click_y"
                },
                {
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Button",
                "conn_type":"Output",
                "name":"click_button"
                }
                ]

        self.properties = []

        self.codes["declaration"] = """
float_callback * $port[click_x]$;
float_callback * $port[click_y]$;
float_callback * $port[click_button]$;
int $port[click_x]$_size = 0;
int $port[click_y]$_size = 0;
int $port[click_button]$_size = 0;

void mouse_click_$id$_callback_click(
                        GtkWidget *widget,
                        GdkEventButton *event,
                        gpointer data){
   for(int i = 0 ; i < $port[click_x]$_size ; i++){
        // Call the stored functions
        (*($port[click_x]$[i]))(event->x);
   }
   for(int i = 0 ; i < $port[click_y]$_size ; i++){
        // Call the stored functions
        (*($port[click_y]$[i]))(event->y);
   }
   for(int i = 0 ; i < $port[click_button]$_size ; i++){
        // Call the stored functions
        (*($port[click_button]$[i]))(event->button);
   }
}
"""

        self.codes["setup"] = """
    g_signal_connect(
                G_OBJECT(window),
                "button_press_event",
                G_CALLBACK(mouse_click_$id$_callback_click),
                NULL
                );
"""
