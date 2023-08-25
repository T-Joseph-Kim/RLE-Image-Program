from console_gfx import ConsoleGfx


def to_hex_string(data):
    hex_string = ""  # set a variable to an empty string that can be added onto
    for item in data:
        if 0 <= item < 10:  # if data list includes an integer 0 to 9, this converts it to a string
            hex_string += str(item)
        if item == 10:  # series of if statements for integers 10 to 15 to convert to letter string
            item = 'a'
            hex_string += item
        if item == 11:
            item = 'b'
            hex_string += item
        if item == 12:
            item = 'c'
            hex_string += item
        if item == 13:
            item = 'd'
            hex_string += item
        if item == 14:
            item = 'e'
            hex_string += item
        if item == 15:
            item = 'f'
            hex_string += item  # this expression in all the if statements add onto the empty hex_string
    return hex_string


def count_runs(flat_data):
    current = flat_data[0]  # set up current, count, and number of sets
    count = 1  # count is equal to 1 because it starts on the first number of the list
    num_sets = 1  # num_sets is equal to 1 because I do not know if the input will begin with a single indifferent #

    for item in flat_data[1:]:
        if current == item:
            count += 1  # increments count in order to keep track of the number of times an integer repeats
        else:  # when the current number does not equal the item, current is set to represent item
            current = item
            count = 1
            num_sets += 1
        if count >= 16:  # special case since a number cannot repeat more than 15 times, resets count
            count = 1
            num_sets += 1

    return num_sets


def encode_rle(flat_data):
    en_list = []  # similar to count_runs, but added a variable for an empty list
    current = flat_data[0]
    count = 1
    for item in flat_data[1:]:  # start from index 1, ignoring the index 0, to test for equality
        if current == item:  # simply if current is equal to item, count is incremented
            count += 1
        else:
            en_list.append(count)  # append functions placed before the reset of current and count to keep track
            en_list.append(current)
            current = item
            count = 1
        if count == 15:
            en_list.append(count)  # special case for 15 repetitions, resets count while also appending the currents
            en_list.append(current)
            count = 0
    en_list.append(count)  # lastly, append the last count/current when there are no more items left to assess
    en_list.append(current)
    return en_list


def get_decoded_length(rle_data):
    dec_len = 0  # set a variable for decoded_length, set it to 0
    for item in rle_data[0::2]:  # skipping in increments of two to assess the length values
        dec_len += item  # increment dec_len by the length values
    return dec_len


def decode_rle(rle_data):
    dec_data = []  # empty variable for final result
    value = []  # value for values in the list
    count = []  # count for lengths in the list

    for item in rle_data[0::2]:  # skips in increments of two to append length values to count variable
        count.append(item)
    for item in rle_data[1::2]:  # skips in increments of two starting from index one to append values to value variable
        value.append(item)
    len_data = len(value)  # len function used to determine the length of the list
    for val in range(len_data):  # range function used to run a for loop for however the length of the list
        dec_data.extend([value[val]] * count[val])
    return dec_data


def string_to_data(data_string):
    data = []  # variable for output
    str_list = []
    str_list[:0] = data_string  # this line changes the data_string to a list of strings
    for item in str_list:  # series of if statements to convert each string item to an integer
        if item == '0':
            data.append(0)
        if item == '1':
            data.append(1)
        if item == '2':
            data.append(2)
        if item == '3':
            data.append(3)
        if item == '4':
            data.append(4)
        if item == '5':
            data.append(5)
        if item == '6':
            data.append(6)
        if item == '7':
            data.append(7)  # data.append function used to add integers to the empty data list
        if item == '8':
            data.append(8)
        if item == '9':
            data.append(9)
        if item == 'a':
            data.append(10)
        if item == 'b':
            data.append(11)
        if item == 'c':
            data.append(12)
        if item == 'd':
            data.append(13)
        if item == 'e':
            data.append(14)
        if item == 'f':
            data.append(15)
    return data


