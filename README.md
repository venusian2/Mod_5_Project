## Song Genre Classification/Lyric Generator

DSC NYC Flatiron Module 5 Project
By: **Jason Drummond**

## Presentation Link https://drive.google.com/file/d/1YVenbHzhBOjG9DXfvh8C3wjeYGen6KI2/view?usp=sharing

## Goal

Create a multi-class classification model that will correctly predict the genre of a song based off of its lyrical contents. 

## Use Case

The Music Industry is looking  to find top song writing talent in in the form of Machine Learning. They envision a future where a computer can write a hit song and have it tailored to a specific artist or genre. As a first step into that future we need to figure out if we can classify song to its correct genre solely on the lyrical content.

## DataSet

We gathered Data from two different sources:
 * Spotify API
 * WebScraping LyricWiki website

First we used the Spotify Api to collect a list of Artists as well as their Genre Classifications. We then used the LyricWiki Website to loop through the list of Artists and Scrape all of the links to their songs found on the site. Once again we looped through each link and scraped that page for the lyrics of the song. We also collected genre classifications for each Artist to fill in the missing values that we had from Spotify.


## EDA

When charting the top twenty most frequent uni-grams in each genre we discovered that there were many similar words being used between genres. The words were also very general and not very informative, in all of the unigrams the Hip-Hop/Rap genre was the only one to show a slight difference having a difference of two words from all other genres. 

We then moved on to Bigram and Trigram analysis and this is where we found that these groupings were even less informative. Songs tend to be very repetitive and that was on display for this type of analysis. The most frequent groupings of words were filled with repetitions of the same word, giving us no context as to what is being discussed in each genre. We tried to add more words to our stopwords list but we kept on getting different groupings of repetitive words. We feared that if we got rid of too many words it may have a negative impact on models performance.

![](/Visuals/trigrams.png)

## Feature Engineering

We were able to create quite a number of features for our dataset including number of lines, number of words, numper of words per line, unique words and use of explicit words in a song. For almost all of these features the Pop, Rock, and Country genre had the about the same distribution for each feature. The Hip-Hop genre far surpassed all other genres in almost every category with the only exception being number of words per line which it was comparatively similar to the Country genre

![](/Visuals/num_lines.png)

![](/Visuals/words_per_line.png)

![](/Visuals/unique_words.png)

## Classification Models

Our baseline model was a dummy classifier that we fit to our dataframe after we downsampled it to the minority class. This gave us an accuracy of 0.253 and an F-1 score of 0.242, we aim to create a model that will beat this baseline and generalize wel to unseen data. We fit three different types of models to our dataset, a Naive Bayes, Decision Tree, and a Random Forest. Through TF-IDF Vectorization we were able to fit a Naive Bayes model to our dataset that performed pretty good giving us an accuracy of 0.432 and an F-1 of 0.432. We were unable to fit a decision tree or random forest utilizing TF_IDF as the dataframe was far too big work with. We moved on to vectorizing our lyrics with Spacy, our best model seemed to be a Naive Bayes Model utilizing our engineered features as it gave us an F-1 of 0.569 and anf Accuracy of 0.397. This spread of scores seemed very suspect so we looked into the confusion matrix for further analysis. The confusion Matrix shows that for the most part we are choosing the Majority class which is Pop/R&B. This is the main reason why we are looking at F-1 and Accuracy score as we want to prioritze F-1 but also want to use accuracy as a second metric to validate that we are choosing the right model. In this case that accuracy was the same as the for the majority class. Moving on to the Random Forest we were able to find our best model giving us an F-1 score of 0.503 and and accuracy of 0.465.

![](/Visuals/classes.png)

## Text generator

Now that we have all of these lyrics we will use them to create a lyric generator based on genre. We will create a corpus of text for each genre which consists of 25,000 songs chosen at random. We will pass this corpus into an rnn utilizing LSTM .LSTM was chosen as it tends to be more accurate on larger datasets and we wanted to create more coherent lyrics. Finally we created an app to generate a song based off a given genre. At the current time you must download streamlit in order to run the generator, all files can be found in the text_gen_app folder. After you have all the files just navigate to the folder where you downloaded them and type ```streamlit run cap.py``` into the terminal. I am working on deploying this with heroku and hopefully it should be up soon.


## Conclusion

We were able to create a multiclass classification model which performs better than our baseline model, although we believe that this has lots of room for improvement. We were limitied in the amount of lyrics that we could get for copyright issues and if we had access to a broader set of lyrics with better genre classifications we may be able to vastly improve our model. For the future we would like to implement topic modeling to further our analysis of topics being discussed in each genre as N-gram analysis was not of much use. 

