import transformations as tr

X = tr.xor_func # операция XOR
S = tr.nonlinear_transformation # нелинейное преобразование в режиме простой замены
L = tr.linear_transformation # линейное преобразование
C = [] # константы
F = [] # ячейки Фейстеля

key = '7766554433221100FFEEDDCCBBAA9988EFCDAB89674523011032547698BADCFE'
# key = '448CC78CEF6A8D2243436915534831DB04FD9F0AC4ADEB1568ECCFE9D853453D'
K = [key[:int(len(key) / 2)], key[int(len(key) / 2) :]]

for i in range(32):
    if len(hex(i + 1)[2:]) == 1:
        C.append(L('0' + hex(i + 1)[2:] + '000000000000000000000000000000').upper())
    else:
        C.append(L(hex(i + 1)[2:] + '000000000000000000000000000000').upper())

# print(*C, sep = '\n')
# CC26ED7ED2BAD38DFA50CA91D584EFD5
# 89DCD46086505C68D6F3A68876D05E4A
# 2AA5144D724B85C2EA7953B5009FADE
# print(X(L(S(X('CC26ED7ED2BAD38DFA50CA91D584EFD5', '076A1A5670B5F550AEA53BC79D81E8C9'))),  '89DCD46086505C68D6F3A68876D05E4A'))

# print(X('8b7685245174e434f85433b326d9a494', '89DCD46086505C68D6F3A68876D05E4A'))

# CB4CF728A20F26DD54F5F1564805071C
# E4FDC081604DEFD808F4A676F26E1614
# 8b7685245174e434f85433b326d9a494
# 2AA5144D724B85C2EA7953B5009FADE
# 6f8b45a531390becf0a095c5d4b7b280 maybe

# print(hex(int('8b7685245174e434f85433b326d9a494', 16) ^ int('89DCD46086505C68D6F3A68876D05E4A', 16)))

# print(X('E4FDC081604DEFD808F4A676F26E1614', '8b7685245174e434f85433b326d9a494'))
# print(X(L(S(X('8b7685245174e434f85433b326d9a494', '082AAA2780A1FBAD895605E6163659F6'))),  '6f8b45a531390becf0a095c5d4b7b280'))

# print([K[0], K[1]])
# F1  = [ K[1], X(L(S(X( K[0], C[0]))),  K[1])]
# F2  = [F1[1], X(L(S(X(F1[0], C[1]))), F1[1])]
# F3  = [F2[1], X(L(S(X(F2[0], C[2]))), F2[1])]
# F4  = [F3[1], X(L(S(X(F3[0], C[3]))), F3[1])]
# F5  = [F4[1], X(L(S(X(F4[0], C[4]))), F4[1])]
# F6  = [F5[1], X(L(S(X(F5[0], C[5]))), F5[1])]
# F7  = [F6[1], X(L(S(X(F6[0], C[6]))), F6[1])]
# F8  = [F7[1], X(L(S(X(F7[0], C[7]))), F7[1])]
# F9  = [F8[1], X(L(S(X(F8[0], C[8]))), F8[1])]
# F10 = [F9[1], X(L(S(X(F9[0], C[9]))), F9[1])]
# F11 = [F10[1], X(L(S(X(F10[0], C[10]))), F10[1])]
# F12 = [F11[1], X(L(S(X(F11[0], C[11]))), F11[1])]
F.append([ K[1], X(L(S(X( K[0], C[0]))),  K[1])])
for i in range(32):
    K = [ F[i][1], X(L(S(X( F[i][0], C[i]))),  F[i][1])]
    F.append(K)

K = [key[:int(len(key) / 2)], key[int(len(key) / 2) :]]

for i in range(len(F)):
    if (i + 1) % 8 == 0:
        K.append(F[i][0])
        K.append(F[i][1])

for i in range(len(K)):
    print(i + 1, K[i])

# text = '8899AABBCCDDEEFF0077665544332211'
#
# for i in range(10):
#     text = L(S(X(text, K[i])))
#     print(text)



# print(L(S(X(text, K[0]))))
