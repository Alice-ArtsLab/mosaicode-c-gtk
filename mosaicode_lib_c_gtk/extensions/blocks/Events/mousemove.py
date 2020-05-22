#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MouseMove(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.label = "Mouse Move"
        self.color = "250:150:150:150"
        self.group = "Event"
        self.ports = [
                {
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Move X",
                "conn_type":"Output",
                "name":"move_x"
                },
                {
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Move Y",
                "conn_type":"Output",
                "name":"move_y"
                }
                ]

        self.properties = []

        self.codes["declaration"] = """
float_callback * $port[move_x]$;
float_callback * $port[move_y]$;
int $port[move_x]$_size = 0;
int $port[move_y]$_size = 0;

void mouse_move_$id$_callback_move(
                        GtkWidget *widget,
                        GdkEventMotion *event,
                        gpointer data){
   for(int i = 0 ; i < $port[move_x]$_size ; i++){
        // Call the stored functions
        (*($port[move_x]$[i]))(event->x);
   }
   for(int i = 0 ; i < $port[move_y]$_size ; i++){
        // Call the stored functions
        (*($port[move_y]$[i]))(event->y);
   }
}
"""

        self.codes["setup"] = """
    g_signal_connect(
                G_OBJECT(window),
                "motion_notify_event",
                G_CALLBACK(mouse_move_$id$_callback_move),
                NULL
                );
"""
