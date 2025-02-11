class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        splitted = queryIP.split('.')

        if len(splitted) != 4:
            splitted = queryIP.split(':')

        length = len(splitted)

        if length == 4:
            for n in splitted:
                try: 
                    if len(n) > 1 and n[0] == "0":
                        return "Neither"

                    n = int(n)

                    if n < 0 or n > 255:
                        return "Neither"
                except (ValueError, TypeError):
                    return "Neither"
            return "IPV4"
        elif length == 8:
            for n in splitted:
                if len(n) < 1 or len(n) > 4:
                    return "Neither"

                try: 
                    n = int(n, 16)
                except (ValueError, TypeError):
                    return "Neither"
            return "IPV6"



        return "Neither"
