# ODM Guidelines

## What is an ODM?

An Object Document Mapper (ODM) is a programming library that maps between objects in your application code and documents stored in a document database like MongoDB. ODMs are conceptually similar to Object Relational Mappers (ORMs) used with relational databases, both let developers work with database records as native objects in their language, with the library handling serialization, querying, and schema validation. 

MongoDB has several ODMs across ecosystems, including [Mongoose](https://mongoosejs.com/) (Node.js), [Mongoid](https://www.mongoid.org/) (Ruby), [Laravel MongoDB](https://www.mongodb.com/docs/drivers/php/laravel-mongodb/) (PHP), and the [MongoDB EF Core Provider](https://www.mongodb.com/docs/entity-framework/current/) (C# / .NET), among others.

ODM Guidelines are a set of lightweight, non-prescriptive blueprints for core features that MongoDB-maintained Object Document Mappers (ODMs) should support. Unlike MongoDB [Driver Specifications](https://github.com/mongodb/specifications), which are strictly uniform across all drivers, ODM Guidelines acknowledge that each ODM is intentionally opinionated and tied to its host language and framework. The goal is to ensure a **comparable and consistent end-user experience** across ODMs for a defined set of important features, while giving each ODM team the flexibility to implement them in the most idiomatic way for their ecosystem.

## What are ODM Guidelines?

MongoDB ODMs sit at a different layer of the application stack than drivers. Where drivers expose the full MongoDB wire protocol uniformly across languages, ODMs provide a higher-level abstraction for data mapping and CRUD operations that is deeply tied to a specific language's conventions, frameworks, and compile-time reflection APIs. This makes strict, prescriptive specifications unsuitable.

ODM Guidelines solve this by defining the **intent and expected behavior** of a feature — not the exact API. Each guideline describes a principle and a blueprint that an ODM team should use as a reference when implementing the feature in their ecosystem. ODM teams retain full ownership over how a feature is expressed in their language and framework.

## Guidelines

The following guidelines define the features that each ODM should implement. Each guideline is a markdown file in the [`guidelines/`](guidelines/) directory.

| # | Guideline |
|---|-----------|
| 1 | [Query Builder](guidelines/query-builder.md) |
| 2 | [Bulk Operations](guidelines/bulk-operations.md) |
| 3 | [Relationship Mapping](guidelines/relationship-mapping.md) |
| 4 | [Index Management](guidelines/index-management.md) |
| 5 | [Transactions](guidelines/transactions.md) |
| 6 | [BSON Data Type Support](guidelines/bson-data-types.md) |
| 7 | [Array Fields](guidelines/array-fields.md) |
| 8 | [Embedded Fields](guidelines/embedded-fields.md) |
| 9 | [Polymorphic Array/Embedded Fields](guidelines/polymorphic-fields.md) |
| 10 | [Security Features (CSFLE & QE)](guidelines/security-features.md) |
| 11 | [Joins ($lookup)](guidelines/joins.md) |
| 12 | [Atlas Search](guidelines/atlas-search.md) |
| 13 | [Vector Search](guidelines/vector-search.md) |
| 14 | [Logging](guidelines/logging.md) |
| 15 | [Escape Hatch](guidelines/escape-hatch.md) |
| 16 | [Performance Benchmarks](guidelines/performance-benchmarks.md) |

## ODM Compliance

The table below shows each MongoDB-maintained ODM and its triage summary — how many of the total guidelines have been formally triaged (marked Done, In Progress, or Won't Do) by the ODM team. **Triage** is the process by which each ODM team reviews these guidelines and assigns a status to each feature, indicating whether they plan to implement it, have already done so, or have decided not to.

| ODM | Language / Ecosystem | Triage Summary |
|-----|----------------------|----------------|
| [Mongoose](odms/mongoose.md) | Node.js / JavaScript | 3/16 |
| [Django](odms/django.md) | Python | 0/16 |
| [Spring Data MongoDB](odms/spring.md) | Java | 0/16 |
| [Hibernate](odms/hibernate.md) | Java | 0/16 |
| [EF Core](odms/efcore.md) | C# / .NET | 5/16 |
| [Doctrine ODM](odms/doctrine.md) | PHP | 0/16 |
| [Laravel MongoDB](odms/laravel.md) | PHP / Laravel | 0/16 |
| [Mongoid](odms/mongoid.md) | Ruby | 0/16 |

### Status Definitions

| Status | Meaning |
|--------|---------|
| **Done** | The feature has been implemented in accordance with the guideline. |
| **In Progress** | The feature is actively being worked on. |
| **Backlog** | The feature has not yet been triaged by the ODM team. |
| **Won't Do** | The ODM team has decided not to implement this feature, with a documented reason. |
