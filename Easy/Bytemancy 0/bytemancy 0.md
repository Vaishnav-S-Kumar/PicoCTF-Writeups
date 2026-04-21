# Bytemancy 0

## Description

Can you conjure the right bytes? The program's source code can be downloaded.

## Solution

Download the source code and analyse how the program works.
``` 
while(True):
  try:
    print('⊹──────[ BYTEMANCY-0 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    user_input = input('==> ')
    if user_input == "\x65\x65\x65":
      print(open("./flag.txt", "r").read())
      break
    else:
      print("That wasn't it. I got: " + str(user_input))
      print()
      print()
      print()
  except Exception as e:
    print(e)
    break
``` 
After Analysis, it is clear that a certain character should typed a certain number of times without spaces. Find the ASCII value of the decimal. 

Launch the instance and type the ASCII value as described in the program.

