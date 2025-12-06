# Predictive parsing table - maps (non-terminal, input symbol) to production rules
# Built as nested dictionary for O(1) lookup time
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

# Set of non-terminals for quick membership checking
NON_TERMINALS_SET = {'E', 'Q', 'T', 'R', 'F'}

def parse(input_string):
    # Initialize stack with $ (bottom) and start symbol E (top)
    stack = ['$', 'E']
    input_index = 0
    
    # Set initial lookahead symbol from input
    if input_index < (len(input_string)):
        lookahead = input_string[input_index]
    else:
        lookahead = '$'
    
    # Main parsing loop - continues until accept or reject
    while True:
        # CHECKPOINT 1: Accept condition - both stack and input at $
        if stack[-1] == '$' and lookahead == '$':
            print('stack:', stack)
            print('String is accepted/ valid.')
            return True
        
        # CHECKPOINT 2: Terminal matching - top of stack matches current input
        elif stack[-1] == lookahead:
            print('stack:', stack)
            
            # Pop matched terminal from stack and advance input
            stack.pop()
            input_index += 1
            
            # Update lookahead, handle end of input with try-except
            try:
                lookahead = input_string[input_index]
            except IndexError: 
                lookahead = '$'
        
        # CHECKPOINT 3: Non-terminal expansion - lookup production in table
        elif stack[-1] in NON_TERMINALS_SET:
            print('stack:', stack)
            
            non_term = stack.pop()
            # Use .get() to safely check if entry exists in parsing table
            rule_rhs = parsing_table[non_term].get(lookahead, None)
            
            # If no entry in table, syntax error
            if rule_rhs is None:
                print('stack: ', stack)
                return print("String is not accepted/ invalid.")
            
            # Epsilon production - push to show it, then it gets removed next iteration
            elif rule_rhs == 'ε':
                stack.append('ε')
            
            # Push production onto stack in reverse order
            # reversed() ensures leftmost symbol ends up on top
            else:
                stack.extend(reversed(rule_rhs))
        
        # Handle epsilon - appears briefly then disappears
        elif stack[-1] == 'ε':
            print('stack:', stack)
            stack.pop()  # Remove epsilon immediately
        
        # Error case - top is terminal but doesn't match input
        else:
            print('String is not accepted/ invalid.')
            return False

# Main program - handles user input
if __name__ == "__main__":
    inpstring = input("inputstring: ")
    
    # Auto-append $ if user forgot it
    if inpstring and inpstring[-1] != '$':
        inpstring += '$'
    
    parse(inpstring)
