'''
Using strip(), replace()
'''

text = "         Hello        "
print text

text_after_strip = text.strip()
print text_after_strip

text_after_replace = text.replace('l','W')
print text_after_replace

text_after_strip_replace = text_after_strip.replace('l','W')
print text_after_strip_replace