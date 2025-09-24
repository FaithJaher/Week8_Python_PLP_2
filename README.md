import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers (sampled data).")

# Load reduced dataset
@st.cache_data
def load_data():
    df = pd.read_csv('metadata_small.csv')
    return df

df = load_data()

# Sidebar Filters
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select Year Range", year_min, year_max, (year_min, year_max))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"### Showing {filtered.shape[0]} papers from {year_range[0]} to {year_range[1]}")

# Publications by Year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax1, color='skyblue')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Papers')
st.pyplot(fig1)

# Top Journals
st.subheader("Top 10 Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax2, color='lightgreen')
ax2.set_xlabel('Number of Papers')
ax2.set_ylabel('Journal')
st.pyplot(fig2)

# Word Cloud of Titles
st.subheader("Common Words in Titles")
all_titles = " ".join(filtered['title'].dropna().tolist())
clean_text = re.sub(r'[^A-Za-z ]', '', all_titles).lower()
wordcloud = WordCloud(width=900, height=450, background_color='white').generate(clean_text)
fig3, ax3 = plt.subplots()
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# Show Sample Data
st.subheader("Sample of Data")
st.dataframe(filtered.head(20))
