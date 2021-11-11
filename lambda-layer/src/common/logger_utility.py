import logging
import os
import boto3
from common.constants import *


class LoggerUtility:
    @staticmethod
    def get_param(ssm_client, key, default_value=None):
        if key in os.environ.keys():
            topic_arn = os.environ[key]
        else:
            try:
                topic_arn = ssm_client.get_parameter(Name='/log4sdc/' + key)['Parameter']['Value']
            except:
                topic_arn = default_value
        return topic_arn


    @staticmethod
    def init(project='SDC Platform',
             team='',
             sdc_service='',
             component='',
             config=None):
        if not config:
            config = {}

        if not 'project' in config:
            config['project'] = project
        if not 'team' in config:
            config['team'] = team
        if not 'sdc_service' in config:
            config['sdc_service'] = sdc_service
        if not 'component' in config:
            config['component'] = component

        ssm = boto3.client('ssm')
        config['TOPIC_ARN_ERROR'] = LoggerUtility.get_param(ssm_client=ssm, key='TOPIC_ARN_ERROR')
        config['TOPIC_ARN_CRITICAL'] = LoggerUtility.get_param(ssm_client=ssm, key='TOPIC_ARN_CRITICAL')
        config['TOPIC_ARN_ALERT'] = LoggerUtility.get_param(ssm_client=ssm, key='TOPIC_ARN_ALERT')
        config['LOG_LEVEL'] = LoggerUtility.get_param(ssm_client=ssm, key='LOG_LEVEL', default_value=Constants.LOGGER_DEFAULT_LOG_LEVEL)

        LoggerUtility.config = config
        LoggerUtility.setLevel()


    @staticmethod
    def setLevel(level=Constants.LOGGER_DEFAULT_LOG_LEVEL):
        logFormat = '%(asctime)-15s %(levelname)s:%(message)s'
        logging.basicConfig(format=logFormat)
        logger = logging.getLogger(Constants.LOGGER_NAME)

        try:
            logLevel = os.environ[Constants.LOGGER_LOG_LEVEL_ENV_VAR]
        except Exception as e:
            #logLevel = Constants.LOGGER_DEFAULT_LOG_LEVEL
            print(e)
            logLevel = level

        try:
            logger.setLevel(logging.getLevelName(logLevel))
        except Exception as e:
            print(e)
            logLevel = Constants.LOGGER_DEFAULT_LOG_LEVEL

        return True

    @staticmethod
    def logDebug(message, subject='Log4SDC DEBUG', userdata=''):
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.debug('%s', message)
        return True

    @staticmethod
    def logInfo(message, subject='Log4SDC INFO', userdata=''):
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.info('%s', message)
        return True

    @staticmethod
    def logWarning(message, subject='Log4SDC WARNING', userdata=''):
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.warning('%s', message)
        return True

    @staticmethod
    def logError(message, subject='Log4SDC ERROR', userdata=''):
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.error('%s', message)
        client = boto3.client('sns')
        if LoggerUtility.config['TOPIC_ARN_ERROR']:
            response = client.publish(TopicArn=LoggerUtility.config['TOPIC_ARN_ERROR'], Subject=subject, Message=message)
        return True

    @staticmethod
    def logCritical(message, subject='Log4SDC CRITICAL', userdata=''):
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.critical('%s', message)
        client = boto3.client('sns')
        if LoggerUtility.config['TOPIC_ARN_CRITICAL']:
            response = client.publish(TopicArn=LoggerUtility.config['TOPIC_ARN_CRITICAL'], Subject=subject, Message=message)
        return True

    @staticmethod
    def alert(message, subject='Log4SDC ALERT', userdata=''):
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.error('%s', message)
        client = boto3.client('sns')
        if LoggerUtility.config['TOPIC_ARN_ALERT']:
            response = client.publish(TopicArn=LoggerUtility.config['TOPIC_ARN_ALERT'], Subject=subject, Message=message)
        return True