def to_rle_string(rle_data):  # translates RLE data into human-readable representation
    rle_string = ""  # variable for final result
    rle_str_list = []  # string list to be translated to single string
    count = []  # list for just count values
    hex_val = []  # list for just hex values
    for item in rle_data[0::2]:  # for loop for appending count values into count list variable
        item = str(item)
        count.append(item)
    for item in rle_data[1::2]:  # for loop for appending hex values into list while translating to hex characters
        if item == 10:
            item = "a:"
        elif item == 11:
            item = "b:"
        elif item == 12:
            item = "c:"  # added colon to hex character to input delimiter
        elif item == 13:
            item = "d:"
        elif item == 14:
            item = "e:"
        elif item == 15:
            item = "f:"
        else:
            item = str(item) + ":"  # if hex value is an integer, convert to string and add delimiter
        hex_val.append(item)
    length = len(count)
    for value in range(length):  # for loop to combine count and hex values into rle_str_list
        rle_str_list.extend([count[value]] + [hex_val[value]])
    for item in rle_str_list:  # for loop to add to rle_string (final result)
        rle_string += item
    rle_string = rle_string[:-1]  # removes colon at the end
    return rle_string


def string_to_rle(rle_string):
    rle_list = []  # variable for final result
    rle_str_split = rle_string.split(":")  # split function to split string according to delimiter
    for item in rle_str_split:
        length = len(item)  # evaluates length of each string, for special cases
        if length == 3:
            just_count = item[:-1]  # sets variable for a string that only includes count value
            rle_list.append(int(just_count))  # adds count integer to rle_list
            just_hex = item[-1]  # sets variable for a string that only includes hex value
            if just_hex == 'a':
                rle_list.append(10)
            elif just_hex == 'b':
                rle_list.append(11)
            elif just_hex == 'c':
                rle_list.append(12) # if, elif, and else statements for translating hex to decimal and appending
            elif just_hex == 'd':
                rle_list.append(13)
            elif just_hex == 'e':
                rle_list.append(14)
            elif just_hex == 'f':
                rle_list.append(15)
            else:
                rle_list.append(int(just_hex))
        if length == 2:
            just_count = item[:-1]  # sets variable for a string that only includes count value
            rle_list.append(int(just_count))
            just_hex = item[-1]  # sets variable for a string that only includes hex value
            if just_hex == 'a':
                rle_list.append(10)
            elif just_hex == 'b':
                rle_list.append(11)
            elif just_hex == 'c':
                rle_list.append(12)  # if, elif, and else statements for translating hex to decimal and appending
            elif just_hex == 'd':
                rle_list.append(13)
            elif just_hex == 'e':
                rle_list.append(14)
            elif just_hex == 'f':
                rle_list.append(15)
            else:
                just_hex = int(just_hex)
                rle_list.append(just_hex)
    return rle_list


if __name__ == "__main__":
    print("Welcome to the RLE image encoder!\n")  # Welcome message
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)  # Displaying spectrum image
    print()

    image_data = None

    while True:
        print("RLE Menu\n--------\n"  # prints menu and options
              "0. Exit\n"
              "1. Load File\n"
              "2. Load Test Image\n"
              "3. Read RLE String\n"
              "4. Read RLE Hex String\n"
              "5. Read Data Hex String\n"
              "6. Display Image\n"
              "7. Display RLE String\n"
              "8. Display Hex RLE Data\n"
              "9. Display Hex Flat Data\n")
        user_option = int(input("Select a Menu Option: "))
        print()

        if user_option == 1:  # load image data from test files
            file_input = input("Enter name of file to load: ")
            print()
            image_data = ConsoleGfx.load_file(file_input)

        elif user_option == 2:  # ONLY load image data from test_image
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.\n")

        elif user_option == 3:  # reads RLE data from the user in decimal notation (with delimiters)
            rle_str_input = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(rle_str_input))
            print()

        elif user_option == 4:  # reads RLE data from user in hexadecimal notation (without delimiters)
            rle_hex_input = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(rle_hex_input))
            print()

        elif user_option == 5:  # reads raw/flat data from user (hexadecimal)
            flat_hex_input = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(flat_hex_input)
            print()

        elif user_option == 6:  # Displaying loaded image data
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)
            print()

        elif user_option == 7:  # translates current image data into human-readable RLE representation
            print("RLE representation: ", end="")
            print(to_rle_string(encode_rle(image_data)))
            print()

        elif user_option == 8:  # translates current image data into RLE hexadecimal representation (without delimiters)
            print("RLE hex values: ", end="")
            print(to_hex_string(encode_rle(image_data)))
            print()

        elif user_option == 9:  # translates current image data (flat) into hexadecimal representation, no delimiters
            print("Flat hex values: ", end="")
            print(to_hex_string(image_data))
            print()
        else:  # else statement for when user picks option 0
            break
