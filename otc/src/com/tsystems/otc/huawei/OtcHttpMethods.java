/* 
 * Copyright (c) 2016 T-Systems GmbH
 * Germany
 * All rights reserved.
 * 
 * Name: ParamFactory.java
 * Author: zsonagy
 * Datum: 08.03.2016
 */

package com.tsystems.otc.huawei;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

import org.apache.http.HttpResponse;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.cloud.sdk.http.HttpMethodName;
import com.tsystems.otc.config.OtcConfig;
import com.tsystems.otc.huawei.AccessService;
import com.tsystems.otc.huawei.AccessServiceImpl;

/***
 * HTTP Methods class to implement GET/POST/PUT/DELETE methods to OTC calls 
 * @author zsonagy
 *
 */
public class OtcHttpMethods {
	
	static final Logger log = LogManager.getLogger(OtcHttpMethods.class.getName());

	public static String put(String requestUrl, String putBody) {
		String ret="";
		
		AccessService accessService = null;
		try {
			accessService = new AccessServiceImpl(OtcConfig.serviceName,
					OtcConfig.region, OtcConfig.sk, OtcConfig.sk);
			URL url = new URL(requestUrl);
			HttpMethodName httpMethod = HttpMethodName.PUT;

			InputStream content = new ByteArrayInputStream(putBody.getBytes());
			HttpResponse response = accessService.access(url, content,
					(long) putBody.getBytes().length, httpMethod);

			ret = convertStreamToString(response.getEntity().getContent());
					//getStatusLine().get();
	
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			accessService.close();
		}
		return ret;
	}

	public static String patch(String requestUrl, String putBody) {

		String ret=null;
		AccessService accessService = null;
		try {
			accessService = new AccessServiceImpl(OtcConfig.serviceName,
					OtcConfig.region, OtcConfig.ak, OtcConfig.sk);
			URL url = new URL(requestUrl);
			HttpMethodName httpMethod = HttpMethodName.PATCH;
			InputStream content = new ByteArrayInputStream(putBody.getBytes());
			HttpResponse response = accessService.access(url, content,
					(long) putBody.getBytes().length, httpMethod);

			ret = convertStreamToString(response.getEntity()
					.getContent());
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			accessService.close();
		}

		return ret;
	}

	public static String delete(String requestUrl) {

		String ret = null;
		AccessService accessService = null;

		try {
			accessService = new AccessServiceImpl(OtcConfig.serviceName,
					OtcConfig.region, OtcConfig.ak, OtcConfig.sk);
			URL url = new URL(requestUrl);
			HttpMethodName httpMethod = HttpMethodName.DELETE;

			HttpResponse response = accessService.access(url, httpMethod);
			ret = convertStreamToString(response.getEntity()
					.getContent());
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			accessService.close();
		}
		return ret;

	}

	public static String get(String requestUrl) {
		String ret = null;

		AccessService accessService = null;

		try {
			accessService = new AccessServiceImpl(OtcConfig.serviceName,
					OtcConfig.region, OtcConfig.ak, OtcConfig.sk);
			URL url = new URL(requestUrl);
			HttpMethodName httpMethod = HttpMethodName.GET;
			HttpResponse response;
			response = accessService.access(url, httpMethod);
			ret = convertStreamToString(response.getEntity().getContent());
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			accessService.close();
		}

		return ret;
	}

	public static String post(String requestUrl, String postbody) {

		String ret = null;
		AccessService accessService = new AccessServiceImpl(
				OtcConfig.serviceName, OtcConfig.region, OtcConfig.ak,
				OtcConfig.sk);
		URL url = null;
		try {
			url = new URL(requestUrl);
		} catch (MalformedURLException e) {
			e.printStackTrace();
		}
		InputStream content = new ByteArrayInputStream(postbody.getBytes());
		HttpMethodName httpMethod = HttpMethodName.POST;
		HttpResponse response;

		try {
			response = accessService.access(url, content,
					(long) postbody.getBytes().length, httpMethod);
			if( response.getHeaders("X-Subject-Token").length > 0)
			{
				OtcConfig.TOKEN = response.getHeaders("X-Subject-Token")[0].getValue();
			}
						
			ret = convertStreamToString(response.getEntity()
					.getContent());
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			accessService.close();
		}
		return ret;
	}

	private static String convertStreamToString(InputStream is) {
		BufferedReader reader = new BufferedReader(new InputStreamReader(is));
		StringBuilder sb = new StringBuilder();

		String line = null;
		try {
			while ((line = reader.readLine()) != null) {
				sb.append(line + "\n");
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				is.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

		return sb.toString();
	}

}