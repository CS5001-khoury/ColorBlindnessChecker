""" 
Student: YOUR NAME
Term: SEMESTER

Compares two colors, both normal, and with various color blindness conditions applied

"""
import math

MIN_DIFFERENCE = .10


def delta(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> float:
    """Uses the following formula to compare two different colors. This
    is a simplified way to compare two colors as it doesn't take
    into account hue or saturation differences. If you are curious
    about a more standard approach, one should look up the CIEDE2000 formula. 

    euclidean = (R_1 - R_2)^2 + (G_1 - G_2)^2 + (B_1 - B2)^2
    euclidean = sqrt(euclidean)  # the two lines are known as the euclidean distance and common for a lot of things
    scaled = floor(euclidean) / 441  #scales the distance between 0 and 1


    Examples:
        >>> delta(255, 255, 255, 255, 255, 255)
        0.0
        >>> delta(255, 255, 255, 0, 0, 0)
        1.0
        >>> round(delta(255, 255, 255, 127, 127, 127), 2) # round helps with floating point errors
        0.5
        >>> delta(0, 0, 0, 0, 0, 0)
        1.0

    Args:
        red_one (int): a color range between 0 and 255 representing the red for the first color
        green_one (int): a color range between 0 and 255 representing the green for the first color
        blue_one (int):a color range between 0 and 255 representing the blue for the first color
        red_two (int): a color range between 0 and 255 representing the red for the second color
        green_two (int): a color range between 0 and 255 representing the green for the second color
        blue_two (int): a color range between 0 and 255 representing the blue for the second color


    Returns:
        float: a value between 0 and 1, representing how different colors are. Lower numbers are more similar. 
    """
    return int(math.sqrt((red_one - red_two) ** 2 + 
                         (green_one - green_two) ** 2 + 
                         (blue_one - blue_two) ** 2)) / 441


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """Converts an RBG color to a HEX string value often used for HTML color pallets. 

    The conversion format string is  f"#{red:02x}{green:02x}{blue:02x}"

    Examples:
    >>> rgb_to_hex(255, 255, 255)
    '#ffffff'
    >>> rgb_to_hex(0, 0, 0)
    '#000000'
    >>> rgb_to_hex(127, 127, 127)
    '#7f7f7f'
    >>> rgb_to_Hex(255, 0, 0)
    '#ff0000'

    Args:
        red (int): red color value
        green (int): green color value
        blue (int): blue color value

    Returns:
        str: the formatted string
    """
    return f"#{red:02x}{green:02x}{blue:02x}"


# Add your functions here 
# Remember write one at a time! (we recommend start with different_colors)
# Follow - define, document, implement, and test - with every function! 


def main():
    # while this main isn't the primary entry point of the program
    # you can use this mean to help test as you develop, this is common practice
    if round(delta(255, 255, 255, 127, 127, 127), 2) != .50:
        print("Fail check delta expected return .5")


if __name__ == "__main__":
    main()
