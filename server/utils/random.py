import random
import string

def random_string(string_length = 10):
  letters = string.ascii_lowercase
  return ''.join(random.choice(letters) for i in range(string_length))