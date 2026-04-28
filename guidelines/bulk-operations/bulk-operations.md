# Bulk Operations

## Principle

Bulk Operations allow users to execute multiple write operations in a single round trip to MongoDB. The ODM must expose this capability in a way that is efficient, idiomatic, and does not obscure the underlying driver's ordered/unordered execution model.

> Where an ODM does not support specific functionality described in this guideline, this will be called out on the respective ODM's page.

## Blueprint

1. **Batch Write Support:** The ODM must support grouped execution of insert, update, replace, and delete operations in a single call (e.g., `bulkWrite`, `insertMany`). Users should not be required to execute these as individual operations.

2. **Ordered and Unordered Execution:** The ODM must expose the ability to specify whether a bulk operation is ordered (stops on first error) or unordered (continues on error). The default behavior must be documented clearly.

3. **Result Reporting:** The result of a bulk operation must include counts of inserted, modified, deleted, and upserted documents, as well as any errors encountered during an unordered operation.

4. **Upsert Support:** Bulk update operations must support upsert semantics, where a document is inserted if no matching document is found.

5. **Error Handling:** Errors during bulk execution must be surfaced in a structured way that allows callers to identify which operations failed without obscuring the results of operations that succeeded.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | In Progress | — |
| EF Core | C# / .NET | Backlog | — |
| Spring Data MongoDB | Java | Backlog | — |
| Hibernate OGM | Java | Backlog | — |
| Doctrine MongoDB ODM | PHP | Backlog | — |
| Laravel MongoDB | PHP | Backlog | — |
| Mongoid | Ruby | Backlog | — |
| Django / MongoEngine | Python | Backlog | — |
