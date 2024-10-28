import pickle
import os

class Model_loader:
    def __init__(self,
                    path_to_dv:os.PathLike = "models/dv.bin",
                        path_to_lr:os.PathLike = "models/model2.bin"):

        # load DictVectorizer
        with open(path_to_dv, 'rb') as dv_file: 
            self.dv = pickle.load(dv_file)

        # load LogisticRegression
        with open(path_to_lr, 'rb') as lr_file: 
            self.lr = pickle.load(lr_file)
        
    def forward(self, client: dict): 
        # make predictions
        X = self.dv.transform(client)
        prob = self.lr.predict_proba(X)[0][1]

        return round(prob, 3)

if __name__ == "__main__": 
    path_to_dv = "models/dv.bin"
    path_to_lr = "models/model1.bin"
    loader = Model_loader(path_to_dv, path_to_lr)
    
    """ Make prediction on client example
    """
    client_example = {"job": "management", "duration": 400, "poutcome": "success"}
    prob = loader.forward(client_example)
    print(f"Prob to get a subscription: {prob:.3f}")
