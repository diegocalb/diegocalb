This directory contains 4 projects:

- Docker_ex
- Blood donor
- Countries
- House price


**Docker_ex** is an exercise where I use Docker to create a container and, get data from IEX cloud and save the df into a postgres table.

**Blood donor** is another project where blood is analyzed and different molecular markers are detected and measured. In that scenario, a patient could be classified as donor or other categories including Hepatitis C. I used a Logistic Regression model.
If you download this project, you can run a web app (I used streamlit) writting the following code:

```streamlit run app.py```

**Countries** is a clustering project. In that project, I identify countries with low income and high child mortality that need help and NGOs could target their resources to them. I used K-means.

**House price** is a project where you can predict the price of a house. I performed a LGBoost model with a grid search to find the best hyperparameters.
If you download this project, you can run a web app (I used streamlit) writting the following code:

```streamlit run app.py```
