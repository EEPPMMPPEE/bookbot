import os
from collections import Counter
from string import ascii_lowercase as lc

def get_file_name():
  file_names = os.listdir('./books')
  for n, x in enumerate(file_names, 1):
    print(f"To select: {x}\t<< enter {n} >>")
  while True:
    try:
      in_num = int(input())
      selected_book = file_names[in_num-1]
      break
    except Exception:
      print("Something wrong")
  return selected_book

def get_str_from_file(filename: str):
  with open(f"books/{filename}", 'r', encoding="utf-8") as file:
    return file.read()

def information_about(text, book_name):
  print(f"--- Begin report of books/{book_name} ---")
  print(f'{len(text.split())} words found in the document')
  for key, value in sorted(Counter(filter(lambda x: x in lc, text.lower())).items(), key=lambda x: -x[1]):
    print(f"The '{key}' character was found {value} times")

def main():
  book_name = get_file_name()
  text = get_str_from_file(book_name)
  information_about(text, book_name)

if __name__ == "__main__":
  main()