
# Keyfactor Python Client SDK
Client SDK in Python for the Keyfactor Web API

## Example usage:
```
# Wrappers for python models and API calls
import keyfactor

# Friendly interfaces to a combination of crypto operations and keyfactor calls
import scenarios

# Generate a keypair on the device, sign a CSR with it, submit to CA via Keyfactor, and return the signed cert
cert,key = scenarios.csrEnrollment("CN=pythonTest","WebServer",{},{"Email-Contact":"j@d.k"})

# Takes a PEM-encoded cert or a Keyfactor Certificate Id and returns a dictionary of Keyfactor metadata for that cert
metadata = scenarios.getMetadata(cert)

# Direct access to the Keyfactor call to get a certificate and parse the response locally
myCert = keyfactor.get_certificate_(id=1).to_dict()["SerialNumber"]
```
