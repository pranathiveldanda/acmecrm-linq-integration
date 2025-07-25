## Linq + AcmeCRM Integration (Technical Demonstration)

## Objective

This project demonstrates how Linq can integrate with a fictional CRM system, AcmeCRM, by:

- Accepting contact details (e.g., from a QR code scan or networking interaction)
- Pushing those contacts into the AcmeCRM system
- Retrieving contacts from AcmeCRM
- Translating CRM-specific fields (e.g., `acme_first_name`) into Linq's normalized format (`firstName`)
- Simulating secure API access via mocked JWT-based authentication.

### Framework & Language

- Python + Flask: Lightweight API web framework.

### Assumptions

- Assumed that the data is simple with no nested values.
- Authorization is only categorized as authorized and unauthorized for all the CRUD operations combined.
- Gave null authorization so that it fails by default
- Mocked JWT via 'Authorization: Bearer mocktoken123'
- Follows common REST API practices to simulate real-world API security

### Improvements

- Easily replaceable with real JWT verification logic using libraries like `PyJWT` or OAuth2 tokens
- Design for nested data and other complex models
- Integrate it data-base and design a front-end UI for all users
- Enforce Role based access control on CRUD operations
