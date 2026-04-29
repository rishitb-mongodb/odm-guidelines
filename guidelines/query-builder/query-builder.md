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
| Mongoose | JavaScript / TypeScript | Done | — |
| EF Core | C# / .NET | Done | — |
| Spring Data MongoDB | Java | Backlog | — |
| Hibernate OGM | Java | Backlog | — |
| Doctrine MongoDB ODM | PHP | Backlog | — |
| Laravel MongoDB | PHP | Backlog | — |
| Mongoid | Ruby | Backlog | — |
| Django MongoDB Backend | Python | Done | Standard Django QuerySet API; `raw_aggregate()` for aggregation pipeline (requires `MongoManager`); `raw()`, `extra()`, `prefetch_related()`, `select_for_update()` not supported |
