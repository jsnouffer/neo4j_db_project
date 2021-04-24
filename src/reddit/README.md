## Neo4j Cypher Queries

__Count all nodes__
```
MATCH (n) RETURN count(n) as count;
```

__Count all relationships__
```
MATCH ()-[r]->()
RETURN count(r) as count;
```

__Retrieve all__
```
MATCH (n) RETURN n;
```

__Retrieve all with limit__
```
MATCH (n) RETURN n LIMIT 25;
```

__Retrieve highly connected graph__
```
MATCH (a)-[:INTERACTED]->(b) RETURN b;
```
```
MATCH (a)-[:SUBMITTER]->(b) RETURN a,b;
```

__Find most connected nodes__
```
MATCH (a)-[:SUBMITTER]->(b)
RETURN b, COLLECT(a) as Redditor
ORDER BY SIZE(Redditor) DESC LIMIT 10;
```
```
MATCH (a)-[:INTERACTED]->(b)
RETURN b, COLLECT(a) as Redditor
ORDER BY SIZE(Redditor) DESC LIMIT 10;
```

__Retrieve highly connected graph w/ Submission nodes__
```
MATCH (x)-[:SUBMITTER]->(p)
CALL {
  MATCH (a)-[:INTERACTED]->(b)
  RETURN a,b
  LIMIT 500
}
RETURN p,a,b,x;
```