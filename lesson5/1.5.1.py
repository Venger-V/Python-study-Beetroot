text = input('Enter a text:')
if len(text) < 2:
    print('')
else:
    text_output = str(text[:2]) + str(text[-2:])
    print(text_output)
    
