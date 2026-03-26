# Polymorphic Array/Embedded Fields

## Principle

Polymorphic fields allow a single field or array to contain documents of different shapes, identified at runtime by a discriminator. The ODM must support this pattern in a way that preserves type safety where the host language allows, and makes the discriminator key transparent to the developer.

## Blueprint

1. **Discriminator Key:** The ODM must support a configurable discriminator key (a field stored in the document, e.g., `__t`, `_type`, or a user-defined name) that identifies the concrete type of a polymorphic embedded document or array element.

2. **Type Registration:** The ODM must provide a mechanism to register multiple concrete types against a single polymorphic field or array. Each registered type must have its own schema or class definition.

3. **Deserialization:** When reading a polymorphic document from MongoDB, the ODM must use the discriminator key to deserialize the document into the correct concrete type, rather than a generic map or base type.

4. **Querying by Type:** The ODM must allow users to filter documents or array elements by their concrete type using the discriminator key, through the query builder or an equivalent idiomatic API.

5. **Schema Inheritance:** Where the host language supports class inheritance, the ODM's discriminator pattern should integrate naturally with the inheritance model so that shared fields are defined on a base type and concrete types extend it.

6. **Array Polymorphism:** The ODM must support arrays where individual elements can be of different registered types, not just fields that hold a single polymorphic sub-document.
