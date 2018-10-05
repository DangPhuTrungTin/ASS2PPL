# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u0256\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\5!\u0120\n!\3!\6!\u0123\n!\r!\16!\u0124\3")
        buf.write("\"\6\"\u0128\n\"\r\"\16\"\u0129\3#\3#\6#\u012e\n#\r#\16")
        buf.write("#\u012f\3#\6#\u0133\n#\r#\16#\u0134\3#\3#\3#\6#\u013a")
        buf.write("\n#\r#\16#\u013b\3#\3#\6#\u0140\n#\r#\16#\u0141\5#\u0144")
        buf.write("\n#\3#\5#\u0147\n#\3#\6#\u014a\n#\r#\16#\u014b\3#\3#\5")
        buf.write("#\u0150\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u015d\n")
        buf.write("$\3%\3%\7%\u0161\n%\f%\16%\u0164\13%\3%\3%\3%\3&\3&\3")
        buf.write("&\5&\u016c\n&\3\'\3\'\3\'\3\'\7\'\u0172\n\'\f\'\16\'\u0175")
        buf.write("\13\'\3\'\5\'\u0178\n\'\3\'\3\'\3(\3(\3(\3(\7(\u0180\n")
        buf.write("(\f(\16(\u0183\13(\3(\3(\3(\3(\3(\3)\3)\7)\u018c\n)\f")
        buf.write(")\16)\u018f\13)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\38\38\38\38\38\38\38\38\38\38\39\39\3")
        buf.write("9\39\3:\3:\3:\3;\3;\3;\3;\3;\3<\3<\3=\3=\3>\3>\3>\7>\u01ff")
        buf.write("\n>\f>\16>\u0202\13>\3?\6?\u0205\n?\r?\16?\u0206\3?\3")
        buf.write("?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3")
        buf.write("H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3")
        buf.write("Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3Z\3")
        buf.write("Z\7Z\u0241\nZ\fZ\16Z\u0244\13Z\3Z\3Z\3[\3[\7[\u024a\n")
        buf.write("[\f[\16[\u024d\13[\3[\3[\3[\3[\3[\3\\\3\\\3\\\7\u0162")
        buf.write("\u0173\u0181\u018d\u024b\2]\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\2C\"E#G$I%K\2M&O\'Q(S)U*W+Y,[-]._/a\60c\61e")
        buf.write("\62g\63i\64k\65m\66o\67q8s9u:w\2y\2{;}<\177\2\u0081\2")
        buf.write("\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f")
        buf.write("\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d")
        buf.write("\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab")
        buf.write("\2\u00ad\2\u00af\2\u00b1\2\u00b3=\u00b5>\u00b7?\3\2\"")
        buf.write("\4\2GGgg\3\2\62;\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppt")
        buf.write("tvv\3\3\f\f\5\2C\\aac|\5\2\13\f\17\17\"\"\4\2CCcc\4\2")
        buf.write("DDdd\4\2EEee\4\2FFff\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4")
        buf.write("\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRr")
        buf.write("r\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2")
        buf.write("YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u024e\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2C\3\2\2\2\2E\3")
        buf.write("\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2{\3\2")
        buf.write("\2\2\2}\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7")
        buf.write("\3\2\2\2\3\u00b9\3\2\2\2\5\u00c1\3\2\2\2\7\u00c6\3\2\2")
        buf.write("\2\t\u00ce\3\2\2\2\13\u00d5\3\2\2\2\r\u00db\3\2\2\2\17")
        buf.write("\u00dd\3\2\2\2\21\u00df\3\2\2\2\23\u00e1\3\2\2\2\25\u00e3")
        buf.write("\3\2\2\2\27\u00e5\3\2\2\2\31\u00e7\3\2\2\2\33\u00e9\3")
        buf.write("\2\2\2\35\u00eb\3\2\2\2\37\u00ed\3\2\2\2!\u00f0\3\2\2")
        buf.write("\2#\u00f4\3\2\2\2%\u00f7\3\2\2\2\'\u00fa\3\2\2\2)\u00fc")
        buf.write("\3\2\2\2+\u00ff\3\2\2\2-\u0103\3\2\2\2/\u0107\3\2\2\2")
        buf.write("\61\u010b\3\2\2\2\63\u010d\3\2\2\2\65\u0110\3\2\2\2\67")
        buf.write("\u0112\3\2\2\29\u0114\3\2\2\2;\u0116\3\2\2\2=\u0118\3")
        buf.write("\2\2\2?\u011a\3\2\2\2A\u011d\3\2\2\2C\u0127\3\2\2\2E\u014f")
        buf.write("\3\2\2\2G\u015c\3\2\2\2I\u015e\3\2\2\2K\u016b\3\2\2\2")
        buf.write("M\u016d\3\2\2\2O\u017b\3\2\2\2Q\u0189\3\2\2\2S\u0194\3")
        buf.write("\2\2\2U\u019b\3\2\2\2W\u01a1\3\2\2\2Y\u01aa\3\2\2\2[\u01ae")
        buf.write("\3\2\2\2]\u01b1\3\2\2\2_\u01b8\3\2\2\2a\u01bb\3\2\2\2")
        buf.write("c\u01be\3\2\2\2e\u01c3\3\2\2\2g\u01c8\3\2\2\2i\u01ce\3")
        buf.write("\2\2\2k\u01d4\3\2\2\2m\u01d8\3\2\2\2o\u01e1\3\2\2\2q\u01eb")
        buf.write("\3\2\2\2s\u01ef\3\2\2\2u\u01f2\3\2\2\2w\u01f7\3\2\2\2")
        buf.write("y\u01f9\3\2\2\2{\u01fb\3\2\2\2}\u0204\3\2\2\2\177\u020a")
        buf.write("\3\2\2\2\u0081\u020c\3\2\2\2\u0083\u020e\3\2\2\2\u0085")
        buf.write("\u0210\3\2\2\2\u0087\u0212\3\2\2\2\u0089\u0214\3\2\2\2")
        buf.write("\u008b\u0216\3\2\2\2\u008d\u0218\3\2\2\2\u008f\u021a\3")
        buf.write("\2\2\2\u0091\u021c\3\2\2\2\u0093\u021e\3\2\2\2\u0095\u0220")
        buf.write("\3\2\2\2\u0097\u0222\3\2\2\2\u0099\u0224\3\2\2\2\u009b")
        buf.write("\u0226\3\2\2\2\u009d\u0228\3\2\2\2\u009f\u022a\3\2\2\2")
        buf.write("\u00a1\u022c\3\2\2\2\u00a3\u022e\3\2\2\2\u00a5\u0230\3")
        buf.write("\2\2\2\u00a7\u0232\3\2\2\2\u00a9\u0234\3\2\2\2\u00ab\u0236")
        buf.write("\3\2\2\2\u00ad\u0238\3\2\2\2\u00af\u023a\3\2\2\2\u00b1")
        buf.write("\u023c\3\2\2\2\u00b3\u023e\3\2\2\2\u00b5\u0247\3\2\2\2")
        buf.write("\u00b7\u0253\3\2\2\2\u00b9\u00ba\5\u008fH\2\u00ba\u00bb")
        buf.write("\5\u0099M\2\u00bb\u00bc\5\u00a5S\2\u00bc\u00bd\5\u0087")
        buf.write("D\2\u00bd\u00be\5\u008bF\2\u00be\u00bf\5\u0087D\2\u00bf")
        buf.write("\u00c0\5\u00a1Q\2\u00c0\4\3\2\2\2\u00c1\u00c2\5\u00a1")
        buf.write("Q\2\u00c2\u00c3\5\u0087D\2\u00c3\u00c4\5\177@\2\u00c4")
        buf.write("\u00c5\5\u0095K\2\u00c5\6\3\2\2\2\u00c6\u00c7\5\u0081")
        buf.write("A\2\u00c7\u00c8\5\u009bN\2\u00c8\u00c9\5\u009bN\2\u00c9")
        buf.write("\u00ca\5\u0095K\2\u00ca\u00cb\5\u0087D\2\u00cb\u00cc\5")
        buf.write("\177@\2\u00cc\u00cd\5\u0099M\2\u00cd\b\3\2\2\2\u00ce\u00cf")
        buf.write("\5\u00a3R\2\u00cf\u00d0\5\u00a5S\2\u00d0\u00d1\5\u00a1")
        buf.write("Q\2\u00d1\u00d2\5\u008fH\2\u00d2\u00d3\5\u0099M\2\u00d3")
        buf.write("\u00d4\5\u008bF\2\u00d4\n\3\2\2\2\u00d5\u00d6\5\177@\2")
        buf.write("\u00d6\u00d7\5\u00a1Q\2\u00d7\u00d8\5\u00a1Q\2\u00d8\u00d9")
        buf.write("\5\177@\2\u00d9\u00da\5\u00afX\2\u00da\f\3\2\2\2\u00db")
        buf.write("\u00dc\7]\2\2\u00dc\16\3\2\2\2\u00dd\u00de\7_\2\2\u00de")
        buf.write("\20\3\2\2\2\u00df\u00e0\7<\2\2\u00e0\22\3\2\2\2\u00e1")
        buf.write("\u00e2\7*\2\2\u00e2\24\3\2\2\2\u00e3\u00e4\7+\2\2\u00e4")
        buf.write("\26\3\2\2\2\u00e5\u00e6\7}\2\2\u00e6\30\3\2\2\2\u00e7")
        buf.write("\u00e8\7\177\2\2\u00e8\32\3\2\2\2\u00e9\u00ea\7=\2\2\u00ea")
        buf.write("\34\3\2\2\2\u00eb\u00ec\7.\2\2\u00ec\36\3\2\2\2\u00ed")
        buf.write("\u00ee\7\60\2\2\u00ee\u00ef\7\60\2\2\u00ef \3\2\2\2\u00f0")
        buf.write("\u00f1\5\u0099M\2\u00f1\u00f2\5\u009bN\2\u00f2\u00f3\5")
        buf.write("\u00a5S\2\u00f3\"\3\2\2\2\u00f4\u00f5\5\u009bN\2\u00f5")
        buf.write("\u00f6\5\u00a1Q\2\u00f6$\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8")
        buf.write("\u00f9\7@\2\2\u00f9&\3\2\2\2\u00fa\u00fb\7>\2\2\u00fb")
        buf.write("(\3\2\2\2\u00fc\u00fd\7>\2\2\u00fd\u00fe\7?\2\2\u00fe")
        buf.write("*\3\2\2\2\u00ff\u0100\5\u0085C\2\u0100\u0101\5\u008fH")
        buf.write("\2\u0101\u0102\5\u00a9U\2\u0102,\3\2\2\2\u0103\u0104\5")
        buf.write("\u0097L\2\u0104\u0105\5\u009bN\2\u0105\u0106\5\u0085C")
        buf.write("\2\u0106.\3\2\2\2\u0107\u0108\5\177@\2\u0108\u0109\5\u0099")
        buf.write("M\2\u0109\u010a\5\u0085C\2\u010a\60\3\2\2\2\u010b\u010c")
        buf.write("\7@\2\2\u010c\62\3\2\2\2\u010d\u010e\7@\2\2\u010e\u010f")
        buf.write("\7?\2\2\u010f\64\3\2\2\2\u0110\u0111\7?\2\2\u0111\66\3")
        buf.write("\2\2\2\u0112\u0113\7-\2\2\u01138\3\2\2\2\u0114\u0115\7")
        buf.write("/\2\2\u0115:\3\2\2\2\u0116\u0117\7,\2\2\u0117<\3\2\2\2")
        buf.write("\u0118\u0119\7\61\2\2\u0119>\3\2\2\2\u011a\u011b\7<\2")
        buf.write("\2\u011b\u011c\7?\2\2\u011c@\3\2\2\2\u011d\u011f\t\2\2")
        buf.write("\2\u011e\u0120\7/\2\2\u011f\u011e\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u0123\5y=\2\u0122\u0121")
        buf.write("\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0122\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125B\3\2\2\2\u0126\u0128\t\3\2\2\u0127")
        buf.write("\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012aD\3\2\2\2\u012b\u012d\7\60\2")
        buf.write("\2\u012c\u012e\5y=\2\u012d\u012c\3\2\2\2\u012e\u012f\3")
        buf.write("\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0144")
        buf.write("\3\2\2\2\u0131\u0133\5y=\2\u0132\u0131\3\2\2\2\u0133\u0134")
        buf.write("\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u0137\7\60\2\2\u0137\u0144\3\2\2")
        buf.write("\2\u0138\u013a\5y=\2\u0139\u0138\3\2\2\2\u013a\u013b\3")
        buf.write("\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013d\u013f\7\60\2\2\u013e\u0140\5y=\2\u013f")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143\u012b\3")
        buf.write("\2\2\2\u0143\u0132\3\2\2\2\u0143\u0139\3\2\2\2\u0144\u0146")
        buf.write("\3\2\2\2\u0145\u0147\5A!\2\u0146\u0145\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147\u0150\3\2\2\2\u0148\u014a\5y=\2\u0149\u0148")
        buf.write("\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\5A!\2\u014e")
        buf.write("\u0150\3\2\2\2\u014f\u0143\3\2\2\2\u014f\u0149\3\2\2\2")
        buf.write("\u0150F\3\2\2\2\u0151\u0152\5\u00a5S\2\u0152\u0153\5\u00a1")
        buf.write("Q\2\u0153\u0154\5\u00a7T\2\u0154\u0155\5\u0087D\2\u0155")
        buf.write("\u015d\3\2\2\2\u0156\u0157\5\u0089E\2\u0157\u0158\5\177")
        buf.write("@\2\u0158\u0159\5\u0095K\2\u0159\u015a\5\u00a3R\2\u015a")
        buf.write("\u015b\5\u0087D\2\u015b\u015d\3\2\2\2\u015c\u0151\3\2")
        buf.write("\2\2\u015c\u0156\3\2\2\2\u015dH\3\2\2\2\u015e\u0162\7")
        buf.write("$\2\2\u015f\u0161\5K&\2\u0160\u015f\3\2\2\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0162\u0160\3\2\2\2\u0163")
        buf.write("\u0165\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166\7$\2\2")
        buf.write("\u0166\u0167\b%\2\2\u0167J\3\2\2\2\u0168\u016c\n\4\2\2")
        buf.write("\u0169\u016a\7^\2\2\u016a\u016c\t\5\2\2\u016b\u0168\3")
        buf.write("\2\2\2\u016b\u0169\3\2\2\2\u016cL\3\2\2\2\u016d\u016e")
        buf.write("\7\61\2\2\u016e\u016f\7\61\2\2\u016f\u0173\3\2\2\2\u0170")
        buf.write("\u0172\13\2\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2")
        buf.write("\2\u0173\u0174\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0177")
        buf.write("\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0178\t\6\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\b\'\3\2")
        buf.write("\u017aN\3\2\2\2\u017b\u017c\7*\2\2\u017c\u017d\7,\2\2")
        buf.write("\u017d\u0181\3\2\2\2\u017e\u0180\13\2\2\2\u017f\u017e")
        buf.write("\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u0182\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0184\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0184\u0185\7,\2\2\u0185\u0186\7+\2\2\u0186\u0187\3\2")
        buf.write("\2\2\u0187\u0188\b(\3\2\u0188P\3\2\2\2\u0189\u018d\7}")
        buf.write("\2\2\u018a\u018c\13\2\2\2\u018b\u018a\3\2\2\2\u018c\u018f")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018e")
        buf.write("\u0190\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\7\177\2")
        buf.write("\2\u0191\u0192\3\2\2\2\u0192\u0193\b)\3\2\u0193R\3\2\2")
        buf.write("\2\u0194\u0195\5\u00a1Q\2\u0195\u0196\5\u0087D\2\u0196")
        buf.write("\u0197\5\u00a5S\2\u0197\u0198\5\u00a7T\2\u0198\u0199\5")
        buf.write("\u00a1Q\2\u0199\u019a\5\u0099M\2\u019aT\3\2\2\2\u019b")
        buf.write("\u019c\5\u0081A\2\u019c\u019d\5\u00a1Q\2\u019d\u019e\5")
        buf.write("\u0087D\2\u019e\u019f\5\177@\2\u019f\u01a0\5\u0093J\2")
        buf.write("\u01a0V\3\2\2\2\u01a1\u01a2\5\u0083B\2\u01a2\u01a3\5\u009b")
        buf.write("N\2\u01a3\u01a4\5\u0099M\2\u01a4\u01a5\5\u00a5S\2\u01a5")
        buf.write("\u01a6\5\u008fH\2\u01a6\u01a7\5\u0099M\2\u01a7\u01a8\5")
        buf.write("\u00a7T\2\u01a8\u01a9\5\u0087D\2\u01a9X\3\2\2\2\u01aa")
        buf.write("\u01ab\5\u0089E\2\u01ab\u01ac\5\u009bN\2\u01ac\u01ad\5")
        buf.write("\u00a1Q\2\u01adZ\3\2\2\2\u01ae\u01af\5\u00a5S\2\u01af")
        buf.write("\u01b0\5\u009bN\2\u01b0\\\3\2\2\2\u01b1\u01b2\5\u0085")
        buf.write("C\2\u01b2\u01b3\5\u009bN\2\u01b3\u01b4\5\u00abV\2\u01b4")
        buf.write("\u01b5\5\u0099M\2\u01b5\u01b6\5\u00a5S\2\u01b6\u01b7\5")
        buf.write("\u009bN\2\u01b7^\3\2\2\2\u01b8\u01b9\5\u0085C\2\u01b9")
        buf.write("\u01ba\5\u009bN\2\u01ba`\3\2\2\2\u01bb\u01bc\5\u008fH")
        buf.write("\2\u01bc\u01bd\5\u0089E\2\u01bdb\3\2\2\2\u01be\u01bf\5")
        buf.write("\u00a5S\2\u01bf\u01c0\5\u008dG\2\u01c0\u01c1\5\u0087D")
        buf.write("\2\u01c1\u01c2\5\u0099M\2\u01c2d\3\2\2\2\u01c3\u01c4\5")
        buf.write("\u0087D\2\u01c4\u01c5\5\u0095K\2\u01c5\u01c6\5\u00a3R")
        buf.write("\2\u01c6\u01c7\5\u0087D\2\u01c7f\3\2\2\2\u01c8\u01c9\5")
        buf.write("\u00abV\2\u01c9\u01ca\5\u008dG\2\u01ca\u01cb\5\u008fH")
        buf.write("\2\u01cb\u01cc\5\u0095K\2\u01cc\u01cd\5\u0087D\2\u01cd")
        buf.write("h\3\2\2\2\u01ce\u01cf\5\u0081A\2\u01cf\u01d0\5\u0087D")
        buf.write("\2\u01d0\u01d1\5\u008bF\2\u01d1\u01d2\5\u008fH\2\u01d2")
        buf.write("\u01d3\5\u0099M\2\u01d3j\3\2\2\2\u01d4\u01d5\5\u0087D")
        buf.write("\2\u01d5\u01d6\5\u0099M\2\u01d6\u01d7\5\u0085C\2\u01d7")
        buf.write("l\3\2\2\2\u01d8\u01d9\5\u0089E\2\u01d9\u01da\5\u00a7T")
        buf.write("\2\u01da\u01db\5\u0099M\2\u01db\u01dc\5\u0083B\2\u01dc")
        buf.write("\u01dd\5\u00a5S\2\u01dd\u01de\5\u008fH\2\u01de\u01df\5")
        buf.write("\u009bN\2\u01df\u01e0\5\u0099M\2\u01e0n\3\2\2\2\u01e1")
        buf.write("\u01e2\5\u009dO\2\u01e2\u01e3\5\u00a1Q\2\u01e3\u01e4\5")
        buf.write("\u009bN\2\u01e4\u01e5\5\u0083B\2\u01e5\u01e6\5\u0087D")
        buf.write("\2\u01e6\u01e7\5\u0085C\2\u01e7\u01e8\5\u00a7T\2\u01e8")
        buf.write("\u01e9\5\u00a1Q\2\u01e9\u01ea\5\u0087D\2\u01eap\3\2\2")
        buf.write("\2\u01eb\u01ec\5\u00a9U\2\u01ec\u01ed\5\177@\2\u01ed\u01ee")
        buf.write("\5\u00a1Q\2\u01eer\3\2\2\2\u01ef\u01f0\5\u009bN\2\u01f0")
        buf.write("\u01f1\5\u0089E\2\u01f1t\3\2\2\2\u01f2\u01f3\5\u00abV")
        buf.write("\2\u01f3\u01f4\5\u008fH\2\u01f4\u01f5\5\u00a5S\2\u01f5")
        buf.write("\u01f6\5\u008dG\2\u01f6v\3\2\2\2\u01f7\u01f8\t\7\2\2\u01f8")
        buf.write("x\3\2\2\2\u01f9\u01fa\t\3\2\2\u01faz\3\2\2\2\u01fb\u0200")
        buf.write("\5w<\2\u01fc\u01ff\5w<\2\u01fd\u01ff\5y=\2\u01fe\u01fc")
        buf.write("\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0202\3\2\2\2\u0200")
        buf.write("\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201|\3\2\2\2\u0202")
        buf.write("\u0200\3\2\2\2\u0203\u0205\t\b\2\2\u0204\u0203\3\2\2\2")
        buf.write("\u0205\u0206\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3")
        buf.write("\2\2\2\u0207\u0208\3\2\2\2\u0208\u0209\b?\3\2\u0209~\3")
        buf.write("\2\2\2\u020a\u020b\t\t\2\2\u020b\u0080\3\2\2\2\u020c\u020d")
        buf.write("\t\n\2\2\u020d\u0082\3\2\2\2\u020e\u020f\t\13\2\2\u020f")
        buf.write("\u0084\3\2\2\2\u0210\u0211\t\f\2\2\u0211\u0086\3\2\2\2")
        buf.write("\u0212\u0213\t\2\2\2\u0213\u0088\3\2\2\2\u0214\u0215\t")
        buf.write("\r\2\2\u0215\u008a\3\2\2\2\u0216\u0217\t\16\2\2\u0217")
        buf.write("\u008c\3\2\2\2\u0218\u0219\t\17\2\2\u0219\u008e\3\2\2")
        buf.write("\2\u021a\u021b\t\20\2\2\u021b\u0090\3\2\2\2\u021c\u021d")
        buf.write("\t\21\2\2\u021d\u0092\3\2\2\2\u021e\u021f\t\22\2\2\u021f")
        buf.write("\u0094\3\2\2\2\u0220\u0221\t\23\2\2\u0221\u0096\3\2\2")
        buf.write("\2\u0222\u0223\t\24\2\2\u0223\u0098\3\2\2\2\u0224\u0225")
        buf.write("\t\25\2\2\u0225\u009a\3\2\2\2\u0226\u0227\t\26\2\2\u0227")
        buf.write("\u009c\3\2\2\2\u0228\u0229\t\27\2\2\u0229\u009e\3\2\2")
        buf.write("\2\u022a\u022b\t\30\2\2\u022b\u00a0\3\2\2\2\u022c\u022d")
        buf.write("\t\31\2\2\u022d\u00a2\3\2\2\2\u022e\u022f\t\32\2\2\u022f")
        buf.write("\u00a4\3\2\2\2\u0230\u0231\t\33\2\2\u0231\u00a6\3\2\2")
        buf.write("\2\u0232\u0233\t\34\2\2\u0233\u00a8\3\2\2\2\u0234\u0235")
        buf.write("\t\35\2\2\u0235\u00aa\3\2\2\2\u0236\u0237\t\36\2\2\u0237")
        buf.write("\u00ac\3\2\2\2\u0238\u0239\t\37\2\2\u0239\u00ae\3\2\2")
        buf.write("\2\u023a\u023b\t \2\2\u023b\u00b0\3\2\2\2\u023c\u023d")
        buf.write("\t!\2\2\u023d\u00b2\3\2\2\2\u023e\u0242\7$\2\2\u023f\u0241")
        buf.write("\5K&\2\u0240\u023f\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0240")
        buf.write("\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0245\3\2\2\2\u0244")
        buf.write("\u0242\3\2\2\2\u0245\u0246\bZ\4\2\u0246\u00b4\3\2\2\2")
        buf.write("\u0247\u024b\7$\2\2\u0248\u024a\5K&\2\u0249\u0248\3\2")
        buf.write("\2\2\u024a\u024d\3\2\2\2\u024b\u024c\3\2\2\2\u024b\u0249")
        buf.write("\3\2\2\2\u024c\u024e\3\2\2\2\u024d\u024b\3\2\2\2\u024e")
        buf.write("\u024f\7^\2\2\u024f\u0250\n\5\2\2\u0250\u0251\3\2\2\2")
        buf.write("\u0251\u0252\b[\5\2\u0252\u00b6\3\2\2\2\u0253\u0254\13")
        buf.write("\2\2\2\u0254\u0255\b\\\6\2\u0255\u00b8\3\2\2\2\32\2\u011f")
        buf.write("\u0124\u0129\u012f\u0134\u013b\u0141\u0143\u0146\u014b")
        buf.write("\u014f\u015c\u0162\u016b\u0173\u0177\u0181\u018d\u01fe")
        buf.write("\u0200\u0206\u0242\u024b\7\3%\2\b\2\2\3Z\3\3[\4\3\\\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER = 1
    REAL = 2
    BOOLEAN = 3
    STRING = 4
    ARRAY = 5
    LSP = 6
    RSP = 7
    CL = 8
    LP = 9
    RP = 10
    LB = 11
    RB = 12
    SM = 13
    CM = 14
    DOUBLEDOT = 15
    NOT = 16
    OR = 17
    NE = 18
    LT = 19
    LTE = 20
    INTEGERDIV = 21
    MOD = 22
    AND = 23
    GT = 24
    GTE = 25
    EQ = 26
    ADD = 27
    SUB = 28
    MUL = 29
    DIV = 30
    EQOP = 31
    INTLIT = 32
    REALLIT = 33
    BOOLLIT = 34
    STRINGLIT = 35
    COMMENT1 = 36
    COMMENT2 = 37
    COMMENT3 = 38
    RETURN_ = 39
    BREAK = 40
    CONTINUE = 41
    FOR = 42
    TO = 43
    DOWNTO = 44
    DO = 45
    IF = 46
    THEN = 47
    ELSE = 48
    WHILE = 49
    BEGIN = 50
    END = 51
    FUNCTION = 52
    PROCEDURE = 53
    VAR = 54
    OF = 55
    WITH = 56
    ID = 57
    WS = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "':'", "'('", "')'", "'{'", "'}'", "';'", "','", 
            "'..'", "'<>'", "'<'", "'<='", "'>'", "'>='", "'='", "'+'", 
            "'-'", "'*'", "'/'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "REAL", "BOOLEAN", "STRING", "ARRAY", "LSP", "RSP", 
            "CL", "LP", "RP", "LB", "RB", "SM", "CM", "DOUBLEDOT", "NOT", 
            "OR", "NE", "LT", "LTE", "INTEGERDIV", "MOD", "AND", "GT", "GTE", 
            "EQ", "ADD", "SUB", "MUL", "DIV", "EQOP", "INTLIT", "REALLIT", 
            "BOOLLIT", "STRINGLIT", "COMMENT1", "COMMENT2", "COMMENT3", 
            "RETURN_", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", 
            "IF", "THEN", "ELSE", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "OF", "WITH", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "INTEGER", "REAL", "BOOLEAN", "STRING", "ARRAY", "LSP", 
                  "RSP", "CL", "LP", "RP", "LB", "RB", "SM", "CM", "DOUBLEDOT", 
                  "NOT", "OR", "NE", "LT", "LTE", "INTEGERDIV", "MOD", "AND", 
                  "GT", "GTE", "EQ", "ADD", "SUB", "MUL", "DIV", "EQOP", 
                  "Exponent", "INTLIT", "REALLIT", "BOOLLIT", "STRINGLIT", 
                  "Stringfactor", "COMMENT1", "COMMENT2", "COMMENT3", "RETURN_", 
                  "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", 
                  "THEN", "ELSE", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
                  "VAR", "OF", "WITH", "Letter", "Digit", "ID", "WS", "A", 
                  "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 
                  "X", "Y", "Z", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[35] = self.STRINGLIT_action 
            actions[88] = self.UNCLOSE_STRING_action 
            actions[89] = self.ILLEGAL_ESCAPE_action 
            actions[90] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text[1:len(self.text)-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


