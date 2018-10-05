import unittest
from AST import *
from TestUtils import TestAST
class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """  
         procedure ptb2() ;
                VAR a,b,c,x1,x2,d:REAL;
                BEGIN
                 clrscr();
                 while(true) do begin
                  write("Nhap cac he so a, b, c: ");
                  readln(a,b,c);
                  if(a<>0) then break;
                 end
                 d:=c:=e:=foo(3)[3+x]:=sqr(b)-4*a*c;
	             e:="\\"tin\\nhello\\"";
                 IF d<0 THEN write("Phuong trinh vo nghiem!");
                 ELSE BEGIN
                  x1:=(-b-sqrt(d))/(2*a);
                  x2:=(-b+sqrt(d))/(2*a);
                  IF d=0 THEN writeln("Phuong trinh co nghiem kep x = ",x1);
                  ELSE writeln("Phuong trinh co 2 nghiem phan biet: ",x1,x2);
                  END
                  readln();
                END
        """
        expect = str(Program([FuncDecl(Id(r'ptb2'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x1'),FloatType()),VarDecl(Id(r'x2'),FloatType()),VarDecl(Id(r'd'),FloatType())],[CallStmt(Id(r'clrscr'),[]),While(BooleanLiteral(True),[CallStmt(Id(r'write'),[StringLiteral(r'Nhap cac he so a, b, c: ')]),CallStmt(Id(r'readln'),[Id(r'a'),Id(r'b'),Id(r'c')]),If(BinaryOp(r'<>',Id(r'a'),IntLiteral(0)),[Break()],[])]),Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(3)]),BinaryOp(r'+',IntLiteral(3),Id(r'x'))),BinaryOp(r'-',CallExpr(Id(r'sqr'),[Id(r'b')]),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(4),Id(r'a')),Id(r'c')))),Assign(Id(r'e'),ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(3)]),BinaryOp(r'+',IntLiteral(3),Id(r'x')))),Assign(Id(r'c'),Id(r'e')),Assign(Id(r'd'),Id(r'c')),Assign(Id(r'e'),StringLiteral(r'\"tin\nhello\"')),If(BinaryOp(r'<',Id(r'd'),IntLiteral(0)),[CallStmt(Id(r'write'),[StringLiteral(r'Phuong trinh vo nghiem!')])],[Assign(Id(r'x1'),BinaryOp(r'/',BinaryOp(r'-',UnaryOp(r'-',Id(r'b')),CallExpr(Id(r'sqrt'),[Id(r'd')])),BinaryOp(r'*',IntLiteral(2),Id(r'a')))),Assign(Id(r'x2'),BinaryOp(r'/',BinaryOp(r'+',UnaryOp(r'-',Id(r'b')),CallExpr(Id(r'sqrt'),[Id(r'd')])),BinaryOp(r'*',IntLiteral(2),Id(r'a')))),If(BinaryOp(r'=',Id(r'd'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Phuong trinh co nghiem kep x = '),Id(r'x1')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'Phuong trinh co 2 nghiem phan biet: '),Id(r'x1'),Id(r'x2')])])]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    def test_associative1(self):
        input = """
            procedure foo();
                begin
                    a := TRUE and then 2 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'andthen',BooleanLiteral(True),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,302))
    def test_associative2(self):
        input = """
            procedure foo();
                begin
                    a := 1+2*3 div 4+5*6+7 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',IntLiteral(1),BinaryOp(r'div',BinaryOp(r'*',IntLiteral(2),IntLiteral(3)),IntLiteral(4))),BinaryOp(r'*',IntLiteral(5),IntLiteral(6))),IntLiteral(7)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,303))
    def test_associative3(self):
        input = """
            procedure foo();
                begin
                    a := TRUE and then not 2 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'andthen',BooleanLiteral(True),UnaryOp(r'not',IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,304))
    def test_associative4(self):

        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := -2+3*4 < 1 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'<',BinaryOp(r'+',UnaryOp(r'-',IntLiteral(2)),BinaryOp(r'*',IntLiteral(3),IntLiteral(4))),IntLiteral(1)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,305))
    def test_associative5(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := 1<2 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'<',IntLiteral(1),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,306))
    def test_associative6(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and true or false ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'or',BinaryOp(r'and',BooleanLiteral(True),BooleanLiteral(True)),BooleanLiteral(False)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,307))
    def test_associative7(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and then 2 < ((1<1)<3) ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'andthen',BooleanLiteral(True),BinaryOp(r'<',IntLiteral(2),BinaryOp(r'<',BinaryOp(r'<',IntLiteral(1),IntLiteral(1)),IntLiteral(3)))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,308))
    def test_associative8(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and then 2 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'andthen',BooleanLiteral(True),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,309))
    def test_errorassociative(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE <1 and then 2 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'andthen',BinaryOp(r'<',BooleanLiteral(True),IntLiteral(1)),IntLiteral(2)))],VoidType())]))  
        self.assertTrue(TestAST.test(input,expect,310))
    def test_errorassociative1(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE[1][3][5] <=5 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'<=',ArrayCell(ArrayCell(ArrayCell(BooleanLiteral(True),IntLiteral(1)),IntLiteral(3)),IntLiteral(5)),IntLiteral(5)))],VoidType())]))
    
        self.assertTrue(TestAST.test(input,expect,311))
    def test_errorassociative2(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE + 1 and then 2 <= not -5[not true] ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'andthen',BinaryOp(r'+',BooleanLiteral(True),IntLiteral(1)),BinaryOp(r'<=',IntLiteral(2),UnaryOp(r'not',UnaryOp(r'-',ArrayCell(IntLiteral(5),UnaryOp(r'not',BooleanLiteral(True))))))))],VoidType())]))    
        self.assertTrue(TestAST.test(input,expect,312))
    def test_errorassociative3(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := (true < true) or 5 and 1 < 3 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'<',BinaryOp(r'or',BinaryOp(r'<',BooleanLiteral(True),BooleanLiteral(True)),BinaryOp(r'and',IntLiteral(5),IntLiteral(1))),IntLiteral(3)))],VoidType())]))    
        self.assertTrue(TestAST.test(input,expect,313))
    def test_Precedence(self):
        """ Test Precedence """
        input = """
            procedure foo();
            var 
            a: real;
            begin
            a := -5 - 6 + not 5 - 9 - not -(3 + not -5)+ a[b[foo()]];
            end
            """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'-',BinaryOp(r'+',BinaryOp(r'-',UnaryOp(r'-',IntLiteral(5)),IntLiteral(6)),UnaryOp(r'not',IntLiteral(5))),IntLiteral(9)),UnaryOp(r'not',UnaryOp(r'-',BinaryOp(r'+',IntLiteral(3),UnaryOp(r'not',UnaryOp(r'-',IntLiteral(5))))))),ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),CallExpr(Id(r'foo'),[])))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))
    def test_Array_Declare_Error(self):
        input = """
        var a, b, c: boolean;
        x, y, z: real ;
        g, h, i: array[0 .. 5] of integer ;
        """
        expect = str(Program([VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType()),VarDecl(Id(r'g'),ArrayType(0,5,IntType())),VarDecl(Id(r'h'),ArrayType(0,5,IntType())),VarDecl(Id(r'i'),ArrayType(0,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,315))
    def test_array_decl(self):
        """ Test Array Declare """
        input = """
        var a: boolean;
        m,n: real ;
        p,q: array[0 .. -1] of integer ;
        """
        expect = str(Program([VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'm'),FloatType()),VarDecl(Id(r'n'),FloatType()),VarDecl(Id(r'p'),ArrayType(0,-1,IntType())),VarDecl(Id(r'q'),ArrayType(0,-1,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,316))
    def test_Array_Declare(self):
        """ Test Array Declare"""
        input = """
        var Tin, Dang, Trung: integer;
        m,n: real ;
        p,q: array[0 .. 5] of boolean ;
        """
        expect = str(Program([VarDecl(Id(r'Tin'),IntType()),VarDecl(Id(r'Dang'),IntType()),VarDecl(Id(r'Trung'),IntType()),VarDecl(Id(r'm'),FloatType()),VarDecl(Id(r'n'),FloatType()),VarDecl(Id(r'p'),ArrayType(0,5,BoolType())),VarDecl(Id(r'q'),ArrayType(0,5,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,317))
    def test_Array_Declare_e(self):
        """ Test Array Declare Error """
        input = """
        var a, b, c: boolean;
        m,n: real ;
        p,q: array[0 .. 318] of real ;
        VAR Tin, Dang, Trung: array[-319 .. 5] of boolean;
        m,n: array[-10 .. -5] of real ;
        p,q: array[10 .. 5] of integer ;
        """
        expect = str(Program([VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'm'),FloatType()),VarDecl(Id(r'n'),FloatType()),VarDecl(Id(r'p'),ArrayType(0,318,FloatType())),VarDecl(Id(r'q'),ArrayType(0,318,FloatType())),VarDecl(Id(r'Tin'),ArrayType(-319,5,BoolType())),VarDecl(Id(r'Dang'),ArrayType(-319,5,BoolType())),VarDecl(Id(r'Trung'),ArrayType(-319,5,BoolType())),VarDecl(Id(r'm'),ArrayType(-10,-5,FloatType())),VarDecl(Id(r'n'),ArrayType(-10,-5,FloatType())),VarDecl(Id(r'p'),ArrayType(10,5,IntType())),VarDecl(Id(r'q'),ArrayType(10,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,318))
    def test_Array_Declare1(self):
        """ Variable Decl """
        input = """
        var a, b, c: boolean;m,n: real ;p,q: array[0 .. 5] of boolean ;
        """
        expect = str(Program([VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'm'),FloatType()),VarDecl(Id(r'n'),FloatType()),VarDecl(Id(r'p'),ArrayType(0,5,BoolType())),VarDecl(Id(r'q'),ArrayType(0,5,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,319))
    def test_Array_Declare2(self):
        """ Test Array Declare """
        input = r"""
        var a, b, c: boolean;//hello
        m,n: real ;(*test*)
        p,q: array[0 .. 5] of boolean ;{declare}
        """
        expect = str(Program([VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'm'),FloatType()),VarDecl(Id(r'n'),FloatType()),VarDecl(Id(r'p'),ArrayType(0,5,BoolType())),VarDecl(Id(r'q'),ArrayType(0,5,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,320))
    def test_Array_Declare3(self):
        """ Test Array Declare """
        input = r"""
        var a, b, c: boolean;
        //comment in this line
        m,n: real ;
        p,q: array[0 .. 5] of boolean ;
        """
        expect = str(Program([VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'm'),FloatType()),VarDecl(Id(r'n'),FloatType()),VarDecl(Id(r'p'),ArrayType(0,5,BoolType())),VarDecl(Id(r'q'),ArrayType(0,5,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,321))    
    def test_Procedure1(self):
        input = """proCeduRe foo() ;
                   BEGIN
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,322))
    def test_Procedure2(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))
    def test_Procedure3(self):
        input = """proCeduRe foo(c: real) ;
                   BEGIN
                    a := 1;
                    c := a[0] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(0)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,324))
    def test_Procedure4(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    if a then if a then begin end else begin end
                    c := a[12] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[If(Id(r'a'),[If(Id(r'a'),[],[])],[]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,325))
    def test_Procedure5(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    with a,b:integer;c:array [1 .. 2] of real;do
                        d:=a+c;
                    c := a[12] ;
                   END
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',Id(r'a'),Id(r'c')))]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,326))
    def test_Procedure6(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    foo(foo(3),m(2),a[3]);
                    c := a[12] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[CallStmt(Id(r'foo'),[CallExpr(Id(r'foo'),[IntLiteral(3)]),CallExpr(Id(r'm'),[IntLiteral(2)]),ArrayCell(Id(r'a'),IntLiteral(3))]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,327))
    def test_Procedure7(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    for a:=1 to 5 do
                        begin end
                    c := a[12] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[For(Id(r'a'),IntLiteral(1),IntLiteral(5),True,[]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,328))
    def test_Procedure8(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                    begin return; end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,329))
    def test_Procedure9(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                    begin break; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Break()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,330))
    def test_Procedure10(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                    BEGIN continue;enD"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Continue()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,331))
    def test_Procedure11(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   beGIN
                   whilE(a) do
                   continue; end
                    """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[While(Id(r'a'),[Continue()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,332))
    def test_function1(self):
        input = """function foo():integer ;
                   BEGIN
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,333))
    def test_function2(self):
        input = """FUNCTION foo(c: real):real ;
                   var x,y: real ;
                   BEGIN END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,334))
    def test_function3(self):
        input = """function foo(c: array[-33 .. 1] of real):real ;
                   BEGIN
                    a := 1;
                    c := a[0] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),ArrayType(-33,1,FloatType()))],[],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(0)))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,335))
    def test_function4(self):
        input = """function foo(c: real):real ;
                   var x,y: real ;
                   BEGIN
                    if a then if a then begin end else begin end
                    c := a[12] ;
                    return 1.0;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[If(Id(r'a'),[If(Id(r'a'),[],[])],[]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12))),Return(FloatLiteral(1.0))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,336))
    def test_function5(self):
        input = """function foo(c: real;c: real;c: real):boolean ;
                   var x,y: real ;
                   BEGIN
                    with a,b:integer;c:array [1 .. 2] of real;do
                        d:=a+c;
                    c := a[12] ;
                    return c[33];
                   END
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',Id(r'a'),Id(r'c')))]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12))),Return(ArrayCell(Id(r'c'),IntLiteral(33)))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,337))
    def test_function6(self):
        input = """function foo(c: string;c: string):boolean ;
                   var x,y: real ;
                   BEGIN
                    foo(foo(3),m(2),a[3]);
                    c := a[12] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'c'),StringType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[CallStmt(Id(r'foo'),[CallExpr(Id(r'foo'),[IntLiteral(3)]),CallExpr(Id(r'm'),[IntLiteral(2)]),ArrayCell(Id(r'a'),IntLiteral(3))]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,338))
    def test_function7(self):
        input = r"""function foo(c: real;str:string; c: real):string ;
                   var x,y: real ;
                   BEGIN
                    for a:=1 to 5 do
                        begin end
                    c := a[12] ;
                    return "hello\n"{hello};
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'str'),StringType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[For(Id(r'a'),IntLiteral(1),IntLiteral(5),True,[]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12))),Return(StringLiteral(r'hello\n'))],StringType())]))
        self.assertTrue(TestAST.test(input,expect,339))
    def test_function8(self):
        input = """function foo(c: real;a:array [1 .. 1] of string):string ;
                    begin return; end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'a'),ArrayType(1,1,StringType()))],[],[Return(None)],StringType())]))
        self.assertTrue(TestAST.test(input,expect,340))
    def test_function9(self):
        input = """funCtion foo(c: real):string ;
                   var x,y: real ;
                    begin break; end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Break()],StringType())]))
        self.assertTrue(TestAST.test(input,expect,341))
    def test_function10(self):
        input = """FUNCtion foo(c: real;bo:boolean):real ;
                   var x,y: real ;
                    BEGIN continue;enD"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'bo'),BoolType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Continue()],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,342))
    def test_function11(self):
        input = """function foo(c: real):array[1 .. 2] of integer ;
                   var x,y: real ;begin
                   whilE(a) do
                   continue;
                    end 
                    """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[While(Id(r'a'),[Continue()])],ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,343))
    def test_randomerror(self):
        """ Test Random Code """
        input = r"""
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
end end
function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        ======================================= *)
end
"""
        expect = str(Program([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x'),BoolType()),VarDecl(Id(r'y'),BoolType()),VarDecl(Id(r'z'),BoolType()),VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'nty'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType())],[CallStmt(Id(r'readLine'),[]),Assign(Id(r'fs'),CallExpr(Id(r'readStdin'),[])),With([VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(4),UnaryOp(r'-',IntLiteral(5)),False,[Assign(Id(r'h'),IntLiteral(6))]),If(BinaryOp(r'>',Id(r'i'),IntLiteral(6)),[Return(IntLiteral(0))],[])])],FloatType()),FuncDecl(Id(r'hgt'),[],[VarDecl(Id(r'a'),StringType())],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,344))
        

    def test_randomerror1(self):
        """ Test Random Code """
        input = r"""
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()
    begin
    fs := readStdin();
    
        for i := 4 downto -5[4][4] do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
end
"""
        expect = str(Program([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x'),BoolType()),VarDecl(Id(r'y'),BoolType()),VarDecl(Id(r'z'),BoolType()),VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'nty'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType())],[CallStmt(Id(r'readLine'),[]),Assign(Id(r'fs'),CallExpr(Id(r'readStdin'),[])),For(Id(r'i'),IntLiteral(4),UnaryOp(r'-',ArrayCell(ArrayCell(IntLiteral(5),IntLiteral(4)),IntLiteral(4))),False,[Assign(Id(r'h'),IntLiteral(6))]),If(BinaryOp(r'>',Id(r'i'),IntLiteral(6)),[Return(IntLiteral(0))],[]),Return(IntLiteral(1))],FloatType()),VarDecl(Id(r'q'),IntType()),VarDecl(Id(r'w'),IntType()),FuncDecl(Id(r'hgt'),[],[VarDecl(Id(r'a'),StringType())],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,345))
        

    def test_randomerror2(self):
        """ Test Random Code """
        input = r"""
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()
    INthis := readStdin();   
    with i: integer; do begin
        for ID := 4 downto -5 do hello := 6;
        if i > 6 then return;
    end

    return 1;
end

var q, w : integer;

function hgt(): Boolean;
begin
    (*
        =======================================
        Comment here
        =======================================
        begin
    *)
end
"""
        expect = str(Program([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x'),BoolType()),VarDecl(Id(r'y'),BoolType()),VarDecl(Id(r'z'),BoolType()),VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'nty'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType())],[CallStmt(Id(r'readLine'),[]),Assign(Id(r'INthis'),CallExpr(Id(r'readStdin'),[])),With([VarDecl(Id(r'i'),IntType())],[For(Id(r'ID'),IntLiteral(4),UnaryOp(r'-',IntLiteral(5)),False,[Assign(Id(r'hello'),IntLiteral(6))]),If(BinaryOp(r'>',Id(r'i'),IntLiteral(6)),[Return(None)],[])]),Return(IntLiteral(1))],FloatType()),VarDecl(Id(r'q'),IntType()),VarDecl(Id(r'w'),IntType()),FuncDecl(Id(r'hgt'),[],[],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,346))
        

    def test_randomerror3(self):
        """ Test Random Code """
        input = r"""
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();

    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end

var q, w : integer;

var a: string;

    (*
        =======================================
        Comment here
        =======================================
    *)

"""
        expect = str(Program([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x'),BoolType()),VarDecl(Id(r'y'),BoolType()),VarDecl(Id(r'z'),BoolType()),VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'nty'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType())],[CallStmt(Id(r'readLine'),[]),Assign(Id(r'fs'),CallExpr(Id(r'readStdin'),[])),With([VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(4),UnaryOp(r'-',IntLiteral(5)),False,[Assign(Id(r'h'),IntLiteral(6))]),If(BinaryOp(r'>',Id(r'i'),IntLiteral(6)),[Return(IntLiteral(0))],[])]),Return(IntLiteral(1))],FloatType()),VarDecl(Id(r'q'),IntType()),VarDecl(Id(r'w'),IntType()),VarDecl(Id(r'a'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,347))
        

    def test_randomerror4(self):
        """ Test Random Code """
        input = r"""
var a, b, c: real;

var x, y, z: Boolean;
    g, h, y: Integer;

function nty(): Real;
var x, y, z: Integer;
begin
    readLine();
    // This is readLine()

    fs := readStdin();
    
    with i: integer; do begin
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    end

    return 1;
end
var q, w : integer;

function hgt(): Boolean;
var a: string;
begin 
    (*
        =======================================
        Comment here
        =======================================
    *)
end
"""
        expect = str(Program([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x'),BoolType()),VarDecl(Id(r'y'),BoolType()),VarDecl(Id(r'z'),BoolType()),VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'nty'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType())],[CallStmt(Id(r'readLine'),[]),Assign(Id(r'fs'),CallExpr(Id(r'readStdin'),[])),With([VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(4),UnaryOp(r'-',IntLiteral(5)),False,[Assign(Id(r'h'),IntLiteral(6))]),If(BinaryOp(r'>',Id(r'i'),IntLiteral(6)),[Return(IntLiteral(0))],[])]),Return(IntLiteral(1))],FloatType()),VarDecl(Id(r'q'),IntType()),VarDecl(Id(r'w'),IntType()),FuncDecl(Id(r'hgt'),[],[VarDecl(Id(r'a'),StringType())],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_Complex(self):
        """ Test Complex Code """
        input = r"""
procedure foo();
begin
    a := "hello foo() \n.This is test"; // comment here
    { this is also comment
        if a = 1 then goto(4) 
        }
    for i:=1 to 10 do begin {
        if True then True()
    }
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),StringLiteral(r'hello foo() \n.This is test')),For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_Complex1(self):
        """ Test Function in Function """
        input = r"""
procedure foo();
begin

end
    function foo():real;
    begin
    end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[],VoidType()),FuncDecl(Id(r'foo'),[],[],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,350))

    
    def test_Complex2(self):
        """ Test Compound Stmt in Compound Stmt """
        input = r"""
procedure foo();
begin
begin
begin
hello();
end
end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'hello'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,351))
        

    def test_assginstmt(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := b[3] := foo(3)[5] := 5;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(3)]),IntLiteral(5)),IntLiteral(5)),Assign(ArrayCell(Id(r'b'),IntLiteral(3)),ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(3)]),IntLiteral(5))),Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,352))
        

    def test_assginstmt1(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := b[3] := foo(3)[3] := 5;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(3)]),IntLiteral(3)),IntLiteral(5)),Assign(ArrayCell(Id(r'b'),IntLiteral(3)),ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(3)]),IntLiteral(3))),Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,353))
        

    def test_assginstmt2(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := b[5] := 5;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'b'),IntLiteral(5)),IntLiteral(5)),Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(5)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,354))
        

    def test_assginstmt3(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := (b+5*6)[d] := 5;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(BinaryOp(r'+',Id(r'b'),BinaryOp(r'*',IntLiteral(5),IntLiteral(6))),Id(r'd')),IntLiteral(5)),Assign(Id(r'a'),ArrayCell(BinaryOp(r'+',Id(r'b'),BinaryOp(r'*',IntLiteral(5),IntLiteral(6))),Id(r'd')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,355))
        

    def test_assginstmt4(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d][t] := 5;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(ArrayCell(Id(r'a'),Id(r'd')),Id(r't')),IntLiteral(5)),Assign(Id(r'a'),ArrayCell(ArrayCell(Id(r'a'),Id(r'd')),Id(r't')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,356))
        

    def test_assginstmt5(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d] := 5;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),Id(r'd')),IntLiteral(5)),Assign(Id(r'a'),ArrayCell(Id(r'a'),Id(r'd')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,357))
        

    def test_assginstmt6(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d=4] := 5;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'=',Id(r'd'),IntLiteral(4))),IntLiteral(5)),Assign(Id(r'a'),ArrayCell(Id(r'a'),BinaryOp(r'=',Id(r'd'),IntLiteral(4))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,358))
        

    def test_assginstmt7(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d<4] := 5;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'<',Id(r'd'),IntLiteral(4))),IntLiteral(5)),Assign(Id(r'a'),ArrayCell(Id(r'a'),BinaryOp(r'<',Id(r'd'),IntLiteral(4))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,359))
        

    def test_assginstmt8(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d>3] := 5;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'>',Id(r'd'),IntLiteral(3))),IntLiteral(5)),Assign(Id(r'a'),ArrayCell(Id(r'a'),BinaryOp(r'>',Id(r'd'),IntLiteral(3))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))
        

    def test_assginstmt9(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d < y(5 > 3) + 3 * n(12)] := 5[3] := 3[2] := b;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(IntLiteral(3),IntLiteral(2)),Id(r'b')),Assign(ArrayCell(IntLiteral(5),IntLiteral(3)),ArrayCell(IntLiteral(3),IntLiteral(2))),Assign(ArrayCell(Id(r'a'),BinaryOp(r'<',Id(r'd'),BinaryOp(r'+',CallExpr(Id(r'y'),[BinaryOp(r'>',IntLiteral(5),IntLiteral(3))]),BinaryOp(r'*',IntLiteral(3),CallExpr(Id(r'n'),[IntLiteral(12)]))))),ArrayCell(IntLiteral(5),IntLiteral(3))),Assign(Id(r'a'),ArrayCell(Id(r'a'),BinaryOp(r'<',Id(r'd'),BinaryOp(r'+',CallExpr(Id(r'y'),[BinaryOp(r'>',IntLiteral(5),IntLiteral(3))]),BinaryOp(r'*',IntLiteral(3),CallExpr(Id(r'n'),[IntLiteral(12)]))))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,361))
        

    def test_Break(self):
        """ Test Break Func call """
        input = r"""
procedure foo();
begin
    ok();
    break;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[]),Break()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))
        

    def test_Statements(self):
        """ Test Statements """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        continue;
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[]),Break(),Continue(),Continue()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,363))
        

    def test_return(self):
        """ Test Return in Compound """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        return 15 * 6 - 3;
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[]),Break(),Continue(),Return(BinaryOp(r'-',BinaryOp(r'*',IntLiteral(15),IntLiteral(6)),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))
        

    def test_return1(self):
        """ Test Return multiple times """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        return;
        return 15 * 6 - 3;
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[]),Break(),Continue(),Return(None),Return(BinaryOp(r'-',BinaryOp(r'*',IntLiteral(15),IntLiteral(6)),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,365))
        

    def test_return2(self):
        """ Test Return in Return """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        return 15 * 6 - 3;
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[]),Break(),Continue(),Return(BinaryOp(r'-',BinaryOp(r'*',IntLiteral(15),IntLiteral(6)),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))
        

    def test1(self):
        """ Test  """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
        return ;
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[]),Break(),Continue(),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))
        

    def test_Return_Break(self):
        """ Test Return Break """
        input = r"""
procedure foo();
begin
    ok();
    break;
    continue;
    begin
         break;
    end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[]),Break(),Continue(),Break()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,368))
        

    def test_2(self):
        """ Test  """
        input = r"""
procedure f();
begin
    a := -------------5.e4;
end
"""
        expect = str(Program([FuncDecl(Id(r'f'),[],[],[Assign(Id(r'a'),UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',FloatLiteral(50000.0)))))))))))))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))
        

    def test_emptyprogram(self):
        """ Test Comment Line in Block """
        input = r"""
        var a:real;
{
    // Line Comment
    (* Block Comment *)
}
"""
        expect = str(Program([VarDecl(Id(r'a'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,370))
    def test_comment2(self):
        input = r"""
            procedure foo();
                begin
                (*hellocmm*)    a := TRUE and then -2 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'andthen',BooleanLiteral(True),UnaryOp(r'-',IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))
    def test_comment3(self):
        input = """
            procedure foo();(*hellocmm*)
                begin(*hellocmm*)
                    a := 1+2*3 div 4+5*6+7 ;(*hellocmm*)
                end(*hellocmm*)
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',IntLiteral(1),BinaryOp(r'div',BinaryOp(r'*',IntLiteral(2),IntLiteral(3)),IntLiteral(4))),BinaryOp(r'*',IntLiteral(5),IntLiteral(6))),IntLiteral(7)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))
    def test_comment4(self):
        input = """
            procedure foo();
                begin
                    //a := TRUE and then not 2 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))
    def test_comment5(self):

        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    {a := -2+3*4 < 1 ;}
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,374))
    def test_comment6(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    {a := -2+3*4 < 1 ;}
                    a := 1<2 ;
                    {a := -2+3*4 < 1 ;}
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'<',IntLiteral(1),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,375))
    def test_comment7(self):
        input = r"""
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and {hello} true or false ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'or',BinaryOp(r'and',BooleanLiteral(True),BooleanLiteral(True)),BooleanLiteral(False)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))
    def test_comment8(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                  //  a := TRUE and then 2 < ((1<1)<3) ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,377))
    def test_comment9(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and then 2 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'andthen',BooleanLiteral(True),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))
    def test_comment10(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    //a := TRUE <1<and then 2 ;
                end
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),FloatType())],[],VoidType())]))
    
        self.assertTrue(TestAST.test(input,expect,379))
    def test_comment11(self):
        input = """function foo():real ;
                   var x,y: real ;
                   BEGIN
                    if a then if a then begin end else begin end
                    (*c := a[12] ;
                    return 1.0;*)
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[If(Id(r'a'),[If(Id(r'a'),[],[])],[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,380))
    def test_comment12(self):
        input = r"""function foo(c: real):boolean ;
                   var x,y: real ;
                   BEGIN
                    with a,b:integer;c:array [1 ..{this is my comment} 2] of real;do
                        d:=a+c;
                    c := a[12] ;
                    return c[33];
                   END
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',Id(r'a'),Id(r'c')))]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12))),Return(ArrayCell(Id(r'c'),IntLiteral(33)))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,381))
    def test_comment13(self):
        input = """function foo(c: string;a:array[2 .. -4] of string):boolean ;
                   var x,y:{this is my comment} real ;
                   BEGIN
                    foo(foo(3),m(2),a[3]);
                    c := a[12] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'a'),ArrayType(2,-4,StringType()))],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[CallStmt(Id(r'foo'),[CallExpr(Id(r'foo'),[IntLiteral(3)]),CallExpr(Id(r'm'),[IntLiteral(2)]),ArrayCell(Id(r'a'),IntLiteral(3))]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,382))
    def test_comment14(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    for a:={this is my comment}1 to 5 do
                        begin end
                    c := a[12] ;
                    return "hello\n"{hello};
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[For(Id(r'a'),IntLiteral(1),IntLiteral(5),True,[]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12))),Return(StringLiteral(r'hello\n'))],StringType())]))
        self.assertTrue(TestAST.test(input,expect,383))
    def test_assignment1(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    c := a[12]:=a[foo()]=1 ;
                    return;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Assign(ArrayCell(Id(r'a'),IntLiteral(12)),BinaryOp(r'=',ArrayCell(Id(r'a'),CallExpr(Id(r'foo'),[])),IntLiteral(1))),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12))),Return(None)],StringType())]))
        self.assertTrue(TestAST.test(input,expect,384))
    def test_assignment2(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    for a:=1 to 5 do
                        begin end
                    c := a[12]:=foo()[3]:=1 ;
                    return "hello\n"{hello};
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[For(Id(r'a'),IntLiteral(1),IntLiteral(5),True,[]),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3)),IntLiteral(1)),Assign(ArrayCell(Id(r'a'),IntLiteral(12)),ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3))),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12))),Return(StringLiteral(r'hello\n'))],StringType())]))
        self.assertTrue(TestAST.test(input,expect,385))
    def test_assignment3(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    c := a[12]=foo(3) ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Assign(Id(r'c'),BinaryOp(r'=',ArrayCell(Id(r'a'),IntLiteral(12)),CallExpr(Id(r'foo'),[IntLiteral(3)])))],StringType())]))
        self.assertTrue(TestAST.test(input,expect,386))
    def test_assignment4(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    for a:=1 to 5 do
                        begin end
                    foo()[4] := a;
                    return "hello\n"{hello};
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[For(Id(r'a'),IntLiteral(1),IntLiteral(5),True,[]),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(4)),Id(r'a')),Return(StringLiteral(r'hello\n'))],StringType())]))
        self.assertTrue(TestAST.test(input,expect,387))
    def test_if(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then b := 2; else c := 3;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'b'),IntLiteral(2))],[Assign(Id(r'c'),IntLiteral(3))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,388))
    def test_if0(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then {hello} return;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Return(None)],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,389))
    def test_if2(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then begin end
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,390))
    def test_if3(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then b := 2; else if 1 then return;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'b'),IntLiteral(2))],[If(IntLiteral(1),[Return(None)],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,391))
    def test_if1(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then if b=1 then return; else continue; else continue;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[If(BinaryOp(r'=',Id(r'b'),IntLiteral(1)),[Return(None)],[Continue()])],[Continue()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,392))
    def test_if5(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then b := 2; else c := 3;
        if a = 1 then b := 2; else c := 3;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'b'),IntLiteral(2))],[Assign(Id(r'c'),IntLiteral(3))]),If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'b'),IntLiteral(2))],[Assign(Id(r'c'),IntLiteral(3))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,393))
    def test_if6(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then b:=1; else return;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'b'),IntLiteral(1))],[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,394))
    def test_errorwhile(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   beGIN
                   whilE ((5 or a[3])[3]) do a:=1;
                   end
                    """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[While(ArrayCell(BinaryOp(r'or',IntLiteral(5),ArrayCell(Id(r'a'),IntLiteral(3))),IntLiteral(3)),[Assign(Id(r'a'),IntLiteral(1))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,395))
    def test_errorwhile2(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   beGIN
                   whilE(1<1) do
                   continue; end
                    """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[While(BinaryOp(r'<',IntLiteral(1),IntLiteral(1)),[Continue()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,396))
    def test_errorfor(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    for ID:=1 to 5 do
                        begin end
                    c := a[12] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[For(Id(r'ID'),IntLiteral(1),IntLiteral(5),True,[]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,397))
    def test_errorfor2(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    for ID:=1 to 5 do
                        begin 
                        for a:=1 to 5 do begin end
                         end
                    c := a[12] ;
                   END"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[For(Id(r'ID'),IntLiteral(1),IntLiteral(5),True,[For(Id(r'a'),IntLiteral(1),IntLiteral(5),True,[])]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,398))
    def test_errorwith(self):
        input = r"""function foo(c: real):boolean ;
                   var x,y: real ;
                   BEGIN
                    with a,b:integer;c:array [1 .. 2] of real;do
                        d:=a+c;
                    c := a[12] ;
                    return c[33];
                   END
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp(r'+',Id(r'a'),Id(r'c')))]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12))),Return(ArrayCell(Id(r'c'),IntLiteral(33)))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,399))
    def test_errorwith1(self):
        input = r"""function foo(c: real):boolean ;
                   var x,y: real ;
                   BEGIN
                    with a,b:integer;c:array [1 .. 2] of real;do
                    c := a[12] ;
                   END
                """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,400))