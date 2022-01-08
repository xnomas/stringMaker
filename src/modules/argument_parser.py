import argparse


def parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stringMaker",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--str",
        help="the original string you wish to represent",
        type=str,
    )
    parser.add_argument(
        "--interpreter",
        help="run the interpreter",
        action="store_true",
    )
    parser.add_argument(
        "--lang",
        help="set the language that the string will be represented in",
        type=str,
    )
    parser.add_argument(
        "--char",
        help="represent the string in ascii in given language",
        action="store_true",
    )
    parser.add_argument(
        "--code-point",
        help="specific to JavaScript, use String.fromCodePoint",
        action="store_true",
    )
    parser.add_argument(
        "--b64",
        help="represent the string in base64 in given language",
        action="store_true",
    )
    parser.add_argument(
        "--url-safe",
        help="use with --b64, sets encoding to url safe base64",
        action="store_true",
    )
    parser.add_argument(
        "--url-encode",
        help="represent the string URL encoded in given language",
        action="store_true",
    )
    parser.add_argument(
        "--hex",
        help="represent the string in hex in given language",
        action="store_true",
    )
    parser.add_argument("--supported", help="supported languages", action="store_true")

    return parser
