from jinja2 import FileSystemLoader
from latex.jinja2 import make_env
from latex import build_pdf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy.random as random
import os

# Read data in
df = pd.read_csv('irisdata.csv')

# Graph path
path = os.path.dirname(os.path.realpath(__file__)) + "/graphs/"

# Calculate descriptive statistics
mean = df["SepalWidth"].mean()
std = df["SepalWidth"].std()
var = df["SepalWidth"].var()
median = df["SepalWidth"].median()
q1 = np.percentile(df["SepalWidth"], 25)
q3 = np.percentile(df["SepalWidth"], 75)

# Create graphs
plt.boxplot(df["SepalWidth"], 0, 'rs', 0)
plt.title('Sepal Width Box Plot')
plt.savefig(path + "boxplot.pdf", format="pdf", transparent=True, bbox_inches='tight', pad_inches=0)
plt.figure()

plt.hist(df["SepalWidth"], bins='auto')
plt.title('Sepal Width Histogram')
plt.savefig(path + "histogram.pdf", format="pdf", transparent=True, bbox_inches='tight', pad_inches=0)

# Create
data = df["SepalWidth"].copy()
data.sort()
norm=random.normal(0,2,len(data))
norm.sort()
plt.figure(figsize=(12,8),facecolor='1.0')

plt.plot(norm,data,"o")

#generate a trend line as in http://widu.tumblr.com/post/43624347354/matplotlib-trendline
z = np.polyfit(norm,data, 1)
p = np.poly1d(z)
plt.plot(norm,p(norm),"k--", linewidth=2)
plt.title("Normal Q-Q plot", size=28)
plt.xlabel("Theoretical quantiles", size=24)
plt.ylabel("Expreimental quantiles", size=24)
plt.tick_params(labelsize=16)
plt.savefig(path + "qqnorm.pdf", format="pdf", transparent=True, bbox_inches='tight', pad_inches=0)



# Output to PDF
env = make_env(loader=FileSystemLoader('.'))
tpl = env.get_template('doc.latex')
filename = 'STAT4705-Extra.pdf'

pdf = build_pdf(tpl.render(mean=mean, std=std, var=var, median=median, q1=q1, q3=q3, path = path))
pdf.save_to(filename)
