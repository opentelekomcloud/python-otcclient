/* 
 * Copyright (c) 2016 T-Systems GmbH
 * Germany
 * All rights reserved.
 * 
 * Name: ParamFactory.java
 * Author: zsonagy
 * Datum: 08.03.2016
 */

package com.tsystems.otc.params;

import java.util.InputMismatchException;
import java.util.Scanner;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.tsystems.otc.config.OtcConfig;

/**
 * Handling the following input from console: - User information - Proxy
 * information
 * 
 * @author zsonagy
 */
public class UserInput {

	static final Logger log = LogManager.getLogger(UserInput.class.getName());
	static Scanner scan;

	public static void getProxyKeys() {
		UserInput.scan = new Scanner(System.in);
		OtcConfig.PROXY_URL = getUserTypedValue("Enter a proxy host:", -1);
		OtcConfig.PROXY_PORT = Integer.parseInt(getUserTypedValue(
				"Enter a proxy port:", 4));
		UserInput.scan.close();
	}

	public static void getAuthKeys() {
		UserInput.scan = new Scanner(System.in);
		OtcConfig.USERNAME = getUserTypedValue("Enter a Username:", 32);
		OtcConfig.PASSWORD = getUserTypedValue("Enter a API Key:", 32);

		OtcConfig.DOMAIN = OtcConfig.USERNAME.split(" ")[1];

		// OtcConfig.PROJECT_ID = getUserTypedValue("Enter a Project ID:", 32);
		OtcConfig.ak = getUserTypedValue("Enter a Access Key:", -1);
		OtcConfig.sk = getUserTypedValue("Enter a Secret Key:", -1);

		UserInput.scan.close();
	}

	private static String getUserTypedValue(String title, int len) {
		boolean validData = false;
		String val = null;
		do {
			System.out.println(title);
			try {
				val = scan.nextLine();// tries to get data. Goes to catch if
										// invalid data
				if (val != null && (val.length() == len || len <= 0)) {
					validData = true;// if gets data successfully, sets boolean
										// to true
				} else {
					throw new InputMismatchException();
				}
			} catch (Exception e) {
				// executes when this exception occurs
				// e.printStackTrace();
				System.out.println("Input has to be a correct. ");
			}
		} while (validData == false);// loops until validData is true
		// scan.close();
		return val;
	}

}
