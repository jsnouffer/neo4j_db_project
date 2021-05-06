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

__Delete all nodes__
```
MATCH (n) DETACH DELETE n;
```

__Visualize database schema__
```
CALL db.schema.visualization();
```

__Summarize relationships__
```
MATCH (n)
OPTIONAL MATCH (n)-[r]->(x)
WITH DISTINCT {l1: labels(n), r: type(r), l2: labels(x)}
AS `first degree connection`
RETURN `first degree connection`;
```
