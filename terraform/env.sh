#!/bin/sh

source ../.env

cat <<EOF
{ 
  "line_channel_secret": "$LINE_CHANNEL_SECRET", 
  "line_channel_access_token": "$LINE_CHANNEL_ACCESS_TOKEN", 
  "openai_api_key": "$OPENAI_API_KEY", 
  "github_token": "$GITHUB_TOKEN" 
} 
EOF
