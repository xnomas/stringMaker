import cmd

class Interpreter(cmd.Cmd):
    """Simple command processor example."""

    def  __init__(self, lang : str):
        super(Interpreter, self).__init__()
        self.lang = lang
        self.prompt = '[str] ' 

    def do_greet(self, line):
        print ('hello')

    def do_EOF(self, line):
       #this command will make you exit from the shell
        return True

    def do_exit(self, line):
        return True

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
    langList = [
        'JavaScript',
        'PHP',
        'Ruby',
        'ASP.NET',
    ] 

    interpreter.cmdloop()

runInterpreter(Interpreter('JavaScript'))