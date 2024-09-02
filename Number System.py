"""
=======================================================================================================================
Creator:    Talha Ahmad
Dated:      15-08-2024
Language:   Python
=======================================================================================================================
This software can be used for:
 - Conversions between different number systems i.e. Decimal, Binary, Octal and Hexadecimal
 - Checks whether a given number is valid related to a system of numbers
 - Perform Arithmetic and boolean operations on numbers of various system
 Note: This program can only perform calculations on non-floating point values
=======================================================================================================================
"""
import tkinter as t
import tkinter.messagebox as tmsg


# Functions
def is_valid_decimal(value: str) -> bool:
    """ Function to check whether given number is decimal or not """
    for digit in value:
        if digit not in "0123456789":
            return False
    return True


def is_valid_binary(value: str) -> bool:
    """ Function to check whether given number is binary or not """
    if value == '':
        return True
    for digit in value:
        if digit not in "01":
            return False
    return True


def is_valid_octal(value: str) -> bool:
    """ Function ot check whether given number is octal or not """
    if len(value) == 0:
        return True
    for digit in value:
        if digit not in "0123456":
            return False
    return True


def is_valid_hexadecimal(value: str) -> bool:
    """ Function to check whether given number is hexadecimal or not """
    if value == '':
        return True
    for digit in value:
        if digit not in "0123456789ABCDEF":
            return False
    return True


# Decimal Class
class Decimal:
    def __init__(self):
        """ Constructor """
        self.__value = None
        self.__base = 10
        self.__list = []

    @property
    def list_decimal(self):
        if len(self.__list) > 0:
            return self.__list
        return None

    @property
    def value(self):
        """ Gets the value """
        if self.__value is not None:
            return self.__value
        return 'Undefined'

    @property
    def base(self) -> int:
        """ Gets the base """
        return self.__base

    @list_decimal.setter
    def list_decimal(self, value: int):
        """ Appends number to decimal list """
        self.__list.append(value)

    @value.setter
    def value(self, value: int):
        """ Sets the value """
        if isinstance(value, int):
            self.__value = value

    def to_binary(self):
        """ Function to convert the value to binary system """
        if self.value is not None:
            binary = Binary()
            binary.value = ''
            value = self.value
            while value > 0:
                binary.value = str(value % binary.base) + binary.value
                value = int(value / binary.base)
            return binary
        return None

    def to_octal(self):
        """ Function to convert the value to octal system """
        if self.value is not None:
            octal = Octal()
            octal.value = ''
            value = self.value
            while value > 0:
                octal.value = str(value % octal.base) + octal.value
                value = int(value / octal.base)
            return octal
        return None

    def to_hexadecimal(self):
        """ Function convert the value to hexadecimal system """
        if self.value is not None:
            hexadecimal = Hexadecimal()
            hexadecimal.value = ''
            value = self.value
            while value > 0:
                rem = value % hexadecimal.base
                if rem > 9:
                    rem = hexadecimal.to_alpha[rem]
                hexadecimal.value = str(rem) + hexadecimal.value
                value = int(value / hexadecimal.base)
            return hexadecimal
        return None


# Binary Class
class Binary:
    def __init__(self):
        """ Constructor """
        self.__value = None
        self.__list = []
        self.__base = 2

    @property
    def binary_list(self):
        """ Gets the list of binary numbers """
        if len(self.__list) > 0:
            return self.__list
        return None

    @property
    def raw_value(self):
        """ Gets the raw value """
        if self.__value is not None:
            return self.__value
        return 'Undefined'

    @property
    def value(self):
        """ Gets the readable value """
        if self.__value is not None:
            binary = ''
            for digit in self.__value:
                if digit:
                    binary += '1'
                else:
                    binary += '0'
            return binary
        return 'Undefined'

    @property
    def base(self) -> int:
        """ Gets the base """
        return self.__base

    @binary_list.setter
    def binary_list(self, binary):
        """ Appends the value to binary list """
        if isinstance(binary, str) and is_valid_binary(binary) and len(binary) > 0:
            self.__list.append(binary)

    @value.setter
    def value(self, value: str):
        """ Sets the value """
        if isinstance(value, str) and is_valid_binary(value):
            # Converting the given value to a boolean list
            value_list = [False, True]
            self.__value = []
            for bit in value:
                self.__value.append(value_list[int(bit)])

    def to_decimal(self):
        """ Function to convert the value to decimal system """
        if self.value is not None:
            power = len(self.value) - 1
            decimal = Decimal()
            decimal.value = 0
            for digit in self.value:
                decimal.value += int(digit) * self.base ** power
                power -= 1
            return decimal
        return None

    def to_octal(self):
        """ Function to convert the value to octal system """
        if self.value is not None:
            decimal = self.to_decimal()
            octal = decimal.to_octal()
            return octal
        return None

    def to_hexadecimal(self):
        """ Function to convert the value to hexadecimal system """
        if self.value is not None:
            decimal = self.to_decimal()
            hexadecimal = decimal.to_hexadecimal()
            return hexadecimal
        return None


