# Embedded Fields

## Principle

Embedded (nested) documents are a core feature of MongoDB's document model and a primary reason users choose a document database. The ODM must provide a first-class mechanism for declaring, querying, updating, and validating nested document structures.

## Blueprint

1. **Nested Schema Declaration:** The ODM must allow nested documents to be declared using a structured schema or type definition that mirrors the host language's type system — for example, nested classes, types, or schema objects.

2. **Dot Notation Querying:** The ODM must support queries on nested fields using dot notation or an equivalent typed accessor, without requiring the user to write raw MQL strings.

3. **Partial Updates:** The ODM must support updating individual fields within an embedded document using MongoDB's `$set` and related update operators, without replacing the entire embedded document.

4. **Validation:** Validation rules (required, type, range, custom) must be expressible on fields within embedded documents, and validation errors must clearly identify which nested field failed.

5. **Schema Reuse:** Embedded document schemas must be reusable across multiple parent schemas without duplication.

6. **Discriminators:** Where an embedded field can hold one of several different document shapes, the ODM should support a discriminator pattern to identify and deserialize the correct type.
