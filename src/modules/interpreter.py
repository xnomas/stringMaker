import cmd

from JavaScript import JavaScript

"""
Simple command processor, to be used when argparser is not present. Or for ease of use.
"""
class Interpreter(cmd.Cmd):

    def  __init__(self, lang : str):
        super(Interpreter, self).__init__()
        self.lang = lang
        self.prompt = 'str > ' 
        self.langObject = None


    def do_EOF(self, line):
        return True


    def do_exit(self, line):
        return True


    def parseLangObj(self):
        if self.lang == 'JS' or self.lang == 'JavaScript':
            self.langObject = JavaScript('test')
            self.prompt = 'JS > '
        
        elif self.lang == 'PHP' or self.lang == 'php':
            self.prompt = 'PHP > '


    def do_use(self, arg):
        self.lang = str(arg)
        self.parseLangObj()
        print(f'set language {self.lang}')


    def do_char(self, arg):
        self.langObject.string = str(arg)
        print(self.langObject.charCode(True))


    def do_code(self, arg):
        if self.lang == 'JS' or self.lang == 'JavaScript':
            self.langObject.string = str(arg)
            print(self.langObject.charCode(False))
        else:
            print(f'! code is only defined for JavaScript !')


    def do_hex(self, arg):
        self.langObject.string = str(arg)
        print(self.langObject.fromHex())        


    def do_url(self, arg):
        self.langObject.string = str(arg)
        print(self.langObject.urlEncode())


    def do_b64(self, arg):
        self.langObject.string = str(arg)
        print(self.langObject.base64(False))        


    def do_url_b64(self, arg):
        self.langObject.string = str(arg)
        print(self.langObject.base64(True))        


    def interrupt(self, line):
        print('^C')


    def cmdloop(self, intro=None):
        while True:
            try:
                super(Interpreter, self).cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("^C")

def runInterpreter(interpreter : Interpreter):
    interpreter.cmdloop()
    