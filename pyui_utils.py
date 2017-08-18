import ui

class PYUILoader(ui.View):
    # this acts as a normal Custom ui.View class
    # the root view of the class is the pyui file read in
    def WrapInstance(obj):
        class Wrapper(obj.__class__):
            def __new__(cls):
                return obj
        return Wrapper
    
    def __init__(self, pyui_fn, *args, **kwargs):
        bindings=globals().copy()
        bindings[self.__class__.__name__]=self.WrapInstance()
        
        ui.load_view(pyui_fn, bindings)
        
        # call after so our kwargs modify attrs
        super().__init__(*args, **kwargs)
