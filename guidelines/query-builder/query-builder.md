# Query Builder

## Principle

The Query Builder is the core abstraction for users interacting with MongoDB through the ODM. It must prioritize an intuitive, idiomatic developer experience that feels natural within the host language and framework.

## Blueprint

1. **Idiomatic Querying:** The ODM should enable developers to express database queries using the host language's native constructs (e.g., LINQ in C#, method chaining in Node.js) rather than requiring them to write raw MQL.

2. **Aggregation Access:** The query interface must provide a clear path for constructing and executing MongoDB's Aggregation Pipeline, translating high-level ODM operations into efficient pipeline stages where necessary.

3. **Extensibility (Escape Hatch):** A mechanism must be available to allow advanced users to bypass the Query Builder and drop directly to the underlying driver or native MQL. This ensures full access to MongoDB features that may not be supported by the ODM's abstraction layer.

4. **Type System Leverage:** The ODM should take advantage of the host language's type system where possible to ensure semantic correctness of queries and to leverage suitable defaults based on those language types.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | Done | Method chaining; Aggregation Pipeline via `Model.aggregate()`; aggregation results are POJOs |
| EF Core | C# / .NET | Done | Full LINQ translation; `Mql.Exists()`, `Mql.IsMissing()`, `Mql.IsNullOrMissing()` helpers |
| Spring Data MongoDB | Java | Done | Fluent `Criteria` API, `MongoTemplate`, repository query derivation, `@Query` annotation for native JSON |
| Hibernate OGM | Java | Done | HQL/JPQL and Criteria API; native MQL via `createNativeQuery()`; `$project` stage mandatory with explicit field listing |
| Doctrine MongoDB ODM | PHP | Done | Fluent `QueryBuilder`; `Criteria` API; `AggregationBuilder`; PHP type auto-configuration (v2.4+) |
| Laravel MongoDB | PHP | Done | Full Eloquent query builder; Aggregation Pipeline builder (v4.3+); raw driver access via `DB::getMongoClient()` |
| Mongoid | Ruby | Done | Chainable Criteria DSL; Aggregation Pipeline via `Model.collection.aggregate([])`; limited DSL for aggregation beyond `$group`/`$project`/`$unwind` |
| Django MongoDB Backend | Python | Done | Standard Django QuerySet API; `raw_aggregate()` for aggregation pipeline (requires `MongoManager`); `raw()`, `extra()`, `prefetch_related()`, `select_for_update()` not supported |
