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
| Mongoose | JavaScript / TypeScript | Done | Nested schema declaration; dot notation querying; `$set` partial updates; nested validation via `runValidators: true`; care needed with `minimize` option on dot notation updates |
| EF Core | C# / .NET | Done | `OwnsOne()`/`OwnsMany()`; LINQ dot notation; partial updates not supported — whole-document updates only; discriminators on embedded (non-root) documents not supported |
| Spring Data MongoDB | Java | Done | Automatic nested object mapping; dot notation in queries and updates; nested field path strings require manual construction (no compile-time type safety) |
| Hibernate OGM | Java | Done | `@Embeddable`/`@Embedded` and `@Struct` for nested documents; nested field querying via HQL/JPQL; partial update behaviour not explicitly documented |
| Doctrine MongoDB ODM | PHP | Done | `@EmbedOne`/`@EmbedMany`; dot notation in QueryBuilder; `$set` partial updates; `#[Validation]` for JSON Schema validation (v2.3+); schema reuse supported |
| Laravel MongoDB | PHP | Done | `embedsOne`/`embedsMany`; dot notation querying; `$set` partial updates; no built-in nested field validation |
| Mongoid | Ruby | Done | `embeds_one`/`embeds_many`; dot notation; `$set` partial updates; `accepts_nested_attributes_for`; embedded documents cannot be queried or updated independently of parent |
| Django MongoDB Backend | Python | Done | `EmbeddedModelField` with `EmbeddedModel` base class; double-underscore dot notation for nested queries; `EmbeddedFieldIndex` for subfield indexes (v6.0.2+); relational fields cannot be used inside `EmbeddedModel` |
