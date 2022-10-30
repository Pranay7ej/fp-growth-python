# Frequent Pattern Growth Algorithm

I used a total of 13 datasets to validate the algorithm (from UC Irvine repository). 

Key observation: As the minimum support value increases the time taken by the algo decreases. It implies that, with a lower support the fp-algo must run the mining for the bigger conditional datasets.

Steps included in this algorithm:
 1) Construct FP tree
 2) Insert FP tree
 3) Mine FP tree recursively
 4) Conditional pattern base
 5) Creating frequent pattern item sets
 
Implementation:
 1) Data preprocessing
 2) Creating and updating FP tree
 3) Mining and creating conditional FP tree
