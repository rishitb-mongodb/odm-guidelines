# Transactions

## Principle

Transactions allow multiple operations across one or more collections to be executed atomically. The ODM must expose MongoDB's multi-document ACID transaction semantics in a way that integrates naturally with the host framework's patterns for managing units of work.

## Blueprint

1. **Session Management:** The ODM must abstract the creation and lifecycle of a MongoDB `ClientSession`. Users should not be required to manage sessions directly in common use cases unless they opt into lower-level control.

2. **Callback-Based and Manual APIs:** The ODM should provide both a callback-based transaction API (where the ODM handles commit and abort automatically on success or error) and a manual API for cases where the user needs explicit control over the transaction lifecycle.

3. **Framework Integration:** Where the host framework provides its own unit-of-work or transaction management abstraction (e.g., `@Transactional` in Spring, `transaction.atomic()` in Django), the ODM must integrate with it rather than introducing a parallel pattern.

4. **Error Handling and Rollback:** Uncaught errors during a transaction must result in the transaction being aborted. The ODM must not silently swallow transaction errors or leave transactions in an indeterminate state.

5. **Replica Set Requirement:** The ODM must document that multi-document transactions require a replica set or sharded cluster, and should surface a clear error if transactions are attempted against a standalone instance.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | Done | `startSession()`, `withTransaction()` callback API; manual `startTransaction()`/`commitTransaction()`/`abortTransaction()`; no nested transactions; no `Promise.all()` inside transactions |
| EF Core | C# / .NET | Done | `SaveChanges()` transactional by default (v8.1+); explicit transactions via `MongoTransactionManager` (v9.0.3+); requires replica set |
| Spring Data MongoDB | Java | Done | `@Transactional` via `MongoTransactionManager`; `TransactionTemplate` for manual control; requires MongoDB 4.0+ replica set |
| Hibernate OGM | Java | Done | `@Transactional` integration; `EntityTransaction`; multi-document ACID; requires replica set; `$search` queries cannot run inside transactions |
| Doctrine MongoDB ODM | PHP | Done | Session and transaction support (v2.7+); `useTransactionalFlush` config; lifecycle events do not dispatch during transaction retries |
| Laravel MongoDB | PHP | Done | `DB::transaction()` callback; manual session API; requires replica set; no nested transactions |
| Mongoid | Ruby | Done | `Model.transaction {}` (v9.0+); `with_session` (v6.4+); `after_commit`/`after_rollback` callbacks; requires replica set |
| Django MongoDB Backend | Python | Done | Custom `django_mongodb_backend.transaction` module — Django's native `django.db.transaction` not supported; `@transaction.atomic` and `with transaction.atomic()`; no savepoints, no DDL transactions; requires replica set |
