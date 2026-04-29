# BSON Data Type Support

## Principle

MongoDB stores data using BSON, a superset of JSON that includes types not found in most host languages. The ODM must provide first-class support for the BSON types most commonly encountered in MongoDB applications, ensuring that values round-trip correctly between the application layer and the database.

## Blueprint

1. **ObjectId:** The ODM must support `ObjectId` as a first-class type for document identifiers. It must serialize correctly to and from BSON, and must be representable and constructable from the host language.

2. **Date:** The ODM must map BSON `Date` values to the host language's native date/time type. Note that some precision loss may occur on platforms whose native date type has lower resolution than BSON's millisecond precision. Many languages also distinguish between a local time, a timezone-aware time, and a UTC time; the ODM must document its default strategy for this distinction and how it maps to BSON `Date`, which is always stored as UTC milliseconds since epoch.

3. **Decimal128:** The ODM must support `Decimal128` for use cases requiring high-precision decimal arithmetic (e.g., financial data). The ODM must document how `Decimal128` values are exposed and whether a native decimal type or string representation is used in the host language.

4. **UUID:** The ODM must support storing and retrieving UUIDs using the BSON `Binary` UUID subtype. UUIDs must be stored as `UUID.Standard` (subtype 4) by default. The ODM must document the subtype used and any implications for querying existing data stored in other representations. Support for the broader BSON `Binary` type beyond UUIDs is recommended but considered a nice-to-have.

5. **Int32, Int64, and Double:** The ODM must preserve the distinction between BSON integer and floating-point types where the host language's type system allows. Implicit coercion between numeric types must be documented.

6. **Null vs. Undefined:** The ODM must have a documented and consistent behavior for the difference between a BSON `null` value and a missing field. This distinction must be surfaceable to the application layer.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | Done | ObjectId, Decimal128, UUID (subtype 4 default since v9.0), BigInt for Int64; no timezone handling at schema level |
| EF Core | C# / .NET | Done | ObjectId, Decimal128, all CLR numeric types; DateTime defaults to UTC; GUID defaults to Standard (UUID subtype 4); `Mql.IsNullOrMissing()` for null vs. missing distinction |
| Spring Data MongoDB | Java | Done | ObjectId, Decimal128 via `BigDecimal`, UUID (must configure representation explicitly); `BigDecimal`/`BigInteger` representation defaults changed in v5.0 |
| Hibernate OGM | Java | In Progress | ObjectId, `java.time.Instant`, UUID, Int32/Int64/Double, String, boolean, byte[] supported; Decimal128 not documented; LocalDate/LocalDateTime support not confirmed |
| Doctrine MongoDB ODM | PHP | Done | ObjectId, Date/DateTime (`MongoDB\BSON\UTCDateTime`), Decimal128 (requires `ext-bcmath`), UUID binary; timezone must be stored separately |
| Laravel MongoDB | PHP | Done | ObjectId, Carbon/DateTime (auto-converts v5.0+), Decimal128, UUID; nested array dates not automatically cast to Carbon |
| Mongoid | Ruby | Done | `BSON::ObjectId`; Date/Time with timezone awareness; Decimal128 via `BigDecimal`; UUID via `BSON::Binary`; no distinct `BSON::Int32`/`BSON::Int64` at model level |
| Django MongoDB Backend | Python | Done | `ObjectIdField` replaces unsupported `AutoField`/`BigAutoField`/`SmallAutoField`; `DateTimeField` has no microsecond granularity; `DurationField` stores milliseconds; `JSONField` cannot distinguish JSON null from SQL null; `CompositePrimaryKey` and `GeneratedField` not supported |
