import keyfactor
import cryptoOps

def pfxEnrollment(subject,template,SANs={},metadata={}):
  cert = keyfactor.pfx_enroll({"Subject":subject,"Template":template,"SANs":SANs,"Metadata":metadata})
  return (cert["CertificateInformation"]["Pkcs12Blob"],cert["CertificateInformation"]["Password"])

def csrEnrollment(subject,template,SANs={},metadata={}):
  csr,key = cryptoOps.createCSR(subject,SANs)
  cert = keyfactor.csr_enroll({"CSR":csr,"Template":template,"Metadata":metadata})
  return cert["CertificateInformation"]["Certificates"][0],key

def queryCertificates(queryDict,query=None,verbose=3):
  if query is None:
    query = 'AND'.join([f'{k} -eq "{v}"' for k,v in queryDict.items()])
  return [c.to_dict() for c in keyfactor.query_certificates_(pq_query_string=query,verbose=verbose)]

def getMetadata(cert):
  lookup = {"CertID":cert} if isinstance(cert, int) else {"Thumbprint": cryptoOps.getThumbprint(cert)}
  return queryCertificates(lookup)[0]["Metadata"]

