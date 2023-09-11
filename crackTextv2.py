import requests

def getWordsWithLength(length, words):
  return [word for word in words if len(word) == length]

def applyKeyToText(key, text):
  return ''.join(key.get(char, char) for char in text)

def applyKeyToAllText(key, all_text):
  return [applyKeyToText(key, text) for text in all_text]

def isKeyInvalid(key, letter):
  return key.get(letter) is not None

def isKeyValid(key, letter):
  return key.get(letter) is None

def word_length_sort(word):
    return len(word)

def generatePossibleSentence(list_target_word, sorted_word, key_mapped, word_mapped, collection_all_words, size_word, current_word):
  # print(current_word)
  # print(size_word)
  if current_word == size_word:
    print("crete sentence")
    sentence = ''
    for word in list_target_word:
      sentence += word_mapped.get(word) + ' '
    print(sentence)
    return

  # print(sorted_word)
  real_current_word = sorted_word[current_word]
  # print(real_current_word)
  current_word_length = len(real_current_word)
  # print(collection_all_words)
  for pos_word in collection_all_words[current_word_length-1]:
      # print(pos_word)
      check_word = True
      # print(pos_word)
      for i in range(current_word_length):
        if (isKeyInvalid(key_mapped, real_current_word[i]) and str(word_mapped.get(real_current_word))[i] != str(pos_word[i])):
          check_word = False
          break

      if check_word:
        # if current_word==2:
        #    print("check2 check word")
        # print("check pass")
        # print(pos_word)

        # items_key_mapped = list(key_mapped.items())
        values_key_mapped = key_mapped.values()
        # for i in range(current_word_length):
        #   # value = items_key_mapped[i][1]
        #   for j in range(len(items_key_mapped)):
        #     if items_key_mapped[j][1] == pos_word[i] and items_key_mapped[j][0] != real_current_word[i]:
        #       return
        #   if values_key_mapped.find(pos_word[i]) != -1 and real_current_word[i] != key:
        #     return
        # for i in range(len(dup_case)):
        #   if pos_word.find(dup_case[i]) == -1:
        #     return

        # new_dup_case = dup_case.copy()
        # for i in range(current_word_length):
        #   new_dup_case.append(pos_word[i])

        new_key_mapped = key_mapped.copy()
        check_double_again = True
        for i in range(current_word_length):
          check_again = True
          items_key_mapped = list(new_key_mapped.items())
          for j in range(len(items_key_mapped)):
            if items_key_mapped[j][1] == pos_word[i] and items_key_mapped[j][0] != real_current_word[i] and pos_word[i] != real_current_word[i]:
              check_again = False
              check_double_again = False
              break
          if check_again == False:
            break
          new_key_mapped[str(real_current_word[i])] = str(pos_word[i])

        if check_double_again == False:
          # if current_word==2:
          #   print("check double again")
          #   sentence = ''
          #   for word in list_target_word:
          #     sentence += word_mapped.get(word) + ' '
          #   print(sentence)
            continue

        # for i in range(current_word_length):
        #   # value = items_key_mapped[i][1]
        #   for j in range(len(items_key_mapped)):
        #     if items_key_mapped[j][1] == pos_word[i] and items_key_mapped[j][0] != real_current_word[i]:
        #       return

        new_word_mapped = word_mapped.copy()
        new_word_mapped[str(real_current_word)] = str(pos_word)
        # for k in list_target_word:
        #   new_word_mapped[str(k)] = str(applyKeyToText(new_key_mapped, k))
        # new_all_word = applyKeyToAllText(key_mapped, sorted_word)
        new_current_word = current_word + 1
        generatePossibleSentence(list_target_word, sorted_word, new_key_mapped, new_word_mapped, collection_all_words, size_word, new_current_word)


def main():
  print("hello")
  target_text = "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."
  # target_text = "FP QDR QDFP" # QDFP = tDis
  url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
  all_words = []
  path_in = "crazy_dict.txt"
  file_input = open(path_in, "r")
  for line in file_input:
    word = line.lower().strip()
    all_words.append(word)
  file_input.close()

  # all_words = requests.get(url).text.strip().split('\n')
  key_mapped = dict()
  word_mapped = dict()

  print(all_words)

  words_15_letters = getWordsWithLength(15, all_words)
  words_14_letters = getWordsWithLength(14, all_words)
  words_13_letters = getWordsWithLength(13, all_words)
  words_12_letters = getWordsWithLength(12, all_words)
  words_11_letters = getWordsWithLength(11, all_words)
  words_10_letters = getWordsWithLength(10, all_words)
  words_9_letters = getWordsWithLength(9, all_words)
  words_8_letters = getWordsWithLength(8, all_words)
  words_7_letters = getWordsWithLength(7, all_words)
  words_6_letters = getWordsWithLength(6, all_words)
  words_5_letters = getWordsWithLength(5, all_words)
  words_4_letters = getWordsWithLength(4, all_words)
  words_3_letters = getWordsWithLength(3, all_words)
  words_2_letters = getWordsWithLength(2, all_words)
  words_1_letters = getWordsWithLength(1, all_words)
  collection_all_words = [words_1_letters, words_2_letters, words_3_letters, words_4_letters, words_5_letters, words_6_letters, words_7_letters, words_8_letters, words_9_letters, words_10_letters, words_11_letters, words_12_letters, words_13_letters, words_14_letters, words_15_letters]
  words = target_text.split()
  list_target_word = [word.strip('.') for word in words]

  sorted_words = sorted(list_target_word, key=word_length_sort)
  print(sorted_words)

  for i in sorted_words:
    word_mapped[i] = i

  generatePossibleSentence(list_target_word, sorted_words, key_mapped, word_mapped, collection_all_words, len(sorted_words), 0)



if __name__ == '__main__':
  main()