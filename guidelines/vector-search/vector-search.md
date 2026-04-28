# Vector Search

## Principle

Atlas Vector Search enables semantic similarity search over high-dimensional vector embeddings stored in MongoDB. The ODM must expose Vector Search in a way that allows developers to perform nearest-neighbor queries without writing raw aggregation pipeline stages.

## Blueprint

1. **Vector Field Declaration:** The ODM must support declaring a field as a vector embedding field, specifying the number of dimensions and the similarity metric (`cosine`, `euclidean`, `dotProduct`) at the schema or model level.

2. **$vectorSearch Query API:** The ODM must provide an API for constructing `$vectorSearch` queries that accepts a query vector and returns results ranked by similarity. This must not require the user to write raw aggregation pipeline syntax for the common case.

3. **Index Configuration Awareness:** The ODM must document the requirement that an Atlas Vector Search index must exist on the vector field before queries can be executed. The ODM may optionally provide utilities to define or reference vector index configurations alongside the schema.

4. **numCandidates and limit:** The ODM must expose `$vectorSearch`'s `numCandidates` and `limit` parameters so that developers can tune the accuracy vs. performance tradeoff of their queries.

5. **Pre-filter Support:** The ODM must expose the `filter` option of `$vectorSearch` to allow hybrid queries that combine vector similarity with standard field-level filters.

6. **Score Exposure:** The vector similarity score (`vectorSearchScore`) must be accessible on query results to allow application-level relevance filtering or display.

7. **Embedding Integration Guidance:** The ODM documentation must describe how to generate and store vector embeddings (e.g., from a third-party model provider) and pass the resulting vector to the query API.
