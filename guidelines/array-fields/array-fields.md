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
| Mongoose | JavaScript / TypeScript | Done | `[SchemaType]` declaration; `$in`, `$all`, `$elemMatch`, `$size`; `$push`, `$pull`, `$addToSet`, `$pop`, positional operators, `arrayFilters` all supported |
| EF Core | C# / .NET | Done | `string[]`, `List<T>`, `ICollection<T>`, `Dictionary<K,V>`; basic LINQ array operators; advanced update operators (`$push`, `$arrayFilters`) require driver-level access |
| Spring Data MongoDB | Java | Done | Native `List<T>` mapping; `$in`, `$all`, `$elemMatch`, `$size` via Criteria; `$push`, `$pull`, `$pop`, `$position`, `$slice`, `arrayFilters` via `Update` |
| Hibernate OGM | Java | Done | `@ElementCollection`; `List`/`Set`/`Map` via `@Embeddable`/`@Struct`; array query operators via HQL/JPQL; advanced update operators require native queries |
| Doctrine MongoDB ODM | PHP | Done | `collection`/`hash` field types; multiple storage strategies; `$push`, `$pull`, `$addToSet`, `$pop`; `arrayFilters` support not fully documented in QueryBuilder |
| Laravel MongoDB | PHP | Done | Array field storage; `$in`, `$all`, `$elemMatch`, `$size`; `$push`, `$pull`, `$addToSet`, `$pop` via MongoDB driver |
| Mongoid | Ruby | Done | `Array` field type; `$in`, `$all`, `$elemMatch`, `$size` via Criteria; `$push`, `$pull`, `$addToSet`, `$pop` require raw collection access |
| Django MongoDB Backend | Python | Done | `ArrayField` (scalar) and `EmbeddedModelArrayField` (embedded models); lookups: `contains`, `contained_by`, `overlap`, `len`; index and slice querying on embedded model arrays; relational fields cannot be used as `ArrayField` base type |
