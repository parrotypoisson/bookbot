def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents

def count(book):
    return len(book.split())

def chars(book):
    count = {}

    for x in book.lower():
        count[x] = count.get(x, 0) + 1
    
    return count

def report(book):
    final = ['--- Begin report of books/frankenstein.txt ---']
    final.append(f'{count(book)} words found in the document')
    final.append('')
    for k,v in chars(book).items():
        if k.isalpha():
            final.append(f"The '{k}' character was found {v} times")
    final.append('--- End report ---')
    return '\n'.join(final)

print(report(main()))