"""
Usage: from Encode import Encode
Example: Encode.decode("Khoor, xqlyhuvh!")

Encodes and decodes all of the letters in a message, while leaving other elements unchanged.
"""


class Encode:


    def encode(message, output = ""):
        """ All of the letters are moved 3 places further in ascii table. """
        for letter in message:
            if letter.isalpha() and ord(letter) + 3 <= Encode.find_range(letter)[1]:
                output += chr(ord(letter) + 3)
            elif letter.isalpha():
                output += chr(ord(letter) + 2 - Encode.find_range(letter)[1] + Encode.find_range(letter)[0])
            else:
                output += letter
        return output

    def decode(message, output = ""):
        """ All of the letters are moved 3 places backwards in ascii table. """
        for letter in message:
            if letter.isalpha() and ord(letter) - 3 >= Encode.find_range(letter)[0]:
                output += chr(ord(letter) - 3)
            elif letter.isalpha():
                output += chr(Encode.find_range(letter)[1] - 2 + (ord(letter) - Encode.find_range(letter)[0]))
            else:
                output += letter
        return output

    @staticmethod
    def find_range(letter):
        """ Selects the correct range, (65, 90) for CAPS and (97, 122) for lowercase letters """
        return (65, 90) if 65 <= ord(letter) <= 95 else (97, 122)


