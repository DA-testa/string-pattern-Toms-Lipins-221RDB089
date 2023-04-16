# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    text = input()
    if 'F' in text:
        with open('tests/06', 'r') as f:
            pattern = f.readline()
            text=f.readline()
    elif 'I' in text:
       pattern = input()
       text=input()
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable

    P = len(pattern) 
    T = len(text)
    i = 0
    j = 0
    p = 0 
    t = 0  
    h = 1
    q=67
    d=256
    result=""
    
    for i in range(P-1):
        h = (h * d)% q
 
   
    for i in range(P):
        p = (d * p + ord(pattern[i]))% q
        t = (d * t + ord(text[i]))% q
 
    
    for i in range(T-P + 1):
       
        if p == t:
           
            for j in range(P):
                if text[i + j] != pattern[j]:
                    break
 
            j+= 1
          
            if j == P:
                result= result + str(i) + " "
                
 
    
        if i < T-P:
            t = (d*(t-ord(text[i])*h) + ord(text[i + P]))% q
 
            
            if t < 0:
                t = t + q

    return [result]

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

