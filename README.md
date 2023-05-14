 # Replit Bounty: Twitter API 

**Deploy a simple serverless API endpoint on AWS lambda** that I can hit with an up-to-15-character twitter username in a query param, and it will automatically send them a password reset email (or any other email from Twitter) via calling Twitters systems -- you can use the API if you wish but I think it will be impossible, so you'll likely have to use Puppeteer or another browser emulation endpoint. Errors should gracefully pass on the caller.

It should also come with a test, and be extensible enough that I can easily adapt it to Github or any other service with a password reset email (that will be the next task if this works).

## Acceptance Criteria
Include a Github or other experience. The best application will be one that has already built as much of it as possible.

# Solution 
[arn:aws:lambda:us-east-1:755164003878:function:twitter-api
](https://fsmx2z5i2ps6s4mqfalv63jot40qazbj.lambda-url.us-east-1.on.aws/)
## How to extend this solution 

```bash

# Clone this repository
$ git clone https://github.com/LNshuti/twitter-api.git

# Go into the repository
$ cd twitter-api

# Activate environment
conda env create -f environment.yml

# Run the app
$ python app.py


