/* 
 * Copyright (c) 2016 T-Systems GmbH	
 * Germany
 * All rights reserved.
 * 
 * Name: ParamFactory.java
 * Author: zsonagy
 * Datum: 08.03.2016
 */

package com.tsystems.otc.config;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.InputMismatchException;
import java.util.Properties;
import java.util.Scanner;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.tsystems.otc.OtcMain;
import com.tsystems.otc.imp.DefaultOtcServiceCalls;
import com.tsystems.otc.interfaces.IOtcServiceCalls;
import com.tsystems.otc.params.UserInput;

/**
 * Utility class to load / persist configuration properties 
 * 
 * @author zsonagy
 */
public class ConfigLoader {
	static final Logger log = LogManager.getLogger(OtcMain.class.getName());


	/**
	 * Factory for config from file
	 * @param jsonFileName
	 * @return Config tree according for json file
	 * @throws JsonParseException
	 * @throws JsonMappingException
	 * @throws IOException
	 */
	public static OtcConfig loadOtcConfig( String jsonFileName ) throws JsonParseException, JsonMappingException, IOException {
		OtcConfig conf = null;
		ObjectMapper mapper = new ObjectMapper();
		InputStream globalConfigFileStream;
		System.out.println(jsonFileName);
		
		if (  new File(jsonFileName).exists()  )
		{
			globalConfigFileStream = new FileInputStream( jsonFileName );
		}
		else
		{
			globalConfigFileStream = new OtcConfig().getClass().getResourceAsStream("/" + jsonFileName); 
		}
		

		conf = mapper.readValue( globalConfigFileStream, OtcConfig.class );
		return conf;
	}
	
	

	public static Properties getVersion()
	{		 
		     Properties prop = new Properties();
		     try {
		         prop.load(OtcMain.class.getResourceAsStream("/version.txt"));
		     } catch (IOException e) {
		    	 System.out.println("Fatal error! No version file avaliable!");
		    	 System.exit(0);
		     }	 
		     return prop;
	}
	
	public static void printVersion()
	{
		Properties prop = getVersion(); 
		 System.out.println("Starting App version: "+prop.getProperty("version"));
		 System.out.println("Build date: "+prop.getProperty("build.date"));

	}



	public static void readUserValues() {
		Properties props = new Properties();
		log.debug("start getUserValues");
		
		try {
			props.load(new FileInputStream(OtcConfig.OTC_USER_FILE));
		} catch (IllegalArgumentException | IOException e) {
			log.warn(
					"NZS: lastPoolingDatedDictionary not avaliable yet.First start?",
					e);
		}
		
		
		OtcConfig.USERNAME = System.getenv("OS_USERNAME");
		OtcConfig.PASSWORD = System.getenv("OS_PASSWORD");
		OtcConfig.DOMAIN = System.getenv("OS_USER_DOMAIN_NAME");
		

		OtcConfig.ak = System.getenv("S3_ACCESS_KEY_ID");
		OtcConfig.sk = System.getenv("S3_SECRET_ACCESS_KEY");
		OtcConfig.PROJECT_ID = System.getenv("PROJECT_ID");
		
		
		
		if( OtcConfig.USERNAME == null ) 
		{
			OtcConfig.USERNAME = props.getProperty("username");
		}
		else
		{
			if( OtcConfig.USERNAME.contains("\""))
			{
				OtcConfig.USERNAME = OtcConfig.USERNAME.replace("\"", "");
			}			
		}
		
		if( OtcConfig.PASSWORD == null ) 
		{
			OtcConfig.PASSWORD = props.getProperty("apikey");
		}
		else
		{
			if( OtcConfig.PASSWORD.contains("\""))
			{
				OtcConfig.PASSWORD = OtcConfig.PASSWORD.replace("\"", "");
			}			
		}

		if( OtcConfig.DOMAIN == null ) 
		{
			if( OtcConfig.USERNAME != null ) {
			OtcConfig.DOMAIN = OtcConfig.USERNAME.split(" ")[1];
			}
		}
		
	
		
		if( OtcConfig.ak == null ) 
		{
			OtcConfig.ak = props.getProperty("otc_access_key_id");
		}
		else
		{
			if( OtcConfig.ak.contains("\""))
			{
				OtcConfig.ak= OtcConfig.ak.replace("\"", "");
			}			
		}
		
		if( OtcConfig.sk == null ) 
		{
			OtcConfig.sk = props.getProperty("otc_secret_access_key");
		}
		else
		{
			if( OtcConfig.sk.contains("\""))
			{
				OtcConfig.sk= OtcConfig.sk.replace("\"", "");
			}			
		}
		

		if( OtcConfig.PROJECT_ID == null ) 
		{
			OtcConfig.PROJECT_ID = props.getProperty("project_id");
		}
		else
		{
			if( OtcConfig.PROJECT_ID.contains("\""))
			{
				OtcConfig.PROJECT_ID = OtcConfig.PROJECT_ID.replace("\"", "");
			}			
		}
		
		
		
		OtcConfig.resetUrlVars();		
	}



