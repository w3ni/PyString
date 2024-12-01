import argparse

parser = argparse.ArgumentParser(
    description="String manipulation tool", 
    usage=' python/python3 %(prog)s --str <string> --o <output_file>', 
    epilog='Example : python/python3 %(prog)s --str "abhishek" --o output.txt'
)

parser.add_argument("--str", type=str, help="Enter your string", required=True)
parser.add_argument("--o", type=str, help="Enter your output file name")

args = parser.parse_args()

input_str = args.str
output_file = args.o

print()
print("=====================================")
print("\n--------[ PyString v1.0]-----------")
print("\n------String Manipulation Tool-----")
print("\n GitHub : https://github.com/w3ni")
print("\n===================================")
print()

while True:
    try:
        print("-" * 70)
        op = input("Enter Your Operation / 1 for exit / 2 for show all options : ").strip().lower()

        result = None

        if op == 'capitalize':
            result = f"Capitalize string: {input_str.capitalize()}"
        elif op == 'casefold':
            result = f"Casefold string: {input_str.casefold()}"
        elif op == 'center':
            cen = int(input("Enter length to center: "))
            result = f"Center string: {input_str.center(cen)}"
        elif op == 'upper':
            result = f"Uppercased string: {input_str.upper()}"
        elif op == 'lower':
            result = f"Lowercased string: {input_str.lower()}"
        elif op == 'reverse':
            result = f"Reversed string: {input_str[::-1]}"
        elif op == 'count':
            word = input("Enter word for count: ")
            result = f"Word '{word}' Total count: {input_str.count(word)}"
        elif op == 'encode':
            format = input("Provide encoding format (default utf-8): ")
            try:
                result = f"Encoded string: {input_str.encode(format or 'utf-8')}"
            except LookupError:
                result = "Error: Invalid encoding format provided."
        elif op == 'maketrans':
            value1 = input('Enter characters to replace (e.g., abc): ')
            value2 = input('Enter replacement characters (e.g., 123): ')
            if len(value1) != len(value2):
                result = "Error: Both strings must have the same length for translation."
            else:
                trans_table = str.maketrans(value1, value2)
                translated_str = input_str.translate(trans_table)
                result = f"Translation table: {trans_table}\nTranslated string: {translated_str}"
        elif op == 'endswith':
            word = input("Enter word to check if string ends with: ")
            result = f"Does the string end with '{word}'? {input_str.endswith(word)}"
        elif op == 'find':
            word = input("Enter the substring to find: ")
            result = f"Find substring '{word}': {input_str.find(word)}"
        elif op == 'index':
            word = input("Enter the substring to find the index: ")
            result = f"Index of '{word}': {input_str.index(word)}"
        elif op == 'isalnum':
            result = f"Is alphanumeric: {input_str.isalnum()}"
        elif op == 'isalpha':
            result = f"Is alphabetic: {input_str.isalpha()}"
        elif op == 'isascii':
            result = f"Is ASCII: {input_str.isascii()}"
        elif op == 'isdecimal':
            result = f"Is decimal: {input_str.isdecimal()}"
        elif op == 'isdigit':
            result = f"Is digit: {input_str.isdigit()}"
        elif op == 'isidentifier':
            result = f"Is identifier: {input_str.isidentifier()}"
        elif op == 'islower':
            result = f"Is lower: {input_str.islower()}"
        elif op == 'isnumeric':
            result = f"Is numeric: {input_str.isnumeric()}"
        elif op == 'isprintable':
            result = f"Is printable: {input_str.isprintable()}"
        elif op == 'isspace':
            result = f"Is space: {input_str.isspace()}"
        elif op == 'istitle':
            result = f"Is title: {input_str.istitle()}"
        elif op == 'isupper':
            result = f"Is upper: {input_str.isupper()}"
        elif op == 'join':
            join_str = input("Enter string to join with: ")
            result = f"Joined string: {join_str.join(input_str)}"
        elif op == 'ljust':
            width = int(input("Enter width to justify: "))
            result = f"Left-justified string: {input_str.ljust(width)}"
        elif op == 'lstrip':
            result = f"Left-stripped string: {input_str.lstrip()}"
        elif op == 'strip':
            result = f"Stripped string: {input_str.strip()}"
        elif op == '1':
            break
        elif op == '2':
            print("\nAvailable operations: capitalize, casefold, center, upper, lower, reverse, count, encode, endswith, find, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lstrip, strip")
        else:
            print("Method not found!")

        if result:
            print(result)
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(result + "\n")
                    print(f"- Result written to {output_file} -")

    except ValueError:
        print("Invalid input. Please try again.")
    except KeyboardInterrupt:
        print("\n[ Program interrupted by user ]")
        break
    except Exception as e:
        print(f"Error: {e}")

print("\nThank you for using PyString!")
