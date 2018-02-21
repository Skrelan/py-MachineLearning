# Python Machine Learning boilerplate w/ docker

# Machine learning

### what is ML?
A branch of AI, when code learns from examples and experience.


----

# Python Pipeline boilerplate w/ docker
## Goal of this Pipeline?
Poorly formatted data exists in the wild, especially Financial data and this kind of data is generally spread across the space, some of it on Financial Exchanges some of it in the Treasury website. We need to format this data into a structure so that we perform some calculations on it.

## Steps
* Download data
* Parse data
* Store data
* Clean data

## Libraries
* requests
* concurrent futures
* python tokenize / BeautifulSoup
* regular expression
* celery (tasks for download,parse,cleanse will be managed via this)
* sqlAlchemy


Inspiration from : https://www.youtube.com/watch?v=AlkuzBbiKk0
