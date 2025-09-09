
Spend 1-2 hours on one or two of the following exercices (a round up of those at the end of each notebook):

### Notebook 1 (1_differential_privacy_intro.ipynb)

* Experiment with parameters
* Modify the EPSILON, try 0.01, 0.1, 10.0, 100.0
* At what point does the noise become excessive?
* Create your own attack
* Add more quasi-indentifiers to the medical dataset
* Try to identify individuals with 2-3 attributes
* How unique are people in high-dimensional data?
* Question: If you were trying to break DP, where would you start?

### Notebook 2 (2_membership_inference_attacks)

* Attack Different Model Types

  
    Try membership inference on Logistic Regression, SVM, or Neural Networks
    Question: Which model types are most vulnerable?


* Vary Dataset Properties

    Create datasets with different sizes (100, 1000, 10000 samples)
    Test attack success vs dataset size
    Question: Are smaller datasets more vulnerable?


* Multi-class Membership Inference

    Extend the attack to datasets with more than 2 classes
    Does attack success change with number of classes?
    Question: How does class imbalance affect membership inference?


* Stretch exercise: Realistic Attack Scenario

    Assume you're an attacker with limited knowledge
    You don't know the exact training data distribution
    Can you still mount a successful membership inference attack?
    Hint: Try using publicly available similar datasets for shadow models


### Notebook 3 (3_federated_learning_attacks.ipynb)

* Experimenting with parameters:

    Increase reconstruction iterations (try 200+)
    Attack more patients simultaneously
    Try different hospitals as targets

* Attack enhancement:

    Can you infer which hospital has the oldest patients?
    Try to determine which hospital has the most severe cases
    Experiment with different gradient analysis techniques

### Discussion

   * Should hospitals be allowed to collaborate this way?
   * What are the trade-offs between medical progress and privacy?
   * How would you explain these risks to hospital administrators?