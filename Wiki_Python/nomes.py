# i = 57
#
# j = i
#
#
# if i == j:
#     print('Valores iguais')
#
# if i is j:
#     print('Mesmo objeto')
#
# if type(i) == type(j):
#     print('mesmo tipo')
#
# f = None
# if f is None:
#     print('é nulo')

def um():
    x = 1
    print(x)
    dois(x)
    print(x)

def dois(y):
    print(y)
    y = 2
    print(y)

um()
print()
dois(3)