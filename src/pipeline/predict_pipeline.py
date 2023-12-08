import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        CreditScore: str,
        Geography: str,
        Gender,
        Age: str,
        Tenure: str,
        Balance: int,
        NoOfProducts: int,
        HasCrCard:str,
        IsActiveMember:str,
        EstimatedSalary:int,
        Exited:str,
        Complain:str,
        SatisfactionScore:int,
        CardType:str,
        PointEarned:int):

        self.CreditScore = CreditScore
        self.Geography = Geography
        self.Gender = Gender
        self.Age = Age
        self.Tenure = Tenure
        self.Balance = Balance
        self.NoOfProducts = NoOfProducts
        self.HasCrCard = HasCrCard
        self.IsActiveMember = IsActiveMember
        self.EstimatedSalary = EstimatedSalary
        self.Exited = Exited
        self.Complain = Complain
        self.SatisfactionScore = SatisfactionScore
        self.CardType = CardType

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "CreditScore": [self.CreditScore],
                "Geography": [self.Geography],
                "Gender": [self.Gender],
                "Age": [self.Age],
                "Tenure": [self.Tenure],
                "Balance": [self.Balance],
                "NoOfProducts": [self.NoOfProducts],
                "HasCrCard": [self.HasCrCard],
                "IsActiveMember": [self.IsActiveMember],
                "EstimatedSalary": [self.EstimatedSalary],
                "Exited": [self.Exited],
                "Complain": [self.Complain],
                "SatisfactionScore": [self.SatisfactionScore],
                "CardType": [self.CardType],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)