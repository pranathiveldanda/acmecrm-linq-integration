def normalize_contact(acme_contact):
    return {
        "id": acme_contact["acme_id"],
        "firstName": acme_contact["acme_first_name"],
        "lastName": acme_contact["acme_last_name"],
        "email": acme_contact["acme_email"]
    }

def denormalize_contact(contact):
    return {
        "acme_id": contact.get("id"),
        "acme_first_name": contact.get("firstName"),
        "acme_last_name": contact.get("lastName"),
        "acme_email": contact.get("email")
    }