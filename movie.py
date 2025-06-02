movies = {"Bad Boys":4.7, "Ride or Die":4, "Avatar":5,"Titanic":4.5}
m = input("Enter a movie title" )

if m in movies:
    print(f"The rating for {m} is {movies[m]}")
else:
    add_movie=input("Would you like to add the movie? (yes/no)" ).strip()
    if add_movie =="yes":
       new_rating =float(input(f"please rate {m} " ))
       movies[m]=new_rating
       print(f"{m} has been added with a rating of {new_rating}")
    else:
        print("Maybe help us adding it🤭")

print(movies)
