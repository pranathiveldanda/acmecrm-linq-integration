# Linq + AcmeCRM Integration (Technical Demonstration)

## Objective

This project demonstrates how **Linq** can integrate with a fictional CRM system, **AcmeCRM**, by:
- Accepting contact details (e.g., from a QR code scan or networking interaction)
- Pushing those contacts into the AcmeCRM system
- Retrieving contacts from AcmeCRM
- Translating CRM-specific fields (e.g., `acme_first_name`) into Linq's normalized format (`firstName`)
- Simulating secure API access via mocked JWT-based authentication.


## Technical Design

### Framework & Language
- **Python + Flask**: Lightweight API web framework.

### Authentication
- Mocked JWT via 'Authorization: Bearer mocktoken123'
- Follows common REST API practices to simulate real-world API security
- Easily replaceable with real JWT verification logic using libraries like `PyJWT` or OAuth2 tokens