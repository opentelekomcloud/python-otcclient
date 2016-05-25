/* 
 * Copyright (c) 2016 T-Systems GmbH
 * Germany
 * All rights reserved.
 * 
 * Name: ParamFactory.java
 * Author: zsonagy
 * Datum: 08.03.2016
 */

package com.tsystems.otc.imp;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.eclipsesource.json.JsonArray;
import com.eclipsesource.json.JsonObject;
import com.eclipsesource.json.JsonValue;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.jayway.jsonpath.JsonPath;
import com.tsystems.otc.OtcMain;
import com.tsystems.otc.config.OtcConfig;
import com.tsystems.otc.interfaces.IOtcOutputHandler;
import com.tsystems.otc.tableoutput.Block;
import com.tsystems.otc.tableoutput.Board;
import com.tsystems.otc.tableoutput.Table;

/**
 * Provide Output function to OTC Service calls  
 * 
 * @author zsonagy
 *
 */
public class DefaultOtcOutputHandler implements IOtcOutputHandler {

	final Logger log = LogManager.getLogger(DefaultOtcOutputHandler.class.getName());

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcOutputHandler#printLevel3(java.lang.String, java.lang.String, java.lang.String, java.util.List)
	 */
	@Override
	@SuppressWarnings("unchecked")
	public void printLevel3(String json, String mainKey,
			String level2Key, List<String> subkeys) {
		try {
			List<HashMap<String, Object>> listKeys = 
					parseJsontoTopLevelList(json, mainKey);

			
			if (OtcConfig.QUERY != null ) {				
				 handleQuery(json);	
				return;
			}
			
			if ("JSON".equalsIgnoreCase(OtcConfig.OUTPUT_FORMAT)) {
				jsonPretyPrint(json);
				return;
			}
			


			 JsonPath path  = JsonPath.read(json, OtcConfig.QUERY );
			 System.out.print(path);
			
			List<List<String>> rows = new ArrayList<List<String>>();

			if (listKeys == null)
				return;

			for (HashMap<String, Object> map : listKeys) {
				List<String> strv2 = new ArrayList<String>();

				HashMap<String, Object> mapsub = (HashMap<String, Object>) map
						.get(level2Key);

				for (String viewItem : subkeys) {						
							String value = (String) mapsub.get(viewItem);						
							strv2.add(value);																			
					}
					rows.add(strv2);

				}
			
//			System.out.println(Arrays.toString(subkeys.toArray()));
//			System.out.println(Arrays.toString(rows.toArray()));
			pretyPrint(rows, subkeys);
		} catch (IOException e) {
			System.out.println("Table output format error: " + e.getMessage());
			System.out.print(json);
		
			log.error(e);
		}
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcOutputHandler#printLevel2(java.lang.String, java.lang.String, java.util.List)
	 */
	@Override
	@SuppressWarnings("unchecked")
	public void printLevel2(String json, String mainKey,
			List<String> subkeys) {
		try {
			List<HashMap<String, Object>> listKeys = 
					parseJsontoTopLevelList(json, mainKey);

			
			if (OtcConfig.QUERY != null ) {				
				 handleQuery(json);	
				return;
			}
			
			
			if ("JSON".equalsIgnoreCase(OtcConfig.OUTPUT_FORMAT)) {
				jsonPretyPrint(json);
				return;
			}

			List<List<String>> rows = new ArrayList<List<String>>();
			List<String> subkeys2 = new ArrayList<String>();
			// subkeys2.addAll(subkeys);

			if (listKeys == null)
				return;

			
			for (HashMap<String, Object> map : listKeys) {
				// List<HashMap<String,Object>> links = (List)
				// map.getOrDefault("links",null);
				List<String> strv2 = new ArrayList<String>(); // Arrays.asList(objectSummary.getKey(),String.valueOf(
																// objectSummary.getSize())
																// );

				// System.out.println("main");
				for (String viewItem : subkeys) {

					if (viewItem.contains(":")) {
						// String viewkey =
						// viewItem.substring(0,viewItem.indexOf(":"));

						// HashMap<String, Object> mapsub= (HashMap<String,
						// Object>) map.get(viewkey) ;
						// String[] viewKeyItems =
						// viewItem.substring(viewItem.indexOf(":")
						// +1).split(",");

						// for (String item : viewKeyItems) {
						// strv2.add(item);
						// //str.append(mapsub.getOrDefault(item, null) + "\t");
						// }

						List<String> strv3 = new ArrayList<String>(); // Arrays.asList(objectSummary.getKey(),String.valueOf(
																		// objectSummary.getSize())
																		// );

						String viewkey = viewItem.substring(0,
								viewItem.indexOf(":"));
						String[] viewKeyItems = viewItem.substring(
								viewItem.indexOf(":") + 1).split(",");

						HashMap<String, Object> mapsub = (HashMap<String, Object>) map
								.get(viewkey);

						for (String item : viewKeyItems) {
							subkeys2.add(item);
						}

						for (String val : mapsub.keySet()) {
							String aaa = (String) mapsub.get(val);

							// ~~~~~for (String item : viewKeyItems) {

							strv3.add(aaa);
							rows.add(strv3);
							// }
						}

						/*
						 * for (String val : mapsub.keySet()) { HashMap<String,
						 * Object> hashMap = (S) mapsub.get(val);
						 * 
						 * 
						 * for (String item : viewKeyItems) { //strv2.add(item);
						 * strv3.add((String)hashMap.get(item)); }
						 * rows.add(strv3);
						 * 
						 * }
						 */
					} else if (viewItem.contains("[")) {
						List<String> strv3 = new ArrayList<String>(); 

						String viewkey = viewItem.substring(0,
								viewItem.indexOf("["));
						String[] viewKeyItems = viewItem.substring(
								viewItem.indexOf("[") + 1).split(",");

						List<HashMap<String, Object>> mapsub = (List<HashMap<String, Object>>) map
								.get(viewkey);

						for (String item : viewKeyItems) {
							subkeys2.add(item);
						}

						for (HashMap<String, Object> hashMap : mapsub) {
							for (String item : viewKeyItems) {
								// strv2.add(item);
								strv3.add((String) hashMap.get(item));
							}
							rows.add(strv3);
						}

					} else {
						strv2.add(String.valueOf(map.get(viewItem)));
						// str.append(map.getOrDefault(viewItem, null) + "\t");
					}

				}
				rows.add(strv2);

			}

			List<String> subkeys3 = new ArrayList<String>(subkeys);
			subkeys3.addAll(subkeys2);

			pretyPrint(rows, subkeys3);
		} catch (Exception e) {
			System.out.println("Table output format error: " + e.getMessage());
			System.out.print(json);

			log.error(e);
		}
	}

	private void handleQuery(String json) {
		Object path  = JsonPath.read(json, OtcConfig.QUERY );
		 if (path instanceof java.util.List ) {
			 List temp = (List) path; 
			 for (Object object : temp) {
				 System.out.println(object);		
			}
		 }
		 else
		 {
			 System.out.println(path);
		 }
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcOutputHandler#parseJsontoTopLevelList(java.lang.String, java.lang.String)
	 */
	@Override
	@SuppressWarnings("unchecked")
	public List<HashMap<String, Object>> parseJsontoTopLevelList(
			String JSON, String mainKey) throws IOException {
		com.fasterxml.jackson.core.JsonFactory factory = new com.fasterxml.jackson.core.JsonFactory();
		ObjectMapper mapper = new ObjectMapper(factory);

		List<HashMap<String, Object>> ret = null;
		try {
			TypeReference<HashMap<String, Object>> typeRef = new com.fasterxml.jackson.core.type.TypeReference<HashMap<String, Object>>() {
			};
			HashMap<String, Object> o = mapper.readValue(JSON, typeRef);
			ret = (List<HashMap<String, Object>>) o.get(mainKey);
		} catch (JsonParseException e) {
			System.out.println("Can not parse output srvice output:"
					+ e.getMessage());
			log.error("Can not parse output srvice output:",e);
		}

		return ret;

	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcOutputHandler#parseJsontoTopLevelSimple(java.lang.String)
	 */
	@Override
	public HashMap<String, Object> parseJsontoTopLevelSimple(String JSON)
			throws IOException {
		com.fasterxml.jackson.core.JsonFactory factory = new com.fasterxml.jackson.core.JsonFactory();
		ObjectMapper mapper = new ObjectMapper(factory);

		TypeReference<HashMap<String, Object>> typeRef = new com.fasterxml.jackson.core.type.TypeReference<HashMap<String, Object>>() {
		};
		HashMap<String, Object> ret = mapper.readValue(JSON, typeRef);

		return ret;

	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcOutputHandler#pretyPrint(java.util.List, java.util.List)
	 */
	@Override
	@SuppressWarnings("unused")
	public void pretyPrint(List<List<String>> rowsList,
			List<String> headersList) {
		List<Integer> maxlist = new ArrayList<Integer>();
		int summax = 0;
		for (String head : headersList) {
			maxlist.add(head.length()+1);
		}

		for (int i = 0; i < rowsList.size(); i++) {
			List<String> cells = rowsList.get(i);
			for (int j = 0; j < cells.size(); j++) {
				String cell = cells.get(j);
				if (cell.length()+1 > maxlist.get(j)) {
					maxlist.set(j, cell.length()+1);
				}
			}

		}

		for (Integer val : maxlist) {
			summax += val;
		}

		if( rowsList == null ||headersList == null || rowsList.size() == 0   )
		{
			return;
		}
		
		Board board = new Board(summax + 20);
		Table table = new Table(board, summax + 20, headersList, rowsList);
		
		if( "text".equalsIgnoreCase( OtcConfig.OUTPUT_FORMAT ) )
		{
			table.setGridMode(Table.GRID_NON);
		}
		else
		{
			table.setGridMode(Table.GRID_COLUMN);
		}
		
		
		// setting width and data-align of columns
		List<Integer> colWidthsList = Arrays.asList(14, 14);
		List<Integer> colAlignList = Arrays.asList(Block.DATA_TOP_LEFT,
				Block.DATA_CENTER, Block.DATA_CENTER, Block.DATA_CENTER,
				Block.DATA_CENTER);
		table.setColWidthsList(maxlist);
		// table.setColAlignsList(colAlignList);

		Block tableBlock = table.tableToBlocks();
		board.setInitialBlock(tableBlock);
		board.build();
		String tableString = board.getPreview();
		System.out.println(tableString);

	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcOutputHandler#jsonPretyPrint(java.lang.String)
	 */
	@Override
	public String jsonPretyPrint(String aIn) throws IOException {

		ObjectMapper mapper = new ObjectMapper();
		Object json = mapper.readValue(aIn, Object.class);
		mapper.enable(SerializationFeature.INDENT_OUTPUT);

		String indented = mapper.writeValueAsString(json);

		System.out.println(indented);// This print statement show correct way I
										// need
		return indented;

	}

	public List<List<String>> trrows = new ArrayList<List<String>>();
	public ArrayList<String> trsubkeys = new ArrayList<String>() {{
	    add("Key");
	    add("Value");	    
	}};
	

    /* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcOutputHandler#printJsonTableTransverse(java.lang.String)
	 */
    @Override
	public void printJsonTableTransverse(String json ) throws IOException
    {
		
		if (OtcConfig.QUERY != null ) {				
			 handleQuery(json);	
			return;
		}

    	
		if ("JSON".equalsIgnoreCase(OtcConfig.OUTPUT_FORMAT)) {
			jsonPretyPrint(json);
			return;
		}

		
        JsonObject jsonObject = JsonObject.readFrom(json);
        handleObject(null,jsonObject);    	
        pretyPrint(trrows, trsubkeys);
    }

    /* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcOutputHandler#handleValue(java.lang.String, com.eclipsesource.json.JsonObject.Member, com.eclipsesource.json.JsonValue)
	 */
    @Override
	public void handleValue(String actual, JsonObject.Member member, JsonValue value) {
        if (value.isArray()) {

            recurseArray(actual,value.asArray());
        }
        else if (value.isObject()) {
            handleObject(actual , value.asObject());
        } else  {
        	ArrayList<String> temp = new ArrayList<String>();
        	temp.add(actual);
        	String val = value.toString().replace("\"\"", "null").replace("\"", "");
        	temp.add(val);
        	trrows.add( temp );
        }
    }

    private void handleObject(String actual, JsonObject object) {
        for (JsonObject.Member next : object) {
            JsonValue value = next.getValue();
            String nextKey = actual == null || actual.length() == 0 ? next.getName() : actual + "." + next.getName();
            handleValue(nextKey, next, value);
        }
    }

    private void recurseArray(String actual,JsonArray array) {
        for (JsonValue value : array) {
            handleValue(actual, null, value);
        }
    }

	
}