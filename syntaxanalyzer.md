# **CPSC 323 \- PROJECT 2**

Project 2 consists of one program to be submitted/uploaded online on Canvas.

You are allowed to write your project in C/C++/Java/Python etc. but you ARE NOT allowed to use Yacc, Bison, or any other items similar that assists in the creation of compilers.

Given the following context free grammar (CFG) and the parsing table, write a program to trace input strings over the alphabet {a, \+, \-, \*, /, (, )} and ending with $.

## **1\. Project Requirements**

**\[60 points\]** Write a program to trace an input string given by the user. Save it as Prog1 and upload it in canvas (either the zip file or GitHub link). Test your program with the following 3 input strings:

1. (a+a)\*a$  
2. a\*(a/a)$  
3. a(a+a)$

**\[20 points\]** Show the content of the stack implementation / stack flow after each match.

**\[20 points\]** Report file \- Your report file should contain explanation of your code, in-built functions used, important checkpoints \[if it is present\], explanation should be short and crisp, output screenshot of your code and should not exceed more than 2 pages.

## **2\. Grammars and Tables**

Following is the grammar, and parsing table.

### **Given CFG (with left-recursion)**

* $E \\to E \+ T$  
* $E \\to E \- T$  
* $E \\to T$  
* $T \\to T \* F$  
* $T \\to T / F$  
* $T \\to F$  
* $F \\to (E)$  
* $F \\to a$

### **CFG (after removing left-recursion)**

* $E \\to TQ$  
* $Q \\to \+TQ$  
* $Q \\to \-TQ$  
* $Q \\to \\epsilon$  
* $T \\to FR$  
* $R \\to \*FR$  
* $R \\to /FR$  
* $R \\to \\epsilon$  
* $F \\to (E)$  
* $F \\to a$

### **First and Follow Table**

Non-Terminal | FIRST Set         | FOLLOW Set                 |
-------------|-------------------|----------------------------|
E            | ( , a             | ) , $                      |
Q            | + , - , ε         | ) , $                      |
T            | ( , a             | + , - , ) , $              |
R            | * , / , ε         | + , - , ) , $              |
F            | ( , a             | + , - , * , / , ) , $      |

### **Predictive Parsing Table**

*(Note: Blank cells in the table represent syntax errors)*

STATE | +     | -     | *     | /     | a     | (     | )     | $     
------|-------|-------|-------|-------|-------|-------|-------|-------
E     |       |       |       |       | TQ    | TQ    |       |       
Q     | +TQ   | -TQ   |       |       |       |       | ε     | ε     
T     |       |       |       |       | FR    | FR    |       |       
R     | ε     | ε     | *FR   | /FR   |       |       | ε     | ε     
F     |       |       |       |       | a     | (E)   |       |       

## **3\. Output Requirements**

For the same grammar and parsing table if the input string is (a+a)$, then Output must be displayed like this along the stack implementation (whole stack flow should be shown, though in the example only the end of the stack is shown) Example,

Input: (a+a)$  
Stack: \['$', 'Q', 'R'\]  
Output: String is accepted/ valid.

Input: (a+a)e$  
Stack: \['$', 'Q', 'R'\]  
Output: String is not accepted/ In valid.  

