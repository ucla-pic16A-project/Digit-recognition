<a name="readme-top"></a>

# Digit Recognition
Contributors: Haoyu Li, Tong Xie, Judy Zhu


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Overview</a>
      <ul>
        <li><a href="#built-with">Requirements</a></li>
      </ul>
      <ul>
        <li><a href="#dataset">Dataset</a></li>
      </ul>
    </li>
    <li>
      <a href="#exploration">Data Exploration</a>
    </li>
    <li><a href="#model">Model Training</a>
    </li>
    <li><a href="#performance">Performance Analysis</a>
      <ul>
        <li><a href="#score">Accuracy Scores</a></li>
      </ul>
      <ul>
        <li><a href="#confusion">Confusion Matrices</a></li>
      </ul>
    </li>
    <li><a href="#efficiency">Efficiency Anlysis</a>
      <ul>
        <li><a href="#time">Execution Times</a></li>
      </ul>
      <ul>
        <li><a href="#plot">Efficiency Plot</a></li>
      </ul>
    </li>
    <li><a href="#logistic">Comparison between Handwritten and Package Function</a>
      <ul>
         <li><a href="#accuracy">Accuracy Matrix</a></li>
      </ul>
    </li>
    <li><a href="#limit">Scope and Limitations</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Reference and Acknowledgments</a></li>
    <li><a href="#demo">Demo Video</a></li>
  </ol>
</details>


<a name="about-the-project"></a>
<!-- GETTING STARTED -->
## Overview

The objective of this project is to classify hand-written digits from 0 to 9 using various machine learning models and compare their efficiency. Four models are selected for analysis: **Logistic Regression, MLP, Random Forest Classifier, KNN**. A manual implementation of Logistic Regression is also included for binary classification to compare with the package logistic regression function.

<a name="built-with"></a>
### Requirements

