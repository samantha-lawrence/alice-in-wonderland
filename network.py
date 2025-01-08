
import re

with open('alice-in-wonderland-book.txt', 'r', encoding='utf8') as txtfile:
    book = txtfile.read() 



book = book[book.find("Alice’s Evidence")+len("Alice’s Evidence"):book.find("*** END OF THE PROJECT GUTENBERG EBOOK")]

print(book[:1000])