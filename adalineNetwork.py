N = int(raw_input('Enter number of cases: '))
alpha = float(raw_input('Enter learning rate(0 to 1.0): '))

Ninputs = int(raw_input('Enter number of inputs: '))
Ninputs += 1 #One extra for bias

weightsVal = float(raw_input('Enter an initial value for weights: '))

inputs = []
weights = []
outputs = []

weights = [ weightsVal for j in range(Ninputs) ]

threshold = float(raw_input('Enter minimum tolerance: '))

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

#Loop until maximum weight change is greater than threshold
while True:
    errors = []
    num+=1
    #maxWeightChange = 0.0
    #Begin an epoch
    for i in range(N):
        yin = sum( a*b for a,b in zip(inputs[i],weights)  )
        print "yin:",yin,", error:", (outputs[i]-yin)**2
        errors.append( (outputs[i]-yin)**2 ) #Append error to the list
        #Update weights
        for j in range(Ninputs):
            weightChange = alpha*(outputs[i]-yin)*inputs[i][j]
            #if weightChange > maxWeightChange:
                #maxWeightChange = weightChange
            weights[j] = weights[j] + weightChange
            print "weights:",weights
    sumOfE = sum(errors)
    print "After epoch: ",num,", weights:",weights,", error:", sumOfE
    #if maxWeightChange < threshold:
        #break
    if sumOfE < threshold or num>10:
        break

print 'Weights: ',weights
