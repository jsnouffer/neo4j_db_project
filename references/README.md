# References for NEO4J_DB_PROJECT

## Graph Database References

- 2015 [O'Reilly's Graph Databases, 2nd Edition textbook](https://www.oreilly.com/library/view/graph-databases-2nd/9781491930885/)
- 2008 [A_comparison_of_a_graph_database_and_a_relational_database](A_comparison_of_a_graph_database_and_a_relational_.pdf)
- [foam VSCode graph knowledge plugin](https://github.com/foambubble/foam)
- [Bloor Graph Database Market Update 2020](https://info.cambridgesemantics.com/bloor-graph-database-market-update-2020)

## Presentation (4/20/2021)

[Power point](https://asrcfederal-my.sharepoint.com/:p:/r/personal/rneely_asrcfederal_com/_layouts/15/Doc.aspx?sourcedoc=%7BC9DB4015-CE74-4AB7-94C6-FCDA9AF5F944%7D&file=adb_graph_db.pptx&action=edit&mobileredirect=true&cid=64984701-5f9e-4d94-b748-de53197c165c)

### Graph Databases – What they are and why we need them (Jonathan)​

### Neo4j – Introduction, Cypher and Visualization (Kevin)​

### Neo4j – top 10 use cases (Jason)​

Examples

- fraud detection
    - traditional: discrete analysis - patterns and trends
    - graphdb: pull back an look a relationships
- recommender engine
- natural language processing
- etc.

### Neo4j – monitoring with Prometheus and Grafana (Ron)​

- Prometheus and Grafana did not work for our project
    - Our project used the free community version of Neo4j
        - Neo4j enterprise version required to support Prometheus
    - Prometheus is for monitoring Kubernetes Pods or multiple docker containers in Docker Swarm
        - our project only ran only a single docker container
- Halin provides a FOSS approach to monitoring the community version of Neo4j
Halin article: https://medium.com/neo4j/monitoring-neo4j-with-halin-4c11429b46ff
Halin repo: https://github.com/moxious/halin

## Project / APIs

### YouTube (Jonathon)

### HackerNews (Ron)

Use [neomodel](https://neomodel.readthedocs.io/en/latest/getting_started.html) import into Neo4j.

Hacker News is Ycombinator Entrepreneur message board.

- [Hacker News/API](https://github.com/HackerNews/API)
- [algolia.com **hn** search api](https://hn.algolia.com/api) from [dzone article](https://dzone.com/articles/algolia-kindly-provides-a-hacker-news-search-api)

View results with https://jsonformatter.org/ 

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


#### agolia only get 20 results max

https://stackoverflow.com/questions/35928272/algolia-hacker-news-search-api-browse-endpoint

May have to directly scrape hn api, i.e. story 8201362:

https://hacker-news.firebaseio.com/v0/item/8201362.json?print=pretty

{
  "by" : "jonbaer",
  "descendants" : 109,
  "id" : 8201362,
  "kids" : [ 8202085, 8201610, 8202130, 8203225, 8201504, 8202234, 8201657, 8202090, 8201499, 8201553, 8201425, 8201733, 8202160, 8201517, 8203149, 8202301, 8203422, 8202521, 8201611, 8203029, 8201842, 8201502, 8205837, 8209198, 8201570, 8201546, 8202185, 8203541, 8201772, 8203503, 8201524, 8201454, 8202732, 8202953, 8201580, 8201547 ],
  "score" : 831,
  "time" : 1408518640,
  "title" : "Fully Functional 1KB Hard Drive in Vanilla Minecraft",
  "type" : "story",
  "url" : "http://imgur.com/a/NJBuH"
}

comment 8202085

https://hacker-news.firebaseio.com/v0/item/8202085.json?print=pretty

{
  "by" : "TheLoneWolfling",
  "id" : 8202085,
  "kids" : [ 8203534, 8202863, 8202964, 8202833 ],
  "parent" : 8201362,
  "text" : "In recent versions of MC, you can do a much better delay line memory with comparators. You can actually end up being able to store 2b &#x2F; block (2 and not 4 because comparators have to be placed on something not a comparator.) - it would be half that but there&#x27;s a trick you can play to avoid requiring redstone dust between comparators.<p>The delay is faster too - 1 redstone tick &#x2F; 4 bits, or 40 bits&#x2F;sec per line, as opposed to this implementation&#x27;s 1 bit &#x2F; 8 redstone ticks &#x2F; line, or 1.25 bits &#x2F; sec &#x2F; line. (Note that this implementation of piston tape is decidedly suboptimal: the maximum is actually 3 bits &#x2F; 4 redstone ticks &#x2F; line = 7.5 bits&#x2F;sec&#x2F;line, as you can actually check for 8 different block types (glass &#x2F; solid &#x2F; sticky&#x2F;non-sticky piston facing 3 directions) and you can make a faster-resetting piston loop.)<p>The biggest issue with comparator delay-line memory is that there&#x27;s no way of pausing it.<p>There&#x27;s also a way of storing arbitrary amounts of data per block, and that&#x27;s to use the fact that items with NBT data will stack only when their NBT data is identical. The easiest way to see this is to try to stack renamed items, but there are others. You can make a hopper or dropper chain and encode data in which line which enchanted item is in.<p>I have yet to see a practical implementation of the above, though.",
  "time" : 1408538913,
  "type" : "comment"
}

author:speedcoder

https://hacker-news.firebaseio.com/v0/user/speedcoder.json?print=pretty

{
  "created" : 1584957453,
  "id" : "speedcoder",
  "karma" : 3,
  "submitted" : [ 26765657, 26739804, 26561262, 26557895, 26382557, 26050359, 25947844, 25365088, 23726509, 23726508, 23723990, 22662462, 22662458 ]
}



Via https://github.com/HackerNews/API .

https://firebase.google.com/docs/libraries/




### Reddit (Jason)

Check out 'jason' branch on our github.

- adds relationships into Neo4j
- uses redis to queue and download via multiple threads
- redis not reddit
  - redis is an in-memory key:node value mapper with queue
    - helps with multi-threading downloads
- src/reddit/data_model.py 
    - add_relationships() - adds relationships between between redditor and subredit 
- utils.py does a recursion
    - look for duplicate nodes when adding data
        - i.e. make sure node doesn't already exist before adding a new node

### Speedrunner (Kevin)

