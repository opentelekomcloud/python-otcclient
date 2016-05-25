package com.tsystems.otc.interfaces;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;

import com.eclipsesource.json.JsonObject;
import com.eclipsesource.json.JsonValue;

public interface IOtcOutputHandler {

	/**
	 * Example: printLevel2(json,"servers",Arrays.asList("id","href"));
	 * 
	 * @param json
	 * @param mainKey
	 * @param subkeys
	 * @throws IOException
	 */
	public abstract void printLevel3(String json, String mainKey,
			String level2Key, List<String> subkeys);

	/**
	 * Example: printLevel2(json,"servers",Arrays.asList("id","href"));
	 * 
	 * @param json
	 * @param mainKey
	 * @param subkeys
	 * @throws IOException
	 */
	public abstract void printLevel2(String json, String mainKey,
			List<String> subkeys);

	public abstract List<HashMap<String, Object>> parseJsontoTopLevelList(
			String JSON, String mainKey) throws IOException;

	public abstract HashMap<String, Object> parseJsontoTopLevelSimple(
			String JSON) throws IOException;

	public abstract void pretyPrint(List<List<String>> rowsList,
			List<String> headersList);

	public abstract String jsonPretyPrint(String aIn) throws IOException;

	public abstract void printJsonTableTransverse(String json)
			throws IOException;

	public abstract void handleValue(String actual, JsonObject.Member member,
			JsonValue value);

}