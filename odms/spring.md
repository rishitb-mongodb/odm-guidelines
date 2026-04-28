# Spring Data MongoDB

**Language / Ecosystem:** Java / Spring Framework
**Repository:** [spring-projects/spring-data-mongodb](https://github.com/spring-projects/spring-data-mongodb)

Spring Data MongoDB is a Spring Framework module that provides repository abstractions, query derivation, and mapping support for MongoDB. It integrates with the broader Spring Data ecosystem and supports both the imperative and reactive MongoDB Java drivers.

## Guidelines Triage

| Feature | Triage Status |
|---------|---------------|
| [Query Builder](../guidelines/query-builder/query-builder.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Fluent `Criteria` API, `MongoTemplate`, repository query derivation, `@Query` annotation for native JSON, full Aggregation Pipeline support |
| [Bulk Operations](../guidelines/bulk-operations/bulk-operations.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `BulkOperations` API with `ORDERED`/`UNORDERED` modes; insert, update, upsert, replace, remove; reactive `ReactiveBulkOperations`; optimistic locking (`@Version`) not supported in bulk operations |
| [Relationship Mapping](../guidelines/relationship-mapping/relationship-mapping.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `@DBRef` (lazy/eager) and `@DocumentReference` (preferred since 3.3); lazy loading of DBRef collections across multiple collections resolves one-by-one (N+1 risk); bulk loading recommended for same-collection refs |
| [Index Management](../guidelines/index-management/index-management.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `@Indexed`, `@CompoundIndex`, `@UniqueIndex` annotations; `IndexOperations` programmatic API; automatic index creation disabled by default since Spring Data 3.0 |
| [Transactions](../guidelines/transactions/transactions.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `@Transactional` via `MongoTransactionManager` since v2.1; `TransactionTemplate` for manual control; requires MongoDB 4.0+ replica set; some known issues with reactive transactions (issue #4804) |
| [BSON Data Type Support](../guidelines/bson-data-types/bson-data-types.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — ObjectId, Decimal128 via `BigDecimal`, UUID (must configure representation explicitly); `BigDecimal`/`BigInteger` representation defaults changed in 5.0; custom converters supported |
| [Array Fields](../guidelines/array-fields/array-fields.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Native `List<T>` mapping; `$in`, `$all`, `$elemMatch`, `$size` via Criteria; `$push`, `$pull`, `$pop`, `$position`, `$slice` via `Update`; `arrayFilters` via `filterArray()` |
| [Embedded Fields](../guidelines/embedded-fields/embedded-fields.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Automatic nested object mapping; dot notation in queries and updates; nested field path strings require manual construction (no compile-time type safety) |
| [Polymorphic Array/Embedded Fields](../guidelines/polymorphic-fields/polymorphic-fields.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `_class` discriminator field added automatically; `@TypeAlias` for stable schema evolution; class name or package refactoring breaks existing documents without `@TypeAlias` |
| [Security Features (CSFLE & QE)](../guidelines/security-features/security-features.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — CSFLE since v4.2; Queryable Encryption since v5.0; CSFLE and QE cannot be used in the same collection; QE adds `__safeContent__` field to documents |
| [Joins ($lookup)](../guidelines/joins/joins.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `LookupOperation` in aggregation; correlated/uncorrelated subqueries; `let` variables; no high-level ORM-style join API — requires aggregation pipeline knowledge |
| [Atlas Search](../guidelines/atlas-search/atlas-search.md) | ![Backlog](https://img.shields.io/badge/Backlog-lightgrey?style=flat) — No native `$search` integration; workaround via custom `AggregationOperation`; GitHub issue #3831 open |
| [Vector Search](../guidelines/vector-search/vector-search.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `@VectorSearch` annotation and `VectorSearchOperation` since v4.5.0; relevance scores returned; Atlas only |
| [Logging](../guidelines/logging/logging.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — SLF4J integration via `org.springframework.data.mongodb.core.MongoTemplate` logger; MongoDB driver command logging via `org.mongodb.driver.protocol.command`; no built-in slow query threshold — relies on server-side profiling |
| [Escape Hatch](../guidelines/escape-hatch/escape-hatch.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `BasicQuery` for raw JSON; `@Query` for native queries in repository methods; `MongoTemplate` callbacks for direct driver access |
| [Performance Benchmarks](../guidelines/performance-benchmarks/performance-benchmarks.md) | ![Backlog](https://img.shields.io/badge/Backlog-lightgrey?style=flat) |
