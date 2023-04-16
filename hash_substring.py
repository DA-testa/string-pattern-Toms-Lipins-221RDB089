# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    text = input()
    if 'F' in text:
        with open('/workspaces/string-pattern-Toms-Lipins-221RDB089/tests/06', 'r') as f:
            line = f.readline()
            line2=f.readline()
    elif 'I' in text:
       line = input()
       line2=input()
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (line.rstrip(), line2.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable

    M = len(pattern) 
    N = len(text)
    i = 0
    j = 0
    p = 0    
    t = 0    
    h = 1
 
    
    for i in xrange(M-1):
        h = (h * d)% q
 
   
    for i in xrange(M):
        p = (d * p + ord(pat[i]))% q
        t = (d * t + ord(txt[i]))% q
 
    
    for i in xrange(N-M + 1):
       
        if p == t:
           
            for j in xrange(M):
                if txt[i + j] != pat[j]:
                    break
 
            j+= 1
          
            if j == M:
                 str(i)
 
    
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q
 
            
            if t < 0:
                t = t + q


    return str(i)


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

