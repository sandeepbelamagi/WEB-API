import pandas as pd

a = pd.read_csv("jsonoutput.csv")

a.to_html("crime.htm")

html_file = a.to_html()