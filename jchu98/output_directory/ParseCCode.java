import java.io.*;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class ParseCCode {

    public static void main(String[] args) throws Exception {
        
	PrintStream fileOut = new PrintStream("output.txt");
        System.setOut(fileOut);

	// create a CharStream that reads from standard input
        CharStream input = CharStreams.fromFileName("example.c");  // adjust the input source

        // create a lexer that feeds off of input CharStream
        CLexer lexer = new CLexer(input);

        // create a buffer of tokens pulled from the lexer
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // create a parser that feeds off the tokens buffer
        CParser parser = new CParser(tokens);

        // begin parsing at the compilationUnit rule
        ParseTree tree = parser.compilationUnit();

        // print LISP-style tree
        System.out.println(tree.toStringTree(parser));

	fileOut.close();
    }
}
