# a program to count number of times a word has occured in text
import string
def cnt_wrd(word: str) -> int:

    text = """Hii there i am abhi. my full name is Abhinav
                but they call me abhi too
                i dont like abhi
                abhi feels so clingy
                they figured out that my name was abhi 
                in school"""

    count = text.count(word)
    print(count)

cnt_wrd("abhi")




