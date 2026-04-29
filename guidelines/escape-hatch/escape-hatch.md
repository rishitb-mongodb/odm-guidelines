# Escape Hatch

## Principle

An Escape Hatch is a mechanism that allows users to bypass the ODM's abstraction layer and interact directly with the underlying MongoDB driver or native MQL. It ensures that the ODM is never a ceiling — any MongoDB feature not yet surfaced by the ODM can always be accessed by dropping to a lower level.

## Blueprint

1. **Raw Collection Access:** The ODM must expose the underlying driver collection object so that users can execute arbitrary operations (find, aggregate, runCommand, etc.) directly against the collection without going through the ODM's model layer.

2. **Raw Aggregation Pipeline:** The ODM must allow users to pass a raw aggregation pipeline array directly to the database, bypassing any ODM-level pipeline construction or transformation.

3. **Session and Transaction Passthrough:** The ODM must allow a native driver session or transaction to be passed through to escape-hatch operations, so that raw operations can participate in the same session or transaction as ODM-managed operations.

4. **Result Mapping:** When the escape hatch returns raw BSON documents, the ODM may optionally provide a utility to deserialize them into ODM model instances or host-language types. This must be documented clearly, including any limitations.

5. **Documentation of Boundaries:** The ODM must clearly document which features require the escape hatch and why, so that users understand when they have crossed from the ODM layer into the driver layer and what guarantees (e.g., middleware hooks, validation, change tracking) no longer apply.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | Done | Raw collection via `Connection.prototype.collection()`; raw DB aggregation via `Connection.prototype.aggregate()`; `getClient()` for `MongoClient` |
| EF Core | C# / .NET | Done | `MongoClient` from DbContext setup; `GetDatabase()`/`GetCollection<T>()` for raw operations; session and transaction passthrough |
| Spring Data MongoDB | Java | Done | `BasicQuery` for raw JSON; `@Query` for native queries in repository methods; `MongoTemplate` callbacks for direct driver access |
| Hibernate OGM | Java | Done | Raw `MongoClient` access for driver-level operations; `createNativeQuery()` for MQL and aggregation pipelines |
| Doctrine MongoDB ODM | PHP | Done | `DocumentManager::getDocumentCollection($class)` returns native `MongoDB\Collection`; always uses primary read preference |
| Laravel MongoDB | PHP | Done | `raw()` method on models and query builder; `DB::getMongoClient()` and `DB::getMongoDB()` for direct driver access |
| Mongoid | Ruby | Done | `Model.collection` for raw `Mongo::Collection`; `Mongoid.client()` for driver-level access; `with_session()` for session passthrough |
| Django MongoDB Backend | Python | Done | `connections["key"].database.client` returns the underlying PyMongo `MongoClient`; `raw_aggregate()` with `MongoManager` for direct pipeline execution |
