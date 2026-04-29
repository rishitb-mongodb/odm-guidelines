# Atlas Search

## Principle

Atlas Search provides full-text and faceted search capabilities built directly into MongoDB Atlas via the `$search` aggregation stage. The ODM must expose Atlas Search in a way that allows developers to construct search queries without writing raw aggregation pipeline stages for common use cases.

## Blueprint

1. **Search Query Builder:** The ODM must provide an API for constructing Atlas Search queries (e.g., `text`, `phrase`, `autocomplete`, `compound`, `range` operators) that integrates with or extends the existing query builder interface.

2. **Index Configuration Awareness:** The ODM must document the requirement that an Atlas Search index must exist on the target collection before search queries can be executed. The ODM may optionally provide utilities to define or reference search index configurations alongside the schema.

3. **Score and Sort:** The ODM must expose Atlas Search's relevance score (`searchScore`) as an accessible field on query results, and must allow results to be sorted by score.

4. **Autocomplete Support:** The ODM should support the Atlas Search `autocomplete` operator, enabling developers to build search-as-you-type features without constructing raw `$search` stages.

5. **Facets:** The ODM should expose Atlas Search's faceting capabilities (`$searchMeta`) for building aggregated search result counts grouped by field values.

6. **Highlight:** Where practical, the ODM should expose Atlas Search's `highlight` option so that matching text snippets can be returned alongside results.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | Done | `$search`/`$searchMeta` via `.aggregate()` pipeline; index managed via `createSearchIndex()`; no wrapper API |
| EF Core | C# / .NET | Won't Do | Not supported; no EF Core equivalent for `$search`; use raw driver aggregation via `MongoClient` escape hatch |
| Spring Data MongoDB | Java | Backlog | No native `$search` integration; workaround via custom `AggregationOperation`; GitHub issue #3831 open |
| Hibernate OGM | Java | Backlog | No native support; accessible via `createNativeQuery()` with `$search` stage; `$search` cannot run inside transactions |
| Doctrine MongoDB ODM | PHP | Done | `#[SearchIndex]` attribute; `$search`/`$searchMeta` stages available; dynamic mapping does not auto-index embedded arrays |
| Laravel MongoDB | PHP | Done | Native `search()` and `autocomplete()` query builder methods (v5.2+); `createSearchIndex()` schema helper; Laravel Scout integration |
| Mongoid | Ruby | Done | `search_index` macro; `create_search_indexes`/`remove_search_indexes`/`search_indexes` helpers; full aggregation pipeline access |
| Django MongoDB Backend | Python | Done | Dedicated expression classes (`SearchText`, `SearchPhrase`, `SearchEquals`, `SearchAutocomplete`, etc.) via `annotate()`; `CompoundExpression` for combining; `SearchScoreOption` for scoring; `SearchIndex` for index management |
