# Array Fields

## Principle

Arrays are a fundamental part of MongoDB's document model. The ODM must expose the full power of MongoDB's array query and update operators while keeping the developer experience idiomatic and avoiding the need to drop to raw MQL for common array operations.

## Blueprint

1. **Array Field Declaration:** The ODM must support declaring a field as an array of a given type at the schema or model level, including arrays of primitives, embedded documents, and references.

2. **Array Query Operators:** The ODM must expose MongoDB's array query operators, including `$in`, `$all`, `$elemMatch`, and `$size`, through the query builder or an equivalent idiomatic API.

3. **Array Update Operators:** The ODM must expose MongoDB's array update operators, including `$push`, `$pull`, `$addToSet`, `$pop`, and the positional operators (`$`, `$[]`, `$[<identifier>]`), for modifying array contents without replacing the entire document.

4. **Array Filters:** For targeted updates to specific array elements, the ODM must support MongoDB's `arrayFilters` option.

5. **Validation:** The ODM must support declaring minimum and maximum length constraints on array fields, as well as constraints on the type and validity of array elements.
