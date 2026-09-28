movies = {
    "3 Idiots": ["comedy", "drama", "college"],
    "Taare Zameen Par": ["drama", "education", "family"],
    "Dangal": ["sports", "drama", "family"],
    "Chhichhore": ["college", "comedy", "drama"],
    "Zindagi Na Milegi Dobara": ["comedy", "friendship", "adventure"],
    "MS Dhoni": ["sports", "biography", "drama"],
    "Yeh Jawaani Hai Deewani": ["romance", "friendship", "comedy"],
    "12th Fail": ["education", "biography", "drama"]
}


def recommend_movies(preference):
    recommendations = []

    for movie, genres in movies.items():
        if preference.lower() in genres:
            recommendations.append(movie)

    return recommendations


print("================================")
print("     MOVIE RECOMMENDATION SYSTEM")
print("================================")

print("\nAvailable preferences:")
print("comedy")
print("drama")
print("college")
print("sports")
print("family")
print("friendship")
print("education")
print("romance")
print("adventure")
print("biography")

preference = input("\nEnter your preference: ")

recommendations = recommend_movies(preference)

if recommendations:
    print("\nRecommended Movies:")

    for movie in recommendations:
        print("-", movie)
else:
    print("\nSorry, no movies found for this preference.")
