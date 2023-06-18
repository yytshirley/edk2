# Generated from SourceVfrSyntax.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



from VfrCompiler.IfrCtypes import *
from VfrCompiler.IfrFormPkg import *
from VfrCompiler.IfrUtility import *
from VfrCompiler.IfrTree import *
from VfrCompiler.IfrPreProcess import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0102")
        buf.write("\u0c5a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\3\2\5\2\u019c\n\2\3\2\5\2\u019f\n\2\3\3\3\3\3\3\7\3\u01a4")
        buf.write("\n\3\f\3\16\3\u01a7\13\3\3\4\3\4\3\5\3\5\3\5\5\5\u01ae")
        buf.write("\n\5\3\5\3\5\5\5\u01b2\n\5\3\6\5\6\u01b5\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7\u01bd\n\7\3\7\3\7\3\b\5\b\u01c2\n\b")
        buf.write("\3\b\3\b\5\b\u01c6\n\b\3\b\5\b\u01c9\n\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u01cf\n\b\3\b\3\b\3\t\5\t\u01d4\n\t\3\t\3\t\5\t")
        buf.write("\u01d8\n\t\3\t\5\t\u01db\n\t\3\t\3\t\3\t\3\t\5\t\u01e1")
        buf.write("\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u01f3\n\n\f\n\16\n\u01f6\13\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u01fd\n\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u0206\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u020f\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u0218")
        buf.write("\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u0221\n")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u022a\n\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u0233\n\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u023c\n\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\5\23\u0245\n\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\5\24\u024e\n\24\3\24\3\24")
        buf.write("\3\25\3\25\5\25\u0254\n\25\3\25\3\25\3\25\3\25\3\26\3")
        buf.write("\26\5\26\u025c\n\26\3\26\3\26\3\26\3\26\3\27\3\27\5\27")
        buf.write("\u0264\n\27\3\27\3\27\3\27\3\27\3\30\3\30\5\30\u026c\n")
        buf.write("\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u028a\n\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\5\31\u0291\n\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u0298\n\31\3\31\3\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\5\32\u02a1\n\32\3\32\3\32\5\32\u02a5\n\32\3\32")
        buf.write("\3\32\5\32\u02a9\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u02c7\n\34\3\34\3\34\3\35\3\35\3\35\7\35\u02ce\n")
        buf.write("\35\f\35\16\35\u02d1\13\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u02dc\n\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u02e4\n\37\3 \7 \u02e7\n \f \16 \u02ea")
        buf.write("\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u02f6\n!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0306")
        buf.write("\n\"\5\"\u0308\n\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\5#\u031d\n#\3#\3#\3#\3#\5#\u0323")
        buf.write("\n#\3#\5#\u0326\n#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0342\n")
        buf.write("$\3$\3$\3$\3$\5$\u0348\n$\3$\5$\u034b\n$\3$\3$\3$\3$\3")
        buf.write("$\7$\u0352\n$\f$\16$\u0355\13$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0367\n$\3$\5$\u036a\n$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\5%\u0373\n%\3&\3&\3&\3&\3&\3&\3&\5")
        buf.write("&\u037c\n&\3&\5&\u037f\n&\3&\3&\3&\3&\3&\3&\3&\6&\u0388")
        buf.write("\n&\r&\16&\u0389\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\5+\u03ab\n+\3+\3+\3+\3+\3+\5+\u03b2\n+\3+\3")
        buf.write("+\3+\3+\5+\u03b8\n+\3+\5+\u03bb\n+\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\5-\u03d3")
        buf.write("\n-\3.\3.\3.\3.\3.\3.\3.\7.\u03dc\n.\f.\16.\u03df\13.")
        buf.write("\5.\u03e1\n.\3/\3/\3/\3/\3/\3/\3/\5/\u03ea\n/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\7/\u040a\n/\f/\16/\u040d")
        buf.write("\13/\3/\5/\u0410\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\5\62\u041d\n\62\3\63\3\63\3\63\7")
        buf.write("\63\u0422\n\63\f\63\16\63\u0425\13\63\3\64\3\64\3\64\3")
        buf.write("\64\3\64\5\64\u042c\n\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\7\64\u0437\n\64\f\64\16\64\u043a\13\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u044e\n\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\5\66\u0455\n\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\7\66")
        buf.write("\u0464\n\66\f\66\16\66\u0467\13\66\3\66\7\66\u046a\n\66")
        buf.write("\f\66\16\66\u046d\13\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\38\39\39\39\39\39\39\39\3:\3:\3:\5:\u0482\n:\3")
        buf.write(";\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u048f\n;\3;\3;\5;\u0493")
        buf.write("\n;\3;\3;\3;\5;\u0498\n;\3;\3;\7;\u049c\n;\f;\16;\u049f")
        buf.write("\13;\5;\u04a1\n;\3;\3;\5;\u04a5\n;\3<\3<\5<\u04a9\n<\3")
        buf.write("=\3=\3=\7=\u04ae\n=\f=\16=\u04b1\13=\3>\3>\3>\5>\u04b6")
        buf.write("\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\5?\u04cd\n?\3?\3?\3?\3?\3?\3?\7?\u04d5\n")
        buf.write("?\f?\16?\u04d8\13?\3?\3?\3?\3?\3?\5?\u04df\n?\5?\u04e1")
        buf.write("\n?\3?\3?\5?\u04e5\n?\3?\3?\3@\3@\3@\5@\u04ec\n@\3A\3")
        buf.write("A\5A\u04f0\nA\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\5B\u0502\nB\3B\3B\3B\3B\3B\5B\u0509\nB\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\5B\u0515\nB\3B\3B\3B\3B\3B\5B\u051c")
        buf.write("\nB\3B\3B\3B\3B\3B\3B\5B\u0524\nB\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\5B\u052d\nB\3B\3B\5B\u0531\nB\3B\5B\u0534\nB\3B\3B\3")
        buf.write("B\3B\3B\5B\u053b\nB\3B\3B\3B\3B\3B\5B\u0542\nB\5B\u0544")
        buf.write("\nB\3B\3B\5B\u0548\nB\3B\3B\3C\3C\3C\7C\u054f\nC\fC\16")
        buf.write("C\u0552\13C\3D\3D\3D\5D\u0557\nD\3E\3E\3E\3E\3E\3E\3E")
        buf.write("\3E\3E\3E\5E\u0563\nE\3E\3E\3E\3F\3F\3F\3F\3F\3F\5F\u056e")
        buf.write("\nF\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u057b\nG\3H\3")
        buf.write("H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\7H\u058a\nH\fH\16H")
        buf.write("\u058d\13H\3H\3H\5H\u0591\nH\3H\3H\3H\5H\u0596\nH\3I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\7I\u05a5\nI\fI\16I")
        buf.write("\u05a8\13I\3I\3I\5I\u05ac\nI\3I\3I\3I\5I\u05b1\nI\3J\3")
        buf.write("J\3J\3J\3J\3J\5J\u05b9\nJ\3K\3K\3K\3K\3K\5K\u05c0\nK\3")
        buf.write("L\3L\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3")
        buf.write("N\3N\3N\3N\3N\3N\3N\5N\u05db\nN\3N\5N\u05de\nN\3N\3N\3")
        buf.write("N\5N\u05e3\nN\3O\7O\u05e6\nO\fO\16O\u05e9\13O\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\5P\u05f2\nP\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5")
        buf.write("Q\u05fd\nQ\3R\3R\3R\3R\3R\3R\3R\3R\7R\u0607\nR\fR\16R")
        buf.write("\u060a\13R\3R\3R\5R\u060e\nR\3R\3R\3R\5R\u0613\nR\3S\3")
        buf.write("S\3S\3S\3S\3S\3S\3S\7S\u061d\nS\fS\16S\u0620\13S\3S\3")
        buf.write("S\5S\u0624\nS\3S\3S\3S\5S\u0629\nS\3T\3T\3T\3T\3T\3T\3")
        buf.write("T\3T\5T\u0633\nT\3T\3T\3T\3T\5T\u0639\nT\3U\3U\3U\3U\3")
        buf.write("V\3V\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3")
        buf.write("W\3W\3W\3W\5W\u0655\nW\5W\u0657\nW\3W\3W\7W\u065b\nW\f")
        buf.write("W\16W\u065e\13W\3W\3W\3X\3X\3X\7X\u0665\nX\fX\16X\u0668")
        buf.write("\13X\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\5Y\u0676\nY\3")
        buf.write("Z\3Z\3Z\3Z\3[\3[\3[\3[\3\\\7\\\u0681\n\\\f\\\16\\\u0684")
        buf.write("\13\\\3]\3]\5]\u0688\n]\3^\3^\5^\u068c\n^\3_\3_\3_\3_")
        buf.write("\3_\3_\3_\3_\3_\5_\u0697\n_\3_\3_\3_\3_\5_\u069d\n_\3")
        buf.write("_\5_\u06a0\n_\3_\3_\3_\3_\3`\3`\3`\7`\u06a9\n`\f`\16`")
        buf.write("\u06ac\13`\3a\3a\3a\3a\3a\3a\3a\5a\u06b5\na\3b\3b\3b\3")
        buf.write("b\3b\3b\3b\3b\5b\u06bf\nb\3b\3b\3b\3b\3b\3b\3b\3b\3b\3")
        buf.write("b\3b\3c\3c\3c\7c\u06cf\nc\fc\16c\u06d2\13c\3d\3d\3d\5")
        buf.write("d\u06d7\nd\3e\3e\5e\u06db\ne\3f\3f\3f\3f\3f\3f\3f\3f\3")
        buf.write("f\5f\u06e6\nf\3f\3f\3f\3f\5f\u06ec\nf\3f\5f\u06ef\nf\3")
        buf.write("f\3f\3f\3f\3f\3g\3g\3g\5g\u06f9\ng\3g\3g\5g\u06fd\ng\3")
        buf.write("g\3g\3g\3g\5g\u0703\ng\3g\3g\5g\u0707\ng\3g\3g\3g\3g\3")
        buf.write("g\5g\u070e\ng\3g\5g\u0711\ng\3h\3h\3h\7h\u0716\nh\fh\16")
        buf.write("h\u0719\13h\3i\3i\3i\3i\3i\3i\3i\3i\3i\3i\5i\u0725\ni")
        buf.write("\3j\3j\3j\3j\3j\3j\3j\3j\3j\5j\u0730\nj\3j\5j\u0733\n")
        buf.write("j\3j\3j\3j\3j\3k\3k\3k\7k\u073c\nk\fk\16k\u073f\13k\3")
        buf.write("l\3l\5l\u0743\nl\3m\3m\3m\3m\3m\3m\3m\3m\5m\u074d\nm\3")
        buf.write("m\3m\3m\3m\5m\u0753\nm\3m\5m\u0756\nm\3m\3m\3m\3m\5m\u075c")
        buf.write("\nm\3m\3m\3m\3m\3m\5m\u0763\nm\3m\3m\3m\3m\3m\3n\3n\3")
        buf.write("n\7n\u076d\nn\fn\16n\u0770\13n\3o\3o\3o\3o\5o\u0776\n")
        buf.write("o\3p\3p\3p\3p\3p\3p\3p\3p\5p\u0780\np\3p\3p\3p\3p\5p\u0786")
        buf.write("\np\3p\5p\u0789\np\3p\3p\3p\3p\5p\u078f\np\3p\3p\3p\3")
        buf.write("p\3p\5p\u0796\np\3p\3p\3p\3p\3p\5p\u079d\np\3p\5p\u07a0")
        buf.write("\np\3p\3p\3p\3p\3q\3q\3q\7q\u07a9\nq\fq\16q\u07ac\13q")
        buf.write("\3r\3r\3r\5r\u07b1\nr\3s\3s\3s\3s\3s\3s\3s\5s\u07ba\n")
        buf.write("s\3s\5s\u07bd\ns\3s\3s\3s\3s\3s\5s\u07c4\ns\3s\3s\3s\3")
        buf.write("s\3t\3t\3t\7t\u07cd\nt\ft\16t\u07d0\13t\3u\3u\3u\3u\3")
        buf.write("u\5u\u07d7\nu\3v\3v\3v\3v\3v\3v\3v\3v\5v\u07e1\nv\3v\3")
        buf.write("v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3")
        buf.write("v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3")
        buf.write("v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3")
        buf.write("v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\5")
        buf.write("v\u082c\nv\3v\7v\u082f\nv\fv\16v\u0832\13v\5v\u0834\n")
        buf.write("v\3v\3v\3v\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3")
        buf.write("w\5w\u0848\nw\3w\3w\3w\3w\3w\5w\u084f\nw\5w\u0851\nw\3")
        buf.write("x\3x\3x\7x\u0856\nx\fx\16x\u0859\13x\3y\3y\3y\3y\3y\3")
        buf.write("y\3y\3y\5y\u0863\ny\3z\3z\3z\3z\3z\3z\3z\3z\5z\u086d\n")
        buf.write("z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3")
        buf.write("z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3")
        buf.write("z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3")
        buf.write("z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3z\3")
        buf.write("z\3z\5z\u08b8\nz\3z\7z\u08bb\nz\fz\16z\u08be\13z\5z\u08c0")
        buf.write("\nz\3z\3z\3z\3{\3{\3{\3{\3{\3{\3{\3{\3{\3{\3{\3{\3{\3")
        buf.write("{\3{\5{\u08d4\n{\3{\3{\3{\3{\3{\5{\u08db\n{\5{\u08dd\n")
        buf.write("{\3|\3|\3|\7|\u08e2\n|\f|\16|\u08e5\13|\3}\3}\3}\3}\3")
        buf.write("}\3}\3}\3}\5}\u08ef\n}\3~\3~\3~\3~\5~\u08f5\n~\3\177\3")
        buf.write("\177\3\177\3\177\3\177\3\u0080\3\u0080\3\u0081\3\u0081")
        buf.write("\3\u0082\3\u0082\3\u0082\3\u0082\3\u0082\3\u0082\5\u0082")
        buf.write("\u0906\n\u0082\3\u0083\3\u0083\3\u0083\3\u0083\5\u0083")
        buf.write("\u090c\n\u0083\3\u0084\3\u0084\3\u0084\3\u0084\7\u0084")
        buf.write("\u0912\n\u0084\f\u0084\16\u0084\u0915\13\u0084\3\u0084")
        buf.write("\3\u0084\3\u0084\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085")
        buf.write("\3\u0085\7\u0085\u0920\n\u0085\f\u0085\16\u0085\u0923")
        buf.write("\13\u0085\3\u0085\3\u0085\5\u0085\u0927\n\u0085\3\u0085")
        buf.write("\3\u0085\3\u0085\3\u0086\3\u0086\3\u0086\3\u0086\3\u0086")
        buf.write("\3\u0086\7\u0086\u0932\n\u0086\f\u0086\16\u0086\u0935")
        buf.write("\13\u0086\3\u0086\3\u0086\5\u0086\u0939\n\u0086\3\u0086")
        buf.write("\3\u0086\3\u0086\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write("\3\u0087\7\u0087\u0944\n\u0087\f\u0087\16\u0087\u0947")
        buf.write("\13\u0087\3\u0087\3\u0087\5\u0087\u094b\n\u0087\3\u0087")
        buf.write("\3\u0087\3\u0087\7\u0087\u0950\n\u0087\f\u0087\16\u0087")
        buf.write("\u0953\13\u0087\3\u0087\3\u0087\3\u0087\3\u0088\3\u0088")
        buf.write("\3\u0088\3\u0088\3\u0088\3\u0088\7\u0088\u095e\n\u0088")
        buf.write("\f\u0088\16\u0088\u0961\13\u0088\3\u0088\3\u0088\5\u0088")
        buf.write("\u0965\n\u0088\3\u0088\3\u0088\3\u0088\7\u0088\u096a\n")
        buf.write("\u0088\f\u0088\16\u0088\u096d\13\u0088\3\u0088\3\u0088")
        buf.write("\3\u0088\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089")
        buf.write("\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089")
        buf.write("\7\u0089\u097f\n\u0089\f\u0089\16\u0089\u0982\13\u0089")
        buf.write("\3\u0089\3\u0089\5\u0089\u0986\n\u0089\3\u0089\3\u0089")
        buf.write("\3\u0089\3\u0089\3\u008a\3\u008a\3\u008a\5\u008a\u098f")
        buf.write("\n\u008a\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b\5\u008b")
        buf.write("\u0996\n\u008b\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b")
        buf.write("\5\u008b\u099d\n\u008b\3\u008b\3\u008b\3\u008c\3\u008c")
        buf.write("\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c")
        buf.write("\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c")
        buf.write("\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\5\u008c\u09b6")
        buf.write("\n\u008c\3\u008c\3\u008c\3\u008d\3\u008d\3\u008d\3\u008d")
        buf.write("\3\u008d\3\u008d\3\u008d\5\u008d\u09c1\n\u008d\3\u008d")
        buf.write("\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d")
        buf.write("\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d")
        buf.write("\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\7\u008d\u09d7")
        buf.write("\n\u008d\f\u008d\16\u008d\u09da\13\u008d\5\u008d\u09dc")
        buf.write("\n\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\5\u008d")
        buf.write("\u09e3\n\u008d\5\u008d\u09e5\n\u008d\3\u008d\3\u008d\3")
        buf.write("\u008e\3\u008e\3\u008e\5\u008e\u09ec\n\u008e\3\u008e\3")
        buf.write("\u008e\3\u008f\3\u008f\5\u008f\u09f2\n\u008f\3\u008f\3")
        buf.write("\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\5\u008f\u09fe\n\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\5\u008f")
        buf.write("\u0a08\n\u008f\3\u008f\5\u008f\u0a0b\n\u008f\3\u0090\3")
        buf.write("\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a18\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a1e\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a24\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a2a\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a30\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a36\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a3c\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a42\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a48\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u0a4e\n\u0090\5\u0090")
        buf.write("\u0a50\n\u0090\3\u0090\7\u0090\u0a53\n\u0090\f\u0090\16")
        buf.write("\u0090\u0a56\13\u0090\5\u0090\u0a58\n\u0090\3\u0090\3")
        buf.write("\u0090\7\u0090\u0a5c\n\u0090\f\u0090\16\u0090\u0a5f\13")
        buf.write("\u0090\3\u0090\5\u0090\u0a62\n\u0090\3\u0090\3\u0090\3")
        buf.write("\u0091\3\u0091\3\u0091\3\u0091\3\u0091\5\u0091\u0a6b\n")
        buf.write("\u0091\3\u0091\3\u0091\7\u0091\u0a6f\n\u0091\f\u0091\16")
        buf.write("\u0091\u0a72\13\u0091\3\u0091\3\u0091\3\u0091\3\u0092")
        buf.write("\3\u0092\3\u0092\3\u0093\3\u0093\3\u0094\3\u0094\3\u0094")
        buf.write("\7\u0094\u0a7f\n\u0094\f\u0094\16\u0094\u0a82\13\u0094")
        buf.write("\3\u0095\3\u0095\3\u0095\7\u0095\u0a87\n\u0095\f\u0095")
        buf.write("\16\u0095\u0a8a\13\u0095\3\u0096\3\u0096\3\u0096\7\u0096")
        buf.write("\u0a8f\n\u0096\f\u0096\16\u0096\u0a92\13\u0096\3\u0097")
        buf.write("\3\u0097\3\u0097\7\u0097\u0a97\n\u0097\f\u0097\16\u0097")
        buf.write("\u0a9a\13\u0097\3\u0098\3\u0098\3\u0098\7\u0098\u0a9f")
        buf.write("\n\u0098\f\u0098\16\u0098\u0aa2\13\u0098\3\u0099\3\u0099")
        buf.write("\7\u0099\u0aa6\n\u0099\f\u0099\16\u0099\u0aa9\13\u0099")
        buf.write("\3\u009a\3\u009a\3\u009a\3\u009a\5\u009a\u0aaf\n\u009a")
        buf.write("\3\u009b\3\u009b\7\u009b\u0ab3\n\u009b\f\u009b\16\u009b")
        buf.write("\u0ab6\13\u009b\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c")
        buf.write("\3\u009c\3\u009c\3\u009c\5\u009c\u0ac0\n\u009c\3\u009d")
        buf.write("\3\u009d\7\u009d\u0ac4\n\u009d\f\u009d\16\u009d\u0ac7")
        buf.write("\13\u009d\3\u009e\3\u009e\3\u009e\3\u009e\5\u009e\u0acd")
        buf.write("\n\u009e\3\u009f\3\u009f\7\u009f\u0ad1\n\u009f\f\u009f")
        buf.write("\16\u009f\u0ad4\13\u009f\3\u00a0\3\u00a0\3\u00a0\3\u00a0")
        buf.write("\5\u00a0\u0ada\n\u00a0\3\u00a1\3\u00a1\7\u00a1\u0ade\n")
        buf.write("\u00a1\f\u00a1\16\u00a1\u0ae1\13\u00a1\3\u00a2\3\u00a2")
        buf.write("\3\u00a2\3\u00a2\3\u00a2\3\u00a2\5\u00a2\u0ae9\n\u00a2")
        buf.write("\3\u00a3\7\u00a3\u0aec\n\u00a3\f\u00a3\16\u00a3\u0aef")
        buf.write("\13\u00a3\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a4")
        buf.write("\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5")
        buf.write("\3\u00a5\3\u00a5\3\u00a5\3\u00a5\5\u00a5\u0b02\n\u00a5")
        buf.write("\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a6")
        buf.write("\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7")
        buf.write("\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a8")
        buf.write("\3\u00a8\3\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00aa")
        buf.write("\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa")
        buf.write("\3\u00aa\3\u00aa\3\u00aa\5\u00aa\u0b2a\n\u00aa\3\u00ab")
        buf.write("\3\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write("\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write("\3\u00ac\3\u00ac\5\u00ac\u0b3d\n\u00ac\3\u00ad\3\u00ad")
        buf.write("\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad")
        buf.write("\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u0b4b\n\u00ad\3\u00ae")
        buf.write("\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae")
        buf.write("\3\u00ae\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u0b59\n\u00ae")
        buf.write("\3\u00af\3\u00af\3\u00af\3\u00af\6\u00af\u0b5f\n\u00af")
        buf.write("\r\u00af\16\u00af\u0b60\3\u00b0\3\u00b0\3\u00b0\3\u00b0")
        buf.write("\3\u00b0\3\u00b0\3\u00b0\7\u00b0\u0b6a\n\u00b0\f\u00b0")
        buf.write("\16\u00b0\u0b6d\13\u00b0\5\u00b0\u0b6f\n\u00b0\3\u00b1")
        buf.write("\3\u00b1\3\u00b1\3\u00b1\5\u00b1\u0b75\n\u00b1\3\u00b2")
        buf.write("\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b3\3\u00b3\3\u00b3")
        buf.write("\3\u00b3\3\u00b3\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4")
        buf.write("\3\u00b4\3\u00b4\5\u00b4\u0b88\n\u00b4\3\u00b4\3\u00b4")
        buf.write("\3\u00b5\3\u00b5\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6")
        buf.write("\3\u00b7\3\u00b7\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8")
        buf.write("\3\u00b8\3\u00b8\5\u00b8\u0b9c\n\u00b8\3\u00b8\3\u00b8")
        buf.write("\3\u00b9\3\u00b9\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba")
        buf.write("\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\5\u00ba\u0bac")
        buf.write("\n\u00ba\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bc")
        buf.write("\3\u00bc\3\u00bc\3\u00bc\3\u00bc\3\u00bd\3\u00bd\3\u00bd")
        buf.write("\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00bd\5\u00bd")
        buf.write("\u0bc1\n\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00bd")
        buf.write("\5\u00bd\u0bc8\n\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00be")
        buf.write("\3\u00be\3\u00be\3\u00be\3\u00be\3\u00bf\3\u00bf\3\u00bf")
        buf.write("\3\u00bf\3\u00bf\3\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c0")
        buf.write("\5\u00c0\u0bdc\n\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c0")
        buf.write("\3\u00c1\3\u00c1\3\u00c1\3\u00c1\3\u00c1\3\u00c2\3\u00c2")
        buf.write("\3\u00c2\3\u00c2\3\u00c2\3\u00c3\3\u00c3\3\u00c3\3\u00c3")
        buf.write("\3\u00c3\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c4")
        buf.write("\3\u00c4\5\u00c4\u0bf8\n\u00c4\3\u00c4\3\u00c4\3\u00c4")
        buf.write("\3\u00c4\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5")
        buf.write("\u0c03\n\u00c5\3\u00c6\3\u00c6\3\u00c6\3\u00c6\3\u00c6")
        buf.write("\3\u00c6\3\u00c6\3\u00c6\3\u00c6\3\u00c7\3\u00c7\3\u00c7")
        buf.write("\3\u00c7\3\u00c7\7\u00c7\u0c13\n\u00c7\f\u00c7\16\u00c7")
        buf.write("\u0c16\13\u00c7\3\u00c7\3\u00c7\3\u00c7\3\u00c7\3\u00c7")
        buf.write("\3\u00c7\3\u00c7\3\u00c7\3\u00c8\3\u00c8\3\u00c9\3\u00c9")
        buf.write("\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9")
        buf.write("\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\3\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cb")
        buf.write("\3\u00cb\3\u00cb\7\u00cb\u0c3b\n\u00cb\f\u00cb\16\u00cb")
        buf.write("\u0c3e\13\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cb")
        buf.write("\3\u00cb\3\u00cb\3\u00cb\3\u00cc\3\u00cc\3\u00cd\3\u00cd")
        buf.write("\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd")
        buf.write("\7\u00cd\u0c53\n\u00cd\f\u00cd\16\u00cd\u0c56\13\u00cd")
        buf.write("\3\u00cd\3\u00cd\3\u00cd\2\2\u00ce\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a")
        buf.write("\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac")
        buf.write("\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be")
        buf.write("\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0")
        buf.write("\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2")
        buf.write("\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4")
        buf.write("\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106")
        buf.write("\u0108\u010a\u010c\u010e\u0110\u0112\u0114\u0116\u0118")
        buf.write("\u011a\u011c\u011e\u0120\u0122\u0124\u0126\u0128\u012a")
        buf.write("\u012c\u012e\u0130\u0132\u0134\u0136\u0138\u013a\u013c")
        buf.write("\u013e\u0140\u0142\u0144\u0146\u0148\u014a\u014c\u014e")
        buf.write("\u0150\u0152\u0154\u0156\u0158\u015a\u015c\u015e\u0160")
        buf.write("\u0162\u0164\u0166\u0168\u016a\u016c\u016e\u0170\u0172")
        buf.write("\u0174\u0176\u0178\u017a\u017c\u017e\u0180\u0182\u0184")
        buf.write("\u0186\u0188\u018a\u018c\u018e\u0190\u0192\u0194\u0196")
        buf.write("\u0198\2\13\3\2\4\5\3\2\u0085\u0086\3\2\u008a\u008c\3")
        buf.write("\2RV\3\2\u00fa\u00fb\3\2\u00ef\u00f2\4\2\u00d3\u00d9\u00fa")
        buf.write("\u00fb\3\2\u00f6\u00f7\3\2\u00f8\u00fa\2\u0d7c\2\u019b")
        buf.write("\3\2\2\2\4\u01a5\3\2\2\2\6\u01a8\3\2\2\2\b\u01aa\3\2\2")
        buf.write("\2\n\u01b4\3\2\2\2\f\u01b6\3\2\2\2\16\u01c1\3\2\2\2\20")
        buf.write("\u01d3\3\2\2\2\22\u01f4\3\2\2\2\24\u01f7\3\2\2\2\26\u0200")
        buf.write("\3\2\2\2\30\u0209\3\2\2\2\32\u0212\3\2\2\2\34\u021b\3")
        buf.write("\2\2\2\36\u0224\3\2\2\2 \u022d\3\2\2\2\"\u0236\3\2\2\2")
        buf.write("$\u023f\3\2\2\2&\u0248\3\2\2\2(\u0251\3\2\2\2*\u0259\3")
        buf.write("\2\2\2,\u0261\3\2\2\2.\u0269\3\2\2\2\60\u0271\3\2\2\2")
        buf.write("\62\u029d\3\2\2\2\64\u02aa\3\2\2\2\66\u02ba\3\2\2\28\u02ca")
        buf.write("\3\2\2\2:\u02db\3\2\2\2<\u02e3\3\2\2\2>\u02e8\3\2\2\2")
        buf.write("@\u02f5\3\2\2\2B\u02f7\3\2\2\2D\u030b\3\2\2\2F\u0330\3")
        buf.write("\2\2\2H\u0372\3\2\2\2J\u0374\3\2\2\2L\u0390\3\2\2\2N\u0397")
        buf.write("\3\2\2\2P\u039e\3\2\2\2R\u03a3\3\2\2\2T\u03aa\3\2\2\2")
        buf.write("V\u03bc\3\2\2\2X\u03d2\3\2\2\2Z\u03e0\3\2\2\2\\\u040f")
        buf.write("\3\2\2\2^\u0411\3\2\2\2`\u0418\3\2\2\2b\u041c\3\2\2\2")
        buf.write("d\u041e\3\2\2\2f\u0426\3\2\2\2h\u044d\3\2\2\2j\u044f\3")
        buf.write("\2\2\2l\u0471\3\2\2\2n\u0474\3\2\2\2p\u0477\3\2\2\2r\u0481")
        buf.write("\3\2\2\2t\u0483\3\2\2\2v\u04a8\3\2\2\2x\u04aa\3\2\2\2")
        buf.write("z\u04b5\3\2\2\2|\u04b7\3\2\2\2~\u04eb\3\2\2\2\u0080\u04ef")
        buf.write("\3\2\2\2\u0082\u04f1\3\2\2\2\u0084\u054b\3\2\2\2\u0086")
        buf.write("\u0556\3\2\2\2\u0088\u0558\3\2\2\2\u008a\u056d\3\2\2\2")
        buf.write("\u008c\u057a\3\2\2\2\u008e\u057c\3\2\2\2\u0090\u0597\3")
        buf.write("\2\2\2\u0092\u05b2\3\2\2\2\u0094\u05bf\3\2\2\2\u0096\u05c1")
        buf.write("\3\2\2\2\u0098\u05c9\3\2\2\2\u009a\u05ce\3\2\2\2\u009c")
        buf.write("\u05e7\3\2\2\2\u009e\u05f1\3\2\2\2\u00a0\u05fc\3\2\2\2")
        buf.write("\u00a2\u05fe\3\2\2\2\u00a4\u0614\3\2\2\2\u00a6\u062a\3")
        buf.write("\2\2\2\u00a8\u063a\3\2\2\2\u00aa\u063e\3\2\2\2\u00ac\u0640")
        buf.write("\3\2\2\2\u00ae\u0661\3\2\2\2\u00b0\u0675\3\2\2\2\u00b2")
        buf.write("\u0677\3\2\2\2\u00b4\u067b\3\2\2\2\u00b6\u0682\3\2\2\2")
        buf.write("\u00b8\u0687\3\2\2\2\u00ba\u068b\3\2\2\2\u00bc\u068d\3")
        buf.write("\2\2\2\u00be\u06a5\3\2\2\2\u00c0\u06b4\3\2\2\2\u00c2\u06b6")
        buf.write("\3\2\2\2\u00c4\u06cb\3\2\2\2\u00c6\u06d6\3\2\2\2\u00c8")
        buf.write("\u06da\3\2\2\2\u00ca\u06dc\3\2\2\2\u00cc\u06f5\3\2\2\2")
        buf.write("\u00ce\u0712\3\2\2\2\u00d0\u0724\3\2\2\2\u00d2\u0726\3")
        buf.write("\2\2\2\u00d4\u0738\3\2\2\2\u00d6\u0742\3\2\2\2\u00d8\u0744")
        buf.write("\3\2\2\2\u00da\u0769\3\2\2\2\u00dc\u0775\3\2\2\2\u00de")
        buf.write("\u0777\3\2\2\2\u00e0\u07a5\3\2\2\2\u00e2\u07b0\3\2\2\2")
        buf.write("\u00e4\u07b2\3\2\2\2\u00e6\u07c9\3\2\2\2\u00e8\u07d6\3")
        buf.write("\2\2\2\u00ea\u07d8\3\2\2\2\u00ec\u0850\3\2\2\2\u00ee\u0852")
        buf.write("\3\2\2\2\u00f0\u0862\3\2\2\2\u00f2\u0864\3\2\2\2\u00f4")
        buf.write("\u08dc\3\2\2\2\u00f6\u08de\3\2\2\2\u00f8\u08ee\3\2\2\2")
        buf.write("\u00fa\u08f4\3\2\2\2\u00fc\u08f6\3\2\2\2\u00fe\u08fb\3")
        buf.write("\2\2\2\u0100\u08fd\3\2\2\2\u0102\u0905\3\2\2\2\u0104\u090b")
        buf.write("\3\2\2\2\u0106\u090d\3\2\2\2\u0108\u0919\3\2\2\2\u010a")
        buf.write("\u092b\3\2\2\2\u010c\u093d\3\2\2\2\u010e\u0957\3\2\2\2")
        buf.write("\u0110\u0971\3\2\2\2\u0112\u098e\3\2\2\2\u0114\u0990\3")
        buf.write("\2\2\2\u0116\u09a0\3\2\2\2\u0118\u09b9\3\2\2\2\u011a\u09e8")
        buf.write("\3\2\2\2\u011c\u09ef\3\2\2\2\u011e\u0a0c\3\2\2\2\u0120")
        buf.write("\u0a65\3\2\2\2\u0122\u0a76\3\2\2\2\u0124\u0a79\3\2\2\2")
        buf.write("\u0126\u0a7b\3\2\2\2\u0128\u0a83\3\2\2\2\u012a\u0a8b\3")
        buf.write("\2\2\2\u012c\u0a93\3\2\2\2\u012e\u0a9b\3\2\2\2\u0130\u0aa3")
        buf.write("\3\2\2\2\u0132\u0aae\3\2\2\2\u0134\u0ab0\3\2\2\2\u0136")
        buf.write("\u0abf\3\2\2\2\u0138\u0ac1\3\2\2\2\u013a\u0acc\3\2\2\2")
        buf.write("\u013c\u0ace\3\2\2\2\u013e\u0ad9\3\2\2\2\u0140\u0adb\3")
        buf.write("\2\2\2\u0142\u0ae8\3\2\2\2\u0144\u0aed\3\2\2\2\u0146\u0af2")
        buf.write("\3\2\2\2\u0148\u0b01\3\2\2\2\u014a\u0b03\3\2\2\2\u014c")
        buf.write("\u0b0a\3\2\2\2\u014e\u0b11\3\2\2\2\u0150\u0b1a\3\2\2\2")
        buf.write("\u0152\u0b29\3\2\2\2\u0154\u0b2b\3\2\2\2\u0156\u0b2d\3")
        buf.write("\2\2\2\u0158\u0b3e\3\2\2\2\u015a\u0b4c\3\2\2\2\u015c\u0b5a")
        buf.write("\3\2\2\2\u015e\u0b6e\3\2\2\2\u0160\u0b70\3\2\2\2\u0162")
        buf.write("\u0b76\3\2\2\2\u0164\u0b7b\3\2\2\2\u0166\u0b80\3\2\2\2")
        buf.write("\u0168\u0b8b\3\2\2\2\u016a\u0b8d\3\2\2\2\u016c\u0b92\3")
        buf.write("\2\2\2\u016e\u0b94\3\2\2\2\u0170\u0b9f\3\2\2\2\u0172\u0bab")
        buf.write("\3\2\2\2\u0174\u0bad\3\2\2\2\u0176\u0bb2\3\2\2\2\u0178")
        buf.write("\u0bb7\3\2\2\2\u017a\u0bcc\3\2\2\2\u017c\u0bd1\3\2\2\2")
        buf.write("\u017e\u0bd6\3\2\2\2\u0180\u0be1\3\2\2\2\u0182\u0be6\3")
        buf.write("\2\2\2\u0184\u0beb\3\2\2\2\u0186\u0bf0\3\2\2\2\u0188\u0c02")
        buf.write("\3\2\2\2\u018a\u0c04\3\2\2\2\u018c\u0c0d\3\2\2\2\u018e")
        buf.write("\u0c1f\3\2\2\2\u0190\u0c21\3\2\2\2\u0192\u0c2a\3\2\2\2")
        buf.write("\u0194\u0c33\3\2\2\2\u0196\u0c47\3\2\2\2\u0198\u0c49\3")
        buf.write("\2\2\2\u019a\u019c\5\4\3\2\u019b\u019a\3\2\2\2\u019b\u019c")
        buf.write("\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u019f\5\60\31\2\u019e")
        buf.write("\u019d\3\2\2\2\u019e\u019f\3\2\2\2\u019f\3\3\2\2\2\u01a0")
        buf.write("\u01a4\5\f\7\2\u01a1\u01a4\5\16\b\2\u01a2\u01a4\5\20\t")
        buf.write("\2\u01a3\u01a0\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\5\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8")
        buf.write("\u01a9\7\3\2\2\u01a9\7\3\2\2\2\u01aa\u01ad\t\2\2\2\u01ab")
        buf.write("\u01ac\7!\2\2\u01ac\u01ae\7\u00fb\2\2\u01ad\u01ab\3\2")
        buf.write("\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01b0")
        buf.write("\7!\2\2\u01b0\u01b2\7\u00fa\2\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\t\3\2\2\2\u01b3\u01b5\7\u00fa\2\2")
        buf.write("\u01b4\u01b3\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\13\3\2")
        buf.write("\2\2\u01b6\u01b7\7\6\2\2\u01b7\u01b8\7\7\2\2\u01b8\u01bc")
        buf.write("\7\30\2\2\u01b9\u01bd\5\6\4\2\u01ba\u01bd\5\b\5\2\u01bb")
        buf.write("\u01bd\5\n\6\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bc\u01bb\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\3")
        buf.write("\2\2\2\u01be\u01bf\7\31\2\2\u01bf\r\3\2\2\2\u01c0\u01c2")
        buf.write("\7\u0084\2\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c3\u01c5\7P\2\2\u01c4\u01c6\7O\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c8\3\2\2\2")
        buf.write("\u01c7\u01c9\7\u00fb\2\2\u01c8\u01c7\3\2\2\2\u01c8\u01c9")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\7\26\2\2\u01cb")
        buf.write("\u01cc\5\22\n\2\u01cc\u01ce\7\27\2\2\u01cd\u01cf\7\u00fb")
        buf.write("\2\2\u01ce\u01cd\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0")
        buf.write("\3\2\2\2\u01d0\u01d1\7 \2\2\u01d1\17\3\2\2\2\u01d2\u01d4")
        buf.write("\7\u0084\2\2\u01d3\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d7\7Q\2\2\u01d6\u01d8\7O\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2")
        buf.write("\u01d9\u01db\7\u00fb\2\2\u01da\u01d9\3\2\2\2\u01da\u01db")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\7\26\2\2\u01dd")
        buf.write("\u01de\5\22\n\2\u01de\u01e0\7\27\2\2\u01df\u01e1\7\u00fb")
        buf.write("\2\2\u01e0\u01df\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e3\7 \2\2\u01e3\21\3\2\2\2\u01e4\u01f3")
        buf.write("\5\24\13\2\u01e5\u01f3\5\26\f\2\u01e6\u01f3\5\30\r\2\u01e7")
        buf.write("\u01f3\5\32\16\2\u01e8\u01f3\5\34\17\2\u01e9\u01f3\5\36")
        buf.write("\20\2\u01ea\u01f3\5 \21\2\u01eb\u01f3\5\"\22\2\u01ec\u01f3")
        buf.write("\5$\23\2\u01ed\u01f3\5&\24\2\u01ee\u01f3\5(\25\2\u01ef")
        buf.write("\u01f3\5*\26\2\u01f0\u01f3\5,\27\2\u01f1\u01f3\5.\30\2")
        buf.write("\u01f2\u01e4\3\2\2\2\u01f2\u01e5\3\2\2\2\u01f2\u01e6\3")
        buf.write("\2\2\2\u01f2\u01e7\3\2\2\2\u01f2\u01e8\3\2\2\2\u01f2\u01e9")
        buf.write("\3\2\2\2\u01f2\u01ea\3\2\2\2\u01f2\u01eb\3\2\2\2\u01f2")
        buf.write("\u01ec\3\2\2\2\u01f2\u01ed\3\2\2\2\u01f2\u01ee\3\2\2\2")
        buf.write("\u01f2\u01ef\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f1\3")
        buf.write("\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\23\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8")
        buf.write("\7S\2\2\u01f8\u01fc\7\u00fb\2\2\u01f9\u01fa\7\32\2\2\u01fa")
        buf.write("\u01fb\7\u00fa\2\2\u01fb\u01fd\7\33\2\2\u01fc\u01f9\3")
        buf.write("\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff")
        buf.write("\7 \2\2\u01ff\25\3\2\2\2\u0200\u0201\7T\2\2\u0201\u0205")
        buf.write("\7\u00fb\2\2\u0202\u0203\7\32\2\2\u0203\u0204\7\u00fa")
        buf.write("\2\2\u0204\u0206\7\33\2\2\u0205\u0202\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\7 \2\2\u0208")
        buf.write("\27\3\2\2\2\u0209\u020a\7U\2\2\u020a\u020e\7\u00fb\2\2")
        buf.write("\u020b\u020c\7\32\2\2\u020c\u020d\7\u00fa\2\2\u020d\u020f")
        buf.write("\7\33\2\2\u020e\u020b\3\2\2\2\u020e\u020f\3\2\2\2\u020f")
        buf.write("\u0210\3\2\2\2\u0210\u0211\7 \2\2\u0211\31\3\2\2\2\u0212")
        buf.write("\u0213\7V\2\2\u0213\u0217\7\u00fb\2\2\u0214\u0215\7\32")
        buf.write("\2\2\u0215\u0216\7\u00fa\2\2\u0216\u0218\7\33\2\2\u0217")
        buf.write("\u0214\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0219\3\2\2\2")
        buf.write("\u0219\u021a\7 \2\2\u021a\33\3\2\2\2\u021b\u021c\7R\2")
        buf.write("\2\u021c\u0220\7\u00fb\2\2\u021d\u021e\7\32\2\2\u021e")
        buf.write("\u021f\7\u00fa\2\2\u021f\u0221\7\33\2\2\u0220\u021d\3")
        buf.write("\2\2\2\u0220\u0221\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0223")
        buf.write("\7 \2\2\u0223\35\3\2\2\2\u0224\u0225\7W\2\2\u0225\u0229")
        buf.write("\7\u00fb\2\2\u0226\u0227\7\32\2\2\u0227\u0228\7\u00fa")
        buf.write("\2\2\u0228\u022a\7\33\2\2\u0229\u0226\3\2\2\2\u0229\u022a")
        buf.write("\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c\7 \2\2\u022c")
        buf.write("\37\3\2\2\2\u022d\u022e\7X\2\2\u022e\u0232\7\u00fb\2\2")
        buf.write("\u022f\u0230\7\32\2\2\u0230\u0231\7\u00fa\2\2\u0231\u0233")
        buf.write("\7\33\2\2\u0232\u022f\3\2\2\2\u0232\u0233\3\2\2\2\u0233")
        buf.write("\u0234\3\2\2\2\u0234\u0235\7 \2\2\u0235!\3\2\2\2\u0236")
        buf.write("\u0237\7Y\2\2\u0237\u023b\7\u00fb\2\2\u0238\u0239\7\32")
        buf.write("\2\2\u0239\u023a\7\u00fa\2\2\u023a\u023c\7\33\2\2\u023b")
        buf.write("\u0238\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d\3\2\2\2")
        buf.write("\u023d\u023e\7 \2\2\u023e#\3\2\2\2\u023f\u0240\7Z\2\2")
        buf.write("\u0240\u0244\7\u00fb\2\2\u0241\u0242\7\32\2\2\u0242\u0243")
        buf.write("\7\u00fa\2\2\u0243\u0245\7\33\2\2\u0244\u0241\3\2\2\2")
        buf.write("\u0244\u0245\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247\7")
        buf.write(" \2\2\u0247%\3\2\2\2\u0248\u0249\7\u00fb\2\2\u0249\u024d")
        buf.write("\7\u00fb\2\2\u024a\u024b\7\32\2\2\u024b\u024c\7\u00fa")
        buf.write("\2\2\u024c\u024e\7\33\2\2\u024d\u024a\3\2\2\2\u024d\u024e")
        buf.write("\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250\7 \2\2\u0250")
        buf.write("\'\3\2\2\2\u0251\u0253\7S\2\2\u0252\u0254\7\u00fb\2\2")
        buf.write("\u0253\u0252\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0255\3")
        buf.write("\2\2\2\u0255\u0256\7\36\2\2\u0256\u0257\7\u00fa\2\2\u0257")
        buf.write("\u0258\7 \2\2\u0258)\3\2\2\2\u0259\u025b\7T\2\2\u025a")
        buf.write("\u025c\7\u00fb\2\2\u025b\u025a\3\2\2\2\u025b\u025c\3\2")
        buf.write("\2\2\u025c\u025d\3\2\2\2\u025d\u025e\7\36\2\2\u025e\u025f")
        buf.write("\7\u00fa\2\2\u025f\u0260\7 \2\2\u0260+\3\2\2\2\u0261\u0263")
        buf.write("\7U\2\2\u0262\u0264\7\u00fb\2\2\u0263\u0262\3\2\2\2\u0263")
        buf.write("\u0264\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0266\7\36\2")
        buf.write("\2\u0266\u0267\7\u00fa\2\2\u0267\u0268\7 \2\2\u0268-\3")
        buf.write("\2\2\2\u0269\u026b\7V\2\2\u026a\u026c\7\u00fb\2\2\u026b")
        buf.write("\u026a\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026d\3\2\2\2")
        buf.write("\u026d\u026e\7\36\2\2\u026e\u026f\7\u00fa\2\2\u026f\u0270")
        buf.write("\7 \2\2\u0270/\3\2\2\2\u0271\u0272\7+\2\2\u0272\u0273")
        buf.write("\7[\2\2\u0273\u0274\7\b\2\2\u0274\u0275\5\66\34\2\u0275")
        buf.write("\u0276\7!\2\2\u0276\u0277\7.\2\2\u0277\u0278\7\b\2\2\u0278")
        buf.write("\u0279\7\u00ec\2\2\u0279\u027a\7\30\2\2\u027a\u027b\7")
        buf.write("\u00fb\2\2\u027b\u027c\7\31\2\2\u027c\u027d\7!\2\2\u027d")
        buf.write("\u027e\7=\2\2\u027e\u027f\7\b\2\2\u027f\u0280\7\u00ec")
        buf.write("\2\2\u0280\u0281\7\30\2\2\u0281\u0282\7\u00fb\2\2\u0282")
        buf.write("\u0283\7\31\2\2\u0283\u0289\7!\2\2\u0284\u0285\7\u0083")
        buf.write("\2\2\u0285\u0286\7\b\2\2\u0286\u0287\5\62\32\2\u0287\u0288")
        buf.write("\7!\2\2\u0288\u028a\3\2\2\2\u0289\u0284\3\2\2\2\u0289")
        buf.write("\u028a\3\2\2\2\u028a\u0290\3\2\2\2\u028b\u028c\7\u0081")
        buf.write("\2\2\u028c\u028d\7\b\2\2\u028d\u028e\58\35\2\u028e\u028f")
        buf.write("\7!\2\2\u028f\u0291\3\2\2\2\u0290\u028b\3\2\2\2\u0290")
        buf.write("\u0291\3\2\2\2\u0291\u0297\3\2\2\2\u0292\u0293\7\u0082")
        buf.write("\2\2\u0293\u0294\7\b\2\2\u0294\u0295\5<\37\2\u0295\u0296")
        buf.write("\7!\2\2\u0296\u0298\3\2\2\2\u0297\u0292\3\2\2\2\u0297")
        buf.write("\u0298\3\2\2\2\u0298\u0299\3\2\2\2\u0299\u029a\5> \2\u029a")
        buf.write("\u029b\7-\2\2\u029b\u029c\7 \2\2\u029c\61\3\2\2\2\u029d")
        buf.write("\u02a0\5\66\34\2\u029e\u029f\7(\2\2\u029f\u02a1\5\66\34")
        buf.write("\2\u02a0\u029e\3\2\2\2\u02a0\u02a1\3\2\2\2\u02a1\u02a4")
        buf.write("\3\2\2\2\u02a2\u02a3\7(\2\2\u02a3\u02a5\5\66\34\2\u02a4")
        buf.write("\u02a2\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02a8\3\2\2\2")
        buf.write("\u02a6\u02a7\7(\2\2\u02a7\u02a9\5\66\34\2\u02a8\u02a6")
        buf.write("\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\63\3\2\2\2\u02aa\u02ab")
        buf.write("\7\u00fa\2\2\u02ab\u02ac\7!\2\2\u02ac\u02ad\7\u00fa\2")
        buf.write("\2\u02ad\u02ae\7!\2\2\u02ae\u02af\7\u00fa\2\2\u02af\u02b0")
        buf.write("\7!\2\2\u02b0\u02b1\7\u00fa\2\2\u02b1\u02b2\7!\2\2\u02b2")
        buf.write("\u02b3\7\u00fa\2\2\u02b3\u02b4\7!\2\2\u02b4\u02b5\7\u00fa")
        buf.write("\2\2\u02b5\u02b6\7!\2\2\u02b6\u02b7\7\u00fa\2\2\u02b7")
        buf.write("\u02b8\7!\2\2\u02b8\u02b9\7\u00fa\2\2\u02b9\65\3\2\2\2")
        buf.write("\u02ba\u02bb\7\26\2\2\u02bb\u02bc\7\u00fa\2\2\u02bc\u02bd")
        buf.write("\7!\2\2\u02bd\u02be\7\u00fa\2\2\u02be\u02bf\7!\2\2\u02bf")
        buf.write("\u02c0\7\u00fa\2\2\u02c0\u02c6\7!\2\2\u02c1\u02c2\7\26")
        buf.write("\2\2\u02c2\u02c3\5\64\33\2\u02c3\u02c4\7\27\2\2\u02c4")
        buf.write("\u02c7\3\2\2\2\u02c5\u02c7\5\64\33\2\u02c6\u02c1\3\2\2")
        buf.write("\2\u02c6\u02c5\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8\u02c9")
        buf.write("\7\27\2\2\u02c9\67\3\2\2\2\u02ca\u02cf\5:\36\2\u02cb\u02cc")
        buf.write("\7(\2\2\u02cc\u02ce\5:\36\2\u02cd\u02cb\3\2\2\2\u02ce")
        buf.write("\u02d1\3\2\2\2\u02cf\u02cd\3\2\2\2\u02cf\u02d0\3\2\2\2")
        buf.write("\u02d09\3\2\2\2\u02d1\u02cf\3\2\2\2\u02d2\u02dc\7\u00ac")
        buf.write("\2\2\u02d3\u02dc\7\u00ad\2\2\u02d4\u02dc\7\u00ae\2\2\u02d5")
        buf.write("\u02dc\7\u00af\2\2\u02d6\u02dc\7\u00b0\2\2\u02d7\u02dc")
        buf.write("\7\u00b1\2\2\u02d8\u02dc\7\u00b2\2\2\u02d9\u02dc\7\u00fb")
        buf.write("\2\2\u02da\u02dc\7\u00fa\2\2\u02db\u02d2\3\2\2\2\u02db")
        buf.write("\u02d3\3\2\2\2\u02db\u02d4\3\2\2\2\u02db\u02d5\3\2\2\2")
        buf.write("\u02db\u02d6\3\2\2\2\u02db\u02d7\3\2\2\2\u02db\u02d8\3")
        buf.write("\2\2\2\u02db\u02d9\3\2\2\2\u02db\u02da\3\2\2\2\u02dc;")
        buf.write("\3\2\2\2\u02dd\u02e4\7\u00b3\2\2\u02de\u02e4\7\u00b4\2")
        buf.write("\2\u02df\u02e4\7\u00b5\2\2\u02e0\u02e4\7\u00b6\2\2\u02e1")
        buf.write("\u02e4\7\u00fb\2\2\u02e2\u02e4\7\u00fa\2\2\u02e3\u02dd")
        buf.write("\3\2\2\2\u02e3\u02de\3\2\2\2\u02e3\u02df\3\2\2\2\u02e3")
        buf.write("\u02e0\3\2\2\2\u02e3\u02e1\3\2\2\2\u02e3\u02e2\3\2\2\2")
        buf.write("\u02e4=\3\2\2\2\u02e5\u02e7\5@!\2\u02e6\u02e5\3\2\2\2")
        buf.write("\u02e7\u02ea\3\2\2\2\u02e8\u02e6\3\2\2\2\u02e8\u02e9\3")
        buf.write("\2\2\2\u02e9?\3\2\2\2\u02ea\u02e8\3\2\2\2\u02eb\u02f6")
        buf.write("\5f\64\2\u02ec\u02f6\5j\66\2\u02ed\u02f6\5l\67\2\u02ee")
        buf.write("\u02f6\5D#\2\u02ef\u02f6\5F$\2\u02f0\u02f6\5J&\2\u02f1")
        buf.write("\u02f6\5B\"\2\u02f2\u02f6\5L\'\2\u02f3\u02f6\5N(\2\u02f4")
        buf.write("\u02f6\5\u011e\u0090\2\u02f5\u02eb\3\2\2\2\u02f5\u02ec")
        buf.write("\3\2\2\2\u02f5\u02ed\3\2\2\2\u02f5\u02ee\3\2\2\2\u02f5")
        buf.write("\u02ef\3\2\2\2\u02f5\u02f0\3\2\2\2\u02f5\u02f1\3\2\2\2")
        buf.write("\u02f5\u02f2\3\2\2\2\u02f5\u02f3\3\2\2\2\u02f5\u02f4\3")
        buf.write("\2\2\2\u02f6A\3\2\2\2\u02f7\u02f8\7\u009b\2\2\u02f8\u02f9")
        buf.write("\7\u00fb\2\2\u02f9\u02fa\7!\2\2\u02fa\u02fb\7\62\2\2\u02fb")
        buf.write("\u02fc\7\b\2\2\u02fc\u02fd\7\u00ec\2\2\u02fd\u02fe\7\30")
        buf.write("\2\2\u02fe\u02ff\7\u00fb\2\2\u02ff\u0307\7\31\2\2\u0300")
        buf.write("\u0301\7!\2\2\u0301\u0302\7\u009c\2\2\u0302\u0305\7\b")
        buf.write("\2\2\u0303\u0306\7\u00fa\2\2\u0304\u0306\7\u00fb\2\2\u0305")
        buf.write("\u0303\3\2\2\2\u0305\u0304\3\2\2\2\u0306\u0308\3\2\2\2")
        buf.write("\u0307\u0300\3\2\2\2\u0307\u0308\3\2\2\2\u0308\u0309\3")
        buf.write("\2\2\2\u0309\u030a\7 \2\2\u030aC\3\2\2\2\u030b\u031c\7")
        buf.write("\u009d\2\2\u030c\u030d\7\u00fb\2\2\u030d\u031d\7!\2\2")
        buf.write("\u030e\u030f\7V\2\2\u030f\u031d\7!\2\2\u0310\u0311\7U")
        buf.write("\2\2\u0311\u031d\7!\2\2\u0312\u0313\7T\2\2\u0313\u031d")
        buf.write("\7!\2\2\u0314\u0315\7S\2\2\u0315\u031d\7!\2\2\u0316\u0317")
        buf.write("\7X\2\2\u0317\u031d\7!\2\2\u0318\u0319\7Y\2\2\u0319\u031d")
        buf.write("\7!\2\2\u031a\u031b\7Z\2\2\u031b\u031d\7!\2\2\u031c\u030c")
        buf.write("\3\2\2\2\u031c\u030e\3\2\2\2\u031c\u0310\3\2\2\2\u031c")
        buf.write("\u0312\3\2\2\2\u031c\u0314\3\2\2\2\u031c\u0316\3\2\2\2")
        buf.write("\u031c\u0318\3\2\2\2\u031c\u031a\3\2\2\2\u031d\u0325\3")
        buf.write("\2\2\2\u031e\u031f\7\u008f\2\2\u031f\u0322\7\b\2\2\u0320")
        buf.write("\u0323\7\u00fa\2\2\u0321\u0323\7\u00fb\2\2\u0322\u0320")
        buf.write("\3\2\2\2\u0322\u0321\3\2\2\2\u0323\u0324\3\2\2\2\u0324")
        buf.write("\u0326\7!\2\2\u0325\u031e\3\2\2\2\u0325\u0326\3\2\2\2")
        buf.write("\u0326\u0327\3\2\2\2\u0327\u0328\7\u008e\2\2\u0328\u0329")
        buf.write("\7\b\2\2\u0329\u032a\7\u00fb\2\2\u032a\u032b\7!\2\2\u032b")
        buf.write("\u032c\7[\2\2\u032c\u032d\7\b\2\2\u032d\u032e\5\66\34")
        buf.write("\2\u032e\u032f\7 \2\2\u032fE\3\2\2\2\u0330\u0341\7\u009e")
        buf.write("\2\2\u0331\u0332\7\u00fb\2\2\u0332\u0342\7!\2\2\u0333")
        buf.write("\u0334\7V\2\2\u0334\u0342\7!\2\2\u0335\u0336\7U\2\2\u0336")
        buf.write("\u0342\7!\2\2\u0337\u0338\7T\2\2\u0338\u0342\7!\2\2\u0339")
        buf.write("\u033a\7S\2\2\u033a\u0342\7!\2\2\u033b\u033c\7X\2\2\u033c")
        buf.write("\u0342\7!\2\2\u033d\u033e\7Y\2\2\u033e\u0342\7!\2\2\u033f")
        buf.write("\u0340\7Z\2\2\u0340\u0342\7!\2\2\u0341\u0331\3\2\2\2\u0341")
        buf.write("\u0333\3\2\2\2\u0341\u0335\3\2\2\2\u0341\u0337\3\2\2\2")
        buf.write("\u0341\u0339\3\2\2\2\u0341\u033b\3\2\2\2\u0341\u033d\3")
        buf.write("\2\2\2\u0341\u033f\3\2\2\2\u0342\u034a\3\2\2\2\u0343\u0344")
        buf.write("\7\u008f\2\2\u0344\u0347\7\b\2\2\u0345\u0348\7\u00fa\2")
        buf.write("\2\u0346\u0348\7\u00fb\2\2\u0347\u0345\3\2\2\2\u0347\u0346")
        buf.write("\3\2\2\2\u0348\u0349\3\2\2\2\u0349\u034b\7!\2\2\u034a")
        buf.write("\u0343\3\2\2\2\u034a\u034b\3\2\2\2\u034b\u034c\3\2\2\2")
        buf.write("\u034c\u034d\7\u009c\2\2\u034d\u034e\7\b\2\2\u034e\u0353")
        buf.write("\5H%\2\u034f\u0350\7(\2\2\u0350\u0352\5H%\2\u0351\u034f")
        buf.write("\3\2\2\2\u0352\u0355\3\2\2\2\u0353\u0351\3\2\2\2\u0353")
        buf.write("\u0354\3\2\2\2\u0354\u0356\3\2\2\2\u0355\u0353\3\2\2\2")
        buf.write("\u0356\u0369\7!\2\2\u0357\u0358\7\u008e\2\2\u0358\u0359")
        buf.write("\7\b\2\2\u0359\u035a\7\u00fb\2\2\u035a\u036a\7!\2\2\u035b")
        buf.write("\u035c\7\u008e\2\2\u035c\u035d\7\b\2\2\u035d\u035e\7\u00ec")
        buf.write("\2\2\u035e\u035f\7\30\2\2\u035f\u0360\7\u00fb\2\2\u0360")
        buf.write("\u0361\7\31\2\2\u0361\u0362\7!\2\2\u0362\u0363\7\u009f")
        buf.write("\2\2\u0363\u0366\7\b\2\2\u0364\u0367\7\u00fa\2\2\u0365")
        buf.write("\u0367\7\u00fb\2\2\u0366\u0364\3\2\2\2\u0366\u0365\3\2")
        buf.write("\2\2\u0367\u0368\3\2\2\2\u0368\u036a\7!\2\2\u0369\u0357")
        buf.write("\3\2\2\2\u0369\u035b\3\2\2\2\u036a\u036b\3\2\2\2\u036b")
        buf.write("\u036c\7[\2\2\u036c\u036d\7\b\2\2\u036d\u036e\5\66\34")
        buf.write("\2\u036e\u036f\7 \2\2\u036fG\3\2\2\2\u0370\u0373\7\u00fa")
        buf.write("\2\2\u0371\u0373\7\u00fb\2\2\u0372\u0370\3\2\2\2\u0372")
        buf.write("\u0371\3\2\2\2\u0373I\3\2\2\2\u0374\u0375\7\u00a0\2\2")
        buf.write("\u0375\u0376\7\u00fb\2\2\u0376\u037e\7!\2\2\u0377\u0378")
        buf.write("\7\u008f\2\2\u0378\u037b\7\b\2\2\u0379\u037c\7\u00fa\2")
        buf.write("\2\u037a\u037c\7\u00fb\2\2\u037b\u0379\3\2\2\2\u037b\u037a")
        buf.write("\3\2\2\2\u037c\u037d\3\2\2\2\u037d\u037f\7!\2\2\u037e")
        buf.write("\u0377\3\2\2\2\u037e\u037f\3\2\2\2\u037f\u0387\3\2\2\2")
        buf.write("\u0380\u0381\7\u008e\2\2\u0381\u0382\7\b\2\2\u0382\u0383")
        buf.write("\7\u00ec\2\2\u0383\u0384\7\30\2\2\u0384\u0385\7\u00fb")
        buf.write("\2\2\u0385\u0386\7\31\2\2\u0386\u0388\7!\2\2\u0387\u0380")
        buf.write("\3\2\2\2\u0388\u0389\3\2\2\2\u0389\u0387\3\2\2\2\u0389")
        buf.write("\u038a\3\2\2\2\u038a\u038b\3\2\2\2\u038b\u038c\7[\2\2")
        buf.write("\u038c\u038d\7\b\2\2\u038d\u038e\5\66\34\2\u038e\u038f")
        buf.write("\7 \2\2\u038fK\3\2\2\2\u0390\u0391\7l\2\2\u0391\u0392")
        buf.write("\5\u0126\u0094\2\u0392\u0393\7 \2\2\u0393\u0394\5> \2")
        buf.write("\u0394\u0395\7s\2\2\u0395\u0396\7 \2\2\u0396M\3\2\2\2")
        buf.write("\u0397\u0398\7k\2\2\u0398\u0399\5\u0126\u0094\2\u0399")
        buf.write("\u039a\7 \2\2\u039a\u039b\5> \2\u039b\u039c\7s\2\2\u039c")
        buf.write("\u039d\7 \2\2\u039dO\3\2\2\2\u039e\u039f\7\u00ec\2\2\u039f")
        buf.write("\u03a0\7\30\2\2\u03a0\u03a1\7\u00fb\2\2\u03a1\u03a2\7")
        buf.write("\31\2\2\u03a2Q\3\2\2\2\u03a3\u03a4\5T+\2\u03a4\u03a5\5")
        buf.write("V,\2\u03a5S\3\2\2\2\u03a6\u03a7\7\u008e\2\2\u03a7\u03a8")
        buf.write("\7\b\2\2\u03a8\u03a9\7\u00fb\2\2\u03a9\u03ab\7!\2\2\u03aa")
        buf.write("\u03a6\3\2\2\2\u03aa\u03ab\3\2\2\2\u03ab\u03b1\3\2\2\2")
        buf.write("\u03ac\u03ad\7\u008f\2\2\u03ad\u03ae\7\b\2\2\u03ae\u03af")
        buf.write("\5Z.\2\u03af\u03b0\7!\2\2\u03b0\u03b2\3\2\2\2\u03b1\u03ac")
        buf.write("\3\2\2\2\u03b1\u03b2\3\2\2\2\u03b2\u03ba\3\2\2\2\u03b3")
        buf.write("\u03b4\7\u0091\2\2\u03b4\u03b7\7\b\2\2\u03b5\u03b8\7\u00fa")
        buf.write("\2\2\u03b6\u03b8\7\u00fb\2\2\u03b7\u03b5\3\2\2\2\u03b7")
        buf.write("\u03b6\3\2\2\2\u03b8\u03b9\3\2\2\2\u03b9\u03bb\7!\2\2")
        buf.write("\u03ba\u03b3\3\2\2\2\u03ba\u03bb\3\2\2\2\u03bbU\3\2\2")
        buf.write("\2\u03bc\u03bd\7\62\2\2\u03bd\u03be\7\b\2\2\u03be\u03bf")
        buf.write("\7\u00ec\2\2\u03bf\u03c0\7\30\2\2\u03c0\u03c1\7\u00fb")
        buf.write("\2\2\u03c1\u03c2\7\31\2\2\u03c2\u03c3\7!\2\2\u03c3\u03c4")
        buf.write("\7=\2\2\u03c4\u03c5\7\b\2\2\u03c5\u03c6\7\u00ec\2\2\u03c6")
        buf.write("\u03c7\7\30\2\2\u03c7\u03c8\7\u00fb\2\2\u03c8\u03c9\7")
        buf.write("\31\2\2\u03c9W\3\2\2\2\u03ca\u03d3\7~\2\2\u03cb\u03d3")
        buf.write("\7y\2\2\u03cc\u03d3\7{\2\2\u03cd\u03d3\7\u0080\2\2\u03ce")
        buf.write("\u03d3\7|\2\2\u03cf\u03d3\7\177\2\2\u03d0\u03d3\7z\2\2")
        buf.write("\u03d1\u03d3\7}\2\2\u03d2\u03ca\3\2\2\2\u03d2\u03cb\3")
        buf.write("\2\2\2\u03d2\u03cc\3\2\2\2\u03d2\u03cd\3\2\2\2\u03d2\u03ce")
        buf.write("\3\2\2\2\u03d2\u03cf\3\2\2\2\u03d2\u03d0\3\2\2\2\u03d2")
        buf.write("\u03d1\3\2\2\2\u03d3Y\3\2\2\2\u03d4\u03d5\7\u00fb\2\2")
        buf.write("\u03d5\u03d6\7\32\2\2\u03d6\u03d7\7\u00fa\2\2\u03d7\u03e1")
        buf.write("\7\33\2\2\u03d8\u03dd\7\u00fb\2\2\u03d9\u03da\7\34\2\2")
        buf.write("\u03da\u03dc\5\u0160\u00b1\2\u03db\u03d9\3\2\2\2\u03dc")
        buf.write("\u03df\3\2\2\2\u03dd\u03db\3\2\2\2\u03dd\u03de\3\2\2\2")
        buf.write("\u03de\u03e1\3\2\2\2\u03df\u03dd\3\2\2\2\u03e0\u03d4\3")
        buf.write("\2\2\2\u03e0\u03d8\3\2\2\2\u03e1[\3\2\2\2\u03e2\u0410")
        buf.write("\7\u00d3\2\2\u03e3\u0410\7\u00d4\2\2\u03e4\u0410\7\u00d5")
        buf.write("\2\2\u03e5\u0410\7\u00d6\2\2\u03e6\u0410\7\u00d7\2\2\u03e7")
        buf.write("\u0410\7\u00fb\2\2\u03e8\u03ea\7\35\2\2\u03e9\u03e8\3")
        buf.write("\2\2\2\u03e9\u03ea\3\2\2\2\u03ea\u03eb\3\2\2\2\u03eb\u0410")
        buf.write("\7\u00fa\2\2\u03ec\u03ed\7\u00fa\2\2\u03ed\u03ee\7\36")
        buf.write("\2\2\u03ee\u03ef\7\u00fa\2\2\u03ef\u03f0\7\36\2\2\u03f0")
        buf.write("\u0410\7\u00fa\2\2\u03f1\u03f2\7\u00fa\2\2\u03f2\u03f3")
        buf.write("\7\37\2\2\u03f3\u03f4\7\u00fa\2\2\u03f4\u03f5\7\37\2\2")
        buf.write("\u03f5\u0410\7\u00fa\2\2\u03f6\u03f7\7\u00fa\2\2\u03f7")
        buf.write("\u03f8\7 \2\2\u03f8\u03f9\7\u00fa\2\2\u03f9\u03fa\7 \2")
        buf.write("\2\u03fa\u03fb\5\66\34\2\u03fb\u03fc\7 \2\2\u03fc\u03fd")
        buf.write("\7\u00ec\2\2\u03fd\u03fe\7\30\2\2\u03fe\u03ff\7\u00fb")
        buf.write("\2\2\u03ff\u0400\7\31\2\2\u0400\u0410\3\2\2\2\u0401\u0402")
        buf.write("\7\u00ec\2\2\u0402\u0403\7\30\2\2\u0403\u0404\7\u00fb")
        buf.write("\2\2\u0404\u0410\7\31\2\2\u0405\u0406\7\26\2\2\u0406\u040b")
        buf.write("\7\u00fa\2\2\u0407\u0408\7!\2\2\u0408\u040a\7\u00fa\2")
        buf.write("\2\u0409\u0407\3\2\2\2\u040a\u040d\3\2\2\2\u040b\u0409")
        buf.write("\3\2\2\2\u040b\u040c\3\2\2\2\u040c\u040e\3\2\2\2\u040d")
        buf.write("\u040b\3\2\2\2\u040e\u0410\7\27\2\2\u040f\u03e2\3\2\2")
        buf.write("\2\u040f\u03e3\3\2\2\2\u040f\u03e4\3\2\2\2\u040f\u03e5")
        buf.write("\3\2\2\2\u040f\u03e6\3\2\2\2\u040f\u03e7\3\2\2\2\u040f")
        buf.write("\u03e9\3\2\2\2\u040f\u03ec\3\2\2\2\u040f\u03f1\3\2\2\2")
        buf.write("\u040f\u03f6\3\2\2\2\u040f\u0401\3\2\2\2\u040f\u0405\3")
        buf.write("\2\2\2\u0410]\3\2\2\2\u0411\u0412\7\u0092\2\2\u0412\u0413")
        buf.write("\7\b\2\2\u0413\u0414\7\t\2\2\u0414\u0415\7\30\2\2\u0415")
        buf.write("\u0416\7\u00fb\2\2\u0416\u0417\7\31\2\2\u0417_\3\2\2\2")
        buf.write("\u0418\u0419\7\u0093\2\2\u0419a\3\2\2\2\u041a\u041d\5")
        buf.write("^\60\2\u041b\u041d\5`\61\2\u041c\u041a\3\2\2\2\u041c\u041b")
        buf.write("\3\2\2\2\u041dc\3\2\2\2\u041e\u0423\5b\62\2\u041f\u0420")
        buf.write("\7!\2\2\u0420\u0422\5b\62\2\u0421\u041f\3\2\2\2\u0422")
        buf.write("\u0425\3\2\2\2\u0423\u0421\3\2\2\2\u0423\u0424\3\2\2\2")
        buf.write("\u0424e\3\2\2\2\u0425\u0423\3\2\2\2\u0426\u0427\7\67\2")
        buf.write("\2\u0427\u0428\7/\2\2\u0428\u042b\7\b\2\2\u0429\u042c")
        buf.write("\7\u00fa\2\2\u042a\u042c\7\u00fb\2\2\u042b\u0429\3\2\2")
        buf.write("\2\u042b\u042a\3\2\2\2\u042c\u042d\3\2\2\2\u042d\u042e")
        buf.write("\7!\2\2\u042e\u042f\7.\2\2\u042f\u0430\7\b\2\2\u0430\u0431")
        buf.write("\7\u00ec\2\2\u0431\u0432\7\30\2\2\u0432\u0433\7\u00fb")
        buf.write("\2\2\u0433\u0434\7\31\2\2\u0434\u0438\7 \2\2\u0435\u0437")
        buf.write("\5h\65\2\u0436\u0435\3\2\2\2\u0437\u043a\3\2\2\2\u0438")
        buf.write("\u0436\3\2\2\2\u0438\u0439\3\2\2\2\u0439\u043b\3\2\2\2")
        buf.write("\u043a\u0438\3\2\2\2\u043b\u043c\7\66\2\2\u043c\u043d")
        buf.write("\7 \2\2\u043dg\3\2\2\2\u043e\u044e\5l\67\2\u043f\u044e")
        buf.write("\5n8\2\u0440\u044e\5p9\2\u0441\u044e\5\u00a6T\2\u0442")
        buf.write("\u044e\5r:\2\u0443\u044e\5\u008aF\2\u0444\u044e\5\u00fa")
        buf.write("~\2\u0445\u044e\5\u011a\u008e\2\u0446\u044e\5\u011c\u008f")
        buf.write("\2\u0447\u044e\5\u0112\u008a\2\u0448\u044e\5\u011e\u0090")
        buf.write("\2\u0449\u044e\5\u0122\u0092\2\u044a\u044b\5\u0098M\2")
        buf.write("\u044b\u044c\7 \2\2\u044c\u044e\3\2\2\2\u044d\u043e\3")
        buf.write("\2\2\2\u044d\u043f\3\2\2\2\u044d\u0440\3\2\2\2\u044d\u0441")
        buf.write("\3\2\2\2\u044d\u0442\3\2\2\2\u044d\u0443\3\2\2\2\u044d")
        buf.write("\u0444\3\2\2\2\u044d\u0445\3\2\2\2\u044d\u0446\3\2\2\2")
        buf.write("\u044d\u0447\3\2\2\2\u044d\u0448\3\2\2\2\u044d\u0449\3")
        buf.write("\2\2\2\u044d\u044a\3\2\2\2\u044ei\3\2\2\2\u044f\u0450")
        buf.write("\78\2\2\u0450\u0451\7/\2\2\u0451\u0454\7\b\2\2\u0452\u0455")
        buf.write("\7\u00fa\2\2\u0453\u0455\7\u00fb\2\2\u0454\u0452\3\2\2")
        buf.write("\2\u0454\u0453\3\2\2\2\u0455\u0456\3\2\2\2\u0456\u0465")
        buf.write("\7!\2\2\u0457\u0458\79\2\2\u0458\u0459\7\b\2\2\u0459\u045a")
        buf.write("\7\u00ec\2\2\u045a\u045b\7\30\2\2\u045b\u045c\7\u00fb")
        buf.write("\2\2\u045c\u045d\7\31\2\2\u045d\u045e\7 \2\2\u045e\u045f")
        buf.write("\7:\2\2\u045f\u0460\7\b\2\2\u0460\u0461\5\66\34\2\u0461")
        buf.write("\u0462\7 \2\2\u0462\u0464\3\2\2\2\u0463\u0457\3\2\2\2")
        buf.write("\u0464\u0467\3\2\2\2\u0465\u0463\3\2\2\2\u0465\u0466\3")
        buf.write("\2\2\2\u0466\u046b\3\2\2\2\u0467\u0465\3\2\2\2\u0468\u046a")
        buf.write("\5h\65\2\u0469\u0468\3\2\2\2\u046a\u046d\3\2\2\2\u046b")
        buf.write("\u0469\3\2\2\2\u046b\u046c\3\2\2\2\u046c\u046e\3\2\2\2")
        buf.write("\u046d\u046b\3\2\2\2\u046e\u046f\7\66\2\2\u046f\u0470")
        buf.write("\7 \2\2\u0470k\3\2\2\2\u0471\u0472\5^\60\2\u0472\u0473")
        buf.write("\7 \2\2\u0473m\3\2\2\2\u0474\u0475\5`\61\2\u0475\u0476")
        buf.write("\7 \2\2\u0476o\3\2\2\2\u0477\u0478\7\u0094\2\2\u0478\u0479")
        buf.write("\7\u00fb\2\2\u0479\u047a\7!\2\2\u047a\u047b\5\u0126\u0094")
        buf.write("\2\u047b\u047c\7\u0095\2\2\u047c\u047d\7 \2\2\u047dq\3")
        buf.write("\2\2\2\u047e\u0482\5t;\2\u047f\u0482\5|?\2\u0480\u0482")
        buf.write("\5\u0080A\2\u0481\u047e\3\2\2\2\u0481\u047f\3\2\2\2\u0481")
        buf.write("\u0480\3\2\2\2\u0482s\3\2\2\2\u0483\u0484\7;\2\2\u0484")
        buf.write("\u0485\7>\2\2\u0485\u0486\7\b\2\2\u0486\u0487\7\u00ec")
        buf.write("\2\2\u0487\u0488\7\30\2\2\u0488\u0489\7\u00fb\2\2\u0489")
        buf.write("\u048e\7\31\2\2\u048a\u048b\7!\2\2\u048b\u048c\7@\2\2")
        buf.write("\u048c\u048d\7\b\2\2\u048d\u048f\5x=\2\u048e\u048a\3\2")
        buf.write("\2\2\u048e\u048f\3\2\2\2\u048f\u04a4\3\2\2\2\u0490\u0491")
        buf.write("\7!\2\2\u0491\u0493\5d\63\2\u0492\u0490\3\2\2\2\u0492")
        buf.write("\u0493\3\2\2\2\u0493\u0494\3\2\2\2\u0494\u04a5\7 \2\2")
        buf.write("\u0495\u0496\7!\2\2\u0496\u0498\5d\63\2\u0497\u0495\3")
        buf.write("\2\2\2\u0497\u0498\3\2\2\2\u0498\u04a0\3\2\2\2\u0499\u049d")
        buf.write("\7!\2\2\u049a\u049c\5v<\2\u049b\u049a\3\2\2\2\u049c\u049f")
        buf.write("\3\2\2\2\u049d\u049b\3\2\2\2\u049d\u049e\3\2\2\2\u049e")
        buf.write("\u04a1\3\2\2\2\u049f\u049d\3\2\2\2\u04a0\u0499\3\2\2\2")
        buf.write("\u04a0\u04a1\3\2\2\2\u04a1\u04a2\3\2\2\2\u04a2\u04a3\7")
        buf.write("<\2\2\u04a3\u04a5\7 \2\2\u04a4\u0492\3\2\2\2\u04a4\u0497")
        buf.write("\3\2\2\2\u04a5u\3\2\2\2\u04a6\u04a9\5r:\2\u04a7\u04a9")
        buf.write("\5\u008aF\2\u04a8\u04a6\3\2\2\2\u04a8\u04a7\3\2\2\2\u04a9")
        buf.write("w\3\2\2\2\u04aa\u04af\5z>\2\u04ab\u04ac\7(\2\2\u04ac\u04ae")
        buf.write("\5z>\2\u04ad\u04ab\3\2\2\2\u04ae\u04b1\3\2\2\2\u04af\u04ad")
        buf.write("\3\2\2\2\u04af\u04b0\3\2\2\2\u04b0y\3\2\2\2\u04b1\u04af")
        buf.write("\3\2\2\2\u04b2\u04b6\7\u00fa\2\2\u04b3\u04b6\7\n\2\2\u04b4")
        buf.write("\u04b6\7\u00fb\2\2\u04b5\u04b2\3\2\2\2\u04b5\u04b3\3\2")
        buf.write("\2\2\u04b5\u04b4\3\2\2\2\u04b6{\3\2\2\2\u04b7\u04b8\7")
        buf.write(">\2\2\u04b8\u04b9\7=\2\2\u04b9\u04ba\7\b\2\2\u04ba\u04bb")
        buf.write("\7\u00ec\2\2\u04bb\u04bc\7\30\2\2\u04bc\u04bd\7\u00fb")
        buf.write("\2\2\u04bd\u04be\7\31\2\2\u04be\u04bf\7!\2\2\u04bf\u04c0")
        buf.write("\7>\2\2\u04c0\u04c1\7\b\2\2\u04c1\u04c2\7\u00ec\2\2\u04c2")
        buf.write("\u04c3\7\30\2\2\u04c3\u04c4\7\u00fb\2\2\u04c4\u04cc\7")
        buf.write("\31\2\2\u04c5\u04c6\7!\2\2\u04c6\u04c7\7>\2\2\u04c7\u04c8")
        buf.write("\7\b\2\2\u04c8\u04c9\7\u00ec\2\2\u04c9\u04ca\7\30\2\2")
        buf.write("\u04ca\u04cb\7\u00fb\2\2\u04cb\u04cd\7\31\2\2\u04cc\u04c5")
        buf.write("\3\2\2\2\u04cc\u04cd\3\2\2\2\u04cd\u04e0\3\2\2\2\u04ce")
        buf.write("\u04cf\7!\2\2\u04cf\u04d0\7@\2\2\u04d0\u04d1\7\b\2\2\u04d1")
        buf.write("\u04d6\5~@\2\u04d2\u04d3\7(\2\2\u04d3\u04d5\5~@\2\u04d4")
        buf.write("\u04d2\3\2\2\2\u04d5\u04d8\3\2\2\2\u04d6\u04d4\3\2\2\2")
        buf.write("\u04d6\u04d7\3\2\2\2\u04d7\u04d9\3\2\2\2\u04d8\u04d6\3")
        buf.write("\2\2\2\u04d9\u04da\7!\2\2\u04da\u04db\7t\2\2\u04db\u04de")
        buf.write("\7\b\2\2\u04dc\u04df\7\u00fa\2\2\u04dd\u04df\7\u00fb\2")
        buf.write("\2\u04de\u04dc\3\2\2\2\u04de\u04dd\3\2\2\2\u04df\u04e1")
        buf.write("\3\2\2\2\u04e0\u04ce\3\2\2\2\u04e0\u04e1\3\2\2\2\u04e1")
        buf.write("\u04e4\3\2\2\2\u04e2\u04e3\7!\2\2\u04e3\u04e5\5d\63\2")
        buf.write("\u04e4\u04e2\3\2\2\2\u04e4\u04e5\3\2\2\2\u04e5\u04e6\3")
        buf.write("\2\2\2\u04e6\u04e7\7 \2\2\u04e7}\3\2\2\2\u04e8\u04ec\7")
        buf.write("\u00fa\2\2\u04e9\u04ec\5X-\2\u04ea\u04ec\7\u00fb\2\2\u04eb")
        buf.write("\u04e8\3\2\2\2\u04eb\u04e9\3\2\2\2\u04eb\u04ea\3\2\2\2")
        buf.write("\u04ec\177\3\2\2\2\u04ed\u04f0\5\u0082B\2\u04ee\u04f0")
        buf.write("\5\u0088E\2\u04ef\u04ed\3\2\2\2\u04ef\u04ee\3\2\2\2\u04f0")
        buf.write("\u0081\3\2\2\2\u04f1\u0533\7n\2\2\u04f2\u04f3\7*\2\2\u04f3")
        buf.write("\u04f4\7\b\2\2\u04f4\u04f5\7\u00ec\2\2\u04f5\u04f6\7\30")
        buf.write("\2\2\u04f6\u04f7\7\u00fb\2\2\u04f7\u04f8\7\31\2\2\u04f8")
        buf.write("\u04f9\7!\2\2\u04f9\u04fa\7o\2\2\u04fa\u04fb\7\b\2\2\u04fb")
        buf.write("\u04fc\5\66\34\2\u04fc\u04fd\7!\2\2\u04fd\u04fe\7/\2\2")
        buf.write("\u04fe\u0501\7\b\2\2\u04ff\u0502\7\u00fa\2\2\u0500\u0502")
        buf.write("\7\u00fb\2\2\u0501\u04ff\3\2\2\2\u0501\u0500\3\2\2\2\u0502")
        buf.write("\u0503\3\2\2\2\u0503\u0504\7!\2\2\u0504\u0505\7\u0090")
        buf.write("\2\2\u0505\u0508\7\b\2\2\u0506\u0509\7\u00fa\2\2\u0507")
        buf.write("\u0509\7\u00fb\2\2\u0508\u0506\3\2\2\2\u0508\u0507\3\2")
        buf.write("\2\2\u0509\u050a\3\2\2\2\u050a\u050b\7!\2\2\u050b\u0534")
        buf.write("\3\2\2\2\u050c\u050d\7o\2\2\u050d\u050e\7\b\2\2\u050e")
        buf.write("\u050f\5\66\34\2\u050f\u0510\7!\2\2\u0510\u0511\7/\2\2")
        buf.write("\u0511\u0514\7\b\2\2\u0512\u0515\7\u00fa\2\2\u0513\u0515")
        buf.write("\7\u00fb\2\2\u0514\u0512\3\2\2\2\u0514\u0513\3\2\2\2\u0515")
        buf.write("\u0516\3\2\2\2\u0516\u0517\7!\2\2\u0517\u0518\7\u0090")
        buf.write("\2\2\u0518\u051b\7\b\2\2\u0519\u051c\7\u00fa\2\2\u051a")
        buf.write("\u051c\7\u00fb\2\2\u051b\u0519\3\2\2\2\u051b\u051a\3\2")
        buf.write("\2\2\u051c\u051d\3\2\2\2\u051d\u051e\7!\2\2\u051e\u0534")
        buf.write("\3\2\2\2\u051f\u0520\7/\2\2\u0520\u0523\7\b\2\2\u0521")
        buf.write("\u0524\7\u00fa\2\2\u0522\u0524\7\u00fb\2\2\u0523\u0521")
        buf.write("\3\2\2\2\u0523\u0522\3\2\2\2\u0524\u0525\3\2\2\2\u0525")
        buf.write("\u0526\7!\2\2\u0526\u0527\7\u0090\2\2\u0527\u052c\7\b")
        buf.write("\2\2\u0528\u0529\7\u00fb\2\2\u0529\u052d\7!\2\2\u052a")
        buf.write("\u052b\7\u00fa\2\2\u052b\u052d\7!\2\2\u052c\u0528\3\2")
        buf.write("\2\2\u052c\u052a\3\2\2\2\u052d\u0534\3\2\2\2\u052e\u0531")
        buf.write("\7\u00fa\2\2\u052f\u0531\7\u00fb\2\2\u0530\u052e\3\2\2")
        buf.write("\2\u0530\u052f\3\2\2\2\u0531\u0532\3\2\2\2\u0532\u0534")
        buf.write("\7!\2\2\u0533\u04f2\3\2\2\2\u0533\u050c\3\2\2\2\u0533")
        buf.write("\u051f\3\2\2\2\u0533\u0530\3\2\2\2\u0533\u0534\3\2\2\2")
        buf.write("\u0534\u0535\3\2\2\2\u0535\u053a\5R*\2\u0536\u0537\7!")
        buf.write("\2\2\u0537\u0538\7@\2\2\u0538\u0539\7\b\2\2\u0539\u053b")
        buf.write("\5\u0084C\2\u053a\u0536\3\2\2\2\u053a\u053b\3\2\2\2\u053b")
        buf.write("\u0543\3\2\2\2\u053c\u053d\7!\2\2\u053d\u053e\7t\2\2\u053e")
        buf.write("\u0541\7\b\2\2\u053f\u0542\7\u00fa\2\2\u0540\u0542\7\u00fb")
        buf.write("\2\2\u0541\u053f\3\2\2\2\u0541\u0540\3\2\2\2\u0542\u0544")
        buf.write("\3\2\2\2\u0543\u053c\3\2\2\2\u0543\u0544\3\2\2\2\u0544")
        buf.write("\u0547\3\2\2\2\u0545\u0546\7!\2\2\u0546\u0548\5\u00b6")
        buf.write("\\\2\u0547\u0545\3\2\2\2\u0547\u0548\3\2\2\2\u0548\u0549")
        buf.write("\3\2\2\2\u0549\u054a\7 \2\2\u054a\u0083\3\2\2\2\u054b")
        buf.write("\u0550\5\u0086D\2\u054c\u054d\7(\2\2\u054d\u054f\5\u0086")
        buf.write("D\2\u054e\u054c\3\2\2\2\u054f\u0552\3\2\2\2\u0550\u054e")
        buf.write("\3\2\2\2\u0550\u0551\3\2\2\2\u0551\u0085\3\2\2\2\u0552")
        buf.write("\u0550\3\2\2\2\u0553\u0557\7\u00fa\2\2\u0554\u0557\5X")
        buf.write("-\2\u0555\u0557\7\u00fb\2\2\u0556\u0553\3\2\2\2\u0556")
        buf.write("\u0554\3\2\2\2\u0556\u0555\3\2\2\2\u0557\u0087\3\2\2\2")
        buf.write("\u0558\u0559\7\u0099\2\2\u0559\u055a\7\u009b\2\2\u055a")
        buf.write("\u055b\7\b\2\2\u055b\u055c\7\u00fb\2\2\u055c\u055d\7!")
        buf.write("\2\2\u055d\u055e\5V,\2\u055e\u0562\7!\2\2\u055f\u0560")
        buf.write("\5d\63\2\u0560\u0561\7!\2\2\u0561\u0563\3\2\2\2\u0562")
        buf.write("\u055f\3\2\2\2\u0562\u0563\3\2\2\2\u0563\u0564\3\2\2\2")
        buf.write("\u0564\u0565\7\u009a\2\2\u0565\u0566\7 \2\2\u0566\u0089")
        buf.write("\3\2\2\2\u0567\u056e\5\u00ba^\2\u0568\u056e\5\u00eav\2")
        buf.write("\u0569\u056e\5\u00c8e\2\u056a\u056e\5\u00d6l\2\u056b\u056e")
        buf.write("\5\u00e4s\2\u056c\u056e\5\u00f2z\2\u056d\u0567\3\2\2\2")
        buf.write("\u056d\u0568\3\2\2\2\u056d\u0569\3\2\2\2\u056d\u056a\3")
        buf.write("\2\2\2\u056d\u056b\3\2\2\2\u056d\u056c\3\2\2\2\u056e\u008b")
        buf.write("\3\2\2\2\u056f\u0570\5b\62\2\u0570\u0571\7!\2\2\u0571")
        buf.write("\u057b\3\2\2\2\u0572\u057b\5\u008eH\2\u0573\u057b\5\u0090")
        buf.write("I\2\u0574\u057b\5\u0092J\2\u0575\u057b\5\u0094K\2\u0576")
        buf.write("\u057b\5\u0096L\2\u0577\u057b\5\u011e\u0090\2\u0578\u057b")
        buf.write("\5\u0098M\2\u0579\u057b\5\u009aN\2\u057a\u056f\3\2\2\2")
        buf.write("\u057a\u0572\3\2\2\2\u057a\u0573\3\2\2\2\u057a\u0574\3")
        buf.write("\2\2\2\u057a\u0575\3\2\2\2\u057a\u0576\3\2\2\2\u057a\u0577")
        buf.write("\3\2\2\2\u057a\u0578\3\2\2\2\u057a\u0579\3\2\2\2\u057b")
        buf.write("\u008d\3\2\2\2\u057c\u057d\7p\2\2\u057d\u057e\7\62\2\2")
        buf.write("\u057e\u057f\7\b\2\2\u057f\u0580\7\u00ec\2\2\u0580\u0581")
        buf.write("\7\30\2\2\u0581\u0582\7\u00fb\2\2\u0582\u0583\7\31\2\2")
        buf.write("\u0583\u0590\7!\2\2\u0584\u0585\7@\2\2\u0585\u0586\7\b")
        buf.write("\2\2\u0586\u058b\5\u00a0Q\2\u0587\u0588\7(\2\2\u0588\u058a")
        buf.write("\5\u00a0Q\2\u0589\u0587\3\2\2\2\u058a\u058d\3\2\2\2\u058b")
        buf.write("\u0589\3\2\2\2\u058b\u058c\3\2\2\2\u058c\u058e\3\2\2\2")
        buf.write("\u058d\u058b\3\2\2\2\u058e\u058f\7!\2\2\u058f\u0591\3")
        buf.write("\2\2\2\u0590\u0584\3\2\2\2\u0590\u0591\3\2\2\2\u0591\u0592")
        buf.write("\3\2\2\2\u0592\u0593\5\u0126\u0094\2\u0593\u0595\7s\2")
        buf.write("\2\u0594\u0596\7 \2\2\u0595\u0594\3\2\2\2\u0595\u0596")
        buf.write("\3\2\2\2\u0596\u008f\3\2\2\2\u0597\u0598\7r\2\2\u0598")
        buf.write("\u0599\7\62\2\2\u0599\u059a\7\b\2\2\u059a\u059b\7\u00ec")
        buf.write("\2\2\u059b\u059c\7\30\2\2\u059c\u059d\7\u00fb\2\2\u059d")
        buf.write("\u059e\7\31\2\2\u059e\u05ab\7!\2\2\u059f\u05a0\7@\2\2")
        buf.write("\u05a0\u05a1\7\b\2\2\u05a1\u05a6\5\u00a0Q\2\u05a2\u05a3")
        buf.write("\7(\2\2\u05a3\u05a5\5\u00a0Q\2\u05a4\u05a2\3\2\2\2\u05a5")
        buf.write("\u05a8\3\2\2\2\u05a6\u05a4\3\2\2\2\u05a6\u05a7\3\2\2\2")
        buf.write("\u05a7\u05a9\3\2\2\2\u05a8\u05a6\3\2\2\2\u05a9\u05aa\7")
        buf.write("!\2\2\u05aa\u05ac\3\2\2\2\u05ab\u059f\3\2\2\2\u05ab\u05ac")
        buf.write("\3\2\2\2\u05ac\u05ad\3\2\2\2\u05ad\u05ae\5\u0126\u0094")
        buf.write("\2\u05ae\u05b0\7s\2\2\u05af\u05b1\7 \2\2\u05b0\u05af\3")
        buf.write("\2\2\2\u05b0\u05b1\3\2\2\2\u05b1\u0091\3\2\2\2\u05b2\u05b3")
        buf.write("\7l\2\2\u05b3\u05b4\5\u0126\u0094\2\u05b4\u05b5\7 \2\2")
        buf.write("\u05b5\u05b6\5\u00b6\\\2\u05b6\u05b8\7s\2\2\u05b7\u05b9")
        buf.write("\7 \2\2\u05b8\u05b7\3\2\2\2\u05b8\u05b9\3\2\2\2\u05b9")
        buf.write("\u0093\3\2\2\2\u05ba\u05bb\7\u00a4\2\2\u05bb\u05bc\7\u00a5")
        buf.write("\2\2\u05bc\u05bd\7\b\2\2\u05bd\u05c0\7\u00fa\2\2\u05be")
        buf.write("\u05c0\7\u00fb\2\2\u05bf\u05ba\3\2\2\2\u05bf\u05be\3\2")
        buf.write("\2\2\u05c0\u0095\3\2\2\2\u05c1\u05c2\7\u00a6\2\2\u05c2")
        buf.write("\u05c3\7\b\2\2\u05c3\u05c4\7\u00ec\2\2\u05c4\u05c5\7\30")
        buf.write("\2\2\u05c5\u05c6\7\u00fb\2\2\u05c6\u05c7\7\31\2\2\u05c7")
        buf.write("\u05c8\7!\2\2\u05c8\u0097\3\2\2\2\u05c9\u05ca\7\u00eb")
        buf.write("\2\2\u05ca\u05cb\7\b\2\2\u05cb\u05cc\5\66\34\2\u05cc\u05cd")
        buf.write("\7!\2\2\u05cd\u0099\3\2\2\2\u05ce\u05cf\7q\2\2\u05cf\u05d0")
        buf.write("\7\62\2\2\u05d0\u05d1\7\b\2\2\u05d1\u05d2\7\u00ec\2\2")
        buf.write("\u05d2\u05d3\7\30\2\2\u05d3\u05d4\7\u00fb\2\2\u05d4\u05d5")
        buf.write("\7\31\2\2\u05d5\u05dd\7!\2\2\u05d6\u05d7\7M\2\2\u05d7")
        buf.write("\u05da\7\b\2\2\u05d8\u05db\7\u00fa\2\2\u05d9\u05db\7\u00fb")
        buf.write("\2\2\u05da\u05d8\3\2\2\2\u05da\u05d9\3\2\2\2\u05db\u05dc")
        buf.write("\3\2\2\2\u05dc\u05de\7!\2\2\u05dd\u05d6\3\2\2\2\u05dd")
        buf.write("\u05de\3\2\2\2\u05de\u05df\3\2\2\2\u05df\u05e0\5\u0126")
        buf.write("\u0094\2\u05e0\u05e2\7s\2\2\u05e1\u05e3\7 \2\2\u05e2\u05e1")
        buf.write("\3\2\2\2\u05e2\u05e3\3\2\2\2\u05e3\u009b\3\2\2\2\u05e4")
        buf.write("\u05e6\5\u008cG\2\u05e5\u05e4\3\2\2\2\u05e6\u05e9\3\2")
        buf.write("\2\2\u05e7\u05e5\3\2\2\2\u05e7\u05e8\3\2\2\2\u05e8\u009d")
        buf.write("\3\2\2\2\u05e9\u05e7\3\2\2\2\u05ea\u05f2\5\u00a2R\2\u05eb")
        buf.write("\u05f2\5\u00a4S\2\u05ec\u05f2\5\u00a8U\2\u05ed\u05f2\5")
        buf.write("\u00a6T\2\u05ee\u05f2\5\u00aaV\2\u05ef\u05f2\5\u00b2Z")
        buf.write("\2\u05f0\u05f2\5\u00b4[\2\u05f1\u05ea\3\2\2\2\u05f1\u05eb")
        buf.write("\3\2\2\2\u05f1\u05ec\3\2\2\2\u05f1\u05ed\3\2\2\2\u05f1")
        buf.write("\u05ee\3\2\2\2\u05f1\u05ef\3\2\2\2\u05f1\u05f0\3\2\2\2")
        buf.write("\u05f2\u009f\3\2\2\2\u05f3\u05fd\7\u00fa\2\2\u05f4\u05fd")
        buf.write("\7y\2\2\u05f5\u05fd\7v\2\2\u05f6\u05fd\7u\2\2\u05f7\u05fd")
        buf.write("\7{\2\2\u05f8\u05fd\7|\2\2\u05f9\u05fd\7z\2\2\u05fa\u05fd")
        buf.write("\7}\2\2\u05fb\u05fd\7\u00fb\2\2\u05fc\u05f3\3\2\2\2\u05fc")
        buf.write("\u05f4\3\2\2\2\u05fc\u05f5\3\2\2\2\u05fc\u05f6\3\2\2\2")
        buf.write("\u05fc\u05f7\3\2\2\2\u05fc\u05f8\3\2\2\2\u05fc\u05f9\3")
        buf.write("\2\2\2\u05fc\u05fa\3\2\2\2\u05fc\u05fb\3\2\2\2\u05fd\u00a1")
        buf.write("\3\2\2\2\u05fe\u05ff\7k\2\2\u05ff\u0600\5\u0126\u0094")
        buf.write("\2\u0600\u060d\7 \2\2\u0601\u0602\7@\2\2\u0602\u0603\7")
        buf.write("\b\2\2\u0603\u0608\5\u00a0Q\2\u0604\u0605\7(\2\2\u0605")
        buf.write("\u0607\5\u00a0Q\2\u0606\u0604\3\2\2\2\u0607\u060a\3\2")
        buf.write("\2\2\u0608\u0606\3\2\2\2\u0608\u0609\3\2\2\2\u0609\u060b")
        buf.write("\3\2\2\2\u060a\u0608\3\2\2\2\u060b\u060c\7!\2\2\u060c")
        buf.write("\u060e\3\2\2\2\u060d\u0601\3\2\2\2\u060d\u060e\3\2\2\2")
        buf.write("\u060e\u060f\3\2\2\2\u060f\u0610\5\u00b6\\\2\u0610\u0612")
        buf.write("\7s\2\2\u0611\u0613\7 \2\2\u0612\u0611\3\2\2\2\u0612\u0613")
        buf.write("\3\2\2\2\u0613\u00a3\3\2\2\2\u0614\u0615\7K\2\2\u0615")
        buf.write("\u0616\5\u0126\u0094\2\u0616\u0623\7 \2\2\u0617\u0618")
        buf.write("\7@\2\2\u0618\u0619\7\b\2\2\u0619\u061e\5\u00a0Q\2\u061a")
        buf.write("\u061b\7(\2\2\u061b\u061d\5\u00a0Q\2\u061c\u061a\3\2\2")
        buf.write("\2\u061d\u0620\3\2\2\2\u061e\u061c\3\2\2\2\u061e\u061f")
        buf.write("\3\2\2\2\u061f\u0621\3\2\2\2\u0620\u061e\3\2\2\2\u0621")
        buf.write("\u0622\7!\2\2\u0622\u0624\3\2\2\2\u0623\u0617\3\2\2\2")
        buf.write("\u0623\u0624\3\2\2\2\u0624\u0625\3\2\2\2\u0625\u0626\5")
        buf.write("\u00b6\\\2\u0626\u0628\7s\2\2\u0627\u0629\7 \2\2\u0628")
        buf.write("\u0627\3\2\2\2\u0628\u0629\3\2\2\2\u0629\u00a5\3\2\2\2")
        buf.write("\u062a\u0632\7c\2\2\u062b\u062c\5\u00a8U\2\u062c\u062d")
        buf.write("\7!\2\2\u062d\u0633\3\2\2\2\u062e\u062f\7\b\2\2\u062f")
        buf.write("\u0630\5\\/\2\u0630\u0631\7!\2\2\u0631\u0633\3\2\2\2\u0632")
        buf.write("\u062b\3\2\2\2\u0632\u062e\3\2\2\2\u0633\u0638\3\2\2\2")
        buf.write("\u0634\u0635\7\u009b\2\2\u0635\u0636\7\b\2\2\u0636\u0637")
        buf.write("\7\u00fb\2\2\u0637\u0639\7!\2\2\u0638\u0634\3\2\2\2\u0638")
        buf.write("\u0639\3\2\2\2\u0639\u00a7\3\2\2\2\u063a\u063b\7\u0096")
        buf.write("\2\2\u063b\u063c\7\b\2\2\u063c\u063d\5\u0126\u0094\2\u063d")
        buf.write("\u00a9\3\2\2\2\u063e\u063f\5\u00acW\2\u063f\u00ab\3\2")
        buf.write("\2\2\u0640\u0641\7?\2\2\u0641\u0642\7>\2\2\u0642\u0643")
        buf.write("\7\b\2\2\u0643\u0644\7\u00ec\2\2\u0644\u0645\7\30\2\2")
        buf.write("\u0645\u0646\7\u00fb\2\2\u0646\u0647\7\31\2\2\u0647\u0648")
        buf.write("\7!\2\2\u0648\u0649\7\u0096\2\2\u0649\u064a\7\b\2\2\u064a")
        buf.write("\u064b\5\\/\2\u064b\u064c\7!\2\2\u064c\u064d\7@\2\2\u064d")
        buf.write("\u064e\7\b\2\2\u064e\u0656\5\u00aeX\2\u064f\u0650\7!\2")
        buf.write("\2\u0650\u0651\7t\2\2\u0651\u0654\7\b\2\2\u0652\u0655")
        buf.write("\7\u00fa\2\2\u0653\u0655\7\u00fb\2\2\u0654\u0652\3\2\2")
        buf.write("\2\u0654\u0653\3\2\2\2\u0655\u0657\3\2\2\2\u0656\u064f")
        buf.write("\3\2\2\2\u0656\u0657\3\2\2\2\u0657\u065c\3\2\2\2\u0658")
        buf.write("\u0659\7!\2\2\u0659\u065b\5^\60\2\u065a\u0658\3\2\2\2")
        buf.write("\u065b\u065e\3\2\2\2\u065c\u065a\3\2\2\2\u065c\u065d\3")
        buf.write("\2\2\2\u065d\u065f\3\2\2\2\u065e\u065c\3\2\2\2\u065f\u0660")
        buf.write("\7 \2\2\u0660\u00ad\3\2\2\2\u0661\u0666\5\u00b0Y\2\u0662")
        buf.write("\u0663\7(\2\2\u0663\u0665\5\u00b0Y\2\u0664\u0662\3\2\2")
        buf.write("\2\u0665\u0668\3\2\2\2\u0666\u0664\3\2\2\2\u0666\u0667")
        buf.write("\3\2\2\2\u0667\u00af\3\2\2\2\u0668\u0666\3\2\2\2\u0669")
        buf.write("\u0676\7\u00fa\2\2\u066a\u0676\7\u00ed\2\2\u066b\u0676")
        buf.write("\7\u00ee\2\2\u066c\u0676\7y\2\2\u066d\u0676\7{\2\2\u066e")
        buf.write("\u0676\7\u0080\2\2\u066f\u0676\7|\2\2\u0670\u0676\7v\2")
        buf.write("\2\u0671\u0676\7u\2\2\u0672\u0676\7z\2\2\u0673\u0676\7")
        buf.write("}\2\2\u0674\u0676\7\u00fb\2\2\u0675\u0669\3\2\2\2\u0675")
        buf.write("\u066a\3\2\2\2\u0675\u066b\3\2\2\2\u0675\u066c\3\2\2\2")
        buf.write("\u0675\u066d\3\2\2\2\u0675\u066e\3\2\2\2\u0675\u066f\3")
        buf.write("\2\2\2\u0675\u0670\3\2\2\2\u0675\u0671\3\2\2\2\u0675\u0672")
        buf.write("\3\2\2\2\u0675\u0673\3\2\2\2\u0675\u0674\3\2\2\2\u0676")
        buf.write("\u00b1\3\2\2\2\u0677\u0678\7\u0097\2\2\u0678\u0679\5\u0126")
        buf.write("\u0094\2\u0679\u067a\7 \2\2\u067a\u00b3\3\2\2\2\u067b")
        buf.write("\u067c\7\u0098\2\2\u067c\u067d\5\u0126\u0094\2\u067d\u067e")
        buf.write("\7 \2\2\u067e\u00b5\3\2\2\2\u067f\u0681\5\u00b8]\2\u0680")
        buf.write("\u067f\3\2\2\2\u0681\u0684\3\2\2\2\u0682\u0680\3\2\2\2")
        buf.write("\u0682\u0683\3\2\2\2\u0683\u00b7\3\2\2\2\u0684\u0682\3")
        buf.write("\2\2\2\u0685\u0688\5\u008cG\2\u0686\u0688\5\u009eP\2\u0687")
        buf.write("\u0685\3\2\2\2\u0687\u0686\3\2\2\2\u0688\u00b9\3\2\2\2")
        buf.write("\u0689\u068c\5\u00bc_\2\u068a\u068c\5\u00c2b\2\u068b\u0689")
        buf.write("\3\2\2\2\u068b\u068a\3\2\2\2\u068c\u00bb\3\2\2\2\u068d")
        buf.write("\u068e\7\\\2\2\u068e\u068f\5T+\2\u068f\u0690\5V,\2\u0690")
        buf.write("\u0696\7!\2\2\u0691\u0692\7@\2\2\u0692\u0693\7\b\2\2\u0693")
        buf.write("\u0694\5\u00be`\2\u0694\u0695\7!\2\2\u0695\u0697\3\2\2")
        buf.write("\2\u0696\u0691\3\2\2\2\u0696\u0697\3\2\2\2\u0697\u069f")
        buf.write("\3\2\2\2\u0698\u0699\7t\2\2\u0699\u069c\7\b\2\2\u069a")
        buf.write("\u069d\7\u00fa\2\2\u069b\u069d\7\u00fb\2\2\u069c\u069a")
        buf.write("\3\2\2\2\u069c\u069b\3\2\2\2\u069d\u069e\3\2\2\2\u069e")
        buf.write("\u06a0\7!\2\2\u069f\u0698\3\2\2\2\u069f\u06a0\3\2\2\2")
        buf.write("\u06a0\u06a1\3\2\2\2\u06a1\u06a2\5\u00b6\\\2\u06a2\u06a3")
        buf.write("\7]\2\2\u06a3\u06a4\7 \2\2\u06a4\u00bd\3\2\2\2\u06a5\u06aa")
        buf.write("\5\u00c0a\2\u06a6\u06a7\7(\2\2\u06a7\u06a9\5\u00c0a\2")
        buf.write("\u06a8\u06a6\3\2\2\2\u06a9\u06ac\3\2\2\2\u06aa\u06a8\3")
        buf.write("\2\2\2\u06aa\u06ab\3\2\2\2\u06ab\u00bf\3\2\2\2\u06ac\u06aa")
        buf.write("\3\2\2\2\u06ad\u06b5\7\u00fa\2\2\u06ae\u06b5\7u\2\2\u06af")
        buf.write("\u06b5\7v\2\2\u06b0\u06b5\7w\2\2\u06b1\u06b5\7x\2\2\u06b2")
        buf.write("\u06b5\5X-\2\u06b3\u06b5\7\u00fb\2\2\u06b4\u06ad\3\2\2")
        buf.write("\2\u06b4\u06ae\3\2\2\2\u06b4\u06af\3\2\2\2\u06b4\u06b0")
        buf.write("\3\2\2\2\u06b4\u06b1\3\2\2\2\u06b4\u06b2\3\2\2\2\u06b4")
        buf.write("\u06b3\3\2\2\2\u06b5\u00c1\3\2\2\2\u06b6\u06b7\7\u00a1")
        buf.write("\2\2\u06b7\u06b8\5R*\2\u06b8\u06be\7!\2\2\u06b9\u06ba")
        buf.write("\7@\2\2\u06ba\u06bb\7\b\2\2\u06bb\u06bc\5\u00c4c\2\u06bc")
        buf.write("\u06bd\7!\2\2\u06bd\u06bf\3\2\2\2\u06be\u06b9\3\2\2\2")
        buf.write("\u06be\u06bf\3\2\2\2\u06bf\u06c0\3\2\2\2\u06c0\u06c1\7")
        buf.write("\u00a2\2\2\u06c1\u06c2\7\b\2\2\u06c2\u06c3\7\u00ec\2\2")
        buf.write("\u06c3\u06c4\7\30\2\2\u06c4\u06c5\7\u00fb\2\2\u06c5\u06c6")
        buf.write("\7\31\2\2\u06c6\u06c7\7!\2\2\u06c7\u06c8\5\u009cO\2\u06c8")
        buf.write("\u06c9\7\u00a3\2\2\u06c9\u06ca\7 \2\2\u06ca\u00c3\3\2")
        buf.write("\2\2\u06cb\u06d0\5\u00c6d\2\u06cc\u06cd\7(\2\2\u06cd\u06cf")
        buf.write("\5\u00c6d\2\u06ce\u06cc\3\2\2\2\u06cf\u06d2\3\2\2\2\u06d0")
        buf.write("\u06ce\3\2\2\2\u06d0\u06d1\3\2\2\2\u06d1\u00c5\3\2\2\2")
        buf.write("\u06d2\u06d0\3\2\2\2\u06d3\u06d7\7\u00fa\2\2\u06d4\u06d7")
        buf.write("\5X-\2\u06d5\u06d7\7\u00fb\2\2\u06d6\u06d3\3\2\2\2\u06d6")
        buf.write("\u06d4\3\2\2\2\u06d6\u06d5\3\2\2\2\u06d7\u00c7\3\2\2\2")
        buf.write("\u06d8\u06db\5\u00caf\2\u06d9\u06db\5\u00d2j\2\u06da\u06d8")
        buf.write("\3\2\2\2\u06da\u06d9\3\2\2\2\u06db\u00c9\3\2\2\2\u06dc")
        buf.write("\u06dd\7^\2\2\u06dd\u06de\5T+\2\u06de\u06df\5V,\2\u06df")
        buf.write("\u06e5\7!\2\2\u06e0\u06e1\7@\2\2\u06e1\u06e2\7\b\2\2\u06e2")
        buf.write("\u06e3\5\u00ceh\2\u06e3\u06e4\7!\2\2\u06e4\u06e6\3\2\2")
        buf.write("\2\u06e5\u06e0\3\2\2\2\u06e5\u06e6\3\2\2\2\u06e6\u06ee")
        buf.write("\3\2\2\2\u06e7\u06e8\7t\2\2\u06e8\u06eb\7\b\2\2\u06e9")
        buf.write("\u06ec\7\u00fa\2\2\u06ea\u06ec\7\u00fb\2\2\u06eb\u06e9")
        buf.write("\3\2\2\2\u06eb\u06ea\3\2\2\2\u06ec\u06ed\3\2\2\2\u06ed")
        buf.write("\u06ef\7!\2\2\u06ee\u06e7\3\2\2\2\u06ee\u06ef\3\2\2\2")
        buf.write("\u06ef\u06f0\3\2\2\2\u06f0\u06f1\5\u00ccg\2\u06f1\u06f2")
        buf.write("\5\u00b6\\\2\u06f2\u06f3\7_\2\2\u06f3\u06f4\7 \2\2\u06f4")
        buf.write("\u00cb\3\2\2\2\u06f5\u06f6\7`\2\2\u06f6\u06fc\7\b\2\2")
        buf.write("\u06f7\u06f9\7\35\2\2\u06f8\u06f7\3\2\2\2\u06f8\u06f9")
        buf.write("\3\2\2\2\u06f9\u06fa\3\2\2\2\u06fa\u06fd\7\u00fa\2\2\u06fb")
        buf.write("\u06fd\7\u00fb\2\2\u06fc\u06f8\3\2\2\2\u06fc\u06fb\3\2")
        buf.write("\2\2\u06fd\u06fe\3\2\2\2\u06fe\u06ff\7!\2\2\u06ff\u0700")
        buf.write("\7a\2\2\u0700\u0706\7\b\2\2\u0701\u0703\7\35\2\2\u0702")
        buf.write("\u0701\3\2\2\2\u0702\u0703\3\2\2\2\u0703\u0704\3\2\2\2")
        buf.write("\u0704\u0707\7\u00fa\2\2\u0705\u0707\7\u00fb\2\2\u0706")
        buf.write("\u0702\3\2\2\2\u0706\u0705\3\2\2\2\u0707\u0708\3\2\2\2")
        buf.write("\u0708\u0710\7!\2\2\u0709\u070a\7b\2\2\u070a\u070d\7\b")
        buf.write("\2\2\u070b\u070e\7\u00fa\2\2\u070c\u070e\7\u00fb\2\2\u070d")
        buf.write("\u070b\3\2\2\2\u070d\u070c\3\2\2\2\u070e\u070f\3\2\2\2")
        buf.write("\u070f\u0711\7!\2\2\u0710\u0709\3\2\2\2\u0710\u0711\3")
        buf.write("\2\2\2\u0711\u00cd\3\2\2\2\u0712\u0717\5\u00d0i\2\u0713")
        buf.write("\u0714\7(\2\2\u0714\u0716\5\u00d0i\2\u0715\u0713\3\2\2")
        buf.write("\2\u0716\u0719\3\2\2\2\u0717\u0715\3\2\2\2\u0717\u0718")
        buf.write("\3\2\2\2\u0718\u00cf\3\2\2\2\u0719\u0717\3\2\2\2\u071a")
        buf.write("\u0725\7\u00fa\2\2\u071b\u0725\7\u00ef\2\2\u071c\u0725")
        buf.write("\7\u00f0\2\2\u071d\u0725\7\u00f1\2\2\u071e\u0725\7\u00f2")
        buf.write("\2\2\u071f\u0725\7\u00f3\2\2\u0720\u0725\7\u00f4\2\2\u0721")
        buf.write("\u0725\7\u00f5\2\2\u0722\u0725\5X-\2\u0723\u0725\7\u00fb")
        buf.write("\2\2\u0724\u071a\3\2\2\2\u0724\u071b\3\2\2\2\u0724\u071c")
        buf.write("\3\2\2\2\u0724\u071d\3\2\2\2\u0724\u071e\3\2\2\2\u0724")
        buf.write("\u071f\3\2\2\2\u0724\u0720\3\2\2\2\u0724\u0721\3\2\2\2")
        buf.write("\u0724\u0722\3\2\2\2\u0724\u0723\3\2\2\2\u0725\u00d1\3")
        buf.write("\2\2\2\u0726\u0727\7\60\2\2\u0727\u0728\5T+\2\u0728\u0729")
        buf.write("\5V,\2\u0729\u072f\7!\2\2\u072a\u072b\7@\2\2\u072b\u072c")
        buf.write("\7\b\2\2\u072c\u072d\5\u00d4k\2\u072d\u072e\7!\2\2\u072e")
        buf.write("\u0730\3\2\2\2\u072f\u072a\3\2\2\2\u072f\u0730\3\2\2\2")
        buf.write("\u0730\u0732\3\2\2\2\u0731\u0733\5\u00ccg\2\u0732\u0731")
        buf.write("\3\2\2\2\u0732\u0733\3\2\2\2\u0733\u0734\3\2\2\2\u0734")
        buf.write("\u0735\5\u00b6\\\2\u0735\u0736\7\61\2\2\u0736\u0737\7")
        buf.write(" \2\2\u0737\u00d3\3\2\2\2\u0738\u073d\5\u00d0i\2\u0739")
        buf.write("\u073a\7(\2\2\u073a\u073c\5\u00d0i\2\u073b\u0739\3\2\2")
        buf.write("\2\u073c\u073f\3\2\2\2\u073d\u073b\3\2\2\2\u073d\u073e")
        buf.write("\3\2\2\2\u073e\u00d5\3\2\2\2\u073f\u073d\3\2\2\2\u0740")
        buf.write("\u0743\5\u00d8m\2\u0741\u0743\5\u00dep\2\u0742\u0740\3")
        buf.write("\2\2\2\u0742\u0741\3\2\2\2\u0743\u00d7\3\2\2\2\u0744\u0745")
        buf.write("\7f\2\2\u0745\u0746\5R*\2\u0746\u074c\7!\2\2\u0747\u0748")
        buf.write("\7@\2\2\u0748\u0749\7\b\2\2\u0749\u074a\5\u00dan\2\u074a")
        buf.write("\u074b\7!\2\2\u074b\u074d\3\2\2\2\u074c\u0747\3\2\2\2")
        buf.write("\u074c\u074d\3\2\2\2\u074d\u0755\3\2\2\2\u074e\u074f\7")
        buf.write("t\2\2\u074f\u0752\7\b\2\2\u0750\u0753\7\u00fa\2\2\u0751")
        buf.write("\u0753\7\u00fb\2\2\u0752\u0750\3\2\2\2\u0752\u0751\3\2")
        buf.write("\2\2\u0753\u0754\3\2\2\2\u0754\u0756\7!\2\2\u0755\u074e")
        buf.write("\3\2\2\2\u0755\u0756\3\2\2\2\u0756\u0757\3\2\2\2\u0757")
        buf.write("\u0758\7h\2\2\u0758\u075b\7\b\2\2\u0759\u075c\7\u00fa")
        buf.write("\2\2\u075a\u075c\7\u00fb\2\2\u075b\u0759\3\2\2\2\u075b")
        buf.write("\u075a\3\2\2\2\u075c\u075d\3\2\2\2\u075d\u075e\7!\2\2")
        buf.write("\u075e\u075f\7i\2\2\u075f\u0762\7\b\2\2\u0760\u0763\7")
        buf.write("\u00fa\2\2\u0761\u0763\7\u00fb\2\2\u0762\u0760\3\2\2\2")
        buf.write("\u0762\u0761\3\2\2\2\u0763\u0764\3\2\2\2\u0764\u0765\7")
        buf.write("!\2\2\u0765\u0766\5\u00b6\\\2\u0766\u0767\7g\2\2\u0767")
        buf.write("\u0768\7 \2\2\u0768\u00d9\3\2\2\2\u0769\u076e\5\u00dc")
        buf.write("o\2\u076a\u076b\7(\2\2\u076b\u076d\5\u00dco\2\u076c\u076a")
        buf.write("\3\2\2\2\u076d\u0770\3\2\2\2\u076e\u076c\3\2\2\2\u076e")
        buf.write("\u076f\3\2\2\2\u076f\u00db\3\2\2\2\u0770\u076e\3\2\2\2")
        buf.write("\u0771\u0776\7\u00fa\2\2\u0772\u0776\7\13\2\2\u0773\u0776")
        buf.write("\5X-\2\u0774\u0776\7\u00fb\2\2\u0775\u0771\3\2\2\2\u0775")
        buf.write("\u0772\3\2\2\2\u0775\u0773\3\2\2\2\u0775\u0774\3\2\2\2")
        buf.write("\u0776\u00dd\3\2\2\2\u0777\u0778\7d\2\2\u0778\u0779\5")
        buf.write("R*\2\u0779\u077f\7!\2\2\u077a\u077b\7@\2\2\u077b\u077c")
        buf.write("\7\b\2\2\u077c\u077d\5\u00e0q\2\u077d\u077e\7!\2\2\u077e")
        buf.write("\u0780\3\2\2\2\u077f\u077a\3\2\2\2\u077f\u0780\3\2\2\2")
        buf.write("\u0780\u0788\3\2\2\2\u0781\u0782\7t\2\2\u0782\u0785\7")
        buf.write("\b\2\2\u0783\u0786\7\u00fa\2\2\u0784\u0786\7\u00fb\2\2")
        buf.write("\u0785\u0783\3\2\2\2\u0785\u0784\3\2\2\2\u0786\u0787\3")
        buf.write("\2\2\2\u0787\u0789\7!\2\2\u0788\u0781\3\2\2\2\u0788\u0789")
        buf.write("\3\2\2\2\u0789\u078a\3\2\2\2\u078a\u078b\7h\2\2\u078b")
        buf.write("\u078e\7\b\2\2\u078c\u078f\7\u00fa\2\2\u078d\u078f\7\u00fb")
        buf.write("\2\2\u078e\u078c\3\2\2\2\u078e\u078d\3\2\2\2\u078f\u0790")
        buf.write("\3\2\2\2\u0790\u0791\7!\2\2\u0791\u0792\7i\2\2\u0792\u0795")
        buf.write("\7\b\2\2\u0793\u0796\7\u00fa\2\2\u0794\u0796\7\u00fb\2")
        buf.write("\2\u0795\u0793\3\2\2\2\u0795\u0794\3\2\2\2\u0796\u0797")
        buf.write("\3\2\2\2\u0797\u079f\7!\2\2\u0798\u0799\7j\2\2\u0799\u079c")
        buf.write("\7\b\2\2\u079a\u079d\7\u00fa\2\2\u079b\u079d\7\u00fb\2")
        buf.write("\2\u079c\u079a\3\2\2\2\u079c\u079b\3\2\2\2\u079d\u079e")
        buf.write("\3\2\2\2\u079e\u07a0\7!\2\2\u079f\u0798\3\2\2\2\u079f")
        buf.write("\u07a0\3\2\2\2\u07a0\u07a1\3\2\2\2\u07a1\u07a2\5\u00b6")
        buf.write("\\\2\u07a2\u07a3\7e\2\2\u07a3\u07a4\7 \2\2\u07a4\u00df")
        buf.write("\3\2\2\2\u07a5\u07aa\5\u00e2r\2\u07a6\u07a7\7(\2\2\u07a7")
        buf.write("\u07a9\5\u00e2r\2\u07a8\u07a6\3\2\2\2\u07a9\u07ac\3\2")
        buf.write("\2\2\u07aa\u07a8\3\2\2\2\u07aa\u07ab\3\2\2\2\u07ab\u00e1")
        buf.write("\3\2\2\2\u07ac\u07aa\3\2\2\2\u07ad\u07b1\7\u00fa\2\2\u07ae")
        buf.write("\u07b1\5X-\2\u07af\u07b1\7\u00fb\2\2\u07b0\u07ad\3\2\2")
        buf.write("\2\u07b0\u07ae\3\2\2\2\u07b0\u07af\3\2\2\2\u07b1\u00e3")
        buf.write("\3\2\2\2\u07b2\u07b3\7\63\2\2\u07b3\u07b4\5R*\2\u07b4")
        buf.write("\u07bc\7!\2\2\u07b5\u07b6\7\64\2\2\u07b6\u07b9\7\b\2\2")
        buf.write("\u07b7\u07ba\7\u00fa\2\2\u07b8\u07ba\7\u00fb\2\2\u07b9")
        buf.write("\u07b7\3\2\2\2\u07b9\u07b8\3\2\2\2\u07ba\u07bb\3\2\2\2")
        buf.write("\u07bb\u07bd\7!\2\2\u07bc\u07b5\3\2\2\2\u07bc\u07bd\3")
        buf.write("\2\2\2\u07bd\u07c3\3\2\2\2\u07be\u07bf\7@\2\2\u07bf\u07c0")
        buf.write("\7\b\2\2\u07c0\u07c1\5\u00e6t\2\u07c1\u07c2\7!\2\2\u07c2")
        buf.write("\u07c4\3\2\2\2\u07c3\u07be\3\2\2\2\u07c3\u07c4\3\2\2\2")
        buf.write("\u07c4\u07c5\3\2\2\2\u07c5\u07c6\5\u00b6\\\2\u07c6\u07c7")
        buf.write("\7\65\2\2\u07c7\u07c8\7 \2\2\u07c8\u00e5\3\2\2\2\u07c9")
        buf.write("\u07ce\5\u00e8u\2\u07ca\u07cb\7(\2\2\u07cb\u07cd\5\u00e8")
        buf.write("u\2\u07cc\u07ca\3\2\2\2\u07cd\u07d0\3\2\2\2\u07ce\u07cc")
        buf.write("\3\2\2\2\u07ce\u07cf\3\2\2\2\u07cf\u00e7\3\2\2\2\u07d0")
        buf.write("\u07ce\3\2\2\2\u07d1\u07d7\7\u00fa\2\2\u07d2\u07d7\7\u00c0")
        buf.write("\2\2\u07d3\u07d7\7\u00c1\2\2\u07d4\u07d7\5X-\2\u07d5\u07d7")
        buf.write("\7\u00fb\2\2\u07d6\u07d1\3\2\2\2\u07d6\u07d2\3\2\2\2\u07d6")
        buf.write("\u07d3\3\2\2\2\u07d6\u07d4\3\2\2\2\u07d6\u07d5\3\2\2\2")
        buf.write("\u07d7\u00e9\3\2\2\2\u07d8\u0833\7A\2\2\u07d9\u07da\5")
        buf.write("R*\2\u07da\u07e0\7!\2\2\u07db\u07dc\7@\2\2\u07dc\u07dd")
        buf.write("\7\b\2\2\u07dd\u07de\5\u00eex\2\u07de\u07df\7!\2\2\u07df")
        buf.write("\u07e1\3\2\2\2\u07e0\u07db\3\2\2\2\u07e0\u07e1\3\2\2\2")
        buf.write("\u07e1\u07e2\3\2\2\2\u07e2\u07e3\5\u00b6\\\2\u07e3\u0834")
        buf.write("\3\2\2\2\u07e4\u07e5\7C\2\2\u07e5\u07e6\7\u008f\2\2\u07e6")
        buf.write("\u07e7\7\b\2\2\u07e7\u07e8\7\u00fb\2\2\u07e8\u07e9\7\34")
        buf.write("\2\2\u07e9\u07ea\7\u00fb\2\2\u07ea\u07eb\7!\2\2\u07eb")
        buf.write("\u07ec\7\62\2\2\u07ec\u07ed\7\b\2\2\u07ed\u07ee\7\u00ec")
        buf.write("\2\2\u07ee\u07ef\7\30\2\2\u07ef\u07f0\7\u00fb\2\2\u07f0")
        buf.write("\u07f1\7\31\2\2\u07f1\u07f2\7!\2\2\u07f2\u07f3\7=\2\2")
        buf.write("\u07f3\u07f4\7\b\2\2\u07f4\u07f5\7\u00ec\2\2\u07f5\u07f6")
        buf.write("\7\30\2\2\u07f6\u07f7\7\u00fb\2\2\u07f7\u07f8\7\31\2\2")
        buf.write("\u07f8\u07f9\7!\2\2\u07f9\u07fa\5\u00ecw\2\u07fa\u07fb")
        buf.write("\7D\2\2\u07fb\u07fc\7\u008f\2\2\u07fc\u07fd\7\b\2\2\u07fd")
        buf.write("\u07fe\7\u00fb\2\2\u07fe\u07ff\7\34\2\2\u07ff\u0800\7")
        buf.write("\u00fb\2\2\u0800\u0801\7!\2\2\u0801\u0802\7\62\2\2\u0802")
        buf.write("\u0803\7\b\2\2\u0803\u0804\7\u00ec\2\2\u0804\u0805\7\30")
        buf.write("\2\2\u0805\u0806\7\u00fb\2\2\u0806\u0807\7\31\2\2\u0807")
        buf.write("\u0808\7!\2\2\u0808\u0809\7=\2\2\u0809\u080a\7\b\2\2\u080a")
        buf.write("\u080b\7\u00ec\2\2\u080b\u080c\7\30\2\2\u080c\u080d\7")
        buf.write("\u00fb\2\2\u080d\u080e\7\31\2\2\u080e\u080f\7!\2\2\u080f")
        buf.write("\u0810\5\u00ecw\2\u0810\u0811\7E\2\2\u0811\u0812\7\u008f")
        buf.write("\2\2\u0812\u0813\7\b\2\2\u0813\u0814\7\u00fb\2\2\u0814")
        buf.write("\u0815\7\34\2\2\u0815\u0816\7\u00fb\2\2\u0816\u0817\7")
        buf.write("!\2\2\u0817\u0818\7\62\2\2\u0818\u0819\7\b\2\2\u0819\u081a")
        buf.write("\7\u00ec\2\2\u081a\u081b\7\30\2\2\u081b\u081c\7\u00fb")
        buf.write("\2\2\u081c\u081d\7\31\2\2\u081d\u081e\7!\2\2\u081e\u081f")
        buf.write("\7=\2\2\u081f\u0820\7\b\2\2\u0820\u0821\7\u00ec\2\2\u0821")
        buf.write("\u0822\7\30\2\2\u0822\u0823\7\u00fb\2\2\u0823\u0824\7")
        buf.write("\31\2\2\u0824\u0825\7!\2\2\u0825\u082b\5\u00ecw\2\u0826")
        buf.write("\u0827\7@\2\2\u0827\u0828\7\b\2\2\u0828\u0829\5\u00ee")
        buf.write("x\2\u0829\u082a\7!\2\2\u082a\u082c\3\2\2\2\u082b\u0826")
        buf.write("\3\2\2\2\u082b\u082c\3\2\2\2\u082c\u0830\3\2\2\2\u082d")
        buf.write("\u082f\5\u008eH\2\u082e\u082d\3\2\2\2\u082f\u0832\3\2")
        buf.write("\2\2\u0830\u082e\3\2\2\2\u0830\u0831\3\2\2\2\u0831\u0834")
        buf.write("\3\2\2\2\u0832\u0830\3\2\2\2\u0833\u07d9\3\2\2\2\u0833")
        buf.write("\u07e4\3\2\2\2\u0834\u0835\3\2\2\2\u0835\u0836\7B\2\2")
        buf.write("\u0836\u0837\7 \2\2\u0837\u00eb\3\2\2\2\u0838\u0839\7")
        buf.write("`\2\2\u0839\u083a\7\b\2\2\u083a\u0851\7\u00fa\2\2\u083b")
        buf.write("\u083c\7\u00fb\2\2\u083c\u083d\7!\2\2\u083d\u083e\7a\2")
        buf.write("\2\u083e\u083f\7\b\2\2\u083f\u0851\7\u00fa\2\2\u0840\u0841")
        buf.write("\7\u00fb\2\2\u0841\u0847\7!\2\2\u0842\u0843\7b\2\2\u0843")
        buf.write("\u0844\7\b\2\2\u0844\u0848\7\u00fa\2\2\u0845\u0846\7\u00fb")
        buf.write("\2\2\u0846\u0848\7!\2\2\u0847\u0842\3\2\2\2\u0847\u0845")
        buf.write("\3\2\2\2\u0847\u0848\3\2\2\2\u0848\u084e\3\2\2\2\u0849")
        buf.write("\u084a\7c\2\2\u084a\u084b\7\b\2\2\u084b\u084f\7\u00fa")
        buf.write("\2\2\u084c\u084d\7\u00fb\2\2\u084d\u084f\7!\2\2\u084e")
        buf.write("\u0849\3\2\2\2\u084e\u084c\3\2\2\2\u084e\u084f\3\2\2\2")
        buf.write("\u084f\u0851\3\2\2\2\u0850\u0838\3\2\2\2\u0850\u083b\3")
        buf.write("\2\2\2\u0850\u0840\3\2\2\2\u0851\u00ed\3\2\2\2\u0852\u0857")
        buf.write("\5\u00f0y\2\u0853\u0854\7(\2\2\u0854\u0856\5\u00f0y\2")
        buf.write("\u0855\u0853\3\2\2\2\u0856\u0859\3\2\2\2\u0857\u0855\3")
        buf.write("\2\2\2\u0857\u0858\3\2\2\2\u0858\u00ef\3\2\2\2\u0859\u0857")
        buf.write("\3\2\2\2\u085a\u0863\7\u00fa\2\2\u085b\u0863\7\u00b7\2")
        buf.write("\2\u085c\u0863\7\u00b8\2\2\u085d\u0863\7\u00b9\2\2\u085e")
        buf.write("\u0863\7\u00bd\2\2\u085f\u0863\7\u00be\2\2\u0860\u0863")
        buf.write("\7\u00bf\2\2\u0861\u0863\7\u00fb\2\2\u0862\u085a\3\2\2")
        buf.write("\2\u0862\u085b\3\2\2\2\u0862\u085c\3\2\2\2\u0862\u085d")
        buf.write("\3\2\2\2\u0862\u085e\3\2\2\2\u0862\u085f\3\2\2\2\u0862")
        buf.write("\u0860\3\2\2\2\u0862\u0861\3\2\2\2\u0863\u00f1\3\2\2\2")
        buf.write("\u0864\u08bf\7F\2\2\u0865\u0866\5R*\2\u0866\u086c\7!\2")
        buf.write("\2\u0867\u0868\7@\2\2\u0868\u0869\7\b\2\2\u0869\u086a")
        buf.write("\5\u00f6|\2\u086a\u086b\7!\2\2\u086b\u086d\3\2\2\2\u086c")
        buf.write("\u0867\3\2\2\2\u086c\u086d\3\2\2\2\u086d\u086e\3\2\2\2")
        buf.write("\u086e\u086f\5\u00b6\\\2\u086f\u08c0\3\2\2\2\u0870\u0871")
        buf.write("\7H\2\2\u0871\u0872\7\u008f\2\2\u0872\u0873\7\b\2\2\u0873")
        buf.write("\u0874\7\u00fb\2\2\u0874\u0875\7\34\2\2\u0875\u0876\7")
        buf.write("\u00fb\2\2\u0876\u0877\7!\2\2\u0877\u0878\7\62\2\2\u0878")
        buf.write("\u0879\7\b\2\2\u0879\u087a\7\u00ec\2\2\u087a\u087b\7\30")
        buf.write("\2\2\u087b\u087c\7\u00fb\2\2\u087c\u087d\7\31\2\2\u087d")
        buf.write("\u087e\7!\2\2\u087e\u087f\7=\2\2\u087f\u0880\7\b\2\2\u0880")
        buf.write("\u0881\7\u00ec\2\2\u0881\u0882\7\30\2\2\u0882\u0883\7")
        buf.write("\u00fb\2\2\u0883\u0884\7\31\2\2\u0884\u0885\7!\2\2\u0885")
        buf.write("\u0886\5\u00f4{\2\u0886\u0887\7I\2\2\u0887\u0888\7\u008f")
        buf.write("\2\2\u0888\u0889\7\b\2\2\u0889\u088a\7\u00fb\2\2\u088a")
        buf.write("\u088b\7\34\2\2\u088b\u088c\7\u00fb\2\2\u088c\u088d\7")
        buf.write("!\2\2\u088d\u088e\7\62\2\2\u088e\u088f\7\b\2\2\u088f\u0890")
        buf.write("\7\u00ec\2\2\u0890\u0891\7\30\2\2\u0891\u0892\7\u00fb")
        buf.write("\2\2\u0892\u0893\7\31\2\2\u0893\u0894\7!\2\2\u0894\u0895")
        buf.write("\7=\2\2\u0895\u0896\7\b\2\2\u0896\u0897\7\u00ec\2\2\u0897")
        buf.write("\u0898\7\30\2\2\u0898\u0899\7\u00fb\2\2\u0899\u089a\7")
        buf.write("\31\2\2\u089a\u089b\7!\2\2\u089b\u089c\5\u00f4{\2\u089c")
        buf.write("\u089d\7J\2\2\u089d\u089e\7\u008f\2\2\u089e\u089f\7\b")
        buf.write("\2\2\u089f\u08a0\7\u00fb\2\2\u08a0\u08a1\7\34\2\2\u08a1")
        buf.write("\u08a2\7\u00fb\2\2\u08a2\u08a3\7!\2\2\u08a3\u08a4\7\62")
        buf.write("\2\2\u08a4\u08a5\7\b\2\2\u08a5\u08a6\7\u00ec\2\2\u08a6")
        buf.write("\u08a7\7\30\2\2\u08a7\u08a8\7\u00fb\2\2\u08a8\u08a9\7")
        buf.write("\31\2\2\u08a9\u08aa\7!\2\2\u08aa\u08ab\7=\2\2\u08ab\u08ac")
        buf.write("\7\b\2\2\u08ac\u08ad\7\u00ec\2\2\u08ad\u08ae\7\30\2\2")
        buf.write("\u08ae\u08af\7\u00fb\2\2\u08af\u08b0\7\31\2\2\u08b0\u08b1")
        buf.write("\7!\2\2\u08b1\u08b7\5\u00f4{\2\u08b2\u08b3\7@\2\2\u08b3")
        buf.write("\u08b4\7\b\2\2\u08b4\u08b5\5\u00f6|\2\u08b5\u08b6\7!\2")
        buf.write("\2\u08b6\u08b8\3\2\2\2\u08b7\u08b2\3\2\2\2\u08b7\u08b8")
        buf.write("\3\2\2\2\u08b8\u08bc\3\2\2\2\u08b9\u08bb\5\u008eH\2\u08ba")
        buf.write("\u08b9\3\2\2\2\u08bb\u08be\3\2\2\2\u08bc\u08ba\3\2\2\2")
        buf.write("\u08bc\u08bd\3\2\2\2\u08bd\u08c0\3\2\2\2\u08be\u08bc\3")
        buf.write("\2\2\2\u08bf\u0865\3\2\2\2\u08bf\u0870\3\2\2\2\u08c0\u08c1")
        buf.write("\3\2\2\2\u08c1\u08c2\7G\2\2\u08c2\u08c3\7 \2\2\u08c3\u00f3")
        buf.write("\3\2\2\2\u08c4\u08c5\7`\2\2\u08c5\u08c6\7\b\2\2\u08c6")
        buf.write("\u08dd\7\u00fa\2\2\u08c7\u08c8\7\u00fb\2\2\u08c8\u08c9")
        buf.write("\7!\2\2\u08c9\u08ca\7a\2\2\u08ca\u08cb\7\b\2\2\u08cb\u08dd")
        buf.write("\7\u00fa\2\2\u08cc\u08cd\7\u00fb\2\2\u08cd\u08d3\7!\2")
        buf.write("\2\u08ce\u08cf\7b\2\2\u08cf\u08d0\7\b\2\2\u08d0\u08d4")
        buf.write("\7\u00fa\2\2\u08d1\u08d2\7\u00fb\2\2\u08d2\u08d4\7!\2")
        buf.write("\2\u08d3\u08ce\3\2\2\2\u08d3\u08d1\3\2\2\2\u08d3\u08d4")
        buf.write("\3\2\2\2\u08d4\u08da\3\2\2\2\u08d5\u08d6\7c\2\2\u08d6")
        buf.write("\u08d7\7\b\2\2\u08d7\u08db\7\u00fa\2\2\u08d8\u08d9\7\u00fb")
        buf.write("\2\2\u08d9\u08db\7!\2\2\u08da\u08d5\3\2\2\2\u08da\u08d8")
        buf.write("\3\2\2\2\u08da\u08db\3\2\2\2\u08db\u08dd\3\2\2\2\u08dc")
        buf.write("\u08c4\3\2\2\2\u08dc\u08c7\3\2\2\2\u08dc\u08cc\3\2\2\2")
        buf.write("\u08dd\u00f5\3\2\2\2\u08de\u08e3\5\u00f8}\2\u08df\u08e0")
        buf.write("\7(\2\2\u08e0\u08e2\5\u00f8}\2\u08e1\u08df\3\2\2\2\u08e2")
        buf.write("\u08e5\3\2\2\2\u08e3\u08e1\3\2\2\2\u08e3\u08e4\3\2\2\2")
        buf.write("\u08e4\u00f7\3\2\2\2\u08e5\u08e3\3\2\2\2\u08e6\u08ef\7")
        buf.write("\u00fa\2\2\u08e7\u08ef\7\u00ba\2\2\u08e8\u08ef\7\u00bb")
        buf.write("\2\2\u08e9\u08ef\7\u00bc\2\2\u08ea\u08ef\7\u00bd\2\2\u08eb")
        buf.write("\u08ef\7\u00be\2\2\u08ec\u08ef\7\u00bf\2\2\u08ed\u08ef")
        buf.write("\7\u00fb\2\2\u08ee\u08e6\3\2\2\2\u08ee\u08e7\3\2\2\2\u08ee")
        buf.write("\u08e8\3\2\2\2\u08ee\u08e9\3\2\2\2\u08ee\u08ea\3\2\2\2")
        buf.write("\u08ee\u08eb\3\2\2\2\u08ee\u08ec\3\2\2\2\u08ee\u08ed\3")
        buf.write("\2\2\2\u08ef\u00f9\3\2\2\2\u08f0\u08f5\5\u0106\u0084\2")
        buf.write("\u08f1\u08f5\5\u00fe\u0080\2\u08f2\u08f5\5\u0100\u0081")
        buf.write("\2\u08f3\u08f5\5\u0110\u0089\2\u08f4\u08f0\3\2\2\2\u08f4")
        buf.write("\u08f1\3\2\2\2\u08f4\u08f2\3\2\2\2\u08f4\u08f3\3\2\2\2")
        buf.write("\u08f5\u00fb\3\2\2\2\u08f6\u08f7\5\u0106\u0084\2\u08f7")
        buf.write("\u08f8\5\u010c\u0087\2\u08f8\u08f9\5\u010e\u0088\2\u08f9")
        buf.write("\u08fa\5\u0110\u0089\2\u08fa\u00fd\3\2\2\2\u08fb\u08fc")
        buf.write("\5\u010c\u0087\2\u08fc\u00ff\3\2\2\2\u08fd\u08fe\5\u010e")
        buf.write("\u0088\2\u08fe\u0101\3\2\2\2\u08ff\u0906\5r:\2\u0900\u0906")
        buf.write("\5\u008aF\2\u0901\u0906\5\u00fa~\2\u0902\u0906\5\u011a")
        buf.write("\u008e\2\u0903\u0906\5\u011e\u0090\2\u0904\u0906\5\u0112")
        buf.write("\u008a\2\u0905\u08ff\3\2\2\2\u0905\u0900\3\2\2\2\u0905")
        buf.write("\u0901\3\2\2\2\u0905\u0902\3\2\2\2\u0905\u0903\3\2\2\2")
        buf.write("\u0905\u0904\3\2\2\2\u0906\u0103\3\2\2\2\u0907\u090c\5")
        buf.write("r:\2\u0908\u090c\5\u008aF\2\u0909\u090c\5\u011a\u008e")
        buf.write("\2\u090a\u090c\5\u0112\u008a\2\u090b\u0907\3\2\2\2\u090b")
        buf.write("\u0908\3\2\2\2\u090b\u0909\3\2\2\2\u090b\u090a\3\2\2\2")
        buf.write("\u090c\u0105\3\2\2\2\u090d\u090e\7l\2\2\u090e\u090f\5")
        buf.write("\u0126\u0094\2\u090f\u0913\7 \2\2\u0910\u0912\5\u0102")
        buf.write("\u0082\2\u0911\u0910\3\2\2\2\u0912\u0915\3\2\2\2\u0913")
        buf.write("\u0911\3\2\2\2\u0913\u0914\3\2\2\2\u0914\u0916\3\2\2\2")
        buf.write("\u0915\u0913\3\2\2\2\u0916\u0917\7s\2\2\u0917\u0918\7")
        buf.write(" \2\2\u0918\u0107\3\2\2\2\u0919\u0926\7k\2\2\u091a\u091b")
        buf.write("\7@\2\2\u091b\u091c\7\b\2\2\u091c\u0921\5\u00a0Q\2\u091d")
        buf.write("\u091e\7(\2\2\u091e\u0920\5\u00a0Q\2\u091f\u091d\3\2\2")
        buf.write("\2\u0920\u0923\3\2\2\2\u0921\u091f\3\2\2\2\u0921\u0922")
        buf.write("\3\2\2\2\u0922\u0924\3\2\2\2\u0923\u0921\3\2\2\2\u0924")
        buf.write("\u0925\7!\2\2\u0925\u0927\3\2\2\2\u0926\u091a\3\2\2\2")
        buf.write("\u0926\u0927\3\2\2\2\u0927\u0928\3\2\2\2\u0928\u0929\5")
        buf.write("\u0126\u0094\2\u0929\u092a\7 \2\2\u092a\u0109\3\2\2\2")
        buf.write("\u092b\u0938\7K\2\2\u092c\u092d\7@\2\2\u092d\u092e\7\b")
        buf.write("\2\2\u092e\u0933\5\u00a0Q\2\u092f\u0930\7(\2\2\u0930\u0932")
        buf.write("\5\u00a0Q\2\u0931\u092f\3\2\2\2\u0932\u0935\3\2\2\2\u0933")
        buf.write("\u0931\3\2\2\2\u0933\u0934\3\2\2\2\u0934\u0936\3\2\2\2")
        buf.write("\u0935\u0933\3\2\2\2\u0936\u0937\7!\2\2\u0937\u0939\3")
        buf.write("\2\2\2\u0938\u092c\3\2\2\2\u0938\u0939\3\2\2\2\u0939\u093a")
        buf.write("\3\2\2\2\u093a\u093b\5\u0126\u0094\2\u093b\u093c\7 \2")
        buf.write("\2\u093c\u010b\3\2\2\2\u093d\u094a\7k\2\2\u093e\u093f")
        buf.write("\7@\2\2\u093f\u0940\7\b\2\2\u0940\u0945\5\u00a0Q\2\u0941")
        buf.write("\u0942\7(\2\2\u0942\u0944\5\u00a0Q\2\u0943\u0941\3\2\2")
        buf.write("\2\u0944\u0947\3\2\2\2\u0945\u0943\3\2\2\2\u0945\u0946")
        buf.write("\3\2\2\2\u0946\u0948\3\2\2\2\u0947\u0945\3\2\2\2\u0948")
        buf.write("\u0949\7!\2\2\u0949\u094b\3\2\2\2\u094a\u093e\3\2\2\2")
        buf.write("\u094a\u094b\3\2\2\2\u094b\u094c\3\2\2\2\u094c\u094d\5")
        buf.write("\u0126\u0094\2\u094d\u0951\7 \2\2\u094e\u0950\5\u0102")
        buf.write("\u0082\2\u094f\u094e\3\2\2\2\u0950\u0953\3\2\2\2\u0951")
        buf.write("\u094f\3\2\2\2\u0951\u0952\3\2\2\2\u0952\u0954\3\2\2\2")
        buf.write("\u0953\u0951\3\2\2\2\u0954\u0955\7s\2\2\u0955\u0956\7")
        buf.write(" \2\2\u0956\u010d\3\2\2\2\u0957\u0964\7K\2\2\u0958\u0959")
        buf.write("\7@\2\2\u0959\u095a\7\b\2\2\u095a\u095f\5\u00a0Q\2\u095b")
        buf.write("\u095c\7(\2\2\u095c\u095e\5\u00a0Q\2\u095d\u095b\3\2\2")
        buf.write("\2\u095e\u0961\3\2\2\2\u095f\u095d\3\2\2\2\u095f\u0960")
        buf.write("\3\2\2\2\u0960\u0962\3\2\2\2\u0961\u095f\3\2\2\2\u0962")
        buf.write("\u0963\7!\2\2\u0963\u0965\3\2\2\2\u0964\u0958\3\2\2\2")
        buf.write("\u0964\u0965\3\2\2\2\u0965\u0966\3\2\2\2\u0966\u0967\5")
        buf.write("\u0126\u0094\2\u0967\u096b\7 \2\2\u0968\u096a\5\u0102")
        buf.write("\u0082\2\u0969\u0968\3\2\2\2\u096a\u096d\3\2\2\2\u096b")
        buf.write("\u0969\3\2\2\2\u096b\u096c\3\2\2\2\u096c\u096e\3\2\2\2")
        buf.write("\u096d\u096b\3\2\2\2\u096e\u096f\7s\2\2\u096f\u0970\7")
        buf.write(" \2\2\u0970\u010f\3\2\2\2\u0971\u0972\7p\2\2\u0972\u0973")
        buf.write("\7\62\2\2\u0973\u0974\7\b\2\2\u0974\u0975\7\u00ec\2\2")
        buf.write("\u0975\u0976\7\30\2\2\u0976\u0977\7\u00fb\2\2\u0977\u0978")
        buf.write("\7\31\2\2\u0978\u0985\7!\2\2\u0979\u097a\7@\2\2\u097a")
        buf.write("\u097b\7\b\2\2\u097b\u0980\5\u00a0Q\2\u097c\u097d\7(\2")
        buf.write("\2\u097d\u097f\5\u00a0Q\2\u097e\u097c\3\2\2\2\u097f\u0982")
        buf.write("\3\2\2\2\u0980\u097e\3\2\2\2\u0980\u0981\3\2\2\2\u0981")
        buf.write("\u0983\3\2\2\2\u0982\u0980\3\2\2\2\u0983\u0984\7!\2\2")
        buf.write("\u0984\u0986\3\2\2\2\u0985\u0979\3\2\2\2\u0985\u0986\3")
        buf.write("\2\2\2\u0986\u0987\3\2\2\2\u0987\u0988\5\u0126\u0094\2")
        buf.write("\u0988\u0989\7s\2\2\u0989\u098a\7 \2\2\u098a\u0111\3\2")
        buf.write("\2\2\u098b\u098f\5\u0114\u008b\2\u098c\u098f\5\u0116\u008c")
        buf.write("\2\u098d\u098f\5\u0118\u008d\2\u098e\u098b\3\2\2\2\u098e")
        buf.write("\u098c\3\2\2\2\u098e\u098d\3\2\2\2\u098f\u0113\3\2\2\2")
        buf.write("\u0990\u0991\7m\2\2\u0991\u0992\7\u0096\2\2\u0992\u0995")
        buf.write("\7\b\2\2\u0993\u0996\7\u00fa\2\2\u0994\u0996\7\u00fb\2")
        buf.write("\2\u0995\u0993\3\2\2\2\u0995\u0994\3\2\2\2\u0996\u0997")
        buf.write("\3\2\2\2\u0997\u0998\7!\2\2\u0998\u0999\7t\2\2\u0999\u099c")
        buf.write("\7\b\2\2\u099a\u099d\7\u00fa\2\2\u099b\u099d\7\u00fb\2")
        buf.write("\2\u099c\u099a\3\2\2\2\u099c\u099b\3\2\2\2\u099d\u099e")
        buf.write("\3\2\2\2\u099e\u099f\7 \2\2\u099f\u0115\3\2\2\2\u09a0")
        buf.write("\u09a1\7N\2\2\u09a1\u09a2\7=\2\2\u09a2\u09a3\7\b\2\2\u09a3")
        buf.write("\u09a4\7\u00ec\2\2\u09a4\u09a5\7\30\2\2\u09a5\u09a6\7")
        buf.write("\u00fb\2\2\u09a6\u09a7\7\31\2\2\u09a7\u09a8\7!\2\2\u09a8")
        buf.write("\u09a9\7>\2\2\u09a9\u09aa\7\b\2\2\u09aa\u09ab\7\u00ec")
        buf.write("\2\2\u09ab\u09ac\7\30\2\2\u09ac\u09ad\7\u00fb\2\2\u09ad")
        buf.write("\u09ae\7\31\2\2\u09ae\u09b5\7!\2\2\u09af\u09b0\7>\2\2")
        buf.write("\u09b0\u09b1\7\b\2\2\u09b1\u09b2\7\u00ec\2\2\u09b2\u09b3")
        buf.write("\7\30\2\2\u09b3\u09b4\7\u00fb\2\2\u09b4\u09b6\7\31\2\2")
        buf.write("\u09b5\u09af\3\2\2\2\u09b5\u09b6\3\2\2\2\u09b6\u09b7\3")
        buf.write("\2\2\2\u09b7\u09b8\7 \2\2\u09b8\u0117\3\2\2\2\u09b9\u09ba")
        buf.write("\t\3\2\2\u09ba\u09bb\7\u0087\2\2\u09bb\u09bc\7!\2\2\u09bc")
        buf.write("\u09bd\7/\2\2\u09bd\u09c0\7\b\2\2\u09be\u09c1\7\u00fa")
        buf.write("\2\2\u09bf\u09c1\7\u00fb\2\2\u09c0\u09be\3\2\2\2\u09c0")
        buf.write("\u09bf\3\2\2\2\u09c1\u09c2\3\2\2\2\u09c2\u09c3\7!\2\2")
        buf.write("\u09c3\u09c4\7\62\2\2\u09c4\u09c5\7\b\2\2\u09c5\u09c6")
        buf.write("\7\u00ec\2\2\u09c6\u09c7\7\30\2\2\u09c7\u09c8\7\u00fb")
        buf.write("\2\2\u09c8\u09c9\7\31\2\2\u09c9\u09ca\7!\2\2\u09ca\u09cb")
        buf.write("\7=\2\2\u09cb\u09cc\7\b\2\2\u09cc\u09cd\7\u00ec\2\2\u09cd")
        buf.write("\u09ce\7\30\2\2\u09ce\u09cf\7\u00fb\2\2\u09cf\u09db\7")
        buf.write("\31\2\2\u09d0\u09d1\7!\2\2\u09d1\u09d2\7@\2\2\u09d2\u09d3")
        buf.write("\7\b\2\2\u09d3\u09d8\5\u00a0Q\2\u09d4\u09d5\7(\2\2\u09d5")
        buf.write("\u09d7\5\u00a0Q\2\u09d6\u09d4\3\2\2\2\u09d7\u09da\3\2")
        buf.write("\2\2\u09d8\u09d6\3\2\2\2\u09d8\u09d9\3\2\2\2\u09d9\u09dc")
        buf.write("\3\2\2\2\u09da\u09d8\3\2\2\2\u09db\u09d0\3\2\2\2\u09db")
        buf.write("\u09dc\3\2\2\2\u09dc\u09e4\3\2\2\2\u09dd\u09de\7!\2\2")
        buf.write("\u09de\u09df\7t\2\2\u09df\u09e2\7\b\2\2\u09e0\u09e3\7")
        buf.write("\u00fa\2\2\u09e1\u09e3\7\u00fb\2\2\u09e2\u09e0\3\2\2\2")
        buf.write("\u09e2\u09e1\3\2\2\2\u09e3\u09e5\3\2\2\2\u09e4\u09dd\3")
        buf.write("\2\2\2\u09e4\u09e5\3\2\2\2\u09e5\u09e6\3\2\2\2\u09e6\u09e7")
        buf.write("\7 \2\2\u09e7\u0119\3\2\2\2\u09e8\u09eb\7L\2\2\u09e9\u09ec")
        buf.write("\7\u00fa\2\2\u09ea\u09ec\7\u00fb\2\2\u09eb\u09e9\3\2\2")
        buf.write("\2\u09eb\u09ea\3\2\2\2\u09ec\u09ed\3\2\2\2\u09ed\u09ee")
        buf.write("\7 \2\2\u09ee\u011b\3\2\2\2\u09ef\u09f1\7\u0088\2\2\u09f0")
        buf.write("\u09f2\7!\2\2\u09f1\u09f0\3\2\2\2\u09f1\u09f2\3\2\2\2")
        buf.write("\u09f2\u09f3\3\2\2\2\u09f3\u09f4\7.\2\2\u09f4\u09f5\7")
        buf.write("\b\2\2\u09f5\u09f6\7\u00ec\2\2\u09f6\u09f7\7\30\2\2\u09f7")
        buf.write("\u09f8\7\u00fb\2\2\u09f8\u09f9\7\31\2\2\u09f9\u0a0a\7")
        buf.write("!\2\2\u09fa\u09fd\7\u008d\2\2\u09fb\u09fe\7\u00fa\2\2")
        buf.write("\u09fc\u09fe\7\u00fb\2\2\u09fd\u09fb\3\2\2\2\u09fd\u09fc")
        buf.write("\3\2\2\2\u09fe\u09ff\3\2\2\2\u09ff\u0a00\7!\2\2\u0a00")
        buf.write("\u0a01\7\u0089\2\2\u0a01\u0a02\t\4\2\2\u0a02\u0a0b\7 ")
        buf.write("\2\2\u0a03\u0a04\7M\2\2\u0a04\u0a07\7\b\2\2\u0a05\u0a08")
        buf.write("\7\u00fa\2\2\u0a06\u0a08\7\u00fb\2\2\u0a07\u0a05\3\2\2")
        buf.write("\2\u0a07\u0a06\3\2\2\2\u0a08\u0a09\3\2\2\2\u0a09\u0a0b")
        buf.write("\7 \2\2\u0a0a\u09fa\3\2\2\2\u0a0a\u0a03\3\2\2\2\u0a0b")
        buf.write("\u011d\3\2\2\2\u0a0c\u0a0d\7\u00a7\2\2\u0a0d\u0a0e\7[")
        buf.write("\2\2\u0a0e\u0a0f\7\b\2\2\u0a0f\u0a57\5\66\34\2\u0a10\u0a11")
        buf.write("\7!\2\2\u0a11\u0a12\7\u00a9\2\2\u0a12\u0a4f\7\b\2\2\u0a13")
        buf.write("\u0a17\7S\2\2\u0a14\u0a15\7\32\2\2\u0a15\u0a16\7\u00fa")
        buf.write("\2\2\u0a16\u0a18\7\33\2\2\u0a17\u0a14\3\2\2\2\u0a17\u0a18")
        buf.write("\3\2\2\2\u0a18\u0a50\3\2\2\2\u0a19\u0a1d\7T\2\2\u0a1a")
        buf.write("\u0a1b\7\32\2\2\u0a1b\u0a1c\7\u00fa\2\2\u0a1c\u0a1e\7")
        buf.write("\33\2\2\u0a1d\u0a1a\3\2\2\2\u0a1d\u0a1e\3\2\2\2\u0a1e")
        buf.write("\u0a50\3\2\2\2\u0a1f\u0a23\7U\2\2\u0a20\u0a21\7\32\2\2")
        buf.write("\u0a21\u0a22\7\u00fa\2\2\u0a22\u0a24\7\33\2\2\u0a23\u0a20")
        buf.write("\3\2\2\2\u0a23\u0a24\3\2\2\2\u0a24\u0a50\3\2\2\2\u0a25")
        buf.write("\u0a29\7V\2\2\u0a26\u0a27\7\32\2\2\u0a27\u0a28\7\u00fa")
        buf.write("\2\2\u0a28\u0a2a\7\33\2\2\u0a29\u0a26\3\2\2\2\u0a29\u0a2a")
        buf.write("\3\2\2\2\u0a2a\u0a50\3\2\2\2\u0a2b\u0a2f\7R\2\2\u0a2c")
        buf.write("\u0a2d\7\32\2\2\u0a2d\u0a2e\7\u00fa\2\2\u0a2e\u0a30\7")
        buf.write("\33\2\2\u0a2f\u0a2c\3\2\2\2\u0a2f\u0a30\3\2\2\2\u0a30")
        buf.write("\u0a50\3\2\2\2\u0a31\u0a35\7W\2\2\u0a32\u0a33\7\32\2\2")
        buf.write("\u0a33\u0a34\7\u00fa\2\2\u0a34\u0a36\7\33\2\2\u0a35\u0a32")
        buf.write("\3\2\2\2\u0a35\u0a36\3\2\2\2\u0a36\u0a50\3\2\2\2\u0a37")
        buf.write("\u0a3b\7X\2\2\u0a38\u0a39\7\32\2\2\u0a39\u0a3a\7\u00fa")
        buf.write("\2\2\u0a3a\u0a3c\7\33\2\2\u0a3b\u0a38\3\2\2\2\u0a3b\u0a3c")
        buf.write("\3\2\2\2\u0a3c\u0a50\3\2\2\2\u0a3d\u0a41\7Y\2\2\u0a3e")
        buf.write("\u0a3f\7\32\2\2\u0a3f\u0a40\7\u00fa\2\2\u0a40\u0a42\7")
        buf.write("\33\2\2\u0a41\u0a3e\3\2\2\2\u0a41\u0a42\3\2\2\2\u0a42")
        buf.write("\u0a50\3\2\2\2\u0a43\u0a47\7Z\2\2\u0a44\u0a45\7\32\2\2")
        buf.write("\u0a45\u0a46\7\u00fa\2\2\u0a46\u0a48\7\33\2\2\u0a47\u0a44")
        buf.write("\3\2\2\2\u0a47\u0a48\3\2\2\2\u0a48\u0a50\3\2\2\2\u0a49")
        buf.write("\u0a4d\7\u00fb\2\2\u0a4a\u0a4b\7\32\2\2\u0a4b\u0a4c\7")
        buf.write("\u00fa\2\2\u0a4c\u0a4e\7\33\2\2\u0a4d\u0a4a\3\2\2\2\u0a4d")
        buf.write("\u0a4e\3\2\2\2\u0a4e\u0a50\3\2\2\2\u0a4f\u0a13\3\2\2\2")
        buf.write("\u0a4f\u0a19\3\2\2\2\u0a4f\u0a1f\3\2\2\2\u0a4f\u0a25\3")
        buf.write("\2\2\2\u0a4f\u0a2b\3\2\2\2\u0a4f\u0a31\3\2\2\2\u0a4f\u0a37")
        buf.write("\3\2\2\2\u0a4f\u0a3d\3\2\2\2\u0a4f\u0a43\3\2\2\2\u0a4f")
        buf.write("\u0a49\3\2\2\2\u0a50\u0a54\3\2\2\2\u0a51\u0a53\5\u0120")
        buf.write("\u0091\2\u0a52\u0a51\3\2\2\2\u0a53\u0a56\3\2\2\2\u0a54")
        buf.write("\u0a52\3\2\2\2\u0a54\u0a55\3\2\2\2\u0a55\u0a58\3\2\2\2")
        buf.write("\u0a56\u0a54\3\2\2\2\u0a57\u0a10\3\2\2\2\u0a57\u0a58\3")
        buf.write("\2\2\2\u0a58\u0a61\3\2\2\2\u0a59\u0a5d\7!\2\2\u0a5a\u0a5c")
        buf.write("\5\u011e\u0090\2\u0a5b\u0a5a\3\2\2\2\u0a5c\u0a5f\3\2\2")
        buf.write("\2\u0a5d\u0a5b\3\2\2\2\u0a5d\u0a5e\3\2\2\2\u0a5e\u0a60")
        buf.write("\3\2\2\2\u0a5f\u0a5d\3\2\2\2\u0a60\u0a62\7\u00a8\2\2\u0a61")
        buf.write("\u0a59\3\2\2\2\u0a61\u0a62\3\2\2\2\u0a62\u0a63\3\2\2\2")
        buf.write("\u0a63\u0a64\7 \2\2\u0a64\u011f\3\2\2\2\u0a65\u0a66\7")
        buf.write("!\2\2\u0a66\u0a6a\7\u00aa\2\2\u0a67\u0a68\7\32\2\2\u0a68")
        buf.write("\u0a69\7\u00fa\2\2\u0a69\u0a6b\7\33\2\2\u0a6a\u0a67\3")
        buf.write("\2\2\2\u0a6a\u0a6b\3\2\2\2\u0a6b\u0a70\3\2\2\2\u0a6c\u0a6d")
        buf.write("\7\34\2\2\u0a6d\u0a6f\5\u0160\u00b1\2\u0a6e\u0a6c\3\2")
        buf.write("\2\2\u0a6f\u0a72\3\2\2\2\u0a70\u0a6e\3\2\2\2\u0a70\u0a71")
        buf.write("\3\2\2\2\u0a71\u0a73\3\2\2\2\u0a72\u0a70\3\2\2\2\u0a73")
        buf.write("\u0a74\7\b\2\2\u0a74\u0a75\7\u00fa\2\2\u0a75\u0121\3\2")
        buf.write("\2\2\u0a76\u0a77\5\u0124\u0093\2\u0a77\u0a78\7 \2\2\u0a78")
        buf.write("\u0123\3\2\2\2\u0a79\u0a7a\7\u00ab\2\2\u0a7a\u0125\3\2")
        buf.write("\2\2\u0a7b\u0a80\5\u012a\u0096\2\u0a7c\u0a7d\7\u00dc\2")
        buf.write("\2\u0a7d\u0a7f\5\u012a\u0096\2\u0a7e\u0a7c\3\2\2\2\u0a7f")
        buf.write("\u0a82\3\2\2\2\u0a80\u0a7e\3\2\2\2\u0a80\u0a81\3\2\2\2")
        buf.write("\u0a81\u0127\3\2\2\2\u0a82\u0a80\3\2\2\2\u0a83\u0a88\5")
        buf.write("\u012a\u0096\2\u0a84\u0a85\7\u00dc\2\2\u0a85\u0a87\5\u012a")
        buf.write("\u0096\2\u0a86\u0a84\3\2\2\2\u0a87\u0a8a\3\2\2\2\u0a88")
        buf.write("\u0a86\3\2\2\2\u0a88\u0a89\3\2\2\2\u0a89\u0129\3\2\2\2")
        buf.write("\u0a8a\u0a88\3\2\2\2\u0a8b\u0a90\5\u012c\u0097\2\u0a8c")
        buf.write("\u0a8d\7\u00db\2\2\u0a8d\u0a8f\5\u012c\u0097\2\u0a8e\u0a8c")
        buf.write("\3\2\2\2\u0a8f\u0a92\3\2\2\2\u0a90\u0a8e\3\2\2\2\u0a90")
        buf.write("\u0a91\3\2\2\2\u0a91\u012b\3\2\2\2\u0a92\u0a90\3\2\2\2")
        buf.write("\u0a93\u0a98\5\u012e\u0098\2\u0a94\u0a95\7(\2\2\u0a95")
        buf.write("\u0a97\5\u012e\u0098\2\u0a96\u0a94\3\2\2\2\u0a97\u0a9a")
        buf.write("\3\2\2\2\u0a98\u0a96\3\2\2\2\u0a98\u0a99\3\2\2\2\u0a99")
        buf.write("\u012d\3\2\2\2\u0a9a\u0a98\3\2\2\2\u0a9b\u0aa0\5\u0130")
        buf.write("\u0099\2\u0a9c\u0a9d\7)\2\2\u0a9d\u0a9f\5\u0130\u0099")
        buf.write("\2\u0a9e\u0a9c\3\2\2\2\u0a9f\u0aa2\3\2\2\2\u0aa0\u0a9e")
        buf.write("\3\2\2\2\u0aa0\u0aa1\3\2\2\2\u0aa1\u012f\3\2\2\2\u0aa2")
        buf.write("\u0aa0\3\2\2\2\u0aa3\u0aa7\5\u0134\u009b\2\u0aa4\u0aa6")
        buf.write("\5\u0132\u009a\2\u0aa5\u0aa4\3\2\2\2\u0aa6\u0aa9\3\2\2")
        buf.write("\2\u0aa7\u0aa5\3\2\2\2\u0aa7\u0aa8\3\2\2\2\u0aa8\u0131")
        buf.write("\3\2\2\2\u0aa9\u0aa7\3\2\2\2\u0aaa\u0aab\7\"\2\2\u0aab")
        buf.write("\u0aaf\5\u0134\u009b\2\u0aac\u0aad\7#\2\2\u0aad\u0aaf")
        buf.write("\5\u0134\u009b\2\u0aae\u0aaa\3\2\2\2\u0aae\u0aac\3\2\2")
        buf.write("\2\u0aaf\u0133\3\2\2\2\u0ab0\u0ab4\5\u0138\u009d\2\u0ab1")
        buf.write("\u0ab3\5\u0136\u009c\2\u0ab2\u0ab1\3\2\2\2\u0ab3\u0ab6")
        buf.write("\3\2\2\2\u0ab4\u0ab2\3\2\2\2\u0ab4\u0ab5\3\2\2\2\u0ab5")
        buf.write("\u0135\3\2\2\2\u0ab6\u0ab4\3\2\2\2\u0ab7\u0ab8\7%\2\2")
        buf.write("\u0ab8\u0ac0\5\u0138\u009d\2\u0ab9\u0aba\7$\2\2\u0aba")
        buf.write("\u0ac0\5\u0138\u009d\2\u0abb\u0abc\7\'\2\2\u0abc\u0ac0")
        buf.write("\5\u0138\u009d\2\u0abd\u0abe\7&\2\2\u0abe\u0ac0\5\u0138")
        buf.write("\u009d\2\u0abf\u0ab7\3\2\2\2\u0abf\u0ab9\3\2\2\2\u0abf")
        buf.write("\u0abb\3\2\2\2\u0abf\u0abd\3\2\2\2\u0ac0\u0137\3\2\2\2")
        buf.write("\u0ac1\u0ac5\5\u013c\u009f\2\u0ac2\u0ac4\5\u013a\u009e")
        buf.write("\2\u0ac3\u0ac2\3\2\2\2\u0ac4\u0ac7\3\2\2\2\u0ac5\u0ac3")
        buf.write("\3\2\2\2\u0ac5\u0ac6\3\2\2\2\u0ac6\u0139\3\2\2\2\u0ac7")
        buf.write("\u0ac5\3\2\2\2\u0ac8\u0ac9\7\f\2\2\u0ac9\u0acd\5\u013c")
        buf.write("\u009f\2\u0aca\u0acb\7\r\2\2\u0acb\u0acd\5\u013c\u009f")
        buf.write("\2\u0acc\u0ac8\3\2\2\2\u0acc\u0aca\3\2\2\2\u0acd\u013b")
        buf.write("\3\2\2\2\u0ace\u0ad2\5\u0140\u00a1\2\u0acf\u0ad1\5\u013e")
        buf.write("\u00a0\2\u0ad0\u0acf\3\2\2\2\u0ad1\u0ad4\3\2\2\2\u0ad2")
        buf.write("\u0ad0\3\2\2\2\u0ad2\u0ad3\3\2\2\2\u0ad3\u013d\3\2\2\2")
        buf.write("\u0ad4\u0ad2\3\2\2\2\u0ad5\u0ad6\7\16\2\2\u0ad6\u0ada")
        buf.write("\5\u0140\u00a1\2\u0ad7\u0ad8\7\35\2\2\u0ad8\u0ada\5\u0140")
        buf.write("\u00a1\2\u0ad9\u0ad5\3\2\2\2\u0ad9\u0ad7\3\2\2\2\u0ada")
        buf.write("\u013f\3\2\2\2\u0adb\u0adf\5\u0144\u00a3\2\u0adc\u0ade")
        buf.write("\5\u0142\u00a2\2\u0add\u0adc\3\2\2\2\u0ade\u0ae1\3\2\2")
        buf.write("\2\u0adf\u0add\3\2\2\2\u0adf\u0ae0\3\2\2\2\u0ae0\u0141")
        buf.write("\3\2\2\2\u0ae1\u0adf\3\2\2\2\u0ae2\u0ae3\7\17\2\2\u0ae3")
        buf.write("\u0ae9\5\u0144\u00a3\2\u0ae4\u0ae5\7\37\2\2\u0ae5\u0ae9")
        buf.write("\5\u0144\u00a3\2\u0ae6\u0ae7\7\20\2\2\u0ae7\u0ae9\5\u0144")
        buf.write("\u00a3\2\u0ae8\u0ae2\3\2\2\2\u0ae8\u0ae4\3\2\2\2\u0ae8")
        buf.write("\u0ae6\3\2\2\2\u0ae9\u0143\3\2\2\2\u0aea\u0aec\5\u0146")
        buf.write("\u00a4\2\u0aeb\u0aea\3\2\2\2\u0aec\u0aef\3\2\2\2\u0aed")
        buf.write("\u0aeb\3\2\2\2\u0aed\u0aee\3\2\2\2\u0aee\u0af0\3\2\2\2")
        buf.write("\u0aef\u0aed\3\2\2\2\u0af0\u0af1\5\u0148\u00a5\2\u0af1")
        buf.write("\u0145\3\2\2\2\u0af2\u0af3\7\30\2\2\u0af3\u0af4\t\5\2")
        buf.write("\2\u0af4\u0af5\7\31\2\2\u0af5\u0147\3\2\2\2\u0af6\u0b02")
        buf.write("\5\u014a\u00a6\2\u0af7\u0b02\5\u014c\u00a7\2\u0af8\u0b02")
        buf.write("\5\u014e\u00a8\2\u0af9\u0b02\5\u0150\u00a9\2\u0afa\u0b02")
        buf.write("\5\u0152\u00aa\2\u0afb\u0b02\5\u0170\u00b9\2\u0afc\u0b02")
        buf.write("\5\u0172\u00ba\2\u0afd\u0b02\5\u0188\u00c5\2\u0afe\u0b02")
        buf.write("\5\u0198\u00cd\2\u0aff\u0b00\7\u00dd\2\2\u0b00\u0b02\5")
        buf.write("\u0148\u00a5\2\u0b01\u0af6\3\2\2\2\u0b01\u0af7\3\2\2\2")
        buf.write("\u0b01\u0af8\3\2\2\2\u0b01\u0af9\3\2\2\2\u0b01\u0afa\3")
        buf.write("\2\2\2\u0b01\u0afb\3\2\2\2\u0b01\u0afc\3\2\2\2\u0b01\u0afd")
        buf.write("\3\2\2\2\u0b01\u0afe\3\2\2\2\u0b01\u0aff\3\2\2\2\u0b02")
        buf.write("\u0149\3\2\2\2\u0b03\u0b04\7\u00e7\2\2\u0b04\u0b05\7\30")
        buf.write("\2\2\u0b05\u0b06\5\u0128\u0095\2\u0b06\u0b07\7!\2\2\u0b07")
        buf.write("\u0b08\5\u0128\u0095\2\u0b08\u0b09\7\31\2\2\u0b09\u014b")
        buf.write("\3\2\2\2\u0b0a\u0b0b\7\u00e5\2\2\u0b0b\u0b0c\7\30\2\2")
        buf.write("\u0b0c\u0b0d\5\u0128\u0095\2\u0b0d\u0b0e\7!\2\2\u0b0e")
        buf.write("\u0b0f\5\u0128\u0095\2\u0b0f\u0b10\7\31\2\2\u0b10\u014d")
        buf.write("\3\2\2\2\u0b11\u0b12\7\u00e6\2\2\u0b12\u0b13\7\30\2\2")
        buf.write("\u0b13\u0b14\5\u0128\u0095\2\u0b14\u0b15\7!\2\2\u0b15")
        buf.write("\u0b16\5\u0128\u0095\2\u0b16\u0b17\7!\2\2\u0b17\u0b18")
        buf.write("\5\66\34\2\u0b18\u0b19\7\31\2\2\u0b19\u014f\3\2\2\2\u0b1a")
        buf.write("\u0b1b\7\30\2\2\u0b1b\u0b1c\5\u0128\u0095\2\u0b1c\u0b1d")
        buf.write("\7\31\2\2\u0b1d\u0151\3\2\2\2\u0b1e\u0b2a\5\u0154\u00ab")
        buf.write("\2\u0b1f\u0b2a\5\u0156\u00ac\2\u0b20\u0b2a\5\u0158\u00ad")
        buf.write("\2\u0b21\u0b2a\5\u015a\u00ae\2\u0b22\u0b2a\5\u015c\u00af")
        buf.write("\2\u0b23\u0b2a\5\u0162\u00b2\2\u0b24\u0b2a\5\u0164\u00b3")
        buf.write("\2\u0b25\u0b2a\5\u0166\u00b4\2\u0b26\u0b2a\5\u0168\u00b5")
        buf.write("\2\u0b27\u0b2a\5\u016a\u00b6\2\u0b28\u0b2a\5\u016e\u00b8")
        buf.write("\2\u0b29\u0b1e\3\2\2\2\u0b29\u0b1f\3\2\2\2\u0b29\u0b20")
        buf.write("\3\2\2\2\u0b29\u0b21\3\2\2\2\u0b29\u0b22\3\2\2\2\u0b29")
        buf.write("\u0b23\3\2\2\2\u0b29\u0b24\3\2\2\2\u0b29\u0b25\3\2\2\2")
        buf.write("\u0b29\u0b26\3\2\2\2\u0b29\u0b27\3\2\2\2\u0b29\u0b28\3")
        buf.write("\2\2\2\u0b2a\u0153\3\2\2\2\u0b2b\u0b2c\7\u00c7\2\2\u0b2c")
        buf.write("\u0155\3\2\2\2\u0b2d\u0b2e\7\u00c8\2\2\u0b2e\u0b2f\7\u00c9")
        buf.write("\2\2\u0b2f\u0b30\7\30\2\2\u0b30\u0b31\7\u00fa\2\2\u0b31")
        buf.write("\u0b3c\7\31\2\2\u0b32\u0b33\7\"\2\2\u0b33\u0b3d\t\6\2")
        buf.write("\2\u0b34\u0b35\7$\2\2\u0b35\u0b3d\t\6\2\2\u0b36\u0b37")
        buf.write("\7%\2\2\u0b37\u0b3d\t\6\2\2\u0b38\u0b39\7&\2\2\u0b39\u0b3d")
        buf.write("\t\6\2\2\u0b3a\u0b3b\7\'\2\2\u0b3b\u0b3d\t\6\2\2\u0b3c")
        buf.write("\u0b32\3\2\2\2\u0b3c\u0b34\3\2\2\2\u0b3c\u0b36\3\2\2\2")
        buf.write("\u0b3c\u0b38\3\2\2\2\u0b3c\u0b3a\3\2\2\2\u0b3d\u0157\3")
        buf.write("\2\2\2\u0b3e\u0b3f\7\u00ca\2\2\u0b3f\u0b4a\5\u015e\u00b0")
        buf.write("\2\u0b40\u0b41\7\"\2\2\u0b41\u0b4b\t\6\2\2\u0b42\u0b43")
        buf.write("\7$\2\2\u0b43\u0b4b\t\6\2\2\u0b44\u0b45\7%\2\2\u0b45\u0b4b")
        buf.write("\t\6\2\2\u0b46\u0b47\7&\2\2\u0b47\u0b4b\t\6\2\2\u0b48")
        buf.write("\u0b49\7\'\2\2\u0b49\u0b4b\t\6\2\2\u0b4a\u0b40\3\2\2\2")
        buf.write("\u0b4a\u0b42\3\2\2\2\u0b4a\u0b44\3\2\2\2\u0b4a\u0b46\3")
        buf.write("\2\2\2\u0b4a\u0b48\3\2\2\2\u0b4b\u0159\3\2\2\2\u0b4c\u0b4d")
        buf.write("\7\u00cb\2\2\u0b4d\u0b58\5\u015e\u00b0\2\u0b4e\u0b4f\7")
        buf.write("\"\2\2\u0b4f\u0b59\5\u015e\u00b0\2\u0b50\u0b51\7$\2\2")
        buf.write("\u0b51\u0b59\5\u015e\u00b0\2\u0b52\u0b53\7%\2\2\u0b53")
        buf.write("\u0b59\5\u015e\u00b0\2\u0b54\u0b55\7&\2\2\u0b55\u0b59")
        buf.write("\5\u015e\u00b0\2\u0b56\u0b57\7\'\2\2\u0b57\u0b59\5\u015e")
        buf.write("\u00b0\2\u0b58\u0b4e\3\2\2\2\u0b58\u0b50\3\2\2\2\u0b58")
        buf.write("\u0b52\3\2\2\2\u0b58\u0b54\3\2\2\2\u0b58\u0b56\3\2\2\2")
        buf.write("\u0b59\u015b\3\2\2\2\u0b5a\u0b5b\7\u00cc\2\2\u0b5b\u0b5c")
        buf.write("\5\u015e\u00b0\2\u0b5c\u0b5e\7\"\2\2\u0b5d\u0b5f\t\6\2")
        buf.write("\2\u0b5e\u0b5d\3\2\2\2\u0b5f\u0b60\3\2\2\2\u0b60\u0b5e")
        buf.write("\3\2\2\2\u0b60\u0b61\3\2\2\2\u0b61\u015d\3\2\2\2\u0b62")
        buf.write("\u0b63\7\u00fb\2\2\u0b63\u0b64\7\32\2\2\u0b64\u0b65\7")
        buf.write("\u00fa\2\2\u0b65\u0b6f\7\33\2\2\u0b66\u0b6b\7\u00fb\2")
        buf.write("\2\u0b67\u0b68\7\34\2\2\u0b68\u0b6a\5\u0160\u00b1\2\u0b69")
        buf.write("\u0b67\3\2\2\2\u0b6a\u0b6d\3\2\2\2\u0b6b\u0b69\3\2\2\2")
        buf.write("\u0b6b\u0b6c\3\2\2\2\u0b6c\u0b6f\3\2\2\2\u0b6d\u0b6b\3")
        buf.write("\2\2\2\u0b6e\u0b62\3\2\2\2\u0b6e\u0b66\3\2\2\2\u0b6f\u015f")
        buf.write("\3\2\2\2\u0b70\u0b74\7\u00fb\2\2\u0b71\u0b72\7\32\2\2")
        buf.write("\u0b72\u0b73\7\u00fa\2\2\u0b73\u0b75\7\33\2\2\u0b74\u0b71")
        buf.write("\3\2\2\2\u0b74\u0b75\3\2\2\2\u0b75\u0161\3\2\2\2\u0b76")
        buf.write("\u0b77\7\u00cd\2\2\u0b77\u0b78\7\30\2\2\u0b78\u0b79\t")
        buf.write("\6\2\2\u0b79\u0b7a\7\31\2\2\u0b7a\u0163\3\2\2\2\u0b7b")
        buf.write("\u0b7c\7\u00ce\2\2\u0b7c\u0b7d\7\30\2\2\u0b7d\u0b7e\7")
        buf.write("\u00fb\2\2\u0b7e\u0b7f\7\31\2\2\u0b7f\u0165\3\2\2\2\u0b80")
        buf.write("\u0b81\7\u00cf\2\2\u0b81\u0b87\7\30\2\2\u0b82\u0b83\7")
        buf.write("\u00ec\2\2\u0b83\u0b84\7\30\2\2\u0b84\u0b85\7\u00fb\2")
        buf.write("\2\u0b85\u0b88\7\31\2\2\u0b86\u0b88\7\u00fa\2\2\u0b87")
        buf.write("\u0b82\3\2\2\2\u0b87\u0b86\3\2\2\2\u0b88\u0b89\3\2\2\2")
        buf.write("\u0b89\u0b8a\7\31\2\2\u0b8a\u0167\3\2\2\2\u0b8b\u0b8c")
        buf.write("\7\u00d0\2\2\u0b8c\u0169\3\2\2\2\u0b8d\u0b8e\7\u00d1\2")
        buf.write("\2\u0b8e\u0b8f\7\30\2\2\u0b8f\u0b90\5\66\34\2\u0b90\u0b91")
        buf.write("\7\31\2\2\u0b91\u016b\3\2\2\2\u0b92\u0b93\t\7\2\2\u0b93")
        buf.write("\u016d\3\2\2\2\u0b94\u0b95\7\u00d2\2\2\u0b95\u0b96\7\30")
        buf.write("\2\2\u0b96\u0b9b\5Z.\2\u0b97\u0b98\7(\2\2\u0b98\u0b99")
        buf.write("\7@\2\2\u0b99\u0b9a\7\b\2\2\u0b9a\u0b9c\5\u016c\u00b7")
        buf.write("\2\u0b9b\u0b97\3\2\2\2\u0b9b\u0b9c\3\2\2\2\u0b9c\u0b9d")
        buf.write("\3\2\2\2\u0b9d\u0b9e\7\31\2\2\u0b9e\u016f\3\2\2\2\u0b9f")
        buf.write("\u0ba0\t\b\2\2\u0ba0\u0171\3\2\2\2\u0ba1\u0bac\5\u0174")
        buf.write("\u00bb\2\u0ba2\u0bac\5\u0176\u00bc\2\u0ba3\u0bac\5\u0178")
        buf.write("\u00bd\2\u0ba4\u0bac\5\u017a\u00be\2\u0ba5\u0bac\5\u017c")
        buf.write("\u00bf\2\u0ba6\u0bac\5\u017e\u00c0\2\u0ba7\u0bac\5\u0180")
        buf.write("\u00c1\2\u0ba8\u0bac\5\u0182\u00c2\2\u0ba9\u0bac\5\u0184")
        buf.write("\u00c3\2\u0baa\u0bac\5\u0186\u00c4\2\u0bab\u0ba1\3\2\2")
        buf.write("\2\u0bab\u0ba2\3\2\2\2\u0bab\u0ba3\3\2\2\2\u0bab\u0ba4")
        buf.write("\3\2\2\2\u0bab\u0ba5\3\2\2\2\u0bab\u0ba6\3\2\2\2\u0bab")
        buf.write("\u0ba7\3\2\2\2\u0bab\u0ba8\3\2\2\2\u0bab\u0ba9\3\2\2\2")
        buf.write("\u0bab\u0baa\3\2\2\2\u0bac\u0173\3\2\2\2\u0bad\u0bae\7")
        buf.write("\u00da\2\2\u0bae\u0baf\7\30\2\2\u0baf\u0bb0\5\u0128\u0095")
        buf.write("\2\u0bb0\u0bb1\7\31\2\2\u0bb1\u0175\3\2\2\2\u0bb2\u0bb3")
        buf.write("\7\u00df\2\2\u0bb3\u0bb4\7\30\2\2\u0bb4\u0bb5\5\u0128")
        buf.write("\u0095\2\u0bb5\u0bb6\7\31\2\2\u0bb6\u0177\3\2\2\2\u0bb7")
        buf.write("\u0bb8\7\u00e8\2\2\u0bb8\u0bc0\7\30\2\2\u0bb9\u0bba\7")
        buf.write("*\2\2\u0bba\u0bbb\7\b\2\2\u0bbb\u0bbc\7\u00ec\2\2\u0bbc")
        buf.write("\u0bbd\7\30\2\2\u0bbd\u0bbe\7\u00fb\2\2\u0bbe\u0bbf\7")
        buf.write("\31\2\2\u0bbf\u0bc1\7!\2\2\u0bc0\u0bb9\3\2\2\2\u0bc0\u0bc1")
        buf.write("\3\2\2\2\u0bc1\u0bc7\3\2\2\2\u0bc2\u0bc3\7[\2\2\u0bc3")
        buf.write("\u0bc4\7\b\2\2\u0bc4\u0bc5\5\66\34\2\u0bc5\u0bc6\7!\2")
        buf.write("\2\u0bc6\u0bc8\3\2\2\2\u0bc7\u0bc2\3\2\2\2\u0bc7\u0bc8")
        buf.write("\3\2\2\2\u0bc8\u0bc9\3\2\2\2\u0bc9\u0bca\5\u0128\u0095")
        buf.write("\2\u0bca\u0bcb\7\31\2\2\u0bcb\u0179\3\2\2\2\u0bcc\u0bcd")
        buf.write("\7\u00e9\2\2\u0bcd\u0bce\7\30\2\2\u0bce\u0bcf\5\u0128")
        buf.write("\u0095\2\u0bcf\u0bd0\7\31\2\2\u0bd0\u017b\3\2\2\2\u0bd1")
        buf.write("\u0bd2\7\u00e0\2\2\u0bd2\u0bd3\7\30\2\2\u0bd3\u0bd4\5")
        buf.write("\u0128\u0095\2\u0bd4\u0bd5\7\31\2\2\u0bd5\u017d\3\2\2")
        buf.write("\2\u0bd6\u0bdb\7\u00e1\2\2\u0bd7\u0bd8\7\21\2\2\u0bd8")
        buf.write("\u0bd9\7\b\2\2\u0bd9\u0bda\7\u00fa\2\2\u0bda\u0bdc\7!")
        buf.write("\2\2\u0bdb\u0bd7\3\2\2\2\u0bdb\u0bdc\3\2\2\2\u0bdc\u0bdd")
        buf.write("\3\2\2\2\u0bdd\u0bde\7\30\2\2\u0bde\u0bdf\5\u0128\u0095")
        buf.write("\2\u0bdf\u0be0\7\31\2\2\u0be0\u017f\3\2\2\2\u0be1\u0be2")
        buf.write("\7\u00e2\2\2\u0be2\u0be3\7\30\2\2\u0be3\u0be4\5\u0128")
        buf.write("\u0095\2\u0be4\u0be5\7\31\2\2\u0be5\u0181\3\2\2\2\u0be6")
        buf.write("\u0be7\7\u00e3\2\2\u0be7\u0be8\7\30\2\2\u0be8\u0be9\5")
        buf.write("\u0128\u0095\2\u0be9\u0bea\7\31\2\2\u0bea\u0183\3\2\2")
        buf.write("\2\u0beb\u0bec\7\u00e4\2\2\u0bec\u0bed\7\30\2\2\u0bed")
        buf.write("\u0bee\5\u0128\u0095\2\u0bee\u0bef\7\31\2\2\u0bef\u0185")
        buf.write("\3\2\2\2\u0bf0\u0bf1\7\u00de\2\2\u0bf1\u0bf2\7\30\2\2")
        buf.write("\u0bf2\u0bf7\5Z.\2\u0bf3\u0bf4\7(\2\2\u0bf4\u0bf5\7@\2")
        buf.write("\2\u0bf5\u0bf6\7\b\2\2\u0bf6\u0bf8\5\u016c\u00b7\2\u0bf7")
        buf.write("\u0bf3\3\2\2\2\u0bf7\u0bf8\3\2\2\2\u0bf8\u0bf9\3\2\2\2")
        buf.write("\u0bf9\u0bfa\7!\2\2\u0bfa\u0bfb\5\u0128\u0095\2\u0bfb")
        buf.write("\u0bfc\7\31\2\2\u0bfc\u0187\3\2\2\2\u0bfd\u0c03\5\u018a")
        buf.write("\u00c6\2\u0bfe\u0c03\5\u018c\u00c7\2\u0bff\u0c03\5\u0190")
        buf.write("\u00c9\2\u0c00\u0c03\5\u0192\u00ca\2\u0c01\u0c03\5\u0194")
        buf.write("\u00cb\2\u0c02\u0bfd\3\2\2\2\u0c02\u0bfe\3\2\2\2\u0c02")
        buf.write("\u0bff\3\2\2\2\u0c02\u0c00\3\2\2\2\u0c02\u0c01\3\2\2\2")
        buf.write("\u0c03\u0189\3\2\2\2\u0c04\u0c05\7\u00c2\2\2\u0c05\u0c06")
        buf.write("\7\30\2\2\u0c06\u0c07\5\u0128\u0095\2\u0c07\u0c08\7\22")
        buf.write("\2\2\u0c08\u0c09\5\u0128\u0095\2\u0c09\u0c0a\7\36\2\2")
        buf.write("\u0c0a\u0c0b\5\u0128\u0095\2\u0c0b\u0c0c\7\31\2\2\u0c0c")
        buf.write("\u018b\3\2\2\2\u0c0d\u0c0e\7\u00c3\2\2\u0c0e\u0c0f\7\30")
        buf.write("\2\2\u0c0f\u0c14\5\u018e\u00c8\2\u0c10\u0c11\7(\2\2\u0c11")
        buf.write("\u0c13\5\u018e\u00c8\2\u0c12\u0c10\3\2\2\2\u0c13\u0c16")
        buf.write("\3\2\2\2\u0c14\u0c12\3\2\2\2\u0c14\u0c15\3\2\2\2\u0c15")
        buf.write("\u0c17\3\2\2\2\u0c16\u0c14\3\2\2\2\u0c17\u0c18\7!\2\2")
        buf.write("\u0c18\u0c19\5\u0128\u0095\2\u0c19\u0c1a\7!\2\2\u0c1a")
        buf.write("\u0c1b\5\u0128\u0095\2\u0c1b\u0c1c\7!\2\2\u0c1c\u0c1d")
        buf.write("\5\u0128\u0095\2\u0c1d\u0c1e\7\31\2\2\u0c1e\u018d\3\2")
        buf.write("\2\2\u0c1f\u0c20\t\t\2\2\u0c20\u018f\3\2\2\2\u0c21\u0c22")
        buf.write("\7\u00c4\2\2\u0c22\u0c23\7\30\2\2\u0c23\u0c24\5\u0128")
        buf.write("\u0095\2\u0c24\u0c25\7!\2\2\u0c25\u0c26\5\u0128\u0095")
        buf.write("\2\u0c26\u0c27\7!\2\2\u0c27\u0c28\5\u0128\u0095\2\u0c28")
        buf.write("\u0c29\7\31\2\2\u0c29\u0191\3\2\2\2\u0c2a\u0c2b\7\u00c5")
        buf.write("\2\2\u0c2b\u0c2c\7\30\2\2\u0c2c\u0c2d\5\u0128\u0095\2")
        buf.write("\u0c2d\u0c2e\7!\2\2\u0c2e\u0c2f\5\u0128\u0095\2\u0c2f")
        buf.write("\u0c30\7!\2\2\u0c30\u0c31\5\u0128\u0095\2\u0c31\u0c32")
        buf.write("\7\31\2\2\u0c32\u0193\3\2\2\2\u0c33\u0c34\7\u00c6\2\2")
        buf.write("\u0c34\u0c35\7\30\2\2\u0c35\u0c36\7@\2\2\u0c36\u0c37\7")
        buf.write("\b\2\2\u0c37\u0c3c\5\u0196\u00cc\2\u0c38\u0c39\7(\2\2")
        buf.write("\u0c39\u0c3b\5\u0196\u00cc\2\u0c3a\u0c38\3\2\2\2\u0c3b")
        buf.write("\u0c3e\3\2\2\2\u0c3c\u0c3a\3\2\2\2\u0c3c\u0c3d\3\2\2\2")
        buf.write("\u0c3d\u0c3f\3\2\2\2\u0c3e\u0c3c\3\2\2\2\u0c3f\u0c40\7")
        buf.write("!\2\2\u0c40\u0c41\5\u0128\u0095\2\u0c41\u0c42\7!\2\2\u0c42")
        buf.write("\u0c43\5\u0128\u0095\2\u0c43\u0c44\7!\2\2\u0c44\u0c45")
        buf.write("\5\u0128\u0095\2\u0c45\u0c46\7\31\2\2\u0c46\u0195\3\2")
        buf.write("\2\2\u0c47\u0c48\t\n\2\2\u0c48\u0197\3\2\2\2\u0c49\u0c4a")
        buf.write("\7\u00ea\2\2\u0c4a\u0c4b\7\30\2\2\u0c4b\u0c4c\5\u0128")
        buf.write("\u0095\2\u0c4c\u0c54\7\36\2\2\u0c4d\u0c4e\5\u0126\u0094")
        buf.write("\2\u0c4e\u0c4f\7!\2\2\u0c4f\u0c50\5\u0126\u0094\2\u0c50")
        buf.write("\u0c51\7 \2\2\u0c51\u0c53\3\2\2\2\u0c52\u0c4d\3\2\2\2")
        buf.write("\u0c53\u0c56\3\2\2\2\u0c54\u0c52\3\2\2\2\u0c54\u0c55\3")
        buf.write("\2\2\2\u0c55\u0c57\3\2\2\2\u0c56\u0c54\3\2\2\2\u0c57\u0c58")
        buf.write("\7\31\2\2\u0c58\u0199\3\2\2\2\u0121\u019b\u019e\u01a3")
        buf.write("\u01a5\u01ad\u01b1\u01b4\u01bc\u01c1\u01c5\u01c8\u01ce")
        buf.write("\u01d3\u01d7\u01da\u01e0\u01f2\u01f4\u01fc\u0205\u020e")
        buf.write("\u0217\u0220\u0229\u0232\u023b\u0244\u024d\u0253\u025b")
        buf.write("\u0263\u026b\u0289\u0290\u0297\u02a0\u02a4\u02a8\u02c6")
        buf.write("\u02cf\u02db\u02e3\u02e8\u02f5\u0305\u0307\u031c\u0322")
        buf.write("\u0325\u0341\u0347\u034a\u0353\u0366\u0369\u0372\u037b")
        buf.write("\u037e\u0389\u03aa\u03b1\u03b7\u03ba\u03d2\u03dd\u03e0")
        buf.write("\u03e9\u040b\u040f\u041c\u0423\u042b\u0438\u044d\u0454")
        buf.write("\u0465\u046b\u0481\u048e\u0492\u0497\u049d\u04a0\u04a4")
        buf.write("\u04a8\u04af\u04b5\u04cc\u04d6\u04de\u04e0\u04e4\u04eb")
        buf.write("\u04ef\u0501\u0508\u0514\u051b\u0523\u052c\u0530\u0533")
        buf.write("\u053a\u0541\u0543\u0547\u0550\u0556\u0562\u056d\u057a")
        buf.write("\u058b\u0590\u0595\u05a6\u05ab\u05b0\u05b8\u05bf\u05da")
        buf.write("\u05dd\u05e2\u05e7\u05f1\u05fc\u0608\u060d\u0612\u061e")
        buf.write("\u0623\u0628\u0632\u0638\u0654\u0656\u065c\u0666\u0675")
        buf.write("\u0682\u0687\u068b\u0696\u069c\u069f\u06aa\u06b4\u06be")
        buf.write("\u06d0\u06d6\u06da\u06e5\u06eb\u06ee\u06f8\u06fc\u0702")
        buf.write("\u0706\u070d\u0710\u0717\u0724\u072f\u0732\u073d\u0742")
        buf.write("\u074c\u0752\u0755\u075b\u0762\u076e\u0775\u077f\u0785")
        buf.write("\u0788\u078e\u0795\u079c\u079f\u07aa\u07b0\u07b9\u07bc")
        buf.write("\u07c3\u07ce\u07d6\u07e0\u082b\u0830\u0833\u0847\u084e")
        buf.write("\u0850\u0857\u0862\u086c\u08b7\u08bc\u08bf\u08d3\u08da")
        buf.write("\u08dc\u08e3\u08ee\u08f4\u0905\u090b\u0913\u0921\u0926")
        buf.write("\u0933\u0938\u0945\u094a\u0951\u095f\u0964\u096b\u0980")
        buf.write("\u0985\u098e\u0995\u099c\u09b5\u09c0\u09d8\u09db\u09e2")
        buf.write("\u09e4\u09eb\u09f1\u09fd\u0a07\u0a0a\u0a17\u0a1d\u0a23")
        buf.write("\u0a29\u0a2f\u0a35\u0a3b\u0a41\u0a47\u0a4d\u0a4f\u0a54")
        buf.write("\u0a57\u0a5d\u0a61\u0a6a\u0a70\u0a80\u0a88\u0a90\u0a98")
        buf.write("\u0aa0\u0aa7\u0aae\u0ab4\u0abf\u0ac5\u0acc\u0ad2\u0ad9")
        buf.write("\u0adf\u0ae8\u0aed\u0b01\u0b29\u0b3c\u0b4a\u0b58\u0b60")
        buf.write("\u0b6b\u0b6e\u0b74\u0b87\u0b9b\u0bab\u0bc0\u0bc7\u0bdb")
        buf.write("\u0bf7\u0c02\u0c14\u0c3c\u0c54")
        return buf.getvalue()


class SourceVfrSyntaxParser ( Parser ):

    grammarFileName = "SourceVfrSyntax.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'show'", "'push'", "'pop'", "'#pragma'",
                     "'pack'", "'='", "'IMAGE_TOKEN'", "'HORIZONTAL'", "'MULTI_LINE'",
                     "'<<'", "'>>'", "'+'", "'*'", "'%'", "'format'", "'?'",
                     "'#define'", "'#include'", "'formpkgtype'", "'{'",
                     "'}'", "'('", "')'", "'['", "']'", "'.'", "'-'", "':'",
                     "'/'", "';'", "','", "'=='", "'!='", "'<='", "'<'",
                     "'>='", "'>'", "'|'", "'&'", "'devicepath'", "'formset'",
                     "'formsetid'", "'endformset'", "'title'", "'formid'",
                     "'oneof'", "'endoneof'", "'prompt'", "'orderedlist'",
                     "'maxcontainers'", "'endlist'", "'endform'", "'form'",
                     "'formmap'", "'maptitle'", "'mapguid'", "'subtitle'",
                     "'endsubtitle'", "'help'", "'text'", "'option'", "'flags'",
                     "'date'", "'enddate'", "'year'", "'month'", "'day'",
                     "'time'", "'endtime'", "'hour'", "'minute'", "'second'",
                     "'grayoutif'", "'label'", "'timeout'", "'inventory'",
                     "'_NON_NV_DATA_MAP'", "'struct'", "'union'", "'BOOLEAN'",
                     "'UINT64'", "'UINT32'", "'UINT16'", "'UINT8'", "'EFI_STRING_ID'",
                     "'EFI_HII_DATE'", "'EFI_HII_TIME'", "'EFI_HII_REF'",
                     "'guid'", "'checkbox'", "'endcheckbox'", "'numeric'",
                     "'endnumeric'", "'minimum'", "'maximum'", "'step'",
                     "'default'", "'password'", "'endpassword'", "'string'",
                     "'endstring'", "'minsize'", "'maxsize'", "'encoding'",
                     "'suppressif'", "'disableif'", "'hidden'", "'goto'",
                     "'formsetguid'", "'inconsistentif'", "'warningif'",
                     "'nosubmitif'", "'endif'", "'key'", "'DEFAULT'", "'MANUFACTURING'",
                     "'CHECKBOX_DEFAULT'", "'CHECKBOX_DEFAULT_MFG'", "'INTERACTIVE'",
                     "'NV_ACCESS'", "'RESET_REQUIRED'", "'RECONNECT_REQUIRED'",
                     "'LATE_CHECK'", "'READ_ONLY'", "'OPTIONS_ONLY'", "'REST_STYLE'",
                     "'class'", "'subclass'", "'classguid'", "'typedef'",
                     "'restore'", "'save'", "'defaults'", "'banner'", "'align'",
                     "'left'", "'right'", "'center'", "'line'", "'name'",
                     "'varid'", "'question'", "'questionid'", "'image'",
                     "'locked'", "'rule'", "'endrule'", "'value'", "'read'",
                     "'write'", "'resetbutton'", "'endresetbutton'", "'defaultstore'",
                     "'attribute'", "'varstore'", "'efivarstore'", "'varsize'",
                     "'namevaluevarstore'", "'action'", "'config'", "'endaction'",
                     "'refresh'", "'interval'", "'varstoredevice'", "'guidop'",
                     "'endguidop'", "'datatype'", "'data'", "'modal'", "'NON_DEVICE'",
                     "'DISK_DEVICE'", "'VIDEO_DEVICE'", "'NETWORK_DEVICE'",
                     "'INPUT_DEVICE'", "'ONBOARD_DEVICE'", "'OTHER_DEVICE'",
                     "'SETUP_APPLICATION'", "'GENERAL_APPLICATION'", "'FRONT_PAGE'",
                     "'SINGLE_USE'", "'YEAR_SUPPRESS'", "'MONTH_SUPPRESS'",
                     "'DAY_SUPPRESS'", "'HOUR_SUPPRESS'", "'MINUTE_SUPPRESS'",
                     "'SECOND_SUPPRESS'", "'STORAGE_NORMAL'", "'STORAGE_TIME'",
                     "'STORAGE_WAKEUP'", "'UNIQUE'", "'NOEMPTY'", "'cond'",
                     "'find'", "'mid'", "'token'", "'span'", "'dup'", "'vareqval'",
                     "'var'", "'ideqval'", "'ideqid'", "'ideqvallist'",
                     "'questionref'", "'ruleref'", "'stringref'", "'pushthis'",
                     "'security'", "'get'", "'TRUE'", "'FALSE'", "'ONE'",
                     "'ONES'", "'ZERO'", "'UNDEFINED'", "'VERSION'", "'length'",
                     "'AND'", "'OR'", "'NOT'", "'set'", "'~'", "'boolval'",
                     "'stringval'", "'unintval'", "'toupper'", "'tolower'",
                     "'match'", "'match2'", "'catenate'", "'questionrefval'",
                     "'stringrefval'", "'map'", "'refreshguid'", "'STRING_TOKEN'",
                     "'OPTION_DEFAULT'", "'OPTION_DEFAULT_MFG'", "'NUMERIC_SIZE_1'",
                     "'NUMERIC_SIZE_2'", "'NUMERIC_SIZE_4'", "'NUMERIC_SIZE_8'",
                     "'DISPLAY_INT_DEC'", "'DISPLAY_UINT_DEC'", "'DISPLAY_UINT_HEX'",
                     "'INSENSITIVE'", "'SENSITIVE'", "'LAST_NON_MATCH'",
                     "'FIRST_NON_MATCH'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "Define", "Include", "FormPkgType", "OpenBrace",
                      "CloseBrace", "OpenParen", "CloseParen", "OpenBracket",
                      "CloseBracket", "Dot", "Negative", "Colon", "Slash",
                      "Semicolon", "Comma", "Equal", "NotEqual", "LessEqual",
                      "Less", "GreaterEqual", "Greater", "BitWiseOr", "BitWiseAnd",
                      "DevicePath", "FormSet", "FormSetId", "EndFormSet",
                      "Title", "FormId", "OneOf", "EndOneOf", "Prompt",
                      "OrderedList", "MaxContainers", "EndList", "EndForm",
                      "Form", "FormMap", "MapTitle", "MapGuid", "Subtitle",
                      "EndSubtitle", "Help", "Text", "Option", "FLAGS",
                      "Date", "EndDate", "Year", "Month", "Day", "Time",
                      "EndTime", "Hour", "Minute", "Second", "GrayOutIf",
                      "Label", "Timeout", "Inventory", "NonNvDataMap", "Struct",
                      "Union", "Boolean", "Uint64", "Uint32", "Uint16",
                      "Uint8", "EFI_STRING_ID", "EFI_HII_DATE", "EFI_HII_TIME",
                      "EFI_HII_REF", "Uuid", "CheckBox", "EndCheckBox",
                      "Numeric", "EndNumeric", "Minimum", "Maximum", "Step",
                      "Default", "Password", "EndPassword", "String", "EndString",
                      "MinSize", "MaxSize", "Encoding", "SuppressIf", "DisableIf",
                      "Hidden", "Goto", "FormSetGuid", "InconsistentIf",
                      "WarningIf", "NoSubmitIf", "EndIf", "Key", "DefaultFlag",
                      "ManufacturingFlag", "CheckBoxDefaultFlag", "CheckBoxDefaultMfgFlag",
                      "InteractiveFlag", "NVAccessFlag", "ResetRequiredFlag",
                      "ReconnectRequiredFlag", "LateCheckFlag", "ReadOnlyFlag",
                      "OptionOnlyFlag", "RestStyleFlag", "Class", "Subclass",
                      "ClassGuid", "TypeDef", "Restore", "Save", "Defaults",
                      "Banner", "Align", "Left", "Right", "Center", "Line",
                      "Name", "VarId", "Question", "QuestionId", "Image",
                      "Locked", "Rule", "EndRule", "Value", "Read", "Write",
                      "ResetButton", "EndResetButton", "DefaultStore", "Attribute",
                      "Varstore", "Efivarstore", "VarSize", "NameValueVarStore",
                      "Action", "Config", "EndAction", "Refresh", "Interval",
                      "VarstoreDevice", "GuidOp", "EndGuidOp", "DataType",
                      "Data", "Modal", "ClassNonDevice", "ClassDiskDevice",
                      "ClassVideoDevice", "ClassNetworkDevice", "ClassInputDevice",
                      "ClassOnBoardDevice", "ClassOtherDevice", "SubclassSetupApplication",
                      "SubclassGeneralApplication", "SubclassFrontPage",
                      "SubclassSingleUse", "YearSupppressFlag", "MonthSuppressFlag",
                      "DaySuppressFlag", "HourSupppressFlag", "MinuteSuppressFlag",
                      "SecondSuppressFlag", "StorageNormalFlag", "StorageTimeFlag",
                      "StorageWakeUpFlag", "UniQueFlag", "NoEmptyFlag",
                      "Cond", "Find", "Mid", "Tok", "Span", "Dup", "VarEqVal",
                      "Var", "IdEqVal", "IdEqId", "IdEqValList", "QuestionRef",
                      "RuleRef", "StringRef", "PushThis", "Security", "Get",
                      "TrueSymbol", "FalseSymbol", "One", "Ones", "Zero",
                      "Undefined", "Version", "Length", "AND", "OR", "NOT",
                      "Set", "BitWiseNot", "BoolVal", "StringVal", "UnIntVal",
                      "ToUpper", "ToLower", "Match", "Match2", "Catenate",
                      "QuestionRefVal", "StringRefVal", "Map", "RefreshGuid",
                      "StringToken", "OptionDefault", "OptionDefaultMfg",
                      "NumericSizeOne", "NumericSizeTwo", "NumericSizeFour",
                      "NumericSizeEight", "DisPlayIntDec", "DisPlayUIntDec",
                      "DisPlayUIntHex", "Insensitive", "Sensitive", "LastNonMatch",
                      "FirstNonMatch", "Number", "StringIdentifier", "ComplexDefine",
                      "LineDefinition", "IncludeDefinition", "Whitespace",
                      "Newline", "LineComment", "Extern" ]

    RULE_vfrProgram = 0
    RULE_vfrHeader = 1
    RULE_pragmaPackShowDef = 2
    RULE_pragmaPackStackDef = 3
    RULE_pragmaPackNumber = 4
    RULE_vfrPragmaPackDefinition = 5
    RULE_vfrDataStructDefinition = 6
    RULE_vfrDataUnionDefinition = 7
    RULE_vfrDataStructFields = 8
    RULE_dataStructField64 = 9
    RULE_dataStructField32 = 10
    RULE_dataStructField16 = 11
    RULE_dataStructField8 = 12
    RULE_dataStructFieldBool = 13
    RULE_dataStructFieldString = 14
    RULE_dataStructFieldDate = 15
    RULE_dataStructFieldTime = 16
    RULE_dataStructFieldRef = 17
    RULE_dataStructFieldUser = 18
    RULE_dataStructBitField64 = 19
    RULE_dataStructBitField32 = 20
    RULE_dataStructBitField16 = 21
    RULE_dataStructBitField8 = 22
    RULE_vfrFormSetDefinition = 23
    RULE_classguidDefinition = 24
    RULE_guidSubDefinition = 25
    RULE_guidDefinition = 26
    RULE_classDefinition = 27
    RULE_validClassNames = 28
    RULE_subclassDefinition = 29
    RULE_vfrFormSetList = 30
    RULE_vfrFormSet = 31
    RULE_vfrStatementDefaultStore = 32
    RULE_vfrStatementVarStoreLinear = 33
    RULE_vfrStatementVarStoreEfi = 34
    RULE_vfrVarStoreEfiAttr = 35
    RULE_vfrStatementVarStoreNameValue = 36
    RULE_vfrStatementDisableIfFormSet = 37
    RULE_vfrStatementSuppressIfFormSet = 38
    RULE_getStringId = 39
    RULE_vfrQuestionHeader = 40
    RULE_vfrQuestionBaseInfo = 41
    RULE_vfrStatementHeader = 42
    RULE_questionheaderFlagsField = 43
    RULE_vfrStorageVarId = 44
    RULE_vfrConstantValueField = 45
    RULE_vfrImageTag = 46
    RULE_vfrLockedTag = 47
    RULE_vfrStatementStatTag = 48
    RULE_vfrStatementStatTagList = 49
    RULE_vfrFormDefinition = 50
    RULE_vfrForm = 51
    RULE_vfrFormMapDefinition = 52
    RULE_vfrStatementImage = 53
    RULE_vfrStatementLocked = 54
    RULE_vfrStatementRules = 55
    RULE_vfrStatementStat = 56
    RULE_vfrStatementSubTitle = 57
    RULE_vfrStatementSubTitleComponent = 58
    RULE_vfrSubtitleFlags = 59
    RULE_subtitleFlagsField = 60
    RULE_vfrStatementStaticText = 61
    RULE_staticTextFlagsField = 62
    RULE_vfrStatementCrossReference = 63
    RULE_vfrStatementGoto = 64
    RULE_vfrGotoFlags = 65
    RULE_gotoFlagsField = 66
    RULE_vfrStatementResetButton = 67
    RULE_vfrStatementQuestions = 68
    RULE_vfrStatementQuestionTag = 69
    RULE_vfrStatementInconsistentIf = 70
    RULE_vfrStatementNoSubmitIf = 71
    RULE_vfrStatementDisableIfQuest = 72
    RULE_vfrStatementRefresh = 73
    RULE_vfrStatementVarstoreDevice = 74
    RULE_vfrStatementRefreshEvent = 75
    RULE_vfrStatementWarningIf = 76
    RULE_vfrStatementQuestionTagList = 77
    RULE_vfrStatementQuestionOptionTag = 78
    RULE_flagsField = 79
    RULE_vfrStatementSuppressIfQuest = 80
    RULE_vfrStatementGrayOutIfQuest = 81
    RULE_vfrStatementDefault = 82
    RULE_vfrStatementValue = 83
    RULE_vfrStatementOptions = 84
    RULE_vfrStatementOneOfOption = 85
    RULE_vfrOneOfOptionFlags = 86
    RULE_oneofoptionFlagsField = 87
    RULE_vfrStatementRead = 88
    RULE_vfrStatementWrite = 89
    RULE_vfrStatementQuestionOptionList = 90
    RULE_vfrStatementQuestionOption = 91
    RULE_vfrStatementBooleanType = 92
    RULE_vfrStatementCheckBox = 93
    RULE_vfrCheckBoxFlags = 94
    RULE_checkboxFlagsField = 95
    RULE_vfrStatementAction = 96
    RULE_vfrActionFlags = 97
    RULE_actionFlagsField = 98
    RULE_vfrStatementNumericType = 99
    RULE_vfrStatementNumeric = 100
    RULE_vfrSetMinMaxStep = 101
    RULE_vfrNumericFlags = 102
    RULE_numericFlagsField = 103
    RULE_vfrStatementOneOf = 104
    RULE_vfrOneofFlagsField = 105
    RULE_vfrStatementStringType = 106
    RULE_vfrStatementString = 107
    RULE_vfrStringFlagsField = 108
    RULE_stringFlagsField = 109
    RULE_vfrStatementPassword = 110
    RULE_vfrPasswordFlagsField = 111
    RULE_passwordFlagsField = 112
    RULE_vfrStatementOrderedList = 113
    RULE_vfrOrderedListFlags = 114
    RULE_orderedlistFlagsField = 115
    RULE_vfrStatementDate = 116
    RULE_minMaxDateStepDefault = 117
    RULE_vfrDateFlags = 118
    RULE_dateFlagsField = 119
    RULE_vfrStatementTime = 120
    RULE_minMaxTimeStepDefault = 121
    RULE_vfrTimeFlags = 122
    RULE_timeFlagsField = 123
    RULE_vfrStatementConditional = 124
    RULE_vfrStatementConditionalNew = 125
    RULE_vfrStatementSuppressIfStat = 126
    RULE_vfrStatementGrayOutIfStat = 127
    RULE_vfrStatementStatList = 128
    RULE_vfrStatementStatListOld = 129
    RULE_vfrStatementDisableIfStat = 130
    RULE_vfrStatementgrayoutIfSuppressIf = 131
    RULE_vfrStatementsuppressIfGrayOutIf = 132
    RULE_vfrStatementSuppressIfStatNew = 133
    RULE_vfrStatementGrayOutIfStatNew = 134
    RULE_vfrStatementInconsistentIfStat = 135
    RULE_vfrStatementInvalid = 136
    RULE_vfrStatementInvalidHidden = 137
    RULE_vfrStatementInvalidInventory = 138
    RULE_vfrStatementInvalidSaveRestoreDefaults = 139
    RULE_vfrStatementLabel = 140
    RULE_vfrStatementBanner = 141
    RULE_vfrStatementExtension = 142
    RULE_vfrExtensionData = 143
    RULE_vfrStatementModal = 144
    RULE_vfrModalTag = 145
    RULE_vfrStatementExpression = 146
    RULE_vfrStatementExpressionSub = 147
    RULE_andTerm = 148
    RULE_bitwiseorTerm = 149
    RULE_bitwiseandTerm = 150
    RULE_equalTerm = 151
    RULE_equalTermSupplementary = 152
    RULE_compareTerm = 153
    RULE_compareTermSupplementary = 154
    RULE_shiftTerm = 155
    RULE_shiftTermSupplementary = 156
    RULE_addMinusTerm = 157
    RULE_addMinusTermSupplementary = 158
    RULE_multdivmodTerm = 159
    RULE_multdivmodTermSupplementary = 160
    RULE_castTerm = 161
    RULE_castTermSub = 162
    RULE_atomTerm = 163
    RULE_vfrExpressionCatenate = 164
    RULE_vfrExpressionMatch = 165
    RULE_vfrExpressionMatch2 = 166
    RULE_vfrExpressionParen = 167
    RULE_vfrExpressionBuildInFunction = 168
    RULE_dupExp = 169
    RULE_vareqvalExp = 170
    RULE_ideqvalExp = 171
    RULE_ideqidExp = 172
    RULE_ideqvallistExp = 173
    RULE_vfrQuestionDataFieldName = 174
    RULE_arrayName = 175
    RULE_questionref1Exp = 176
    RULE_rulerefExp = 177
    RULE_stringref1Exp = 178
    RULE_pushthisExp = 179
    RULE_securityExp = 180
    RULE_numericVarStoreType = 181
    RULE_getExp = 182
    RULE_vfrExpressionConstant = 183
    RULE_vfrExpressionUnaryOp = 184
    RULE_lengthExp = 185
    RULE_bitwisenotExp = 186
    RULE_question23refExp = 187
    RULE_stringref2Exp = 188
    RULE_toboolExp = 189
    RULE_tostringExp = 190
    RULE_unintExp = 191
    RULE_toupperExp = 192
    RULE_tolwerExp = 193
    RULE_setExp = 194
    RULE_vfrExpressionTernaryOp = 195
    RULE_conditionalExp = 196
    RULE_findExp = 197
    RULE_findFormat = 198
    RULE_midExp = 199
    RULE_tokenExp = 200
    RULE_spanExp = 201
    RULE_spanFlags = 202
    RULE_vfrExpressionMap = 203

    ruleNames =  [ "vfrProgram", "vfrHeader", "pragmaPackShowDef", "pragmaPackStackDef",
                   "pragmaPackNumber", "vfrPragmaPackDefinition", "vfrDataStructDefinition",
                   "vfrDataUnionDefinition", "vfrDataStructFields", "dataStructField64",
                   "dataStructField32", "dataStructField16", "dataStructField8",
                   "dataStructFieldBool", "dataStructFieldString", "dataStructFieldDate",
                   "dataStructFieldTime", "dataStructFieldRef", "dataStructFieldUser",
                   "dataStructBitField64", "dataStructBitField32", "dataStructBitField16",
                   "dataStructBitField8", "vfrFormSetDefinition", "classguidDefinition",
                   "guidSubDefinition", "guidDefinition", "classDefinition",
                   "validClassNames", "subclassDefinition", "vfrFormSetList",
                   "vfrFormSet", "vfrStatementDefaultStore", "vfrStatementVarStoreLinear",
                   "vfrStatementVarStoreEfi", "vfrVarStoreEfiAttr", "vfrStatementVarStoreNameValue",
                   "vfrStatementDisableIfFormSet", "vfrStatementSuppressIfFormSet",
                   "getStringId", "vfrQuestionHeader", "vfrQuestionBaseInfo",
                   "vfrStatementHeader", "questionheaderFlagsField", "vfrStorageVarId",
                   "vfrConstantValueField", "vfrImageTag", "vfrLockedTag",
                   "vfrStatementStatTag", "vfrStatementStatTagList", "vfrFormDefinition",
                   "vfrForm", "vfrFormMapDefinition", "vfrStatementImage",
                   "vfrStatementLocked", "vfrStatementRules", "vfrStatementStat",
                   "vfrStatementSubTitle", "vfrStatementSubTitleComponent",
                   "vfrSubtitleFlags", "subtitleFlagsField", "vfrStatementStaticText",
                   "staticTextFlagsField", "vfrStatementCrossReference",
                   "vfrStatementGoto", "vfrGotoFlags", "gotoFlagsField",
                   "vfrStatementResetButton", "vfrStatementQuestions", "vfrStatementQuestionTag",
                   "vfrStatementInconsistentIf", "vfrStatementNoSubmitIf",
                   "vfrStatementDisableIfQuest", "vfrStatementRefresh",
                   "vfrStatementVarstoreDevice", "vfrStatementRefreshEvent",
                   "vfrStatementWarningIf", "vfrStatementQuestionTagList",
                   "vfrStatementQuestionOptionTag", "flagsField", "vfrStatementSuppressIfQuest",
                   "vfrStatementGrayOutIfQuest", "vfrStatementDefault",
                   "vfrStatementValue", "vfrStatementOptions", "vfrStatementOneOfOption",
                   "vfrOneOfOptionFlags", "oneofoptionFlagsField", "vfrStatementRead",
                   "vfrStatementWrite", "vfrStatementQuestionOptionList",
                   "vfrStatementQuestionOption", "vfrStatementBooleanType",
                   "vfrStatementCheckBox", "vfrCheckBoxFlags", "checkboxFlagsField",
                   "vfrStatementAction", "vfrActionFlags", "actionFlagsField",
                   "vfrStatementNumericType", "vfrStatementNumeric", "vfrSetMinMaxStep",
                   "vfrNumericFlags", "numericFlagsField", "vfrStatementOneOf",
                   "vfrOneofFlagsField", "vfrStatementStringType", "vfrStatementString",
                   "vfrStringFlagsField", "stringFlagsField", "vfrStatementPassword",
                   "vfrPasswordFlagsField", "passwordFlagsField", "vfrStatementOrderedList",
                   "vfrOrderedListFlags", "orderedlistFlagsField", "vfrStatementDate",
                   "minMaxDateStepDefault", "vfrDateFlags", "dateFlagsField",
                   "vfrStatementTime", "minMaxTimeStepDefault", "vfrTimeFlags",
                   "timeFlagsField", "vfrStatementConditional", "vfrStatementConditionalNew",
                   "vfrStatementSuppressIfStat", "vfrStatementGrayOutIfStat",
                   "vfrStatementStatList", "vfrStatementStatListOld", "vfrStatementDisableIfStat",
                   "vfrStatementgrayoutIfSuppressIf", "vfrStatementsuppressIfGrayOutIf",
                   "vfrStatementSuppressIfStatNew", "vfrStatementGrayOutIfStatNew",
                   "vfrStatementInconsistentIfStat", "vfrStatementInvalid",
                   "vfrStatementInvalidHidden", "vfrStatementInvalidInventory",
                   "vfrStatementInvalidSaveRestoreDefaults", "vfrStatementLabel",
                   "vfrStatementBanner", "vfrStatementExtension", "vfrExtensionData",
                   "vfrStatementModal", "vfrModalTag", "vfrStatementExpression",
                   "vfrStatementExpressionSub", "andTerm", "bitwiseorTerm",
                   "bitwiseandTerm", "equalTerm", "equalTermSupplementary",
                   "compareTerm", "compareTermSupplementary", "shiftTerm",
                   "shiftTermSupplementary", "addMinusTerm", "addMinusTermSupplementary",
                   "multdivmodTerm", "multdivmodTermSupplementary", "castTerm",
                   "castTermSub", "atomTerm", "vfrExpressionCatenate", "vfrExpressionMatch",
                   "vfrExpressionMatch2", "vfrExpressionParen", "vfrExpressionBuildInFunction",
                   "dupExp", "vareqvalExp", "ideqvalExp", "ideqidExp", "ideqvallistExp",
                   "vfrQuestionDataFieldName", "arrayName", "questionref1Exp",
                   "rulerefExp", "stringref1Exp", "pushthisExp", "securityExp",
                   "numericVarStoreType", "getExp", "vfrExpressionConstant",
                   "vfrExpressionUnaryOp", "lengthExp", "bitwisenotExp",
                   "question23refExp", "stringref2Exp", "toboolExp", "tostringExp",
                   "unintExp", "toupperExp", "tolwerExp", "setExp", "vfrExpressionTernaryOp",
                   "conditionalExp", "findExp", "findFormat", "midExp",
                   "tokenExp", "spanExp", "spanFlags", "vfrExpressionMap" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    Define=17
    Include=18
    FormPkgType=19
    OpenBrace=20
    CloseBrace=21
    OpenParen=22
    CloseParen=23
    OpenBracket=24
    CloseBracket=25
    Dot=26
    Negative=27
    Colon=28
    Slash=29
    Semicolon=30
    Comma=31
    Equal=32
    NotEqual=33
    LessEqual=34
    Less=35
    GreaterEqual=36
    Greater=37
    BitWiseOr=38
    BitWiseAnd=39
    DevicePath=40
    FormSet=41
    FormSetId=42
    EndFormSet=43
    Title=44
    FormId=45
    OneOf=46
    EndOneOf=47
    Prompt=48
    OrderedList=49
    MaxContainers=50
    EndList=51
    EndForm=52
    Form=53
    FormMap=54
    MapTitle=55
    MapGuid=56
    Subtitle=57
    EndSubtitle=58
    Help=59
    Text=60
    Option=61
    FLAGS=62
    Date=63
    EndDate=64
    Year=65
    Month=66
    Day=67
    Time=68
    EndTime=69
    Hour=70
    Minute=71
    Second=72
    GrayOutIf=73
    Label=74
    Timeout=75
    Inventory=76
    NonNvDataMap=77
    Struct=78
    Union=79
    Boolean=80
    Uint64=81
    Uint32=82
    Uint16=83
    Uint8=84
    EFI_STRING_ID=85
    EFI_HII_DATE=86
    EFI_HII_TIME=87
    EFI_HII_REF=88
    Uuid=89
    CheckBox=90
    EndCheckBox=91
    Numeric=92
    EndNumeric=93
    Minimum=94
    Maximum=95
    Step=96
    Default=97
    Password=98
    EndPassword=99
    String=100
    EndString=101
    MinSize=102
    MaxSize=103
    Encoding=104
    SuppressIf=105
    DisableIf=106
    Hidden=107
    Goto=108
    FormSetGuid=109
    InconsistentIf=110
    WarningIf=111
    NoSubmitIf=112
    EndIf=113
    Key=114
    DefaultFlag=115
    ManufacturingFlag=116
    CheckBoxDefaultFlag=117
    CheckBoxDefaultMfgFlag=118
    InteractiveFlag=119
    NVAccessFlag=120
    ResetRequiredFlag=121
    ReconnectRequiredFlag=122
    LateCheckFlag=123
    ReadOnlyFlag=124
    OptionOnlyFlag=125
    RestStyleFlag=126
    Class=127
    Subclass=128
    ClassGuid=129
    TypeDef=130
    Restore=131
    Save=132
    Defaults=133
    Banner=134
    Align=135
    Left=136
    Right=137
    Center=138
    Line=139
    Name=140
    VarId=141
    Question=142
    QuestionId=143
    Image=144
    Locked=145
    Rule=146
    EndRule=147
    Value=148
    Read=149
    Write=150
    ResetButton=151
    EndResetButton=152
    DefaultStore=153
    Attribute=154
    Varstore=155
    Efivarstore=156
    VarSize=157
    NameValueVarStore=158
    Action=159
    Config=160
    EndAction=161
    Refresh=162
    Interval=163
    VarstoreDevice=164
    GuidOp=165
    EndGuidOp=166
    DataType=167
    Data=168
    Modal=169
    ClassNonDevice=170
    ClassDiskDevice=171
    ClassVideoDevice=172
    ClassNetworkDevice=173
    ClassInputDevice=174
    ClassOnBoardDevice=175
    ClassOtherDevice=176
    SubclassSetupApplication=177
    SubclassGeneralApplication=178
    SubclassFrontPage=179
    SubclassSingleUse=180
    YearSupppressFlag=181
    MonthSuppressFlag=182
    DaySuppressFlag=183
    HourSupppressFlag=184
    MinuteSuppressFlag=185
    SecondSuppressFlag=186
    StorageNormalFlag=187
    StorageTimeFlag=188
    StorageWakeUpFlag=189
    UniQueFlag=190
    NoEmptyFlag=191
    Cond=192
    Find=193
    Mid=194
    Tok=195
    Span=196
    Dup=197
    VarEqVal=198
    Var=199
    IdEqVal=200
    IdEqId=201
    IdEqValList=202
    QuestionRef=203
    RuleRef=204
    StringRef=205
    PushThis=206
    Security=207
    Get=208
    TrueSymbol=209
    FalseSymbol=210
    One=211
    Ones=212
    Zero=213
    Undefined=214
    Version=215
    Length=216
    AND=217
    OR=218
    NOT=219
    Set=220
    BitWiseNot=221
    BoolVal=222
    StringVal=223
    UnIntVal=224
    ToUpper=225
    ToLower=226
    Match=227
    Match2=228
    Catenate=229
    QuestionRefVal=230
    StringRefVal=231
    Map=232
    RefreshGuid=233
    StringToken=234
    OptionDefault=235
    OptionDefaultMfg=236
    NumericSizeOne=237
    NumericSizeTwo=238
    NumericSizeFour=239
    NumericSizeEight=240
    DisPlayIntDec=241
    DisPlayUIntDec=242
    DisPlayUIntHex=243
    Insensitive=244
    Sensitive=245
    LastNonMatch=246
    FirstNonMatch=247
    Number=248
    StringIdentifier=249
    ComplexDefine=250
    LineDefinition=251
    IncludeDefinition=252
    Whitespace=253
    Newline=254
    LineComment=255
    Extern=256

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class VfrProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vfrHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrHeaderContext,0)


        def vfrFormSetDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrFormSetDefinitionContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrProgram

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrProgram" ):
                return visitor.visitVfrProgram(self)
            else:
                return visitor.visitChildren(self)




    def vfrProgram(self):

        localctx = SourceVfrSyntaxParser.VfrProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_vfrProgram)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 408
                self.vfrHeader()


            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FormSet:
                self.state = 411
                self.vfrFormSetDefinition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrHeaderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vfrPragmaPackDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrPragmaPackDefinitionContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrPragmaPackDefinitionContext,i)


        def vfrDataStructDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrDataStructDefinitionContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrDataStructDefinitionContext,i)


        def vfrDataUnionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrDataUnionDefinitionContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrDataUnionDefinitionContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrHeader

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrHeader" ):
                return visitor.visitVfrHeader(self)
            else:
                return visitor.visitChildren(self)




    def vfrHeader(self):

        localctx = SourceVfrSyntaxParser.VfrHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vfrHeader)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.T__3 or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & ((1 << (SourceVfrSyntaxParser.Struct - 78)) | (1 << (SourceVfrSyntaxParser.Union - 78)) | (1 << (SourceVfrSyntaxParser.TypeDef - 78)))) != 0):
                self.state = 417
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 414
                    self.vfrPragmaPackDefinition()
                    pass

                elif la_ == 2:
                    self.state = 415
                    self.vfrDataStructDefinition()
                    pass

                elif la_ == 3:
                    self.state = 416
                    self.vfrDataUnionDefinition()
                    pass


                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PragmaPackShowDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_pragmaPackShowDef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragmaPackShowDef" ):
                return visitor.visitPragmaPackShowDef(self)
            else:
                return visitor.visitChildren(self)




    def pragmaPackShowDef(self):

        localctx = SourceVfrSyntaxParser.PragmaPackShowDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pragmaPackShowDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(SourceVfrSyntaxParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PragmaPackStackDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_pragmaPackStackDef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragmaPackStackDef" ):
                return visitor.visitPragmaPackStackDef(self)
            else:
                return visitor.visitChildren(self)




    def pragmaPackStackDef(self):

        localctx = SourceVfrSyntaxParser.PragmaPackStackDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pragmaPackStackDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            _la = self._input.LA(1)
            if not(_la==SourceVfrSyntaxParser.T__1 or _la==SourceVfrSyntaxParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 425
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 426
                self.match(SourceVfrSyntaxParser.StringIdentifier)


            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Comma:
                self.state = 429
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 430
                self.match(SourceVfrSyntaxParser.Number)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PragmaPackNumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_pragmaPackNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragmaPackNumber" ):
                return visitor.visitPragmaPackNumber(self)
            else:
                return visitor.visitChildren(self)




    def pragmaPackNumber(self):

        localctx = SourceVfrSyntaxParser.PragmaPackNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pragmaPackNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Number:
                self.state = 433
                self.match(SourceVfrSyntaxParser.Number)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrPragmaPackDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def pragmaPackShowDef(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.PragmaPackShowDefContext,0)


        def pragmaPackStackDef(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.PragmaPackStackDefContext,0)


        def pragmaPackNumber(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.PragmaPackNumberContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrPragmaPackDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrPragmaPackDefinition" ):
                return visitor.visitVfrPragmaPackDefinition(self)
            else:
                return visitor.visitChildren(self)




    def vfrPragmaPackDefinition(self):

        localctx = SourceVfrSyntaxParser.VfrPragmaPackDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vfrPragmaPackDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(SourceVfrSyntaxParser.T__3)
            self.state = 437
            self.match(SourceVfrSyntaxParser.T__4)
            self.state = 438
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 439
                self.pragmaPackShowDef()

            elif la_ == 2:
                self.state = 440
                self.pragmaPackStackDef()

            elif la_ == 3:
                self.state = 441
                self.pragmaPackNumber()


            self.state = 444
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrDataStructDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.N1 = None # Token
            self.N2 = None # Token

        def Struct(self):
            return self.getToken(SourceVfrSyntaxParser.Struct, 0)

        def OpenBrace(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBrace, 0)

        def vfrDataStructFields(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrDataStructFieldsContext,0)


        def CloseBrace(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBrace, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def TypeDef(self):
            return self.getToken(SourceVfrSyntaxParser.TypeDef, 0)

        def NonNvDataMap(self):
            return self.getToken(SourceVfrSyntaxParser.NonNvDataMap, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrDataStructDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrDataStructDefinition" ):
                return visitor.visitVfrDataStructDefinition(self)
            else:
                return visitor.visitChildren(self)




    def vfrDataStructDefinition(self):

        localctx = SourceVfrSyntaxParser.VfrDataStructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vfrDataStructDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.TypeDef:
                self.state = 446
                self.match(SourceVfrSyntaxParser.TypeDef)


            self.state = 449
            self.match(SourceVfrSyntaxParser.Struct)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.NonNvDataMap:
                self.state = 450
                self.match(SourceVfrSyntaxParser.NonNvDataMap)


            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 453
                localctx.N1 = self.match(SourceVfrSyntaxParser.StringIdentifier)


            self.state = 456
            self.match(SourceVfrSyntaxParser.OpenBrace)
            self.state = 457
            self.vfrDataStructFields(False)
            self.state = 458
            self.match(SourceVfrSyntaxParser.CloseBrace)
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 459
                localctx.N2 = self.match(SourceVfrSyntaxParser.StringIdentifier)


            self.state = 462
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrDataUnionDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.N1 = None # Token
            self.N2 = None # Token

        def Union(self):
            return self.getToken(SourceVfrSyntaxParser.Union, 0)

        def OpenBrace(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBrace, 0)

        def vfrDataStructFields(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrDataStructFieldsContext,0)


        def CloseBrace(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBrace, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def TypeDef(self):
            return self.getToken(SourceVfrSyntaxParser.TypeDef, 0)

        def NonNvDataMap(self):
            return self.getToken(SourceVfrSyntaxParser.NonNvDataMap, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrDataUnionDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrDataUnionDefinition" ):
                return visitor.visitVfrDataUnionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def vfrDataUnionDefinition(self):

        localctx = SourceVfrSyntaxParser.VfrDataUnionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vfrDataUnionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.TypeDef:
                self.state = 464
                self.match(SourceVfrSyntaxParser.TypeDef)


            self.state = 467
            self.match(SourceVfrSyntaxParser.Union)
            self.state = 469
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.NonNvDataMap:
                self.state = 468
                self.match(SourceVfrSyntaxParser.NonNvDataMap)


            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 471
                localctx.N1 = self.match(SourceVfrSyntaxParser.StringIdentifier)


            self.state = 474
            self.match(SourceVfrSyntaxParser.OpenBrace)
            self.state = 475
            self.vfrDataStructFields(True)
            self.state = 476
            self.match(SourceVfrSyntaxParser.CloseBrace)
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 477
                localctx.N2 = self.match(SourceVfrSyntaxParser.StringIdentifier)


            self.state = 480
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrDataStructFieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.FieldInUnion = FieldInUnion

        def dataStructField64(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructField64Context)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructField64Context,i)


        def dataStructField32(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructField32Context)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructField32Context,i)


        def dataStructField16(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructField16Context)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructField16Context,i)


        def dataStructField8(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructField8Context)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructField8Context,i)


        def dataStructFieldBool(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructFieldBoolContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructFieldBoolContext,i)


        def dataStructFieldString(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructFieldStringContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructFieldStringContext,i)


        def dataStructFieldDate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructFieldDateContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructFieldDateContext,i)


        def dataStructFieldTime(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructFieldTimeContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructFieldTimeContext,i)


        def dataStructFieldRef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructFieldRefContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructFieldRefContext,i)


        def dataStructFieldUser(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructFieldUserContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructFieldUserContext,i)


        def dataStructBitField64(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructBitField64Context)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructBitField64Context,i)


        def dataStructBitField32(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructBitField32Context)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructBitField32Context,i)


        def dataStructBitField16(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructBitField16Context)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructBitField16Context,i)


        def dataStructBitField8(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DataStructBitField8Context)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DataStructBitField8Context,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrDataStructFields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrDataStructFields" ):
                return visitor.visitVfrDataStructFields(self)
            else:
                return visitor.visitChildren(self)




    def vfrDataStructFields(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.VfrDataStructFieldsContext(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 16, self.RULE_vfrDataStructFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (SourceVfrSyntaxParser.Boolean - 80)) | (1 << (SourceVfrSyntaxParser.Uint64 - 80)) | (1 << (SourceVfrSyntaxParser.Uint32 - 80)) | (1 << (SourceVfrSyntaxParser.Uint16 - 80)) | (1 << (SourceVfrSyntaxParser.Uint8 - 80)) | (1 << (SourceVfrSyntaxParser.EFI_STRING_ID - 80)) | (1 << (SourceVfrSyntaxParser.EFI_HII_DATE - 80)) | (1 << (SourceVfrSyntaxParser.EFI_HII_TIME - 80)) | (1 << (SourceVfrSyntaxParser.EFI_HII_REF - 80)))) != 0) or _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 496
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 482
                    self.dataStructField64(FieldInUnion)
                    pass

                elif la_ == 2:
                    self.state = 483
                    self.dataStructField32(FieldInUnion)
                    pass

                elif la_ == 3:
                    self.state = 484
                    self.dataStructField16(FieldInUnion)
                    pass

                elif la_ == 4:
                    self.state = 485
                    self.dataStructField8(FieldInUnion)
                    pass

                elif la_ == 5:
                    self.state = 486
                    self.dataStructFieldBool(FieldInUnion)
                    pass

                elif la_ == 6:
                    self.state = 487
                    self.dataStructFieldString(FieldInUnion)
                    pass

                elif la_ == 7:
                    self.state = 488
                    self.dataStructFieldDate(FieldInUnion)
                    pass

                elif la_ == 8:
                    self.state = 489
                    self.dataStructFieldTime(FieldInUnion)
                    pass

                elif la_ == 9:
                    self.state = 490
                    self.dataStructFieldRef(FieldInUnion)
                    pass

                elif la_ == 10:
                    self.state = 491
                    self.dataStructFieldUser(FieldInUnion)
                    pass

                elif la_ == 11:
                    self.state = 492
                    self.dataStructBitField64(FieldInUnion)
                    pass

                elif la_ == 12:
                    self.state = 493
                    self.dataStructBitField32(FieldInUnion)
                    pass

                elif la_ == 13:
                    self.state = 494
                    self.dataStructBitField16(FieldInUnion)
                    pass

                elif la_ == 14:
                    self.state = 495
                    self.dataStructBitField8(FieldInUnion)
                    pass


                self.state = 500
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructField64Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Uint64(self):
            return self.getToken(SourceVfrSyntaxParser.Uint64, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructField64

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructField64" ):
                return visitor.visitDataStructField64(self)
            else:
                return visitor.visitChildren(self)




    def dataStructField64(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructField64Context(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 18, self.RULE_dataStructField64)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(SourceVfrSyntaxParser.Uint64)
            self.state = 502
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 503
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 504
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 505
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 508
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructField32Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Uint32(self):
            return self.getToken(SourceVfrSyntaxParser.Uint32, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructField32

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructField32" ):
                return visitor.visitDataStructField32(self)
            else:
                return visitor.visitChildren(self)




    def dataStructField32(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructField32Context(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 20, self.RULE_dataStructField32)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(SourceVfrSyntaxParser.Uint32)
            self.state = 511
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 512
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 513
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 514
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 517
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructField16Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Uint16(self):
            return self.getToken(SourceVfrSyntaxParser.Uint16, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructField16

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructField16" ):
                return visitor.visitDataStructField16(self)
            else:
                return visitor.visitChildren(self)




    def dataStructField16(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructField16Context(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 22, self.RULE_dataStructField16)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(SourceVfrSyntaxParser.Uint16)
            self.state = 520
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 521
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 522
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 523
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 526
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructField8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Uint8(self):
            return self.getToken(SourceVfrSyntaxParser.Uint8, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructField8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructField8" ):
                return visitor.visitDataStructField8(self)
            else:
                return visitor.visitChildren(self)




    def dataStructField8(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructField8Context(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 24, self.RULE_dataStructField8)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(SourceVfrSyntaxParser.Uint8)
            self.state = 529
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 533
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 530
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 531
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 532
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 535
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructFieldBoolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Boolean(self):
            return self.getToken(SourceVfrSyntaxParser.Boolean, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructFieldBool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructFieldBool" ):
                return visitor.visitDataStructFieldBool(self)
            else:
                return visitor.visitChildren(self)




    def dataStructFieldBool(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructFieldBoolContext(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 26, self.RULE_dataStructFieldBool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(SourceVfrSyntaxParser.Boolean)
            self.state = 538
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 539
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 540
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 541
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 544
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructFieldStringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def EFI_STRING_ID(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_STRING_ID, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructFieldString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructFieldString" ):
                return visitor.visitDataStructFieldString(self)
            else:
                return visitor.visitChildren(self)




    def dataStructFieldString(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructFieldStringContext(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 28, self.RULE_dataStructFieldString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.match(SourceVfrSyntaxParser.EFI_STRING_ID)
            self.state = 547
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 551
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 548
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 549
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 550
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 553
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructFieldDateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def EFI_HII_DATE(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_DATE, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructFieldDate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructFieldDate" ):
                return visitor.visitDataStructFieldDate(self)
            else:
                return visitor.visitChildren(self)




    def dataStructFieldDate(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructFieldDateContext(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 30, self.RULE_dataStructFieldDate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(SourceVfrSyntaxParser.EFI_HII_DATE)
            self.state = 556
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 560
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 557
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 558
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 559
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 562
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructFieldTimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def EFI_HII_TIME(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_TIME, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructFieldTime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructFieldTime" ):
                return visitor.visitDataStructFieldTime(self)
            else:
                return visitor.visitChildren(self)




    def dataStructFieldTime(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructFieldTimeContext(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 32, self.RULE_dataStructFieldTime)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(SourceVfrSyntaxParser.EFI_HII_TIME)
            self.state = 565
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 569
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 566
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 567
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 568
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 571
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructFieldRefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def EFI_HII_REF(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_REF, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructFieldRef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructFieldRef" ):
                return visitor.visitDataStructFieldRef(self)
            else:
                return visitor.visitChildren(self)




    def dataStructFieldRef(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructFieldRefContext(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 34, self.RULE_dataStructFieldRef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.match(SourceVfrSyntaxParser.EFI_HII_REF)
            self.state = 574
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 578
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 575
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 576
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 577
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 580
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructFieldUserContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.T = None # Token
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructFieldUser

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructFieldUser" ):
                return visitor.visitDataStructFieldUser(self)
            else:
                return visitor.visitChildren(self)




    def dataStructFieldUser(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructFieldUserContext(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 36, self.RULE_dataStructFieldUser)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            localctx.T = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 583
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 587
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 584
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 585
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 586
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 589
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructBitField64Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.D = None # Token
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Colon(self):
            return self.getToken(SourceVfrSyntaxParser.Colon, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Uint64(self):
            return self.getToken(SourceVfrSyntaxParser.Uint64, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructBitField64

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructBitField64" ):
                return visitor.visitDataStructBitField64(self)
            else:
                return visitor.visitChildren(self)




    def dataStructBitField64(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructBitField64Context(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 38, self.RULE_dataStructBitField64)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            localctx.D = self.match(SourceVfrSyntaxParser.Uint64)
            self.state = 593
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 592
                localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)


            self.state = 595
            self.match(SourceVfrSyntaxParser.Colon)
            self.state = 596
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 597
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructBitField32Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.D = None # Token
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Colon(self):
            return self.getToken(SourceVfrSyntaxParser.Colon, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Uint32(self):
            return self.getToken(SourceVfrSyntaxParser.Uint32, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructBitField32

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructBitField32" ):
                return visitor.visitDataStructBitField32(self)
            else:
                return visitor.visitChildren(self)




    def dataStructBitField32(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructBitField32Context(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 40, self.RULE_dataStructBitField32)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            localctx.D = self.match(SourceVfrSyntaxParser.Uint32)
            self.state = 601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 600
                localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)


            self.state = 603
            self.match(SourceVfrSyntaxParser.Colon)
            self.state = 604
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 605
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructBitField16Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.D = None # Token
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Colon(self):
            return self.getToken(SourceVfrSyntaxParser.Colon, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Uint16(self):
            return self.getToken(SourceVfrSyntaxParser.Uint16, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructBitField16

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructBitField16" ):
                return visitor.visitDataStructBitField16(self)
            else:
                return visitor.visitChildren(self)




    def dataStructBitField16(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructBitField16Context(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 42, self.RULE_dataStructBitField16)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            localctx.D = self.match(SourceVfrSyntaxParser.Uint16)
            self.state = 609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 608
                localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)


            self.state = 611
            self.match(SourceVfrSyntaxParser.Colon)
            self.state = 612
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 613
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStructBitField8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, FieldInUnion=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.FieldInUnion = None
            self.D = None # Token
            self.N = None # Token
            self.FieldInUnion = FieldInUnion

        def Colon(self):
            return self.getToken(SourceVfrSyntaxParser.Colon, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Uint8(self):
            return self.getToken(SourceVfrSyntaxParser.Uint8, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dataStructBitField8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStructBitField8" ):
                return visitor.visitDataStructBitField8(self)
            else:
                return visitor.visitChildren(self)




    def dataStructBitField8(self, FieldInUnion):

        localctx = SourceVfrSyntaxParser.DataStructBitField8Context(self, self._ctx, self.state, FieldInUnion)
        self.enterRule(localctx, 44, self.RULE_dataStructBitField8)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            localctx.D = self.match(SourceVfrSyntaxParser.Uint8)
            self.state = 617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 616
                localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)


            self.state = 619
            self.match(SourceVfrSyntaxParser.Colon)
            self.state = 620
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 621
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrFormSetDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_FORM_SET_OP)
            self.S1 = None # GuidDefinitionContext
            self.S2 = None # Token
            self.S3 = None # Token

        def FormSet(self):
            return self.getToken(SourceVfrSyntaxParser.FormSet, 0)

        def Uuid(self):
            return self.getToken(SourceVfrSyntaxParser.Uuid, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Title(self):
            return self.getToken(SourceVfrSyntaxParser.Title, 0)

        def StringToken(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringToken)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringToken, i)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def Help(self):
            return self.getToken(SourceVfrSyntaxParser.Help, 0)

        def vfrFormSetList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrFormSetListContext,0)


        def EndFormSet(self):
            return self.getToken(SourceVfrSyntaxParser.EndFormSet, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def ClassGuid(self):
            return self.getToken(SourceVfrSyntaxParser.ClassGuid, 0)

        def classguidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ClassguidDefinitionContext,0)


        def Class(self):
            return self.getToken(SourceVfrSyntaxParser.Class, 0)

        def classDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ClassDefinitionContext,0)


        def Subclass(self):
            return self.getToken(SourceVfrSyntaxParser.Subclass, 0)

        def subclassDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.SubclassDefinitionContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrFormSetDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrFormSetDefinition" ):
                return visitor.visitVfrFormSetDefinition(self)
            else:
                return visitor.visitChildren(self)




    def vfrFormSetDefinition(self):

        localctx = SourceVfrSyntaxParser.VfrFormSetDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_vfrFormSetDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.match(SourceVfrSyntaxParser.FormSet)
            self.state = 624
            self.match(SourceVfrSyntaxParser.Uuid)
            self.state = 625
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 626
            localctx.S1 = self.guidDefinition()
            self.state = 627
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 628
            self.match(SourceVfrSyntaxParser.Title)
            self.state = 629
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 630
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 631
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 632
            localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 633
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 634
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 635
            self.match(SourceVfrSyntaxParser.Help)
            self.state = 636
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 637
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 638
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 639
            localctx.S3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 640
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 641
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 647
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.ClassGuid:
                self.state = 642
                self.match(SourceVfrSyntaxParser.ClassGuid)
                self.state = 643
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 644
                self.classguidDefinition(localctx.Node)
                self.state = 645
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 654
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Class:
                self.state = 649
                self.match(SourceVfrSyntaxParser.Class)
                self.state = 650
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 651
                self.classDefinition()
                self.state = 652
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 661
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Subclass:
                self.state = 656
                self.match(SourceVfrSyntaxParser.Subclass)
                self.state = 657
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 658
                self.subclassDefinition()
                self.state = 659
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 663
            self.vfrFormSetList(localctx.Node)
            self.state = 664
            self.match(SourceVfrSyntaxParser.EndFormSet)
            self.state = 665
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassguidDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.GuidList = []
            self.Node = Node

        def guidDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.GuidDefinitionContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_classguidDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassguidDefinition" ):
                return visitor.visitClassguidDefinition(self)
            else:
                return visitor.visitChildren(self)




    def classguidDefinition(self, Node):

        localctx = SourceVfrSyntaxParser.ClassguidDefinitionContext(self, self._ctx, self.state, Node)
        self.enterRule(localctx, 48, self.RULE_classguidDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.guidDefinition()
            self.state = 670
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 668
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 669
                self.guidDefinition()


            self.state = 674
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 672
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 673
                self.guidDefinition()


            self.state = 678
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 676
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 677
                self.guidDefinition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GuidSubDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Guid=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Guid = None
            self.Guid = Guid

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_guidSubDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGuidSubDefinition" ):
                return visitor.visitGuidSubDefinition(self)
            else:
                return visitor.visitChildren(self)




    def guidSubDefinition(self, Guid):

        localctx = SourceVfrSyntaxParser.GuidSubDefinitionContext(self, self._ctx, self.state, Guid)
        self.enterRule(localctx, 50, self.RULE_guidSubDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 681
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 682
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 683
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 684
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 685
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 686
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 687
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 688
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 689
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 690
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 691
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 692
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 693
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 694
            self.match(SourceVfrSyntaxParser.Number)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GuidDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Guid = EFI_GUID()

        def OpenBrace(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenBrace)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenBrace, i)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def CloseBrace(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseBrace)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseBrace, i)

        def guidSubDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidSubDefinitionContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_guidDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGuidDefinition" ):
                return visitor.visitGuidDefinition(self)
            else:
                return visitor.visitChildren(self)




    def guidDefinition(self):

        localctx = SourceVfrSyntaxParser.GuidDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_guidDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            self.match(SourceVfrSyntaxParser.OpenBrace)
            self.state = 697
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 698
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 699
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 700
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 701
            self.match(SourceVfrSyntaxParser.Number)
            self.state = 702
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 708
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.OpenBrace]:
                self.state = 703
                self.match(SourceVfrSyntaxParser.OpenBrace)
                self.state = 704
                self.guidSubDefinition(localctx.Guid)
                self.state = 705
                self.match(SourceVfrSyntaxParser.CloseBrace)
                pass
            elif token in [SourceVfrSyntaxParser.Number]:
                self.state = 707
                self.guidSubDefinition(localctx.Guid)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 710
            self.match(SourceVfrSyntaxParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_GUID_OP)

        def validClassNames(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.ValidClassNamesContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.ValidClassNamesContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_classDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDefinition" ):
                return visitor.visitClassDefinition(self)
            else:
                return visitor.visitChildren(self)




    def classDefinition(self):

        localctx = SourceVfrSyntaxParser.ClassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.validClassNames()
            self.state = 717
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 713
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 714
                self.validClassNames()
                self.state = 719
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValidClassNamesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ClassName = 0
            self.S = None # Token

        def ClassNonDevice(self):
            return self.getToken(SourceVfrSyntaxParser.ClassNonDevice, 0)

        def ClassDiskDevice(self):
            return self.getToken(SourceVfrSyntaxParser.ClassDiskDevice, 0)

        def ClassVideoDevice(self):
            return self.getToken(SourceVfrSyntaxParser.ClassVideoDevice, 0)

        def ClassNetworkDevice(self):
            return self.getToken(SourceVfrSyntaxParser.ClassNetworkDevice, 0)

        def ClassInputDevice(self):
            return self.getToken(SourceVfrSyntaxParser.ClassInputDevice, 0)

        def ClassOnBoardDevice(self):
            return self.getToken(SourceVfrSyntaxParser.ClassOnBoardDevice, 0)

        def ClassOtherDevice(self):
            return self.getToken(SourceVfrSyntaxParser.ClassOtherDevice, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_validClassNames

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValidClassNames" ):
                return visitor.visitValidClassNames(self)
            else:
                return visitor.visitChildren(self)




    def validClassNames(self):

        localctx = SourceVfrSyntaxParser.ValidClassNamesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_validClassNames)
        try:
            self.state = 729
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.ClassNonDevice]:
                self.enterOuterAlt(localctx, 1)
                self.state = 720
                self.match(SourceVfrSyntaxParser.ClassNonDevice)
                pass
            elif token in [SourceVfrSyntaxParser.ClassDiskDevice]:
                self.enterOuterAlt(localctx, 2)
                self.state = 721
                self.match(SourceVfrSyntaxParser.ClassDiskDevice)
                pass
            elif token in [SourceVfrSyntaxParser.ClassVideoDevice]:
                self.enterOuterAlt(localctx, 3)
                self.state = 722
                self.match(SourceVfrSyntaxParser.ClassVideoDevice)
                pass
            elif token in [SourceVfrSyntaxParser.ClassNetworkDevice]:
                self.enterOuterAlt(localctx, 4)
                self.state = 723
                self.match(SourceVfrSyntaxParser.ClassNetworkDevice)
                pass
            elif token in [SourceVfrSyntaxParser.ClassInputDevice]:
                self.enterOuterAlt(localctx, 5)
                self.state = 724
                self.match(SourceVfrSyntaxParser.ClassInputDevice)
                pass
            elif token in [SourceVfrSyntaxParser.ClassOnBoardDevice]:
                self.enterOuterAlt(localctx, 6)
                self.state = 725
                self.match(SourceVfrSyntaxParser.ClassOnBoardDevice)
                pass
            elif token in [SourceVfrSyntaxParser.ClassOtherDevice]:
                self.enterOuterAlt(localctx, 7)
                self.state = 726
                self.match(SourceVfrSyntaxParser.ClassOtherDevice)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 8)
                self.state = 727
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            elif token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 9)
                self.state = 728
                self.match(SourceVfrSyntaxParser.Number)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubclassDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_GUID_OP)
            self.S = None # Token

        def SubclassSetupApplication(self):
            return self.getToken(SourceVfrSyntaxParser.SubclassSetupApplication, 0)

        def SubclassGeneralApplication(self):
            return self.getToken(SourceVfrSyntaxParser.SubclassGeneralApplication, 0)

        def SubclassFrontPage(self):
            return self.getToken(SourceVfrSyntaxParser.SubclassFrontPage, 0)

        def SubclassSingleUse(self):
            return self.getToken(SourceVfrSyntaxParser.SubclassSingleUse, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_subclassDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubclassDefinition" ):
                return visitor.visitSubclassDefinition(self)
            else:
                return visitor.visitChildren(self)




    def subclassDefinition(self):

        localctx = SourceVfrSyntaxParser.SubclassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_subclassDefinition)
        try:
            self.state = 737
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.SubclassSetupApplication]:
                self.enterOuterAlt(localctx, 1)
                self.state = 731
                self.match(SourceVfrSyntaxParser.SubclassSetupApplication)
                pass
            elif token in [SourceVfrSyntaxParser.SubclassGeneralApplication]:
                self.enterOuterAlt(localctx, 2)
                self.state = 732
                self.match(SourceVfrSyntaxParser.SubclassGeneralApplication)
                pass
            elif token in [SourceVfrSyntaxParser.SubclassFrontPage]:
                self.enterOuterAlt(localctx, 3)
                self.state = 733
                self.match(SourceVfrSyntaxParser.SubclassFrontPage)
                pass
            elif token in [SourceVfrSyntaxParser.SubclassSingleUse]:
                self.enterOuterAlt(localctx, 4)
                self.state = 734
                self.match(SourceVfrSyntaxParser.SubclassSingleUse)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 5)
                self.state = 735
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            elif token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 6)
                self.state = 736
                self.match(SourceVfrSyntaxParser.Number)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrFormSetListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.Node = Node

        def vfrFormSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrFormSetContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrFormSetContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrFormSetList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrFormSetList" ):
                return visitor.visitVfrFormSetList(self)
            else:
                return visitor.visitChildren(self)




    def vfrFormSetList(self, Node):

        localctx = SourceVfrSyntaxParser.VfrFormSetListContext(self, self._ctx, self.state, Node)
        self.enterRule(localctx, 60, self.RULE_vfrFormSetList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 742
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.Form or _la==SourceVfrSyntaxParser.FormMap or ((((_la - 105)) & ~0x3f) == 0 and ((1 << (_la - 105)) & ((1 << (SourceVfrSyntaxParser.SuppressIf - 105)) | (1 << (SourceVfrSyntaxParser.DisableIf - 105)) | (1 << (SourceVfrSyntaxParser.Image - 105)) | (1 << (SourceVfrSyntaxParser.DefaultStore - 105)) | (1 << (SourceVfrSyntaxParser.Varstore - 105)) | (1 << (SourceVfrSyntaxParser.Efivarstore - 105)) | (1 << (SourceVfrSyntaxParser.NameValueVarStore - 105)) | (1 << (SourceVfrSyntaxParser.GuidOp - 105)))) != 0):
                self.state = 739
                self.vfrFormSet()
                self.state = 744
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrFormSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrFormDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrFormDefinitionContext,0)


        def vfrFormMapDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrFormMapDefinitionContext,0)


        def vfrStatementImage(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementImageContext,0)


        def vfrStatementVarStoreLinear(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementVarStoreLinearContext,0)


        def vfrStatementVarStoreEfi(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementVarStoreEfiContext,0)


        def vfrStatementVarStoreNameValue(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementVarStoreNameValueContext,0)


        def vfrStatementDefaultStore(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementDefaultStoreContext,0)


        def vfrStatementDisableIfFormSet(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementDisableIfFormSetContext,0)


        def vfrStatementSuppressIfFormSet(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementSuppressIfFormSetContext,0)


        def vfrStatementExtension(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExtensionContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrFormSet

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrFormSet" ):
                return visitor.visitVfrFormSet(self)
            else:
                return visitor.visitChildren(self)




    def vfrFormSet(self):

        localctx = SourceVfrSyntaxParser.VfrFormSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_vfrFormSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Form]:
                self.state = 745
                self.vfrFormDefinition()
                pass
            elif token in [SourceVfrSyntaxParser.FormMap]:
                self.state = 746
                self.vfrFormMapDefinition()
                pass
            elif token in [SourceVfrSyntaxParser.Image]:
                self.state = 747
                self.vfrStatementImage()
                pass
            elif token in [SourceVfrSyntaxParser.Varstore]:
                self.state = 748
                self.vfrStatementVarStoreLinear()
                pass
            elif token in [SourceVfrSyntaxParser.Efivarstore]:
                self.state = 749
                self.vfrStatementVarStoreEfi()
                pass
            elif token in [SourceVfrSyntaxParser.NameValueVarStore]:
                self.state = 750
                self.vfrStatementVarStoreNameValue()
                pass
            elif token in [SourceVfrSyntaxParser.DefaultStore]:
                self.state = 751
                self.vfrStatementDefaultStore()
                pass
            elif token in [SourceVfrSyntaxParser.DisableIf]:
                self.state = 752
                self.vfrStatementDisableIfFormSet()
                pass
            elif token in [SourceVfrSyntaxParser.SuppressIf]:
                self.state = 753
                self.vfrStatementSuppressIfFormSet()
                pass
            elif token in [SourceVfrSyntaxParser.GuidOp]:
                self.state = 754
                self.vfrStatementExtension()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementDefaultStoreContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_DEFAULTSTORE_OP)
            self.D = None # Token
            self.P = None # Token
            self.A = None # Token
            self.S = None # Token

        def DefaultStore(self):
            return self.getToken(SourceVfrSyntaxParser.DefaultStore, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Prompt(self):
            return self.getToken(SourceVfrSyntaxParser.Prompt, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Attribute(self):
            return self.getToken(SourceVfrSyntaxParser.Attribute, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementDefaultStore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementDefaultStore" ):
                return visitor.visitVfrStatementDefaultStore(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementDefaultStore(self):

        localctx = SourceVfrSyntaxParser.VfrStatementDefaultStoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_vfrStatementDefaultStore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 757
            self.match(SourceVfrSyntaxParser.DefaultStore)
            self.state = 758
            localctx.D = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 759
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 760
            self.match(SourceVfrSyntaxParser.Prompt)
            self.state = 761
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 762
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 763
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 764
            localctx.P = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 765
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 773
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Comma:
                self.state = 766
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 767
                self.match(SourceVfrSyntaxParser.Attribute)
                self.state = 768
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 771
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 769
                    localctx.A = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 770
                    localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 775
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementVarStoreLinearContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_VARSTORE_OP)
            self.TN = None # Token
            self.ID = None # Token
            self.S = None # Token
            self.SN = None # Token

        def Varstore(self):
            return self.getToken(SourceVfrSyntaxParser.Varstore, 0)

        def Name(self):
            return self.getToken(SourceVfrSyntaxParser.Name, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Uuid(self):
            return self.getToken(SourceVfrSyntaxParser.Uuid, 0)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Uint8(self):
            return self.getToken(SourceVfrSyntaxParser.Uint8, 0)

        def Uint16(self):
            return self.getToken(SourceVfrSyntaxParser.Uint16, 0)

        def Uint32(self):
            return self.getToken(SourceVfrSyntaxParser.Uint32, 0)

        def Uint64(self):
            return self.getToken(SourceVfrSyntaxParser.Uint64, 0)

        def EFI_HII_DATE(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_DATE, 0)

        def EFI_HII_TIME(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_TIME, 0)

        def EFI_HII_REF(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_REF, 0)

        def VarId(self):
            return self.getToken(SourceVfrSyntaxParser.VarId, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementVarStoreLinear

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementVarStoreLinear" ):
                return visitor.visitVfrStatementVarStoreLinear(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementVarStoreLinear(self):

        localctx = SourceVfrSyntaxParser.VfrStatementVarStoreLinearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_vfrStatementVarStoreLinear)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 777
            self.match(SourceVfrSyntaxParser.Varstore)
            self.state = 794
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 778
                localctx.TN = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 779
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.Uint8]:
                self.state = 780
                self.match(SourceVfrSyntaxParser.Uint8)
                self.state = 781
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.Uint16]:
                self.state = 782
                self.match(SourceVfrSyntaxParser.Uint16)
                self.state = 783
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.Uint32]:
                self.state = 784
                self.match(SourceVfrSyntaxParser.Uint32)
                self.state = 785
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.Uint64]:
                self.state = 786
                self.match(SourceVfrSyntaxParser.Uint64)
                self.state = 787
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.EFI_HII_DATE]:
                self.state = 788
                self.match(SourceVfrSyntaxParser.EFI_HII_DATE)
                self.state = 789
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.EFI_HII_TIME]:
                self.state = 790
                self.match(SourceVfrSyntaxParser.EFI_HII_TIME)
                self.state = 791
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.EFI_HII_REF]:
                self.state = 792
                self.match(SourceVfrSyntaxParser.EFI_HII_REF)
                self.state = 793
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 803
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.VarId:
                self.state = 796
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 797
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 800
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 798
                    localctx.ID = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 799
                    localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 802
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 805
            self.match(SourceVfrSyntaxParser.Name)
            self.state = 806
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 807
            localctx.SN = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 808
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 809
            self.match(SourceVfrSyntaxParser.Uuid)
            self.state = 810
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 811
            self.guidDefinition()
            self.state = 812
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementVarStoreEfiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_VARSTORE_EFI_OP)
            self.TN = None # Token
            self.ID = None # Token
            self.S1 = None # Token
            self.SN = None # Token
            self.VN = None # Token
            self.N = None # Token
            self.S2 = None # Token

        def Efivarstore(self):
            return self.getToken(SourceVfrSyntaxParser.Efivarstore, 0)

        def Attribute(self):
            return self.getToken(SourceVfrSyntaxParser.Attribute, 0)

        def vfrVarStoreEfiAttr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrVarStoreEfiAttrContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrVarStoreEfiAttrContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Uuid(self):
            return self.getToken(SourceVfrSyntaxParser.Uuid, 0)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Uint8(self):
            return self.getToken(SourceVfrSyntaxParser.Uint8, 0)

        def Uint16(self):
            return self.getToken(SourceVfrSyntaxParser.Uint16, 0)

        def Uint32(self):
            return self.getToken(SourceVfrSyntaxParser.Uint32, 0)

        def Uint64(self):
            return self.getToken(SourceVfrSyntaxParser.Uint64, 0)

        def EFI_HII_DATE(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_DATE, 0)

        def EFI_HII_TIME(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_TIME, 0)

        def EFI_HII_REF(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_REF, 0)

        def Name(self):
            return self.getToken(SourceVfrSyntaxParser.Name, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def VarSize(self):
            return self.getToken(SourceVfrSyntaxParser.VarSize, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def VarId(self):
            return self.getToken(SourceVfrSyntaxParser.VarId, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementVarStoreEfi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementVarStoreEfi" ):
                return visitor.visitVfrStatementVarStoreEfi(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementVarStoreEfi(self):

        localctx = SourceVfrSyntaxParser.VfrStatementVarStoreEfiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_vfrStatementVarStoreEfi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 814
            self.match(SourceVfrSyntaxParser.Efivarstore)
            self.state = 831
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 815
                localctx.TN = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 816
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.Uint8]:
                self.state = 817
                self.match(SourceVfrSyntaxParser.Uint8)
                self.state = 818
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.Uint16]:
                self.state = 819
                self.match(SourceVfrSyntaxParser.Uint16)
                self.state = 820
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.Uint32]:
                self.state = 821
                self.match(SourceVfrSyntaxParser.Uint32)
                self.state = 822
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.Uint64]:
                self.state = 823
                self.match(SourceVfrSyntaxParser.Uint64)
                self.state = 824
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.EFI_HII_DATE]:
                self.state = 825
                self.match(SourceVfrSyntaxParser.EFI_HII_DATE)
                self.state = 826
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.EFI_HII_TIME]:
                self.state = 827
                self.match(SourceVfrSyntaxParser.EFI_HII_TIME)
                self.state = 828
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.EFI_HII_REF]:
                self.state = 829
                self.match(SourceVfrSyntaxParser.EFI_HII_REF)
                self.state = 830
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 840
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.VarId:
                self.state = 833
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 834
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 837
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 835
                    localctx.ID = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 836
                    localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 839
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 842
            self.match(SourceVfrSyntaxParser.Attribute)
            self.state = 843
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 844
            self.vfrVarStoreEfiAttr()
            self.state = 849
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 845
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 846
                self.vfrVarStoreEfiAttr()
                self.state = 851
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 852
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 871
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 853
                self.match(SourceVfrSyntaxParser.Name)
                self.state = 854
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 855
                localctx.SN = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 856
                self.match(SourceVfrSyntaxParser.Comma)
                pass

            elif la_ == 2:
                self.state = 857
                self.match(SourceVfrSyntaxParser.Name)
                self.state = 858
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 859
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 860
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 861
                localctx.VN = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 862
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 863
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 864
                self.match(SourceVfrSyntaxParser.VarSize)
                self.state = 865
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 868
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 866
                    localctx.N = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 867
                    localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 870
                self.match(SourceVfrSyntaxParser.Comma)
                pass


            self.state = 873
            self.match(SourceVfrSyntaxParser.Uuid)
            self.state = 874
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 875
            self.guidDefinition()
            self.state = 876
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrVarStoreEfiAttrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Attr = 0
            self.N = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrVarStoreEfiAttr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrVarStoreEfiAttr" ):
                return visitor.visitVfrVarStoreEfiAttr(self)
            else:
                return visitor.visitChildren(self)




    def vfrVarStoreEfiAttr(self):

        localctx = SourceVfrSyntaxParser.VfrVarStoreEfiAttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_vfrVarStoreEfiAttr)
        try:
            self.state = 880
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 878
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 879
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementVarStoreNameValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_VARSTORE_NAME_VALUE_OP)
            self.SN = None # Token
            self.ID = None # Token
            self.SID = None # Token
            self.SN2 = None # Token

        def NameValueVarStore(self):
            return self.getToken(SourceVfrSyntaxParser.NameValueVarStore, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Uuid(self):
            return self.getToken(SourceVfrSyntaxParser.Uuid, 0)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def VarId(self):
            return self.getToken(SourceVfrSyntaxParser.VarId, 0)

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Name)
            else:
                return self.getToken(SourceVfrSyntaxParser.Name, i)

        def StringToken(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringToken)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringToken, i)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementVarStoreNameValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementVarStoreNameValue" ):
                return visitor.visitVfrStatementVarStoreNameValue(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementVarStoreNameValue(self):

        localctx = SourceVfrSyntaxParser.VfrStatementVarStoreNameValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_vfrStatementVarStoreNameValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 882
            self.match(SourceVfrSyntaxParser.NameValueVarStore)
            self.state = 883
            localctx.SN = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 884
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 892
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.VarId:
                self.state = 885
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 886
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 889
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 887
                    localctx.ID = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 888
                    localctx.SID = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 891
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 901
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 894
                self.match(SourceVfrSyntaxParser.Name)
                self.state = 895
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 896
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 897
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 898
                localctx.SN2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 899
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 900
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 903
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SourceVfrSyntaxParser.Name):
                    break

            self.state = 905
            self.match(SourceVfrSyntaxParser.Uuid)
            self.state = 906
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 907
            self.guidDefinition()
            self.state = 908
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementDisableIfFormSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_DISABLE_IF_OP)

        def DisableIf(self):
            return self.getToken(SourceVfrSyntaxParser.DisableIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def vfrFormSetList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrFormSetListContext,0)


        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementDisableIfFormSet

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementDisableIfFormSet" ):
                return visitor.visitVfrStatementDisableIfFormSet(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementDisableIfFormSet(self):

        localctx = SourceVfrSyntaxParser.VfrStatementDisableIfFormSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_vfrStatementDisableIfFormSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 910
            self.match(SourceVfrSyntaxParser.DisableIf)
            self.state = 911
            self.vfrStatementExpression(localctx.Node)
            self.state = 912
            self.match(SourceVfrSyntaxParser.Semicolon)
            self.state = 913
            self.vfrFormSetList(localctx.Node)
            self.state = 914
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 915
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementSuppressIfFormSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_SUPPRESS_IF_OP)

        def SuppressIf(self):
            return self.getToken(SourceVfrSyntaxParser.SuppressIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def vfrFormSetList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrFormSetListContext,0)


        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementSuppressIfFormSet

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementSuppressIfFormSet" ):
                return visitor.visitVfrStatementSuppressIfFormSet(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementSuppressIfFormSet(self):

        localctx = SourceVfrSyntaxParser.VfrStatementSuppressIfFormSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_vfrStatementSuppressIfFormSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 917
            self.match(SourceVfrSyntaxParser.SuppressIf)
            self.state = 918
            self.vfrStatementExpression(localctx.Node)
            self.state = 919
            self.match(SourceVfrSyntaxParser.Semicolon)
            self.state = 920
            self.vfrFormSetList(localctx.Node)
            self.state = 921
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 922
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetStringIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.StringId = ''

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_getStringId

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetStringId" ):
                return visitor.visitGetStringId(self)
            else:
                return visitor.visitChildren(self)




    def getStringId(self):

        localctx = SourceVfrSyntaxParser.GetStringIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_getStringId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 924
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 925
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 926
            self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 927
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrQuestionHeaderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None, QType=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.QType = None
            self.Node = Node
            self.QType = QType

        def vfrQuestionBaseInfo(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionBaseInfoContext,0)


        def vfrStatementHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementHeaderContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrQuestionHeader

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrQuestionHeader" ):
                return visitor.visitVfrQuestionHeader(self)
            else:
                return visitor.visitChildren(self)




    def vfrQuestionHeader(self, Node, QType):

        localctx = SourceVfrSyntaxParser.VfrQuestionHeaderContext(self, self._ctx, self.state, Node, QType)
        self.enterRule(localctx, 80, self.RULE_vfrQuestionHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 929
            self.vfrQuestionBaseInfo(Node, QType)
            self.state = 930
            self.vfrStatementHeader(Node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrQuestionBaseInfoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None, QType=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.QType = None
            self.BaseInfo = EFI_VARSTORE_INFO()
            self.QId = EFI_QUESTION_ID_INVALID
            self.CheckFlag = True
            self.QName = None
            self.VarIdStr = ''
            self.QN = None # Token
            self.ID = None # Token
            self.SID = None # Token
            self.Node = Node
            self.QType = QType

        def Name(self):
            return self.getToken(SourceVfrSyntaxParser.Name, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def VarId(self):
            return self.getToken(SourceVfrSyntaxParser.VarId, 0)

        def vfrStorageVarId(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStorageVarIdContext,0)


        def QuestionId(self):
            return self.getToken(SourceVfrSyntaxParser.QuestionId, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrQuestionBaseInfo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrQuestionBaseInfo" ):
                return visitor.visitVfrQuestionBaseInfo(self)
            else:
                return visitor.visitChildren(self)




    def vfrQuestionBaseInfo(self, Node, QType):

        localctx = SourceVfrSyntaxParser.VfrQuestionBaseInfoContext(self, self._ctx, self.state, Node, QType)
        self.enterRule(localctx, 82, self.RULE_vfrQuestionBaseInfo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 936
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Name:
                self.state = 932
                self.match(SourceVfrSyntaxParser.Name)
                self.state = 933
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 934
                localctx.QN = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 935
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 943
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.VarId:
                self.state = 938
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 939
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 940
                self.vfrStorageVarId(localctx.BaseInfo, localctx.CheckFlag)
                self.state = 941
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 952
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.QuestionId:
                self.state = 945
                self.match(SourceVfrSyntaxParser.QuestionId)
                self.state = 946
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 949
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 947
                    localctx.ID = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 948
                    localctx.SID = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 951
                self.match(SourceVfrSyntaxParser.Comma)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementHeaderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.P = None # Token
            self.H = None # Token
            self.Node = Node

        def Prompt(self):
            return self.getToken(SourceVfrSyntaxParser.Prompt, 0)

        def StringToken(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringToken)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringToken, i)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def Help(self):
            return self.getToken(SourceVfrSyntaxParser.Help, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementHeader

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementHeader" ):
                return visitor.visitVfrStatementHeader(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementHeader(self, Node):

        localctx = SourceVfrSyntaxParser.VfrStatementHeaderContext(self, self._ctx, self.state, Node)
        self.enterRule(localctx, 84, self.RULE_vfrStatementHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 954
            self.match(SourceVfrSyntaxParser.Prompt)
            self.state = 955
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 956
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 957
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 958
            localctx.P = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 959
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 960
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 961
            self.match(SourceVfrSyntaxParser.Help)
            self.state = 962
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 963
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 964
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 965
            localctx.H = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 966
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuestionheaderFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.QHFlag = 0
            self.O = None # Token
            self.N = None # Token
            self.L = None # Token

        def ReadOnlyFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ReadOnlyFlag, 0)

        def InteractiveFlag(self):
            return self.getToken(SourceVfrSyntaxParser.InteractiveFlag, 0)

        def ResetRequiredFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ResetRequiredFlag, 0)

        def RestStyleFlag(self):
            return self.getToken(SourceVfrSyntaxParser.RestStyleFlag, 0)

        def ReconnectRequiredFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ReconnectRequiredFlag, 0)

        def OptionOnlyFlag(self):
            return self.getToken(SourceVfrSyntaxParser.OptionOnlyFlag, 0)

        def NVAccessFlag(self):
            return self.getToken(SourceVfrSyntaxParser.NVAccessFlag, 0)

        def LateCheckFlag(self):
            return self.getToken(SourceVfrSyntaxParser.LateCheckFlag, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_questionheaderFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestionheaderFlagsField" ):
                return visitor.visitQuestionheaderFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def questionheaderFlagsField(self):

        localctx = SourceVfrSyntaxParser.QuestionheaderFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_questionheaderFlagsField)
        try:
            self.state = 976
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.ReadOnlyFlag]:
                self.enterOuterAlt(localctx, 1)
                self.state = 968
                self.match(SourceVfrSyntaxParser.ReadOnlyFlag)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 969
                self.match(SourceVfrSyntaxParser.InteractiveFlag)
                pass
            elif token in [SourceVfrSyntaxParser.ResetRequiredFlag]:
                self.enterOuterAlt(localctx, 3)
                self.state = 970
                self.match(SourceVfrSyntaxParser.ResetRequiredFlag)
                pass
            elif token in [SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 4)
                self.state = 971
                self.match(SourceVfrSyntaxParser.RestStyleFlag)
                pass
            elif token in [SourceVfrSyntaxParser.ReconnectRequiredFlag]:
                self.enterOuterAlt(localctx, 5)
                self.state = 972
                self.match(SourceVfrSyntaxParser.ReconnectRequiredFlag)
                pass
            elif token in [SourceVfrSyntaxParser.OptionOnlyFlag]:
                self.enterOuterAlt(localctx, 6)
                self.state = 973
                localctx.O = self.match(SourceVfrSyntaxParser.OptionOnlyFlag)
                pass
            elif token in [SourceVfrSyntaxParser.NVAccessFlag]:
                self.enterOuterAlt(localctx, 7)
                self.state = 974
                localctx.N = self.match(SourceVfrSyntaxParser.NVAccessFlag)
                pass
            elif token in [SourceVfrSyntaxParser.LateCheckFlag]:
                self.enterOuterAlt(localctx, 8)
                self.state = 975
                localctx.L = self.match(SourceVfrSyntaxParser.LateCheckFlag)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStorageVarIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, BaseInfo=None, CheckFlag=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.BaseInfo = None
            self.CheckFlag = None
            self.VarIdStr = ''
            self.BaseInfo = BaseInfo
            self.CheckFlag = CheckFlag


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStorageVarId


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.BaseInfo = ctx.BaseInfo
            self.CheckFlag = ctx.CheckFlag
            self.VarIdStr = ctx.VarIdStr



    class VfrStorageVarIdRule1Context(VfrStorageVarIdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.VfrStorageVarIdContext
            super().__init__(parser)
            self.SN1 = None # Token
            self.I = None # Token
            self.copyFrom(ctx)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)
        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)
        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)
        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStorageVarIdRule1" ):
                return visitor.visitVfrStorageVarIdRule1(self)
            else:
                return visitor.visitChildren(self)


    class VfrStorageVarIdRule2Context(VfrStorageVarIdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.VfrStorageVarIdContext
            super().__init__(parser)
            self.SN2 = None # Token
            self.copyFrom(ctx)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)
        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Dot)
            else:
                return self.getToken(SourceVfrSyntaxParser.Dot, i)
        def arrayName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.ArrayNameContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.ArrayNameContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStorageVarIdRule2" ):
                return visitor.visitVfrStorageVarIdRule2(self)
            else:
                return visitor.visitChildren(self)



    def vfrStorageVarId(self, BaseInfo, CheckFlag):

        localctx = SourceVfrSyntaxParser.VfrStorageVarIdContext(self, self._ctx, self.state, BaseInfo, CheckFlag)
        self.enterRule(localctx, 88, self.RULE_vfrStorageVarId)
        self._la = 0 # Token type
        try:
            self.state = 990
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                localctx = SourceVfrSyntaxParser.VfrStorageVarIdRule1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 978
                localctx.SN1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 979
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 980
                localctx.I = self.match(SourceVfrSyntaxParser.Number)
                self.state = 981
                self.match(SourceVfrSyntaxParser.CloseBracket)
                pass

            elif la_ == 2:
                localctx = SourceVfrSyntaxParser.VfrStorageVarIdRule2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 982
                localctx.SN2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 987
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.Dot:
                    self.state = 983
                    self.match(SourceVfrSyntaxParser.Dot)
                    self.state = 984
                    self.arrayName()
                    self.state = 989
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrConstantValueFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.ValueList = []
            self.ListType = False
            self.S1 = None # Token
            self.S2 = None # GuidDefinitionContext
            self.S3 = None # Token
            self.S4 = None # Token
            self.Node = Node

        def TrueSymbol(self):
            return self.getToken(SourceVfrSyntaxParser.TrueSymbol, 0)

        def FalseSymbol(self):
            return self.getToken(SourceVfrSyntaxParser.FalseSymbol, 0)

        def One(self):
            return self.getToken(SourceVfrSyntaxParser.One, 0)

        def Ones(self):
            return self.getToken(SourceVfrSyntaxParser.Ones, 0)

        def Zero(self):
            return self.getToken(SourceVfrSyntaxParser.Zero, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def Negative(self):
            return self.getToken(SourceVfrSyntaxParser.Negative, 0)

        def Colon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Colon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Colon, i)

        def Slash(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Slash)
            else:
                return self.getToken(SourceVfrSyntaxParser.Slash, i)

        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def OpenBrace(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBrace, 0)

        def CloseBrace(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBrace, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrConstantValueField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrConstantValueField" ):
                return visitor.visitVfrConstantValueField(self)
            else:
                return visitor.visitChildren(self)




    def vfrConstantValueField(self, Node):

        localctx = SourceVfrSyntaxParser.VfrConstantValueFieldContext(self, self._ctx, self.state, Node)
        self.enterRule(localctx, 90, self.RULE_vfrConstantValueField)
        self._la = 0 # Token type
        try:
            self.state = 1037
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 992
                self.match(SourceVfrSyntaxParser.TrueSymbol)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 993
                self.match(SourceVfrSyntaxParser.FalseSymbol)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 994
                self.match(SourceVfrSyntaxParser.One)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 995
                self.match(SourceVfrSyntaxParser.Ones)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 996
                self.match(SourceVfrSyntaxParser.Zero)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 997
                localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 999
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SourceVfrSyntaxParser.Negative:
                    self.state = 998
                    self.match(SourceVfrSyntaxParser.Negative)


                self.state = 1001
                self.match(SourceVfrSyntaxParser.Number)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1002
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 1003
                self.match(SourceVfrSyntaxParser.Colon)
                self.state = 1004
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 1005
                self.match(SourceVfrSyntaxParser.Colon)
                self.state = 1006
                self.match(SourceVfrSyntaxParser.Number)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1007
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 1008
                self.match(SourceVfrSyntaxParser.Slash)
                self.state = 1009
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 1010
                self.match(SourceVfrSyntaxParser.Slash)
                self.state = 1011
                self.match(SourceVfrSyntaxParser.Number)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1012
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 1013
                self.match(SourceVfrSyntaxParser.Semicolon)
                self.state = 1014
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 1015
                self.match(SourceVfrSyntaxParser.Semicolon)
                self.state = 1016
                localctx.S2 = self.guidDefinition()
                self.state = 1017
                self.match(SourceVfrSyntaxParser.Semicolon)
                self.state = 1018
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 1019
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 1020
                localctx.S3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 1021
                self.match(SourceVfrSyntaxParser.CloseParen)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1023
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 1024
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 1025
                localctx.S4 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 1026
                self.match(SourceVfrSyntaxParser.CloseParen)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 1027
                self.match(SourceVfrSyntaxParser.OpenBrace)
                self.state = 1028
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 1033
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.Comma:
                    self.state = 1029
                    self.match(SourceVfrSyntaxParser.Comma)
                    self.state = 1030
                    self.match(SourceVfrSyntaxParser.Number)
                    self.state = 1035
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1036
                self.match(SourceVfrSyntaxParser.CloseBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrImageTagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_IMAGE_OP)

        def Image(self):
            return self.getToken(SourceVfrSyntaxParser.Image, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrImageTag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrImageTag" ):
                return visitor.visitVfrImageTag(self)
            else:
                return visitor.visitChildren(self)




    def vfrImageTag(self):

        localctx = SourceVfrSyntaxParser.VfrImageTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_vfrImageTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1039
            self.match(SourceVfrSyntaxParser.Image)
            self.state = 1040
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1041
            self.match(SourceVfrSyntaxParser.T__6)
            self.state = 1042
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1043
            self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1044
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrLockedTagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_LOCKED_OP)

        def Locked(self):
            return self.getToken(SourceVfrSyntaxParser.Locked, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrLockedTag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrLockedTag" ):
                return visitor.visitVfrLockedTag(self)
            else:
                return visitor.visitChildren(self)




    def vfrLockedTag(self):

        localctx = SourceVfrSyntaxParser.VfrLockedTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_vfrLockedTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1046
            self.match(SourceVfrSyntaxParser.Locked)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementStatTagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrImageTag(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrImageTagContext,0)


        def vfrLockedTag(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrLockedTagContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementStatTag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementStatTag" ):
                return visitor.visitVfrStatementStatTag(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementStatTag(self):

        localctx = SourceVfrSyntaxParser.VfrStatementStatTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_vfrStatementStatTag)
        try:
            self.state = 1050
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Image]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1048
                self.vfrImageTag()
                pass
            elif token in [SourceVfrSyntaxParser.Locked]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1049
                self.vfrLockedTag()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementStatTagListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.Node = Node

        def vfrStatementStatTag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementStatTagContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatTagContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementStatTagList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementStatTagList" ):
                return visitor.visitVfrStatementStatTagList(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementStatTagList(self, Node):

        localctx = SourceVfrSyntaxParser.VfrStatementStatTagListContext(self, self._ctx, self.state, Node)
        self.enterRule(localctx, 98, self.RULE_vfrStatementStatTagList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1052
            self.vfrStatementStatTag()
            self.state = 1057
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1053
                    self.match(SourceVfrSyntaxParser.Comma)
                    self.state = 1054
                    self.vfrStatementStatTag()
                self.state = 1059
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrFormDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_FORM_OP)
            self.N = None # Token
            self.S = None # Token
            self.ST = None # Token

        def Form(self):
            return self.getToken(SourceVfrSyntaxParser.Form, 0)

        def FormId(self):
            return self.getToken(SourceVfrSyntaxParser.FormId, 0)

        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def Title(self):
            return self.getToken(SourceVfrSyntaxParser.Title, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def EndForm(self):
            return self.getToken(SourceVfrSyntaxParser.EndForm, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def vfrForm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrFormContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrFormContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrFormDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrFormDefinition" ):
                return visitor.visitVfrFormDefinition(self)
            else:
                return visitor.visitChildren(self)




    def vfrFormDefinition(self):

        localctx = SourceVfrSyntaxParser.VfrFormDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_vfrFormDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1060
            self.match(SourceVfrSyntaxParser.Form)
            self.state = 1061
            self.match(SourceVfrSyntaxParser.FormId)
            self.state = 1062
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1065
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 1063
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 1064
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1067
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1068
            self.match(SourceVfrSyntaxParser.Title)
            self.state = 1069
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1070
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1071
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1072
            localctx.ST = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1073
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1074
            self.match(SourceVfrSyntaxParser.Semicolon)
            self.state = 1078
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (SourceVfrSyntaxParser.OneOf - 46)) | (1 << (SourceVfrSyntaxParser.OrderedList - 46)) | (1 << (SourceVfrSyntaxParser.Subtitle - 46)) | (1 << (SourceVfrSyntaxParser.Text - 46)) | (1 << (SourceVfrSyntaxParser.Date - 46)) | (1 << (SourceVfrSyntaxParser.Time - 46)) | (1 << (SourceVfrSyntaxParser.GrayOutIf - 46)) | (1 << (SourceVfrSyntaxParser.Label - 46)) | (1 << (SourceVfrSyntaxParser.Inventory - 46)) | (1 << (SourceVfrSyntaxParser.CheckBox - 46)) | (1 << (SourceVfrSyntaxParser.Numeric - 46)) | (1 << (SourceVfrSyntaxParser.Default - 46)) | (1 << (SourceVfrSyntaxParser.Password - 46)) | (1 << (SourceVfrSyntaxParser.String - 46)) | (1 << (SourceVfrSyntaxParser.SuppressIf - 46)) | (1 << (SourceVfrSyntaxParser.DisableIf - 46)) | (1 << (SourceVfrSyntaxParser.Hidden - 46)) | (1 << (SourceVfrSyntaxParser.Goto - 46)))) != 0) or ((((_la - 110)) & ~0x3f) == 0 and ((1 << (_la - 110)) & ((1 << (SourceVfrSyntaxParser.InconsistentIf - 110)) | (1 << (SourceVfrSyntaxParser.Restore - 110)) | (1 << (SourceVfrSyntaxParser.Save - 110)) | (1 << (SourceVfrSyntaxParser.Banner - 110)) | (1 << (SourceVfrSyntaxParser.Image - 110)) | (1 << (SourceVfrSyntaxParser.Locked - 110)) | (1 << (SourceVfrSyntaxParser.Rule - 110)) | (1 << (SourceVfrSyntaxParser.ResetButton - 110)) | (1 << (SourceVfrSyntaxParser.Action - 110)) | (1 << (SourceVfrSyntaxParser.GuidOp - 110)) | (1 << (SourceVfrSyntaxParser.Modal - 110)))) != 0) or _la==SourceVfrSyntaxParser.RefreshGuid:
                self.state = 1075
                self.vfrForm()
                self.state = 1080
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1081
            self.match(SourceVfrSyntaxParser.EndForm)
            self.state = 1082
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrFormContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementImage(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementImageContext,0)


        def vfrStatementLocked(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementLockedContext,0)


        def vfrStatementRules(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementRulesContext,0)


        def vfrStatementDefault(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementDefaultContext,0)


        def vfrStatementStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatContext,0)


        def vfrStatementQuestions(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionsContext,0)


        def vfrStatementConditional(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementConditionalContext,0)


        def vfrStatementLabel(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementLabelContext,0)


        def vfrStatementBanner(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementBannerContext,0)


        def vfrStatementInvalid(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInvalidContext,0)


        def vfrStatementExtension(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExtensionContext,0)


        def vfrStatementModal(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementModalContext,0)


        def vfrStatementRefreshEvent(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementRefreshEventContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrForm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrForm" ):
                return visitor.visitVfrForm(self)
            else:
                return visitor.visitChildren(self)




    def vfrForm(self):

        localctx = SourceVfrSyntaxParser.VfrFormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_vfrForm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1099
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Image]:
                self.state = 1084
                self.vfrStatementImage()
                pass
            elif token in [SourceVfrSyntaxParser.Locked]:
                self.state = 1085
                self.vfrStatementLocked()
                pass
            elif token in [SourceVfrSyntaxParser.Rule]:
                self.state = 1086
                self.vfrStatementRules()
                pass
            elif token in [SourceVfrSyntaxParser.Default]:
                self.state = 1087
                self.vfrStatementDefault()
                pass
            elif token in [SourceVfrSyntaxParser.Subtitle, SourceVfrSyntaxParser.Text, SourceVfrSyntaxParser.Goto, SourceVfrSyntaxParser.ResetButton]:
                self.state = 1088
                self.vfrStatementStat()
                pass
            elif token in [SourceVfrSyntaxParser.OneOf, SourceVfrSyntaxParser.OrderedList, SourceVfrSyntaxParser.Date, SourceVfrSyntaxParser.Time, SourceVfrSyntaxParser.CheckBox, SourceVfrSyntaxParser.Numeric, SourceVfrSyntaxParser.Password, SourceVfrSyntaxParser.String, SourceVfrSyntaxParser.Action]:
                self.state = 1089
                self.vfrStatementQuestions()
                pass
            elif token in [SourceVfrSyntaxParser.GrayOutIf, SourceVfrSyntaxParser.SuppressIf, SourceVfrSyntaxParser.DisableIf, SourceVfrSyntaxParser.InconsistentIf]:
                self.state = 1090
                self.vfrStatementConditional()
                pass
            elif token in [SourceVfrSyntaxParser.Label]:
                self.state = 1091
                self.vfrStatementLabel()
                pass
            elif token in [SourceVfrSyntaxParser.Banner]:
                self.state = 1092
                self.vfrStatementBanner()
                pass
            elif token in [SourceVfrSyntaxParser.Inventory, SourceVfrSyntaxParser.Hidden, SourceVfrSyntaxParser.Restore, SourceVfrSyntaxParser.Save]:
                self.state = 1093
                self.vfrStatementInvalid()
                pass
            elif token in [SourceVfrSyntaxParser.GuidOp]:
                self.state = 1094
                self.vfrStatementExtension()
                pass
            elif token in [SourceVfrSyntaxParser.Modal]:
                self.state = 1095
                self.vfrStatementModal()
                pass
            elif token in [SourceVfrSyntaxParser.RefreshGuid]:
                self.state = 1096
                self.vfrStatementRefreshEvent()
                self.state = 1097
                self.match(SourceVfrSyntaxParser.Semicolon)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrFormMapDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_FORM_MAP_OP)
            self.N = None # Token
            self.S = None # Token
            self.SM = None # Token

        def FormMap(self):
            return self.getToken(SourceVfrSyntaxParser.FormMap, 0)

        def FormId(self):
            return self.getToken(SourceVfrSyntaxParser.FormId, 0)

        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def EndForm(self):
            return self.getToken(SourceVfrSyntaxParser.EndForm, 0)

        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def MapTitle(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.MapTitle)
            else:
                return self.getToken(SourceVfrSyntaxParser.MapTitle, i)

        def StringToken(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringToken)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringToken, i)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def MapGuid(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.MapGuid)
            else:
                return self.getToken(SourceVfrSyntaxParser.MapGuid, i)

        def guidDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.GuidDefinitionContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,i)


        def vfrForm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrFormContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrFormContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrFormMapDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrFormMapDefinition" ):
                return visitor.visitVfrFormMapDefinition(self)
            else:
                return visitor.visitChildren(self)




    def vfrFormMapDefinition(self):

        localctx = SourceVfrSyntaxParser.VfrFormMapDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_vfrFormMapDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1101
            self.match(SourceVfrSyntaxParser.FormMap)
            self.state = 1102
            self.match(SourceVfrSyntaxParser.FormId)
            self.state = 1103
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 1104
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 1105
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1108
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.MapTitle:
                self.state = 1109
                self.match(SourceVfrSyntaxParser.MapTitle)
                self.state = 1110
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1111
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 1112
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 1113
                localctx.SM = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 1114
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 1115
                self.match(SourceVfrSyntaxParser.Semicolon)
                self.state = 1116
                self.match(SourceVfrSyntaxParser.MapGuid)
                self.state = 1117
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1118
                self.guidDefinition()
                self.state = 1119
                self.match(SourceVfrSyntaxParser.Semicolon)
                self.state = 1125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (SourceVfrSyntaxParser.OneOf - 46)) | (1 << (SourceVfrSyntaxParser.OrderedList - 46)) | (1 << (SourceVfrSyntaxParser.Subtitle - 46)) | (1 << (SourceVfrSyntaxParser.Text - 46)) | (1 << (SourceVfrSyntaxParser.Date - 46)) | (1 << (SourceVfrSyntaxParser.Time - 46)) | (1 << (SourceVfrSyntaxParser.GrayOutIf - 46)) | (1 << (SourceVfrSyntaxParser.Label - 46)) | (1 << (SourceVfrSyntaxParser.Inventory - 46)) | (1 << (SourceVfrSyntaxParser.CheckBox - 46)) | (1 << (SourceVfrSyntaxParser.Numeric - 46)) | (1 << (SourceVfrSyntaxParser.Default - 46)) | (1 << (SourceVfrSyntaxParser.Password - 46)) | (1 << (SourceVfrSyntaxParser.String - 46)) | (1 << (SourceVfrSyntaxParser.SuppressIf - 46)) | (1 << (SourceVfrSyntaxParser.DisableIf - 46)) | (1 << (SourceVfrSyntaxParser.Hidden - 46)) | (1 << (SourceVfrSyntaxParser.Goto - 46)))) != 0) or ((((_la - 110)) & ~0x3f) == 0 and ((1 << (_la - 110)) & ((1 << (SourceVfrSyntaxParser.InconsistentIf - 110)) | (1 << (SourceVfrSyntaxParser.Restore - 110)) | (1 << (SourceVfrSyntaxParser.Save - 110)) | (1 << (SourceVfrSyntaxParser.Banner - 110)) | (1 << (SourceVfrSyntaxParser.Image - 110)) | (1 << (SourceVfrSyntaxParser.Locked - 110)) | (1 << (SourceVfrSyntaxParser.Rule - 110)) | (1 << (SourceVfrSyntaxParser.ResetButton - 110)) | (1 << (SourceVfrSyntaxParser.Action - 110)) | (1 << (SourceVfrSyntaxParser.GuidOp - 110)) | (1 << (SourceVfrSyntaxParser.Modal - 110)))) != 0) or _la==SourceVfrSyntaxParser.RefreshGuid:
                self.state = 1126
                self.vfrForm()
                self.state = 1131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1132
            self.match(SourceVfrSyntaxParser.EndForm)
            self.state = 1133
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementImageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrImageTag(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrImageTagContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementImage

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementImage" ):
                return visitor.visitVfrStatementImage(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementImage(self):

        localctx = SourceVfrSyntaxParser.VfrStatementImageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_vfrStatementImage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1135
            self.vfrImageTag()
            self.state = 1136
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementLockedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrLockedTag(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrLockedTagContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementLocked

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementLocked" ):
                return visitor.visitVfrStatementLocked(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementLocked(self):

        localctx = SourceVfrSyntaxParser.VfrStatementLockedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_vfrStatementLocked)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1138
            self.vfrLockedTag()
            self.state = 1139
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementRulesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_RULE_OP)

        def Rule(self):
            return self.getToken(SourceVfrSyntaxParser.Rule, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def EndRule(self):
            return self.getToken(SourceVfrSyntaxParser.EndRule, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementRules

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementRules" ):
                return visitor.visitVfrStatementRules(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementRules(self):

        localctx = SourceVfrSyntaxParser.VfrStatementRulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_vfrStatementRules)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1141
            self.match(SourceVfrSyntaxParser.Rule)
            self.state = 1142
            self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1143
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1144
            self.vfrStatementExpression(localctx.Node)
            self.state = 1145
            self.match(SourceVfrSyntaxParser.EndRule)
            self.state = 1146
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementSubTitle(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementSubTitleContext,0)


        def vfrStatementStaticText(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStaticTextContext,0)


        def vfrStatementCrossReference(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementCrossReferenceContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementStat" ):
                return visitor.visitVfrStatementStat(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementStat(self):

        localctx = SourceVfrSyntaxParser.VfrStatementStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_vfrStatementStat)
        try:
            self.state = 1151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Subtitle]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1148
                self.vfrStatementSubTitle()
                pass
            elif token in [SourceVfrSyntaxParser.Text]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1149
                self.vfrStatementStaticText()
                pass
            elif token in [SourceVfrSyntaxParser.Goto, SourceVfrSyntaxParser.ResetButton]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1150
                self.vfrStatementCrossReference()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementSubTitleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_SUBTITLE_OP)
            self.S = None # Token

        def Subtitle(self):
            return self.getToken(SourceVfrSyntaxParser.Subtitle, 0)

        def Text(self):
            return self.getToken(SourceVfrSyntaxParser.Text, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def EndSubtitle(self):
            return self.getToken(SourceVfrSyntaxParser.EndSubtitle, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def vfrSubtitleFlags(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrSubtitleFlagsContext,0)


        def vfrStatementStatTagList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatTagListContext,0)


        def vfrStatementSubTitleComponent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementSubTitleComponentContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementSubTitleComponentContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementSubTitle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementSubTitle" ):
                return visitor.visitVfrStatementSubTitle(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementSubTitle(self):

        localctx = SourceVfrSyntaxParser.VfrStatementSubTitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_vfrStatementSubTitle)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1153
            self.match(SourceVfrSyntaxParser.Subtitle)
            self.state = 1154
            self.match(SourceVfrSyntaxParser.Text)
            self.state = 1155
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1156
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1157
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1158
            localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1159
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 1160
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1161
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1162
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1163
                self.vfrSubtitleFlags(localctx.Node)


            self.state = 1186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 1168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SourceVfrSyntaxParser.Comma:
                    self.state = 1166
                    self.match(SourceVfrSyntaxParser.Comma)
                    self.state = 1167
                    self.vfrStatementStatTagList(localctx.Node)


                self.state = 1170
                self.match(SourceVfrSyntaxParser.Semicolon)
                pass

            elif la_ == 2:
                self.state = 1173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
                if la_ == 1:
                    self.state = 1171
                    self.match(SourceVfrSyntaxParser.Comma)
                    self.state = 1172
                    self.vfrStatementStatTagList(localctx.Node)


                self.state = 1182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SourceVfrSyntaxParser.Comma:
                    self.state = 1175
                    self.match(SourceVfrSyntaxParser.Comma)
                    self.state = 1179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (SourceVfrSyntaxParser.OneOf - 46)) | (1 << (SourceVfrSyntaxParser.OrderedList - 46)) | (1 << (SourceVfrSyntaxParser.Subtitle - 46)) | (1 << (SourceVfrSyntaxParser.Text - 46)) | (1 << (SourceVfrSyntaxParser.Date - 46)) | (1 << (SourceVfrSyntaxParser.Time - 46)) | (1 << (SourceVfrSyntaxParser.CheckBox - 46)) | (1 << (SourceVfrSyntaxParser.Numeric - 46)) | (1 << (SourceVfrSyntaxParser.Password - 46)) | (1 << (SourceVfrSyntaxParser.String - 46)) | (1 << (SourceVfrSyntaxParser.Goto - 46)))) != 0) or _la==SourceVfrSyntaxParser.ResetButton or _la==SourceVfrSyntaxParser.Action:
                        self.state = 1176
                        self.vfrStatementSubTitleComponent()
                        self.state = 1181
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 1184
                self.match(SourceVfrSyntaxParser.EndSubtitle)
                self.state = 1185
                self.match(SourceVfrSyntaxParser.Semicolon)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementSubTitleComponentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatContext,0)


        def vfrStatementQuestions(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionsContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementSubTitleComponent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementSubTitleComponent" ):
                return visitor.visitVfrStatementSubTitleComponent(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementSubTitleComponent(self):

        localctx = SourceVfrSyntaxParser.VfrStatementSubTitleComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_vfrStatementSubTitleComponent)
        try:
            self.state = 1190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Subtitle, SourceVfrSyntaxParser.Text, SourceVfrSyntaxParser.Goto, SourceVfrSyntaxParser.ResetButton]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1188
                self.vfrStatementStat()
                pass
            elif token in [SourceVfrSyntaxParser.OneOf, SourceVfrSyntaxParser.OrderedList, SourceVfrSyntaxParser.Date, SourceVfrSyntaxParser.Time, SourceVfrSyntaxParser.CheckBox, SourceVfrSyntaxParser.Numeric, SourceVfrSyntaxParser.Password, SourceVfrSyntaxParser.String, SourceVfrSyntaxParser.Action]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1189
                self.vfrStatementQuestions()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrSubtitleFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.SubFlags = 0
            self.Node = Node

        def subtitleFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.SubtitleFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.SubtitleFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrSubtitleFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrSubtitleFlags" ):
                return visitor.visitVfrSubtitleFlags(self)
            else:
                return visitor.visitChildren(self)




    def vfrSubtitleFlags(self, Node):

        localctx = SourceVfrSyntaxParser.VfrSubtitleFlagsContext(self, self._ctx, self.state, Node)
        self.enterRule(localctx, 118, self.RULE_vfrSubtitleFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1192
            self.subtitleFlagsField()
            self.state = 1197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1193
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1194
                self.subtitleFlagsField()
                self.state = 1199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubtitleFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Flag = 0
            self.N = None # Token
            self.H = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_subtitleFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtitleFlagsField" ):
                return visitor.visitSubtitleFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def subtitleFlagsField(self):

        localctx = SourceVfrSyntaxParser.SubtitleFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_subtitleFlagsField)
        try:
            self.state = 1203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1200
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1201
                localctx.H = self.match(SourceVfrSyntaxParser.T__7)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1202
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementStaticTextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_TEXT_OP)
            self.S1 = None # Token
            self.S2 = None # Token
            self.S3 = None # Token
            self.F = None # Token
            self.N = None # Token
            self.S4 = None # Token

        def Text(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Text)
            else:
                return self.getToken(SourceVfrSyntaxParser.Text, i)

        def Help(self):
            return self.getToken(SourceVfrSyntaxParser.Help, 0)

        def StringToken(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringToken)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringToken, i)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def staticTextFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.StaticTextFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.StaticTextFlagsFieldContext,i)


        def Key(self):
            return self.getToken(SourceVfrSyntaxParser.Key, 0)

        def vfrStatementStatTagList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatTagListContext,0)


        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementStaticText

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementStaticText" ):
                return visitor.visitVfrStatementStaticText(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementStaticText(self):

        localctx = SourceVfrSyntaxParser.VfrStatementStaticTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_vfrStatementStaticText)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1205
            self.match(SourceVfrSyntaxParser.Text)
            self.state = 1206
            self.match(SourceVfrSyntaxParser.Help)
            self.state = 1207
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1208
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1209
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1210
            localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1211
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1212
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1213
            self.match(SourceVfrSyntaxParser.Text)
            self.state = 1214
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1215
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1216
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1217
            localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1218
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.state = 1219
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1220
                self.match(SourceVfrSyntaxParser.Text)
                self.state = 1221
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1222
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 1223
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 1224
                localctx.S3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 1225
                self.match(SourceVfrSyntaxParser.CloseParen)


            self.state = 1246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.state = 1228
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1229
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1230
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1231
                self.staticTextFlagsField()
                self.state = 1236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 1232
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 1233
                    self.staticTextFlagsField()
                    self.state = 1238
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1239
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1240
                self.match(SourceVfrSyntaxParser.Key)
                self.state = 1241
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1244
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1242
                    localctx.N = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1243
                    localctx.S4 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 1250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Comma:
                self.state = 1248
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1249
                self.vfrStatementStatTagList(localctx.Node)


            self.state = 1252
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticTextFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Flag = 0
            self.N = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def questionheaderFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.QuestionheaderFlagsFieldContext,0)


        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_staticTextFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticTextFlagsField" ):
                return visitor.visitStaticTextFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def staticTextFlagsField(self):

        localctx = SourceVfrSyntaxParser.StaticTextFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_staticTextFlagsField)
        try:
            self.state = 1257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1254
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag, SourceVfrSyntaxParser.NVAccessFlag, SourceVfrSyntaxParser.ResetRequiredFlag, SourceVfrSyntaxParser.ReconnectRequiredFlag, SourceVfrSyntaxParser.LateCheckFlag, SourceVfrSyntaxParser.ReadOnlyFlag, SourceVfrSyntaxParser.OptionOnlyFlag, SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1255
                self.questionheaderFlagsField()
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1256
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementCrossReferenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementGoto(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementGotoContext,0)


        def vfrStatementResetButton(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementResetButtonContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementCrossReference

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementCrossReference" ):
                return visitor.visitVfrStatementCrossReference(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementCrossReference(self):

        localctx = SourceVfrSyntaxParser.VfrStatementCrossReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_vfrStatementCrossReference)
        try:
            self.state = 1261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Goto]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1259
                self.vfrStatementGoto()
                pass
            elif token in [SourceVfrSyntaxParser.ResetButton]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1260
                self.vfrStatementResetButton()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementGotoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_REF_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_REF
            self.S = None # Token
            self.SG1 = None # GuidDefinitionContext
            self.NF1 = None # Token
            self.SF1 = None # Token
            self.NQ1 = None # Token
            self.SQ1 = None # Token
            self.SG2 = None # GuidDefinitionContext
            self.NF2 = None # Token
            self.SF2 = None # Token
            self.NQ2 = None # Token
            self.SQ2 = None # Token
            self.NF3 = None # Token
            self.SF3 = None # Token
            self.SQ3 = None # Token
            self.NQ3 = None # Token
            self.N1 = None # Token
            self.S1 = None # Token
            self.KN = None # Token
            self.SN = None # Token
            self.E = None # Token

        def Goto(self):
            return self.getToken(SourceVfrSyntaxParser.Goto, 0)

        def vfrQuestionHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionHeaderContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def vfrGotoFlags(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrGotoFlagsContext,0)


        def Key(self):
            return self.getToken(SourceVfrSyntaxParser.Key, 0)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def DevicePath(self):
            return self.getToken(SourceVfrSyntaxParser.DevicePath, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def FormSetGuid(self):
            return self.getToken(SourceVfrSyntaxParser.FormSetGuid, 0)

        def FormId(self):
            return self.getToken(SourceVfrSyntaxParser.FormId, 0)

        def Question(self):
            return self.getToken(SourceVfrSyntaxParser.Question, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementGoto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementGoto" ):
                return visitor.visitVfrStatementGoto(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementGoto(self):

        localctx = SourceVfrSyntaxParser.VfrStatementGotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_vfrStatementGoto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1263
            self.match(SourceVfrSyntaxParser.Goto)
            self.state = 1329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.DevicePath]:
                self.state = 1264
                self.match(SourceVfrSyntaxParser.DevicePath)
                self.state = 1265
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1266
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 1267
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 1268
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 1269
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 1270
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1271
                self.match(SourceVfrSyntaxParser.FormSetGuid)
                self.state = 1272
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1273
                localctx.SG1 = self.guidDefinition()
                self.state = 1274
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1275
                self.match(SourceVfrSyntaxParser.FormId)
                self.state = 1276
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1279
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1277
                    localctx.NF1 = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1278
                    localctx.SF1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1281
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1282
                self.match(SourceVfrSyntaxParser.Question)
                self.state = 1283
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1286
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1284
                    localctx.NQ1 = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1285
                    localctx.SQ1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1288
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.FormSetGuid]:
                self.state = 1290
                self.match(SourceVfrSyntaxParser.FormSetGuid)
                self.state = 1291
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1292
                localctx.SG2 = self.guidDefinition()
                self.state = 1293
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1294
                self.match(SourceVfrSyntaxParser.FormId)
                self.state = 1295
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1298
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1296
                    localctx.NF2 = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1297
                    localctx.SF2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1300
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1301
                self.match(SourceVfrSyntaxParser.Question)
                self.state = 1302
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1305
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1303
                    localctx.NQ2 = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1304
                    localctx.SQ2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1307
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.FormId]:
                self.state = 1309
                self.match(SourceVfrSyntaxParser.FormId)
                self.state = 1310
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1313
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1311
                    localctx.NF3 = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1312
                    localctx.SF3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1315
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1316
                self.match(SourceVfrSyntaxParser.Question)
                self.state = 1317
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1322
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1318
                    localctx.SQ3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    self.state = 1319
                    self.match(SourceVfrSyntaxParser.Comma)
                    pass
                elif token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1320
                    localctx.NQ3 = self.match(SourceVfrSyntaxParser.Number)
                    self.state = 1321
                    self.match(SourceVfrSyntaxParser.Comma)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SourceVfrSyntaxParser.Number, SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 1326
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1324
                    localctx.N1 = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1325
                    localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1328
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.Prompt, SourceVfrSyntaxParser.Name, SourceVfrSyntaxParser.VarId, SourceVfrSyntaxParser.QuestionId]:
                pass
            else:
                pass
            self.state = 1331
            self.vfrQuestionHeader(localctx.Node, localctx.QType)
            self.state = 1336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.state = 1332
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1333
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1334
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1335
                self.vfrGotoFlags()


            self.state = 1345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.state = 1338
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1339
                self.match(SourceVfrSyntaxParser.Key)
                self.state = 1340
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1343
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1341
                    localctx.KN = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1342
                    localctx.SN = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 1349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Comma:
                self.state = 1347
                localctx.E = self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1348
                self.vfrStatementQuestionOptionList(localctx.Node)


            self.state = 1351
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrGotoFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.GotoFlags = 0

        def gotoFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.GotoFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.GotoFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrGotoFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrGotoFlags" ):
                return visitor.visitVfrGotoFlags(self)
            else:
                return visitor.visitChildren(self)




    def vfrGotoFlags(self):

        localctx = SourceVfrSyntaxParser.VfrGotoFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_vfrGotoFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1353
            self.gotoFlagsField()
            self.state = 1358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1354
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1355
                self.gotoFlagsField()
                self.state = 1360
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Flag = 0
            self.N = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def questionheaderFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.QuestionheaderFlagsFieldContext,0)


        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_gotoFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoFlagsField" ):
                return visitor.visitGotoFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def gotoFlagsField(self):

        localctx = SourceVfrSyntaxParser.GotoFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_gotoFlagsField)
        try:
            self.state = 1364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1361
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag, SourceVfrSyntaxParser.NVAccessFlag, SourceVfrSyntaxParser.ResetRequiredFlag, SourceVfrSyntaxParser.ReconnectRequiredFlag, SourceVfrSyntaxParser.LateCheckFlag, SourceVfrSyntaxParser.ReadOnlyFlag, SourceVfrSyntaxParser.OptionOnlyFlag, SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1362
                self.questionheaderFlagsField()
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1363
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementResetButtonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_RESET_BUTTON_OP)
            self.N = None # Token

        def ResetButton(self):
            return self.getToken(SourceVfrSyntaxParser.ResetButton, 0)

        def DefaultStore(self):
            return self.getToken(SourceVfrSyntaxParser.DefaultStore, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementHeaderContext,0)


        def EndResetButton(self):
            return self.getToken(SourceVfrSyntaxParser.EndResetButton, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def vfrStatementStatTagList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatTagListContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementResetButton

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementResetButton" ):
                return visitor.visitVfrStatementResetButton(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementResetButton(self):

        localctx = SourceVfrSyntaxParser.VfrStatementResetButtonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_vfrStatementResetButton)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1366
            self.match(SourceVfrSyntaxParser.ResetButton)
            self.state = 1367
            self.match(SourceVfrSyntaxParser.DefaultStore)
            self.state = 1368
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1369
            localctx.N = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1370
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1371
            self.vfrStatementHeader(localctx.Node)
            self.state = 1372
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Image or _la==SourceVfrSyntaxParser.Locked:
                self.state = 1373
                self.vfrStatementStatTagList(localctx.Node)
                self.state = 1374
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1378
            self.match(SourceVfrSyntaxParser.EndResetButton)
            self.state = 1379
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementQuestionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementBooleanType(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementBooleanTypeContext,0)


        def vfrStatementDate(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementDateContext,0)


        def vfrStatementNumericType(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementNumericTypeContext,0)


        def vfrStatementStringType(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStringTypeContext,0)


        def vfrStatementOrderedList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementOrderedListContext,0)


        def vfrStatementTime(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementTimeContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementQuestions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementQuestions" ):
                return visitor.visitVfrStatementQuestions(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementQuestions(self):

        localctx = SourceVfrSyntaxParser.VfrStatementQuestionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_vfrStatementQuestions)
        try:
            self.state = 1387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.CheckBox, SourceVfrSyntaxParser.Action]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1381
                self.vfrStatementBooleanType()
                pass
            elif token in [SourceVfrSyntaxParser.Date]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1382
                self.vfrStatementDate()
                pass
            elif token in [SourceVfrSyntaxParser.OneOf, SourceVfrSyntaxParser.Numeric]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1383
                self.vfrStatementNumericType()
                pass
            elif token in [SourceVfrSyntaxParser.Password, SourceVfrSyntaxParser.String]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1384
                self.vfrStatementStringType()
                pass
            elif token in [SourceVfrSyntaxParser.OrderedList]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1385
                self.vfrStatementOrderedList()
                pass
            elif token in [SourceVfrSyntaxParser.Time]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1386
                self.vfrStatementTime()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementQuestionTagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementStatTag(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatTagContext,0)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def vfrStatementInconsistentIf(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInconsistentIfContext,0)


        def vfrStatementNoSubmitIf(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementNoSubmitIfContext,0)


        def vfrStatementDisableIfQuest(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementDisableIfQuestContext,0)


        def vfrStatementRefresh(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementRefreshContext,0)


        def vfrStatementVarstoreDevice(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementVarstoreDeviceContext,0)


        def vfrStatementExtension(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExtensionContext,0)


        def vfrStatementRefreshEvent(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementRefreshEventContext,0)


        def vfrStatementWarningIf(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementWarningIfContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementQuestionTag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementQuestionTag" ):
                return visitor.visitVfrStatementQuestionTag(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementQuestionTag(self):

        localctx = SourceVfrSyntaxParser.VfrStatementQuestionTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_vfrStatementQuestionTag)
        try:
            self.state = 1400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Image, SourceVfrSyntaxParser.Locked]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1389
                self.vfrStatementStatTag()
                self.state = 1390
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.InconsistentIf]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1392
                self.vfrStatementInconsistentIf()
                pass
            elif token in [SourceVfrSyntaxParser.NoSubmitIf]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1393
                self.vfrStatementNoSubmitIf()
                pass
            elif token in [SourceVfrSyntaxParser.DisableIf]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1394
                self.vfrStatementDisableIfQuest()
                pass
            elif token in [SourceVfrSyntaxParser.Refresh, SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1395
                self.vfrStatementRefresh()
                pass
            elif token in [SourceVfrSyntaxParser.VarstoreDevice]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1396
                self.vfrStatementVarstoreDevice()
                pass
            elif token in [SourceVfrSyntaxParser.GuidOp]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1397
                self.vfrStatementExtension()
                pass
            elif token in [SourceVfrSyntaxParser.RefreshGuid]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1398
                self.vfrStatementRefreshEvent()
                pass
            elif token in [SourceVfrSyntaxParser.WarningIf]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1399
                self.vfrStatementWarningIf()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementInconsistentIfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_INCONSISTENT_IF_OP)
            self.S = None # Token
            self.F = None # Token

        def InconsistentIf(self):
            return self.getToken(SourceVfrSyntaxParser.InconsistentIf, 0)

        def Prompt(self):
            return self.getToken(SourceVfrSyntaxParser.Prompt, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementInconsistentIf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementInconsistentIf" ):
                return visitor.visitVfrStatementInconsistentIf(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementInconsistentIf(self):

        localctx = SourceVfrSyntaxParser.VfrStatementInconsistentIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_vfrStatementInconsistentIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1402
            self.match(SourceVfrSyntaxParser.InconsistentIf)
            self.state = 1403
            self.match(SourceVfrSyntaxParser.Prompt)
            self.state = 1404
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1405
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1406
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1407
            localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1408
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1409
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1410
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1411
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1412
                self.flagsField()
                self.state = 1417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 1413
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 1414
                    self.flagsField()
                    self.state = 1419
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1420
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1424
            self.vfrStatementExpression(localctx.Node)
            self.state = 1425
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 1427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                self.state = 1426
                self.match(SourceVfrSyntaxParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementNoSubmitIfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_NO_SUBMIT_IF_OP)
            self.S = None # Token
            self.F = None # Token

        def NoSubmitIf(self):
            return self.getToken(SourceVfrSyntaxParser.NoSubmitIf, 0)

        def Prompt(self):
            return self.getToken(SourceVfrSyntaxParser.Prompt, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementNoSubmitIf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementNoSubmitIf" ):
                return visitor.visitVfrStatementNoSubmitIf(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementNoSubmitIf(self):

        localctx = SourceVfrSyntaxParser.VfrStatementNoSubmitIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_vfrStatementNoSubmitIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1429
            self.match(SourceVfrSyntaxParser.NoSubmitIf)
            self.state = 1430
            self.match(SourceVfrSyntaxParser.Prompt)
            self.state = 1431
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1432
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1433
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1434
            localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1435
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1436
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1437
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1438
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1439
                self.flagsField()
                self.state = 1444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 1440
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 1441
                    self.flagsField()
                    self.state = 1446
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1447
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1451
            self.vfrStatementExpression(localctx.Node)
            self.state = 1452
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 1454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
            if la_ == 1:
                self.state = 1453
                self.match(SourceVfrSyntaxParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementDisableIfQuestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_DISABLE_IF_OP)

        def DisableIf(self):
            return self.getToken(SourceVfrSyntaxParser.DisableIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementDisableIfQuest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementDisableIfQuest" ):
                return visitor.visitVfrStatementDisableIfQuest(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementDisableIfQuest(self):

        localctx = SourceVfrSyntaxParser.VfrStatementDisableIfQuestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_vfrStatementDisableIfQuest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1456
            self.match(SourceVfrSyntaxParser.DisableIf)
            self.state = 1457
            self.vfrStatementExpression(localctx.Node)
            self.state = 1458
            self.match(SourceVfrSyntaxParser.Semicolon)
            self.state = 1459
            self.vfrStatementQuestionOptionList(localctx.Node)
            self.state = 1460
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 1462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,117,self._ctx)
            if la_ == 1:
                self.state = 1461
                self.match(SourceVfrSyntaxParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementRefreshContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_REFRESH_OP)
            self.N = None # Token
            self.S = None # Token

        def Refresh(self):
            return self.getToken(SourceVfrSyntaxParser.Refresh, 0)

        def Interval(self):
            return self.getToken(SourceVfrSyntaxParser.Interval, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementRefresh

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementRefresh" ):
                return visitor.visitVfrStatementRefresh(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementRefresh(self):

        localctx = SourceVfrSyntaxParser.VfrStatementRefreshContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_vfrStatementRefresh)
        try:
            self.state = 1469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Refresh]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1464
                self.match(SourceVfrSyntaxParser.Refresh)
                self.state = 1465
                self.match(SourceVfrSyntaxParser.Interval)
                self.state = 1466
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1467
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1468
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementVarstoreDeviceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_VARSTORE_DEVICE_OP)
            self.S = None # Token

        def VarstoreDevice(self):
            return self.getToken(SourceVfrSyntaxParser.VarstoreDevice, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementVarstoreDevice

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementVarstoreDevice" ):
                return visitor.visitVfrStatementVarstoreDevice(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementVarstoreDevice(self):

        localctx = SourceVfrSyntaxParser.VfrStatementVarstoreDeviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_vfrStatementVarstoreDevice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1471
            self.match(SourceVfrSyntaxParser.VarstoreDevice)
            self.state = 1472
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1473
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1474
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1475
            localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1476
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1477
            self.match(SourceVfrSyntaxParser.Comma)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementRefreshEventContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_REFRESH_ID_OP)

        def RefreshGuid(self):
            return self.getToken(SourceVfrSyntaxParser.RefreshGuid, 0)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementRefreshEvent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementRefreshEvent" ):
                return visitor.visitVfrStatementRefreshEvent(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementRefreshEvent(self):

        localctx = SourceVfrSyntaxParser.VfrStatementRefreshEventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_vfrStatementRefreshEvent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1479
            self.match(SourceVfrSyntaxParser.RefreshGuid)
            self.state = 1480
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1481
            self.guidDefinition()
            self.state = 1482
            self.match(SourceVfrSyntaxParser.Comma)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementWarningIfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_WARNING_IF_OP)
            self.S = None # Token
            self.N = None # Token
            self.ST = None # Token

        def WarningIf(self):
            return self.getToken(SourceVfrSyntaxParser.WarningIf, 0)

        def Prompt(self):
            return self.getToken(SourceVfrSyntaxParser.Prompt, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Timeout(self):
            return self.getToken(SourceVfrSyntaxParser.Timeout, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementWarningIf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementWarningIf" ):
                return visitor.visitVfrStatementWarningIf(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementWarningIf(self):

        localctx = SourceVfrSyntaxParser.VfrStatementWarningIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_vfrStatementWarningIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1484
            self.match(SourceVfrSyntaxParser.WarningIf)
            self.state = 1485
            self.match(SourceVfrSyntaxParser.Prompt)
            self.state = 1486
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1487
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1488
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1489
            localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1490
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1491
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Timeout:
                self.state = 1492
                self.match(SourceVfrSyntaxParser.Timeout)
                self.state = 1493
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1496
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1494
                    localctx.N = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1495
                    localctx.ST = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1498
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1501
            self.vfrStatementExpression(localctx.Node)
            self.state = 1502
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 1504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
            if la_ == 1:
                self.state = 1503
                self.match(SourceVfrSyntaxParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementQuestionTagListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.Node = Node

        def vfrStatementQuestionTag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementQuestionTagContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionTagContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementQuestionTagList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementQuestionTagList" ):
                return visitor.visitVfrStatementQuestionTagList(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementQuestionTagList(self, Node):

        localctx = SourceVfrSyntaxParser.VfrStatementQuestionTagListContext(self, self._ctx, self.state, Node)
        self.enterRule(localctx, 154, self.RULE_vfrStatementQuestionTagList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (SourceVfrSyntaxParser.DisableIf - 106)) | (1 << (SourceVfrSyntaxParser.InconsistentIf - 106)) | (1 << (SourceVfrSyntaxParser.WarningIf - 106)) | (1 << (SourceVfrSyntaxParser.NoSubmitIf - 106)) | (1 << (SourceVfrSyntaxParser.Image - 106)) | (1 << (SourceVfrSyntaxParser.Locked - 106)) | (1 << (SourceVfrSyntaxParser.Refresh - 106)) | (1 << (SourceVfrSyntaxParser.VarstoreDevice - 106)) | (1 << (SourceVfrSyntaxParser.GuidOp - 106)))) != 0) or _la==SourceVfrSyntaxParser.RefreshGuid or _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 1506
                self.vfrStatementQuestionTag()
                self.state = 1511
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementQuestionOptionTagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementSuppressIfQuest(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementSuppressIfQuestContext,0)


        def vfrStatementGrayOutIfQuest(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementGrayOutIfQuestContext,0)


        def vfrStatementValue(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementValueContext,0)


        def vfrStatementDefault(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementDefaultContext,0)


        def vfrStatementOptions(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementOptionsContext,0)


        def vfrStatementRead(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementReadContext,0)


        def vfrStatementWrite(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementWriteContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementQuestionOptionTag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementQuestionOptionTag" ):
                return visitor.visitVfrStatementQuestionOptionTag(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementQuestionOptionTag(self):

        localctx = SourceVfrSyntaxParser.VfrStatementQuestionOptionTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_vfrStatementQuestionOptionTag)
        try:
            self.state = 1519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.SuppressIf]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1512
                self.vfrStatementSuppressIfQuest()
                pass
            elif token in [SourceVfrSyntaxParser.GrayOutIf]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1513
                self.vfrStatementGrayOutIfQuest()
                pass
            elif token in [SourceVfrSyntaxParser.Value]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1514
                self.vfrStatementValue()
                pass
            elif token in [SourceVfrSyntaxParser.Default]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1515
                self.vfrStatementDefault()
                pass
            elif token in [SourceVfrSyntaxParser.Option]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1516
                self.vfrStatementOptions()
                pass
            elif token in [SourceVfrSyntaxParser.Read]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1517
                self.vfrStatementRead()
                pass
            elif token in [SourceVfrSyntaxParser.Write]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1518
                self.vfrStatementWrite()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.N = None # Token
            self.L = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def InteractiveFlag(self):
            return self.getToken(SourceVfrSyntaxParser.InteractiveFlag, 0)

        def ManufacturingFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ManufacturingFlag, 0)

        def DefaultFlag(self):
            return self.getToken(SourceVfrSyntaxParser.DefaultFlag, 0)

        def ResetRequiredFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ResetRequiredFlag, 0)

        def ReconnectRequiredFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ReconnectRequiredFlag, 0)

        def NVAccessFlag(self):
            return self.getToken(SourceVfrSyntaxParser.NVAccessFlag, 0)

        def LateCheckFlag(self):
            return self.getToken(SourceVfrSyntaxParser.LateCheckFlag, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_flagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlagsField" ):
                return visitor.visitFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def flagsField(self):

        localctx = SourceVfrSyntaxParser.FlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_flagsField)
        try:
            self.state = 1530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1521
                self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1522
                self.match(SourceVfrSyntaxParser.InteractiveFlag)
                pass
            elif token in [SourceVfrSyntaxParser.ManufacturingFlag]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1523
                self.match(SourceVfrSyntaxParser.ManufacturingFlag)
                pass
            elif token in [SourceVfrSyntaxParser.DefaultFlag]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1524
                self.match(SourceVfrSyntaxParser.DefaultFlag)
                pass
            elif token in [SourceVfrSyntaxParser.ResetRequiredFlag]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1525
                self.match(SourceVfrSyntaxParser.ResetRequiredFlag)
                pass
            elif token in [SourceVfrSyntaxParser.ReconnectRequiredFlag]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1526
                self.match(SourceVfrSyntaxParser.ReconnectRequiredFlag)
                pass
            elif token in [SourceVfrSyntaxParser.NVAccessFlag]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1527
                localctx.N = self.match(SourceVfrSyntaxParser.NVAccessFlag)
                pass
            elif token in [SourceVfrSyntaxParser.LateCheckFlag]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1528
                localctx.L = self.match(SourceVfrSyntaxParser.LateCheckFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1529
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementSuppressIfQuestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_SUPPRESS_IF_OP)
            self.F = None # Token

        def SuppressIf(self):
            return self.getToken(SourceVfrSyntaxParser.SuppressIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementSuppressIfQuest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementSuppressIfQuest" ):
                return visitor.visitVfrStatementSuppressIfQuest(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementSuppressIfQuest(self):

        localctx = SourceVfrSyntaxParser.VfrStatementSuppressIfQuestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_vfrStatementSuppressIfQuest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1532
            self.match(SourceVfrSyntaxParser.SuppressIf)
            self.state = 1533
            self.vfrStatementExpression(localctx.Node)
            self.state = 1534
            self.match(SourceVfrSyntaxParser.Semicolon)
            self.state = 1547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1535
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1536
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1537
                self.flagsField()
                self.state = 1542
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 1538
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 1539
                    self.flagsField()
                    self.state = 1544
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1545
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1549
            self.vfrStatementQuestionOptionList(localctx.Node)
            self.state = 1550
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 1552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                self.state = 1551
                self.match(SourceVfrSyntaxParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementGrayOutIfQuestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_SUPPRESS_IF_OP)
            self.F = None # Token

        def GrayOutIf(self):
            return self.getToken(SourceVfrSyntaxParser.GrayOutIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementGrayOutIfQuest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementGrayOutIfQuest" ):
                return visitor.visitVfrStatementGrayOutIfQuest(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementGrayOutIfQuest(self):

        localctx = SourceVfrSyntaxParser.VfrStatementGrayOutIfQuestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_vfrStatementGrayOutIfQuest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1554
            self.match(SourceVfrSyntaxParser.GrayOutIf)
            self.state = 1555
            self.vfrStatementExpression(localctx.Node)
            self.state = 1556
            self.match(SourceVfrSyntaxParser.Semicolon)
            self.state = 1569
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1557
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1558
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1559
                self.flagsField()
                self.state = 1564
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 1560
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 1561
                    self.flagsField()
                    self.state = 1566
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1567
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1571
            self.vfrStatementQuestionOptionList(localctx.Node)
            self.state = 1572
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 1574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
            if la_ == 1:
                self.state = 1573
                self.match(SourceVfrSyntaxParser.Semicolon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementDefaultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_DEFAULT_OP)
            self.D = None # Token
            self.V = None # VfrStatementValueContext
            self.SN = None # Token

        def Default(self):
            return self.getToken(SourceVfrSyntaxParser.Default, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrConstantValueField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrConstantValueFieldContext,0)


        def vfrStatementValue(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementValueContext,0)


        def DefaultStore(self):
            return self.getToken(SourceVfrSyntaxParser.DefaultStore, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementDefault

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementDefault" ):
                return visitor.visitVfrStatementDefault(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementDefault(self):

        localctx = SourceVfrSyntaxParser.VfrStatementDefaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_vfrStatementDefault)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1576
            localctx.D = self.match(SourceVfrSyntaxParser.Default)

            self.state = 1584
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Value]:
                self.state = 1577
                localctx.V = self.vfrStatementValue()
                self.state = 1578
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            elif token in [SourceVfrSyntaxParser.T__5]:
                self.state = 1580
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1581
                self.vfrConstantValueField(localctx.Node)
                self.state = 1582
                self.match(SourceVfrSyntaxParser.Comma)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1590
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.DefaultStore:
                self.state = 1586
                self.match(SourceVfrSyntaxParser.DefaultStore)
                self.state = 1587
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1588
                localctx.SN = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 1589
                self.match(SourceVfrSyntaxParser.Comma)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_VALUE_OP)

        def Value(self):
            return self.getToken(SourceVfrSyntaxParser.Value, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementValue" ):
                return visitor.visitVfrStatementValue(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementValue(self):

        localctx = SourceVfrSyntaxParser.VfrStatementValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_vfrStatementValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1592
            self.match(SourceVfrSyntaxParser.Value)
            self.state = 1593
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1594
            self.vfrStatementExpression(localctx.Node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementOptionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementOneOfOption(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementOneOfOptionContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementOptions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementOptions" ):
                return visitor.visitVfrStatementOptions(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementOptions(self):

        localctx = SourceVfrSyntaxParser.VfrStatementOptionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_vfrStatementOptions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1596
            self.vfrStatementOneOfOption()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementOneOfOptionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_ONE_OF_OPTION_OP)
            self.S = None # Token
            self.F = None # Token
            self.KN = None # Token
            self.KS = None # Token
            self.T = None # Token

        def Option(self):
            return self.getToken(SourceVfrSyntaxParser.Option, 0)

        def Text(self):
            return self.getToken(SourceVfrSyntaxParser.Text, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Value(self):
            return self.getToken(SourceVfrSyntaxParser.Value, 0)

        def vfrConstantValueField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrConstantValueFieldContext,0)


        def vfrOneOfOptionFlags(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrOneOfOptionFlagsContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def Key(self):
            return self.getToken(SourceVfrSyntaxParser.Key, 0)

        def vfrImageTag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrImageTagContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrImageTagContext,i)


        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementOneOfOption

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementOneOfOption" ):
                return visitor.visitVfrStatementOneOfOption(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementOneOfOption(self):

        localctx = SourceVfrSyntaxParser.VfrStatementOneOfOptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_vfrStatementOneOfOption)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1598
            self.match(SourceVfrSyntaxParser.Option)
            self.state = 1599
            self.match(SourceVfrSyntaxParser.Text)
            self.state = 1600
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1601
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1602
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1603
            localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1604
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1605
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1606
            self.match(SourceVfrSyntaxParser.Value)
            self.state = 1607
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1608
            self.vfrConstantValueField(localctx.Node)
            self.state = 1609
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1610
            localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
            self.state = 1611
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1612
            self.vfrOneOfOptionFlags()
            self.state = 1620
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
            if la_ == 1:
                self.state = 1613
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1614
                self.match(SourceVfrSyntaxParser.Key)
                self.state = 1615
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1618
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1616
                    localctx.KN = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1617
                    localctx.KS = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 1626
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.Comma:
                self.state = 1622
                localctx.T = self.match(SourceVfrSyntaxParser.Comma)
                self.state = 1623
                self.vfrImageTag()
                self.state = 1628
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1629
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrOneOfOptionFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlags = 0
            self.LFlags = 0

        def oneofoptionFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.OneofoptionFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.OneofoptionFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrOneOfOptionFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrOneOfOptionFlags" ):
                return visitor.visitVfrOneOfOptionFlags(self)
            else:
                return visitor.visitChildren(self)




    def vfrOneOfOptionFlags(self):

        localctx = SourceVfrSyntaxParser.VfrOneOfOptionFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_vfrOneOfOptionFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1631
            self.oneofoptionFlagsField()
            self.state = 1636
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1632
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1633
                self.oneofoptionFlagsField()
                self.state = 1638
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OneofoptionFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlag = 0
            self.LFlag = 0
            self.A = None # Token
            self.L = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def OptionDefault(self):
            return self.getToken(SourceVfrSyntaxParser.OptionDefault, 0)

        def OptionDefaultMfg(self):
            return self.getToken(SourceVfrSyntaxParser.OptionDefaultMfg, 0)

        def InteractiveFlag(self):
            return self.getToken(SourceVfrSyntaxParser.InteractiveFlag, 0)

        def ResetRequiredFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ResetRequiredFlag, 0)

        def RestStyleFlag(self):
            return self.getToken(SourceVfrSyntaxParser.RestStyleFlag, 0)

        def ReconnectRequiredFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ReconnectRequiredFlag, 0)

        def ManufacturingFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ManufacturingFlag, 0)

        def DefaultFlag(self):
            return self.getToken(SourceVfrSyntaxParser.DefaultFlag, 0)

        def NVAccessFlag(self):
            return self.getToken(SourceVfrSyntaxParser.NVAccessFlag, 0)

        def LateCheckFlag(self):
            return self.getToken(SourceVfrSyntaxParser.LateCheckFlag, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_oneofoptionFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOneofoptionFlagsField" ):
                return visitor.visitOneofoptionFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def oneofoptionFlagsField(self):

        localctx = SourceVfrSyntaxParser.OneofoptionFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_oneofoptionFlagsField)
        try:
            self.state = 1651
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1639
                self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.OptionDefault]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1640
                self.match(SourceVfrSyntaxParser.OptionDefault)
                pass
            elif token in [SourceVfrSyntaxParser.OptionDefaultMfg]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1641
                self.match(SourceVfrSyntaxParser.OptionDefaultMfg)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1642
                self.match(SourceVfrSyntaxParser.InteractiveFlag)
                pass
            elif token in [SourceVfrSyntaxParser.ResetRequiredFlag]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1643
                self.match(SourceVfrSyntaxParser.ResetRequiredFlag)
                pass
            elif token in [SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1644
                self.match(SourceVfrSyntaxParser.RestStyleFlag)
                pass
            elif token in [SourceVfrSyntaxParser.ReconnectRequiredFlag]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1645
                self.match(SourceVfrSyntaxParser.ReconnectRequiredFlag)
                pass
            elif token in [SourceVfrSyntaxParser.ManufacturingFlag]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1646
                self.match(SourceVfrSyntaxParser.ManufacturingFlag)
                pass
            elif token in [SourceVfrSyntaxParser.DefaultFlag]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1647
                self.match(SourceVfrSyntaxParser.DefaultFlag)
                pass
            elif token in [SourceVfrSyntaxParser.NVAccessFlag]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1648
                localctx.A = self.match(SourceVfrSyntaxParser.NVAccessFlag)
                pass
            elif token in [SourceVfrSyntaxParser.LateCheckFlag]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1649
                localctx.L = self.match(SourceVfrSyntaxParser.LateCheckFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1650
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementReadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_READ_OP)

        def Read(self):
            return self.getToken(SourceVfrSyntaxParser.Read, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementRead

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementRead" ):
                return visitor.visitVfrStatementRead(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementRead(self):

        localctx = SourceVfrSyntaxParser.VfrStatementReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_vfrStatementRead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1653
            self.match(SourceVfrSyntaxParser.Read)
            self.state = 1654
            self.vfrStatementExpression(localctx.Node)
            self.state = 1655
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementWriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_WRITE_OP)

        def Write(self):
            return self.getToken(SourceVfrSyntaxParser.Write, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementWrite

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementWrite" ):
                return visitor.visitVfrStatementWrite(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementWrite(self):

        localctx = SourceVfrSyntaxParser.VfrStatementWriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_vfrStatementWrite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1657
            self.match(SourceVfrSyntaxParser.Write)
            self.state = 1658
            self.vfrStatementExpression(localctx.Node)
            self.state = 1659
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementQuestionOptionListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.Node = Node

        def vfrStatementQuestionOption(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementQuestionOptionContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementQuestionOptionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementQuestionOptionList" ):
                return visitor.visitVfrStatementQuestionOptionList(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementQuestionOptionList(self, Node):

        localctx = SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext(self, self._ctx, self.state, Node)
        self.enterRule(localctx, 180, self.RULE_vfrStatementQuestionOptionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1664
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & ((1 << (SourceVfrSyntaxParser.Option - 61)) | (1 << (SourceVfrSyntaxParser.GrayOutIf - 61)) | (1 << (SourceVfrSyntaxParser.Default - 61)) | (1 << (SourceVfrSyntaxParser.SuppressIf - 61)) | (1 << (SourceVfrSyntaxParser.DisableIf - 61)) | (1 << (SourceVfrSyntaxParser.InconsistentIf - 61)) | (1 << (SourceVfrSyntaxParser.WarningIf - 61)) | (1 << (SourceVfrSyntaxParser.NoSubmitIf - 61)))) != 0) or ((((_la - 144)) & ~0x3f) == 0 and ((1 << (_la - 144)) & ((1 << (SourceVfrSyntaxParser.Image - 144)) | (1 << (SourceVfrSyntaxParser.Locked - 144)) | (1 << (SourceVfrSyntaxParser.Value - 144)) | (1 << (SourceVfrSyntaxParser.Read - 144)) | (1 << (SourceVfrSyntaxParser.Write - 144)) | (1 << (SourceVfrSyntaxParser.Refresh - 144)) | (1 << (SourceVfrSyntaxParser.VarstoreDevice - 144)) | (1 << (SourceVfrSyntaxParser.GuidOp - 144)))) != 0) or _la==SourceVfrSyntaxParser.RefreshGuid or _la==SourceVfrSyntaxParser.StringIdentifier:
                self.state = 1661
                self.vfrStatementQuestionOption()
                self.state = 1666
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementQuestionOptionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementQuestionTag(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionTagContext,0)


        def vfrStatementQuestionOptionTag(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionTagContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementQuestionOption

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementQuestionOption" ):
                return visitor.visitVfrStatementQuestionOption(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementQuestionOption(self):

        localctx = SourceVfrSyntaxParser.VfrStatementQuestionOptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_vfrStatementQuestionOption)
        try:
            self.state = 1669
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.DisableIf, SourceVfrSyntaxParser.InconsistentIf, SourceVfrSyntaxParser.WarningIf, SourceVfrSyntaxParser.NoSubmitIf, SourceVfrSyntaxParser.Image, SourceVfrSyntaxParser.Locked, SourceVfrSyntaxParser.Refresh, SourceVfrSyntaxParser.VarstoreDevice, SourceVfrSyntaxParser.GuidOp, SourceVfrSyntaxParser.RefreshGuid, SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1667
                self.vfrStatementQuestionTag()
                pass
            elif token in [SourceVfrSyntaxParser.Option, SourceVfrSyntaxParser.GrayOutIf, SourceVfrSyntaxParser.Default, SourceVfrSyntaxParser.SuppressIf, SourceVfrSyntaxParser.Value, SourceVfrSyntaxParser.Read, SourceVfrSyntaxParser.Write]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1668
                self.vfrStatementQuestionOptionTag()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementBooleanTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementCheckBox(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementCheckBoxContext,0)


        def vfrStatementAction(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementActionContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementBooleanType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementBooleanType" ):
                return visitor.visitVfrStatementBooleanType(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementBooleanType(self):

        localctx = SourceVfrSyntaxParser.VfrStatementBooleanTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_vfrStatementBooleanType)
        try:
            self.state = 1673
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.CheckBox]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1671
                self.vfrStatementCheckBox()
                pass
            elif token in [SourceVfrSyntaxParser.Action]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1672
                self.vfrStatementAction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementCheckBoxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_CHECKBOX_OP)
            self.GuidNode = IfrTreeNode(EFI_IFR_GUID_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_NORMAL
            self.L = None # Token
            self.F = None # Token
            self.N = None # Token
            self.S = None # Token

        def vfrQuestionBaseInfo(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionBaseInfoContext,0)


        def vfrStatementHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementHeaderContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def EndCheckBox(self):
            return self.getToken(SourceVfrSyntaxParser.EndCheckBox, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def CheckBox(self):
            return self.getToken(SourceVfrSyntaxParser.CheckBox, 0)

        def vfrCheckBoxFlags(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrCheckBoxFlagsContext,0)


        def Key(self):
            return self.getToken(SourceVfrSyntaxParser.Key, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementCheckBox

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementCheckBox" ):
                return visitor.visitVfrStatementCheckBox(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementCheckBox(self):

        localctx = SourceVfrSyntaxParser.VfrStatementCheckBoxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_vfrStatementCheckBox)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1675
            localctx.L = self.match(SourceVfrSyntaxParser.CheckBox)
            self.state = 1676
            self.vfrQuestionBaseInfo(localctx.Node, localctx.QType)
            self.state = 1677
            self.vfrStatementHeader(localctx.Node)
            self.state = 1678
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1684
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1679
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1680
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1681
                self.vfrCheckBoxFlags()
                self.state = 1682
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1693
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Key:
                self.state = 1686
                self.match(SourceVfrSyntaxParser.Key)
                self.state = 1687
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1690
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1688
                    localctx.N = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1689
                    localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1692
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1695
            self.vfrStatementQuestionOptionList(localctx.Node)
            self.state = 1696
            self.match(SourceVfrSyntaxParser.EndCheckBox)
            self.state = 1697
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrCheckBoxFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.LFlags = 0
            self.HFlags = 0

        def checkboxFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.CheckboxFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.CheckboxFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrCheckBoxFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrCheckBoxFlags" ):
                return visitor.visitVfrCheckBoxFlags(self)
            else:
                return visitor.visitChildren(self)




    def vfrCheckBoxFlags(self):

        localctx = SourceVfrSyntaxParser.VfrCheckBoxFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_vfrCheckBoxFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1699
            self.checkboxFlagsField()
            self.state = 1704
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1700
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1701
                self.checkboxFlagsField()
                self.state = 1706
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CheckboxFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.LFlag = 0
            self.HFlag = 0
            self.D = None # Token
            self.M = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def DefaultFlag(self):
            return self.getToken(SourceVfrSyntaxParser.DefaultFlag, 0)

        def ManufacturingFlag(self):
            return self.getToken(SourceVfrSyntaxParser.ManufacturingFlag, 0)

        def CheckBoxDefaultFlag(self):
            return self.getToken(SourceVfrSyntaxParser.CheckBoxDefaultFlag, 0)

        def CheckBoxDefaultMfgFlag(self):
            return self.getToken(SourceVfrSyntaxParser.CheckBoxDefaultMfgFlag, 0)

        def questionheaderFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.QuestionheaderFlagsFieldContext,0)


        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_checkboxFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCheckboxFlagsField" ):
                return visitor.visitCheckboxFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def checkboxFlagsField(self):

        localctx = SourceVfrSyntaxParser.CheckboxFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_checkboxFlagsField)
        try:
            self.state = 1714
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1707
                self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.DefaultFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1708
                localctx.D = self.match(SourceVfrSyntaxParser.DefaultFlag)
                pass
            elif token in [SourceVfrSyntaxParser.ManufacturingFlag]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1709
                localctx.M = self.match(SourceVfrSyntaxParser.ManufacturingFlag)
                pass
            elif token in [SourceVfrSyntaxParser.CheckBoxDefaultFlag]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1710
                self.match(SourceVfrSyntaxParser.CheckBoxDefaultFlag)
                pass
            elif token in [SourceVfrSyntaxParser.CheckBoxDefaultMfgFlag]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1711
                self.match(SourceVfrSyntaxParser.CheckBoxDefaultMfgFlag)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag, SourceVfrSyntaxParser.NVAccessFlag, SourceVfrSyntaxParser.ResetRequiredFlag, SourceVfrSyntaxParser.ReconnectRequiredFlag, SourceVfrSyntaxParser.LateCheckFlag, SourceVfrSyntaxParser.ReadOnlyFlag, SourceVfrSyntaxParser.OptionOnlyFlag, SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1712
                self.questionheaderFlagsField()
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1713
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_ACTION_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_NORMAL
            self.S = None # Token

        def Action(self):
            return self.getToken(SourceVfrSyntaxParser.Action, 0)

        def vfrQuestionHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionHeaderContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Config(self):
            return self.getToken(SourceVfrSyntaxParser.Config, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def vfrStatementQuestionTagList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionTagListContext,0)


        def EndAction(self):
            return self.getToken(SourceVfrSyntaxParser.EndAction, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def vfrActionFlags(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrActionFlagsContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementAction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementAction" ):
                return visitor.visitVfrStatementAction(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementAction(self):

        localctx = SourceVfrSyntaxParser.VfrStatementActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_vfrStatementAction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1716
            self.match(SourceVfrSyntaxParser.Action)
            self.state = 1717
            self.vfrQuestionHeader(localctx.Node, localctx.QType)
            self.state = 1718
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1724
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1719
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1720
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1721
                self.vfrActionFlags()
                self.state = 1722
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1726
            self.match(SourceVfrSyntaxParser.Config)
            self.state = 1727
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1728
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 1729
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 1730
            localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 1731
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 1732
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1733
            self.vfrStatementQuestionTagList(localctx.Node)
            self.state = 1734
            self.match(SourceVfrSyntaxParser.EndAction)
            self.state = 1735
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrActionFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlags = 0

        def actionFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.ActionFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.ActionFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrActionFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrActionFlags" ):
                return visitor.visitVfrActionFlags(self)
            else:
                return visitor.visitChildren(self)




    def vfrActionFlags(self):

        localctx = SourceVfrSyntaxParser.VfrActionFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_vfrActionFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1737
            self.actionFlagsField()
            self.state = 1742
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1738
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1739
                self.actionFlagsField()
                self.state = 1744
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlag = 0
            self.N = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def questionheaderFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.QuestionheaderFlagsFieldContext,0)


        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_actionFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionFlagsField" ):
                return visitor.visitActionFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def actionFlagsField(self):

        localctx = SourceVfrSyntaxParser.ActionFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_actionFlagsField)
        try:
            self.state = 1748
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1745
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag, SourceVfrSyntaxParser.NVAccessFlag, SourceVfrSyntaxParser.ResetRequiredFlag, SourceVfrSyntaxParser.ReconnectRequiredFlag, SourceVfrSyntaxParser.LateCheckFlag, SourceVfrSyntaxParser.ReadOnlyFlag, SourceVfrSyntaxParser.OptionOnlyFlag, SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1746
                self.questionheaderFlagsField()
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1747
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementNumericTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementNumeric(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementNumericContext,0)


        def vfrStatementOneOf(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementOneOfContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementNumericType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementNumericType" ):
                return visitor.visitVfrStatementNumericType(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementNumericType(self):

        localctx = SourceVfrSyntaxParser.VfrStatementNumericTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_vfrStatementNumericType)
        try:
            self.state = 1752
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Numeric]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1750
                self.vfrStatementNumeric()
                pass
            elif token in [SourceVfrSyntaxParser.OneOf]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1751
                self.vfrStatementOneOf()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementNumericContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_NUMERIC_OP)
            self.GuidNode = IfrTreeNode(EFI_IFR_GUID_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_NORMAL
            self.F = None # Token
            self.N = None # Token
            self.S = None # Token

        def Numeric(self):
            return self.getToken(SourceVfrSyntaxParser.Numeric, 0)

        def vfrQuestionBaseInfo(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionBaseInfoContext,0)


        def vfrStatementHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementHeaderContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrSetMinMaxStep(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrSetMinMaxStepContext,0)


        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def EndNumeric(self):
            return self.getToken(SourceVfrSyntaxParser.EndNumeric, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def vfrNumericFlags(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrNumericFlagsContext,0)


        def Key(self):
            return self.getToken(SourceVfrSyntaxParser.Key, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementNumeric

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementNumeric" ):
                return visitor.visitVfrStatementNumeric(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementNumeric(self):

        localctx = SourceVfrSyntaxParser.VfrStatementNumericContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_vfrStatementNumeric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1754
            self.match(SourceVfrSyntaxParser.Numeric)
            self.state = 1755
            self.vfrQuestionBaseInfo(localctx.Node, localctx.QType)
            self.state = 1756
            self.vfrStatementHeader(localctx.Node)
            self.state = 1757
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1763
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1758
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1759
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1760
                self.vfrNumericFlags()
                self.state = 1761
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1772
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Key:
                self.state = 1765
                self.match(SourceVfrSyntaxParser.Key)
                self.state = 1766
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1769
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1767
                    localctx.N = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1768
                    localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1771
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1774
            self.vfrSetMinMaxStep(localctx.Node)
            self.state = 1775
            self.vfrStatementQuestionOptionList(localctx.Node)
            self.state = 1776
            self.match(SourceVfrSyntaxParser.EndNumeric)
            self.state = 1777
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrSetMinMaxStepContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.N1 = None # Token
            self.I = None # Token
            self.S1 = None # Token
            self.N2 = None # Token
            self.A = None # Token
            self.S2 = None # Token
            self.S = None # Token
            self.S3 = None # Token
            self.Node = Node

        def Minimum(self):
            return self.getToken(SourceVfrSyntaxParser.Minimum, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Maximum(self):
            return self.getToken(SourceVfrSyntaxParser.Maximum, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Step(self):
            return self.getToken(SourceVfrSyntaxParser.Step, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def Negative(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Negative)
            else:
                return self.getToken(SourceVfrSyntaxParser.Negative, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrSetMinMaxStep

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrSetMinMaxStep" ):
                return visitor.visitVfrSetMinMaxStep(self)
            else:
                return visitor.visitChildren(self)




    def vfrSetMinMaxStep(self, Node):

        localctx = SourceVfrSyntaxParser.VfrSetMinMaxStepContext(self, self._ctx, self.state, Node)
        self.enterRule(localctx, 202, self.RULE_vfrSetMinMaxStep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1779
            self.match(SourceVfrSyntaxParser.Minimum)
            self.state = 1780
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1786
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Negative, SourceVfrSyntaxParser.Number]:
                self.state = 1782
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SourceVfrSyntaxParser.Negative:
                    self.state = 1781
                    localctx.N1 = self.match(SourceVfrSyntaxParser.Negative)


                self.state = 1784
                localctx.I = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 1785
                localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1788
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1789
            self.match(SourceVfrSyntaxParser.Maximum)
            self.state = 1790
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1796
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Negative, SourceVfrSyntaxParser.Number]:
                self.state = 1792
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SourceVfrSyntaxParser.Negative:
                    self.state = 1791
                    localctx.N2 = self.match(SourceVfrSyntaxParser.Negative)


                self.state = 1794
                localctx.A = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 1795
                localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1798
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1806
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Step:
                self.state = 1799
                self.match(SourceVfrSyntaxParser.Step)
                self.state = 1800
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1803
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1801
                    localctx.S = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1802
                    localctx.S3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1805
                self.match(SourceVfrSyntaxParser.Comma)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrNumericFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlags = 0
            self.LFlags = 0
            self.IsDisplaySpecified = False
            self.UpdateVarType = False

        def numericFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.NumericFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.NumericFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrNumericFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrNumericFlags" ):
                return visitor.visitVfrNumericFlags(self)
            else:
                return visitor.visitChildren(self)




    def vfrNumericFlags(self):

        localctx = SourceVfrSyntaxParser.VfrNumericFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_vfrNumericFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1808
            self.numericFlagsField()
            self.state = 1813
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1809
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1810
                self.numericFlagsField()
                self.state = 1815
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlag = 0
            self.IsSetType = False
            self.IsDisplaySpecified = False
            self.N = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def NumericSizeOne(self):
            return self.getToken(SourceVfrSyntaxParser.NumericSizeOne, 0)

        def NumericSizeTwo(self):
            return self.getToken(SourceVfrSyntaxParser.NumericSizeTwo, 0)

        def NumericSizeFour(self):
            return self.getToken(SourceVfrSyntaxParser.NumericSizeFour, 0)

        def NumericSizeEight(self):
            return self.getToken(SourceVfrSyntaxParser.NumericSizeEight, 0)

        def DisPlayIntDec(self):
            return self.getToken(SourceVfrSyntaxParser.DisPlayIntDec, 0)

        def DisPlayUIntDec(self):
            return self.getToken(SourceVfrSyntaxParser.DisPlayUIntDec, 0)

        def DisPlayUIntHex(self):
            return self.getToken(SourceVfrSyntaxParser.DisPlayUIntHex, 0)

        def questionheaderFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.QuestionheaderFlagsFieldContext,0)


        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_numericFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericFlagsField" ):
                return visitor.visitNumericFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def numericFlagsField(self):

        localctx = SourceVfrSyntaxParser.NumericFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_numericFlagsField)
        try:
            self.state = 1826
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1816
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.NumericSizeOne]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1817
                self.match(SourceVfrSyntaxParser.NumericSizeOne)
                pass
            elif token in [SourceVfrSyntaxParser.NumericSizeTwo]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1818
                self.match(SourceVfrSyntaxParser.NumericSizeTwo)
                pass
            elif token in [SourceVfrSyntaxParser.NumericSizeFour]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1819
                self.match(SourceVfrSyntaxParser.NumericSizeFour)
                pass
            elif token in [SourceVfrSyntaxParser.NumericSizeEight]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1820
                self.match(SourceVfrSyntaxParser.NumericSizeEight)
                pass
            elif token in [SourceVfrSyntaxParser.DisPlayIntDec]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1821
                self.match(SourceVfrSyntaxParser.DisPlayIntDec)
                pass
            elif token in [SourceVfrSyntaxParser.DisPlayUIntDec]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1822
                self.match(SourceVfrSyntaxParser.DisPlayUIntDec)
                pass
            elif token in [SourceVfrSyntaxParser.DisPlayUIntHex]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1823
                self.match(SourceVfrSyntaxParser.DisPlayUIntHex)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag, SourceVfrSyntaxParser.NVAccessFlag, SourceVfrSyntaxParser.ResetRequiredFlag, SourceVfrSyntaxParser.ReconnectRequiredFlag, SourceVfrSyntaxParser.LateCheckFlag, SourceVfrSyntaxParser.ReadOnlyFlag, SourceVfrSyntaxParser.OptionOnlyFlag, SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1824
                self.questionheaderFlagsField()
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1825
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementOneOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_ONE_OF_OP)
            self.GuidNode = IfrTreeNode(EFI_IFR_GUID_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_NORMAL
            self.F = None # Token

        def OneOf(self):
            return self.getToken(SourceVfrSyntaxParser.OneOf, 0)

        def vfrQuestionBaseInfo(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionBaseInfoContext,0)


        def vfrStatementHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementHeaderContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def EndOneOf(self):
            return self.getToken(SourceVfrSyntaxParser.EndOneOf, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def vfrOneofFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrOneofFlagsFieldContext,0)


        def vfrSetMinMaxStep(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrSetMinMaxStepContext,0)


        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementOneOf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementOneOf" ):
                return visitor.visitVfrStatementOneOf(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementOneOf(self):

        localctx = SourceVfrSyntaxParser.VfrStatementOneOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_vfrStatementOneOf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1828
            self.match(SourceVfrSyntaxParser.OneOf)
            self.state = 1829
            self.vfrQuestionBaseInfo(localctx.Node, localctx.QType)
            self.state = 1830
            self.vfrStatementHeader(localctx.Node)
            self.state = 1831
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1837
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1832
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1833
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1834
                self.vfrOneofFlagsField()
                self.state = 1835
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1840
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Minimum:
                self.state = 1839
                self.vfrSetMinMaxStep(localctx.Node)


            self.state = 1842
            self.vfrStatementQuestionOptionList(localctx.Node)
            self.state = 1843
            self.match(SourceVfrSyntaxParser.EndOneOf)
            self.state = 1844
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrOneofFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlags = 0
            self.LFlags = 0
            self.UpdateVarType = False

        def numericFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.NumericFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.NumericFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrOneofFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrOneofFlagsField" ):
                return visitor.visitVfrOneofFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def vfrOneofFlagsField(self):

        localctx = SourceVfrSyntaxParser.VfrOneofFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_vfrOneofFlagsField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1846
            self.numericFlagsField()
            self.state = 1851
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1847
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1848
                self.numericFlagsField()
                self.state = 1853
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementStringTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementString(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStringContext,0)


        def vfrStatementPassword(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementPasswordContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementStringType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementStringType" ):
                return visitor.visitVfrStatementStringType(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementStringType(self):

        localctx = SourceVfrSyntaxParser.VfrStatementStringTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_vfrStatementStringType)
        try:
            self.state = 1856
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.String]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1854
                self.vfrStatementString()
                pass
            elif token in [SourceVfrSyntaxParser.Password]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1855
                self.vfrStatementPassword()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementStringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_STRING_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_NORMAL
            self.F = None # Token
            self.N = None # Token
            self.S = None # Token
            self.Min = None # Token
            self.N1 = None # Token
            self.S1 = None # Token
            self.Max = None # Token
            self.N2 = None # Token
            self.S2 = None # Token

        def String(self):
            return self.getToken(SourceVfrSyntaxParser.String, 0)

        def vfrQuestionHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionHeaderContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def EndString(self):
            return self.getToken(SourceVfrSyntaxParser.EndString, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def MinSize(self):
            return self.getToken(SourceVfrSyntaxParser.MinSize, 0)

        def MaxSize(self):
            return self.getToken(SourceVfrSyntaxParser.MaxSize, 0)

        def vfrStringFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStringFlagsFieldContext,0)


        def Key(self):
            return self.getToken(SourceVfrSyntaxParser.Key, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementString" ):
                return visitor.visitVfrStatementString(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementString(self):

        localctx = SourceVfrSyntaxParser.VfrStatementStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_vfrStatementString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1858
            self.match(SourceVfrSyntaxParser.String)
            self.state = 1859
            self.vfrQuestionHeader(localctx.Node, localctx.QType)
            self.state = 1860
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1866
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1861
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1862
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1863
                self.vfrStringFlagsField()
                self.state = 1864
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1875
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Key:
                self.state = 1868
                self.match(SourceVfrSyntaxParser.Key)
                self.state = 1869
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1872
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1870
                    localctx.N = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1871
                    localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1874
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1877
            localctx.Min = self.match(SourceVfrSyntaxParser.MinSize)
            self.state = 1878
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1881
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 1879
                localctx.N1 = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 1880
                localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1883
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1884
            localctx.Max = self.match(SourceVfrSyntaxParser.MaxSize)
            self.state = 1885
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1888
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 1886
                localctx.N2 = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 1887
                localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1890
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1891
            self.vfrStatementQuestionOptionList(localctx.Node)
            self.state = 1892
            self.match(SourceVfrSyntaxParser.EndString)
            self.state = 1893
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStringFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlags = 0
            self.LFlags = 0

        def stringFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.StringFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.StringFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStringFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStringFlagsField" ):
                return visitor.visitVfrStringFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def vfrStringFlagsField(self):

        localctx = SourceVfrSyntaxParser.VfrStringFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_vfrStringFlagsField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1895
            self.stringFlagsField()
            self.state = 1900
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1896
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1897
                self.stringFlagsField()
                self.state = 1902
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlag = 0
            self.LFlag = 0
            self.N = None # Token
            self.M = None # Token
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def questionheaderFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.QuestionheaderFlagsFieldContext,0)


        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_stringFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringFlagsField" ):
                return visitor.visitStringFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def stringFlagsField(self):

        localctx = SourceVfrSyntaxParser.StringFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_stringFlagsField)
        try:
            self.state = 1907
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1903
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1904
                localctx.M = self.match(SourceVfrSyntaxParser.T__8)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag, SourceVfrSyntaxParser.NVAccessFlag, SourceVfrSyntaxParser.ResetRequiredFlag, SourceVfrSyntaxParser.ReconnectRequiredFlag, SourceVfrSyntaxParser.LateCheckFlag, SourceVfrSyntaxParser.ReadOnlyFlag, SourceVfrSyntaxParser.OptionOnlyFlag, SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1905
                self.questionheaderFlagsField()
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1906
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementPasswordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_PASSWORD_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_NORMAL
            self.F = None # Token
            self.N = None # Token
            self.S = None # Token
            self.Min = None # Token
            self.N1 = None # Token
            self.S1 = None # Token
            self.Max = None # Token
            self.N2 = None # Token
            self.S2 = None # Token
            self.EN = None # Token
            self.ES = None # Token

        def Password(self):
            return self.getToken(SourceVfrSyntaxParser.Password, 0)

        def vfrQuestionHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionHeaderContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def EndPassword(self):
            return self.getToken(SourceVfrSyntaxParser.EndPassword, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def MinSize(self):
            return self.getToken(SourceVfrSyntaxParser.MinSize, 0)

        def MaxSize(self):
            return self.getToken(SourceVfrSyntaxParser.MaxSize, 0)

        def vfrPasswordFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrPasswordFlagsFieldContext,0)


        def Key(self):
            return self.getToken(SourceVfrSyntaxParser.Key, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Encoding(self):
            return self.getToken(SourceVfrSyntaxParser.Encoding, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementPassword

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementPassword" ):
                return visitor.visitVfrStatementPassword(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementPassword(self):

        localctx = SourceVfrSyntaxParser.VfrStatementPasswordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_vfrStatementPassword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1909
            self.match(SourceVfrSyntaxParser.Password)
            self.state = 1910
            self.vfrQuestionHeader(localctx.Node, localctx.QType)
            self.state = 1911
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1917
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1912
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1913
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1914
                self.vfrPasswordFlagsField()
                self.state = 1915
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1926
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Key:
                self.state = 1919
                self.match(SourceVfrSyntaxParser.Key)
                self.state = 1920
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1923
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1921
                    localctx.N = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1922
                    localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1925
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1928
            localctx.Min = self.match(SourceVfrSyntaxParser.MinSize)
            self.state = 1929
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1932
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 1930
                localctx.N1 = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 1931
                localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1934
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1935
            localctx.Max = self.match(SourceVfrSyntaxParser.MaxSize)
            self.state = 1936
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 1939
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 1937
                localctx.N2 = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 1938
                localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1941
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1949
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Encoding:
                self.state = 1942
                self.match(SourceVfrSyntaxParser.Encoding)
                self.state = 1943
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1946
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1944
                    localctx.EN = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1945
                    localctx.ES = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1948
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1951
            self.vfrStatementQuestionOptionList(localctx.Node)
            self.state = 1952
            self.match(SourceVfrSyntaxParser.EndPassword)
            self.state = 1953
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrPasswordFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlags = 0

        def passwordFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.PasswordFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.PasswordFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrPasswordFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrPasswordFlagsField" ):
                return visitor.visitVfrPasswordFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def vfrPasswordFlagsField(self):

        localctx = SourceVfrSyntaxParser.VfrPasswordFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_vfrPasswordFlagsField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1955
            self.passwordFlagsField()
            self.state = 1960
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1956
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1957
                self.passwordFlagsField()
                self.state = 1962
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PasswordFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlag = 0
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def questionheaderFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.QuestionheaderFlagsFieldContext,0)


        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_passwordFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPasswordFlagsField" ):
                return visitor.visitPasswordFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def passwordFlagsField(self):

        localctx = SourceVfrSyntaxParser.PasswordFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_passwordFlagsField)
        try:
            self.state = 1966
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1963
                self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag, SourceVfrSyntaxParser.NVAccessFlag, SourceVfrSyntaxParser.ResetRequiredFlag, SourceVfrSyntaxParser.ReconnectRequiredFlag, SourceVfrSyntaxParser.LateCheckFlag, SourceVfrSyntaxParser.ReadOnlyFlag, SourceVfrSyntaxParser.OptionOnlyFlag, SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1964
                self.questionheaderFlagsField()
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1965
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementOrderedListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_ORDERED_LIST_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_NORMAL
            self.M = None # Token
            self.N = None # Token
            self.S = None # Token
            self.F = None # Token

        def OrderedList(self):
            return self.getToken(SourceVfrSyntaxParser.OrderedList, 0)

        def vfrQuestionHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionHeaderContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def EndList(self):
            return self.getToken(SourceVfrSyntaxParser.EndList, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def vfrOrderedListFlags(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrOrderedListFlagsContext,0)


        def MaxContainers(self):
            return self.getToken(SourceVfrSyntaxParser.MaxContainers, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementOrderedList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementOrderedList" ):
                return visitor.visitVfrStatementOrderedList(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementOrderedList(self):

        localctx = SourceVfrSyntaxParser.VfrStatementOrderedListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_vfrStatementOrderedList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1968
            self.match(SourceVfrSyntaxParser.OrderedList)
            self.state = 1969
            self.vfrQuestionHeader(localctx.Node, localctx.QType)
            self.state = 1970
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 1978
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.MaxContainers:
                self.state = 1971
                localctx.M = self.match(SourceVfrSyntaxParser.MaxContainers)
                self.state = 1972
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1975
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 1973
                    localctx.N = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 1974
                    localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1977
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1985
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 1980
                localctx.F = self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 1981
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 1982
                self.vfrOrderedListFlags()
                self.state = 1983
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 1987
            self.vfrStatementQuestionOptionList(localctx.Node)
            self.state = 1988
            self.match(SourceVfrSyntaxParser.EndList)
            self.state = 1989
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrOrderedListFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlags = 0
            self.LFlags = 0

        def orderedlistFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.OrderedlistFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.OrderedlistFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrOrderedListFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrOrderedListFlags" ):
                return visitor.visitVfrOrderedListFlags(self)
            else:
                return visitor.visitChildren(self)




    def vfrOrderedListFlags(self):

        localctx = SourceVfrSyntaxParser.VfrOrderedListFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_vfrOrderedListFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1991
            self.orderedlistFlagsField()
            self.state = 1996
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 1992
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 1993
                self.orderedlistFlagsField()
                self.state = 1998
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderedlistFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.HFlag = 0
            self.LFlag = 0
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def UniQueFlag(self):
            return self.getToken(SourceVfrSyntaxParser.UniQueFlag, 0)

        def NoEmptyFlag(self):
            return self.getToken(SourceVfrSyntaxParser.NoEmptyFlag, 0)

        def questionheaderFlagsField(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.QuestionheaderFlagsFieldContext,0)


        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_orderedlistFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderedlistFlagsField" ):
                return visitor.visitOrderedlistFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def orderedlistFlagsField(self):

        localctx = SourceVfrSyntaxParser.OrderedlistFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_orderedlistFlagsField)
        try:
            self.state = 2004
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1999
                self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.UniQueFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2000
                self.match(SourceVfrSyntaxParser.UniQueFlag)
                pass
            elif token in [SourceVfrSyntaxParser.NoEmptyFlag]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2001
                self.match(SourceVfrSyntaxParser.NoEmptyFlag)
                pass
            elif token in [SourceVfrSyntaxParser.InteractiveFlag, SourceVfrSyntaxParser.NVAccessFlag, SourceVfrSyntaxParser.ResetRequiredFlag, SourceVfrSyntaxParser.ReconnectRequiredFlag, SourceVfrSyntaxParser.LateCheckFlag, SourceVfrSyntaxParser.ReadOnlyFlag, SourceVfrSyntaxParser.OptionOnlyFlag, SourceVfrSyntaxParser.RestStyleFlag]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2002
                self.questionheaderFlagsField()
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2003
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementDateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_DATE_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_DATE
            self.Val = EFI_HII_DATE()
            self.F1 = None # Token
            self.S1 = None # Token
            self.S2 = None # Token
            self.S3 = None # Token
            self.S4 = None # Token
            self.S5 = None # Token
            self.S6 = None # Token
            self.S7 = None # Token
            self.S8 = None # Token
            self.S9 = None # Token
            self.S10 = None # Token
            self.S11 = None # Token
            self.S12 = None # Token
            self.F2 = None # Token

        def Date(self):
            return self.getToken(SourceVfrSyntaxParser.Date, 0)

        def EndDate(self):
            return self.getToken(SourceVfrSyntaxParser.EndDate, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def vfrQuestionHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionHeaderContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def Year(self):
            return self.getToken(SourceVfrSyntaxParser.Year, 0)

        def VarId(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.VarId)
            else:
                return self.getToken(SourceVfrSyntaxParser.VarId, i)

        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Dot)
            else:
                return self.getToken(SourceVfrSyntaxParser.Dot, i)

        def Prompt(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Prompt)
            else:
                return self.getToken(SourceVfrSyntaxParser.Prompt, i)

        def StringToken(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringToken)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringToken, i)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def Help(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Help)
            else:
                return self.getToken(SourceVfrSyntaxParser.Help, i)

        def minMaxDateStepDefault(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.MinMaxDateStepDefaultContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.MinMaxDateStepDefaultContext,i)


        def Month(self):
            return self.getToken(SourceVfrSyntaxParser.Month, 0)

        def Day(self):
            return self.getToken(SourceVfrSyntaxParser.Day, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def vfrDateFlags(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrDateFlagsContext,0)


        def vfrStatementInconsistentIf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementInconsistentIfContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInconsistentIfContext,i)


        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementDate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementDate" ):
                return visitor.visitVfrStatementDate(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementDate(self):

        localctx = SourceVfrSyntaxParser.VfrStatementDateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_vfrStatementDate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2006
            self.match(SourceVfrSyntaxParser.Date)
            self.state = 2097
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Prompt, SourceVfrSyntaxParser.Name, SourceVfrSyntaxParser.VarId, SourceVfrSyntaxParser.QuestionId]:
                self.state = 2007
                self.vfrQuestionHeader(localctx.Node, localctx.QType)
                self.state = 2008
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2014
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SourceVfrSyntaxParser.FLAGS:
                    self.state = 2009
                    localctx.F1 = self.match(SourceVfrSyntaxParser.FLAGS)
                    self.state = 2010
                    self.match(SourceVfrSyntaxParser.T__5)
                    self.state = 2011
                    self.vfrDateFlags()
                    self.state = 2012
                    self.match(SourceVfrSyntaxParser.Comma)


                self.state = 2016
                self.vfrStatementQuestionOptionList(localctx.Node)
                pass
            elif token in [SourceVfrSyntaxParser.Year]:
                self.state = 2018
                self.match(SourceVfrSyntaxParser.Year)
                self.state = 2019
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 2020
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2021
                localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2022
                self.match(SourceVfrSyntaxParser.Dot)
                self.state = 2023
                localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2024
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2025
                self.match(SourceVfrSyntaxParser.Prompt)
                self.state = 2026
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2027
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2028
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2029
                localctx.S3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2030
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2031
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2032
                self.match(SourceVfrSyntaxParser.Help)
                self.state = 2033
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2034
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2035
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2036
                localctx.S4 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2037
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2038
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2039
                self.minMaxDateStepDefault(localctx.Node, localctx.Val, 0)
                self.state = 2040
                self.match(SourceVfrSyntaxParser.Month)
                self.state = 2041
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 2042
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2043
                localctx.S5 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2044
                self.match(SourceVfrSyntaxParser.Dot)
                self.state = 2045
                localctx.S6 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2046
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2047
                self.match(SourceVfrSyntaxParser.Prompt)
                self.state = 2048
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2049
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2050
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2051
                localctx.S7 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2052
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2053
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2054
                self.match(SourceVfrSyntaxParser.Help)
                self.state = 2055
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2056
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2057
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2058
                localctx.S8 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2059
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2060
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2061
                self.minMaxDateStepDefault(localctx.Node, localctx.Val, 1)
                self.state = 2062
                self.match(SourceVfrSyntaxParser.Day)
                self.state = 2063
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 2064
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2065
                localctx.S9 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2066
                self.match(SourceVfrSyntaxParser.Dot)
                self.state = 2067
                localctx.S10 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2068
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2069
                self.match(SourceVfrSyntaxParser.Prompt)
                self.state = 2070
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2071
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2072
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2073
                localctx.S11 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2074
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2075
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2076
                self.match(SourceVfrSyntaxParser.Help)
                self.state = 2077
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2078
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2079
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2080
                localctx.S12 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2081
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2082
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2083
                self.minMaxDateStepDefault(localctx.Node, localctx.Val, 2)
                self.state = 2089
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SourceVfrSyntaxParser.FLAGS:
                    self.state = 2084
                    localctx.F2 = self.match(SourceVfrSyntaxParser.FLAGS)
                    self.state = 2085
                    self.match(SourceVfrSyntaxParser.T__5)
                    self.state = 2086
                    self.vfrDateFlags()
                    self.state = 2087
                    self.match(SourceVfrSyntaxParser.Comma)


                self.state = 2094
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.InconsistentIf:
                    self.state = 2091
                    self.vfrStatementInconsistentIf()
                    self.state = 2096
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 2099
            self.match(SourceVfrSyntaxParser.EndDate)
            self.state = 2100
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MinMaxDateStepDefaultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None, Date=None, KeyValue=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.Date = None
            self.KeyValue = None
            self.N1 = None # Token
            self.S1 = None # Token
            self.N2 = None # Token
            self.S2 = None # Token
            self.N3 = None # Token
            self.S3 = None # Token
            self.D = None # Token
            self.N4 = None # Token
            self.S4 = None # Token
            self.Node = Node
            self.Date = Date
            self.KeyValue = KeyValue

        def Minimum(self):
            return self.getToken(SourceVfrSyntaxParser.Minimum, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Maximum(self):
            return self.getToken(SourceVfrSyntaxParser.Maximum, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Step(self):
            return self.getToken(SourceVfrSyntaxParser.Step, 0)

        def Default(self):
            return self.getToken(SourceVfrSyntaxParser.Default, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_minMaxDateStepDefault

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinMaxDateStepDefault" ):
                return visitor.visitMinMaxDateStepDefault(self)
            else:
                return visitor.visitChildren(self)




    def minMaxDateStepDefault(self, Node, Date, KeyValue):

        localctx = SourceVfrSyntaxParser.MinMaxDateStepDefaultContext(self, self._ctx, self.state, Node, Date, KeyValue)
        self.enterRule(localctx, 234, self.RULE_minMaxDateStepDefault)
        try:
            self.state = 2126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,192,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2102
                self.match(SourceVfrSyntaxParser.Minimum)
                self.state = 2103
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2104
                localctx.N1 = self.match(SourceVfrSyntaxParser.Number)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2105
                localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2106
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2107
                self.match(SourceVfrSyntaxParser.Maximum)
                self.state = 2108
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2109
                localctx.N2 = self.match(SourceVfrSyntaxParser.Number)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2110
                localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2111
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2117
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,190,self._ctx)
                if la_ == 1:
                    self.state = 2112
                    self.match(SourceVfrSyntaxParser.Step)
                    self.state = 2113
                    self.match(SourceVfrSyntaxParser.T__5)
                    self.state = 2114
                    localctx.N3 = self.match(SourceVfrSyntaxParser.Number)

                elif la_ == 2:
                    self.state = 2115
                    localctx.S3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    self.state = 2116
                    self.match(SourceVfrSyntaxParser.Comma)


                self.state = 2124
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Default]:
                    self.state = 2119
                    localctx.D = self.match(SourceVfrSyntaxParser.Default)
                    self.state = 2120
                    self.match(SourceVfrSyntaxParser.T__5)
                    self.state = 2121
                    localctx.N4 = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 2122
                    localctx.S4 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    self.state = 2123
                    self.match(SourceVfrSyntaxParser.Comma)
                    pass
                elif token in [SourceVfrSyntaxParser.FLAGS, SourceVfrSyntaxParser.EndDate, SourceVfrSyntaxParser.Month, SourceVfrSyntaxParser.Day, SourceVfrSyntaxParser.InconsistentIf]:
                    pass
                else:
                    pass
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrDateFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.LFlags = 0

        def dateFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.DateFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.DateFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrDateFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrDateFlags" ):
                return visitor.visitVfrDateFlags(self)
            else:
                return visitor.visitChildren(self)




    def vfrDateFlags(self):

        localctx = SourceVfrSyntaxParser.VfrDateFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_vfrDateFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2128
            self.dateFlagsField()
            self.state = 2133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 2129
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 2130
                self.dateFlagsField()
                self.state = 2135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.LFlag = 0
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def YearSupppressFlag(self):
            return self.getToken(SourceVfrSyntaxParser.YearSupppressFlag, 0)

        def MonthSuppressFlag(self):
            return self.getToken(SourceVfrSyntaxParser.MonthSuppressFlag, 0)

        def DaySuppressFlag(self):
            return self.getToken(SourceVfrSyntaxParser.DaySuppressFlag, 0)

        def StorageNormalFlag(self):
            return self.getToken(SourceVfrSyntaxParser.StorageNormalFlag, 0)

        def StorageTimeFlag(self):
            return self.getToken(SourceVfrSyntaxParser.StorageTimeFlag, 0)

        def StorageWakeUpFlag(self):
            return self.getToken(SourceVfrSyntaxParser.StorageWakeUpFlag, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dateFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateFlagsField" ):
                return visitor.visitDateFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def dateFlagsField(self):

        localctx = SourceVfrSyntaxParser.DateFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_dateFlagsField)
        try:
            self.state = 2144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2136
                self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.YearSupppressFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2137
                self.match(SourceVfrSyntaxParser.YearSupppressFlag)
                pass
            elif token in [SourceVfrSyntaxParser.MonthSuppressFlag]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2138
                self.match(SourceVfrSyntaxParser.MonthSuppressFlag)
                pass
            elif token in [SourceVfrSyntaxParser.DaySuppressFlag]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2139
                self.match(SourceVfrSyntaxParser.DaySuppressFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StorageNormalFlag]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2140
                self.match(SourceVfrSyntaxParser.StorageNormalFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StorageTimeFlag]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2141
                self.match(SourceVfrSyntaxParser.StorageTimeFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StorageWakeUpFlag]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2142
                self.match(SourceVfrSyntaxParser.StorageWakeUpFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2143
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementTimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_TIME_OP)
            self.QType = EFI_QUESION_TYPE.QUESTION_TIME
            self.Val = EFI_HII_TIME()
            self.F1 = None # Token
            self.S1 = None # Token
            self.S2 = None # Token
            self.S3 = None # Token
            self.S4 = None # Token
            self.S5 = None # Token
            self.S6 = None # Token
            self.S7 = None # Token
            self.S8 = None # Token
            self.S9 = None # Token
            self.S10 = None # Token
            self.S11 = None # Token
            self.S12 = None # Token
            self.F2 = None # Token

        def Time(self):
            return self.getToken(SourceVfrSyntaxParser.Time, 0)

        def EndTime(self):
            return self.getToken(SourceVfrSyntaxParser.EndTime, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def vfrQuestionHeader(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionHeaderContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementQuestionOptionList(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionOptionListContext,0)


        def Hour(self):
            return self.getToken(SourceVfrSyntaxParser.Hour, 0)

        def VarId(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.VarId)
            else:
                return self.getToken(SourceVfrSyntaxParser.VarId, i)

        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Dot)
            else:
                return self.getToken(SourceVfrSyntaxParser.Dot, i)

        def Prompt(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Prompt)
            else:
                return self.getToken(SourceVfrSyntaxParser.Prompt, i)

        def StringToken(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringToken)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringToken, i)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def Help(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Help)
            else:
                return self.getToken(SourceVfrSyntaxParser.Help, i)

        def minMaxTimeStepDefault(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.MinMaxTimeStepDefaultContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.MinMaxTimeStepDefaultContext,i)


        def Minute(self):
            return self.getToken(SourceVfrSyntaxParser.Minute, 0)

        def Second(self):
            return self.getToken(SourceVfrSyntaxParser.Second, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def vfrTimeFlags(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrTimeFlagsContext,0)


        def vfrStatementInconsistentIf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementInconsistentIfContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInconsistentIfContext,i)


        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementTime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementTime" ):
                return visitor.visitVfrStatementTime(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementTime(self):

        localctx = SourceVfrSyntaxParser.VfrStatementTimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_vfrStatementTime)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2146
            self.match(SourceVfrSyntaxParser.Time)
            self.state = 2237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Prompt, SourceVfrSyntaxParser.Name, SourceVfrSyntaxParser.VarId, SourceVfrSyntaxParser.QuestionId]:
                self.state = 2147
                self.vfrQuestionHeader(localctx.Node, localctx.QType)
                self.state = 2148
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SourceVfrSyntaxParser.FLAGS:
                    self.state = 2149
                    localctx.F1 = self.match(SourceVfrSyntaxParser.FLAGS)
                    self.state = 2150
                    self.match(SourceVfrSyntaxParser.T__5)
                    self.state = 2151
                    self.vfrTimeFlags()
                    self.state = 2152
                    self.match(SourceVfrSyntaxParser.Comma)


                self.state = 2156
                self.vfrStatementQuestionOptionList(localctx.Node)
                pass
            elif token in [SourceVfrSyntaxParser.Hour]:
                self.state = 2158
                self.match(SourceVfrSyntaxParser.Hour)
                self.state = 2159
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 2160
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2161
                localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2162
                self.match(SourceVfrSyntaxParser.Dot)
                self.state = 2163
                localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2164
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2165
                self.match(SourceVfrSyntaxParser.Prompt)
                self.state = 2166
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2167
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2168
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2169
                localctx.S3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2170
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2171
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2172
                self.match(SourceVfrSyntaxParser.Help)
                self.state = 2173
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2174
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2175
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2176
                localctx.S4 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2177
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2178
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2179
                self.minMaxTimeStepDefault(localctx.Node. localctx.Val, 0)
                self.state = 2180
                self.match(SourceVfrSyntaxParser.Minute)
                self.state = 2181
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 2182
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2183
                localctx.S5 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2184
                self.match(SourceVfrSyntaxParser.Dot)
                self.state = 2185
                localctx.S6 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2186
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2187
                self.match(SourceVfrSyntaxParser.Prompt)
                self.state = 2188
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2189
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2190
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2191
                localctx.S7 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2192
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2193
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2194
                self.match(SourceVfrSyntaxParser.Help)
                self.state = 2195
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2196
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2197
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2198
                localctx.S8 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2199
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2200
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2201
                self.minMaxTimeStepDefault(localctx.Node, localctx.Val, 1)
                self.state = 2202
                self.match(SourceVfrSyntaxParser.Second)
                self.state = 2203
                self.match(SourceVfrSyntaxParser.VarId)
                self.state = 2204
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2205
                localctx.S9 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2206
                self.match(SourceVfrSyntaxParser.Dot)
                self.state = 2207
                localctx.S10 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2208
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2209
                self.match(SourceVfrSyntaxParser.Prompt)
                self.state = 2210
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2211
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2212
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2213
                localctx.S11 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2214
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2215
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2216
                self.match(SourceVfrSyntaxParser.Help)
                self.state = 2217
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2218
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2219
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2220
                localctx.S12 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2221
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 2222
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2223
                self.minMaxTimeStepDefault(localctx.Node, localctx.Val, 2)
                self.state = 2229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SourceVfrSyntaxParser.FLAGS:
                    self.state = 2224
                    localctx.F2 = self.match(SourceVfrSyntaxParser.FLAGS)
                    self.state = 2225
                    self.match(SourceVfrSyntaxParser.T__5)
                    self.state = 2226
                    self.vfrTimeFlags()
                    self.state = 2227
                    self.match(SourceVfrSyntaxParser.Comma)


                self.state = 2234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.InconsistentIf:
                    self.state = 2231
                    self.vfrStatementInconsistentIf()
                    self.state = 2236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 2239
            self.match(SourceVfrSyntaxParser.EndTime)
            self.state = 2240
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MinMaxTimeStepDefaultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, Node=None, Time=None, KeyValue=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None
            self.Time = None
            self.KeyValue = None
            self.N1 = None # Token
            self.S1 = None # Token
            self.N2 = None # Token
            self.S2 = None # Token
            self.N3 = None # Token
            self.S3 = None # Token
            self.D = None # Token
            self.N4 = None # Token
            self.S4 = None # Token
            self.Node = Node
            self.Time = Time
            self.KeyValue = KeyValue

        def Minimum(self):
            return self.getToken(SourceVfrSyntaxParser.Minimum, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Maximum(self):
            return self.getToken(SourceVfrSyntaxParser.Maximum, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Step(self):
            return self.getToken(SourceVfrSyntaxParser.Step, 0)

        def Default(self):
            return self.getToken(SourceVfrSyntaxParser.Default, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_minMaxTimeStepDefault

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinMaxTimeStepDefault" ):
                return visitor.visitMinMaxTimeStepDefault(self)
            else:
                return visitor.visitChildren(self)




    def minMaxTimeStepDefault(self, Node, Time, KeyValue):

        localctx = SourceVfrSyntaxParser.MinMaxTimeStepDefaultContext(self, self._ctx, self.state, Node, Time, KeyValue)
        self.enterRule(localctx, 242, self.RULE_minMaxTimeStepDefault)
        try:
            self.state = 2266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,201,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2242
                self.match(SourceVfrSyntaxParser.Minimum)
                self.state = 2243
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2244
                localctx.N1 = self.match(SourceVfrSyntaxParser.Number)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2245
                localctx.S1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2246
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2247
                self.match(SourceVfrSyntaxParser.Maximum)
                self.state = 2248
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2249
                localctx.N2 = self.match(SourceVfrSyntaxParser.Number)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2250
                localctx.S2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2251
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2257
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,199,self._ctx)
                if la_ == 1:
                    self.state = 2252
                    self.match(SourceVfrSyntaxParser.Step)
                    self.state = 2253
                    self.match(SourceVfrSyntaxParser.T__5)
                    self.state = 2254
                    localctx.N3 = self.match(SourceVfrSyntaxParser.Number)

                elif la_ == 2:
                    self.state = 2255
                    localctx.S3 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    self.state = 2256
                    self.match(SourceVfrSyntaxParser.Comma)


                self.state = 2264
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Default]:
                    self.state = 2259
                    localctx.D = self.match(SourceVfrSyntaxParser.Default)
                    self.state = 2260
                    self.match(SourceVfrSyntaxParser.T__5)
                    self.state = 2261
                    localctx.N4 = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 2262
                    localctx.S4 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    self.state = 2263
                    self.match(SourceVfrSyntaxParser.Comma)
                    pass
                elif token in [SourceVfrSyntaxParser.FLAGS, SourceVfrSyntaxParser.EndTime, SourceVfrSyntaxParser.Minute, SourceVfrSyntaxParser.Second, SourceVfrSyntaxParser.InconsistentIf]:
                    pass
                else:
                    pass
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrTimeFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.LFlags = 0

        def timeFlagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.TimeFlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.TimeFlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrTimeFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrTimeFlags" ):
                return visitor.visitVfrTimeFlags(self)
            else:
                return visitor.visitChildren(self)




    def vfrTimeFlags(self):

        localctx = SourceVfrSyntaxParser.VfrTimeFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_vfrTimeFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2268
            self.timeFlagsField()
            self.state = 2273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 2269
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 2270
                self.timeFlagsField()
                self.state = 2275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeFlagsFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.LFlag = 0
            self.S = None # Token

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def HourSupppressFlag(self):
            return self.getToken(SourceVfrSyntaxParser.HourSupppressFlag, 0)

        def MinuteSuppressFlag(self):
            return self.getToken(SourceVfrSyntaxParser.MinuteSuppressFlag, 0)

        def SecondSuppressFlag(self):
            return self.getToken(SourceVfrSyntaxParser.SecondSuppressFlag, 0)

        def StorageNormalFlag(self):
            return self.getToken(SourceVfrSyntaxParser.StorageNormalFlag, 0)

        def StorageTimeFlag(self):
            return self.getToken(SourceVfrSyntaxParser.StorageTimeFlag, 0)

        def StorageWakeUpFlag(self):
            return self.getToken(SourceVfrSyntaxParser.StorageWakeUpFlag, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_timeFlagsField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeFlagsField" ):
                return visitor.visitTimeFlagsField(self)
            else:
                return visitor.visitChildren(self)




    def timeFlagsField(self):

        localctx = SourceVfrSyntaxParser.TimeFlagsFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_timeFlagsField)
        try:
            self.state = 2284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2276
                self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.HourSupppressFlag]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2277
                self.match(SourceVfrSyntaxParser.HourSupppressFlag)
                pass
            elif token in [SourceVfrSyntaxParser.MinuteSuppressFlag]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2278
                self.match(SourceVfrSyntaxParser.MinuteSuppressFlag)
                pass
            elif token in [SourceVfrSyntaxParser.SecondSuppressFlag]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2279
                self.match(SourceVfrSyntaxParser.SecondSuppressFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StorageNormalFlag]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2280
                self.match(SourceVfrSyntaxParser.StorageNormalFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StorageTimeFlag]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2281
                self.match(SourceVfrSyntaxParser.StorageTimeFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StorageWakeUpFlag]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2282
                self.match(SourceVfrSyntaxParser.StorageWakeUpFlag)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2283
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementDisableIfStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementDisableIfStatContext,0)


        def vfrStatementSuppressIfStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementSuppressIfStatContext,0)


        def vfrStatementGrayOutIfStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementGrayOutIfStatContext,0)


        def vfrStatementInconsistentIfStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInconsistentIfStatContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementConditional" ):
                return visitor.visitVfrStatementConditional(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementConditional(self):

        localctx = SourceVfrSyntaxParser.VfrStatementConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_vfrStatementConditional)
        try:
            self.state = 2290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.DisableIf]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2286
                self.vfrStatementDisableIfStat()
                pass
            elif token in [SourceVfrSyntaxParser.SuppressIf]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2287
                self.vfrStatementSuppressIfStat()
                pass
            elif token in [SourceVfrSyntaxParser.GrayOutIf]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2288
                self.vfrStatementGrayOutIfStat()
                pass
            elif token in [SourceVfrSyntaxParser.InconsistentIf]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2289
                self.vfrStatementInconsistentIfStat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementConditionalNewContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementDisableIfStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementDisableIfStatContext,0)


        def vfrStatementSuppressIfStatNew(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementSuppressIfStatNewContext,0)


        def vfrStatementGrayOutIfStatNew(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementGrayOutIfStatNewContext,0)


        def vfrStatementInconsistentIfStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInconsistentIfStatContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementConditionalNew

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementConditionalNew" ):
                return visitor.visitVfrStatementConditionalNew(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementConditionalNew(self):

        localctx = SourceVfrSyntaxParser.VfrStatementConditionalNewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_vfrStatementConditionalNew)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2292
            self.vfrStatementDisableIfStat()
            self.state = 2293
            self.vfrStatementSuppressIfStatNew()
            self.state = 2294
            self.vfrStatementGrayOutIfStatNew()
            self.state = 2295
            self.vfrStatementInconsistentIfStat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementSuppressIfStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementSuppressIfStatNew(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementSuppressIfStatNewContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementSuppressIfStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementSuppressIfStat" ):
                return visitor.visitVfrStatementSuppressIfStat(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementSuppressIfStat(self):

        localctx = SourceVfrSyntaxParser.VfrStatementSuppressIfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_vfrStatementSuppressIfStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2297
            self.vfrStatementSuppressIfStatNew()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementGrayOutIfStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementGrayOutIfStatNew(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementGrayOutIfStatNewContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementGrayOutIfStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementGrayOutIfStat" ):
                return visitor.visitVfrStatementGrayOutIfStat(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementGrayOutIfStat(self):

        localctx = SourceVfrSyntaxParser.VfrStatementGrayOutIfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_vfrStatementGrayOutIfStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2299
            self.vfrStatementGrayOutIfStatNew()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementStatListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrStatementStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatContext,0)


        def vfrStatementQuestions(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionsContext,0)


        def vfrStatementConditional(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementConditionalContext,0)


        def vfrStatementLabel(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementLabelContext,0)


        def vfrStatementExtension(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExtensionContext,0)


        def vfrStatementInvalid(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInvalidContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementStatList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementStatList" ):
                return visitor.visitVfrStatementStatList(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementStatList(self):

        localctx = SourceVfrSyntaxParser.VfrStatementStatListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_vfrStatementStatList)
        try:
            self.state = 2307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Subtitle, SourceVfrSyntaxParser.Text, SourceVfrSyntaxParser.Goto, SourceVfrSyntaxParser.ResetButton]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2301
                self.vfrStatementStat()
                pass
            elif token in [SourceVfrSyntaxParser.OneOf, SourceVfrSyntaxParser.OrderedList, SourceVfrSyntaxParser.Date, SourceVfrSyntaxParser.Time, SourceVfrSyntaxParser.CheckBox, SourceVfrSyntaxParser.Numeric, SourceVfrSyntaxParser.Password, SourceVfrSyntaxParser.String, SourceVfrSyntaxParser.Action]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2302
                self.vfrStatementQuestions()
                pass
            elif token in [SourceVfrSyntaxParser.GrayOutIf, SourceVfrSyntaxParser.SuppressIf, SourceVfrSyntaxParser.DisableIf, SourceVfrSyntaxParser.InconsistentIf]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2303
                self.vfrStatementConditional()
                pass
            elif token in [SourceVfrSyntaxParser.Label]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2304
                self.vfrStatementLabel()
                pass
            elif token in [SourceVfrSyntaxParser.GuidOp]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2305
                self.vfrStatementExtension()
                pass
            elif token in [SourceVfrSyntaxParser.Inventory, SourceVfrSyntaxParser.Hidden, SourceVfrSyntaxParser.Restore, SourceVfrSyntaxParser.Save]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2306
                self.vfrStatementInvalid()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementStatListOldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vfrStatementStat(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatContext,0)


        def vfrStatementQuestions(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementQuestionsContext,0)


        def vfrStatementLabel(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementLabelContext,0)


        def vfrStatementInvalid(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInvalidContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementStatListOld

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementStatListOld" ):
                return visitor.visitVfrStatementStatListOld(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementStatListOld(self):

        localctx = SourceVfrSyntaxParser.VfrStatementStatListOldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_vfrStatementStatListOld)
        try:
            self.state = 2313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Subtitle, SourceVfrSyntaxParser.Text, SourceVfrSyntaxParser.Goto, SourceVfrSyntaxParser.ResetButton]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2309
                self.vfrStatementStat()
                pass
            elif token in [SourceVfrSyntaxParser.OneOf, SourceVfrSyntaxParser.OrderedList, SourceVfrSyntaxParser.Date, SourceVfrSyntaxParser.Time, SourceVfrSyntaxParser.CheckBox, SourceVfrSyntaxParser.Numeric, SourceVfrSyntaxParser.Password, SourceVfrSyntaxParser.String, SourceVfrSyntaxParser.Action]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2310
                self.vfrStatementQuestions()
                pass
            elif token in [SourceVfrSyntaxParser.Label]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2311
                self.vfrStatementLabel()
                pass
            elif token in [SourceVfrSyntaxParser.Inventory, SourceVfrSyntaxParser.Hidden, SourceVfrSyntaxParser.Restore, SourceVfrSyntaxParser.Save]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2312
                self.vfrStatementInvalid()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementDisableIfStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_DISABLE_IF_OP)

        def DisableIf(self):
            return self.getToken(SourceVfrSyntaxParser.DisableIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def vfrStatementStatList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementStatListContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatListContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementDisableIfStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementDisableIfStat" ):
                return visitor.visitVfrStatementDisableIfStat(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementDisableIfStat(self):

        localctx = SourceVfrSyntaxParser.VfrStatementDisableIfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_vfrStatementDisableIfStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2315
            self.match(SourceVfrSyntaxParser.DisableIf)
            self.state = 2316
            self.vfrStatementExpression(localctx.Node)
            self.state = 2317
            self.match(SourceVfrSyntaxParser.Semicolon)
            self.state = 2321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (SourceVfrSyntaxParser.OneOf - 46)) | (1 << (SourceVfrSyntaxParser.OrderedList - 46)) | (1 << (SourceVfrSyntaxParser.Subtitle - 46)) | (1 << (SourceVfrSyntaxParser.Text - 46)) | (1 << (SourceVfrSyntaxParser.Date - 46)) | (1 << (SourceVfrSyntaxParser.Time - 46)) | (1 << (SourceVfrSyntaxParser.GrayOutIf - 46)) | (1 << (SourceVfrSyntaxParser.Label - 46)) | (1 << (SourceVfrSyntaxParser.Inventory - 46)) | (1 << (SourceVfrSyntaxParser.CheckBox - 46)) | (1 << (SourceVfrSyntaxParser.Numeric - 46)) | (1 << (SourceVfrSyntaxParser.Password - 46)) | (1 << (SourceVfrSyntaxParser.String - 46)) | (1 << (SourceVfrSyntaxParser.SuppressIf - 46)) | (1 << (SourceVfrSyntaxParser.DisableIf - 46)) | (1 << (SourceVfrSyntaxParser.Hidden - 46)) | (1 << (SourceVfrSyntaxParser.Goto - 46)))) != 0) or ((((_la - 110)) & ~0x3f) == 0 and ((1 << (_la - 110)) & ((1 << (SourceVfrSyntaxParser.InconsistentIf - 110)) | (1 << (SourceVfrSyntaxParser.Restore - 110)) | (1 << (SourceVfrSyntaxParser.Save - 110)) | (1 << (SourceVfrSyntaxParser.ResetButton - 110)) | (1 << (SourceVfrSyntaxParser.Action - 110)) | (1 << (SourceVfrSyntaxParser.GuidOp - 110)))) != 0):
                self.state = 2318
                self.vfrStatementStatList()
                self.state = 2323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2324
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 2325
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementgrayoutIfSuppressIfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def SuppressIf(self):
            return self.getToken(SourceVfrSyntaxParser.SuppressIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementgrayoutIfSuppressIf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementgrayoutIfSuppressIf" ):
                return visitor.visitVfrStatementgrayoutIfSuppressIf(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementgrayoutIfSuppressIf(self):

        localctx = SourceVfrSyntaxParser.VfrStatementgrayoutIfSuppressIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_vfrStatementgrayoutIfSuppressIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2327
            self.match(SourceVfrSyntaxParser.SuppressIf)
            self.state = 2340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 2328
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 2329
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2330
                self.flagsField()
                self.state = 2335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 2331
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 2332
                    self.flagsField()
                    self.state = 2337
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2338
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 2342
            self.vfrStatementExpression(localctx.Node)
            self.state = 2343
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementsuppressIfGrayOutIfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def GrayOutIf(self):
            return self.getToken(SourceVfrSyntaxParser.GrayOutIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementsuppressIfGrayOutIf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementsuppressIfGrayOutIf" ):
                return visitor.visitVfrStatementsuppressIfGrayOutIf(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementsuppressIfGrayOutIf(self):

        localctx = SourceVfrSyntaxParser.VfrStatementsuppressIfGrayOutIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_vfrStatementsuppressIfGrayOutIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2345
            self.match(SourceVfrSyntaxParser.GrayOutIf)
            self.state = 2358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 2346
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 2347
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2348
                self.flagsField()
                self.state = 2353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 2349
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 2350
                    self.flagsField()
                    self.state = 2355
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2356
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 2360
            self.vfrStatementExpression(localctx.Node)
            self.state = 2361
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementSuppressIfStatNewContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_SUPPRESS_IF_OP)

        def SuppressIf(self):
            return self.getToken(SourceVfrSyntaxParser.SuppressIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def vfrStatementStatList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementStatListContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatListContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementSuppressIfStatNew

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementSuppressIfStatNew" ):
                return visitor.visitVfrStatementSuppressIfStatNew(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementSuppressIfStatNew(self):

        localctx = SourceVfrSyntaxParser.VfrStatementSuppressIfStatNewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_vfrStatementSuppressIfStatNew)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2363
            self.match(SourceVfrSyntaxParser.SuppressIf)
            self.state = 2376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 2364
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 2365
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2366
                self.flagsField()
                self.state = 2371
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 2367
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 2368
                    self.flagsField()
                    self.state = 2373
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2374
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 2378
            self.vfrStatementExpression(localctx.Node)
            self.state = 2379
            self.match(SourceVfrSyntaxParser.Semicolon)
            self.state = 2383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (SourceVfrSyntaxParser.OneOf - 46)) | (1 << (SourceVfrSyntaxParser.OrderedList - 46)) | (1 << (SourceVfrSyntaxParser.Subtitle - 46)) | (1 << (SourceVfrSyntaxParser.Text - 46)) | (1 << (SourceVfrSyntaxParser.Date - 46)) | (1 << (SourceVfrSyntaxParser.Time - 46)) | (1 << (SourceVfrSyntaxParser.GrayOutIf - 46)) | (1 << (SourceVfrSyntaxParser.Label - 46)) | (1 << (SourceVfrSyntaxParser.Inventory - 46)) | (1 << (SourceVfrSyntaxParser.CheckBox - 46)) | (1 << (SourceVfrSyntaxParser.Numeric - 46)) | (1 << (SourceVfrSyntaxParser.Password - 46)) | (1 << (SourceVfrSyntaxParser.String - 46)) | (1 << (SourceVfrSyntaxParser.SuppressIf - 46)) | (1 << (SourceVfrSyntaxParser.DisableIf - 46)) | (1 << (SourceVfrSyntaxParser.Hidden - 46)) | (1 << (SourceVfrSyntaxParser.Goto - 46)))) != 0) or ((((_la - 110)) & ~0x3f) == 0 and ((1 << (_la - 110)) & ((1 << (SourceVfrSyntaxParser.InconsistentIf - 110)) | (1 << (SourceVfrSyntaxParser.Restore - 110)) | (1 << (SourceVfrSyntaxParser.Save - 110)) | (1 << (SourceVfrSyntaxParser.ResetButton - 110)) | (1 << (SourceVfrSyntaxParser.Action - 110)) | (1 << (SourceVfrSyntaxParser.GuidOp - 110)))) != 0):
                self.state = 2380
                self.vfrStatementStatList()
                self.state = 2385
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2386
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 2387
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementGrayOutIfStatNewContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_GRAY_OUT_IF_OP)

        def GrayOutIf(self):
            return self.getToken(SourceVfrSyntaxParser.GrayOutIf, 0)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def vfrStatementStatList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementStatListContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementStatListContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementGrayOutIfStatNew

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementGrayOutIfStatNew" ):
                return visitor.visitVfrStatementGrayOutIfStatNew(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementGrayOutIfStatNew(self):

        localctx = SourceVfrSyntaxParser.VfrStatementGrayOutIfStatNewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_vfrStatementGrayOutIfStatNew)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2389
            self.match(SourceVfrSyntaxParser.GrayOutIf)
            self.state = 2402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 2390
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 2391
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2392
                self.flagsField()
                self.state = 2397
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 2393
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 2394
                    self.flagsField()
                    self.state = 2399
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2400
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 2404
            self.vfrStatementExpression(localctx.Node)
            self.state = 2405
            self.match(SourceVfrSyntaxParser.Semicolon)
            self.state = 2409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (SourceVfrSyntaxParser.OneOf - 46)) | (1 << (SourceVfrSyntaxParser.OrderedList - 46)) | (1 << (SourceVfrSyntaxParser.Subtitle - 46)) | (1 << (SourceVfrSyntaxParser.Text - 46)) | (1 << (SourceVfrSyntaxParser.Date - 46)) | (1 << (SourceVfrSyntaxParser.Time - 46)) | (1 << (SourceVfrSyntaxParser.GrayOutIf - 46)) | (1 << (SourceVfrSyntaxParser.Label - 46)) | (1 << (SourceVfrSyntaxParser.Inventory - 46)) | (1 << (SourceVfrSyntaxParser.CheckBox - 46)) | (1 << (SourceVfrSyntaxParser.Numeric - 46)) | (1 << (SourceVfrSyntaxParser.Password - 46)) | (1 << (SourceVfrSyntaxParser.String - 46)) | (1 << (SourceVfrSyntaxParser.SuppressIf - 46)) | (1 << (SourceVfrSyntaxParser.DisableIf - 46)) | (1 << (SourceVfrSyntaxParser.Hidden - 46)) | (1 << (SourceVfrSyntaxParser.Goto - 46)))) != 0) or ((((_la - 110)) & ~0x3f) == 0 and ((1 << (_la - 110)) & ((1 << (SourceVfrSyntaxParser.InconsistentIf - 110)) | (1 << (SourceVfrSyntaxParser.Restore - 110)) | (1 << (SourceVfrSyntaxParser.Save - 110)) | (1 << (SourceVfrSyntaxParser.ResetButton - 110)) | (1 << (SourceVfrSyntaxParser.Action - 110)) | (1 << (SourceVfrSyntaxParser.GuidOp - 110)))) != 0):
                self.state = 2406
                self.vfrStatementStatList()
                self.state = 2411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2412
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 2413
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementInconsistentIfStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_INCONSISTENT_IF_OP)
            self.S = None # Token

        def InconsistentIf(self):
            return self.getToken(SourceVfrSyntaxParser.InconsistentIf, 0)

        def Prompt(self):
            return self.getToken(SourceVfrSyntaxParser.Prompt, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementExpression(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,0)


        def EndIf(self):
            return self.getToken(SourceVfrSyntaxParser.EndIf, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementInconsistentIfStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementInconsistentIfStat" ):
                return visitor.visitVfrStatementInconsistentIfStat(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementInconsistentIfStat(self):

        localctx = SourceVfrSyntaxParser.VfrStatementInconsistentIfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_vfrStatementInconsistentIfStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2415
            self.match(SourceVfrSyntaxParser.InconsistentIf)
            self.state = 2416
            self.match(SourceVfrSyntaxParser.Prompt)
            self.state = 2417
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2418
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 2419
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2420
            localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 2421
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 2422
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.FLAGS:
                self.state = 2423
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 2424
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2425
                self.flagsField()
                self.state = 2430
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 2426
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 2427
                    self.flagsField()
                    self.state = 2432
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2433
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 2437
            self.vfrStatementExpression(localctx.Node)
            self.state = 2438
            self.match(SourceVfrSyntaxParser.EndIf)
            self.state = 2439
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementInvalidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vfrStatementInvalidHidden(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInvalidHiddenContext,0)


        def vfrStatementInvalidInventory(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInvalidInventoryContext,0)


        def vfrStatementInvalidSaveRestoreDefaults(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementInvalidSaveRestoreDefaultsContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementInvalid

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementInvalid" ):
                return visitor.visitVfrStatementInvalid(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementInvalid(self):

        localctx = SourceVfrSyntaxParser.VfrStatementInvalidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_vfrStatementInvalid)
        try:
            self.state = 2444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Hidden]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2441
                self.vfrStatementInvalidHidden()
                pass
            elif token in [SourceVfrSyntaxParser.Inventory]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2442
                self.vfrStatementInvalidInventory()
                pass
            elif token in [SourceVfrSyntaxParser.Restore, SourceVfrSyntaxParser.Save]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2443
                self.vfrStatementInvalidSaveRestoreDefaults()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementInvalidHiddenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.V = None # Token
            self.S = None # Token
            self.KV = None # Token
            self.KS = None # Token

        def Hidden(self):
            return self.getToken(SourceVfrSyntaxParser.Hidden, 0)

        def Value(self):
            return self.getToken(SourceVfrSyntaxParser.Value, 0)

        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def Key(self):
            return self.getToken(SourceVfrSyntaxParser.Key, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementInvalidHidden

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementInvalidHidden" ):
                return visitor.visitVfrStatementInvalidHidden(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementInvalidHidden(self):

        localctx = SourceVfrSyntaxParser.VfrStatementInvalidHiddenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_vfrStatementInvalidHidden)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2446
            self.match(SourceVfrSyntaxParser.Hidden)
            self.state = 2447
            self.match(SourceVfrSyntaxParser.Value)
            self.state = 2448
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 2449
                localctx.V = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 2450
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2453
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2454
            self.match(SourceVfrSyntaxParser.Key)
            self.state = 2455
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 2456
                localctx.KV = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 2457
                localctx.KS = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2460
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementInvalidInventoryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Inventory(self):
            return self.getToken(SourceVfrSyntaxParser.Inventory, 0)

        def Help(self):
            return self.getToken(SourceVfrSyntaxParser.Help, 0)

        def StringToken(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringToken)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringToken, i)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Text(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Text)
            else:
                return self.getToken(SourceVfrSyntaxParser.Text, i)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementInvalidInventory

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementInvalidInventory" ):
                return visitor.visitVfrStatementInvalidInventory(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementInvalidInventory(self):

        localctx = SourceVfrSyntaxParser.VfrStatementInvalidInventoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_vfrStatementInvalidInventory)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2462
            self.match(SourceVfrSyntaxParser.Inventory)
            self.state = 2463
            self.match(SourceVfrSyntaxParser.Help)
            self.state = 2464
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2465
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 2466
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2467
            self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 2468
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 2469
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2470
            self.match(SourceVfrSyntaxParser.Text)
            self.state = 2471
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2472
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 2473
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2474
            self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 2475
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 2476
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Text:
                self.state = 2477
                self.match(SourceVfrSyntaxParser.Text)
                self.state = 2478
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2479
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2480
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2481
                self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2482
                self.match(SourceVfrSyntaxParser.CloseParen)


            self.state = 2485
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementInvalidSaveRestoreDefaultsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.N = None # Token
            self.S = None # Token
            self.PS = None # Token
            self.HS = None # Token
            self.KN = None # Token
            self.KS = None # Token

        def Defaults(self):
            return self.getToken(SourceVfrSyntaxParser.Defaults, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def FormId(self):
            return self.getToken(SourceVfrSyntaxParser.FormId, 0)

        def Prompt(self):
            return self.getToken(SourceVfrSyntaxParser.Prompt, 0)

        def StringToken(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringToken)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringToken, i)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def Help(self):
            return self.getToken(SourceVfrSyntaxParser.Help, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Save(self):
            return self.getToken(SourceVfrSyntaxParser.Save, 0)

        def Restore(self):
            return self.getToken(SourceVfrSyntaxParser.Restore, 0)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def flagsField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FlagsFieldContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FlagsFieldContext,i)


        def Key(self):
            return self.getToken(SourceVfrSyntaxParser.Key, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementInvalidSaveRestoreDefaults

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementInvalidSaveRestoreDefaults" ):
                return visitor.visitVfrStatementInvalidSaveRestoreDefaults(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementInvalidSaveRestoreDefaults(self):

        localctx = SourceVfrSyntaxParser.VfrStatementInvalidSaveRestoreDefaultsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_vfrStatementInvalidSaveRestoreDefaults)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2487
            _la = self._input.LA(1)
            if not(_la==SourceVfrSyntaxParser.Restore or _la==SourceVfrSyntaxParser.Save):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 2488
            self.match(SourceVfrSyntaxParser.Defaults)
            self.state = 2489
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2490
            self.match(SourceVfrSyntaxParser.FormId)
            self.state = 2491
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 2492
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 2493
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2496
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2497
            self.match(SourceVfrSyntaxParser.Prompt)
            self.state = 2498
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2499
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 2500
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2501
            localctx.PS = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 2502
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 2503
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2504
            self.match(SourceVfrSyntaxParser.Help)
            self.state = 2505
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2506
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 2507
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2508
            localctx.HS = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 2509
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 2521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,226,self._ctx)
            if la_ == 1:
                self.state = 2510
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2511
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 2512
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2513
                self.flagsField()
                self.state = 2518
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.BitWiseOr:
                    self.state = 2514
                    self.match(SourceVfrSyntaxParser.BitWiseOr)
                    self.state = 2515
                    self.flagsField()
                    self.state = 2520
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 2530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Comma:
                self.state = 2523
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2524
                self.match(SourceVfrSyntaxParser.Key)
                self.state = 2525
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2528
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 2526
                    localctx.KN = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 2527
                    localctx.KS = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 2532
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementLabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_GUID_OP)
            self.N = None # Token
            self.S = None # Token

        def Label(self):
            return self.getToken(SourceVfrSyntaxParser.Label, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementLabel

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementLabel" ):
                return visitor.visitVfrStatementLabel(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementLabel(self):

        localctx = SourceVfrSyntaxParser.VfrStatementLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_vfrStatementLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2534
            self.match(SourceVfrSyntaxParser.Label)
            self.state = 2537
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Number]:
                self.state = 2535
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                pass
            elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                self.state = 2536
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2539
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementBannerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_GUID_OP)
            self.S = None # Token
            self.NL = None # Token
            self.SL = None # Token
            self.TN = None # Token
            self.TS = None # Token

        def Banner(self):
            return self.getToken(SourceVfrSyntaxParser.Banner, 0)

        def Title(self):
            return self.getToken(SourceVfrSyntaxParser.Title, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def Line(self):
            return self.getToken(SourceVfrSyntaxParser.Line, 0)

        def Align(self):
            return self.getToken(SourceVfrSyntaxParser.Align, 0)

        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Timeout(self):
            return self.getToken(SourceVfrSyntaxParser.Timeout, 0)

        def Left(self):
            return self.getToken(SourceVfrSyntaxParser.Left, 0)

        def Center(self):
            return self.getToken(SourceVfrSyntaxParser.Center, 0)

        def Right(self):
            return self.getToken(SourceVfrSyntaxParser.Right, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementBanner

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementBanner" ):
                return visitor.visitVfrStatementBanner(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementBanner(self):

        localctx = SourceVfrSyntaxParser.VfrStatementBannerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_vfrStatementBanner)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2541
            self.match(SourceVfrSyntaxParser.Banner)
            self.state = 2543
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Comma:
                self.state = 2542
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 2545
            self.match(SourceVfrSyntaxParser.Title)
            self.state = 2546
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2547
            self.match(SourceVfrSyntaxParser.StringToken)
            self.state = 2548
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2549
            localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 2550
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 2551
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2568
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Line]:
                self.state = 2552
                self.match(SourceVfrSyntaxParser.Line)
                self.state = 2555
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 2553
                    localctx.NL = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 2554
                    localctx.SL = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2557
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2558
                self.match(SourceVfrSyntaxParser.Align)
                self.state = 2559
                _la = self._input.LA(1)
                if not(((((_la - 136)) & ~0x3f) == 0 and ((1 << (_la - 136)) & ((1 << (SourceVfrSyntaxParser.Left - 136)) | (1 << (SourceVfrSyntaxParser.Right - 136)) | (1 << (SourceVfrSyntaxParser.Center - 136)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 2560
                self.match(SourceVfrSyntaxParser.Semicolon)
                pass
            elif token in [SourceVfrSyntaxParser.Timeout]:
                self.state = 2561
                self.match(SourceVfrSyntaxParser.Timeout)
                self.state = 2562
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2565
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Number]:
                    self.state = 2563
                    localctx.TN = self.match(SourceVfrSyntaxParser.Number)
                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 2564
                    localctx.TS = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2567
                self.match(SourceVfrSyntaxParser.Semicolon)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementExtensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_GUID_OP)
            self.Buffer = []
            self.Size = 0
            self.TypeName = ''
            self.TypeSize = 0
            self.IsStruct = False
            self.ArrayNum = 0
            self.D = None # Token
            self.ST = None # Token

        def GuidOp(self):
            return self.getToken(SourceVfrSyntaxParser.GuidOp, 0)

        def Uuid(self):
            return self.getToken(SourceVfrSyntaxParser.Uuid, 0)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def EndGuidOp(self):
            return self.getToken(SourceVfrSyntaxParser.EndGuidOp, 0)

        def DataType(self):
            return self.getToken(SourceVfrSyntaxParser.DataType, 0)

        def Uint64(self):
            return self.getToken(SourceVfrSyntaxParser.Uint64, 0)

        def Uint32(self):
            return self.getToken(SourceVfrSyntaxParser.Uint32, 0)

        def Uint16(self):
            return self.getToken(SourceVfrSyntaxParser.Uint16, 0)

        def Uint8(self):
            return self.getToken(SourceVfrSyntaxParser.Uint8, 0)

        def Boolean(self):
            return self.getToken(SourceVfrSyntaxParser.Boolean, 0)

        def EFI_STRING_ID(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_STRING_ID, 0)

        def EFI_HII_DATE(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_DATE, 0)

        def EFI_HII_TIME(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_TIME, 0)

        def EFI_HII_REF(self):
            return self.getToken(SourceVfrSyntaxParser.EFI_HII_REF, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def vfrExtensionData(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrExtensionDataContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExtensionDataContext,i)


        def vfrStatementExtension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExtensionContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExtensionContext,i)


        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementExtension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementExtension" ):
                return visitor.visitVfrStatementExtension(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementExtension(self):

        localctx = SourceVfrSyntaxParser.VfrStatementExtensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_vfrStatementExtension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2570
            self.match(SourceVfrSyntaxParser.GuidOp)
            self.state = 2571
            self.match(SourceVfrSyntaxParser.Uuid)
            self.state = 2572
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2573
            self.guidDefinition()
            self.state = 2645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,246,self._ctx)
            if la_ == 1:
                self.state = 2574
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2575
                localctx.D = self.match(SourceVfrSyntaxParser.DataType)
                self.state = 2576
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2637
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SourceVfrSyntaxParser.Uint64]:
                    self.state = 2577
                    self.match(SourceVfrSyntaxParser.Uint64)
                    self.state = 2581
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2578
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2579
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2580
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                elif token in [SourceVfrSyntaxParser.Uint32]:
                    self.state = 2583
                    self.match(SourceVfrSyntaxParser.Uint32)
                    self.state = 2587
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2584
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2585
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2586
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                elif token in [SourceVfrSyntaxParser.Uint16]:
                    self.state = 2589
                    self.match(SourceVfrSyntaxParser.Uint16)
                    self.state = 2593
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2590
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2591
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2592
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                elif token in [SourceVfrSyntaxParser.Uint8]:
                    self.state = 2595
                    self.match(SourceVfrSyntaxParser.Uint8)
                    self.state = 2599
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2596
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2597
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2598
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                elif token in [SourceVfrSyntaxParser.Boolean]:
                    self.state = 2601
                    self.match(SourceVfrSyntaxParser.Boolean)
                    self.state = 2605
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2602
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2603
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2604
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                elif token in [SourceVfrSyntaxParser.EFI_STRING_ID]:
                    self.state = 2607
                    self.match(SourceVfrSyntaxParser.EFI_STRING_ID)
                    self.state = 2611
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2608
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2609
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2610
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                elif token in [SourceVfrSyntaxParser.EFI_HII_DATE]:
                    self.state = 2613
                    self.match(SourceVfrSyntaxParser.EFI_HII_DATE)
                    self.state = 2617
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2614
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2615
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2616
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                elif token in [SourceVfrSyntaxParser.EFI_HII_TIME]:
                    self.state = 2619
                    self.match(SourceVfrSyntaxParser.EFI_HII_TIME)
                    self.state = 2623
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2620
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2621
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2622
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                elif token in [SourceVfrSyntaxParser.EFI_HII_REF]:
                    self.state = 2625
                    self.match(SourceVfrSyntaxParser.EFI_HII_REF)
                    self.state = 2629
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2626
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2627
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2628
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                elif token in [SourceVfrSyntaxParser.StringIdentifier]:
                    self.state = 2631
                    localctx.ST = self.match(SourceVfrSyntaxParser.StringIdentifier)
                    self.state = 2635
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SourceVfrSyntaxParser.OpenBracket:
                        self.state = 2632
                        self.match(SourceVfrSyntaxParser.OpenBracket)
                        self.state = 2633
                        self.match(SourceVfrSyntaxParser.Number)
                        self.state = 2634
                        self.match(SourceVfrSyntaxParser.CloseBracket)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2642
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,245,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2639
                        self.vfrExtensionData()
                    self.state = 2644
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,245,self._ctx)



            self.state = 2655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Comma:
                self.state = 2647
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 2651
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.GuidOp:
                    self.state = 2648
                    self.vfrStatementExtension()
                    self.state = 2653
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2654
                self.match(SourceVfrSyntaxParser.EndGuidOp)


            self.state = 2657
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExtensionDataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.TFName = ''
            self.FName = ''
            self.TFValue = None
            self.I = None # Token
            self.N = None # Token

        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def Data(self):
            return self.getToken(SourceVfrSyntaxParser.Data, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Dot)
            else:
                return self.getToken(SourceVfrSyntaxParser.Dot, i)

        def arrayName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.ArrayNameContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.ArrayNameContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExtensionData

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExtensionData" ):
                return visitor.visitVfrExtensionData(self)
            else:
                return visitor.visitChildren(self)




    def vfrExtensionData(self):

        localctx = SourceVfrSyntaxParser.VfrExtensionDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_vfrExtensionData)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2659
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2660
            self.match(SourceVfrSyntaxParser.Data)
            self.state = 2664
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 2661
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 2662
                localctx.I = self.match(SourceVfrSyntaxParser.Number)
                self.state = 2663
                self.match(SourceVfrSyntaxParser.CloseBracket)


            self.state = 2670
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.Dot:
                self.state = 2666
                self.match(SourceVfrSyntaxParser.Dot)
                self.state = 2667
                self.arrayName()
                self.state = 2672
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2673
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 2674
            localctx.N = self.match(SourceVfrSyntaxParser.Number)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementModalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = None

        def vfrModalTag(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrModalTagContext,0)


        def Semicolon(self):
            return self.getToken(SourceVfrSyntaxParser.Semicolon, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementModal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementModal" ):
                return visitor.visitVfrStatementModal(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementModal(self):

        localctx = SourceVfrSyntaxParser.VfrStatementModalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_vfrStatementModal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2676
            self.vfrModalTag()
            self.state = 2677
            self.match(SourceVfrSyntaxParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrModalTagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Node = IfrTreeNode(EFI_IFR_MODAL_TAG_OP)

        def Modal(self):
            return self.getToken(SourceVfrSyntaxParser.Modal, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrModalTag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrModalTag" ):
                return visitor.visitVfrModalTag(self)
            else:
                return visitor.visitChildren(self)




    def vfrModalTag(self):

        localctx = SourceVfrSyntaxParser.VfrModalTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_vfrModalTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2679
            self.match(SourceVfrSyntaxParser.Modal)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ParentNode=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ParentNode = None
            self.ExpInfo = ExpressionInfo()
            self.Nodes = []
            self.L = None # Token
            self.ParentNode = ParentNode

        def andTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.AndTermContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.AndTermContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OR)
            else:
                return self.getToken(SourceVfrSyntaxParser.OR, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementExpression" ):
                return visitor.visitVfrStatementExpression(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementExpression(self, ParentNode):

        localctx = SourceVfrSyntaxParser.VfrStatementExpressionContext(self, self._ctx, self.state, ParentNode)
        self.enterRule(localctx, 292, self.RULE_vfrStatementExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2681
            self.andTerm(localctx.ExpInfo)
            self.state = 2686
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.OR:
                self.state = 2682
                localctx.L = self.match(SourceVfrSyntaxParser.OR)
                self.state = 2683
                self.andTerm(localctx.ExpInfo)
                self.state = 2688
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrStatementExpressionSubContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ParentNodes=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ParentNodes = None
            self.ExpInfo = ExpressionInfo()
            self.Nodes = []
            self.ParentNodes = ParentNodes

        def andTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.AndTermContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.AndTermContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OR)
            else:
                return self.getToken(SourceVfrSyntaxParser.OR, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrStatementExpressionSub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrStatementExpressionSub" ):
                return visitor.visitVfrStatementExpressionSub(self)
            else:
                return visitor.visitChildren(self)




    def vfrStatementExpressionSub(self, ParentNodes):

        localctx = SourceVfrSyntaxParser.VfrStatementExpressionSubContext(self, self._ctx, self.state, ParentNodes)
        self.enterRule(localctx, 294, self.RULE_vfrStatementExpressionSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2689
            self.andTerm(localctx.ExpInfo)
            self.state = 2694
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.OR:
                self.state = 2690
                self.match(SourceVfrSyntaxParser.OR)
                self.state = 2691
                self.andTerm(localctx.ExpInfo)
                self.state = 2696
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.Line = None
            self.L = None # Token
            self.ExpInfo = ExpInfo

        def bitwiseorTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.BitwiseorTermContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.BitwiseorTermContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.AND)
            else:
                return self.getToken(SourceVfrSyntaxParser.AND, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_andTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndTerm" ):
                return visitor.visitAndTerm(self)
            else:
                return visitor.visitChildren(self)




    def andTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.AndTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 296, self.RULE_andTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2697
            self.bitwiseorTerm(ExpInfo)
            self.state = 2702
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.AND:
                self.state = 2698
                localctx.L = self.match(SourceVfrSyntaxParser.AND)
                self.state = 2699
                self.bitwiseorTerm(ExpInfo)
                self.state = 2704
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseorTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.Line = None
            self.L = None # Token
            self.ExpInfo = ExpInfo

        def bitwiseandTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.BitwiseandTermContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.BitwiseandTermContext,i)


        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_bitwiseorTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseorTerm" ):
                return visitor.visitBitwiseorTerm(self)
            else:
                return visitor.visitChildren(self)




    def bitwiseorTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.BitwiseorTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 298, self.RULE_bitwiseorTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2705
            self.bitwiseandTerm(ExpInfo)
            self.state = 2710
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 2706
                localctx.L = self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 2707
                self.bitwiseandTerm(ExpInfo)
                self.state = 2712
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseandTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.Line = None
            self.L = None # Token
            self.ExpInfo = ExpInfo

        def equalTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.EqualTermContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.EqualTermContext,i)


        def BitWiseAnd(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseAnd)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseAnd, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_bitwiseandTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseandTerm" ):
                return visitor.visitBitwiseandTerm(self)
            else:
                return visitor.visitChildren(self)




    def bitwiseandTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.BitwiseandTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 300, self.RULE_bitwiseandTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2713
            self.equalTerm(ExpInfo)
            self.state = 2718
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseAnd:
                self.state = 2714
                localctx.L = self.match(SourceVfrSyntaxParser.BitWiseAnd)
                self.state = 2715
                self.equalTerm(ExpInfo)
                self.state = 2720
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.Line = None
            self.ExpInfo = ExpInfo

        def compareTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.CompareTermContext,0)


        def equalTermSupplementary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.EqualTermSupplementaryContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.EqualTermSupplementaryContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_equalTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualTerm" ):
                return visitor.visitEqualTerm(self)
            else:
                return visitor.visitChildren(self)




    def equalTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.EqualTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 302, self.RULE_equalTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2721
            self.compareTerm(ExpInfo)
            self.state = 2725
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.Equal or _la==SourceVfrSyntaxParser.NotEqual:
                self.state = 2722
                self.equalTermSupplementary(ExpInfo)
                self.state = 2727
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualTermSupplementaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_equalTermSupplementary


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.ExpInfo = ctx.ExpInfo
            self.Nodes = ctx.Nodes



    class EqualTermEqualRuleContext(EqualTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.EqualTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Equal(self):
            return self.getToken(SourceVfrSyntaxParser.Equal, 0)
        def compareTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.CompareTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualTermEqualRule" ):
                return visitor.visitEqualTermEqualRule(self)
            else:
                return visitor.visitChildren(self)


    class EqualTermNotEqualRuleContext(EqualTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.EqualTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NotEqual(self):
            return self.getToken(SourceVfrSyntaxParser.NotEqual, 0)
        def compareTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.CompareTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualTermNotEqualRule" ):
                return visitor.visitEqualTermNotEqualRule(self)
            else:
                return visitor.visitChildren(self)



    def equalTermSupplementary(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.EqualTermSupplementaryContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 304, self.RULE_equalTermSupplementary)
        try:
            self.state = 2732
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Equal]:
                localctx = SourceVfrSyntaxParser.EqualTermEqualRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2728
                self.match(SourceVfrSyntaxParser.Equal)
                self.state = 2729
                self.compareTerm(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.NotEqual]:
                localctx = SourceVfrSyntaxParser.EqualTermNotEqualRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2730
                self.match(SourceVfrSyntaxParser.NotEqual)
                self.state = 2731
                self.compareTerm(ExpInfo)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def shiftTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ShiftTermContext,0)


        def compareTermSupplementary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.CompareTermSupplementaryContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.CompareTermSupplementaryContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_compareTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareTerm" ):
                return visitor.visitCompareTerm(self)
            else:
                return visitor.visitChildren(self)




    def compareTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.CompareTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 306, self.RULE_compareTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2734
            self.shiftTerm(ExpInfo)
            self.state = 2738
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SourceVfrSyntaxParser.LessEqual) | (1 << SourceVfrSyntaxParser.Less) | (1 << SourceVfrSyntaxParser.GreaterEqual) | (1 << SourceVfrSyntaxParser.Greater))) != 0):
                self.state = 2735
                self.compareTermSupplementary(ExpInfo)
                self.state = 2740
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareTermSupplementaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_compareTermSupplementary


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.ExpInfo = ctx.ExpInfo
            self.Nodes = ctx.Nodes



    class CompareTermLessRuleContext(CompareTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.CompareTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Less(self):
            return self.getToken(SourceVfrSyntaxParser.Less, 0)
        def shiftTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ShiftTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareTermLessRule" ):
                return visitor.visitCompareTermLessRule(self)
            else:
                return visitor.visitChildren(self)


    class CompareTermGreaterEqualRuleContext(CompareTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.CompareTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GreaterEqual(self):
            return self.getToken(SourceVfrSyntaxParser.GreaterEqual, 0)
        def shiftTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ShiftTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareTermGreaterEqualRule" ):
                return visitor.visitCompareTermGreaterEqualRule(self)
            else:
                return visitor.visitChildren(self)


    class CompareTermGreaterRuleContext(CompareTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.CompareTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Greater(self):
            return self.getToken(SourceVfrSyntaxParser.Greater, 0)
        def shiftTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ShiftTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareTermGreaterRule" ):
                return visitor.visitCompareTermGreaterRule(self)
            else:
                return visitor.visitChildren(self)


    class CompareTermLessEqualRuleContext(CompareTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.CompareTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LessEqual(self):
            return self.getToken(SourceVfrSyntaxParser.LessEqual, 0)
        def shiftTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ShiftTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareTermLessEqualRule" ):
                return visitor.visitCompareTermLessEqualRule(self)
            else:
                return visitor.visitChildren(self)



    def compareTermSupplementary(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.CompareTermSupplementaryContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 308, self.RULE_compareTermSupplementary)
        try:
            self.state = 2749
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Less]:
                localctx = SourceVfrSyntaxParser.CompareTermLessRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2741
                self.match(SourceVfrSyntaxParser.Less)
                self.state = 2742
                self.shiftTerm(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.LessEqual]:
                localctx = SourceVfrSyntaxParser.CompareTermLessEqualRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2743
                self.match(SourceVfrSyntaxParser.LessEqual)
                self.state = 2744
                self.shiftTerm(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Greater]:
                localctx = SourceVfrSyntaxParser.CompareTermGreaterRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2745
                self.match(SourceVfrSyntaxParser.Greater)
                self.state = 2746
                self.shiftTerm(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.GreaterEqual]:
                localctx = SourceVfrSyntaxParser.CompareTermGreaterEqualRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2747
                self.match(SourceVfrSyntaxParser.GreaterEqual)
                self.state = 2748
                self.shiftTerm(ExpInfo)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def addMinusTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.AddMinusTermContext,0)


        def shiftTermSupplementary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.ShiftTermSupplementaryContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.ShiftTermSupplementaryContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_shiftTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftTerm" ):
                return visitor.visitShiftTerm(self)
            else:
                return visitor.visitChildren(self)




    def shiftTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.ShiftTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 310, self.RULE_shiftTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2751
            self.addMinusTerm(ExpInfo)
            self.state = 2755
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.T__9 or _la==SourceVfrSyntaxParser.T__10:
                self.state = 2752
                self.shiftTermSupplementary(ExpInfo)
                self.state = 2757
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftTermSupplementaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_shiftTermSupplementary


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.ExpInfo = ctx.ExpInfo
            self.Nodes = ctx.Nodes



    class ShiftTermRightContext(ShiftTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.ShiftTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addMinusTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.AddMinusTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftTermRight" ):
                return visitor.visitShiftTermRight(self)
            else:
                return visitor.visitChildren(self)


    class ShiftTermLeftContext(ShiftTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.ShiftTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addMinusTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.AddMinusTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftTermLeft" ):
                return visitor.visitShiftTermLeft(self)
            else:
                return visitor.visitChildren(self)



    def shiftTermSupplementary(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.ShiftTermSupplementaryContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 312, self.RULE_shiftTermSupplementary)
        try:
            self.state = 2762
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.T__9]:
                localctx = SourceVfrSyntaxParser.ShiftTermLeftContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2758
                self.match(SourceVfrSyntaxParser.T__9)
                self.state = 2759
                self.addMinusTerm(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.T__10]:
                localctx = SourceVfrSyntaxParser.ShiftTermRightContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2760
                self.match(SourceVfrSyntaxParser.T__10)
                self.state = 2761
                self.addMinusTerm(ExpInfo)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddMinusTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def multdivmodTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.MultdivmodTermContext,0)


        def addMinusTermSupplementary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.AddMinusTermSupplementaryContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.AddMinusTermSupplementaryContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_addMinusTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddMinusTerm" ):
                return visitor.visitAddMinusTerm(self)
            else:
                return visitor.visitChildren(self)




    def addMinusTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.AddMinusTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 314, self.RULE_addMinusTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2764
            self.multdivmodTerm(ExpInfo)
            self.state = 2768
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.T__11 or _la==SourceVfrSyntaxParser.Negative:
                self.state = 2765
                self.addMinusTermSupplementary(ExpInfo)
                self.state = 2770
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddMinusTermSupplementaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_addMinusTermSupplementary


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.ExpInfo = ctx.ExpInfo
            self.Nodes = ctx.Nodes



    class AddMinusTermpAddContext(AddMinusTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.AddMinusTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multdivmodTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.MultdivmodTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddMinusTermpAdd" ):
                return visitor.visitAddMinusTermpAdd(self)
            else:
                return visitor.visitChildren(self)


    class AddMinusTermSubtractContext(AddMinusTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.AddMinusTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Negative(self):
            return self.getToken(SourceVfrSyntaxParser.Negative, 0)
        def multdivmodTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.MultdivmodTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddMinusTermSubtract" ):
                return visitor.visitAddMinusTermSubtract(self)
            else:
                return visitor.visitChildren(self)



    def addMinusTermSupplementary(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.AddMinusTermSupplementaryContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 316, self.RULE_addMinusTermSupplementary)
        try:
            self.state = 2775
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.T__11]:
                localctx = SourceVfrSyntaxParser.AddMinusTermpAddContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2771
                self.match(SourceVfrSyntaxParser.T__11)
                self.state = 2772
                self.multdivmodTerm(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Negative]:
                localctx = SourceVfrSyntaxParser.AddMinusTermSubtractContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2773
                self.match(SourceVfrSyntaxParser.Negative)
                self.state = 2774
                self.multdivmodTerm(ExpInfo)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultdivmodTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def castTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.CastTermContext,0)


        def multdivmodTermSupplementary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.MultdivmodTermSupplementaryContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.MultdivmodTermSupplementaryContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_multdivmodTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultdivmodTerm" ):
                return visitor.visitMultdivmodTerm(self)
            else:
                return visitor.visitChildren(self)




    def multdivmodTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.MultdivmodTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 318, self.RULE_multdivmodTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2777
            self.castTerm(ExpInfo)
            self.state = 2781
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SourceVfrSyntaxParser.T__12) | (1 << SourceVfrSyntaxParser.T__13) | (1 << SourceVfrSyntaxParser.Slash))) != 0):
                self.state = 2778
                self.multdivmodTermSupplementary(ExpInfo)
                self.state = 2783
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultdivmodTermSupplementaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_multdivmodTermSupplementary


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.ExpInfo = ctx.ExpInfo
            self.Nodes = ctx.Nodes



    class MultdivmodTermDivContext(MultdivmodTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.MultdivmodTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Slash(self):
            return self.getToken(SourceVfrSyntaxParser.Slash, 0)
        def castTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.CastTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultdivmodTermDiv" ):
                return visitor.visitMultdivmodTermDiv(self)
            else:
                return visitor.visitChildren(self)


    class MultdivmodTermMulContext(MultdivmodTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.MultdivmodTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def castTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.CastTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultdivmodTermMul" ):
                return visitor.visitMultdivmodTermMul(self)
            else:
                return visitor.visitChildren(self)


    class MultdivmodTermModuloContext(MultdivmodTermSupplementaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.MultdivmodTermSupplementaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def castTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.CastTermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultdivmodTermModulo" ):
                return visitor.visitMultdivmodTermModulo(self)
            else:
                return visitor.visitChildren(self)



    def multdivmodTermSupplementary(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.MultdivmodTermSupplementaryContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 320, self.RULE_multdivmodTermSupplementary)
        try:
            self.state = 2790
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.T__12]:
                localctx = SourceVfrSyntaxParser.MultdivmodTermMulContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2784
                self.match(SourceVfrSyntaxParser.T__12)
                self.state = 2785
                self.castTerm(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Slash]:
                localctx = SourceVfrSyntaxParser.MultdivmodTermDivContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2786
                self.match(SourceVfrSyntaxParser.Slash)
                self.state = 2787
                self.castTerm(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.T__13]:
                localctx = SourceVfrSyntaxParser.MultdivmodTermModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2788
                self.match(SourceVfrSyntaxParser.T__13)
                self.state = 2789
                self.castTerm(ExpInfo)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def atomTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.AtomTermContext,0)


        def castTermSub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.CastTermSubContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.CastTermSubContext,i)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_castTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastTerm" ):
                return visitor.visitCastTerm(self)
            else:
                return visitor.visitChildren(self)




    def castTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.CastTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 322, self.RULE_castTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2795
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,266,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2792
                    self.castTermSub()
                self.state = 2797
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,266,self._ctx)

            self.state = 2798
            self.atomTerm(ExpInfo)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastTermSubContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.CastType = 0xFF

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Boolean(self):
            return self.getToken(SourceVfrSyntaxParser.Boolean, 0)

        def Uint64(self):
            return self.getToken(SourceVfrSyntaxParser.Uint64, 0)

        def Uint32(self):
            return self.getToken(SourceVfrSyntaxParser.Uint32, 0)

        def Uint16(self):
            return self.getToken(SourceVfrSyntaxParser.Uint16, 0)

        def Uint8(self):
            return self.getToken(SourceVfrSyntaxParser.Uint8, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_castTermSub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastTermSub" ):
                return visitor.visitCastTermSub(self)
            else:
                return visitor.visitChildren(self)




    def castTermSub(self):

        localctx = SourceVfrSyntaxParser.CastTermSubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_castTermSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2800
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2801
            _la = self._input.LA(1)
            if not(((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (SourceVfrSyntaxParser.Boolean - 80)) | (1 << (SourceVfrSyntaxParser.Uint64 - 80)) | (1 << (SourceVfrSyntaxParser.Uint32 - 80)) | (1 << (SourceVfrSyntaxParser.Uint16 - 80)) | (1 << (SourceVfrSyntaxParser.Uint8 - 80)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 2802
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def vfrExpressionCatenate(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExpressionCatenateContext,0)


        def vfrExpressionMatch(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExpressionMatchContext,0)


        def vfrExpressionMatch2(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExpressionMatch2Context,0)


        def vfrExpressionParen(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExpressionParenContext,0)


        def vfrExpressionBuildInFunction(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExpressionBuildInFunctionContext,0)


        def vfrExpressionConstant(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExpressionConstantContext,0)


        def vfrExpressionUnaryOp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExpressionUnaryOpContext,0)


        def vfrExpressionTernaryOp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExpressionTernaryOpContext,0)


        def vfrExpressionMap(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrExpressionMapContext,0)


        def NOT(self):
            return self.getToken(SourceVfrSyntaxParser.NOT, 0)

        def atomTerm(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.AtomTermContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_atomTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomTerm" ):
                return visitor.visitAtomTerm(self)
            else:
                return visitor.visitChildren(self)




    def atomTerm(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.AtomTermContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 326, self.RULE_atomTerm)
        try:
            self.state = 2815
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Catenate]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2804
                self.vfrExpressionCatenate(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Match]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2805
                self.vfrExpressionMatch(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Match2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2806
                self.vfrExpressionMatch2(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.OpenParen]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2807
                self.vfrExpressionParen(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Dup, SourceVfrSyntaxParser.VarEqVal, SourceVfrSyntaxParser.IdEqVal, SourceVfrSyntaxParser.IdEqId, SourceVfrSyntaxParser.IdEqValList, SourceVfrSyntaxParser.QuestionRef, SourceVfrSyntaxParser.RuleRef, SourceVfrSyntaxParser.StringRef, SourceVfrSyntaxParser.PushThis, SourceVfrSyntaxParser.Security, SourceVfrSyntaxParser.Get]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2808
                self.vfrExpressionBuildInFunction(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.TrueSymbol, SourceVfrSyntaxParser.FalseSymbol, SourceVfrSyntaxParser.One, SourceVfrSyntaxParser.Ones, SourceVfrSyntaxParser.Zero, SourceVfrSyntaxParser.Undefined, SourceVfrSyntaxParser.Version, SourceVfrSyntaxParser.Number, SourceVfrSyntaxParser.StringIdentifier]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2809
                self.vfrExpressionConstant(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Length, SourceVfrSyntaxParser.Set, SourceVfrSyntaxParser.BitWiseNot, SourceVfrSyntaxParser.BoolVal, SourceVfrSyntaxParser.StringVal, SourceVfrSyntaxParser.UnIntVal, SourceVfrSyntaxParser.ToUpper, SourceVfrSyntaxParser.ToLower, SourceVfrSyntaxParser.QuestionRefVal, SourceVfrSyntaxParser.StringRefVal]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2810
                self.vfrExpressionUnaryOp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Cond, SourceVfrSyntaxParser.Find, SourceVfrSyntaxParser.Mid, SourceVfrSyntaxParser.Tok, SourceVfrSyntaxParser.Span]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2811
                self.vfrExpressionTernaryOp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Map]:
                self.enterOuterAlt(localctx, 9)
                self.state = 2812
                self.vfrExpressionMap(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.NOT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 2813
                self.match(SourceVfrSyntaxParser.NOT)
                self.state = 2814
                self.atomTerm(ExpInfo)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExpressionCatenateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Catenate(self):
            return self.getToken(SourceVfrSyntaxParser.Catenate, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExpressionSubContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,i)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExpressionCatenate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExpressionCatenate" ):
                return visitor.visitVfrExpressionCatenate(self)
            else:
                return visitor.visitChildren(self)




    def vfrExpressionCatenate(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VfrExpressionCatenateContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 328, self.RULE_vfrExpressionCatenate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2817
            self.match(SourceVfrSyntaxParser.Catenate)
            self.state = 2818
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2819
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 2820
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2821
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 2822
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExpressionMatchContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Match(self):
            return self.getToken(SourceVfrSyntaxParser.Match, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExpressionSubContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,i)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExpressionMatch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExpressionMatch" ):
                return visitor.visitVfrExpressionMatch(self)
            else:
                return visitor.visitChildren(self)




    def vfrExpressionMatch(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VfrExpressionMatchContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 330, self.RULE_vfrExpressionMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2824
            self.match(SourceVfrSyntaxParser.Match)
            self.state = 2825
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2826
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 2827
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2828
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 2829
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExpressionMatch2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Match2(self):
            return self.getToken(SourceVfrSyntaxParser.Match2, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExpressionSubContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExpressionMatch2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExpressionMatch2" ):
                return visitor.visitVfrExpressionMatch2(self)
            else:
                return visitor.visitChildren(self)




    def vfrExpressionMatch2(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VfrExpressionMatch2Context(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 332, self.RULE_vfrExpressionMatch2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2831
            self.match(SourceVfrSyntaxParser.Match2)
            self.state = 2832
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2833
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 2834
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2835
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 2836
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 2837
            self.guidDefinition()
            self.state = 2838
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExpressionParenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExpressionParen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExpressionParen" ):
                return visitor.visitVfrExpressionParen(self)
            else:
                return visitor.visitChildren(self)




    def vfrExpressionParen(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VfrExpressionParenContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 334, self.RULE_vfrExpressionParen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2840
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2841
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 2842
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExpressionBuildInFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = None
            self.ExpInfo = ExpInfo

        def dupExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.DupExpContext,0)


        def vareqvalExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VareqvalExpContext,0)


        def ideqvalExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.IdeqvalExpContext,0)


        def ideqidExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.IdeqidExpContext,0)


        def ideqvallistExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.IdeqvallistExpContext,0)


        def questionref1Exp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.Questionref1ExpContext,0)


        def rulerefExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.RulerefExpContext,0)


        def stringref1Exp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.Stringref1ExpContext,0)


        def pushthisExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.PushthisExpContext,0)


        def securityExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.SecurityExpContext,0)


        def getExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GetExpContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExpressionBuildInFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExpressionBuildInFunction" ):
                return visitor.visitVfrExpressionBuildInFunction(self)
            else:
                return visitor.visitChildren(self)




    def vfrExpressionBuildInFunction(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VfrExpressionBuildInFunctionContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 336, self.RULE_vfrExpressionBuildInFunction)
        try:
            self.state = 2855
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Dup]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2844
                self.dupExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.VarEqVal]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2845
                self.vareqvalExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.IdEqVal]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2846
                self.ideqvalExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.IdEqId]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2847
                self.ideqidExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.IdEqValList]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2848
                self.ideqvallistExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.QuestionRef]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2849
                self.questionref1Exp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.RuleRef]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2850
                self.rulerefExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.StringRef]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2851
                self.stringref1Exp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.PushThis]:
                self.enterOuterAlt(localctx, 9)
                self.state = 2852
                self.pushthisExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Security]:
                self.enterOuterAlt(localctx, 10)
                self.state = 2853
                self.securityExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Get]:
                self.enterOuterAlt(localctx, 11)
                self.state = 2854
                self.getExp(ExpInfo)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DupExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = IfrTreeNode(EFI_IFR_DUP_OP)
            self.ExpInfo = ExpInfo

        def Dup(self):
            return self.getToken(SourceVfrSyntaxParser.Dup, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_dupExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDupExp" ):
                return visitor.visitDupExp(self)
            else:
                return visitor.visitChildren(self)




    def dupExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.DupExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 338, self.RULE_dupExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2857
            self.match(SourceVfrSyntaxParser.Dup)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VareqvalExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = None
            self.VN = None # Token
            self.ExpInfo = ExpInfo

        def VarEqVal(self):
            return self.getToken(SourceVfrSyntaxParser.VarEqVal, 0)

        def Var(self):
            return self.getToken(SourceVfrSyntaxParser.Var, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def Equal(self):
            return self.getToken(SourceVfrSyntaxParser.Equal, 0)

        def LessEqual(self):
            return self.getToken(SourceVfrSyntaxParser.LessEqual, 0)

        def Less(self):
            return self.getToken(SourceVfrSyntaxParser.Less, 0)

        def GreaterEqual(self):
            return self.getToken(SourceVfrSyntaxParser.GreaterEqual, 0)

        def Greater(self):
            return self.getToken(SourceVfrSyntaxParser.Greater, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vareqvalExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVareqvalExp" ):
                return visitor.visitVareqvalExp(self)
            else:
                return visitor.visitChildren(self)




    def vareqvalExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VareqvalExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 340, self.RULE_vareqvalExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2859
            self.match(SourceVfrSyntaxParser.VarEqVal)
            self.state = 2860
            self.match(SourceVfrSyntaxParser.Var)
            self.state = 2861
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2862
            localctx.VN = self.match(SourceVfrSyntaxParser.Number)
            self.state = 2863
            self.match(SourceVfrSyntaxParser.CloseParen)
            self.state = 2874
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Equal]:
                self.state = 2864
                self.match(SourceVfrSyntaxParser.Equal)
                self.state = 2865
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [SourceVfrSyntaxParser.LessEqual]:
                self.state = 2866
                self.match(SourceVfrSyntaxParser.LessEqual)
                self.state = 2867
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [SourceVfrSyntaxParser.Less]:
                self.state = 2868
                self.match(SourceVfrSyntaxParser.Less)
                self.state = 2869
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [SourceVfrSyntaxParser.GreaterEqual]:
                self.state = 2870
                self.match(SourceVfrSyntaxParser.GreaterEqual)
                self.state = 2871
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [SourceVfrSyntaxParser.Greater]:
                self.state = 2872
                self.match(SourceVfrSyntaxParser.Greater)
                self.state = 2873
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdeqvalExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = None
            self.I = None # Token
            self.ExpInfo = ExpInfo

        def vfrQuestionDataFieldName(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionDataFieldNameContext,0)


        def IdEqVal(self):
            return self.getToken(SourceVfrSyntaxParser.IdEqVal, 0)

        def Equal(self):
            return self.getToken(SourceVfrSyntaxParser.Equal, 0)

        def LessEqual(self):
            return self.getToken(SourceVfrSyntaxParser.LessEqual, 0)

        def Less(self):
            return self.getToken(SourceVfrSyntaxParser.Less, 0)

        def GreaterEqual(self):
            return self.getToken(SourceVfrSyntaxParser.GreaterEqual, 0)

        def Greater(self):
            return self.getToken(SourceVfrSyntaxParser.Greater, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_ideqvalExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdeqvalExp" ):
                return visitor.visitIdeqvalExp(self)
            else:
                return visitor.visitChildren(self)




    def ideqvalExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.IdeqvalExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 342, self.RULE_ideqvalExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2876
            localctx.I = self.match(SourceVfrSyntaxParser.IdEqVal)
            self.state = 2877
            self.vfrQuestionDataFieldName()
            self.state = 2888
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Equal]:
                self.state = 2878
                self.match(SourceVfrSyntaxParser.Equal)
                self.state = 2879
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [SourceVfrSyntaxParser.LessEqual]:
                self.state = 2880
                self.match(SourceVfrSyntaxParser.LessEqual)
                self.state = 2881
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [SourceVfrSyntaxParser.Less]:
                self.state = 2882
                self.match(SourceVfrSyntaxParser.Less)
                self.state = 2883
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [SourceVfrSyntaxParser.GreaterEqual]:
                self.state = 2884
                self.match(SourceVfrSyntaxParser.GreaterEqual)
                self.state = 2885
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [SourceVfrSyntaxParser.Greater]:
                self.state = 2886
                self.match(SourceVfrSyntaxParser.Greater)
                self.state = 2887
                _la = self._input.LA(1)
                if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdeqidExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = None
            self.I = None # Token
            self.E = None # Token
            self.LE = None # Token
            self.L = None # Token
            self.BE = None # Token
            self.B = None # Token
            self.ExpInfo = ExpInfo

        def vfrQuestionDataFieldName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrQuestionDataFieldNameContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionDataFieldNameContext,i)


        def IdEqId(self):
            return self.getToken(SourceVfrSyntaxParser.IdEqId, 0)

        def Equal(self):
            return self.getToken(SourceVfrSyntaxParser.Equal, 0)

        def LessEqual(self):
            return self.getToken(SourceVfrSyntaxParser.LessEqual, 0)

        def Less(self):
            return self.getToken(SourceVfrSyntaxParser.Less, 0)

        def GreaterEqual(self):
            return self.getToken(SourceVfrSyntaxParser.GreaterEqual, 0)

        def Greater(self):
            return self.getToken(SourceVfrSyntaxParser.Greater, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_ideqidExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdeqidExp" ):
                return visitor.visitIdeqidExp(self)
            else:
                return visitor.visitChildren(self)




    def ideqidExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.IdeqidExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 344, self.RULE_ideqidExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2890
            localctx.I = self.match(SourceVfrSyntaxParser.IdEqId)
            self.state = 2891
            self.vfrQuestionDataFieldName()
            self.state = 2902
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Equal]:
                self.state = 2892
                localctx.E = self.match(SourceVfrSyntaxParser.Equal)
                self.state = 2893
                self.vfrQuestionDataFieldName()
                pass
            elif token in [SourceVfrSyntaxParser.LessEqual]:
                self.state = 2894
                localctx.LE = self.match(SourceVfrSyntaxParser.LessEqual)
                self.state = 2895
                self.vfrQuestionDataFieldName()
                pass
            elif token in [SourceVfrSyntaxParser.Less]:
                self.state = 2896
                localctx.L = self.match(SourceVfrSyntaxParser.Less)
                self.state = 2897
                self.vfrQuestionDataFieldName()
                pass
            elif token in [SourceVfrSyntaxParser.GreaterEqual]:
                self.state = 2898
                localctx.BE = self.match(SourceVfrSyntaxParser.GreaterEqual)
                self.state = 2899
                self.vfrQuestionDataFieldName()
                pass
            elif token in [SourceVfrSyntaxParser.Greater]:
                self.state = 2900
                localctx.B = self.match(SourceVfrSyntaxParser.Greater)
                self.state = 2901
                self.vfrQuestionDataFieldName()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdeqvallistExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = None
            self.ExpInfo = ExpInfo

        def IdEqValList(self):
            return self.getToken(SourceVfrSyntaxParser.IdEqValList, 0)

        def vfrQuestionDataFieldName(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrQuestionDataFieldNameContext,0)


        def Equal(self):
            return self.getToken(SourceVfrSyntaxParser.Equal, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Number)
            else:
                return self.getToken(SourceVfrSyntaxParser.Number, i)

        def StringIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.StringIdentifier)
            else:
                return self.getToken(SourceVfrSyntaxParser.StringIdentifier, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_ideqvallistExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdeqvallistExp" ):
                return visitor.visitIdeqvallistExp(self)
            else:
                return visitor.visitChildren(self)




    def ideqvallistExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.IdeqvallistExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 346, self.RULE_ideqvallistExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2904
            self.match(SourceVfrSyntaxParser.IdEqValList)
            self.state = 2905
            self.vfrQuestionDataFieldName()
            self.state = 2906
            self.match(SourceVfrSyntaxParser.Equal)
            self.state = 2908
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2907
                    _la = self._input.LA(1)
                    if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 2910
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,272,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrQuestionDataFieldNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.QId = EFI_QUESTION_ID_INVALID
            self.Mask = 0
            self.VarIdStr = ''
            self.Line = None


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrQuestionDataFieldName


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.QId = ctx.QId
            self.Mask = ctx.Mask
            self.VarIdStr = ctx.VarIdStr
            self.Line = ctx.Line



    class VfrQuestionDataFieldNameRule2Context(VfrQuestionDataFieldNameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.VfrQuestionDataFieldNameContext
            super().__init__(parser)
            self.SN2 = None # Token
            self.copyFrom(ctx)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)
        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Dot)
            else:
                return self.getToken(SourceVfrSyntaxParser.Dot, i)
        def arrayName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.ArrayNameContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.ArrayNameContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrQuestionDataFieldNameRule2" ):
                return visitor.visitVfrQuestionDataFieldNameRule2(self)
            else:
                return visitor.visitChildren(self)


    class VfrQuestionDataFieldNameRule1Context(VfrQuestionDataFieldNameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SourceVfrSyntaxParser.VfrQuestionDataFieldNameContext
            super().__init__(parser)
            self.SN1 = None # Token
            self.I = None # Token
            self.copyFrom(ctx)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)
        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)
        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)
        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrQuestionDataFieldNameRule1" ):
                return visitor.visitVfrQuestionDataFieldNameRule1(self)
            else:
                return visitor.visitChildren(self)



    def vfrQuestionDataFieldName(self):

        localctx = SourceVfrSyntaxParser.VfrQuestionDataFieldNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_vfrQuestionDataFieldName)
        self._la = 0 # Token type
        try:
            self.state = 2924
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,274,self._ctx)
            if la_ == 1:
                localctx = SourceVfrSyntaxParser.VfrQuestionDataFieldNameRule1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2912
                localctx.SN1 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2913
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 2914
                localctx.I = self.match(SourceVfrSyntaxParser.Number)
                self.state = 2915
                self.match(SourceVfrSyntaxParser.CloseBracket)
                pass

            elif la_ == 2:
                localctx = SourceVfrSyntaxParser.VfrQuestionDataFieldNameRule2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2916
                localctx.SN2 = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2921
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SourceVfrSyntaxParser.Dot:
                    self.state = 2917
                    self.match(SourceVfrSyntaxParser.Dot)
                    self.state = 2918
                    self.arrayName()
                    self.state = 2923
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.SubStr = ''
            self.SubStrZ = ''
            self.N = None # Token

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def OpenBracket(self):
            return self.getToken(SourceVfrSyntaxParser.OpenBracket, 0)

        def CloseBracket(self):
            return self.getToken(SourceVfrSyntaxParser.CloseBracket, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_arrayName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayName" ):
                return visitor.visitArrayName(self)
            else:
                return visitor.visitChildren(self)




    def arrayName(self):

        localctx = SourceVfrSyntaxParser.ArrayNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_arrayName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2926
            self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 2930
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.OpenBracket:
                self.state = 2927
                self.match(SourceVfrSyntaxParser.OpenBracket)
                self.state = 2928
                localctx.N = self.match(SourceVfrSyntaxParser.Number)
                self.state = 2929
                self.match(SourceVfrSyntaxParser.CloseBracket)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Questionref1ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = IfrTreeNode(EFI_IFR_QUESTION_REF1_OP)
            self.ExpInfo = ExpInfo

        def QuestionRef(self):
            return self.getToken(SourceVfrSyntaxParser.QuestionRef, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_questionref1Exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestionref1Exp" ):
                return visitor.visitQuestionref1Exp(self)
            else:
                return visitor.visitChildren(self)




    def questionref1Exp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.Questionref1ExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 352, self.RULE_questionref1Exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2932
            self.match(SourceVfrSyntaxParser.QuestionRef)
            self.state = 2933
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2934
            _la = self._input.LA(1)
            if not(_la==SourceVfrSyntaxParser.Number or _la==SourceVfrSyntaxParser.StringIdentifier):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 2935
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RulerefExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = IfrTreeNode(EFI_IFR_RULE_REF_OP)
            self.ExpInfo = ExpInfo

        def RuleRef(self):
            return self.getToken(SourceVfrSyntaxParser.RuleRef, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_rulerefExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRulerefExp" ):
                return visitor.visitRulerefExp(self)
            else:
                return visitor.visitChildren(self)




    def rulerefExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.RulerefExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 354, self.RULE_rulerefExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2937
            self.match(SourceVfrSyntaxParser.RuleRef)
            self.state = 2938
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2939
            self.match(SourceVfrSyntaxParser.StringIdentifier)
            self.state = 2940
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stringref1ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = IfrTreeNode(EFI_IFR_STRING_REF1_OP)
            self.S = None # Token
            self.ExpInfo = ExpInfo

        def StringRef(self):
            return self.getToken(SourceVfrSyntaxParser.StringRef, 0)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_stringref1Exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringref1Exp" ):
                return visitor.visitStringref1Exp(self)
            else:
                return visitor.visitChildren(self)




    def stringref1Exp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.Stringref1ExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 356, self.RULE_stringref1Exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2942
            self.match(SourceVfrSyntaxParser.StringRef)
            self.state = 2943
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2949
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.StringToken]:
                self.state = 2944
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 2945
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 2946
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 2947
                self.match(SourceVfrSyntaxParser.CloseParen)
                pass
            elif token in [SourceVfrSyntaxParser.Number]:
                self.state = 2948
                self.match(SourceVfrSyntaxParser.Number)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2951
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PushthisExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = IfrTreeNode(EFI_IFR_THIS_OP)
            self.ExpInfo = ExpInfo

        def PushThis(self):
            return self.getToken(SourceVfrSyntaxParser.PushThis, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_pushthisExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPushthisExp" ):
                return visitor.visitPushthisExp(self)
            else:
                return visitor.visitChildren(self)




    def pushthisExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.PushthisExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 358, self.RULE_pushthisExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2953
            self.match(SourceVfrSyntaxParser.PushThis)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecurityExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = IfrTreeNode(EFI_IFR_SECURITY_OP)
            self.ExpInfo = ExpInfo

        def Security(self):
            return self.getToken(SourceVfrSyntaxParser.Security, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_securityExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecurityExp" ):
                return visitor.visitSecurityExp(self)
            else:
                return visitor.visitChildren(self)




    def securityExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.SecurityExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 360, self.RULE_securityExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2955
            self.match(SourceVfrSyntaxParser.Security)
            self.state = 2956
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2957
            self.guidDefinition()
            self.state = 2958
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericVarStoreTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.VarType = None

        def NumericSizeOne(self):
            return self.getToken(SourceVfrSyntaxParser.NumericSizeOne, 0)

        def NumericSizeTwo(self):
            return self.getToken(SourceVfrSyntaxParser.NumericSizeTwo, 0)

        def NumericSizeFour(self):
            return self.getToken(SourceVfrSyntaxParser.NumericSizeFour, 0)

        def NumericSizeEight(self):
            return self.getToken(SourceVfrSyntaxParser.NumericSizeEight, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_numericVarStoreType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericVarStoreType" ):
                return visitor.visitNumericVarStoreType(self)
            else:
                return visitor.visitChildren(self)




    def numericVarStoreType(self):

        localctx = SourceVfrSyntaxParser.NumericVarStoreTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_numericVarStoreType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2960
            _la = self._input.LA(1)
            if not(((((_la - 237)) & ~0x3f) == 0 and ((1 << (_la - 237)) & ((1 << (SourceVfrSyntaxParser.NumericSizeOne - 237)) | (1 << (SourceVfrSyntaxParser.NumericSizeTwo - 237)) | (1 << (SourceVfrSyntaxParser.NumericSizeFour - 237)) | (1 << (SourceVfrSyntaxParser.NumericSizeEight - 237)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.BaseInfo = EFI_VARSTORE_INFO()
            self.Node = IfrTreeNode(EFI_IFR_GET_OP)
            self.ExpInfo = ExpInfo

        def Get(self):
            return self.getToken(SourceVfrSyntaxParser.Get, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStorageVarId(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStorageVarIdContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def BitWiseOr(self):
            return self.getToken(SourceVfrSyntaxParser.BitWiseOr, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def numericVarStoreType(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.NumericVarStoreTypeContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_getExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetExp" ):
                return visitor.visitGetExp(self)
            else:
                return visitor.visitChildren(self)




    def getExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.GetExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 364, self.RULE_getExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2962
            self.match(SourceVfrSyntaxParser.Get)
            self.state = 2963
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2964
            self.vfrStorageVarId(localctx.BaseInfo, False)
            self.state = 2969
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 2965
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 2966
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 2967
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 2968
                self.numericVarStoreType()


            self.state = 2971
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExpressionConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Node = None
            self.ExpInfo = ExpInfo

        def TrueSymbol(self):
            return self.getToken(SourceVfrSyntaxParser.TrueSymbol, 0)

        def FalseSymbol(self):
            return self.getToken(SourceVfrSyntaxParser.FalseSymbol, 0)

        def One(self):
            return self.getToken(SourceVfrSyntaxParser.One, 0)

        def Ones(self):
            return self.getToken(SourceVfrSyntaxParser.Ones, 0)

        def Zero(self):
            return self.getToken(SourceVfrSyntaxParser.Zero, 0)

        def Undefined(self):
            return self.getToken(SourceVfrSyntaxParser.Undefined, 0)

        def Version(self):
            return self.getToken(SourceVfrSyntaxParser.Version, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExpressionConstant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExpressionConstant" ):
                return visitor.visitVfrExpressionConstant(self)
            else:
                return visitor.visitChildren(self)




    def vfrExpressionConstant(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VfrExpressionConstantContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 366, self.RULE_vfrExpressionConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2973
            _la = self._input.LA(1)
            if not(((((_la - 209)) & ~0x3f) == 0 and ((1 << (_la - 209)) & ((1 << (SourceVfrSyntaxParser.TrueSymbol - 209)) | (1 << (SourceVfrSyntaxParser.FalseSymbol - 209)) | (1 << (SourceVfrSyntaxParser.One - 209)) | (1 << (SourceVfrSyntaxParser.Ones - 209)) | (1 << (SourceVfrSyntaxParser.Zero - 209)) | (1 << (SourceVfrSyntaxParser.Undefined - 209)) | (1 << (SourceVfrSyntaxParser.Version - 209)) | (1 << (SourceVfrSyntaxParser.Number - 209)) | (1 << (SourceVfrSyntaxParser.StringIdentifier - 209)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExpressionUnaryOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = None
            self.ExpInfo = ExpInfo

        def lengthExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.LengthExpContext,0)


        def bitwisenotExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.BitwisenotExpContext,0)


        def question23refExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.Question23refExpContext,0)


        def stringref2Exp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.Stringref2ExpContext,0)


        def toboolExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ToboolExpContext,0)


        def tostringExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.TostringExpContext,0)


        def unintExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.UnintExpContext,0)


        def toupperExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ToupperExpContext,0)


        def tolwerExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.TolwerExpContext,0)


        def setExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.SetExpContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExpressionUnaryOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExpressionUnaryOp" ):
                return visitor.visitVfrExpressionUnaryOp(self)
            else:
                return visitor.visitChildren(self)




    def vfrExpressionUnaryOp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VfrExpressionUnaryOpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 368, self.RULE_vfrExpressionUnaryOp)
        try:
            self.state = 2985
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Length]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2975
                self.lengthExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.BitWiseNot]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2976
                self.bitwisenotExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.QuestionRefVal]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2977
                self.question23refExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.StringRefVal]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2978
                self.stringref2Exp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.BoolVal]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2979
                self.toboolExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.StringVal]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2980
                self.tostringExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.UnIntVal]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2981
                self.unintExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.ToUpper]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2982
                self.toupperExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.ToLower]:
                self.enterOuterAlt(localctx, 9)
                self.state = 2983
                self.tolwerExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Set]:
                self.enterOuterAlt(localctx, 10)
                self.state = 2984
                self.setExp(ExpInfo)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LengthExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Length(self):
            return self.getToken(SourceVfrSyntaxParser.Length, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_lengthExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLengthExp" ):
                return visitor.visitLengthExp(self)
            else:
                return visitor.visitChildren(self)




    def lengthExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.LengthExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 370, self.RULE_lengthExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2987
            self.match(SourceVfrSyntaxParser.Length)
            self.state = 2988
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2989
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 2990
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwisenotExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def BitWiseNot(self):
            return self.getToken(SourceVfrSyntaxParser.BitWiseNot, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_bitwisenotExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwisenotExp" ):
                return visitor.visitBitwisenotExp(self)
            else:
                return visitor.visitChildren(self)




    def bitwisenotExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.BitwisenotExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 372, self.RULE_bitwisenotExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2992
            self.match(SourceVfrSyntaxParser.BitWiseNot)
            self.state = 2993
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 2994
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 2995
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Question23refExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.S = None # Token
            self.ExpInfo = ExpInfo

        def QuestionRefVal(self):
            return self.getToken(SourceVfrSyntaxParser.QuestionRefVal, 0)

        def OpenParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.OpenParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.OpenParen, i)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.CloseParen)
            else:
                return self.getToken(SourceVfrSyntaxParser.CloseParen, i)

        def DevicePath(self):
            return self.getToken(SourceVfrSyntaxParser.DevicePath, 0)

        def StringToken(self):
            return self.getToken(SourceVfrSyntaxParser.StringToken, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Uuid(self):
            return self.getToken(SourceVfrSyntaxParser.Uuid, 0)

        def guidDefinition(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.GuidDefinitionContext,0)


        def StringIdentifier(self):
            return self.getToken(SourceVfrSyntaxParser.StringIdentifier, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_question23refExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestion23refExp" ):
                return visitor.visitQuestion23refExp(self)
            else:
                return visitor.visitChildren(self)




    def question23refExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.Question23refExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 374, self.RULE_question23refExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2997
            self.match(SourceVfrSyntaxParser.QuestionRefVal)
            self.state = 2998
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3006
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.DevicePath:
                self.state = 2999
                self.match(SourceVfrSyntaxParser.DevicePath)
                self.state = 3000
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 3001
                self.match(SourceVfrSyntaxParser.StringToken)
                self.state = 3002
                self.match(SourceVfrSyntaxParser.OpenParen)
                self.state = 3003
                localctx.S = self.match(SourceVfrSyntaxParser.StringIdentifier)
                self.state = 3004
                self.match(SourceVfrSyntaxParser.CloseParen)
                self.state = 3005
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 3013
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.Uuid:
                self.state = 3008
                self.match(SourceVfrSyntaxParser.Uuid)
                self.state = 3009
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 3010
                self.guidDefinition()
                self.state = 3011
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 3015
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3016
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stringref2ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def StringRefVal(self):
            return self.getToken(SourceVfrSyntaxParser.StringRefVal, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_stringref2Exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringref2Exp" ):
                return visitor.visitStringref2Exp(self)
            else:
                return visitor.visitChildren(self)




    def stringref2Exp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.Stringref2ExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 376, self.RULE_stringref2Exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3018
            self.match(SourceVfrSyntaxParser.StringRefVal)
            self.state = 3019
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3020
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3021
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToboolExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def BoolVal(self):
            return self.getToken(SourceVfrSyntaxParser.BoolVal, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_toboolExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToboolExp" ):
                return visitor.visitToboolExp(self)
            else:
                return visitor.visitChildren(self)




    def toboolExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.ToboolExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 378, self.RULE_toboolExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3023
            self.match(SourceVfrSyntaxParser.BoolVal)
            self.state = 3024
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3025
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3026
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TostringExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def StringVal(self):
            return self.getToken(SourceVfrSyntaxParser.StringVal, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_tostringExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTostringExp" ):
                return visitor.visitTostringExp(self)
            else:
                return visitor.visitChildren(self)




    def tostringExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.TostringExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 380, self.RULE_tostringExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3028
            self.match(SourceVfrSyntaxParser.StringVal)
            self.state = 3033
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.T__14:
                self.state = 3029
                self.match(SourceVfrSyntaxParser.T__14)
                self.state = 3030
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 3031
                self.match(SourceVfrSyntaxParser.Number)
                self.state = 3032
                self.match(SourceVfrSyntaxParser.Comma)


            self.state = 3035
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3036
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3037
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnintExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def UnIntVal(self):
            return self.getToken(SourceVfrSyntaxParser.UnIntVal, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_unintExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnintExp" ):
                return visitor.visitUnintExp(self)
            else:
                return visitor.visitChildren(self)




    def unintExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.UnintExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 382, self.RULE_unintExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3039
            self.match(SourceVfrSyntaxParser.UnIntVal)
            self.state = 3040
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3041
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3042
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToupperExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def ToUpper(self):
            return self.getToken(SourceVfrSyntaxParser.ToUpper, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_toupperExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToupperExp" ):
                return visitor.visitToupperExp(self)
            else:
                return visitor.visitChildren(self)




    def toupperExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.ToupperExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 384, self.RULE_toupperExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3044
            self.match(SourceVfrSyntaxParser.ToUpper)
            self.state = 3045
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3046
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3047
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TolwerExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def ToLower(self):
            return self.getToken(SourceVfrSyntaxParser.ToLower, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_tolwerExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTolwerExp" ):
                return visitor.visitTolwerExp(self)
            else:
                return visitor.visitChildren(self)




    def tolwerExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.TolwerExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 386, self.RULE_tolwerExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3049
            self.match(SourceVfrSyntaxParser.ToLower)
            self.state = 3050
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3051
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3052
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.BaseInfo = EFI_VARSTORE_INFO()
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Set(self):
            return self.getToken(SourceVfrSyntaxParser.Set, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStorageVarId(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStorageVarIdContext,0)


        def Comma(self):
            return self.getToken(SourceVfrSyntaxParser.Comma, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def BitWiseOr(self):
            return self.getToken(SourceVfrSyntaxParser.BitWiseOr, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def numericVarStoreType(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.NumericVarStoreTypeContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_setExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetExp" ):
                return visitor.visitSetExp(self)
            else:
                return visitor.visitChildren(self)




    def setExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.SetExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 388, self.RULE_setExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3054
            self.match(SourceVfrSyntaxParser.Set)
            self.state = 3055
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3056
            self.vfrStorageVarId(localctx.BaseInfo, False)
            self.state = 3061
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 3057
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 3058
                self.match(SourceVfrSyntaxParser.FLAGS)
                self.state = 3059
                self.match(SourceVfrSyntaxParser.T__5)
                self.state = 3060
                self.numericVarStoreType()


            self.state = 3063
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3064
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3065
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExpressionTernaryOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = None
            self.ExpInfo = ExpInfo

        def conditionalExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.ConditionalExpContext,0)


        def findExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.FindExpContext,0)


        def midExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.MidExpContext,0)


        def tokenExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.TokenExpContext,0)


        def spanExp(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.SpanExpContext,0)


        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExpressionTernaryOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExpressionTernaryOp" ):
                return visitor.visitVfrExpressionTernaryOp(self)
            else:
                return visitor.visitChildren(self)




    def vfrExpressionTernaryOp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VfrExpressionTernaryOpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 390, self.RULE_vfrExpressionTernaryOp)
        try:
            self.state = 3072
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SourceVfrSyntaxParser.Cond]:
                self.enterOuterAlt(localctx, 1)
                self.state = 3067
                self.conditionalExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Find]:
                self.enterOuterAlt(localctx, 2)
                self.state = 3068
                self.findExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Mid]:
                self.enterOuterAlt(localctx, 3)
                self.state = 3069
                self.midExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Tok]:
                self.enterOuterAlt(localctx, 4)
                self.state = 3070
                self.tokenExp(ExpInfo)
                pass
            elif token in [SourceVfrSyntaxParser.Span]:
                self.enterOuterAlt(localctx, 5)
                self.state = 3071
                self.spanExp(ExpInfo)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Cond(self):
            return self.getToken(SourceVfrSyntaxParser.Cond, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExpressionSubContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,i)


        def Colon(self):
            return self.getToken(SourceVfrSyntaxParser.Colon, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_conditionalExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalExp" ):
                return visitor.visitConditionalExp(self)
            else:
                return visitor.visitChildren(self)




    def conditionalExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.ConditionalExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 392, self.RULE_conditionalExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3074
            self.match(SourceVfrSyntaxParser.Cond)
            self.state = 3075
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3076
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3077
            self.match(SourceVfrSyntaxParser.T__15)
            self.state = 3078
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3079
            self.match(SourceVfrSyntaxParser.Colon)
            self.state = 3080
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3081
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FindExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Find(self):
            return self.getToken(SourceVfrSyntaxParser.Find, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def findFormat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.FindFormatContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.FindFormatContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementExpressionSub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExpressionSubContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,i)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_findExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFindExp" ):
                return visitor.visitFindExp(self)
            else:
                return visitor.visitChildren(self)




    def findExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.FindExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 394, self.RULE_findExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3083
            self.match(SourceVfrSyntaxParser.Find)
            self.state = 3084
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3085
            self.findFormat(ExpInfo)
            self.state = 3090
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 3086
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 3087
                self.findFormat(ExpInfo)
                self.state = 3092
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 3093
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3094
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3095
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3096
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3097
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3098
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3099
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FindFormatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Format = 0
            self.ExpInfo = ExpInfo

        def Sensitive(self):
            return self.getToken(SourceVfrSyntaxParser.Sensitive, 0)

        def Insensitive(self):
            return self.getToken(SourceVfrSyntaxParser.Insensitive, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_findFormat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFindFormat" ):
                return visitor.visitFindFormat(self)
            else:
                return visitor.visitChildren(self)




    def findFormat(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.FindFormatContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 396, self.RULE_findFormat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3101
            _la = self._input.LA(1)
            if not(_la==SourceVfrSyntaxParser.Insensitive or _la==SourceVfrSyntaxParser.Sensitive):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MidExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Mid(self):
            return self.getToken(SourceVfrSyntaxParser.Mid, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExpressionSubContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_midExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMidExp" ):
                return visitor.visitMidExp(self)
            else:
                return visitor.visitChildren(self)




    def midExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.MidExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 398, self.RULE_midExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3103
            self.match(SourceVfrSyntaxParser.Mid)
            self.state = 3104
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3105
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3106
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3107
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3108
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3109
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3110
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Tok(self):
            return self.getToken(SourceVfrSyntaxParser.Tok, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExpressionSubContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_tokenExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenExp" ):
                return visitor.visitTokenExp(self)
            else:
                return visitor.visitChildren(self)




    def tokenExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.TokenExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 400, self.RULE_tokenExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3112
            self.match(SourceVfrSyntaxParser.Tok)
            self.state = 3113
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3114
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3115
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3116
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3117
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3118
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3119
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpanExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.ExpInfo = ExpInfo

        def Span(self):
            return self.getToken(SourceVfrSyntaxParser.Span, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def FLAGS(self):
            return self.getToken(SourceVfrSyntaxParser.FLAGS, 0)

        def spanFlags(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.SpanFlagsContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.SpanFlagsContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def vfrStatementExpressionSub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExpressionSubContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,i)


        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def BitWiseOr(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.BitWiseOr)
            else:
                return self.getToken(SourceVfrSyntaxParser.BitWiseOr, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_spanExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpanExp" ):
                return visitor.visitSpanExp(self)
            else:
                return visitor.visitChildren(self)




    def spanExp(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.SpanExpContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 402, self.RULE_spanExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3121
            self.match(SourceVfrSyntaxParser.Span)
            self.state = 3122
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3123
            self.match(SourceVfrSyntaxParser.FLAGS)
            self.state = 3124
            self.match(SourceVfrSyntaxParser.T__5)
            self.state = 3125
            self.spanFlags()
            self.state = 3130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.BitWiseOr:
                self.state = 3126
                self.match(SourceVfrSyntaxParser.BitWiseOr)
                self.state = 3127
                self.spanFlags()
                self.state = 3132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 3133
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3134
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3135
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3136
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3137
            self.match(SourceVfrSyntaxParser.Comma)
            self.state = 3138
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3139
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpanFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Flag = 0

        def Number(self):
            return self.getToken(SourceVfrSyntaxParser.Number, 0)

        def LastNonMatch(self):
            return self.getToken(SourceVfrSyntaxParser.LastNonMatch, 0)

        def FirstNonMatch(self):
            return self.getToken(SourceVfrSyntaxParser.FirstNonMatch, 0)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_spanFlags

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpanFlags" ):
                return visitor.visitSpanFlags(self)
            else:
                return visitor.visitChildren(self)




    def spanFlags(self):

        localctx = SourceVfrSyntaxParser.SpanFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_spanFlags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3141
            _la = self._input.LA(1)
            if not(((((_la - 246)) & ~0x3f) == 0 and ((1 << (_la - 246)) & ((1 << (SourceVfrSyntaxParser.LastNonMatch - 246)) | (1 << (SourceVfrSyntaxParser.FirstNonMatch - 246)) | (1 << (SourceVfrSyntaxParser.Number - 246)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VfrExpressionMapContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, ExpInfo=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ExpInfo = None
            self.Nodes = []
            self.Node = IfrTreeNode()
            self.ExpInfo = ExpInfo

        def Map(self):
            return self.getToken(SourceVfrSyntaxParser.Map, 0)

        def OpenParen(self):
            return self.getToken(SourceVfrSyntaxParser.OpenParen, 0)

        def vfrStatementExpressionSub(self):
            return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionSubContext,0)


        def Colon(self):
            return self.getToken(SourceVfrSyntaxParser.Colon, 0)

        def CloseParen(self):
            return self.getToken(SourceVfrSyntaxParser.CloseParen, 0)

        def vfrStatementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SourceVfrSyntaxParser.VfrStatementExpressionContext)
            else:
                return self.getTypedRuleContext(SourceVfrSyntaxParser.VfrStatementExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Comma)
            else:
                return self.getToken(SourceVfrSyntaxParser.Comma, i)

        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SourceVfrSyntaxParser.Semicolon)
            else:
                return self.getToken(SourceVfrSyntaxParser.Semicolon, i)

        def getRuleIndex(self):
            return SourceVfrSyntaxParser.RULE_vfrExpressionMap

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVfrExpressionMap" ):
                return visitor.visitVfrExpressionMap(self)
            else:
                return visitor.visitChildren(self)




    def vfrExpressionMap(self, ExpInfo):

        localctx = SourceVfrSyntaxParser.VfrExpressionMapContext(self, self._ctx, self.state, ExpInfo)
        self.enterRule(localctx, 406, self.RULE_vfrExpressionMap)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3143
            self.match(SourceVfrSyntaxParser.Map)
            self.state = 3144
            self.match(SourceVfrSyntaxParser.OpenParen)
            self.state = 3145
            self.vfrStatementExpressionSub(localctx.Nodes)
            self.state = 3146
            self.match(SourceVfrSyntaxParser.Colon)
            self.state = 3154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SourceVfrSyntaxParser.OpenParen or ((((_la - 192)) & ~0x3f) == 0 and ((1 << (_la - 192)) & ((1 << (SourceVfrSyntaxParser.Cond - 192)) | (1 << (SourceVfrSyntaxParser.Find - 192)) | (1 << (SourceVfrSyntaxParser.Mid - 192)) | (1 << (SourceVfrSyntaxParser.Tok - 192)) | (1 << (SourceVfrSyntaxParser.Span - 192)) | (1 << (SourceVfrSyntaxParser.Dup - 192)) | (1 << (SourceVfrSyntaxParser.VarEqVal - 192)) | (1 << (SourceVfrSyntaxParser.IdEqVal - 192)) | (1 << (SourceVfrSyntaxParser.IdEqId - 192)) | (1 << (SourceVfrSyntaxParser.IdEqValList - 192)) | (1 << (SourceVfrSyntaxParser.QuestionRef - 192)) | (1 << (SourceVfrSyntaxParser.RuleRef - 192)) | (1 << (SourceVfrSyntaxParser.StringRef - 192)) | (1 << (SourceVfrSyntaxParser.PushThis - 192)) | (1 << (SourceVfrSyntaxParser.Security - 192)) | (1 << (SourceVfrSyntaxParser.Get - 192)) | (1 << (SourceVfrSyntaxParser.TrueSymbol - 192)) | (1 << (SourceVfrSyntaxParser.FalseSymbol - 192)) | (1 << (SourceVfrSyntaxParser.One - 192)) | (1 << (SourceVfrSyntaxParser.Ones - 192)) | (1 << (SourceVfrSyntaxParser.Zero - 192)) | (1 << (SourceVfrSyntaxParser.Undefined - 192)) | (1 << (SourceVfrSyntaxParser.Version - 192)) | (1 << (SourceVfrSyntaxParser.Length - 192)) | (1 << (SourceVfrSyntaxParser.NOT - 192)) | (1 << (SourceVfrSyntaxParser.Set - 192)) | (1 << (SourceVfrSyntaxParser.BitWiseNot - 192)) | (1 << (SourceVfrSyntaxParser.BoolVal - 192)) | (1 << (SourceVfrSyntaxParser.StringVal - 192)) | (1 << (SourceVfrSyntaxParser.UnIntVal - 192)) | (1 << (SourceVfrSyntaxParser.ToUpper - 192)) | (1 << (SourceVfrSyntaxParser.ToLower - 192)) | (1 << (SourceVfrSyntaxParser.Match - 192)) | (1 << (SourceVfrSyntaxParser.Match2 - 192)) | (1 << (SourceVfrSyntaxParser.Catenate - 192)) | (1 << (SourceVfrSyntaxParser.QuestionRefVal - 192)) | (1 << (SourceVfrSyntaxParser.StringRefVal - 192)) | (1 << (SourceVfrSyntaxParser.Map - 192)) | (1 << (SourceVfrSyntaxParser.Number - 192)) | (1 << (SourceVfrSyntaxParser.StringIdentifier - 192)))) != 0):
                self.state = 3147
                self.vfrStatementExpression(localctx.Node)
                self.state = 3148
                self.match(SourceVfrSyntaxParser.Comma)
                self.state = 3149
                self.vfrStatementExpression(localctx.Node)
                self.state = 3150
                self.match(SourceVfrSyntaxParser.Semicolon)
                self.state = 3156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 3157
            self.match(SourceVfrSyntaxParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





