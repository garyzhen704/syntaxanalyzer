parsing_table = {
    'E': {
        'a': 'TQ',
        '(': 'TQ'
    },
    'Q': {
        '+': '+TQ',
        '-': '-TQ',
        ')': 'ε',
        "$": 'ε'
    },
    'T': {
        'a': 'FR',
        '(': 'FR'           
    },
    'R': {
        '+': 'ε',
        '-': 'ε',
        '*': '*FR',
        '/': '/FR',
        ')': 'ε',
        '$': 'ε'
    },
    'F': {
        'a': 'a',
        '(': '(E)'
    }
}

NON_TERMINALS_SET = {'E', 'Q', 'T', 'R', 'F'}

def parse(input_string):
    stack = ['$', 'E']
    input_index = 0
    lookahead = input_string[input_index]
    while stack[-1] != '$' or lookahead != '$':
        print('stack:', stack)
        print('lookahead: ', lookahead)
        if stack[-1] == lookahead:
            stack.pop()
            input_index += 1
            
            lookahead = input_string[input_index]
        elif stack[-1] in NON_TERMINALS_SET:
            non_term = stack.pop()
            rule_rhs = parsing_table[non_term][lookahead]
            print('nonterm: ', non_term)
            print('rulerhs: ', rule_rhs)
            stack.extend(reversed(rule_rhs))
        else:
            return False
    return
            
            
            
        
    

if __name__ == "__main__":
    
    print(parsing_table['F']['a'])
    
    inpstring = input("inputstring: ")
    parse(inpstring)