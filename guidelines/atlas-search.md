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
