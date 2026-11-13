ShopEase - Authentication, User and Product Catalog Services

shopease-auth-service/             Authentication Service   (port 8001, MySQL host port 3307)
shopease-user-service/             User Service             (port 8002, MySQL host port 3308)
shopease-product-catalog-service/  Product Catalog Service  (port 8003, MySQL host port 3309)
Documentation/                     Implementation reports (DOCX + PDF) and Swagger UI screenshots

All three services are independent projects with their own database and docker-compose.yml.
They must use the SAME JWT_SECRET_KEY and JWT_ALGORITHM in their .env files.
The Product Catalog Service needs the role claim "admin" for its admin APIs: promote one account in
the Authentication Service database (see section 5 of its README.md) and log in again.
See the README.md inside each project for setup, Docker commands, API details and test results.
Docker image builds and MySQL containers were not run where these projects were built; run
"docker compose up -d --build" in each project folder to confirm them.
