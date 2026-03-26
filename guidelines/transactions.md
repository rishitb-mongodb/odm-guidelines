# Transactions

## Principle

Transactions allow multiple operations across one or more collections to be executed atomically. The ODM must expose MongoDB's multi-document ACID transaction semantics in a way that integrates naturally with the host framework's patterns for managing units of work.

## Blueprint

1. **Session Management:** The ODM must abstract the creation and lifecycle of a MongoDB `ClientSession`. Users should not be required to manage sessions directly in common use cases unless they opt into lower-level control.

2. **Callback-Based and Manual APIs:** The ODM should provide both a callback-based transaction API (where the ODM handles commit and abort automatically on success or error) and a manual API for cases where the user needs explicit control over the transaction lifecycle.

3. **Retry Logic:** The ODM must implement or expose MongoDB's recommended transaction retry logic for transient errors (e.g., `TransientTransactionError`, `UnknownTransactionCommitResult`). This behavior must be documented clearly.

4. **Framework Integration:** Where the host framework provides its own unit-of-work or transaction management abstraction (e.g., `@Transactional` in Spring, `transaction.atomic()` in Django), the ODM must integrate with it rather than introducing a parallel pattern.

5. **Error Handling and Rollback:** Uncaught errors during a transaction must result in the transaction being aborted. The ODM must not silently swallow transaction errors or leave transactions in an indeterminate state.

6. **Replica Set Requirement:** The ODM must document that multi-document transactions require a replica set or sharded cluster, and should surface a clear error if transactions are attempted against a standalone instance.
