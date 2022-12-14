# Community supported 
We welcome contributions.
 
The Keyfactor Python Client SDK is open source and community supported, meaning that there is **no SLA** applicable for these tools.

To report a problem or suggest a new feature, use the **[Issues](../../issues)** tab. If you want to contribute actual bug fixes or proposed enhancements, use the **[Pull requests](../../pulls)** tab.

# Keyfactor Python Client SDK
Client SDK in Python for the Keyfactor Web API

The SDK has three layers intended for consumer use:
1. The contents of the kfclient folder are low-level modules autogenerated by the [openapi-python-client](https://pypi.org/project/openapi-python-client/0.6.0a4/) tool, with modifications from a Keyfactor-maintained tool, and can be used directly. However, the added flexibility gained by using this directly comes at the cost of more cumbersome and less untuitive usage requirements. You can follow the [readme](kfclient/README.md) in the kfclient folder for examples of doing this. You can also use this source code to find examples of calling the Keyfactor API from Python without using any of the SDK modules.
2. The keyfactor.py module is a wrapper for the kfclient code, generated by a Keyfactor-maintained tool, and greatly simplifies use of the openapi-generated modules. An example is given below. cryptoOps.py provides some utilities that work in conjunction with the keyfactor.py module for generating and processing certificates and keys.
3. The scenarios.py module is a user-friendly, high-level wrapper for keyfactor.py and cryptoOps.py, and provides the simplest access to functions for common tasks related to certificate issuance, search, and metadata management. Two examples are given below.

# Example usage:
```
# Wrappers for python models and API calls
import keyfactor

# User-friendly interfaces to a combination of crypto operations and keyfactor calls
import scenarios

# Generate a keypair on the device, sign a CSR with it, submit to CA via Keyfactor, and return the signed cert
cert,key = scenarios.csrEnrollment("CN=pythonTest","WebServer",{},{"Email-Contact":"j@d.k"})

# Takes a PEM-encoded cert or a Keyfactor Certificate Id and returns a dictionary of Keyfactor metadata for that cert
metadata = scenarios.getMetadata(cert)

# Direct access to the Keyfactor call to get a certificate and parse the response locally
myCert = keyfactor.get_certificate_(id=1).to_dict()["SerialNumber"]
```
