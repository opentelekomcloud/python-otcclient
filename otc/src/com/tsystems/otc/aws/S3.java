/* 
 * Copyright (c) 2016 T-Systems GmbH
 * Germany
 * All rights reserved.
 * 
 * Name: ParamFactory.java
 * Author: zsonagy
 * Datum: 08.03.2016
 */

package com.tsystems.otc.aws;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.S3ClientOptions;
import com.amazonaws.services.s3.model.AccessControlList;
import com.amazonaws.services.s3.model.Bucket;
import com.amazonaws.services.s3.model.CannedAccessControlList;
import com.amazonaws.services.s3.model.CanonicalGrantee;
import com.amazonaws.services.s3.model.CreateBucketRequest;
import com.amazonaws.services.s3.model.DeleteBucketRequest;
import com.amazonaws.services.s3.model.DeleteObjectRequest;
import com.amazonaws.services.s3.model.GeneratePresignedUrlRequest;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.Grant;
import com.amazonaws.services.s3.model.GroupGrantee;
import com.amazonaws.services.s3.model.ObjectListing;
import com.amazonaws.services.s3.model.Permission;
import com.amazonaws.services.s3.model.S3Object;
import com.amazonaws.services.s3.model.S3ObjectSummary;
import com.amazonaws.services.s3.transfer.MultipleFileDownload;
import com.amazonaws.services.s3.transfer.MultipleFileUpload;
import com.amazonaws.services.s3.transfer.TransferManager;
import com.amazonaws.services.s3.transfer.Upload;
import com.tsystems.otc.config.OtcConfig;
import com.tsystems.otc.imp.DefaultOtcOutputHandler;
import com.tsystems.otc.interfaces.IOtcOutputHandler;
import com.tsystems.otc.params.ParamFactory;

/**
 * S3 Fucntion implementation of OTC client tool
 * @author zsonagy
 */
public class S3 {
	/** just for testing the json file */

    AmazonS3       s3;
    IOtcOutputHandler otcOutputHandler = new DefaultOtcOutputHandler(); 
    
	public void example ( String [] args ) {	
		   init();
        /*
         * Amazon S3
         *
         * The AWS S3 client allows you to manage buckets and programmatically
         * put and get objects to those buckets.
         *
         * In this sample, we use an S3 client to iterate over all the buckets
         * owned by the current user, and all the object metadata in each
         * bucket, to obtain a total object and space usage count. This is done
         * without ever actually downloading a single object -- the requests
         * work with object metadata only.
         */
        try {
            List<Bucket> buckets = s3.listBuckets();

            long totalSize  = 0;
            int  totalItems = 0;
            for (Bucket bucket : buckets) {
                /*
                 * In order to save bandwidth, an S3 object listing does not
                 * contain every object in the bucket; after a certain point the
                 * S3ObjectListing is truncated, and further pages must be
                 * obtained with the AmazonS3Client.listNextBatchOfObjects()
                 * method.
                 */
                ObjectListing objects = s3.listObjects(bucket.getName());
                do {
                    for (S3ObjectSummary objectSummary : objects.getObjectSummaries()) {
                        totalSize += objectSummary.getSize();
                        totalItems++;
                    }
                    objects = s3.listNextBatchOfObjects(objects);
                } while (objects.isTruncated());
            }

            System.out.println("You have " + buckets.size() + " Amazon S3 bucket(s), " +
                    "containing " + totalItems + " objects with a total size of " + totalSize + " bytes.");
        } catch (AmazonServiceException ase) {
            /*
             * AmazonServiceExceptions represent an error response from an AWS
             * services, i.e. your request made it to AWS, but the AWS service
             * either found it invalid or encountered an error trying to execute
             * it.
             */
            System.out.println("Error Message:    " + ase.getMessage());
            System.out.println("HTTP Status Code: " + ase.getStatusCode());
            System.out.println("AWS Error Code:   " + ase.getErrorCode());
            System.out.println("Error Type:       " + ase.getErrorType());
            System.out.println("Request ID:       " + ase.getRequestId());
        } catch (AmazonClientException ace) {
            /*
             * AmazonClientExceptions represent an error that occurred inside
             * the client on the local host, either while trying to send the
             * request to AWS or interpret the response. For example, if no
             * network connection is available, the client won't be able to
             * connect to AWS to execute a request and will throw an
             * AmazonClientException.
             */
            System.out.println("Error Message: " + ace.getMessage());
        }
    }

