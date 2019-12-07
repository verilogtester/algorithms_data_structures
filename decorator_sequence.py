
def prepost(f):
  def prepost_wrapper(self, *args, **kwargs):
    pre_name  = 'pre_'  + f.__name__
    post_name = 'post_' + f.__name__
    if hasattr(self, pre_name):  
      getattr(self, pre_name) (*args, **kwargs)
      ret = f(self, *args, **kwargs)
      if hasattr(self, post_name): 
        getattr(self, post_name)(*args, **kwargs)
      return ret
    return prepost_wrapper

class MakePhase:
    def init(self): pass
    def config(self): pass
    def run(self): pass
    def check(self): pass
    def final(self): pass



    def exec(self):
        self.init()
        self.config()
        self.run()
        self.check()
        self.final()

class MakeInit(MakePhase):
    def __init__(self):
      pass
        #self.pre_init()
        #self.init()
        #self.post_init()
    
    @prepost
    def pre_init(self):
        print("in pre init phase")
    @prepost
    def post_init(self):
        print("in post init phase")
    
    def init(self):
        print("in init phase")

class MakeConfig(MakePhase):
    def __init__(self):
      pass
        #self.pre_config()
        #self.config()
        #self.post_config()
    
    def pre_config(self):
        print("in pre config phase")
    
    def post_config(self):
        print("in post config phase")
    
    def config(self):
        print("in config phase")
        
init_phase = MakeInit()
config_phase = MakeConfig()
init_phase.exec()
config_phase.exec()
