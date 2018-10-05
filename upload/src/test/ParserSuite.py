import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_associative1(self):
        input = """
            procedure foo();
                begin
                    a := TRUE and then 2 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_associative2(self):
        input = """
            procedure foo();
                begin
                    a := 1+2*3 div 4+5*6+7 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_associative3(self):
        input = """
            procedure foo();
                begin
                    a := TRUE and then not 2 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_associative4(self):

        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := -2+3*4 < 1 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_associative5(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := 1<2 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_associative6(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and true or false ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_associative7(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and then 2 < ((1<1)<3) ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_associative8(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and then 2 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_errorassociative(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE <1 and then 2 ;
                end
                """
        expect = "successful"  
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_errorassociative1(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE[1][3][5] <=5 ;
                end
                """
        expect = "successful"
    
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_errorassociative2(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE + 1 and then 2 <= not -5[not true] ;
                end
                """
        expect = "successful"    
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_errorassociative3(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := (true < true) or 5 and 1 < 3 ;
                end
                """
        expect = "successful"    
        self.assertTrue(TestParser.test(input, expect, 213))
    def Test_Precedence(self):
        """ Test Precedence """
        input = """
            procedure foo();
            var 
            a: real;
            begin
            a := -5 - 6 + not 5 - 9 - not -(3 + not -5)+ a[b[foo()]];
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def Test_Array_Declare_Error(self):
        input = """
        var a, b, c: boolean;
        x, y, z: real ;
        g, h, i: array[0 .. 5] of integer ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    def array_decl(self):
        """ Test Array Declare """
        input = """
        var a: boolean;
        m,n: real ;
        p,q: array[0 .. foo("hello")] of integer ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_Array_Declare(self):
        """ Test Array Declare"""
        input = """
        var Tin, Dang, Trung: integer;
        m,n: real ;
        p,q: array[0 .. 5] of boolean ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_Array_Declare_e(self):
        """ Test Array Declare Error """
        input = """
        var a, b, c: boolean;
        m,n: real ;
        p,q: array[0 .. 218] of real ;
        VAR Tin, Dang, Trung: array[-219 .. 5] of boolean;
        m,n: array[-10 .. -5] of real ;
        p,q: array[10 .. 5] of integer ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_Array_Declare1(self):
        """ Variable Decl """
        input = """
        var a, b, c: boolean;m,n: real ;p,q: array[0 .. 5] of boolean ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_Array_Declare2(self):
        """ Test Array Declare """
        input = r"""
        var a, b, c: boolean;//hello
        m,n: real ;(*test*)
        p,q: array[0 .. 5] of boolean ;{declare}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_Array_Declare3(self):
        """ Test Array Declare """
        input = r"""
        var a, b, c: boolean;
        //comment in this line
        m,n: real ;
        p,q: array[0 .. 5] of boolean ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))    
    def test_Procedure1(self):
        input = """proCeduRe foo() ;
                   BEGIN
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_Procedure2(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_Procedure3(self):
        input = """proCeduRe foo(c: real) ;
                   BEGIN
                    a := 1;
                    c := a[0] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_Procedure4(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    if a then if a then begin end else begin end
                    c := a[12] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_Procedure5(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    with a,b:integer;c:array [1 .. 2] of real;do
                        d:=a+c;
                    c := a[12] ;
                   END
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_Procedure6(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    foo(foo(3),m(2),a[3]);
                    c := a[12] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_Procedure7(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    for a:=1 to 5 do
                        begin end
                    c := a[12] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_Procedure8(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                    begin return; end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_Procedure9(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                    begin break; end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_Procedure10(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                    BEGIN continue;enD"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_Procedure11(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   beGIN
                   whilE(a) do
                   continue; end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_function1(self):
        input = """function foo():integer ;
                   BEGIN
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_function2(self):
        input = """FUNCTION foo(c: real):real ;
                   var x,y: real ;
                   BEGIN END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_function3(self):
        input = """function foo(c: array[-235 .. 1] of real):real ;
                   BEGIN
                    a := 1;
                    c := a[0] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_function4(self):
        input = """function foo(c: real):real ;
                   var x,y: real ;
                   BEGIN
                    if a then if a then begin end else begin end
                    c := a[12] ;
                    return 1.0;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_function6(self):
        input = """function foo(c: string;c: string):boolean ;
                   var x,y: real ;
                   BEGIN
                    foo(foo(3),m(2),a[3]);
                    c := a[12] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_function7(self):
        input = r"""function foo(c: real;str:string; c: real):string ;
                   var x,y: real ;
                   BEGIN
                    for a:=1 to 5 do
                        begin end
                    c := a[12] ;
                    return "hello\n"{hello};
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_function8(self):
        input = """function foo(c: real;a:array [1 .. 1] of string):string ;
                    begin return; end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_function9(self):
        input = """funCtion foo(c: real):string ;
                   var x,y: real ;
                    begin break; end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_function10(self):
        input = """FUNCtion foo(c: real;bo:boolean):real ;
                   var x,y: real ;
                    BEGIN continue;enD"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_function11(self):
        input = """function foo(c: real):array[1 .. 2] of integer ;
                   var x,y: real ;begin
                   whilE(a) do
                   continue;
                    end 
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 244))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 245))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 246))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 247))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 248))

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 249))

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    
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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 251))
        

    def test_assginstmt(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := b[3] := foo(3)[5] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 252))
        

    def test_assginstmt1(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := b[3] := foo(3)[3] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 253))
        

    def test_assginstmt2(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := b[5] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 254))
        

    def test_assginstmt3(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := (b+5*6)[d] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 255))
        

    def test_assginstmt4(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d][t] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 256))
        

    def test_assginstmt5(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 257))
        

    def test_assginstmt6(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d=4] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 258))
        

    def test_assginstmt7(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d<4] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 259))
        

    def test_assginstmt8(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d>3] := 5;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 260))
        

    def test_assginstmt9(self):
        """ Test Assignment Stmt """
        input = r"""
procedure foo();
begin
    a := a[d < y(5 > 3) + 3 * n(12)] := 5[3] := 3[2] := b;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 261))
        

    def test_Break(self):
        """ Test Break Func call """
        input = r"""
procedure foo();
begin
    ok();
    break;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 263))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 264))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 265))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 266))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 267))
        

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
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 268))
        

    def test2(self):
        """ Test  """
        input = r"""
procedure f();
begin
    a := -------------5.e4;
end
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 269))
        

    def test_emptyprogram(self):
        """ Test Comment Line in Block """
        input = r"""
        var a:real;
{
    // Line Comment
    (* Block Comment *)
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_comment2(self):
        input = r"""
            procedure foo();
                begin
                (*hellocmm*)    a := TRUE and then -2 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test_comment3(self):
        input = """
            procedure foo();(*hellocmm*)
                begin(*hellocmm*)
                    a := 1+2*3 div 4+5*6+7 ;(*hellocmm*)
                end(*hellocmm*)
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_comment4(self):
        input = """
            procedure foo();
                begin
                    //a := TRUE and then not 2 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_comment5(self):

        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    {a := -2+3*4 < 1 ;}
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_comment7(self):
        input = r"""
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and {hello} true or false ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_comment8(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                  //  a := TRUE and then 2 < ((1<1)<3) ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_comment9(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    a := TRUE and then 2 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_comment10(self):
        input = """
            procedure foo();
                var 
                    a: real;
                begin
                    //a := TRUE <1<and then 2 ;
                end
                """
        expect = "successful"
    
        self.assertTrue(TestParser.test(input, expect, 279))
    def test_comment11(self):
        input = """function foo():real ;
                   var x,y: real ;
                   BEGIN
                    if a then if a then begin end else begin end
                    (*c := a[12] ;
                    return 1.0;*)
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_comment13(self):
        input = """function foo(c: string;a:array[2 .. -4] of string):boolean ;
                   var x,y:{this is my comment} real ;
                   BEGIN
                    foo(foo(3),m(2),a[3]);
                    c := a[12] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_comment14(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    for a:={this is my comment}1 to 5 do
                        begin end
                    c := a[12] ;
                    return "hello\n"{hello};
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_assignment1(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    c := a[12]:=a[foo()]=1 ;
                    return;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_assignment2(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    for a:=1 to 5 do
                        begin end
                    c := a[12]:=foo()[3]:=1 ;
                    return "hello\n"{hello};
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_assignment3(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    c := a[12]=foo(3) ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_assignment4(self):
        input = r"""function foo(c: real):string ;
                   var x,y: real ;
                   BEGIN
                    for a:=1 to 5 do
                        begin end
                    foo()[4] := a;
                    return "hello\n"{hello};
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_if(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then b := 2; else c := 3;
end
"""
        expect=r"successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_if0(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then {hello} return;
end
"""
        expect=r"successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_if2(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then begin end
end
"""
        expect=r"successful"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_if3(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then b := 2; else if 1 then return;
end
"""
        expect=r"successful"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_if1(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then if b=1 then return; else continue; else continue;
end
"""
        expect=r"successful"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_if5(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then b := 2; else c := 3;
        if a = 1 then b := 2; else c := 3;
end
"""
        expect=r"successful"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_if6(self):
        """ Test ... """
        input=r"""
procedure foo();
begin
    if a = 1 then b:=1; else return;
end
"""
        expect=r"successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_errorwhile(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   beGIN
                   whilE ((5 or a[3])[3]) do a:=1;
                   end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_errorwhile2(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   beGIN
                   whilE(1<1) do
                   continue; end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_errorfor(self):
        input = """proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    for ID:=1 to 5 do
                        begin end
                    c := a[12] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_errorwith1(self):
        input = r"""function foo(c: real):boolean ;
                   var x,y: real ;
                   BEGIN
                    with a,b:integer;c:array [1 .. 2] of real;do
                    c := a[12] ;
                   END
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))