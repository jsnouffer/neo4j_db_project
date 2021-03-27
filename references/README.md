# References for NEO4J_DB_PROJECT

## Graph Database References

- 2015 [O'Reilly's Graph Databases, 2nd Edition textbook](https://www.oreilly.com/library/view/graph-databases-2nd/9781491930885/)
- 2008 [A_comparison_of_a_graph_database_and_a_relational_database](A_comparison_of_a_graph_database_and_a_relational_.pdf)
- [foam VSCode graph knowledge plugin](https://github.com/foambubble/foam)
- [Bloor Graph Database Market Update 2020](https://info.cambridgesemantics.com/bloor-graph-database-market-update-2020)

## APIs

### Reddit (Jason)

### YouTube (Jonathon)

### HackerNews (Ronald)

Hacker News is Ycombinator Entrepreneur message board.

- [Hacker News/API](https://github.com/HackerNews/API)
- [algolia.com **hn** search api](https://hn.algolia.com/api) from [dzone article](https://dzone.com/articles/algolia-kindly-provides-a-hacker-news-search-api)

Examples # https://jsonformatter.org/ can be used to pretty print json results

    # hn stories on minecraft
    curl https://hn.algolia.com/api/v1/search?query=minecraft
    # will return hits, each hit will either have a url or story text, i.e.
    # hits[0]["url"]["value"]
    # hits[0]["story_text"]
    # much of the text is encoded for urls, i.e. requests.utils.quote or urllib.parse.quote
    # these can be unquoted via [urllib.parse.unquote](https://docs.python.org/3.8/library/urllib.parse.html#urllib.parse.unquote)

    # hn stories on ~ 3/10/2021 
    curl https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i>1615332811,created_at_i<1615419211
    curl https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i%3E1615332811,created_at_i%3C1615419211
    # above relies on int unix seconds timestamp, i.e.
    # python -c "import datetime;print(int(datetime.datetime.now().timestamp()));"

    # hn stories on ~ 3/10/2021 about minecraft
    curl https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i>1615332811,created_at_i<1615419211&query=minecraft
    # above returns "hits" json with an entry for each story

    # author for story can be taken from hits[0]["author"], i.e. "lawrenceyan"
    curl https://hn.algolia.com/api/v1/users/lawrenceyan
    # funfact: my hn user 'speedcoder' info
    curl https://hn.algolia.com/api/v1/users/speedcoder

    # story number can be taken from hits[0]["objectID"], i.e. "26415048"
    # comments for the story can then be queried
    # comments for story_x
    # http://hn.algolia.com/api/v1/search?tags=comment,story_X, i.e.
    http://hn.algolia.com/api/v1/search?tags=comment,story_26415048
    # the comments come back in 1 big hits array with each hit a comment
    # each author of a comment can be retrieved via hits[0]["author"]
    # text of comment can be retrieved via hits[0]["comment_text"]

### Speedrunner (Kevin)
