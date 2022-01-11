"""
Module to turn the input string into an expression,
that will return the same string in PHP.
"""

from base64 import b64encode, urlsafe_b64encode
from urllib.parse import quote_plus


class PHP(object):
    """PHP object"""

    def __init__(self, string: str):
        super(PHP, self).__init__()
        self.string = string

    def charCode(self, pointless: bool) -> str:
        expression = ""
        length = len(self.string)

        for index in range(length):
            current = f"chr({str(ord(self.string[index]))})"

            if index == length - 1:
                expression = expression + current
                break
            expression = expression + current + "."

        return expression

    def base64(self, url_safe: bool) -> str:
        if not url_safe:
            return f"base64_decode('{b64encode(bytes(self.string,'utf-8')).decode()}',false)"
        else:
            """
            Taken from https://github.com/yowcow/php-mime-base64-urlsafe/blob/master/lib/MIME/Base64URLSafe.php
            """
            expression = """function urlsafe_b64decode($data){$data=preg_replace('/[\t-\x0d\s]/','',strtr($data, '-_', '+/'));"""
            expression = (
                expression
                + """$mod4=strlen($data)%4;if($mod4){$data.=substr('====',$mod4);}return base64_decode($data,false);}"""
            )
            return (
                expression
                + f";urlsafe_b64decode('{urlsafe_b64encode(bytes(self.string,'utf-8')).decode()}')"
            )

    def urlDecode(self) -> str:
        return f"urldecode('{quote_plus(self.string)}')"

    def fromHex(self) -> str:
        hexes = "".join([str(hex(ord(x)).strip("0x")) for x in self.string])
        return f"pack('H*', '{hexes}');"
