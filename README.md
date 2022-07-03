# HomeCreditDefaultRisk
## Notebook Files:
### Main File:
#### Capstone_Project-Home-Credit-Default-Risk_V0.1.ipynb:  This file contained every main body parts of the project

### Supplementary Files: (To avoid long execution time, modeling parts are in seperate notebooks)
##### Bagging_Model.ipynb: The file contained RandomForest Classifier modeling.
##### Boosting_Model.ipynb: The file contained GradientBoosting Classifier modeling.
##### Base_Model.ipynb: The file contained DecisionTree Classifier modeling.

## Datasets: 
![image](https://user-images.githubusercontent.com/61896045/177057284-9469216d-f04d-4161-bae8-49edb532bf23.png)
Note: I only picked four tables contain the main information in the project

Data Source: https://www.kaggle.com/competitions/home-credit-default-risk/data
### bureau.csv:
- Monthly balances of previous credits in Credit Bureau.
- This table has one row for each month of history of every previous credit reported to Credit Bureau – i.e the table has (#loans in sample # of relative previous credits # of months where we have some history observable for the previous credits) rows.
### previous_application.csv:
- All previous applications for Home Credit loans of clients who have loans in our sample.
- There is one row for each previous application related to loans in our data sample.
### application_test/train.csv:
- This is the main table, broken into two files for Train (with TARGET) and Test (without TARGET).
- Static data for all applications. One row represents one loan in our data sample.
### HomeCredit_columns_description.csv: 
- This file contains descriptions for the columns in the various data files.
## Model Files: format(Model_Name_WithSMote_WithUndersampling)
### DecisionTree_model.sav
### DecisionTree_model_smote.sav
### DecisionTree_model_smote_under.sav
### GradientBoost_model.sav
### GradientBoost_model_smote.sav
### GradientBoost_model_smote_under.sav
### RandomForest_model.sav
### RandomForest_model_smote.sav
### RandomForest_model_smote_under.sav
