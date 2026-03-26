# Relationship Mapping

## Principle

Relationship Mapping covers how an ODM represents and resolves associations between documents, either by embedding related data directly or by storing references across collections. The ODM should expose a clear model for both approaches while remaining idiomatic to the host language and framework.

## Blueprint

1. **Embedded vs. Referenced Relationships:** The ODM must support both embedding sub-documents directly within a parent document and referencing documents in separate collections by their identifier. Each approach must be explicitly declarable at the schema or model level.

2. **Reference Resolution (Population):** For referenced relationships, the ODM must provide a mechanism to resolve references into full documents — commonly referred to as "population" or "eager loading". The resolution strategy (lazy vs. eager) must be documented.

3. **Cascading Behavior:** The ODM should document behavior for cascading operations (e.g., whether deleting a parent document deletes or orphans referenced children) and should allow this behavior to be configured where practical.

4. **Circular Reference Handling:** The ODM must handle circular references gracefully during serialization and population, without entering infinite loops or crashing.

5. **Idiomatic Expression:** The approach used to define relationships (e.g., decorators, schema options, annotations) must be consistent with the conventions of the host framework rather than introducing a foreign pattern.
