# Install packages
import numpy as np
import pandas as pd # Organize data; i.e. pf
import matplotlib.pyplot as plt
import itertools
import lxml.html as lh
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#from flask import Flask, request

# Start Flask
#app = Flask(__name__)

#@app.route("/", methods =['POST'])
#def Results():
#    print("Debugging String")
#    #return str(makePrediction(request.form['nameless_array']))
#    return request.form['Hello']




# Read files
df_x = pd.read_csv('num_line.csv')
df_main = df_x[['Jan', 'Andy', 'Angela', 'Creed', 'Darryl', 'David', 'Deangelo', 'Dwight', 'Erin', 'Gabe', 'Holly', 'Jim', \
    'Karen', 'Kelly', 'Kevin', 'Meredith', 'Michael', 'Oscar', 'Pam', 'Phyllis', 'Robert', 'Roy', 'Ryan', 'Stanley', 'Toby', 'Todd']]
df_y = pd.read_csv('main_ratings.csv')
df_y = df_y.drop_duplicates(subset = ['Avg_Rating'])
df_y = df_y.round(3)

# Combine datasets
df_main['Avg_Rating'] = df_y['Avg_Rating']
# Assign coordinates
X = df_main[['Jan', 'Andy', 'Angela', 'Creed', 'Darryl', 'David', 'Deangelo', 'Dwight', 'Erin', 'Gabe', 'Holly', 'Jim', \
    'Karen', 'Kelly', 'Kevin', 'Meredith', 'Michael', 'Oscar', 'Pam', 'Phyllis', 'Robert', 'Roy', 'Ryan', 'Stanley', 'Toby', 'Todd']]
X_array = X.to_numpy()
# Y 
Y = df_main['Avg_Rating']
Y_array = Y.to_numpy()

# Number of rows & columns 
# print('X -', X_array.shape)
# print('Y - ', Y_array.shape)

# Training & test sets
train, test = train_test_split(df_main, test_size=0.2, random_state=42, shuffle=True)

# Training & test cases
train_x = train.iloc[:,0:26] # Used to make the train model (formula)
train_y = train.iloc[:,26]

test_x = test.iloc[:,0:26] # Used as input values into the newly made model
test_y = test.iloc[:,26] # Used to see if predictions are right

# Training the model
reg2 = LinearRegression().fit(train_x, train_y)

print("Score: ", reg2.score(X_array, Y_array))
print("coef: ", reg2.coef_)
print("intercept", reg2.intercept_)

# Training the model
# reg = LinearRegression().fit(X_array, Y_array)
# print("Score: ", reg.score(X_array, Y_array))
# print("coef: ", reg.coef_)
# print("intercept", reg.intercept_)

# Predicting; reminder: predict() takes in a dataframe as parameters!
pred = reg2.predict([test_x.iloc[1]])
#print(pred)
#print(test_x.iloc[1])


# Demo
'''
Parameters: Takes in a normal Python list of percentages (in decimal form, i.e. 0.2)
'''
def makePrediction(percentages):
    for line in range(len(percentages)):
        percentages[line] = 5964 * percentages[line]
        prediction = reg2.predict(np.array([percentages]))
    print(prediction)
    return prediction

# Run Flask
#app.run(host='0.0.0.0')













# train.to_csv(train_path, sep='\t', index=False)
# test.to_csv(test_path, sep='\t', index=False)

'''
# Assign coordinates
# X
X = df_x[['Jan', 'Andy', 'Angela', 'Creed', 'Darryl', 'David', 'Deangelo', 'Dwight', 'Erin', 'Gabe', 'Holly', 'Jim', \
    'Karen', 'Kelly', 'Kevin', 'Meredith', 'Michael', 'Oscar', 'Pam', 'Phyllis', 'Robert', 'Roy', 'Ryan', 'Stanley', 'Toby', 'Todd']]
X_array = X.to_numpy()
# Y 
Y =  df_y['Avg_Rating']
Y_array = Y.to_numpy()
# print(X)
# print(Y)

# Number of rows & columns 
print('X -', X_array.shape)
print('Y - ', Y_array.shape)

# Training the model
reg = LinearRegression().fit(X_array, Y_array)
print("Score: ",reg.score(X_array, Y_array))
print("coef: ",reg.coef_)
print("intercept",reg.intercept_)

# Training sets (80%), odd numbered seasons
train, test = train_test_split(df_text_genre, test_size=0.2, random_state=42, shuffle=True)

# Test sets (20%), even numbered seasons


# Make predictions
# features = np.array([[57, 8, 2, 7, 5, 2, 4, 6, 202, 90, 435, 23, 45, 234, 23 , 435, 134, 80, 100, 0, 21, 56, 11, 124, 35, 345]])
# prediction = reg.predict(features)
# print(prediction)

features = np.array([[0, 1125, 166, 33, 312, 26, 0, 946, 427, 119, 0, 869, 0, 123, 247, 83, 0, 235, 475, 123, 458, 0, 189, 91, 106, 41]])
prediction = reg.predict(features)
print(prediction)

# Compare prediction to actual value
actual = 7.629166667
residual = abs(actual - prediction)
print(residual)
'''


















# data_set = []
# with open('ratings.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         new_tuple = (str(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])) # Title, Season, Episode, Rating, Avg_Rating
#         data_set.append(new_tuple)

# avg_ratings = []
# for row in data_set:
#     if row[3] in avg_ratings:
#         continue
#     avg_ratings.append(row[3])

# def main():
#     season = int(input('Enter a season: '))
#     while season != 0:
#         for row in data_set:
#             if row[1] == season:
#                 print('Average rating for this season was:', row[3])
#                 break
#         season = int(input('Enter a season. Enter 0 to quit: '))
# main()

# Web Scrape the ratings
# URL = 'https://www.ratingraph.com/tv-shows/the-office-ratings-17546/#episodes'
# page = requests.get(URL)
#doc = lh.fromstring(page.content)
#tr_elements = doc.xpath('//table')
# print([len(T) for T in tr_elements[:15]])
#print(tr_elements)
#print(tr_elements[1].text_content())

# col = []
# i = []
# for t in tr_elements[0]:
#     i += 1
#     name = t.text_context()
#     print(i, name)

 
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
#results = soup.find(id = 'episodes')
#avg_ratings = results.find_all('tr', class_='')
# print(avg_ratings)

# result = soup.find_all(class_='dataTables_wrapper no-footer')
# print(result)
# Read text file

# Cleaning the data "massaging the data"

# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import PassiveAggressiveClassifier
# from sklearn.metrics import accuracy_score, confusion_matrix

