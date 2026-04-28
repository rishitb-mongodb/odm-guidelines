# Array Fields

## Principle

Arrays are a fundamental part of MongoDB's document model. The ODM must expose the full power of MongoDB's array query and update operators while keeping the developer experience idiomatic and avoiding the need to drop to raw MQL for common array operations.

## Blueprint

1. **Array Field Declaration:** The ODM must support declaring a field as an array of a given type at the schema or model level, including arrays of primitives, embedded documents, and references.

2. **Array Query Operators:** The ODM must expose MongoDB's array query operators, including `$in`, `$all`, `$elemMatch`, and `$size`, through the query builder or an equivalent idiomatic API.

3. **Array Update Operators:** The ODM should expose MongoDB's array update operators, including `$push`, `$pull`, `$addToSet`, `$pop`, and the positional operators (`$`, `$[]`, `$[<identifier>]`), for modifying array contents without replacing the entire document. Note that these operations are highly unlikely to be achievable safely in most ODMs without concurrency controls (e.g., version tokens or timestamps), as concurrent modifications to the same array can produce invalid or conflicting state.

4. **Array Filters:** The ODM should support MongoDB's `arrayFilters` option for targeted updates to specific array elements. The same concurrency caveats as bullet 3 apply.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | Backlog | — |
| EF Core | C# / .NET | Backlog | — |
| Spring Data MongoDB | Java | Backlog | — |
| Hibernate OGM | Java | Backlog | — |
| Doctrine MongoDB ODM | PHP | Backlog | — |
| Laravel MongoDB | PHP | Backlog | — |
| Mongoid | Ruby | Backlog | — |
| Django / MongoEngine | Python | Backlog | — |