	public static void readProxyValues() {
		Properties props = new Properties();
		log.debug("start getProxyValues");
		
		try {
			props.load(new FileInputStream(OtcConfig.OTC_PROXY_FILE));
		} catch (Exception e) {
			log.warn(
					"No Proxy file exist!",
					e);
			return;
		}
		
		OtcConfig.PROXY_URL = props.getProperty("proxy_host");		
		String temp = props.getProperty("proxy_port");
		OtcConfig.PROXY_PORT = Integer.parseInt(temp);
				
	}



	public static void reSetUserValues() {		
		readUserValues();		 
		UserInput.getAuthKeys();	
		ConfigLoader.persistUserValues();
	}



	public static void persistProxyValues() {
		Properties props = new Properties();
		props.setProperty("proxy_host",OtcConfig.PROXY_URL);
		props.setProperty("proxy_port",String.valueOf(OtcConfig.PROXY_PORT)) ;
	
		new File( OtcConfig.OTC_USER_DIR).mkdirs();
		try {
			File f = new File(OtcConfig.OTC_PROXY_FILE);
			OutputStream out = new FileOutputStream(f);
			props.store(out,
					"Otc Common Information");
		} catch (Exception e) {
			log.error("Error during save keys/date pairs", e);
		}
	}



	public static void persistUserValues() {
		Properties props = new Properties();
		//props.setProperty("project_id",OtcConfig.PROJECT_ID);
		props.setProperty("otc_access_key_id",OtcConfig.ak );
		props.setProperty("otc_secret_access_key",OtcConfig.sk);

		props.setProperty("username",OtcConfig.USERNAME );
		props.setProperty("apikey",OtcConfig.PASSWORD);		
		
		new File( OtcConfig.OTC_USER_DIR).mkdirs();
		try {	
			File f = new File(OtcConfig.OTC_USER_FILE);
			OutputStream out = new FileOutputStream(f);
			props.store(out,
					"Otc User Information");
		} catch (Exception e) {
			log.error("Error during save keys/date pairs", e);
		}
	}



	public static void reSetProxyValues() {
		
		readProxyValues();
		
		UserInput.getProxyKeys();
		
		persistProxyValues();
	}



	public static void validateConfig() throws IOException {

		if( OtcConfig.USERNAME != null && OtcConfig.USERNAME.length() == 32 &&
			OtcConfig.PASSWORD != null && OtcConfig.PASSWORD.length() == 32 && 
			OtcConfig.DOMAIN!= null && OtcConfig.DOMAIN.length() == 23 )
		{
			IOtcServiceCalls otcServiceCalls = new DefaultOtcServiceCalls(); 
			otcServiceCalls.getIamToken();
		}
		else if( OtcConfig.ak != null && OtcConfig.ak .length() == 32 &&
				OtcConfig.sk != null && OtcConfig.sk.length() == 32  ) 			
		{
			
		}
		else
		{
        	throw new InputMismatchException();
		}

	}
}
