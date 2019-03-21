# fashion MNIST  Classification

This was a [Data Challenge](https://www.kaggle.com/c/fall-2018-stat-441841-data-challenge-1) done as part of University of Waterloo STAT 441 : Statistical Learning - Classification class. Using the data set borrowed from [Fashion MNIST](https://www.kaggle.com/zalando-research/fashionmnist/data) the aim was to predict the label for each id in the test set.

Restrictions
* Test set information can not be used when developing model
* 3 submissions per day

## Data
Each row in the train and test sets represent a 28 by 28 image.
The train and test set are similar except that the train set has an additional column *label*. Following are explanations of that column.

Label | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- 
Description | T-shirt/top | Trouser | Pullover | Dress | Coat | Sandal | Shirt | Sneaker | Bag | Ankle boot 

## File Descriptions
* fashion-mnist_train.csv - the training set
* test_data.csv - the test set
* sample_submission.csv - a sample submission file in the correct format

## Approach
