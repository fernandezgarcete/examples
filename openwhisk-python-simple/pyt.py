is_old = True
is_licensed = True
is_young = False


if is_old:
    print('You can drive!')
else:
    print('You can still enjoying your life')


if is_old:
    print('You already growth')
elif is_young:
    print('Hello young!')
else:
    print('Hey kiddo!')


if is_old and is_licensed:
    print('You can drive legally')
elif is_young or not is_licensed:
    print('Sorry but you cannot drive')
else:
    print('Someone wants to drive?')