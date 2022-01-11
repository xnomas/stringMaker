import re

from modules.JavaScript import JavaScript
from modules.PHP import PHP
from modules.interpreter import Interpreter, runInterpreter
from modules.argument_parser import parser


def Main():
    argp = parser()

    args = argp.parse_args()
    settings = {
        "string": args.str,
        "interpreter": args.interpreter,
        "lang": args.lang,
        "char": args.char,
        "code_point": args.code_point,
        "b64": args.b64,
        "url_safe": args.url_safe,
        "url_decode": args.url_decode,
        "hex": args.hex,
        "supported": args.supported,
    }

    langs = {"JS": r"[Jj]?([aAvV]{3}|())[Ss].*", "PHP": r"[Pp]?[Hh][Pp].*"}

    # init the object in function scope
    langObj = None
    setLang = ""

    if settings["supported"]:
        print("[?] Supported langs: JavaScript PHP")
        return True

    if not settings["string"] and not settings["interpreter"]:
        print("[!] No string provided, use --str")
        return False
    elif settings["interpreter"]:
        runInterpreter(Interpreter(""))
        return True

    if not settings["lang"] and not settings["interpreter"]:
        print("[!] No language set, use --lang")
        return False
    elif settings["interpreter"]:
        runInterpreter(Interpreter(""))
        return True

    if re.match(langs["JS"], settings["lang"]) is not None:
        langObj = JavaScript(settings["string"])
        setLang = "JS"
    elif re.match(langs["PHP"], settings["lang"]) is not None:
        langObj = PHP(settings["string"])
        setLang = "PHP"
    else:
        print("[!] unknown language, use --supported")

    if settings["char"]:
        print(langObj.charCode(True))
    elif settings["code_point"] and setLang == "JS":
        print(langObj.charCode(False))
    elif settings["code_point"] and setLang != "JS":
        print("[!] --code-point only works with JavaScript")

    if settings["hex"]:
        print(langObj.fromHex())

    if settings["b64"]:
        print(langObj.base64(False))
    elif settings["b64"] and settings["url_safe"]:
        print(langObj.base64(True))

    if settings["url_decode"]:
        print(langObj.urlDecode())

    return True


if __name__ == "__main__":
    Main()
