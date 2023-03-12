build:
	echo "Compiling for Linux and MacOS"
	GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o bin/cloudtrail-elastic_linux_amd64 ./...
	GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -o bin/cloudtrail-elastic_darwin_amd64 ./...

deploy: build
	serverless deploy