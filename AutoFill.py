import keyboard


def write_card_number():
    keyboard.write("xxxx xxxx xxxx xxxn")


while True:
    keyboard.wait("ctrl+alt+z+c")
    keyboard.write("xxxx xxxx xxxx xxxn")
