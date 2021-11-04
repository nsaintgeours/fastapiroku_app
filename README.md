# Fastapiroku: a Streamlit dashboard deployed with Heroku.

This project is a very basic demo of how to deploy a Python dashboard in the cloud using:
* `streamlit` for web app' implementation
* **Heroku** for free deployment
* a call to a REST API that returns some predicted value from user inputs

The app' is available here: https://fastapiroku.herokuapp.com/  

## How to deploy the app' on Heroku 

I have followed these two tutorials: 
- https://towardsdatascience.com/deploying-a-basic-streamlit-app-to-heroku-be25a527fcb3  
- https://towardsdatascience.com/a-quick-tutorial-on-how-to-deploy-your-streamlit-app-to-heroku-874e1250dadd

## Making calls to a regressor through a home-made REST API

The Streamlit dashboard allows the user to enter four values of model inputs `x1` to `x4`. 
It then calls a prediction REST API that returns some predicted value for these model inputs, and this output value is 
displayed on the dashboard.

This prediction API was built in another Github project called [fastapiroku_ml](https://github.com/nsaintgeours/fastapiroku_ml).
In this other project, I trained a basic linear regressor on some data with `sklearn`, and deployed it as a REST API on
the web using `fastapi` and **Heroku**.  
