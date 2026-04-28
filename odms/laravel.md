# Laravel MongoDB

**Language / Ecosystem:** PHP / Laravel
**Repository:** [mongodb/laravel-mongodb](https://github.com/mongodb/laravel-mongodb)

Laravel MongoDB is a MongoDB-maintained package that extends the Laravel Eloquent ORM to support MongoDB. It allows developers to use Laravel's standard model, query builder, and relationship APIs with MongoDB as the backing database, without switching to a different programming model.

## Guidelines Triage

| Feature | Triage Status |
|---------|---------------|
| [Query Builder](../guidelines/query-builder/query-builder.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Full Eloquent query builder integration with method chaining; Aggregation Pipeline builder (v4.3+); raw driver access via `DB::getMongoClient()` and `raw()` method |
| [Bulk Operations](../guidelines/bulk-operations/bulk-operations.md) | ![In Progress](https://img.shields.io/badge/In_Progress-yellow?style=flat) — `insert()` for batch inserts; `upsert()` for batch upserts (v4.7+); native ordered/unordered `BulkWrite` API not exposed — issues #500 and #733 open since 2015–16; attribute casting skipped on bulk insert |
| [Relationship Mapping](../guidelines/relationship-mapping/relationship-mapping.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `hasOne`, `hasMany`, `belongsTo`, `embedsOne`, `embedsMany`; polymorphic relationships added (PR #2608); embedded documents returned as raw objects unless `$with` used for hydration |
| [Index Management](../guidelines/index-management/index-management.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Schema Builder with `index()`, `unique()`, `sparse()`, `ttl()`; compound and text indexes; geospatial indexes not explicitly documented |
| [Transactions](../guidelines/transactions/transactions.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `DB::transaction()` callback; manual session API; requires replica set or sharded cluster; no nested transactions |
| [BSON Data Type Support](../guidelines/bson-data-types/bson-data-types.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — ObjectId, Carbon/DateTime (v5.0+ auto-converts BSON UTC DateTime to Carbon); Decimal128, UUID via PHP driver; nested array dates not automatically cast to Carbon (issues #1252, #902) |
| [Array Fields](../guidelines/array-fields/array-fields.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Array field storage; `$in`, `$all`, `$elemMatch`, `$size` via query builder; `$push`, `$pull`, `$addToSet`, `$pop` via MongoDB driver |
| [Embedded Fields](../guidelines/embedded-fields/embedded-fields.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `embedsOne`/`embedsMany`; dot notation querying; `$set` partial updates; no built-in nested field validation — requires manual implementation |
| [Polymorphic Array/Embedded Fields](../guidelines/polymorphic-fields/polymorphic-fields.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `morphTo`/`morphMany` recently added (PR #2608); `*_type`/`*_id` discriminator pattern; documentation still being developed (issue #2696) |
| [Security Features (CSFLE & QE)](../guidelines/security-features/security-features.md) | ![Won't Do](https://img.shields.io/badge/Won't_Do-red?style=flat) — No Laravel-level CSFLE or QE integration; must be configured at PHP driver level |
| [Joins ($lookup)](../guidelines/joins/joins.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `$lookup` via Aggregation Pipeline builder (v4.3+); correlated subquery syntax (MongoDB 5.0+); no Eloquent join method |
| [Atlas Search](../guidelines/atlas-search/atlas-search.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Native `search()` and `autocomplete()` query builder methods (v5.2+); `createSearchIndex()` schema helper; Laravel Scout integration; Atlas only |
| [Vector Search](../guidelines/vector-search/vector-search.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Native `vectorSearch()` query builder method (v5.2+); `createSearchIndex()` for vector indexes; Atlas only |
| [Logging](../guidelines/logging/logging.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `DB::listen()` for query logging; Laravel logging integration; no built-in slow query logger — requires custom middleware |
| [Escape Hatch](../guidelines/escape-hatch/escape-hatch.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `raw()` method on models and query builder; `DB::getMongoClient()` and `DB::getMongoDB()` for direct driver access; session passthrough |
| [Performance Benchmarks](../guidelines/performance-benchmarks/performance-benchmarks.md) | ![Backlog](https://img.shields.io/badge/Backlog-lightgrey?style=flat) |
