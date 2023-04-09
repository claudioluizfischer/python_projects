'''
Name: Claudio Fischer
Unumber: 92525778
Description: The program uses a dictionary to encrypt a text file. The program
reads an input file where it encodes the text using the dictionary previously
created, then writes the result to a output text file.
'''

code_encrypt = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
'@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
'%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
'*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
"'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
'{':'[','[':'{','}':']',']':'}'
  }

# read input file
with open("input.txt", "r") as input_file:
    input_text = input_file.read()

#function to encruypt the file where accpets the contents of the file (as a string) and return the encrypted content.
def encrypt_text(text):
  encrypted_text = ""
  for char in text:
      if char in code_encrypt:
          encrypted_text += code_encrypt[char]
      else:
          encrypted_text += char
  return encrypted_text

# encrypt the text
encrypted_text = encrypt_text(input_text)

# write encrypted text to output file
with open("output.txt", "w") as output_file:
    output_file.write(encrypted_text)