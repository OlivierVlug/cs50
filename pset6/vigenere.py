import cs50
import sys

def main():
    if len(sys.argv) != 2:
        print("You should provide a cmd line arguments!")
        exit(1)
    
    if sys.argv[1].isalpha() == False:
        print("You should provide valid keyword!")
        exit(1)
