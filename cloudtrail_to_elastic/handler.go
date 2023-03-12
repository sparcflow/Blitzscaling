package main

import (
	"bytes"
	"compress/zlib"
	"context"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
	"time"

	"github.com/pkg/errors"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/hashicorp/go-multierror"
	log "github.com/sirupsen/logrus"
)

type Handler struct {
	S3Client *s3.S3
}

func (h *Handler) ProcessRequest(ctx context.Context, s3Event events.S3Event) (err error) {
	var merr *multierror.Error
	log.Infof("processing %d records", len(s3Event.Records))
	for _, record := range s3Event.Records {
		if strings.Contains(record.S3.Object.Key, "/CloudTrail-Digest") {
			continue
		}
		if err = h.ProcessObject(record.S3.Bucket.Name, record.S3.Object.Key); err != nil {
			merr = multierror.Append(merr, err)
		}

	}
	return merr.ErrorOrNil()
}

func (h *Handler) ProcessObject(bucket, key string) (err error) {
	var trailRecords TrailLog
	data, err := DownloadObject(h.S3Client, bucket, key)
	if err != nil {
		return errors.Wrap(err, "DownloadObject")
	}
	if err = json.Unmarshal(data, &trailRecords); err != nil {
		return errors.Wrap(err, "Unmarshal")
	}
	for _, r := range trailRecords.Records {
		event, _ := json.Marshal(r)
		if skipRecord(event) {
			continue
		}
		if err = SendDataToEs(event); err != nil {
			return errors.Wrap(err, "SendDataToEs")
		}
	}
	return nil
}

func DownloadObject(client *s3.S3, bucket, key string) (data []byte, err error) {
	input := new(s3.GetObjectInput).SetBucket(bucket).SetKey(key)
	res, err := client.GetObject(input)
	if err != nil {
		return nil, errors.Wrap(err, "GetObject")
	}
	stream := res.Body
	if strings.HasSuffix(key, "tar.gz") {
		if stream, err = zlib.NewReader(res.Body); err != nil {
			return nil, err
		}
	}
	return ioutil.ReadAll(stream)
}

func SendDataToEs(data []byte) error {
	year, week := time.Now().ISOWeek()
	url := fmt.Sprintf("%s/%s-%d-%d/_doc", elasticHost, indexPrefix, year, week)
	client := &http.Client{}
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(data))
	if err != nil {
		return errors.Wrap(err, "NewRequest")
	}
	for key, value := range elasticHeaders {
		req.Header.Add(key, value)
	}
	resp, err := client.Do(req)
	if err != nil {
		return errors.Wrap(err, "HTTP Do")
	}
	defer resp.Body.Close()
	respBody, err := ioutil.ReadAll(resp.Body)

	if resp.StatusCode != 201 && resp.StatusCode != 200 {
		return fmt.Errorf("Error status %d: %s", resp.StatusCode, string(respBody))
	}
	return err
}