# Octal Class
class Octal:
    def __init__(self):
        """ Constructor """
        self.__value = None
        self.__list = []
        self.__base = 8

    @property
    def list_octal(self):
        """ Gets the list of octal numbers """
        if len(self.__list) > 0:
            return self.__list
        return None

    @property
    def value(self):
        """ Gets the value """
        if self.__value is not None:
            return self.__value
        return 'Undefined'

    @property
    def base(self) -> int:
        return self.__base

    @list_octal.setter
    def list_octal(self, octal: str):
        if is_valid_octal(octal) and len(octal) > 0:
            self.__list.append(octal)

    @value.setter
    def value(self, value: str):
        if isinstance(value, str) and is_valid_octal(value):
            self.__value = value

    def to_decimal(self):
        """ Function to convert the value to decimal system """
        if self.value is not None:
            power = len(self.value) - 1
            decimal = Decimal()
            decimal.value = 0
            for digit in self.value:
                decimal.value += int(digit) * self.base ** power
                power -= 1
            return decimal
        return None

    def to_binary(self):
        """ Function to convert the value to binary system """
        if self.value is not None:
            decimal = self.to_decimal()
            binary = decimal.to_binary()
            return binary
        return None

    def to_hexadecimal(self):
        """ Function to convert the value to hexadecimal system """
        if self.value is not None:
            decimal = self.to_decimal()
            hexadecimal = decimal.to_hexadecimal()
            return hexadecimal
        return None


# Hexadecimal class
class Hexadecimal:
    def __init__(self):
        """ Constructor """
        self.__value = None
        self.__base = 16
        self.__list = []
        self.__to_alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        self.__from_alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    @property
    def list_hexadecimal(self):
        """ Gets the list of hexadecimal numbers """
        if len(self.__list) > 0:
            return self.__list
        return None

    @property
    def base(self):
        """ Gets the base """
        return self.__base

    @property
    def value(self):
        """ Gets the value """
        if self.__value is not None:
            return self.__value
        return 'Undefined'

    @property
    def to_alpha(self) -> dict:
        return self.__to_alpha

    @property
    def from_alpha(self) -> dict:
        return self.__from_alpha

    @list_hexadecimal.setter
    def list_hexadecimal(self, value: str):
        """ Appends value to the hexadecimal list """
        if is_valid_hexadecimal(value) and len(value) > 0:
            self.__list.append(value)

    @value.setter
    def value(self, value: str):
        """ Function to set the value """
        if isinstance(value, str) and is_valid_hexadecimal(value):
            self.__value = value

    def to_decimal(self):
        """ Function to convert the value to decimal system """
        if self.value is not None:
            power = len(self.value) - 1
            decimal = Decimal()
            decimal.value = 0
            for digit in self.value:
                if digit not in '0123456789':
                    decimal.value += self.from_alpha[digit] * self.base ** power
                else:
                    decimal.value += int(digit) * self.base ** power
                power -= 1
            return decimal
        return None

    def to_binary(self):
        """ Function to convert the value to binary """
        if self.value is not None:
            decimal = self.to_decimal()
            binary = decimal.to_binary()
            return binary
        return None

    def to_octal(self):
        """ Function to convert the value to octal """
        if self.value is not None:
            decimal = self.to_decimal()
            octal = decimal.to_octal()
            return octal
        return None


