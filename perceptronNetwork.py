N = int(raw_input('Enter number of cases: '))
alpha = float(raw_input('Enter learning rate(0 to 1.0): '))

Ninputs = int(raw_input('Enter number of inputs: '))
Ninputs += 1 #For bias

inputs = []
weights = []
outputs = []

weights = [ 0 for j in range(Ninputs) ]

threshold = float(raw_input('Enter threshold: '))

print 'Enter inputs and outputs:'
print 'Ex: 1 -1 1 means 1 and -1 are inputs and 1 is the output of that case'

for i in range(N):
    inputStr = raw_input()
    inp = inputStr.split(' ')[:-1] #First (N-1) values are inputs
    inp = [ int(x) for x in inp ] #Convert input values to integers
    inp.append(1) #1 is for bias, xb
    outp = int(inputStr.split(' ')[-1]) #Last (Nth value) for each line is output
    inputs.append(inp)
    outputs.append(outp)

num = 0

#Loop until all target values are not equal to the actual output in an epoch
while True:
    num+=1
    completed = True
    #Begin an epoch
    for i in range(N):
        yin = sum( a*b for a,b in zip(inputs[i],weights)  )
        if yin < -threshold:
            y = -1
        elif -threshold <= yin <= threshold:
            y = 0
        else:
            y = +1

        if y != outputs[i]:
            completed = False
            #Adjust weights
            for j in range(Ninputs):
                weights[j] = weights[j] + alpha*outputs[i]*inputs[i][j]
    print "After epoch: ",num,", weights:",weights
    if completed:
        break

print 'Weights: ',weights
