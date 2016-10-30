# LL1_Parser
A simple LL1 parser using Python which accepts a grammar sequence and constructs the Parsing Table

LL1 Parsing
In computer science, an LL parser is a top-down parser for a subset of context-free languages. It parses the input from Left to right, performing Leftmost derivation of the sentence.

An LL parser is called an LL(k) parser if it uses k tokens of lookahead when parsing a sentence. If such a parser exists for a certain grammar and it can parse sentences of this grammar without backtracking then it is called an LL(k) grammar. LL(k) grammars can generate more languages the higher the number k of lookahead tokens.[1] A corollary of this is that not all context-free languages can be recognized by an LL(k) parser. An LL parser is called an LL(*) parser (an LL-regular parser[2]) if it is not restricted to a finite k tokens of lookahead, but can make parsing decisions by recognizing whether the following tokens belong to a regular language (for example by means of a Deterministic Finite Automaton).

LL grammars, particularly LL(1) grammars, are of great practical interest, as parsers for these grammars are easy to construct, and many computer languages are designed to be LL(1) for this reason. LL parsers are table-based parsers, similar to LR parsers. LL grammars can also be parsed by recursive descent parsers.

Constructing an LL(1) parsing table
In order to fill the parsing table, we have to establish what grammar rule the parser should choose if it sees a nonterminal A on the top of its stack and a symbol a on its input stream. It is easy to see that such a rule should be of the form A → w and that the language corresponding to w should have at least one string starting with a. For this purpose we define the First-set of w, written here as Fi(w), as the set of terminals that can be found at the start of some string in w, plus ε if the empty string also belongs to w. Given a grammar with the rules A1 → w1, ..., An → wn, we can compute the Fi(wi) and Fi(Ai) for every rule as follows:

initialize every Fi(Ai) with the empty set
set Fi(wi) to Fi(wi) for every rule Ai → wi, where Fi is defined as follows:
Fi(a w' ) = { a } for every terminal a
Fi(A w' ) = Fi(A) for every nonterminal A with ε not in Fi(A)
Fi(A w' ) = Fi(A) \ { ε } ∪ Fi(w' ) for every nonterminal A with ε in Fi(A)
Fi(ε) = { ε }
add Fi(wi) to Fi(Ai) for every rule Ai → wi
do steps 2 and 3 until all Fi sets stay the same.
Unfortunately, the First-sets are not sufficient to compute the parsing table. This is because a right-hand side w of a rule might ultimately be rewritten to the empty string. So the parser should also use the rule A → w if ε is in Fi(w) and it sees on the input stream a symbol that could follow A. Therefore, we also need the Follow-set of A, written as Fo(A) here, which is defined as the set of terminals a such that there is a string of symbols αAaβ that can be derived from the start symbol. We use $ as a special terminal indicating end of input stream and S as start symbol.

Computing the Follow-sets for the nonterminals in a grammar can be done as follows:

initialize Fo(S) with { $ } and every other Fo(Ai) with the empty set
if there is a rule of the form Aj → wAiw' , then
if the terminal a is in Fi(w' ), then add a to Fo(Ai)
if ε is in Fi(w' ), then add Fo(Aj) to Fo(Ai)
if w' has length 0, then add Fo(Aj) to Fo(Ai)
repeat step 2 until all Fo sets stay the same.
Now we can define exactly which rules will be contained where in the parsing table. If T[A, a] denotes the entry in the table for nonterminal A and terminal a, then

T[A,a] contains the rule A → w if and only if
a is in Fi(w) or
ε is in Fi(w) and a is in Fo(A).
If the table contains at most one rule in every one of its cells, then the parser will always know which rule it has to use and can therefore parse strings without backtracking. It is in precisely this case that the grammar is called an LL(1) grammar.


Steps to run the code:
1. Download or clone the repo
2. Python3 needs to be installed on the system.
3. Run main.py and enter details for the LL1 parser.
