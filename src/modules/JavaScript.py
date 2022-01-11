"""
Module to turn the input string into an expression,
that will return the same string in JavaScript.
"""

from base64 import b64encode, urlsafe_b64encode
from urllib.parse import quote_plus


class JavaScript(object):
    """JavaScript object"""

    def __init__(self, string: str):
        super(JavaScript, self).__init__()
        self.string = string

    def charCode(self, char_allowed: bool) -> str:
        if char_allowed:
            expression = "String.fromCharCode("
        else:
            expression = "String.fromCodePoint("
        length = len(self.string)

        for index in range(length):
            current = str(ord(self.string[index]))

            if index == length - 1:
                expression = expression + current + ")"
                break
            expression = expression + current + ","

        return expression

    def base64(self, url_safe: bool) -> str:
        if not url_safe:
            return f"atob('{b64encode(bytes(self.string,'utf-8')).decode()}')"
        else:
            return f"atob('{urlsafe_b64encode(bytes(self.string,'utf-8')).decode()}')"

    def urlDecode(self) -> str:
        return f"decodeURIComponent('{quote_plus(self.string)}')"

    def fromHex(self) -> str:
        # minified version of function that converts hex to string
        func = 'function h(e){let b,c="";for(let i=0;i<e.length;i+=2){b=parseInt(e.substr(i,2),16);if(b)c+=String.fromCharCode(b)}return c;}'
        # for each character in the string get ascii value, turn to hex, strip 0x and to string
        hexes = "".join([str(hex(ord(x)).strip("0x")) for x in self.string])

        return f"{func};h({hexes})"
