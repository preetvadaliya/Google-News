<h1 align = "center">
  G O O G L E &nbsp;&nbsp; N E W S
  <br>
  <img src="https://img.shields.io/static/v1?label=Made%20with&message=Python&color=red&logo=python&logoColor=white" />
  <img src="https://img.shields.io/static/v1?label=Python&message=3.7.7&color=red&logo=python&logoColor=white" />
  <img src="https://img.shields.io/static/v1?label=Use%20of&message=Web%20Scraping&color=red&logo=google-chrome&logoColor=white" />
  <img src="https://img.shields.io/static/v1?label=Made%20with&message=BeautifulSoup&color=red" />
</h1>
<p align="center">Simple News app built in Python using Beautiful-soup web scraping.</p>

<br>
<br>

### How to use?
Download **GoogleNews.py** file and add into your project.

<br>
<br>

### How to get user agent?
Search **my user agent** into your chrome.

<br>
<br>

## E X A M P L E
```python

from GoogleNews import GoogleNews
news = GoogleNews("your user agent")

```

<br>
<br>

## M E T H O D S

### getTopStories( )
return top stories headlines from Google News.
```python

news.getTopStories()

```

<br>

### getForYou( )
return headlines recommended based on your interests.
```python

news.getForYou()

```

<br>

### getCoronaNews( )
return headlines of corona news.
```python

news.getCoronaNews()

```

<br>

### getCountryNews( )
return headlines of your country.
```python

news.getCountryNews()

```

<br>

### getWorldNews( )
return headlines of world.
```python

news.getWorldNews()

```

<br>

### getTechnologyNews( )
return headlines of technology.
```python

news.getTechnologyNews()

```

<br>

### getEntertainmentNews( )
return headlines of entertainment.
```python

news.getEntertainmentNews()

```

<br>

### getSportsNews( )
return headlines of sports.
```python

news.getSportsNews()

```

<br>

### getScienceNews( )
return headlines of science.
```python

news.getScienceNews()

```

<br>

### getHealthNews( )
return headlines of health.
```python

news.getHealthNews()

```