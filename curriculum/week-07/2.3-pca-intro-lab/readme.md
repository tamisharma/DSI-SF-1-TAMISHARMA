---
title: PCA Lab - Choose Your Own Adventure
type: lab
duration: "1:25"
creator:
    name: Patrick Smith
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) PCA Lab: Choose Your Own Adventure

## Introduction

> **Note:** _This should be a pair or small group exercise._

We've learned what dimensionality reduction is, how it's applied through PCA, and mathematically what PCA does to our data; now, it's time to put your skills to the test! For this lab session, we are going to complete a full principal component analysis using python on two different datasets.  

Here's the cases: 

**Case 1:**

You're working for a political watchdog that wants to track and analyze the voting behavior of various politicians. Specifically, we want to understand how the political affiliation of a member of the House of Representatives affects their voting record. You're given a [dataset](./assets/datasets/votes.csv) with a affiliations as well as voting records for a variety of key bills. 

Your task is to perform PCA to determine the principal components of this dataset so that your data science team can perform a clustering analysis to learn how political affiliation is related to voting.

**Case 2:**

You're working for the FAA and want to understand the nature of flight delays. Looking at the [operations data](./assets/datasets/Airport_operations.csv) for various airports, you want to understand what components are most important for each airport so that the FAA can target and assess poor performing airports. 

Your task is conduct a PCA on this data so that your team can perform a clustering analysis later on. 

## Exercise

#### Requirements

- Import the data
- Perform a Principal Component Analysis on both dataset to determine which components are most significant for each of the use cases.
    - Conduct a PCA using the long-form method as well as using Scikit-Learn.
- Create a write-up of your findings; for the technical team members make sure to comment your process, and for the non-technical team members, draft a brief report to outline why your findings are significant.

Just as in a real life scenario, the data and your analysis will not always be clear cut. While you may be wondering when you've succeeded in solving the problem,  we're looking for your best recommendations based on the available data. Work through the process until you and your teammate have enough information to provide an in-depth analysis.

**Bonus:**
- Perform a K-Means analysis after you have conducted the PCA.
- Plot the principal components.

#### Starter Code & Data

- Download the [congressional data](./assets/datasets/votes.csv) and the [airline data](./assets/datasets/Airport_operations.csv).
- Grab the [starter code](./code/starter-code.ipynb) to get started. 

**Note:**
The index for the bill column variables of the Congressional voting dataset are as follows: 

  - V1. handicapped-infants: 2 (y,n)
  - V2. water-project-cost-sharing: 2 (y,n)
  - V3. adoption-of-the-budget-resolution: 2 (y,n)
  - V4. physician-fee-freeze: 2 (y,n)
  - V5. el-salvador-aid: 2 (y,n)
  - V6. religious-groups-in-schools: 2 (y,n)
  - V7. anti-satellite-test-ban: 2 (y,n)
  - V8. aid-to-nicaraguan-contras: 2 (y,n)
  - V9. mx-missile: 2 (y,n)
  - V10. immigration: 2 (y,n)
  - V11. synfuels-corporation-cutback: 2 (y,n)
  - V12. education-spending: 2 (y,n)
  - V13. superfund-right-to-sue: 2 (y,n)
  - V14. crime: 2 (y,n)
  - V15. duty-free-exports: 2 (y,n)
  - V16. export-administration-act-south-africa: 2 (y,n)

#### Deliverable

Your finished product will be a Jupyter Notebook containing your analysis, including:

- Your solution code
- A brief write-up on your findings, with one paragraph on your findings and one paragraph on your procedures, related to voting trends and airport delays 
- Recommendations for analytical procedures for these datasets

## Additional Resources

- A link to [Scikit PCA Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- Extra relevant [long-form PCA documentation](http://sebastianraschka.com/Articles/2014_pca_step_by_step.html)
