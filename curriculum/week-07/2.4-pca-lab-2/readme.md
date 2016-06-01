---
title: PCA Lab - Put It All Together
type: lab
duration: "1:25"
creator:
    name: Patrick Smith
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) PCA Lab: Put It All Together

## Introduction

> ***Note:*** _This should be done in pairs or small groups.

You've conducted principal component analysis on numerous datasets by this point and you're well on your way to adding more complex methods to your toolbox. We're going to look back at the airport delays data from the last lab and dive a little deeper - conducting a k-means clustering, after finding the principal components of the data.

Here's the case: 

You're working for the FAA and want to understand the nature of flight delays. Looking at the [operations data](./assets/datasets/airport_operations.csv) for various airports, you want to understand what components are most important for each airport so that the FAA can target and assess poor performing airports. Your task is to first conduct a PCA on this data and second perform a k-means clustering analysis to understand the principal components - the clusters - and how they interact!

## Exercise

#### Requirements

- Import the data
- Perform a Principal Component Analysis to determine which components are most significant in relation to flight delays.
- Graph your PCA results to better understand the distribution of the principal components
- Perform k-means clustering on and graph it against the principal components
- Create a write-up of your findings; for the technical team members make sure to comment your process, and for the non-technical team members, draft a brief report to outline why your findings are significant.

Just as in a real life scenario, the data and your analysis will not always be clear cut. While you may be wondering when you've succeeded in solving the problem, we're looking for your best recommendations based on the available data. Work through the process until you and your teammate have enough information to provide an in-depth analysis.

**Bonus:**
- Repeat your analysis on subsets of the data to understand deeper insights into the behavior of flight delays. For instance, instead of looking at all of the data, subset your analysis to look at just delay or arrival metrics. 

#### Starter Code & Data

- Download the [airline data](./assets/datasets/airport_operations.csv).
- Grab the [starter code](./code/starter-code/starter_code.ipynb) to get started. 

> [Solution code here](./code/solution-code/solution_code.ipynb)

#### Deliverable

Your finished product will be a Jupyter Notebook containing your analysis, which will include;

- Your solution code
- A brief write-up on your finds related to airport delays 
- Recommendations for analytical procedures for the datasets

If you don't finish in time, that's ok! Complete the assignment as additional practice outside of class. Remember, this lab is a valuable opportunity to refine the skills you'll need to tackle your project!

## Additional Resources

- [Scikit PCA Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- [Long-form PCA documentation](http://sebastianraschka.com/Articles/2014_pca_step_by_step.html)
