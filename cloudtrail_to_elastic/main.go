package main

import (
	"fmt"
	"os"

	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/aws/aws-sdk-go/service/ssm"
)

var (
	elasticHost    = os.Getenv("ELASTIC_HOST")
	indexPrefix    = os.Getenv("cloudtrail")
	elasticHeaders = map[string]string{
		"Content-Type":  "application/json",
		"Authorization": fmt.Sprintf("ApiKey %s", getSecret(os.Getenv("ES_API_KEY"))),
	}
)

func main() {
	sess := session.Must(session.NewSession())

	handler := Handler{
		S3Client: s3.New(sess, &aws.Config{}),
	}
	lambda.Start(handler.ProcessRequest)
}

func getSecret(key string) string {
	sess := session.Must(session.NewSession())
	ssmClient := ssm.New(sess, &aws.Config{})
	out, err := ssmClient.GetParameter(&ssm.GetParameterInput{
		Name:           aws.String(key),
		WithDecryption: aws.Bool(true),
	})
	if err != nil {
		panic(err)
	}
	return *out.Parameter.Value

}
