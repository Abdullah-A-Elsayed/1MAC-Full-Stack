"""
invisible guest
inception
source code
interstellar
shawshank
end of watch
"""
import movie
import fresh_tomatoes
a = movie.Movie("The Invisible Guest",
	"A young businessman wakes up in a locked hotel room next to the body of his dead lover. He hires a prestigious lawyer to defend him, and over the course of one night, they work together to find out what happened.",
	"https://www.youtube.com/watch?v=epCg2RbyF80",
	"https://occ-0-999-1001.1.nflxso.net/art/03505/528ab16bb9bdd765a40d0f646b46e1a4def03505.jpg"
	)
b = movie.Movie("Inception",
	"Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious.",
	"https://www.youtube.com/watch?v=d3A3-zSOBT4",
	"https://usercontent1.hubstatic.com/12893496_f520.jpg"
	)
c = movie.Movie("Source Code",
	"Helicopter pilot Colter Stevens (Jake Gyllenhaal) is part of a top-secret military operation that enables him to experience the last few minutes in the life of Sean Fentress, a man who died in a commuter-train explosion.",
	"https://www.youtube.com/watch?v=zDMXC0nLaxI",
	"http://www.asset1.net/tv/pictures/movie/source-code-2011/KA-SourceCode.jpg"
	)
d = movie.Movie("Interstellar",
	"In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable.",
	"https://www.youtube.com/watch?v=0vxOhd4qlnA",
	"https://therealsasha.files.wordpress.com/2015/03/interstellar-main-one-sheet.jpg"
	)
e = movie.Movie("The Shawshank Redemption",
	"Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms in prison for the murders of his wife and her lover and is sentenced to a tough prison.",
	"https://www.youtube.com/watch?v=K_tLp7T6U1c",
	"https://images-na.ssl-images-amazon.com/images/I/519NBNHX5BL._SY445_.jpg"
	)
f = movie.Movie("End of Watch",
	"Longtime LAPD partners and friends, Brian Taylor (Jake Gyllenhaal) and Mike Zavala (Michael Pena) patrol one of the most dangerous neighborhoods in Los Angeles.",
	"https://www.youtube.com/watch?v=mf2K9GzgiF0",
	"https://images-na.ssl-images-amazon.com/images/I/91YZy2zZAWL._SY445_.jpg"
	)
movies = [a,b,c,d,e,f]
fresh_tomatoes.open_movies_page(movies)