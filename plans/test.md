# Test Plan

[v1.2](https://github.com/USDOT-SDC/log4sdc/tree/1.2)

## Log message ingest setup
* Log on into the AWS Console for the SDC system account, navigate to the Lambda configuration
* Create a test function with Python 3.7+ runtime
  * The layer is compatible with Python 3.7, 3.8, and 3.9 runtimes
* Add this code to the function:

```
import json
from common.logger_utility import *

def lambda_handler(event, context):

    config = {
    'project': 'FOO', 
    'team': 'FOO-BAR', 
    'sdc_service': 'DATA_INGEST', 
    'component': 'log4sdc-common', 
    }
    
    LoggerUtility.init(config=config)
    LoggerUtility.setLevel('DEBUG')
    LoggerUtility.logDebug("DEBUG Test LoggerUtility")
    LoggerUtility.logInfo("INFO Test LoggerUtility")
    LoggerUtility.logWarning("WARN Test LoggerUtility")
    LoggerUtility.logError("ERROR Test LoggerUtility")
    LoggerUtility.logCritical("CRITICAL Test LoggerUtility")
    LoggerUtility.alert("ALERT Test LoggerUtility")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Log4SDC Lambda!')
    }
```

* Execute function test. Make sure there are no errors and that similar printout is produced:

```
[DEBUG]	2021-10-27T01:04:10.811Z	e81909a0-196c-4bd2-990f-021732be96c6	DEBUG Test LoggerUtility
[INFO]	2021-10-27T01:04:10.811Z	e81909a0-196c-4bd2-990f-021732be96c6	INFO Test LoggerUtility
[WARNING]	2021-10-27T01:04:10.811Z	e81909a0-196c-4bd2-990f-021732be96c6	WARN Test LoggerUtility
[ERROR]	2021-10-27T01:04:10.812Z	e81909a0-196c-4bd2-990f-021732be96c6	ERROR Test LoggerUtility
[CRITICAL]	2021-10-27T01:04:12.052Z	e81909a0-196c-4bd2-990f-021732be96c6	CRITICAL Test LoggerUtility
[ERROR]	2021-10-27T01:04:12.325Z	e81909a0-196c-4bd2-990f-021732be96c6	ALERT Test LoggerUtility
END RequestId: e81909a0-196c-4bd2-990f-021732be96c6
REPORT RequestId: e81909a0-196c-4bd2-990f-021732be96c6	Duration: 1796.73 ms	Billed Duration: 1797 ms	Memory Size: 128 MB	Max Memory Used: 67 MB	Init Duration: 332.22 ms
```

## ElasticSearch log message repository verification
* Log on into ElasticSearch Kibana interface (through AWS console OpenSearch view)
* Navigate to Discover section
* Select "log4sdc-*" index pattern from the drop down control under "Add a filter" 
* Select "This month" for the time range, or another appropriate value to make sure that your messages are included
* Verify that the messages with all data appear in the list of log messages.


