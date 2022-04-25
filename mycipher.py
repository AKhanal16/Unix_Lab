import sys

def give_outside(output):
    ans = ""
    line = ""
    ans_counter = 0
    for letter in output:
        ans += letter 
        if len(ans) == 5 and ans_counter < 9:
            ans += " "
            line += ans
            ans_counter += 1
            ans = ""
        elif len(ans) == 5 and ans_counter == 9:
            line += ans +"\n"
            ans_counter = 0
            ans = ""
    return(line + ans + "\n")

def encryption(message, shift):
    upper_case_message = message.upper()
    only_alphabets = ""
    for ele in upper_case_message:
      if ele.isalpha():
        only_alphabets += ele
    encoded_text = ""
    for element in only_alphabets:
      equivalent_ascii = ord(element)
      resulting_ascii = equivalent_ascii + shift
      if resulting_ascii > ord("Z"):
        resultant = (resulting_ascii - ord("Z")) % 26
        if resultant == 0:
          resultant = 26
        resulting_ascii = resultant + 64
      encoded_text += chr(resulting_ascii)
    
    result = give_outside(encoded_text)
    return result

for line in sys.stdin:
    output = encryption(line.strip(), int(sys.argv[1]))
    sys.stdout.write(output)
