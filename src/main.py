print("Hello World!")

from textnode import TextNode

def main():
    dummy1 = TextNode("bold test", "bold", "boot.dev")
    dummy2 = TextNode("bold tests", "bold", "boot.dev")
    print(dummy1)
    print(dummy2)
    print(dummy1 == dummy2)
    
    
main()