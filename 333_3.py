def reverse_words(sentence):
    words = sentence.split() 
    reversed_sentence = ' '.join(words[::-1]) 
    return reversed_sentence

input_sentence = "Hello World! This is a test."
reversed_sentence = reverse_words(input_sentence)
print("Реверс слів у введеному реченні:", reversed_sentence)
