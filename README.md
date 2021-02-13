# Convert regular grammar to Finite Automaton (FA)

The main purpose of LAB_1 is to check if a given string is compatible with the grammar that the program reads from the v21.txt file.

The program follows several logical steps listed below:

1.  **_Parse Grammar_** from v21.txt file. Grammar is an ordered quadruple G = (VN, VT, P, S) so, after running the _parseGrammar_ function in the main program we will have **vn vt** and **grammar** variables initialized, where **vn** is the alphabet of variables (or nonterminal symbols), **vt** is the alphabet of terminal symbols and **grammar** also written as **P** is a set of productions.
2.  **_Read the input string_** that the user wants to check if it is accepted by FA.
3.  **_Check if the input string can be generated by traversing the FA_**, if so write the path that we have to follow to generate the input string.

    The case when the input string is valid:

    ![Valid word console result](/assets/validWord.png)

    The case when the input string is not valid:

    ![Not valid word console result](/assets/notValidInputWord.png)

    The case when the input string contains invalid terminal symbols:

    ![Not valid terminal symbols console result](/assets/invalidTerminalSymbols.png)

4.  **_Draw the FA graph_**. (The graph is shown only for valid inputs)

    ![FA GRAPH](/assets/graph.svg)

# Determine the grammar type by the Chromsky classification.

By the Chomsky the grammar is classified in 4 types (type 0, type 1, type 2 and type 3). The grammar that is used for this program is of **type 3**(regular grammar) because its productions are of the form:

1. A -> aB;
2. A -> b,

Also it is **Right linear grammar** because it has at most one nonterminal in the right-hand side of each of its productions.
