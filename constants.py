DEBUG = False

CURL_TIMEOUT = 10
SLEEP_TIME = 1

NP_CURL = "curl -X GET -H 'Content-type: application/json' 'http://joshjohnson.io/projects/npwebhook/data.php?game_id=%s&v=%s'"
SLACK_CURL = "curl -X POST -H 'Content-type: application/json' --data '%s' %s"
