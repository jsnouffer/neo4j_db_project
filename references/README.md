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

Examples

    curl https://hn.algolia.com/api/v1/search?query=minecraft

    # hn stories on ~ 3/10/2021
    curl http://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i>1615332811,created_at_i<1615419211

    # hn stories on ~ 3/10/2021 about minecraft
    curl https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i%3E1615332811,created_at_i%3C1615419211&query=minecraft

    # user 'speedcoder' info
    curl https://hn.algolia.com/api/v1/users/speedcoder

    # comments for story_x
    http://hn.algolia.com/api/v1/search?tags=comment,story_X

### Speedrunner (Kevin)
