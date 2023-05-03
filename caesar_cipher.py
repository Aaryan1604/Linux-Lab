import sys

def encryption(text,shift):
    #shifting characters
    filter = []
    for  char in text:
        if  char.isalpha():
            if ord(char.upper())+shift <= ord("Z"):
                filter.append(chr(ord(char.upper())+shift))
            else:
                filter.append(chr(ord(char.upper()) + shift - 26))
    #placing it in block of 5
    five_block=[]
    count = 0
    block = ""
    for char in filter:
        block+=char
        count+=1
        if count == 5:
            five_block.append(block)
            count=0
            block=""
    if block:
        five_block.append(block)

    #keepting 10 blocks in each line
    output = ""
    count =0 
    for char in five_block:
        if count == 10:
            output+="\n"
            count=0
        output+=char+" "
        count+=1
    
    print(output.strip())
        

text = sys.argv[1]
shift = int(sys.argv[2])
encryption(text,shift)








    

        

