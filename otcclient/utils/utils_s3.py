#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import boto3
from botocore.exceptions import ClientError
from otcclient.core.OtcConfig import OtcConfig
import os


def createclient( ak , sk, region ):
    otcsession = boto3.session.Session()
    s3client = otcsession.client('s3', region,
                               config=boto3.session.Config(signature_version='s3v4'),
                               endpoint_url="https://"+ OtcConfig.DEFAULT_OBS_HOST,
                               aws_access_key_id=ak,
                               aws_secret_access_key=sk
                               )

    return s3client


def s3init():
    return createclient(OtcConfig.ak, OtcConfig.sk,OtcConfig.region)

def ls_buckets():
    s3client = s3init()
    buckets=None
    try:
        buckets = s3client.list_buckets()["Buckets"]
    except ClientError as e:
        print(str(e))
    return buckets


def ls_bucket(Bucket = None, Prefix = None):
    s3client = s3init()
    result=None
    try:
        result = s3client.list_objects(Bucket=Bucket, Prefix=Prefix)["Contents"]
    except ClientError as e:
        print(str(e))
    return result


def __download_dir(client, dist=None, local='/tmp', bucket='your_bucket'):
    paginator = client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                __download_dir(client,  subdir.get('Prefix'), local)
        if result.get('Contents') is not None:
            for dfile in result.get('Contents'):
                if not os.path.exists(os.path.dirname(local + os.sep + dfile.get('Key'))):
                    os.makedirs(os.path.dirname(local + os.sep + dfile.get('Key')))
                boto3.resource('s3').meta.client.download_file(bucket, dfile.get('Key'), local + os.sep + dfile.get('Key'))

def download_dir(Bucket = None, Prefix = None, Local=None):
    s3client = s3init()
    __download_dir(s3client, Prefix,Local, Bucket)

def upload_dir(Bucket = None, Prefix = None, Local=None):
    s3client = s3init()
    __upload_dir(s3client, Prefix,Local, Bucket)

def __upload_dir(client, dist, local='/tmp', bucket='your_bucket'):
    # enumerate local files recursively
    for root, dirs, files in os.walk(local):    # @UnusedVariable
        for filename in files:
            # construct the full local path
            local_path = os.path.join(root, filename)

            # construct the full path
            relative_path = os.path.relpath(local_path, local)
            s3_path = os.path.join(dist, relative_path)

            # relative_path = os.path.relpath(os.path.join(root, filename))
            print('Searching "%s" in "%s"' % (s3_path, bucket))
            try:
                client.head_object(Bucket=bucket, Key=s3_path)
                print("Path found on S3! Skipping %s..." % s3_path)
                # try:
                    # client.delete_object(Bucket=bucket, Key=s3_path)
                # except:
                    # print ("Unable to delete %s..." % s3_path)
            except:
                print("Uploading %s..." % s3_path)
                client.upload_file(local_path, bucket, s3_path)

def create_bucket(Bucket = None):
    s3client = s3init()
    s3client.create_bucket(Bucket=Bucket)


def delete_bucket(Bucket = None):
    s3client = s3init()
    s3client.delete_bucket(Bucket=Bucket)

def get_bucket_versioning(Bucket = None, Prefix = None):
    s3client = s3init()
    ver = s3client.get_bucket_versioning(Bucket=Bucket)
#    ver = s3client.BucketVersioning(Bucket=Bucket).get_available_subresources()

    return ver

def list_object_versions(Bucket = None, Prefix = None):
    s3client = s3init()
    ver = s3client.get_bucket_versioning(Bucket=Bucket)["Contents"]
    return ver

def delete_object(Bucket = None, Prefix = None):
    s3client = s3init()
    bucket = s3client.Bucket(Bucket)
    for obj in bucket.objects.filter(Prefix=Prefix):
        print(s3client.Object(bucket.name, obj.key).etag[1 :-1])
        s3client.Object(bucket.name, obj.key).delete()

def upload_file(File=None,Bucket = None, Prefix = None):
    s3client = s3init()
    s3client.upload_file(File, Bucket, Prefix)

def download_file(Bucket = None, Prefix = None, File=None):
    s3client = s3init()
    s3client.download_file(Bucket, Prefix,File)

def sync():
    raise RuntimeError( "not implemented yet")
