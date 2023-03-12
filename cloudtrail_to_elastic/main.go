package main

import (
	"fmt"
	"os"

	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
)

const (
	elasticHost = "http://192.168.1.38:9200"
	indexPrefix = "cloudtrail"
)

var elasticHeaders = map[string]string{
	"Content-Type":  "application/json",
	"Authorization": fmt.Sprintf("ApiKey %s", os.Getenv("ES_API_KEY")),
}

func main() {
	sess := session.Must(session.NewSession())

	handler := Handler{
		S3Client: s3.New(sess, &aws.Config{}),
	}
	lambda.Start(handler.ProcessRequest)
}
