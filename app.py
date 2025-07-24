from flask import Flask, jsonify, request
from auth import mock_auth_required
from utils import normalize_contact, denormalize_contact

app = Flask(__name__)

# In-memory mocked AcmeCRM store
acme_contacts = [
    {
        "acme_id": "1",
        "acme_first_name": "Ada",
        "acme_last_name": "Lovelace",
        "acme_email": "ada@acme.com"
    }
]

@app.route("/contacts", methods=["GET"])
@mock_auth_required
def get_contacts():
    normalized = [normalize_contact(c) for c in acme_contacts]
    return jsonify(normalized), 200

@app.route("/contacts", methods=["POST"])
@mock_auth_required
def post_contact():
    data = request.get_json()
    required = ["firstName", "lastName", "email"]

    if not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    new_id = str(len(acme_contacts) + 1)
    acme_contact = denormalize_contact({**data, "id": new_id})
    acme_contacts.append(acme_contact)

    return jsonify({
        "message": "Contact added successfully",
        "contact": normalize_contact(acme_contact)
    }), 201

if __name__ == "__main__":
    app.run(debug=True)