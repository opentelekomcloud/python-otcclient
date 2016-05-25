package com.tsystems.otc.interfaces;

import java.io.IOException;

public interface IOtcServiceCalls {

	public abstract String getECSVM(String VM) throws IOException;

	public abstract String getECSList() throws IOException;

	public abstract String getECSDetail() throws IOException;

	public abstract String getVPCList() throws IOException;

	public abstract String getPUBLICIPSList() throws IOException;

	public abstract String getSECGROUPList() throws IOException;

	public abstract String getSECGROUPRULESList() throws Exception;

	public abstract String getSUBNETList() throws Exception;

	public abstract String getIMAGEList() throws Exception;

	public abstract String getFLAVORList() throws IOException;

	public abstract String getKEYPAIRList() throws IOException;

	public abstract String KEYPAIRCreate();

	public abstract String PUBLICIPSAllocate();

	public abstract String PUBLICIPSAssociate();

	public abstract String KEYPAIRDelete();

	public abstract String getECSJOBList() throws IOException;

	public abstract String getFileContentJSON(String aSource, String aTarget)
			throws IOException;

	public abstract String getPersonalizationJSON() throws IOException;

	public abstract String ECSAction();

	public abstract String ECSDelete();

	public abstract String VPCCreate();

	public abstract String SUBNETCreate();

	public abstract String SECGROUPCreate();

	public abstract String SECGROUPRULECreate();

	public abstract String ECSCreate() throws IOException;

	public abstract String getIamToken() throws IOException;

	public abstract void convertFlavorNameToId() throws IOException;

	public abstract void convertPublicIpNameToId() throws IOException;

	public abstract void convertVPCNameToId() throws IOException;

	public abstract void convertSUBNETNameToId() throws IOException;

	public abstract void convertIMAGENameToId() throws IOException;

	public abstract void convertSECUGROUPNameToId() throws IOException;

	public abstract void CreateLaunchConfiguration();

	public abstract void AttachInstances();

	public abstract void AttachLoadBalancers();

	public abstract void CreateAutoScalingGroup();

	public abstract void DeleteAutoScalingGroup();

	public abstract void DeleteLaunchConfiguration();

	public abstract String getVolumeList() throws IOException;

	public abstract String CreateVolume();

	public abstract String AttachVolume();

	public abstract String DetachVolume();

	public abstract String DeleteVolume();

	public abstract String DescribeQuotas() throws IOException;

	public abstract String getBackupList() throws IOException;

	public abstract String RestoreBackupDisk();

	public abstract String DeleteBackup();

	public abstract String CreateBackup();

}