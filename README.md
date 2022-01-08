# stringMaker
 A simple tool for string obfuscation and construction

## Installation

Simply git clone:
```
git clone https://github.com/xnomas/stringMaker
```

## Usage

The tool supports two modes:
1. Command line mode
2. Interpreter mode

For command line mode treat it like a standard UNIX app:
```
python stringMaker.py --help
usage: stringMaker [-h] [--str STR] [--interpreter] [--lang LANG] [--char] [--code-point] [--b64] [--url-safe] [--url-encode] [--hex] [--supported]

optional arguments:
  -h, --help     show this help message and exit
  --str STR      the original string you wish to represent (default: None)
  --interpreter  run the interpreter (default: False)
  --lang LANG    set the language that the string will be represented in (default: None)
  --char         represent the string in ascii in given language (default: False)
  --code-point   specific to JavaScript, use String.fromCodePoint (default: False)
  --b64          represent the string in base64 in given language (default: False)
  --url-safe     use with --b64, sets encoding to url safe base64 (default: False)
  --url-encode   represent the string URL encoded in given language (default: False)
  --hex          represent the string in hex in given language (default: False)
  --supported    supported languages (default: False)
```
To enter interpreter mode use `python stringMaker.py --interpreter`:

![interpreter](https://github.com/xnomas/stringMaker/blob/main/img/interpreter.png)

## Suggestions

If you have a suggestion, feel free to open an [issue](https://github.com/xnomas/stringMaker/issues) or see the [discussions tab](https://github.com/xnomas/stringMaker/discussions).


## Contributions

The tool is open source so contributions are welcome. I use the python-black linter.
