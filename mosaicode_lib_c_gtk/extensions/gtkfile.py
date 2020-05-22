# -*- coding: utf-8 -*-
# [MOSAICODE PROJECT]
#
"""
This module contains the JavascriptTemplate class.
"""
from mosaicode.model.codetemplate import CodeTemplate
from mosaicode.GUI.fieldtypes import *

class GtkFile(CodeTemplate):
    """
    This class contains methods related the JavascriptTemplate class.
    """
    # ----------------------------------------------------------------------

    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "gtk"
        self.language = "c"
        self.description = "A full template to generate gtk code"
        self.command = "make && $dir_name$./main\n"
        self.code_parts = ["declaration", "setup"]
        self.properties = [{"name": "title",
                            "label": "Title",
                            "value": "Title",
                            "type": MOSAICODE_STRING
                            },
                            {"name": "border",
                            "label": "Border",
                            "value": 50,
                            "type": MOSAICODE_INT
                            },
                            {"name": "width",
                            "label": "Width",
                            "value": 800,
                            "type": MOSAICODE_INT
                            },
                            {"name": "height",
                            "label": "Height",
                            "value": 600,
                            "type": MOSAICODE_INT
                            }
                           ]

        self.files["callback.h"] = r"""
typedef void (*string_callback)(const char * value);
typedef void (*float_callback)(float value);
typedef void (*int_callback)(int value);
typedef void (*char_callback)(char value);
"""

        self.files["main.c"] = r"""
#include <gtk/gtk.h>
#include <limits.h>
#include <string.h>
#include <time.h>
#include <math.h>
#include "callback.h"

GtkWidget * window;
GtkWidget * fixed_layout;
$code[declaration]$

void destroy(void){
    gtk_main_quit ();
}

int main(int argc, char *argv[]){
    gtk_init(&argc, &argv);

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "$prop[title]$");
    g_signal_connect(window, "destroy",G_CALLBACK(destroy), NULL);
    gtk_window_resize(GTK_WINDOW(window), $prop[width]$, $prop[height]$);
    gtk_container_set_border_width(GTK_CONTAINER(window), $prop[border]$);

    fixed_layout = gtk_fixed_new();
    gtk_container_add(GTK_CONTAINER(window), fixed_layout);


    $code[setup]$
    $connections$

    gtk_widget_show_all(window);
    gtk_main();
    return 0;
}
"""

        self.files["Makefile"] = \
r"""CC := gcc
CFLAGS := -g -Wall
LIBS := -lm `pkg-config --cflags --libs gtk+-3.0`
LIB_FLAGS :=
TARGET := main

all:	$(TARGET)

main: main.o
	$(CC) $(CFLAGS) $^ $(LIB_FLAGS) -o $@  $(LIBS)

main.o: main.c
	$(CC) $(CFLAGS) -c $< $(LIB_FLAGS) -o $@  $(LIBS)

"""


# -------------------------------------------------------------------------
