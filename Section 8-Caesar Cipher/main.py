alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text):
  b=int(len(text))
  if direction=='encode':
    while b>=1:
      a=text[-b]
      i=alphabet.index(a)
      s=str(int(i)+shift)
      b-=1
      if b==-1:
        break
      x=alphabet[int(s)]
      print(x, end='')
      
  elif direction=='decode':
    while b>=1:
      a=text[-b]
      i=alphabet.index(a)
      s=str(int(i)-shift)
      b-=1
      if b==-1:
        break
      x=alphabet[int(s)]
      print(x, end='')
      
  else:
    print('chose one')


encrypt(text)