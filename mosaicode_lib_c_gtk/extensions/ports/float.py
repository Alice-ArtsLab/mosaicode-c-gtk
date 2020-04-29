from mosaicode.model.port import Port

class Float(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "FLOAT"
        self.color = "#fc2300"
        self.multiple = True
        self.code = """
    $output$ = (float_callback *) realloc($output$, ($output$_size + 1 ) * sizeof(float_callback));
    $output$[$output$_size] = &$input$;
    $output$_size++;
"""
        self.var_name = "$port[name]$$block[id]$"
