# Index Management

## Principle

Index Management covers how an ODM exposes the creation and deletion of MongoDB indexes through the model or schema layer. The ODM should make it easy to declare indexes alongside the schema definition and provide a clear mechanism for applying them to the database on demand.

## Blueprint

1. **Declarative Index Definition:** Indexes must be definable at the schema or model level alongside the field definitions they apply to, rather than requiring separate imperative setup scripts.

2. **Index Types:** The ODM must support the full set of MongoDB index types relevant to the ODM's use cases, including: single-field, compound, text, sparse, TTL (time-to-live), unique, and geospatial indexes. Support for wildcard and partial indexes is recommended.

3. **On-Demand Index Creation:** The ODM should provide an explicit, developer-triggered mechanism to create declared indexes against the database. Automatic index creation at application startup should be approached with caution: if it forces recreation of all indexes, this is a very dangerous default for production environments and must not be the behaviour unless the developer has explicitly opted in. Index synchronisation (detecting and dropping indexes that are no longer declared) is not currently recommended — without named indexes there is no reliable way to associate a server-side index with a declared one, and silently dropping indexes risks significant data access regressions.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | Done | Declarative schema-level indexes; `syncIndexes()`, `ensureIndexes()`, `diffIndexes()` (dry-run); Atlas Search indexes via `createSearchIndex()` |
| EF Core | C# / .NET | Done | `HasIndex()` in `OnModelCreating()`; `HasCreateIndexOptions()` for MongoDB-specific options; indexes created only on `Database.EnsureCreated()`; geospatial indexes not supported |
| Spring Data MongoDB | Java | Done | `@Indexed`, `@CompoundIndex`, `@UniqueIndex` annotations; `IndexOperations` programmatic API; automatic index creation disabled by default since v3.0 |
| Hibernate OGM | Java | Backlog | No index support in public preview; workaround via raw `MongoClient`; all index types planned for GA |
| Doctrine MongoDB ODM | PHP | Done | `#[Index]`/`#[UniqueIndex]` PHP attributes; single-field, compound, text, TTL, geospatial, sparse, partial indexes; `SchemaManager` console commands |
| Laravel MongoDB | PHP | Done | Schema Builder with `index()`, `unique()`, `sparse()`, `ttl()`; compound and text indexes; geospatial indexes not explicitly documented |
| Mongoid | Ruby | Done | `index` macro; single-field, compound, unique, sparse, text, TTL, geospatial (2dsphere); `rake db:mongoid:create_indexes`; `search_index` macro for Atlas Search |
| Django MongoDB Backend | Python | Done | Single-field, compound, multikey, partial, unique, geospatial, and embedded indexes via `Meta.indexes`; `EmbeddedFieldIndex` for subfield indexes (v6.0.2+); `SearchIndex`/`VectorSearchIndex` for Atlas indexes; embedded/array field index updates not tracked by migrations |
