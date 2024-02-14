import base64

string1 = ""
string2 = ""

a = string1
A = base64.b64decode(a)

b = string2
B = base64.b64decode(b)

c = []
l = len(A)

i = 0
while i < l:
  c.append(chr(A[i] ^ B[i]))
  i += 1

print(c)
print(''.join(c))

