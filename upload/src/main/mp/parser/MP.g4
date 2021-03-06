//MSSV:1613557
grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
program  :  body+ EOF;
body:vardecl|funcdecl|procdecl;
//////////expresstion//////////
//expr:intexpr|boolexpr|realexpr|indexexpr|stringexpr|invocationexpr;
expr: expr (AND THEN|OR ELSE) expr1|expr1;
expr1:expr2 (EQ|NE|LT|LTE|GT|GTE) expr2|expr2;
expr2: expr2 (SUB|ADD|OR) expr3|expr3;
expr3: expr3 (DIV|MUL|INTEGERDIV|MOD|AND) expr4|expr4;
expr4:(NOT|SUB) expr4|expr5;
expr5: (LP expr RP) | factor;
factor:	invocationexpr
		|indexexpr
		|BOOLLIT
		|STRINGLIT
		|INTLIT
		|REALLIT
		|ID	
		;
factor1:LP expr RP
		|invocationexpr
		|BOOLLIT
		|STRINGLIT
		|INTLIT
		|REALLIT
		|ID	
		;
//indexexpr1: factor1 (LSP expr RSP);///sua intexpr|indexexpr ////
indexexpr: factor1 (LSP expr RSP)
		|indexexpr (LSP expr RSP)
		;
//invocation Expression
invocationexpr: ID LP listexpr RP;
listexpr:expr (CM expr)*|;
///////////////////////////////

//////////statements:///////////
//assignment
assignmentstatement: assignmentfactor (EQOP assignmentfactor)* EQOP expr SM;
assignmentfactor:ID|indexexpr ;
//if statement:
ifstatement: IF expr THEN statement (ELSE statement)? ;
//while Statement
whilestatement: WHILE expr DO statement ;
//for statement
forstatement: FOR ID EQOP expr (TO|DOWNTO) expr DO statement ;//cai 1 nen la intexpr cai 2 la intexpr|realexpr//
// break Statement:
breakstatement: BREAK SM;
// continue Statement:
continuestatement:CONTINUE SM;
// return Statement:
returnstatement:RETURN_ expr? SM;//procedure tra ve rong
// compound Statement:
compoundstatement: BEGIN statement* END ;
// with Statement:
withstatement: WITH listofvardec DO statement ;
// call Statement:
callstatement:ID LP listexpr RP SM;
///////////////////////////////////

/////////////statement in use//////////////////
statement:assignmentstatement|ifstatement|whilestatement|
		forstatement|compoundstatement|withstatement|callstatement
		|breakstatement|continuestatement|returnstatement;
////////////////////////////////////////////////

//////////////declaration/////////////
//Variable declaration
vardecl: VAR listofvardec;
mtype:arraydec|BOOLEAN|INTEGER|REAL|STRING;
range_:LSP limitingint DOUBLEDOT limitingint RSP;
limitingint:SUB? INTLIT;
//DOT:'.';
//error_rangesyntax:expr DOUBLEDOT DOT+ expr {raise SyntaxException(DOT.text)};
arraydec:ARRAY range_ OF (BOOLEAN|INTEGER|REAL|STRING);
listofvardec:(listid CL mtype SM)+;
listid: ID (CM ID)*;
//Function declaration:
funcdecl: FUNCTION ID (LP pardec RP) (CL mtype SM) vardecl? compoundstatement;

//compoundstatebody:BEGIN statement* END;
pardec: (listid CL mtype) (SM (listid CL mtype))*|;
//pardec1:; //dang nghi van cho array [1..22] of integer
//Procedure declaration
procdecl:PROCEDURE ID (LP pardec RP) SM vardecl? compoundstatement;
///////////////////////////////////////

////////type///////////
INTEGER: I N T E G E R ;
REAL:R E A L;
BOOLEAN: B O O L E A N;
STRING: S T R I N G;
ARRAY: A R R A Y;
///////////////////////

///////Convention////////
//Separators
LSP:'[';
RSP:']';
CL:':';
LP: '(' ;
RP: ')' ;
LB: '{';
RB: '}';
SM: ';' ;
CM:',';
//operators
DOUBLEDOT:'..';
NOT: N O T;
OR: O R;
NE: '<>';
LT:'<';
LTE:'<=';
INTEGERDIV: D I V;
MOD: M O D;
AND: A N D;
GT:'>';
GTE:'>=';
EQ:'=';
ADD:'+';
SUB:'-';
MUL:'*';
DIV:'/';
EQOP:':=';
/////////////////////////////

//////////literals/////////////
fragment Exponent: [eE]'-'?Digit+ ;
literal:INTLIT|BOOLLIT|REALLIT|STRINGLIT;
INTLIT: [0-9]+;
REALLIT: ('.'Digit+|Digit+'.'|Digit+'.'Digit+)Exponent?
		| Digit+Exponent;
BOOLLIT: (T R U E|F A L S E);
STRINGLIT: '"'Stringfactor*?'"'
{self.text=self.text[1:len(self.text)-1]};
fragment Stringfactor:(~[\b\f\r\n\t'"\\] | '\\' [bfrnt'"\\]);
///////////////////////////////

////////////comment////////////
//fragment CMSYMBOL:'(*'|'{'|'//';
// \r\n\t thi s
COMMENT1:'//'.*?([\n]|EOF)->skip ;
COMMENT2:'(*'.*?'*)' ->skip;
COMMENT3:'{'.*?'}'->skip;
// comment:COMMENT1
// 		| COMMENT2
// 		| COMMENT3
// 		 ->skip;
// ly do la ',\ duoc dung nhu 1 cu phap nen muon no thanh ki tu f dung \
///////////////////////////////

///////////logic syntax////////////
RETURN_:R E T U R N;
BREAK:B R E A K;
CONTINUE:C O N T I N U E;
FOR:F O R;
TO:T O;
DOWNTO:D O W N T O;
DO:D O;
IF:I F;
THEN:T H E N;
ELSE:E L S E;
WHILE:W H I L E;
BEGIN:B E G I N;
END:E N D;
FUNCTION:F U N C T I O N;
PROCEDURE:P R O C E D U R E;
VAR:V A R;
OF:O F;
WITH:W I T H;
///////////////////////////////////

//////////////list keyword/////////
keyword:BREAK|CONTINUE|FOR|TO|DOWNTO|DO|IF|THEN|ELSE|RETURN_
		|WHILE|BEGIN|END|FUNCTION|PROCEDURE|VAR|BOOLLIT|WITH
		|ARRAY|OF|REAL|BOOLEAN|INTEGER|STRING|NOT|AND|OR|DIV|MOD;
//////////////////////////////////

/////////identifiers/////////////
fragment Letter: [a-zA-Z_];
fragment Digit: [0-9];
ID: Letter(Letter|Digit)*;//dat ID o cuoi de tru KEYWORD ra
/////////////////////////////////

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
/////// replace (?i)///////////////////
fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];
UNCLOSE_STRING: '"'Stringfactor*
{
	raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"'Stringfactor*?('\\'~[btnfr'"\\])
{raise IllegalEscape(self.text[1:])};
//fragment LigalEscapesequence: '\\'('\''|'"'|'\\'|'b'|'f'|'r'|'n'|'t');
ERROR_CHAR: .{raise ErrorToken(self.text)};
////NOTE/////
//cac decl deu khong co SM cuoi
//comment co o 1 line,sau statement -> sau dau SM
//1: sua unclose,illegal,sua boolexpr tren while,if
//if rỗng được k