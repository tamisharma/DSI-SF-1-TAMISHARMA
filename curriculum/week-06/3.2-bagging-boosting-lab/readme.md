---
title: Random Forest and Boosting Lab
type: lab
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Random Forest and Boosting Lab

## Introduction

In this lab we will practice using Random Forest Regressors and Boosted Trees Regressors on the SF restaurant health code violations data. You can find it as usual in the ```./assets/datasets``` folder.

We will be training several classification and regression models. For classification, you can choose to predict:

- Neighborhood
- Health code violation category
- Zip code

For the regression problem, you will predict either:

- Health code score

OR (BONUS), aggregate total number of violations by (using groupby):

- Neighborhood *adjusted for number of businesses and population in area*.

## Exercise

The [Starter Code](./code/starter-code/starter-code-3_2.ipynb) will guide you through the following points.

### Requirements

1. Load and inspect the data.
- Train and evaluate performance of a Decision Tree Regressor
- Train and evaluate performance of a Random Forest Regressor
- Train and evaluate performance of a AdaBoost Regressor
- Train and evaluate performance of a Gradient Boosting Trees Regressor

**Bonus:**

- Use Grid Search to improve your results
- Use total violations by neighborhood as regression dependent variable.

### Code

[Starter Code](./code/starter-code/starter-code-3_2.ipynb)

## Additional Resources

- [AdaBoost Regressor](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)
- [Example on Adaboost regression](http://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html)
- [Gradient Boosting Regression](http://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)
- [Random Forest Regression](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
