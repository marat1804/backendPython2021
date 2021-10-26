echo "Test nginx"
ab -n $1 -c $2 -k 127.0.0.1:8000/picture.png > nginx.txt
echo ""

echo "Test gunicorn"
ab -n $1 -c $2 -k 127.0.0.1:8000/ > gunicorn.txt
echo ""

echo "Test nginx+gunicorn"
ab -n $1 -c $2 -k 127.0.0.1:8080/api/ > proxy.txt
echo ""
