# Security Features (CSFLE & QE)

## Principle

MongoDB provides client-side encryption capabilities — Client-Side Field Level Encryption (CSFLE) and Queryable Encryption (QE) — that allow sensitive fields to be encrypted in the application before being sent to the server. The ODM must surface these capabilities in a way that integrates with the schema/model definition and does not require users to configure the underlying driver directly for common use cases.

## Blueprint

1. **Field-Level Encryption Declaration:** The ODM must allow encryption to be declared at the field level within the schema or model definition, specifying the encryption algorithm and key identifier for each encrypted field.

2. **CSFLE Support:** The ODM must support MongoDB's Client-Side Field Level Encryption (CSFLE), including both explicit (manual) and automatic encryption modes. For automatic encryption, the ODM must generate or accept a JSON Schema that the driver uses to identify fields for encryption.

3. **Queryable Encryption (QE) Support:** The ODM must support Queryable Encryption for use cases requiring encrypted fields to be queried. The ODM must surface QE's query type options (e.g., `equality`, `range`, `substring`) at the field declaration level, including the newer substring query support.

4. **Key Management Integration:** The ODM should document how encryption keys are managed and should support integration with MongoDB's Key Management Service (KMS) providers (AWS, Azure, GCP, local). For ODMs that are built upon a driver, key management should not be duplicated at the ODM layer — the driver already provides this surface, and duplicating it would double the API without meaningful benefit. The ODM should instead document how to access the driver's key management capabilities where needed.

5. **Transparent Decryption:** Encrypted fields must be transparently decrypted when documents are read back through the ODM, without requiring explicit decryption calls in application code.

6. **Error Transparency:** Encryption and decryption errors must be surfaced as clear, actionable errors at the ODM layer rather than being wrapped in generic driver exceptions.

## ODM Support

| ODM | Language | Status | Notes |
|-----|----------|--------|-------|
| Mongoose | JavaScript / TypeScript | Backlog | — |
| EF Core | C# / .NET | Done | — |
| Spring Data MongoDB | Java | Backlog | — |
| Hibernate OGM | Java | Backlog | — |
| Doctrine MongoDB ODM | PHP | Backlog | — |
| Laravel MongoDB | PHP | Backlog | — |
| Mongoid | Ruby | Backlog | — |
| Django MongoDB Backend | Python | Done | Queryable Encryption (QE) supported as a first-class feature; Client-Side Field Level Encryption (CSFLE) not supported |
