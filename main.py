def main():
   wordcount = 0
   words_dict = {}
   words_string = ""
   strings_set = set()

   with open("books/frankenstein.txt") as f:
     print("--- Begin report of books/frankenstein.txt ---")
     file_contents = f.read()
     words = file_contents.split()
     words_string = file_contents.lower()

     for word in words:
        wordcount += 1 
     print(wordcount , "words found in the document")

     for word_string in words_string:
        if word_string.isalpha():
           strings_set.add(word_string)

     for strings in strings_set:
        for word_string in words_string:
           if word_string == strings:
              words_dict[strings] = words_dict.get(strings, 0) + 1

     words_dict = dict(sorted(words_dict.items(), reverse=True, key= lambda item: item[1]))
     
     for word_dict, value in words_dict.items():
        print ("The" , word_dict,"character was found" , value, "times") 

    
     print("--- End report ---")


main()