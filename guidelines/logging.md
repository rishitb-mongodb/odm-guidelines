# Logging

## Principle

Logging allows developers and operators to observe the behavior of the ODM and the underlying driver at runtime. The ODM must provide a structured, configurable logging interface that integrates with the host ecosystem's standard logging frameworks and exposes enough information for debugging and performance analysis.

## Blueprint

1. **Log Levels:** The ODM must support standard log levels (e.g., `debug`, `info`, `warn`, `error`) and must allow the log level to be configured independently for ODM-layer events and driver-layer events.

2. **Command Logging:** The ODM must be capable of logging the MongoDB commands it generates (including the final MQL or aggregation pipeline), at a configurable log level. Sensitive field values in commands must be redactable.

3. **Slow Query Detection:** The ODM should support a configurable slow query threshold, above which executed operations are logged at a warning level along with their duration.

4. **Structured Output:** Log entries must include at minimum: timestamp, log level, operation type, collection name, and duration (where applicable). Log output must be in a structured format (e.g., JSON) when integrated with a structured logging framework.

5. **Framework Integration:** The ODM must integrate with the host ecosystem's standard logging framework (e.g., SLF4J in Java, `logging` in Python, `winston`/`pino` in Node.js) rather than emitting logs to a proprietary sink.

6. **Driver Log Passthrough:** The ODM must provide a way for users to access or forward log events emitted by the underlying MongoDB driver, so that connection pool, server selection, and topology events are observable alongside ODM-layer events.
