# Dosage-Tester
This is about a neural network utilized to test dosages of a medicine. 
It's a demo based on a YouTube video, "Neural Networks Pt. 1: Inside the Black Box" by StatQuest with Josh Starmer.
The author does a great job explaining math details of a simple forward propagation using softplus activation. 

## Background 
Apparently in a previous operation, a training dataset with labels has been utilized to obtain parameters that classify dosages of a medication.    
The premise is that low and high dosages result in efficacy of 0, and medium dosages result in efficacy of 1 (highest:good).

## How it works 
I think in most NNs, the testing phase does not utilize the steps of propagation. 
But to explain the math of forward propagation, the video makes one pass to produce a result.   
In my demo, I have dosages of (0.1, 0.3, 0.5, 0.7, and 0.9).
The network has two nodes in one middle layer. 
The video shows two blue curved lines for the top node, and two orange curved lines for the bottom node. 
I call these g1 and g2. The activation function produces g2 values. 
The two g2 values are summed to g3 values, the green curve line.
A final negative bias is added to produce the final efficacy value.

## Plots
A Matplotlib plot is generated with six plots:
<br>top g1 and g2 (blue)
<br>bottom g1 and g2 (orange)
<br>sum g3 (green)
<br>efficacy (red)

## My problem
The green and red lines are supposed to be squiggly lines, centered on y values of 0 and 1.
The medium dosage value (0.5) is the only one that works as planned, with efficacy of 1.
My code does not produce squiggly lines as shown in the video, to show both the low and high dosage values close to zero. 
Perhaps you can show my error.
