# news_flagger 

This repository contains the code for flaggin false news articles using a machine learning model and some not so genious techniques. It uses a similarity measure to compare the articles with a set of known true article and then generate a score based on the similarity. The articles are then flagged based on the score. It uses multiple articles to generate a score for each article and then uses a threshold to flag the articles.

## Usage
This can be used to flag articles in a news feed or any other source of articles. 

While testing the code, I used the following articles:
- [Bidya Bhandari’s political adventurism hits a brake—for now](https://kathmandupost.com/politics/2025/07/23/bidya-bhandari-s-political-adventurism-hits-a-brake-for-now)

and to measure the similarity, I used the following articles:
- [Bidya Bhandari intensifying party activities](https://en.setopati.com/political/164318)
- [Former Prez Bhandari defends her UML membership](https://mypeoplesreview.com/2025/07/26/former-prez-bhandari-defends-her-uml-membership/)
- [Chair Oli toughens stance; Bhandari barred from party politics](https://mypeoplesreview.com/2025/07/24/chair-oli-toughens-stance-bhandari-barred-from-party-politics/)

These articles provide with similar context and can be used to measure the similarity of the articles. But these articles are not too similar to the original article. So they provide a good test case for the model. These articles are used to generate a score for the original article and then the score is used to flag the article. The final score was `0.578` which is above the threshold of `0.5` and hence the article was flagged as true news.

Note: The threshold used in this project doesnot signify any scientific measure. It is just a random number that I used to flag the articles. You can change the threshold based on your requirements.

## Installation
To run this project, first clone the repository and then install the required packages using pip.

```bash
git clone https://github.com/raichu03/news_flagger
```
The navigation to the project directory and install the required packages using pip.

```bash
cd news_flagger
pip install -r requirements.txt
```

To run the web searh api you will need to have the valid google search api key and the custom search engine id. Once you have the key and id, create a `.env` file in the root directory of the project and add the following lines:

```
SEARCH_KEY=<your_search_key>
SEARCH_ID=<your_search_id>
```

Then you can add the link to the article you want to flag in the `main.py` file and run the following command to start the web server:

```bash
python main.py
```

Note: The code currently only supports articles from the Kathmandu Post. You can modify the code to support other news websites.