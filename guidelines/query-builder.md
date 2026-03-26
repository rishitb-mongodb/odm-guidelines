# Query Builder

## Principle

The Query Builder is the core abstraction for users interacting with MongoDB through the ODM. It must prioritize an intuitive, idiomatic developer experience over strict, cross-language uniformity.

## Blueprint

1. **Idiomatic Querying:** The ODM should enable developers to express database queries using the host language's native constructs (e.g., LINQ in C#, method chaining in Node.js) rather than requiring them to write raw MQL.

2. **Aggregation Access:** The query interface must provide a clear path for constructing and executing MongoDB's Aggregation Pipeline, translating high-level ODM operations into efficient pipeline stages where necessary.

3. **Extensibility (Escape Hatch):** A mechanism must be available to allow advanced users to bypass the Query Builder and drop directly to the underlying driver or native MQL. This ensures full access to MongoDB features that may not be supported by the ODM's abstraction layer.

4. **Consistency of Result:** The end-user experience for common operations (e.g., filtering, sorting, basic CRUD) should feel consistent and comparable across different standardized ODMs.
