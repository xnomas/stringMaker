import cmd

from re import match

from modules.JavaScript import JavaScript
from modules.PHP import PHP

"""
Simple command processor, to be used when argparser is not present. Or for ease of use.
"""


class Interpreter(cmd.Cmd):
    def __init__(self, lang: str):
        super(Interpreter, self).__init__()
        self.lang = lang
        self.prompt = "str > "
        self.langObject = None

    def checkSet(self):
        return self.langObject is not None

    def do_EOF(self, line):
        return True

    def help_EOF(self, line):
        print("exit the interpreter")

    def do_exit(self, line):
        return True

    def help_exit(self, line):
        print("exit the interpreter")

    def parseLangObj(self):
        if match(r"[Jj]?([aAvV]{3}|())[Ss]", self.lang) is not None:
            self.langObject = JavaScript("test")
            self.prompt = "JS > "

        elif match(r"[Pp]?[Hh][Pp]*", self.lang) is not None:
            self.langObject = PHP("test")
            self.prompt = "PHP > "

    def do_use(self, arg):
        self.lang = str(arg)
        self.parseLangObj()
        print(f"set language {self.lang}")

    def help_use(self):
        print("set the language to be used by future functions")

    def do_char(self, arg):
        if self.checkSet():
            self.langObject.string = str(arg)
            print(self.langObject.charCode(True))
        else:
            print(f"! no language set !")

    def help_char(self):
        print("prints the string in ascii form")

    def do_code(self, arg):
        if match(r"[Jj]?([aAvV]{3}|())[Ss]", self.lang) is not None:
            self.langObject.string = str(arg)
            print(self.langObject.charCode(False))
        else:
            print(f"! code is only defined for JavaScript !")

    def help_code(self):
        print(
            "prints the string in ascii form with String.fromCodePoint, only for JavaScript"
        )

    def do_hex(self, arg):
        if self.checkSet():
            self.langObject.string = str(arg)
            print(self.langObject.fromHex())
        else:
            print(f"! no language set !")

    def help_hex(self):
        print("prints the string in hex form")

    def do_url(self, arg):
        if self.checkSet():
            self.langObject.string = str(arg)
            print(self.langObject.urlDecode())
        else:
            print(f"! no language set !")

    def help_url(self):
        print("prints string URL encoded")

    def do_b64(self, arg):
        if self.checkSet():
            self.langObject.string = str(arg)
            print(self.langObject.base64(False))
        else:
            print(f"! no language set !")

    def help_b64(self):
        print("prints the string in base64 form")

    def do_urlb64(self, arg):
        if self.checkSet():
            self.langObject.string = str(arg)
            print(self.langObject.base64(True))
        else:
            print(f"! no language set !")

    def help_urlb64(self):
        print("prints the string in url safe base64 form")

    def interrupt(self, line):
        print("^C")

    def cmdloop(self, intro=None):
        if self.lang != "":
            self.do_use(self.lang)
        while True:
            try:
                super(Interpreter, self).cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("^C")


def runInterpreter(interpreter: Interpreter):
    interpreter.cmdloop()
