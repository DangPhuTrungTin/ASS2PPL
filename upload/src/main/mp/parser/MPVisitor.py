# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#body.
    def visitBody(self, ctx:MPParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr.
    def visitExpr(self, ctx:MPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr1.
    def visitExpr1(self, ctx:MPParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr2.
    def visitExpr2(self, ctx:MPParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr3.
    def visitExpr3(self, ctx:MPParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr4.
    def visitExpr4(self, ctx:MPParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr5.
    def visitExpr5(self, ctx:MPParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#factor.
    def visitFactor(self, ctx:MPParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#factor1.
    def visitFactor1(self, ctx:MPParser.Factor1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexexpr.
    def visitIndexexpr(self, ctx:MPParser.IndexexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#invocationexpr.
    def visitInvocationexpr(self, ctx:MPParser.InvocationexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listexpr.
    def visitListexpr(self, ctx:MPParser.ListexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignmentstatement.
    def visitAssignmentstatement(self, ctx:MPParser.AssignmentstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignmentfactor.
    def visitAssignmentfactor(self, ctx:MPParser.AssignmentfactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifstatement.
    def visitIfstatement(self, ctx:MPParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilestatement.
    def visitWhilestatement(self, ctx:MPParser.WhilestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstatement.
    def visitForstatement(self, ctx:MPParser.ForstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakstatement.
    def visitBreakstatement(self, ctx:MPParser.BreakstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continuestatement.
    def visitContinuestatement(self, ctx:MPParser.ContinuestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnstatement.
    def visitReturnstatement(self, ctx:MPParser.ReturnstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundstatement.
    def visitCompoundstatement(self, ctx:MPParser.CompoundstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withstatement.
    def visitWithstatement(self, ctx:MPParser.WithstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callstatement.
    def visitCallstatement(self, ctx:MPParser.CallstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardecl.
    def visitVardecl(self, ctx:MPParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#mtype.
    def visitMtype(self, ctx:MPParser.MtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#range_.
    def visitRange_(self, ctx:MPParser.Range_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#limitingint.
    def visitLimitingint(self, ctx:MPParser.LimitingintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arraydec.
    def visitArraydec(self, ctx:MPParser.ArraydecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listofvardec.
    def visitListofvardec(self, ctx:MPParser.ListofvardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listid.
    def visitListid(self, ctx:MPParser.ListidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcdecl.
    def visitFuncdecl(self, ctx:MPParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#pardec.
    def visitPardec(self, ctx:MPParser.PardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procdecl.
    def visitProcdecl(self, ctx:MPParser.ProcdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#keyword.
    def visitKeyword(self, ctx:MPParser.KeywordContext):
        return self.visitChildren(ctx)



del MPParser