	private void init() {
	    ClientConfiguration clientConfiguration = null;
	    if (OtcConfig.PROXY_URL != null && OtcConfig.PROXY_URL.length() > 0 ) {
		    clientConfiguration = new ClientConfiguration();	    
	        clientConfiguration.setProxyDomain(OtcConfig.PROXY_URL);
	        clientConfiguration.setProxyPort(OtcConfig.PROXY_PORT);
			s3 = new AmazonS3Client( new BasicAWSCredentials(
				    // provide access key and secret key
				   OtcConfig.ak,
				   OtcConfig.sk
				  ) ,clientConfiguration );
	        
	    }
	    else{

		s3 = new AmazonS3Client( new BasicAWSCredentials(
				    // provide access key and secret key
				   OtcConfig.ak,
				   OtcConfig.sk
				  )  );

	    }

	
	    
				  s3.setEndpoint( OtcConfig.S3_HOSTNAME );
				  
				  
				  /*
				   // REGION definition not correct in S3 donwload THIS HAVE TO BE checked 
				  Region or = RegionUtils.getRegionByEndpoint(OtcConfig.S3_HOSTNAME);
				  Region eude_region = RegionUtils.getRegion("eu-de");
 
				  RegionImpl myregion = new RegionImpl() {
					
					@Override
					public boolean isServiceSupported(String arg0) {
						
						return true;
					}
					
					@Override
					public boolean hasHttpsEndpoint(String arg0) {
						
						return true;
					}
					
					@Override
					public boolean hasHttpEndpoint(String arg0) {
						
						return false;
					}
					
					@Override
					public String getServiceEndpoint(String arg0) {
						
						return OtcConfig.S3_HOSTNAME;
					}
					
					@Override
					public String getName() {
						
						return "eu-de";
					}
					
					@Override
					public String getDomain() {
						
						return "otc.t-systems.com";
					}
					
					@Override
					public Collection<String> getAvailableEndpoints() {
						Collection<String> stra = new ArrayList<String>();
						stra.add(OtcConfig.S3_HOSTNAME);
						return stra;
					}
				};
				 s3.setRegion( new Region (myregion));	 
			*/
			
				 
						

				  // configure path-style S3 access if desired
				  s3.setS3ClientOptions( new S3ClientOptions() .withPathStyleAccess( false ) );
	}

	public void listBuckets() {
		init();
	
		List<Bucket> buckets = s3.listBuckets();
		
		List<List<String>> rows= new ArrayList<List<String>>();
        List<String> headers = Arrays.asList("Bucketname", "Owner","Owner Id");

		for (Bucket bucket : buckets) {				
			List<String> str = Arrays.asList(bucket.getName(),bucket.getOwner().getDisplayName(),bucket.getOwner().getId());
			rows.add(str);
		}
				
		otcOutputHandler.pretyPrint(rows, headers);
		
	}	

	@SuppressWarnings("unused")
	public void listBucketContent(String aBucketName) {
		init();
        long totalSize  = 0;
        int  totalItems = 0;
        List<String> headers = Arrays.asList("File", "Size" /*, "Url" TODO NOT IMPLEMENTED YET*/);
		List<List<String>> rows= new ArrayList<List<String>>();

			
        ObjectListing objects = s3.listObjects(aBucketName);
        do {
        	
            for (S3ObjectSummary objectSummary : objects.getObjectSummaries()) {
            	GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest(aBucketName, objectSummary.getKey());
            	
            	List<String> str = Arrays.asList(objectSummary.getKey(),String.valueOf( objectSummary.getSize()));
            	
            	
            	//request.
            	rows.add(str);    
            	totalSize += objectSummary.getSize();
                totalItems++;
            }
            objects = s3.listNextBatchOfObjects(objects);
        } while (objects.isTruncated());
        otcOutputHandler.pretyPrint(rows, headers);        
    	System.out.print("totalItems: "+ totalItems +  "\t"  + "totalSize: "+ totalSize );
	}	

	
	public void download( String aTarget ) throws MalformedURLException
	{
		init();		
	    TransferManager tx = null;
	    try {
	        tx = new TransferManager(s3);
	        
	        File tf = new File(aTarget);
	        if( OtcConfig.S3RECURSIVE )
	        {
		        MultipleFileDownload downloadDir= tx.downloadDirectory(OtcConfig.S3BUCKET, OtcConfig.S3OBJECT, tf);
		        downloadDir.waitForCompletion();
		        System.out.println("Transfered byte: " + downloadDir.getProgress().getTotalBytesToTransfer());
	        }
	        else
	        {	
	        	System.out.println(OtcConfig.S3BUCKET);
	        	System.out.println(OtcConfig.S3OBJECT);
	        	System.out.println(aTarget);
	        	
		        GetObjectRequest por = new GetObjectRequest(OtcConfig.S3BUCKET, OtcConfig.S3OBJECT);
		        
		        S3Object obj = s3.getObject(por);
		        obj.getObjectContent();
		        
		        Files.copy(obj.getObjectContent(), tf.toPath());
		        

	        	//Download download = tx.download(OtcConfig.S3BUCKET, OtcConfig.S3OBJECT, tf);	        
		        //download.waitForCompletion();
	        }
	    } catch (InterruptedException | IOException e) {
	        throw new IllegalStateException("Interrupted when uploading the image to S3", e);
	        }	    
	    finally {
	        if (tx != null) {
	        	
	            tx.shutdownNow();
	        }
	    }		
	}

