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
    if input_index < (len(input_string)):
        lookahead = input_string[input_index]
    else:
        lookahead = '$'
    while True:
        if stack[-1] == '$' and lookahead == '$':
            print('stack:', stack)
            #print('lookahead: ', lookahead)
            print('String is accepted/ valid.')
            return True
        elif stack[-1] == lookahead:
            print('stack:', stack)
            #print('lookahead: ', lookahead)
            
            stack.pop()
            input_index += 1
            
            try:
                lookahead = input_string[input_index]
            except IndexError: 
                lookahead = '$'
                    
        elif stack[-1] in NON_TERMINALS_SET:
            print('stack:', stack)
            #print('lookahead: ', lookahead)
            
            non_term = stack.pop()
            rule_rhs = parsing_table[non_term].get(lookahead, None)
            
            #print('nonterm: ', non_term)
            #Sprint('rulerhs: ', rule_rhs)
            
            if rule_rhs is None:
                print('stack: ', stack)
                return print("String is not accepted/ invalid.")
            elif rule_rhs == 'ε':
                pass
            else:
                stack.extend(reversed(rule_rhs))
        else:
            print('String is not accepted/ invalid.')
            return False
            
            
            
        
    

if __name__ == "__main__":
    
    #print(parsing_table['F']['a'])
    
    inpstring = input("inputstring: ")
    if inpstring and inpstring[-1] != '$':
        inpstring += '$'
        
    parse(inpstring)