# BSON Data Type Support

## Principle

MongoDB stores data using BSON, a superset of JSON that includes types not found in most host languages. The ODM must provide first-class support for the BSON types most commonly encountered in MongoDB applications, ensuring that values round-trip correctly between the application layer and the database.

## Blueprint

1. **ObjectId:** The ODM must support `ObjectId` as a first-class type for document identifiers. It must serialize correctly to and from BSON, and must be representable and constructable from the host language.

2. **Date:** The ODM must map BSON `Date` values to the host language's native date/time type. The mapping must preserve timezone semantics and must not silently truncate precision.

3. **Decimal128:** The ODM must support `Decimal128` for use cases requiring high-precision decimal arithmetic (e.g., financial data). The ODM must document how `Decimal128` values are exposed and whether a native decimal type or string representation is used in the host language.

4. **Binary and UUID:** The ODM must support the BSON `Binary` type, including the UUID subtype. The UUID representation must be consistent and the ODM must document the expected subtype used when storing and querying UUIDs.

5. **Int32, Int64, and Double:** The ODM must preserve the distinction between BSON integer and floating-point types where the host language's type system allows. Implicit coercion between numeric types must be documented.

6. **Null vs. Undefined:** The ODM must have a documented and consistent behavior for the difference between a BSON `null` value and a missing field. This distinction must be surfaceable to the application layer.
