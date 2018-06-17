# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False
    
        
def checking_brackets(initial_string):
    opening_brackets_stack = []
    
    for i, next in enumerate(text, start=1):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next,i))
            pass

        if next == ')' or next == ']' or next == '}':
            top = opening_brackets_stack.pop()
            if top.Match(next) == False:
                return i
                break
        
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position
    
    return 'Success'


if __name__ == "__main__":
    text = input()
    error_position = checking_brackets(text)
    print(error_position)
