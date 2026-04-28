# Mongoose

**Language / Ecosystem:** Node.js / JavaScript (and TypeScript)
**Repository:** [Automattic/mongoose](https://github.com/Automattic/mongoose)

Mongoose is a MongoDB ODM for Node.js that provides schema-based modeling, validation, query building, and middleware hooks on top of the official Node.js driver. It is one of the most widely used MongoDB ODMs across all ecosystems.

## Guidelines Triage

| Feature | Triage Status |
|---------|---------------|
| [Query Builder](../guidelines/query-builder/query-builder.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Method chaining, Criteria DSL, full Aggregation Pipeline access via `Model.aggregate()`; aggregation results are POJOs, not hydrated Mongoose documents |
| [Bulk Operations](../guidelines/bulk-operations/bulk-operations.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `Model.bulkWrite()` and `Model.insertMany()` supported; ordered/unordered modes inherit MongoDB driver defaults |
| [Relationship Mapping](../guidelines/relationship-mapping/relationship-mapping.md) | ![Won't Do](https://img.shields.io/badge/Won't_Do-red?style=flat) — Mongoose's `populate()` covers reference-based relationships idiomatically; a prescriptive guideline would conflict with its established conventions |
| [Index Management](../guidelines/index-management/index-management.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Declarative schema-level indexes; `syncIndexes()`, `ensureIndexes()`, `diffIndexes()` (dry-run); Atlas Search indexes via `createSearchIndex()`; use `diffIndexes()` before `syncIndexes()` in production |
| [Transactions](../guidelines/transactions/transactions.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `startSession()`, `withTransaction()` callback API, manual `startTransaction()`/`commitTransaction()`/`abortTransaction()`; no nested transactions on same session; no `Promise.all()` inside transactions |
| [BSON Data Type Support](../guidelines/bson-data-types/bson-data-types.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — ObjectId, Decimal128, UUID (subtype 4 default since v9.0), BigInt for Int64; no timezone handling at schema level — developer responsibility |
| [Array Fields](../guidelines/array-fields/array-fields.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `[SchemaType]` declaration; `$in`, `$all`, `$elemMatch`, `$size` via query methods; `$push`, `$pull`, `$addToSet`, `$pop`, positional operators, `arrayFilters` all supported |
| [Embedded Fields](../guidelines/embedded-fields/embedded-fields.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Nested schema declaration; dot notation querying; `$set` partial updates; nested validation via `runValidators: true`; schema reuse; care needed with `minimize` option on dot notation updates |
| [Polymorphic Array/Embedded Fields](../guidelines/polymorphic-fields/polymorphic-fields.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `Schema.discriminator()` with configurable key (default `__t`); embedded discriminators in arrays supported |
| [Security Features (CSFLE & QE)](../guidelines/security-features/security-features.md) | ![Backlog](https://img.shields.io/badge/Backlog-lightgrey?style=flat) — No schema-level CSFLE or QE integration; 12+ open GitHub issues; QE enhancement #14516 open as of April 2024; users must configure via driver's `autoEncryption` directly |
| [Joins ($lookup)](../guidelines/joins/joins.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `$lookup` via `Model.aggregate()` pipeline; sub-pipeline option supported; results are POJOs |
| [Atlas Search](../guidelines/atlas-search/atlas-search.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — `$search` via aggregation pipeline; index managed via `createSearchIndex()`; incompatible with `autoEncryption` (issue #12660) |
| [Vector Search](../guidelines/vector-search/vector-search.md) | ![In Progress](https://img.shields.io/badge/In_Progress-yellow?style=flat) — TypeScript types merged (PR #14428); no dedicated `$vectorSearch` aggregate method; must use raw stage; Community Server support in development (enhancement #15645) |
| [Logging](../guidelines/logging/logging.md) | ![In Progress](https://img.shields.io/badge/In_Progress-yellow?style=flat) — Debug callback via `connection.set('debug', fn)` for command logging; no slow query detection, no structured output, no driver log passthrough |
| [Escape Hatch](../guidelines/escape-hatch/escape-hatch.md) | ![Done](https://img.shields.io/badge/Done-brightgreen?style=flat) — Raw collection via `Connection.prototype.collection()`; raw DB aggregation via `Connection.prototype.aggregate()`; `getClient()` for MongoClient; no automatic result mapping to Mongoose docs |
| [Performance Benchmarks](../guidelines/performance-benchmarks/performance-benchmarks.md) | ![Backlog](https://img.shields.io/badge/Backlog-lightgrey?style=flat) |
