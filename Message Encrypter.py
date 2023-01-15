from time import sleep
import os

#the code for the messages, using caeser cipher, numbers and punctuations
Mapping = {
'A':'N',
'B':'O',
'C':'P',
'D':'Q',
'E':'R',
'F':'S',
'G':'T',
'H':'U',
'I':'V',
'J':'W',
'K':'X',
'L':'Y',
'M':'Z',
'N':'A',
'O':'B',
'P':'C',
'Q':'D',
'R':'E',
'S':'F',
'T':'G',
'U':'H',
'V':'I',
'W':'J',
'X':'K',
'Y':'L',
'Z':'M',
' ':'#',
'#':' ',
'.':'+',
'+':'.',
',':'-',
'-':',',
'*':'=',
'+':'*',
'?':'|',
'|':'?',
'(':'[',
'[':'(',
')':']',
']':')',
'0':'9',
'1':'8',
'2':'7',
'3':'6',
'4':'5',
'5':'4',
'6':'3',
'7':'2',
'8':'1',
'9':'0',
':':';',
';':':',
'/':'>',
'>':'/',
'a':'n',
'b':'o',
'c':'p',
'd':'q',
'e':'r',
'f':'s',
'g':'t',
'h':'u',
'i':'v',
'j':'w',
'k':'x',
'l':'y',
'm':'z',
'n':'a',
'o':'b',
'p':'c',
'q':'d',
'r':'e',
's':'f',
't':'g',
'u':'h',
'v':'i',
'w':'j',
'x':'k',
'y':'l',
'z':'m',
}

#the function that encrypts the message
def cipher(original):
  text = ""
  for letter in original:
    if letter.upper() == True:
      letter = letter.lower()
    elif letter.upper()==False:
      letter = letter.upper()
    newletter = Mapping[letter]
    text = text + newletter
  return text

#the function that checks for unsupported characters in the inputed message
def check(original):
  for letter in original:
    if letter not in Mapping:
      print(f'This character {letter} is not supported.')
      return True
  return False

#the function that runs the previous two functions and return the result
def run_program():
  text = input('\nSecret Text Program.\n\nEnter the encrypted text: ')
  if check(text):
    return
  result = cipher(text)
  print(result)

#an infinite loop that asks the user if they want to repeat the process
while True:
  run_program()
  sleep(2)
  print('\n\n\nWant to try again?')
  rerun = input("Type 'y' for yes, 'n' for no: ")
  if rerun != 'y':
    sleep(2)
    break
  else:
    os.system('cls')

#uses the 'time' and 'os' libraries