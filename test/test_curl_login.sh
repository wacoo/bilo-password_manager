//token_stored_in_TOKEN
TOKEN=$(curl -s -X POST -H "Content-Type: application/json" -d '{"email":"wac@example.com", "password": "password123"}' http://localhost:5000/auth/login | jq -r '.token')
curl -X GET -H "Authorization: Bearer $TOKEN" http://localhost:5000/view/

//token_not_stored

curl -X POST -H "Content-Type: application/json" -d '{"email":"wac@example.com", "password": "password123"}' http://localhost:5000/auth/login
curl -X GET -H "Authorization: Bearer a421b906-0621-4772-909b-b0c5b8633962" http://localhost:5000/view/