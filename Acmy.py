# Validation
# Computer checks if input is reasonable (E.G user is asked to input age and enters 10, so it is reasonable)
# Possible validation methods
# Presence check - is there an answer?
# Range check - are values between lower and upper bounds?
# Type check - is the data of the correct type?
# Lookup check - also now as a drop-down box
# Python cant do a graphical interface but the point of drop box is to give a set number of options to the user
# Length check - the entry has to bbe a set number of chars long
# Format check - the input matches a pre determined order
# Verification
# Where the value input is correct
# e.g "do you want to delete this file?"
classes = [['a', 'b', 'c'], ['e', 'f', 'g'], ['h', 'i', 'j']]
#Psuedocode
# DECLARE classID, student AS INT
# DECLARE classes : ARRAY [1:3,1:3] OF CHAR
# classes <= [['a', 'b', 'c'], ['e', 'f', 'g'], ['h', 'i', 'j']]
# length
# myStr <= 'Hello communism'
# l = LENGTH(myStr) // 15
a = int(input('1 or 0'))
b = int(input('1 or 0'))
if (a + b) > 1 or (a + b) == 0:
    print(0)
else:
    print(1)