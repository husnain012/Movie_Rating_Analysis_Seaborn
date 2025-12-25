import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("="*50)
print("MOVIE RATINGS ANALYSIS")
print("="*50)
print("\n")

# Load Data
data = pd.read_csv("movies_dataset.csv")
print("------------ Data Overview ------------")
print("\n")
print(data.head())
print("\n")

# 1) Top 5 Highest Rated Movies
high_rated = data.sort_values(by="rating", ascending=False)
top_5 = high_rated.head(5)
print("------------ Top 5 Highest Rated Movies ------------")
print("\n")
print(top_5)
print("\n")

# 2) Average Rating Per Genre
avg_rating = data.groupby("genre")["rating"].mean()
print("------------ Average Rating Per Genre ------------")
print("\n")
print(avg_rating)
print("\n")

# 3) Count of Movies Released Each Year
movies_count = data.groupby("release_year")["movie_name"].count()
print("------------ Count of Movies Released Each Year ------------")
print("\n")
print(movies_count)
print("\n")

# 4) Movies with rating > 8.0 and votes > 50000
highly_rated_popular_movies = data[(data["rating"] > 8.0) & (data["votes"] > 50000)]
print("------------ Movies with rating > 8.0 and votes > 50000 ------------")
print("\n")
print(highly_rated_popular_movies)
print("\n")

# 5) Genre with the Highest Average Votes
h_avg_rating = data.groupby("genre")["votes"].mean().idxmax() 
print("------------ Genre with the Highest Average Votes ------------")
print("\n")
avg_votes = data.groupby("genre")["votes"].mean()
print(h_avg_rating, ":", avg_votes[h_avg_rating])
print("\n")

# 6) Longest Movie by Duration
long_movie = data.loc[data["duration"].idxmax()]
print("------------ Longest Movie by Duration ------------")
print("\n")
print(long_movie)
print("\n")

# 7) Bar Chart — Genre vs Average Rating

plt.figure(figsize=(9, 4))
sns.set_style(style="whitegrid")
ax = sns.barplot(data=data, x="genre", y="rating", palette="viridis",
                 hue="genre", legend=False,
                 edgecolor="black", errorbar=None)
plt.title("Average Rating Per Genre", fontweight='bold')
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Rating", fontsize=12)

# Add value labels
for container in ax.containers:
    ax.bar_label(container, fmt="%.2f", padding=1, )

plt.tight_layout()
plt.savefig('Visualization/genre_ratings_seaborn.png', dpi=300,
            bbox_inches='tight', transparent=False)
plt.show()
print("\n")

# 8) Line Plot — Movies Released Per Year

sns.set_style(style="whitegrid")
movies_count = data.groupby("release_year")["movie_name"].count()
line_data = pd.DataFrame({
    "year": movies_count.index,
    "movies": movies_count.values
})
plt.figure(figsize=(10, 6))
sns.lineplot(data=line_data, x="year", y="movies",
             marker="o", color="#2E8B57", linewidth=2,
             alpha=0.6, linestyle="--")
plt.title("Movies Released Per Year", fontweight="bold")
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Number of Movies", fontsize=12)

for year, count in movies_count.items():
    plt.text(year, count, str(count),
             ha="center", va="bottom", fontweight="bold")

plt.tight_layout()
plt.savefig('Visualization/movies_releases_per_year_seaborn.png', dpi=300,
            bbox_inches='tight', transparent=False)
plt.show()
print("\n")

# 9) Horizontal Bar Plot- Top 5 Highest Rated Movies

plt.figure(figsize=(10, 5))
sns.set_style("whitegrid")

ax = sns.barplot(data=top_5, x="rating", y="movie_name",
                 palette="viridis", hue="genre")

plt.title("Top 5 Highest Rated Movies", fontweight='bold')
plt.xlabel("Rating", fontsize=12)

plt.legend(title='Genre', bbox_to_anchor=(1.05, 0.5), loc='center left')

# Value labels
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f', padding=5, fontweight='bold')

plt.tight_layout()
plt.savefig('Visualization/high_rated_movies_seaborn.png', dpi=300,
            bbox_inches='tight', transparent=False)
plt.show()
print("\n")

# 10) Scatter Plot - Highly-Rated Popular Movies by Genre

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

sns.scatterplot(data=highly_rated_popular_movies, x="rating",
                y="votes", hue="genre", s=100, alpha=0.7)

plt.title("Highly-Rated Popular Movies", fontsize=14, fontweight='bold')
plt.xlabel("Rating (IMDb)", fontsize=12)
plt.ylabel("Votes", fontsize=12)

plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('Visualization/high_rated_movies_genre_seaborn.png', dpi=300,
            bbox_inches='tight', transparent=False)
plt.show()
print("\n")

# 11) Bar Plot  with highest average votes

h_votes_genre = data.groupby("genre")["votes"].mean().idxmax() 
highest_value = data.groupby("genre")["votes"].mean().max()

plt.figure(figsize=(9, 4))
sns.set_style(style="whitegrid")
sns.set_palette("Set2")
ax = sns.barplot(data=data, x="genre", y="votes",
                 edgecolor="black", errorbar=None)
plt.title(f"Genre with highest average votes: {h_votes_genre }({highest_value:.0f} votes)",
          fontweight='bold')
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Votes", fontsize=12)

# Add value labels
for container in ax.containers:
    ax.bar_label(container,
             fmt=lambda x: f'{x:,.0f}', padding=5, fontweight='bold')

plt.tight_layout()
plt.savefig('Visualization/genre_high_votes_genre_seaborn.png', dpi=300,
            bbox_inches='tight', transparent=False)
plt.show()