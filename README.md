
# MLOps Project

The purpose of this MLOPs project is to compete in a Kaggle competition using deep learning techniques. The goal of the chosen competition is to develop a deep learning model that can accurately predict the ratings of players based on Scrabble gameplay. The project will utilize Docker to containerize the model and its dependencies, Kubernetes will be used to manage the containers and ensure that the model is highly available and can scale up or down as needed. And FastAPI to build the API for the model, that will be consumed in a convenient and user-friendly web platform of SPA (Single Page Application) type to perform the predictions.




## Demo

Preview of the web platform of type SPA
![alt text](https://github.com/be-soumaya/DeepLearning_Project/blob/main/DeepLearning_Project-Frontend/result.png?raw=true)

## Run Locally

Clone the project

```bash
  git clone https://github.com/be-soumaya/DeepLearning_Project
```

Go to the backend project directory

```bash
  cd DeepLearning_Project\DeepLearning_Project-Backend\app
```

Run FastAPI server 

```bash
  uvicorn main:app --reload
```

Go to the frontend project directory

```bash
  cd DeepLearning_Project\DeepLearning_Project-Frontend\app
```

Run Angular server 

```bash
  ng serve
```

## Developed by:
EL BELHADJI Soumaya

FAHAM Hassan
