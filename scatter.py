import pandas as pd 
import plotly.express as py

data = pd.read_csv('./data.csv')

#students = data.loc[ data['student_id'] == 'TRL_987']
level = data.groupby('student_id')
meanlevel = level['attempt'].mean()
print(meanlevel)

graph = py.scatter(data , x = "student_id" , y = "level" , color = "attempt")
graph.show()
