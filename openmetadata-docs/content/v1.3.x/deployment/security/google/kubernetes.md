---
title: Google SSO for Kubernetes
slug: /deployment/security/google/kubernetes
---

# Google SSO for Kubernetes

Check the Helm information [here](https://artifacthub.io/packages/search?repo=open-metadata).

Once the `Client Id` is generated, see the snippet below for an example of where to
place the client id value and update the authorizer configurations in the `values.yaml`.


```yaml
openmetadata:
  config:
    authorizer:
      className: "org.openmetadata.service.security.DefaultAuthorizer"
      containerRequestFilter: "org.openmetadata.service.security.JwtFilter"
      initialAdmins:
        - "user1"
        - "user2"
      botPrincipals:
        - "<service_application_client_id>"
      principalDomain: "open-metadata.org"
    authentication:
      provider: "google"
      publicKeys:
        - "https://www.googleapis.com/oauth2/v3/certs"
        - "http://{your openmetadata domain}/api/v1/config/jwks" # Update with your Domain and Make sure this "/api/v1/config/jwks" is always configured to enable JWT tokens
      authority: "https://accounts.google.com"
      clientId: "{client id}"
      callbackUrl: "http://localhost:8585/callback"
```

{% partial file="/v1.3/deployment/configure-ingestion.md" /%}
