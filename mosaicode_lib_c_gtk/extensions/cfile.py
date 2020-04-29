# -*- coding: utf-8 -*-
# [MOSAICODE PROJECT]
#
"""
This module contains the JavascriptTemplate class.
"""
from mosaicode.model.codetemplate import CodeTemplate
from mosaicode.GUI.fieldtypes import *

class CFile(CodeTemplate):
    """
    This class contains methods related the JavascriptTemplate class.
    """
    # ----------------------------------------------------------------------

    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "gtk"
        self.language = "c"
        self.description = "A full template to generate gtk code"
        self.command = "g++ -o $dir_name$main $dir_name$main.c `pkg-config --cflags --libs gtk+-3.0`\n"
        self.command += "$dir_name$./main"
        self.code_parts = ["declaration", "function", "configuration"]
        self.properties = [{"name": "title",
                            "label": "Title",
                            "value": "Title",
                            "type": MOSAICODE_STRING
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

        self.files["main.c"] = r"""
#include <gtk/gtk.h>

void destroy(void){
   gtk_main_quit ();
}
$code[declaration]$

$code[function]$

int main(int argc, char *argv[]){
   GtkWidget *window;
   GtkWidget *vbox;

   gtk_init(&argc, &argv);


   window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
   gtk_window_set_title(GTK_WINDOW(window), "$prop[title]$");
   g_signal_connect(window, "destroy",G_CALLBACK(destroy), NULL);
   gtk_window_resize(GTK_WINDOW(window), $prop[width]$, $prop[height]$);

   vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL,3);
   gtk_container_add(GTK_CONTAINER(window), vbox);

   $code[configuration]$
   $connections$

   gtk_widget_show_all(window);
   gtk_main();
   return 0;
}
"""

# -------------------------------------------------------------------------
