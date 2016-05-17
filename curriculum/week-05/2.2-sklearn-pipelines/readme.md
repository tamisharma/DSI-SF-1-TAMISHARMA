---
title: Pipelines and Custom Transformers in SKLearn
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Pipelines and custom transfomers in SKLearn
Week 5 | Lesson 2.2

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Create pipelines for cleaning and manipulating data
- Use pipelines to preprocess data from the SQL database
- Use pipeline in combination with classification
- Create a custom transformer using the `TransformerMixin` class

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Extract data from a database
- Perform classification

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### LESSON GUIDE

| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 mins | [Opening](#opening) | Opening |
| 10 mins | [Introduction](#introduction) | Data Pipelines |
| 25 mins | [Demo](#demo) | Pipelines in scikit-learn |
| 15 mins | [Guided-practice](#guided-practice) | Make Pipeline and the preprocessing module |
| 10 minutes | [Demo](#demo_2) | Custom Transformers |
| 20 minutes | [Ind-practice](#ind-practice) | Putting it all together |
| 5 mins | [Conclusion](#conclusion) | Conclusion |


<a name="opening"></a>
## Opening (5 mins)
**Data pipelines** are a series of automated data transformations that ensure the validity of your work for routine data maintenance tasks. Many organizations rely on data engineering teams to encode common tasks into pipelines.

<a name="introduction"></a>
## Data Pipelines (10 mins)

The term _pipeline_ is used to indicate a series of concatenated data transformations. Each stage of a pipeline feeds from the previous stage, i.e. the output of a stage is plugged into the input of the next stage and data flows through the pipeline from beginning to end just as water flows through a pipeline.

![Pipeline](./assets/images/pipeline.png)

Each processing stage has an input, where data comes in, and an output, where processed data comes out.

**Check:** Ask the students to give some examples of data transformations.

> Examples of data transformations:
> - change in units (lbs -> kg)
> - change of scale
> - change of base
> - text vectorization
> - image vectorization
> - sound file vectorization
> - missing data imputation
> - clipping

Pipelines provide a higher level of abstraction than the individual building blocks of a data science process and are a great way to organize analyses.

<a name="demo"></a>
## Pipelines in scikit-learn (25 mins)
Pipelines improve coding and model management in `scikit-learn`. These tie together all the steps that you may need to prepare your dataset and make your predictions. Because you will need to perform all of the exact same transformations on your evaluation data, encoding the exact steps is important for reproducibility and consistency.


```python
from sklearn.pipeline import Pipeline
```

To show how a pipeline works, we'll use an example involving Natural Language Processing. Data comes from the [Evergreen Stumbleupon Kaggle Competition](https://www.kaggle.com/c/stumbleupon/data), where participants where challenged to build a classifier to categorize webpages as evergreen or non-evergreen. Binary evergreen labels (either evergreen (1) or non-evergreen (0)) were provided. We'll focus on the page title text.


```python
import pandas as pd
import json

data = pd.read_csv("assets/datasets/stumbleupon.tsv", sep='\t')
data['title'] = data.boilerplate.map(lambda x: json.loads(x).get('title', ''))
data['body'] = data.boilerplate.map(lambda x: json.loads(x).get('body', ''))

titles = data['title'].fillna('')
titles[0:3]
```




    0    IBM Sees Holographic Calls Air Breathing Batte...
    1    The Fully Electronic Futuristic Starting Gun T...
    2    Fruits that Fight the Flu fruits that fight th...
    Name: title, dtype: object




```python
y = data['label']
y[0:3]
```




    0    0
    1    1
    2    1
    Name: label, dtype: int64




```python
y.value_counts() / len(y)
```




    1    0.51332
    0    0.48668
    Name: label, dtype: float64



Each datapoint is a string of free form text. How can we feed this to a model? The simplest way is to build a dictionary of words and use those as features. This is what a `CountVectorizer` does.

Example:


|Sentence|the|cat|is|on|table|blue|
|---|---|---|---|---|---|---|
|The cat is on the table|2|1|1|1|1|0|
|The table is blue|1|0|1|0|1|1|
|...||||||


```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features = 1000,
                             ngram_range=(1, 2),
                             stop_words='english',
                             binary=True)

vectorizer.fit(['IBM Sees Holographic Calls Air Breathing'])
```




    CountVectorizer(analyzer=u'word', binary=True, decode_error=u'strict',
            dtype=<type 'numpy.int64'>, encoding=u'utf-8', input=u'content',
            lowercase=True, max_df=1.0, max_features=1000, min_df=1,
            ngram_range=(1, 2), preprocessor=None, stop_words='english',
            strip_accents=None, token_pattern=u'(?u)\\b\\w\\w+\\b',
            tokenizer=None, vocabulary=None)




```python
vectorizer.get_feature_names()
```




    [u'air',
     u'air breathing',
     u'breathing',
     u'calls',
     u'calls air',
     u'holographic',
     u'holographic calls',
     u'ibm',
     u'ibm sees',
     u'sees',
     u'sees holographic']




```python
vectorizer.transform(['IBM Sees Holographic Air']).todense()
```




    matrix([[1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]])



**Check**: What is the meaning of the various parameters used at initialization of the Vectorizer?


Let's use the vectorizer to fit all the titles and build a feature matrix.


```python
# Use `fit` to learn the vocabulary of the titles
vectorizer.fit(titles)

# Use `transform` to generate the sample X word matrix - one column per feature (word or n-grams)
X = vectorizer.transform(titles)
```

We use `X`, a matrix of all common n-grams in the dataset, as an input to our classifier. We want to classify how evergreen a story is based on these inputs.



```python
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score

model = LogisticRegression()
scores = cross_val_score(model, X, y)

print('CV scores: {}'.format(scores))

print('Average CVScore: {:0.3f} +/- {:0.3f}'.format(scores.mean(), scores.std()))
```

    CV scores: [ 0.74574209  0.75659229  0.75487013]
    Average CVScore: 0.752 +/- 0.005


#### Combining Steps in Pipelines

Often we will want to combine these steps to evaluate some future dataset. Therefore, we need to make sure we perform the _exact same_ transformations on the data. If "has_brownies_in_text" is column 19, we need to make sure it is _also_ column 19 during future evaluation.

Pipelines combines both pre-processing and model building steps into a _single object_. Rather than manually evaluating the transformers and then feeding them into the models, pipelines ties both of these steps together.

Similar to models and vectorizers in scikit-learn, pipelines are equipped with `fit` and `predict` or `predict_proba` methods (as any model would be), and they ensure that proper data transformations are performed.


```python
# Split the data into a training set
training_data = data[:6000]
X_train = training_data['title'].fillna('')
y_train = training_data['label']

# These rows are rows obtained in the future, unavailable at training time
X_new = data[6000:]['title'].fillna('')

from sklearn.pipeline import Pipeline

pipeline = Pipeline([
        ('vec', vectorizer),
        ('model', model)   
    ])

# Fit the full pipeline
# This means we perform the steps laid out above
# First we fit the vectorizer,
# And then feed the output of that into the fit function of the model

pipeline.fit(X_train, y_train)

# Here again we apply the full pipeline for predictions
# The text is transformed automatically to match the features from the pipeline
pipeline.predict_proba(X_new)
```




    array([[ 0.46800424,  0.53199576],
           [ 0.28316267,  0.71683733],
           [ 0.00514   ,  0.99486   ],
           ..., 
           [ 0.29063018,  0.70936982],
           [ 0.60683954,  0.39316046],
           [ 0.66318704,  0.33681296]])



**Check**: Add a `MaxAbsScaler` scaling step to the pipeline, which should occur after the vectorization.

#### Merging Feature Sets in Pipelines

Additionally, we often want to merge many different feature sets automatically. Here we can use scikit-learn's `FeatureUnion`.

While scikit-learn pipelines help with managing the transformation from raw data, there may be many steps before this takes place in your pipeline. These pipelines are often referred to as *ETL* pipelines for (Extract, Transform, Load).

In an ETL pipeline, the data is pulled or extracted from some source (like a database), transformed or manipulated, and then loaded into whatever system will analyze the data.

Many data science teams rely on software tools to manage these ETL pipelines. If a transformation step fails, these tools alert you, or ensure that step can be re-run. If these transformation steps need to happen daily or weekly, these tools can manage that timeline.

- One of the most popular Python tools for this is [Luigi](https://github.com/spotify/luigi) developed by Spotify.
- An alternative is [Airflow](https://github.com/airbnb/airflow) by AirBnB.

<a name="guided-practice"></a>
## `make_pipeline` and the preprocessing module (15 mins)

#### make_pipeline
Scikit-learn pipelines can also be built using the `make_pipeline` command.


```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe1 = make_pipeline(StandardScaler(), LogisticRegression())    

pipe2 = Pipeline(steps=[('standardscaler',StandardScaler()),
                        ('logistic_regr',LogisticRegression())
                       ])
```


```python
pipe1
```




    Pipeline(steps=[('standardscaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('logisticregression', LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
              intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
              penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
              verbose=0, warm_start=False))])




```python
pipe2
```




    Pipeline(steps=[('standardscaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('logistic_regr', LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
              intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
              penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
              verbose=0, warm_start=False))])



The two pipelines created above are identical.

### Preprocessing in sklearn (in pairs)

The preprocessing module comes loaded with many very useful pre-processing classes.

**Check**: In pairs, assign one function to each pair, they have to read about it in the doc and then explain it to the class.


Data Manipulators
- Binarizer
- KernelCenterer
- MaxAbsScaler
- MinMaxScaler
- Normalizer
- OneHotEncoder
- PolynomialFeatures
- RobustScaler
- StandardScaler

Data Imputation
- Imputer

Function Transformer
- FunctionTransformer

Label Manipulators
- LabelBinarizer
- LabelEncoder
- MultiLabelBinarizer

<a name="demo_2"></a>
## Custom Transformers (10 minutes)

We can implement custom transformers by extending the BaseClass in Scikit-Learn.


```python
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class FeatureMultiplier(BaseEstimator, TransformerMixin):
    def __init__(self, factor):
        self.factor = factor
        
    def transform(self, X, *_):
        return X * self.factor
    
    def fit(self, *_):
        return self

fm = FeatureMultiplier(2)

test = np.diag((1,2,3,4))
print test

fm.transform(test)
```

    [[1 0 0 0]
     [0 2 0 0]
     [0 0 3 0]
     [0 0 0 4]]





    array([[2, 0, 0, 0],
           [0, 4, 0, 0],
           [0, 0, 6, 0],
           [0, 0, 0, 8]])



**Check**: Compare this with the `FunctionTransformer` from the preprocessing module.

**Check**: Implement a custom transformer that selects a specific feature from a Pandas dataframe. It should be initialized with the column name or the column index and it should return the selected column when transforming a dataframe.

<a name="ind-practice"></a>
## Putting it all together (20 minutes)

**Check**: Revisit the dataset of lab 1.4. How could you use `make_pipeline` and `make_union` to build a pipeline that performs the same steps all in one pass?

> Answer: you will have to build something like this:
>
    Data --> SelectCategoricalFeaturesTransformer --> OneHotEncoder --> FeatureUnion --> Model
          \-> SelectNumericalFeaturesTransformer ------> Scaler ----/
A good practice for instructor is to have students work in this way:
1. review lab 1.4 and identify the steps that were performed
- for each of this steps figure out what the input and what the output is
    - is the input the whole dataframe or only a subset of the features?
    - is the output new features or a prediction?
- for each of this steps identify what kind of transformer is needed:
    - is it a custom transformer?
    - does scikit-learn provide a transformer like this out of the box?
- if different features are treated differently, have students figure out how to recombine them (Feature Union)

<a name="conclusion"></a>
## Conclusion (5 mins)
We learned how to use the `Pipeline` construct in order to chain several instructions in one single object. This enables to treat data-processing from a more abstract and more powerful perspective, and it's a pre-cursor to the work we will do when working with Big Data technologies.

***
### ADDITIONAL RESOURCES

- [Pipelines and Feature Union](http://scikit-learn.org/stable/modules/pipeline.html)
- [Example with complex pipeline](http://scikit-learn.org/stable/auto_examples/hetero_feature_union.html#example-hetero-feature-union-py)