* [Numpy (1.21.5)](http://www.numpy.org/) - Multidimensional Mathematical Computing
* [Pandas (1.4.2)](https://pandas.pydata.org/docs/getting_started/overview.html#) - Access Tabular data
* [Matplotlib (3.5.1)](https://matplotlib.org/contents.html) - Used to plot Graph
* [Sklearn (1.0.2)](https://scikit-learn.org/stable/) - Machine learning models

<a name="dataset"></a>
### Dataset
* [OpenML Dataset](https://www.openml.org/d/554) - Dataset for Digit Recognition


<a name="exploration"></a>
<!-- Data Intro -->
## Data Exploration
The dataset is a collection of 70,000 handwritten digits ranging from 0 to 9. <br /> <br />
Image of each data point is 28 pixels wide and long, which gives the total of 28 x 28 = 724 pixels. The 724 pixels make up the 724 features of a data point and each feature stores a value ranging from 0 to 1 to indicate the handwritting.

Examples of data point images
![image](https://user-images.githubusercontent.com/117710195/206927660-c0333f6d-948b-41e1-b0c3-50015441df1d.png)

Spliting the dataset into features X and label y
<img width="1305" alt="X" src="https://user-images.githubusercontent.com/117710195/206927242-24fecc98-e3bc-43b4-89b6-273570403ba1.png">
<img width="161" alt="y" src="https://user-images.githubusercontent.com/117710195/206927690-7ea0263c-986b-4a8a-98f8-285c57193065.png">

<a name="model"></a>
<!-- Model Training -->
## Model Training
The **70/30 train_test_split** is performed before fitting the models. <br />

X_train <br />
<img width="1307" alt="image" src="https://user-images.githubusercontent.com/117710195/206931660-ea530241-8516-49a7-aff7-6fe2464afe41.png"> <br />

y_train <br />
<img width="234" alt="image" src="https://user-images.githubusercontent.com/117710195/206931681-25b385ff-1f60-4ee2-8801-ba1beb27fb33.png">

Shape of X_train, y_train <br />
<img width="169" alt="image" src="https://user-images.githubusercontent.com/117710195/206931717-67602c4e-29a8-40bb-b264-92e78803e565.png">

Four classification models (Logistic Regression, MLP, Random Forest Classifier, KNN) are trained using _model.fit(X_train, y_train)_ <br />
The corresponding scores are then calculated using _model.score(X_test, y_test)_

<a name="performance"></a>
<!-- Performance Analysis -->
## Performance Analysis

<a name="score"></a>
### Accuracy Scores
1. Logistic Regression: 0.91614
2. Multilayer Perceptron: 0.97452
3. Random Forest Classifier: 0.96795
4. K-nearest Neighbors: 0.97086

<a name="confusion"></a>
### Confusion Matrices
Visualize and compare the performance of models used

<img width="1204" alt="Screen Shot 2022-12-11 at 1 05 08 PM" src="https://user-images.githubusercontent.com/117710195/206928747-b4e52f5e-4c10-410b-8eeb-0db494da7994.png">

***How to interprete these matrices?***
1. For entry i, j in the matrix, the number in it represents the number of predicts which has predicted label i and actual label j.
2. As can be seen in the color bar on the right hand side, darker blue means more, so we can see most of samples are predicted correctly for all the models.
3. One particularly intresting thing is that, it seems that our models are good at predicting different kinds of numbers, for example, logistic regression often confuses between 1 and 8, but random forest and KNN did super good on it.

Overall, the four different classification models used all show higher inaccurary with predicting digits 2, 3, and 8.


<a name="efficiency"></a>
<!-- Efficiency -->
## Efficiency Analysis
This section analyzes the efficiency of the four models by comparing their accuracy score and execution time. <br />

<a name="time"></a>
### Execution Times (Seconds)
1. Logistic Regression: 54.3764
2. Multilayer Perceptron: 51.386
3. Random Forest Classifier: 21.981
4. K-nearest Neighbors: 36.4333

<img width="1209" alt="image" src="https://user-images.githubusercontent.com/117710195/206930061-0d2ff940-593e-48ac-aa27-58a4a47e19e0.png"> <br />

***How to interprete these histograms?***
1. It seems that logistic regression is bad in this particular dataset. It's not that accurate, and takes a long time...
2. Multilayer perceptron is good in performance, but in the same time it's quite time consuming. I guess that's like a typical neural network behavior, which seems to take a lot of resourses.
3. KNN and Random Forest seems to be the best algorithms to employ here. They both have good performance (KNN is slightly higher but within range of error), and they are both resource friendly.

<a name="plot"></a>
### Efficiency Plot <br />
<img width="544" alt="image" src="https://user-images.githubusercontent.com/117710195/206930171-75786f4c-18ee-41c6-a7dd-441bd1b7ccda.png">

***How to interprete this scatter plot?*** 
1. This graph plots one time behavior (score vs. time) for all four classification models
2. Points closer to the bottom right have higher efficiency (high accuracy score + short execution time)

According to the metrics of accuracy score and execution time, **K-nearest Neighbors** and **Random Forest Classifier** appear to be the best-performing models out of the four utilized in this project. To further extend the study, other prevailing models for image classification such as Convolutional Neural Network (CNN) may also be included for analysis.


<a name="logistic"></a>
<!-- Logistic regression -->
## Comparison between Handwritten and Package Function
We implemented a binary logistic regression classifier based on gradient descent. Then we compared this handwritten class performance with the sklearn package logistic regression function with solver liblinear. 

<a name="accuracy"></a>
### Accuracy Matrices
<img width="500" alt="handwritten" src="https://user-images.githubusercontent.com/108601140/206944681-f0ebb919-3383-4b01-84a7-6ce5c21dfc7c.png">
<img width="500" alt="package" src="https://user-images.githubusercontent.com/108601140/206945695-f58bb3c0-5deb-4382-a571-68e03c7cca91.png">

***How to interprete these two matrices?***
1. Overall I think the handwritten model did fairly well in predicting data, the accuracy achived by the library function is only slightly better.
2. It's interesting to see that both the handwritten models and the provided models are weak in classifying between certain numbers like 3 and 5. 
3. However, a major drawback for the handwritten naive version is that the time performace is much weaker than the library function, and I belive that makes sense.

<a name="limit"></a>
## Scope and Limitations
1. This method of digit recognition has errors and might results in incorrection preditions of the handwrittings compared to classification by humans. This misinformation may cause issues when working with real-life applications that require high accuracy in data recognition.
2. The current sample database is limited to the handwritting styles collected. Therefore may not be applicable to certain texts or may result in highly inaccurate predictions.
3. To enhance the performance of this model, more complex and extensive database that contains diverse handwritting styles should be included. 
4. Potential extension of this project may include generalizing the recognition for numbers with more digits, other handwritten characters, such as alphabets, mathematical symbols, calligraphy, and foreigns characters.

<a name="license"></a>
<!-- LICENSE -->
## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


<a name="acknowledgments"></a>
<!-- ACKNOWLEDGMENTS -->
## Reference and Acknowledgment

* [UCLA PIC16A](https://sa.ucla.edu/ro/ClassSearch/Results/ClassDetail?subj_area_cd=COMPTNG&crs_catlg_no=0016A+++&class_no=+002++&class_id=157048210&term_cd=22F) - Source of most theoretical concepts
* [CS229.stanford.edu](https://cs229.stanford.edu/) - Some theoretical concepts of Logistic Regression
* [UCLA Math156 Notes](https://github.com/HanbaekLyu/Math156_UCLA_SP21/blob/main/LectureNotes/lecturenote_156.pdf) - Background knowledge on implementation of Logistic Regression in Python


<a name="demo"></a>
## Demo Video
The following is the link for our demo video of the project, which consists of a short overview of the project and a presentation of our final result:
[Project Demo Video](https://youtu.be/WCYJ7D4p3pY)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
