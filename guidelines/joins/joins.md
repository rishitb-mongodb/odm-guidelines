# Joins ($lookup)

## Principle

MongoDB's `$lookup` aggregation stage enables joining documents from different collections within a single query. The ODM should expose this capability in a way that feels natural alongside the rest of the query interface, without requiring users to write raw aggregation pipeline stages for common join patterns.

## Blueprint

1. **Idiomatic Join API:** The ODM should provide a high-level API for expressing `$lookup`-style joins that integrates with the query builder, rather than requiring users to drop directly to the aggregation pipeline for common use cases.

2. **Local and Foreign Key Configuration:** The ODM must allow the user to specify the local field, the foreign collection, and the foreign field for a join. For ODMs with a declared schema, this configuration may be inferred from relationship definitions where applicable.

3. **Pipeline-Based Lookups:** For advanced join scenarios (e.g., filtered or correlated joins), the ODM must allow users to specify a sub-pipeline within `$lookup`. This may require dropping to the aggregation pipeline level and must be documented clearly.

4. **Result Mapping:** The result of a join operation must be mapped back to a structured type in the host language. The ODM must document how joined documents are represented — whether as nested objects, separate result types, or flattened fields.

5. **Performance Guidance:** The ODM documentation must note that `$lookup` performs a join at query time and does not cache results. Guidance on using indexes on the joined collection's foreign key field should be included.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | Done | `$lookup` via `Model.aggregate()` pipeline; sub-pipeline option supported; results are POJOs |
| EF Core | C# / .NET | Backlog | Basic `Include()` for single navigation properties works; complex `Include().ThenInclude()` chains and `$lookup` sub-pipelines not yet supported |
| Spring Data MongoDB | Java | Done | `LookupOperation` in aggregation; correlated/uncorrelated subqueries; `let` variables; no high-level ORM-style join API |
| Hibernate OGM | Java | Backlog | `@OneToMany`/`@ManyToOne` not supported; `$lookup` only via `createNativeQuery()` with aggregation pipeline; planned for GA |
| Doctrine MongoDB ODM | PHP | Done | `$lookup` and `$graphLookup` in `AggregationBuilder`; cannot be used with `@DBRef` references |
| Laravel MongoDB | PHP | Done | `$lookup` via Aggregation Pipeline builder (v4.3+); correlated subquery syntax (MongoDB 5.0+) |
| Mongoid | Ruby | Done | `$lookup` via `Model.collection.aggregate([])` with raw array syntax; sub-pipeline option supported; no high-level DSL |
| Django MongoDB Backend | Python | Done | Relational fields (`ForeignKey`/`OneToOneField`/`ManyToManyField`) generate `$lookup` implicitly; custom `$lookup` via `raw_aggregate()`; `$lookup` flagged as slow — prefer embedded models |
