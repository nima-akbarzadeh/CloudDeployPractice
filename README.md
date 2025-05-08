# CloudDeployPractice
Example of a simple API call, docker build up, and CI/CD.

### App test with GitHub Actions


### To call Microservice
```bash
curl -X 'POST' \
  'https://opulent-barnacle-9pvj597vx472xrr7-8080.app.github.dev/summarize' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build container
`docker build .`


