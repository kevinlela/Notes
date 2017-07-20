# Decision Tree:
what is a good question to split a node? The one can split a nodes into a pure node. A pure node means a node containing all samples from the same class. How do we measure it?
Information gain: I(Y; X) = H(Y) - H(Y|X)
H is the entropy

Information gain:
1) we want to determine which attribute in a given set of training feature vectors is most useful for discriminating between classes to be learned
2) information gain tells us how important a given attribute of the feature vectors is
3) we will use it to decide the ordering of attributes in the nodes of a decision tree
information gain = entropy(parent) - [average entropy(children)]
a node with all samples in the same class -> lowest entropy
a node with all mixed samples (uniform distribution) -> highest entropy
For each node, choose an attribute which can generate largest information gain

Decision tree is very easy to be overfit
Strategy:
1) Prunning: greedily prune a tree iteratively

Say N samples and M features, for each node, randomly select m features, for each tree randomly select n samples.

Each tree is fully grown and not pruned. Each node is splitted by the feature with best gini index

Node gini index
Gini(T) = 1 - sum(p_j^2), the smaller the better, p_j stands for the portion of jth class in node T.
Split gini index
Gini_split(T) = (N_1/N)gini(T_1) + (N_2/N)gini(T_2), A size N node T is splited into class T1 with N1 samples and class T2 with N2 samples

