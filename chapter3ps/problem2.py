# Write a program to fill in a letter template given below with name and date.
# letter = '''
#     Dear <|Name|>,
#     You are selected!
#     <|Date|>
# '''
letter = '''Dear <|Name>,
you are selected ! 
<|Data|>'''
print(letter.replace("<|Name|>","Harry").replace("<|Date|","24 SEP 2050"))#HERE CHAINING IS USED