
def reverse_sentence(sentence):
  reversed_sentence = ' '.join(reversed(sentence.split()))
  return reversed_sentence

def count_words_in_sentence(sentence):
  words = sentence.split()
  sentence_length = len(words)
  return sentence_length

def count_occurrences_of_word_in_sentence(sentence):
  occurrences = {}
  words = sentence.split()

  for word in words:
    if word in occurrences:
      occurrences[word] += 1
    else:
      occurrences[word] = 1

  return occurrences

sentence = 'Playing with words is fun fun fun'

print(sentence)
print('Reversed: ' + reverse_sentence(sentence))
print('Number of words: ', count_words_in_sentence(sentence))
print('Occurrences: ', count_occurrences_of_word_in_sentence(sentence))

