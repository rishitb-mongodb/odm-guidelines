# Index Management

## Principle

Index Management covers how an ODM exposes the creation, synchronization, and deletion of MongoDB indexes through the model or schema layer. The ODM should make it easy to declare indexes alongside the schema definition and provide a clear mechanism for keeping the database state in sync.

## Blueprint

1. **Declarative Index Definition:** Indexes must be definable at the schema or model level alongside the field definitions they apply to, rather than requiring separate imperative setup scripts.

2. **Index Types:** The ODM must support the full set of MongoDB index types relevant to the ODM's use cases, including: single-field, compound, text, sparse, TTL (time-to-live), unique, and geospatial indexes. Support for wildcard and partial indexes is recommended.

3. **Index Synchronization:** The ODM must provide a mechanism to synchronize declared indexes with the MongoDB database (e.g., `syncIndexes`, `ensureIndexes`). The behavior of this operation — including whether it drops and recreates existing indexes — must be clearly documented.

4. **Startup vs. On-Demand Sync:** The ODM must document whether indexes are automatically synchronized at application startup or only when explicitly triggered, and must allow the developer to control this behavior.

5. **Background Index Creation:** Where the underlying MongoDB version supports it, index creation must not block the collection during synchronization. The ODM must pass through the appropriate driver options to enable this.