# Conversion GUI class
class ConvertApp(t.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x380")
        self.maxsize(400, 400)
        self.minsize(250, 350)
        self.title("NS Convert")
        self.iconbitmap("convert-icon.ico")
        self.__number = t.StringVar()
        self.__from_selection = t.IntVar()
        self.__to_selection = t.IntVar()

    def set_appearance(self):
        """ Method to set the UI """

        # Title - Heading
        t.Label(
            self,
            text="Welcome to the Conversion App",
            bg="green",
            fg="lime",
            font="forte 15 italic"
        ).pack(fill='x')

        # Entry Box
        t.Entry(
            self,
            textvariable=self.__number,
            borderwidth=2,
            bg="grey",
            font="system 10",
            fg="white",
        ).pack(
            fill='x',
            padx=5,
            pady=5
        )

        # Conversion Selection
        txt = [
            "From",
            "To"
        ]
        for count in range(2):
            t.Label(
                self,
                text=txt[count],
                fg="white",
                bg="red",
                font="cambria 10 bold"
            ).pack(fill='x')
            self.__radiobuttons(count)

        # Button
        t.Button(
            self,
            text="Convert !",
            command=self.__action,
            border=0,
            font="system 25 bold",
            fg="blue",
        ).pack(
            fill='x',
            pady=5
        )

    def __action(self):
        """ Method to perform conversions between decimal, binary, octal and hexadecimal number systems """

        # Get the required values
        value = self.__number.get()
        _from = self.__from_selection.get()
        _to = self.__to_selection.get()

        # Variables
        ns_label = [
            "Decimal",
            "Binary",
            "Octal",
            "Hexadecimal"
        ]

        # Convert
        if _from != _to and (_from != 0 or _to != 0):
            if len(value) > 0:
                invalid_value_error = False
                converted = None

                match _from:
                    case 1:     # Decimal
                        if is_valid_decimal(value):
                            number = Decimal()
                            number.value = int(value)
                            match _to:
                                case 2:     # Binary
                                    converted = number.to_binary()
                                case 3:     # Octal
                                    converted = number.to_octal()
                                case 4:     # Hexadecimal
                                    converted = number.to_hexadecimal()
                        else:
                            invalid_value_error = True
                    case 2:     # Binary
                        if is_valid_binary(value):
                            number = Binary()
                            number.value = value
                            match _to:
                                case 1:     # Decimal
                                    converted = number.to_decimal()
                                case 3:     # Octal
                                    converted = number.to_octal()
                                case 4:     # Hexadecimal
                                    converted = number.to_hexadecimal()
                        else:
                            invalid_value_error = True
                    case 3:     # Octal
                        if is_valid_octal(value):
                            number = Octal()
                            number.value = value
                            match _to:
                                case 1:     # Decimal
                                    converted = number.to_decimal()
                                case 2:     # Binary
                                    converted = number.to_binary()
                                case 4:     # Hexadecimal
                                    converted = number.to_hexadecimal()
                        else:
                            invalid_value_error = True
                    case 4:     # Hexadecimal
                        if is_valid_hexadecimal(value):
                            number = Hexadecimal()
                            number.value = value
                            match _to:
                                case 1:     # Decimal
                                    converted = number.to_decimal()
                                case 2:     # Binary
                                    converted = number.to_binary()
                                case 3:     # Octal
                                    converted = number.to_octal()
                        else:
                            invalid_value_error = True
                if not invalid_value_error:     # No error case
                    tmsg.showinfo(
                        "Result",
                        f"{ns_label[_from - 1]} number is \"{value}\"\n{ns_label[_to - 1]} number is \"{converted.value}\""
                    )
                else:   # Error case
                    tmsg.showerror(
                        "Value Error",
                        f"You have entered wrong {ns_label[_from - 1]} number."
                    )
            else:   # Error case
                tmsg.showerror(
                    "Value Error",
                    "You have to enter a number before conversion."
                )
        else:   # Error case
            tmsg.showerror(
                "Selection Error",
                "Please select the number system conversion options correctly."
            )

    def __radiobuttons(self, selection_type):
        """ Method to create radiobuttons """
        txt = [
            "Decimal",
            "Binary",
            "Octal",
            "Hexadecimal"
        ]
        var = [
            self.__from_selection,
            self.__to_selection
        ]
        for count in range(4):
            button = t.Radiobutton(
                self,
                text=txt[count],
                value=count + 1,
                fg="green",
                variable=var[selection_type],
                font="serif 8 bold"
            )
            button.pack(
                fill='x',
                padx=1
            )


# Functions - Calculations
def add_binary(binary: list[str]) -> Binary:
    """ Function to sum up all binary numbers """
    _sum = Decimal()
    _bin = Binary()
    _sum.value = 0
    for number in binary:
        _bin.value = number
        _sum.value += _bin.to_decimal().value
    return _sum.to_binary()


def add_octal(octal: list[str]) -> Octal:
    """ Function to sum up all octal numbers """
    _sum = Decimal()
    _oct = Octal()
    _sum.value = 0
    for number in octal:
        _oct.value = number
        _sum.value += _oct.to_decimal().value
    return _sum.to_octal()


def add_hexadecimal(hexadecimal: list[str]) -> Hexadecimal:
    """ Function to sum up all hexadecimal numbers """
    _sum = Decimal()
    _hexa = Hexadecimal()
    _sum.value = 0
    for number in hexadecimal:
        _hexa.value = number
        _sum.value += _hexa.to_decimal().value
    return _sum.to_hexadecimal()


def add_decimal(decimal: list[int]) -> Decimal:
    """ Function to sum up all decimal numbers """
    _sum = Decimal()
    _sum.value = 0
    for number in decimal:
        _sum.value += number
    return _sum


# NS Operations app
class ArithmeticApp(t.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x400")
        self.title("NS Arithmetic")
        self.__number = t.StringVar()

    def set_appearance(self):
        """ Method to set the appearance of the app """

        # Title - Heading
        t.Label(
            self,
            text="Welcome to the Arithmetic App",
            bg="grey",
            fg="black",
            font="forte 15 italic"
        ).pack(fill='x')

        # Number Input


# Testing
if __name__ == '__main__':
    sample_app = ConvertApp()
    sample_app.set_appearance()
    sample_app.mainloop()

    # sample_app = ArithmeticApp()
    # sample_app.set_appearance()
    # sample_app.mainloop()
