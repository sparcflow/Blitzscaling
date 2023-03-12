package main

import (
	"encoding/json"

	log "github.com/sirupsen/logrus"
)

type TrailLog struct {
	Records []interface{} `json:"Records"`
}

type TrailEvent struct {
	EventID      string `json:"eventID"`
	EventSource  string `json:"eventSource"`
	UserIdentity struct {
		AccountID string `json:"accountId"`
		Arn       string `json:"arn"`
		UserName  string `json:"userName"`
	} `json:"userIdentity"`
	EventName          string            `json:"eventName"`
	RecipientAccountID string            `json:"recipientAccountId"`
	AwsRegion          string            `json:"awsRegion"`
	RequestParameters  RequestParameters `json:"requestParameters"`
	Resources          []struct {
		Type      string `json:"type"`
		ARN       string `json:"ARN"`
		AccountID string `json:"accountId,omitempty"`
	} `json:"resources"`
	UserAgent       string `json:"userAgent"`
	ManagementEvent bool   `json:"managementEvent"`
}

type RequestParameters struct {
	BucketName string `json:"bucketName"`
	Key        string `json:"key"`
	RoleName   string `json:"roleName"`
}

// log all operations on these buckets
var whitelistedBuckets = map[string]bool{
	"important-bucket": true,
}

// ignored events
var skippedEventNames = map[string]bool{
	"GetObject":                  true,
	"GetBucketPublicAccessBlock": true,
}

func NoisyEvent(trailEvent TrailEvent) bool {
	if _, ok := whitelistedBuckets[trailEvent.RequestParameters.BucketName]; ok {
		return false
	}
	if _, ok := skippedEventNames[trailEvent.EventName]; ok {
		return true
	}
	return false
}

func skipRecord(event []byte) bool {
	var trailEvent TrailEvent
	var err error

	if err = json.Unmarshal(event, &trailEvent); err != nil {
		log.Warnf("Unmarshal: %s", err.Error())
		return false
	}
	if NoisyEvent(trailEvent) {
		return true
	}
	return false
}
