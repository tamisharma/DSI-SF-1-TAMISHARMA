---
title: Evaluating Model Fit
duration: "1:25"
creator:
    name: John Doe
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Evaluating Model Fit
Week 4 Lesson 2.3

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Understand the fundamentals of evaluating classifiers
- Understand precision, recall, accuracy, f1-score, and ROC curves
- Know how to use sklearn.metrics functions to easily compute these metrics


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*


### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Gather materials needed for class
- Complete Prep work required
- Prepare any specific instructions

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | How to use scikit-learn to run logistic  |
| 5 min  | [Introduction](#introduction)   | Topic description  |
| 30 min  | [Guided Practice](#guided-practice<a name="opening"></a>)  | Exploring classifier evaluation metrics  |
| 15 min  | [Demo](#demo)  | AUC and ROC curves |
| 25 min  | [Independent Practice](#ind-practice)  | Practice AUC and ROC curves |
| 5 min  | [Conclusion](#conclusion)  | Topic description  |

---

<a name="opening"></a>
## Opening: Run logistic regression with sklearn (5 mins)

Like statsmodels, sklearn also has a function to run logistic regression. The implementation is different than statsmodels but is easy use.

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# Set up fake X and Y
X = np.random.randn(100, 3)
Y = np.random.binomial(1, 0.5, 100)

logreg = LogisticRegression()
logreg.fit(X, Y)

# coefficients:
logreg.coef_

X_new = np.random.randn(100, 3)

# predict class:
y_pred = logreg.predict(X_new)

# predicted probability:
y_pp = logreg.predict_proba(X_new)
```

The sklearn implementation of logistic regression is focused more on flexibility
than the statsmodels implementation, but does not return as many summary
statistics. We will be using the sklearn implementation for this lesson.

<a name="introduction"></a>
## Introduction: Topic (5 mins)

Classification problems and models are evaluated differently than regression models. Whereas regression models predict a continuous variable, classification problems predict probability of belonging to a class of outcome.

Instead of evaluating models based on error like in regression, we evaluate the models based on the correct and incorrect labeling of classes.

Most classification metrics are based on four outcome categories during prediction:

- **True Positives:** A positive class observation (1) is correctly classified as positive by the model.
- **False Positive:** A negative class observation (0) is incorrectly classified as positive.
- **True Negative:** A negative class observation is correctly classified as negative.
- **False Negative:** A positive class observation is incorrectly classified as negative.

Fair warning – this is going to be a difficult lecture. There are a lot of concepts covered!


## Exploring classifier evaluation metrics (25 min)

For this section, let's say we have predicted Y for a test set from a logistic regression trained on a train set, as outlined in the code below.

You can follow along in the ipython notebook file:

[Evaluation metrics guided practice] (assets/code/lessons/week04-lesson4.1-guided-practice.ipynb)

Keep in mind your numbers will be different than the results in this presentation since the data is randomly generated.

```python
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)

logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
Y_pred = logreg.predict(X_test)
```

### Classification evaluation metric fundamentals

##### Confusion matrix

  The confusion matrix is very basic, and while may not seem that useful contains all of the information required for calculating more complex evaluation metrics.

  A confusion matrix has as rows and columns the classes modeled by your classifier. In the case of logistic regression this will be a 2x2 matrix. Rows indicate the actual class, and columns indicate the predicted class.

|                | Predicted Cancer | Predicted Healthy |
| --------------:|:----------------:|:-----------------:|
| **Has Cancer** | 168              | 31                |
| **Is Healthy** | 46               | 85                |

  In the medical example above, 168 of the people who actually have cancer were correctly identified as having cancer and 85 healthy people were correctly identified as being healthy. However, 46 people who were actually healthy were incorrectly identified as having cancer, and 31 people who had cancer were incorrectly identified as being healthy.

  From the 2-variable confusion matrix we can calculate **true positives**, **false positives**, **true negatives**, and **false negatives** directly from the cells. Tuning your model to adjust these metrics depends on your priorities. In healthcare for example, you may want to minimize false negatives at the expense of more false positives.

  ```python
  from sklearn.metrics import confusion_matrix

  confusion = np.array(confusion_matrix(Y_test, Y_pred))

  print(confusion)
  [[168  31]
  [ 46  85]]

  # calculate true positives, the number of 1s correctly predicted to be 1
  TP = confusion[0,0]

  # calculate false positives, the number of 0s incorrectly predicted to be 1
  FP  = confusion[1,0]

  # calculate true negatives, the number of 0s correctly predicted to be 0
  TN = confusion[1,1]

  # calculate false negatives, the number of 1s incorrectly predicted to be 0
  FN = confusion[0,1]
  ```

##### Accuracy

  Accuracy is simply the proportion of classes correctly predicted by the model.

  ```
  Accuracy = (True Positives + True Negatives) / Total
  ```

  ```python
  from sklearn.metrics import accuracy_score

  acc = accuracy_score(Y_test, Y_pred)

  # This is equivalent to:
  acc = np.sum(Y_test == Y_pred)/len(Y_test)
  ```

##### sklearn classification report

  The classification report function returns a detailed printout of metrics about your model.

  ```python
  from sklearn.metrics import classification_report

  # Example printout:
  print(classification_report(Y_test, Y_pred))

                   precision recall    f1-score   support

  0                 0.79      0.84      0.81       199
  1                 0.73      0.65      0.69       131

  avg / total       0.76      0.77      0.76       330
  ```

  The 0 and 1 on the left column indicate the two classes predicted by the model. For models with multiple classes there would be more rows and labels.

  Each of the columns indicate an important metric for evaluating classification model performance.

  **precision** is the ability of the classifier to avoid labeling a class as a member of another class.

  ```
  Precision = True Positives / (True Positives + False Positives)
  ```

  A precision score of 1 indicates that the classifier never mistakenly classified the current class as another class. A precision score of 0 would mean that the classifier misclassified every instance of the current class.

  **recall** is the ability of the classifier to correctly identify the current class.

  ```
  Recall = True Positives / (True Positives + False Negatives)
  ```

  A recall score of 1 indicates that the classifier correctly predicted all observations of the current class (with no false negatives, aka misclassifications of the current class). A recall score of 0 alternatively means that the classifier predicted all observations of the current class incorrectly as another class.

  **f1-score** is the harmonic mean of the precision and recall. The harmonic mean is used here rather than the more conventional arithmetic mean because the harmonic mean is more appropriate for averaging rates.

  ```
  F1-Score = 2 * (Precision * Recall) / (Precision + Recall)
  ```

  The f1-score's best value is 1 and worst value is 0, like the precision and recall scores. It is a useful metric for taking into account both measures at once.

  **support** is simply the number of observations of the labelled class.


<a name="demo"></a>
## Demo / Codealong: AUC and ROC curves (15 mins)

Open the jupyter notebook for the codealong to learn about area under the curve (AUC) and the receiver operating characteristic curve (ROC).


[AUC ROC codealong] (assets/code/lessons/AUC-ROC-codealong.ipynb)


**Check for understanding:***
- What are some reasons that you might change the class assignment threshold in a classifier?
- How does changing the threshold for assigning a class label affect the confusion matrix?
- How is the ROC related to the confusion matrix?
- Why is the ROC curve unaffected by the distribution of classes in the data?


<a name="ind-practice"></a>
## Independent Practice: metrics and ROC with housing data (25 minutes)

Practice classification evaluation metrics and plotting ROC curves with the Sacramento housing data. Load the starter code below to begin.

[AUC housing starter code] (assets/data/starter-code/AUC-sacramento-housing-starter-code.ipynb)

<a name="conclusion"></a>
## Conclusion (5 mins)
- Review independent practice deliverable(s)
- Recap topic(s) covered

***


### ADDITIONAL RESOURCES
