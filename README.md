# Flask subscription web app

Web service for ML model deploying using flask & Dockerization. The model predicts that the client will get a subscription based on its features like job, duration and poutcome

<img src="https://www.sender.net/wp-content/uploads/2023/01/B088-Email-Subscription-small.webp" alt="Email Subscription" width="400">


To run the project you can do the following: 

``` 
# build the docker image

docker build -t flask_app .
```

```
# run the docker container

docker run --rm flask_app
```

As a result you will see the probability that the client will get a subscription like this: 

```
{'subscription_prob': 0.757}
```

You can change your client features in the src/prediction.py file: 

```
client = {"job": "management", "duration": 400, "poutcome": "success"}
```