	public void upload( String aSoruce ) throws MalformedURLException
	{
		init();		
	    TransferManager tx = null;
	    try {
	        tx = new TransferManager(s3);
	        File sourcefile = new File(aSoruce);
	        if( sourcefile.isDirectory() )
	        {
		        MultipleFileUpload uploadDir = tx.uploadDirectory(OtcConfig.S3BUCKET, OtcConfig.S3OBJECT, sourcefile,OtcConfig.S3RECURSIVE );
		        uploadDir.waitForCompletion();
	        }
	        else
	        {
	        	System.out.println(OtcConfig.S3BUCKET);
	        	System.out.println(OtcConfig.S3OBJECT);
	        	System.out.println(sourcefile);
	        	
		        Upload upload = tx.upload(OtcConfig.S3BUCKET, OtcConfig.S3OBJECT, sourcefile );
// ALTERNATE SOLUTION		        
//		        PutObjectRequest por = new PutObjectRequest(bucketName, targetFile, sourcefile);
//		        por.setCannedAcl(CannedAccessControlList.PublicRead);
//		        s3.putObject(por);		        
		        com.amazonaws.services.s3.transfer.model.UploadResult resfile = upload.waitForUploadResult();
		        System.out.println("Upload result:" + resfile.getKey() );
	        }
	    } catch (InterruptedException e) {
	        throw new IllegalStateException("Interrupted when uploading the image to S3", e);
	        }	    

	    finally {
	        if (tx != null) {
	        	
	            tx.shutdownNow();
	        }
	    }		
	}
	
	
	
	@SuppressWarnings({ "unused", "deprecation" })
	public String AclExample( String bucketName )
	{
		init();
		
		Collection<Grant> grantCollection = new ArrayList<Grant>();
		
        // 1. Create bucket with Canned ACL.
        CreateBucketRequest createBucketRequest = 
        	new CreateBucketRequest(bucketName).withCannedAcl(CannedAccessControlList.LogDeliveryWrite);  
        
        Bucket resp = s3.createBucket(createBucketRequest);

        // 2. Update ACL on the existing bucket.
        AccessControlList bucketAcl = s3.getBucketAcl(bucketName);
       
        
        // (Optional) delete all grants.
        bucketAcl.getGrants().clear();
        
        // Add grant - owner.
        Grant grant0 = new Grant(
        		new CanonicalGrantee("852b113e7a2f25102679df27bb0ae12b3f85be6f290b936c4393484beExample"), 
        		Permission.FullControl);
        grantCollection.add(grant0);       
        
        // Add grant using canonical user id.
        Grant grant1 = new Grant(
        		new CanonicalGrantee("d25639fbe9c19cd30a4c0f43fbf00e2d3f96400a9aa8dabfbbebe1906Example"),
        		Permission.Write);        
        grantCollection.add(grant1);
                   
        // Grant LogDelivery group permission to write to the bucket.
        Grant grant3 = new Grant(GroupGrantee.LogDelivery, 
        		                 Permission.Write);
        grantCollection.add(grant3);
        
       bucketAcl.getGrants().addAll(grantCollection);

        // Save (replace) ACL.
        s3.setBucketAcl(bucketName, bucketAcl);
		return bucketName;
		
	}

	public void fileCopy(String aFrom,String aTo ) throws MalformedURLException {
		
		if( aFrom == null || aTo == null ) 
		{
			System.out.println("S3 Copy error. Please add params correctly. ");
			ParamFactory.printHelp(); 
			System.exit(1);
		}
		
		if( aFrom.startsWith("s3://") )
		{
			fillS3Values(aFrom);
			download(aTo);
			
		}
		else if( aTo.startsWith("s3://") ) 
		{
			fillS3Values(aTo);			
			upload(aFrom);
		}

		
	}

	private void fillS3Values(String s3Path) {
		String temp = s3Path.replaceAll("s3://", "");
		OtcConfig.S3BUCKET = temp.substring(0,temp.indexOf("/"));
		OtcConfig.S3OBJECT= temp.substring(temp.indexOf("/") +1 );
	}


	public void createBucket() {
		init();
		//
		Bucket bucket = s3.createBucket(OtcConfig.S3BUCKET,OtcConfig.region);
		System.out.println("Bucket created: "+ bucket.getName());
		
		
	}

	public void getObject() throws IOException {
		init();
		S3Object obj = s3.getObject(OtcConfig.S3BUCKET,OtcConfig.S3OBJECT);        	
		InputStream reader = new BufferedInputStream(
				   obj.getObjectContent());
				int read = -1;

				while ( ( read = reader.read() ) != -1 ) {
					System.out.print(read);				 
				}
				reader.close();
	}

	public void remove(String input) {
		
		init();
		fillS3Values(input);
		
		if( OtcConfig.S3OBJECT == null || OtcConfig.S3OBJECT.length() ==  0 )
		{
			s3.deleteObject(new DeleteObjectRequest(OtcConfig.S3BUCKET, OtcConfig.S3OBJECT));
		}
		else
		{
			s3.deleteBucket(new DeleteBucketRequest(OtcConfig.S3BUCKET));
		}
			 
		System.out.println("Deleted object: "+ OtcConfig.S3BUCKET + OtcConfig.S3OBJECT);		
	}
}
	
