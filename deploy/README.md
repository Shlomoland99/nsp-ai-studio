# Deployment

Use Docker Compose for local integration. For production, deploy the API and web container to your chosen provider, attach PostgreSQL/object storage, configure secrets in the provider secret manager, and set NEXT_PUBLIC_API_URL. No provider credentials are included.