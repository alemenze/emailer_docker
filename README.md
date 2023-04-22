# Docker container to send emails during workflows
[![run with docker](https://img.shields.io/badge/run%20with-docker-0db7ed?labelColor=000000&logo=docker)](https://www.docker.com/)
[![run with singularity](https://img.shields.io/badge/run%20with-singularity-1d355c.svg?labelColor=000000)](https://sylabs.io/docs/)

This project is meant to containerize an email process to allow sending of status emails from workflows. 

## Build new image with outgoing email info
First you must build your own image to contain the appropriate outgoing email. An example environment file has been included- generate your own .env file containing the MAILSENDER and MAILPASSWORD.

From my own pain and testing, Gmail is no longer viable for easy setup. It can be done, but with major customization. Protonmail can be used with only mild customization. 
As of initial building, the easiest was getting a [free outlook account](https://outlook.live.com/owa/). 

## Running image
Once you have created a new .env file with MAILSENDER and MAILPASSWORD, simply build the container `docker build . -t emailer`. If you wish you can push it to dockerhub or similar, or use it with local execution. 

From there, you can flexibly insert this into any workflow you use. Have a script to request an HPC node for RStudio? Have this spit out the tunnel info to an email. Have pipelines running around? Add this to the end to send over a summary or jobs done notification. 

### Run as docker
When running this container, call it as:
```
docker run emailer "recipient_email" "email_subject" "email_body"
```

### Run as singularity
```
singularity exec docker://emailer python3 /app/emailer.py \
   "recipient_email" \
   "email_subject" \
   "email_body"
```