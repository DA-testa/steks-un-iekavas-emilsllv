# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # enumerate atdod kārtas numuru un simbolu
        if next in "([{":
            # Process opening bracket, write your code here
            #jāpievieno struktūrai vērtība

            opening_brackets_stack.append(Bracket(next,i+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            # empty neeksistē
            # Matchc == are_matching
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next):
                return i+1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"


def main():
    # Printing answer, write your code here
    izvele = input("F or I:")
    if "I" in izvele:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
    elif "F" in izvele:
        fails = input("Name of the file:")
        with open("test/"+fails,"r") as file:
            text = file.read()
            mismatch = find_mismatch(text)
            print(mismatch)
    else :
        print("Input is not correct")

if __name__ == "__main__":
    main()
