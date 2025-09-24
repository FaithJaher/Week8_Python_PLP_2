import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from wordcloud import WordCloud

# Part 1: Data Loading and Basic Exploration 
df = pd.read_csv('metadata_small.csv')
print("Shape:", df.shape)
print(df.info())
print(df.head())

# Basic Exploration
print("Missing values per column:")
print(df.isnull().sum())

print("Basic stats for numeric columns:")
print(df.describe())

# Part 3: Data Analysis and Visualization
# Publications by Year
year_counts = df['year'].value_counts().sort_index()

plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values, color='skyblue')
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top Journals
top_journals = df['journal'].value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(y=top_journals.index, x=top_journals.values, color='lightgreen')
plt.title('Top 10 Journals')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
plt.tight_layout()
plt.show()

# Word Frequency in Titles
# Combine all titles into a single string
all_titles = " ".join(df['title'].dropna().tolist())

# Clean text (letters only, lowercase)
clean_text = re.sub(r'[^A-Za-z ]', '', all_titles).lower()

# Generate a word cloud
wordcloud = WordCloud(width=900, height=450, background_color='white').generate(clean_text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Frequent Words in Paper Titles')
plt.show()

# Paper Counts by Source
source_counts = df['source_x'].value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(y=source_counts.index, x=source_counts.values, color='orange')
plt.title('Top 10 Sources')
plt.xlabel('Number of Papers')
plt.ylabel('Source')
plt.tight_layout()
plt.show()
