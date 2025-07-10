# movie_api_analysis
Provided project files contain 10 Oscar-winning movies and their IMDb ids. Gather data on these movies for an analysis using the [OMDb API](http://www.omdbapi.com) and the IMDb Ids from the CSV. Save the information into a CSV file. Then answer a few questions about the data using JupyterLab.

## Instructions
1. Create a project folder, set up a virtual environment, and install Python's `requests` library
2. Create a `requirements.txt` file
3. Create a python file called `movie_requests.py` to hold your code
4. Import `requests`, `csv`, and your API key
5. Create a function to request data from the OMDb API for each movie in the CSV file using their IMDB Ids
6. Save the returned data to a new CSV file named `movies.csv`. It should include:
    - Movie title (string)
    - Runtime (integer)
    - Genre (string)
    - Award Wins (integer)
    - Award Nominations (integer)
    - Box Office (integer)
_Note: when the reviewer runs your file, it should make the requests and create the CSV file without errors_
7. Open your project folder in JupyterLab and create a new notebook called `movie_analysis`
8. At the top, import `pandas`, `matplotlib`, and your `movies.csv` file
9. Answer the following questions in your notebook:
    - What was the runtime for each movie? (graph)
    - What movie had the longest runtime?
    - Is there any relationship between the length of the movie (runtime) and the number of awards a movie won?
    - How many awards and nominations did each movie receive? (graph)
10. Use markdown cells in your notebook to separate out each question. Write out how you got your answersa nd make sure to clearly note the answer to each question.
11. Create a presentation of your analysis using Google slides. It should include:
    - a title slide
    - information about the data used
    - details about your analysis (more than 1 slide)
    - conclusion

## Extra Credit
1. Add 5 movies of your choice. You can either add them to the CSV or add them via your python file. The python program should then call the movie API to gather data on these 5 movies as well, and add them to the CSV for analysis. They should be included in each analysis question.
_Note: to find a movie's IMDb Id, you can search for the movie on IMDB. In the address bar, you should be able to find the id._
2. Add 3 additional columns of information to the `movies.csv` file. Example:
    - Rated
    - Director
    - Released
    - Language
    - etc.
3. Answer the following additional questions:
    - Is there a relationship between the amoun of box office earnings a movie had and the amount of total nominations the movie received? (total nominations = award wins + award nominations)
    - Is there a relationship between box office earnings and movie runtimes?
    - How much did each movie earn at the box office? (graph)
    - What is the total count of each genre present in the dataset? (graph) (how many times does fantasy, drama, adventure, etc. show up?)
4. Use markdown in your notebook to separate each question. Write out how you got your answers and make sure to clearly note the answer to each question. 