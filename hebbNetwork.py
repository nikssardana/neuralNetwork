N = int(raw_input('Enter number of cases: '))

Ninputs = int(raw_input('Enter number of inputs: '))
Ninputs += 1 #For bias

inputs = []
weights = []
outputs = []

print 'Enter inputs and outputs:'
print 'Ex: 1 -1 1 means 1 and -1 are inputs and 1 is the output of that case'

for i in range(N):
    inputStr = raw_input()
    inp = inputStr.split(' ')[:-1]
    inp = [ int(x) for x in inp ]
    inp.append(1) #1 is for bias, xb
    outp = inputStr.split(' ')[-1]
    outp = int(outp)
    inputs.append(inp)
    outputs.append(outp)

weights = [ 0 for j in range(Ninputs) ]
for j in range(N):
    for i in range(Ninputs):
        weights[i] = weights[i] + outputs[j]*inputs[j][i]

print "Weights",weights

#initialising sum and bestSum
bestSum = 0
summation = sum( a*b for a,b in zip(inputs[0],weights)  )
print summation

for j in range(N):
    if outputs[j] == -1:
        summation = sum( a*b for a,b in zip(inputs[i],weights) )
        print summation
        if summation > bestSum:
            bestSum = summation
T = bestSum + 1
print "Threshold: ",T

'''
Hebb Network Algorithm

Inputs = -1 or 1
Weights = -1 or 1

Output = 1 if Summation(Ii * Wi >= T)
           = 0 if Summation < 0

Algo:
	Initialise Wi = 0 for all i
	For each input vector j and output value y:
		For each weight Wi:
			Wi(new) = Wi + Xi*Wi for all i
	Yin = maxNegY = X0*W0
	Find out the max value of Yin for which the output should be -1. Threshold T is this value.

	For each output Yj:
		summation = 0
		if Yj == -1:
			For each weight Wi in jth row:
				summation += Wi * Xi
			if summation > bestSum:
				bestSum = summation
	T = bestSum
Answer = All weights and T
'''
