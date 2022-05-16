# Rollback Plan

[v2.1](https://github.com/USDOT-SDC/sdc-dot-gitlab/tree/2.1)

* Log on into the AWS Console for the SDC system account, navigate to the gitlab autoscaling group launch template configuration
* Delete the latest template version so that the previous stable version becomes the latest
* In the autoscaling group instance management view, initiate instance refresh.

