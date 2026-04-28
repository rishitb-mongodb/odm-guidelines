# Embedded Fields

## Principle

Embedded (nested) documents are a core feature of MongoDB's document model and a primary reason users choose a document database. The ODM must provide a first-class mechanism for declaring, querying, updating, and validating nested document structures.

## Blueprint

1. **Nested Schema Declaration:** The ODM must allow nested documents to be declared using a structured schema or type definition that mirrors the host language's type system — for example, nested classes, types, or schema objects.

2. **Dot Notation Querying:** The ODM must support queries on nested fields using dot notation or an equivalent typed accessor, without requiring the user to write raw MQL strings.

3. **Partial Updates:** The ODM must support updating individual fields within an embedded document using MongoDB's `$set` and related update operators, without replacing the entire embedded document. This must only be done safely when concurrency tokens (e.g., version fields or optimistic concurrency checks) are in use; without them, partial updates risk overwriting changes made by concurrent writers and producing invalid document state.

4. **Validation:** Validation rules (required, type, range, custom) must be expressible on fields within embedded documents, and validation errors must clearly identify which nested field failed.

5. **Schema Reuse:** Embedded document schemas must be reusable across multiple parent schemas without duplication.

6. **Discriminators:** Where an embedded field can hold one of several different document shapes, the ODM may support a discriminator pattern to identify and deserialize the correct type. Note that some ODMs — including EF Core — have no concept of discriminators on embedded (non-root) documents, and other ODMs may similarly lack this capability. Support for this feature should be documented clearly per ODM.

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
