#!/usr/bin/python
# -*- coding: utf-8 -*-

import get_file_path
from logging_maker import logger
from find_text import fun_find_text
from find_text import find_text_a2l
from find_mech import fun_find_mech
from specifical_variable_find import *

#
#
#
# if file_a2l:
#     print(f"17{file_a2l}")

# file_a2l = get_file_path.file_a2l
# file_dcm = get_file_path.file_dcm
# file_geskon = get_file_path.file_geskon
# file_mech_table = get_file_path.file_mech_table
# file_data_mytable = get_file_path.file_data_mytable

variable_name_list = ("Time_Rampup_Suspension",
                      "Position_Deviation_Rack_Safety_CSAP",
                      "Gradient_Handling_Rotortorque_Safety_BLOCK",
                      "Min_Vehicle_speed",
                      "rotor_speed_LSS",
                      "Factor_Input_Shaft_Torque_2_Rotor_Torque",
                      "Speed_Rack_HSD_Start_1",
                      "Speed_Rack_HSD_Start_2",
                      "Speed_Rotor_Damping_Activate",
                      "Torque_HSD_Short_Before_Endstop",
                      "Torque_HSD_High_Distance_2_Endstop",
                      "Speed_Tie_Rod_Damping_Activate",
                      "Voltage_Power_Supply_Threshold",
                      "Speed_Tie_Rod_Low",
                      "Speed_Tie_Rod_High",
                      "Speed_Tie_Rod_Undervoltage_Offset",
                      "Speed_Vehicle_Thres_DynStMotTrq",
                      "Force_Rack_Max_TargetStTrqCurve",
                      "Ratio_RackForce2MotorTrq",
                      "Distance_Travel_UpdateStatus_EndStopLearning_Rack",
                      "Distance_Travel_FromEndStop_EndStopDampingActive",
                      "Distance_Travel_FromEndStop_EndStopDampingPeak",
                      "Speed_Border1_ExtraDamping_Motor",
                      "Speed_Border2_ExtraDamping_Motor",
                      "Supply_Voltage_Threshold",
                      "Speed_Rotor_Threshold_Activate_HSD_Forward",
                      "Voltage_Min_Range_Active_Reduction",
                      "Voltage_Max_Range_Active_Reduction",
                      "Voltage_Min_Range_Active_Limitation",
                      "Voltage_Max_Range_Active_Limitation",
                      "Voltage_Min_Range_Limitation_Gradient",
                      "Voltage_Max_Range_Limitation_Gradient",
                      )

print(variable_name_list)

logger.info(f"variable_name_list:{variable_name_list}")

# 需要在机械参数表、dcm、geskon中查询的参数
dict_mech_parameter = {"Speed_Max_LSD_Rotor": ["nRpSync_MaxRotSpdLowDyn_XDU16", "", "", "", 1],
                       "Torque_Limited_LSD_Motor": ["mRpSync_MaxMMotLowDyn_XDU16", "Steering Angle", 121, 1, 1],
                       "Torque_Max_LSD_TorsionBar": ["mRpSync_MaxTBTLowDyn_XDU16", "", "", "", 1],
                       "Speed_Calib_Max_Vehicle": ["vRpSync_MaxCalibVehicleSpeed_XDU16", "", "", "", 1],
                       "Factor_ShortTerm_Integral": ["xRpCorr_STIntegrationFactor_XDU16", "", "", "", 1],
                       "Time_ShortTerm_Correction": ["tRpCorr_DetectionTimerST_XDU8", "", "", "", 1],
                       "Torque_LongTerm_AheadCheck_TorsionBar": ["mRpCorr_LTATBT_XDU16", "", "", "", 1],
                       "Torque_LongTerm_AheadCheck_Motor": ["mRpCorr_LTMaxMotTorq_XDU16", "", "", "", 1],
                       "Time_RackPosition_ErrorFilter": ["tRackPo_ErrorFilterTimeout_XDU16", "", "", "", 1],
                       "Time_Ahead_RackPosition_ErrorFilter": ["tRackPo_ErrorFilterAheadTimeout_XDU16", "", "", "", 1],
                       "Angle_LongTerm_Integ_Range": ["wRpCorr_LTACompIntegRange_XDU16", "", "", "", 1],
                       "Factor_LongTerm_Integral": ["xRpCorr_LTACompIntegFactor_XDU16", "", "", "", 1],
                       "Time_LongTerm_Correction": ["tRpCorr_DetectionTimerLT_XDU8", "", "", "", 1],
                       "Factor_Speed_LongTerm_Vehicle": ["vRpCorr_VehicleSpeedWeight_XDU16", "", "", "", 1],
                       "Angle_Max_Calib_Rotor": ["wRpSync_MaxRotorAngleForCalib", "", "", "", 1],
                       "Angle_Allowed_Shift_Index": ["wRpSync_AllowedIndexShift_XDU16", "", "", "", 1],
                       "Angle_Additional_Tolerance_Rotor": ["wRpSync_AdditionalToleranceRawSync_XDU16", "", "", "", 1],
                       "Angle_SteeringWheel_Turn_Rotor": ["wRpSync_SteeringWheelOneTurn_XDU16", "", "", "", 1],
                       "Angle_Additional_Tolerance_OneTurn_Rotor": ["wRpSync_AdditionalToleranceOneTurn_XDU16", "", "", "", 1],
                       "Angle_Max_Pinion": ["wRackPo_SteeringAngleMax_XDU16", "", "", "", 1],
                       "Position_Max_Rack": ["lRackPo_RackPositionMax_XDU16", "", "", "", 1],
                       "Angle_ShortTerm_Max_Offset_Steering": ["wRackPo_StCorrAngleMax_XDU16", "", "", "", 1],
                       "Angle_LongTerm_Max_Offset_Steering": ["wRackPo_LtCorrAngleMax_XDU16", "", "", "", 1],
                       "Angle_Gradient_Integral_Threshold": ["wRackPo_GradErrLimit_XDU16", "", "", "", 1],
                       "Angle_Compare_Deviation_UP_Rotor": ["wRackPo_RackposToleranceRA_XDU16", "", "", "", 1],
                       "Angle_Compare_Deviation_Down_Rotor": ["wRackPo_RackposToleranceRA_XDU16", "", "", "", -1],
                       "Angle_Reference_Deviation_Rotor": ["wRackPo_RackposToleranceRA_XDU16", "", "", "", 1],
                       "Position_Straight_Ahead_Rack": ["lRackPo_RackPosRangeAhead_XDU16", "", "", "", 1],
                       "Angle_SyncDiff_Min_Difference_Rotor": ["wRpSync_MinSyncDiffRaw_XDU16", "", "", "", 1],
                       "Time_Ahead_Detection": ["tRpSync_InitTimeStraight_XDU16", "", "", "", 1],
                       "Angle_Straight_Range_Rotor": ["wRpSync_RotAngRangeStraight_XDU16", "", "", "", 1],
                       "Angle_Range_HalfSteer_Min_Rotor": ["wRpSync_MinSteeringRangeHalf_XDU16", "", "", "", 1],
                       "Angle_Difference_SyncExact_Rotor": ["wRpSync_MinSyncDiff_XDU16", "Steering Angle", 126, 1, 1],
                       "Angle_Width_Max_Index_Rotor": ["wRpSync_MaxAllowedIdxWidth_XDU16", "", "", "", 1],
                       "Angle_Width_Min_Index_Rotor": ["wRpSync_MinAllowedIdxWidth_XDU16", "", "", "", 1],
                       "Angle_Gradient_Integral_Start_Threshold": ["vRackPo_RotAngGradientDiffMax_XDU16", "", "", "", 1],
                       "Speed_Valid_Min_Rack": ["vDthrCtrl_MaxRackSpeed_XDU16", "Steering Angle", 6, 1, -1],
                       "Speed_Valid_Max_Rack": ["vDthrCtrl_MaxRackSpeed_XDU16", "Steering Angle", 6, 1, 1],
                       "AngleSpeed_Backward_Max_Rotor": ["vRackPo_RotorSpeedTolerance_XDU16", "", "", "", 1],
                       "AngleSpeed_Backward_Min_Rotor": ["vRackPo_RotorSpeedTolerance_XDU16", "", "", "", 1],
                       "AngleSpeed_Valid_Max_Rotor": ["nRackPo_MaxRotorSpeedRackSpeedPlausi_XDU16", "", "", "", 1],
                       "AngleSpeed_Valid_Min_Rotor": ["nRackPo_MaxRotorSpeedRackSpeedPlausi_XDU16", "", "", "", 1],
                       "Factor_Torsion_Compensation": ["xRpSync_TorsionRpsFactor_XDU16", "", "", "", 1],
                       }
mech_parameter_list = list(dict_mech_parameter.keys())
# block end

# 需要在A2L中查询的参数
dict_a2l_parameter = {"ROTOR_SPEED_MIN_VALID": ["nrsI_IntRotorSpeed_xds16", "min", 1],
                       "ROTOR_SPEED_MAX_VALID": ["nrsI_IntRotorSpeed_xds16", "max", 1],
                       "GRADIENT_MAX_CALCULATE_ROTOR_MOTION": ["aApplI_RotAcceleration_xds16", "max", 0.006],
                      "LMT_MIN_ROTORSPEED": ["nApplI_RotorSpeedFilt_xds16", "min", 1],
                      "LMT_MAX_ROTORSPEED": ["nApplI_RotorSpeedFilt_xds16", "max", 1],
                      "LMT_MAX_NOMINALMOTORTORQUE": ["mApplI_NominalMotorTorque_xds16", "max", 1],
                      "LMT_MIN_NOMINALMOTORTORQUE": ["mApplI_NominalMotorTorque_xds16", "min", 1],
                      "LMT_MIN_STEERTORQUESUM": ["mTrqSumI_SteerTrqSum_xds16", "min", 1],
                      "LMT_MAX_STEERTORQUESUM": ["mTrqSumI_SteerTrqSum_xds16", "max", 1],
                      "PTSF_MIN_MOTTRQSUM": ["mTrqSumI_MotTrqSum1_xds16", "min", 1],
                      "PTSF_MAX_MOTTRQSUM": ["mTrqSumI_MotTrqSum1_xds16", "max", 1],
                      "PTSF_MIN_STEERINGANGLE": ["wApplI_SteeringAngle_xds16", "min", 1],
                      "PTSF_MAX_STEERINGANGLE": ["wApplI_SteeringAngle_xds16", "max", 1],
                      "PTSF_MIN_ROTORSPEED": ["nApplI_RotorSpeed_xds16", "min", 1],
                      "PTSF_MAX_ROTORSPEED": ["nApplI_RotorSpeed_xds16", "max", 1],
                      "PTSF_MIN_CURRENTLOWESTREDLEVEL": ["xHwlWrapI_CurrentLowestReductionLevel_xdu16", "min", 1],
                      "PTSF_MAX_CURRENTLOWESTREDLEVEL": ["xHwlWrapI_CurrentLowestReductionLevel_xdu16", "max", 1],
                      }
a2l_parameter_list = list(dict_a2l_parameter.keys())
print(a2l_parameter_list)
logger.info(f"a2l_parameter_list:{a2l_parameter_list}")
# block end




parameter_list = ["lEndStop_SteerRange_XDU16",
                  "mHwlWrapI_MaxMechAllowedTorque_XDF32",
                  "xEndStop_RateLimiterToZeroRate_XDU32",
                  "lEndStop_uAbsSteerLearn_XDU16",
                  "lEndStop_oAbsSteerLearn_XDU16",
                  "lEndStop_MinSteerRangeLearned_XDU16",
                  "lEndStop_RelearnOffset_XDU16",
                  "lEndStop_uDistanceLearnCondition_XDU16",
                  "tEndStop_DebounceTimeLearnFin_XDU8",
                  "vEndStop_uVehSpeedLearnFinished_XDU16",
                  "mEndStop_uTBTLearn_XDU16",
                  "mEndStop_uMotorTorque_XDU16",
                  "xEndStop_uTotalMotTorLimLearnFinished_XDU16",
                  "nEndStop_oRotSpeedLearn_XDU16",
                  "nEndStop_oRotSpeedLearnFinished_XDU16",
                  "lEndStop_OffsetNotExactlyInit_XDU16",
                  "lEndStop_AllowedPosBorder_XDU16",
                  "xEndStop_SpringFactorGrad_XDU16",
                  "mEndStop_LimitDamping_XDU16",
                  "mEndStop_oMaxDamping_XDU16",
                  # "xEndStop_FadeFactorMotTrq_XAU16",
                  "xEndStop_ResidualAssistance_XDU16",
                  "tEndStop_MaxTimeIncrDamping_XDU8"]


def fun_find_para(variable_name, variable,file_a2l,file_geskon,file_dcm,file_data_mytable,file_mech_table):
    print(f"查找对象: {variable_name}, {variable}")
    logger.info(f"-----调用查找-----")
    logger.info(f"查找对象: {variable_name}, {variable}")
    fun_find_result = False
    fun_find_para = ""
    if variable in parameter_list:
        fun_find_result, fun_find_para = spec_fun_find_varaible_mech_and_kon(file_a2l,file_geskon,file_dcm,file_mech_table, variable)
    elif variable_name in a2l_parameter_list:
        fun_find_result, fun_find_para = find_text_a2l(dict_a2l_parameter[variable_name][0],
                                                       file_a2l,
                                                       dict_a2l_parameter[variable_name][1],
                                                       dict_a2l_parameter[variable_name][2])
    elif variable_name in mech_parameter_list:
        fun_find_result, fun_find_para = spec_fun_find_varaible_mech_and_kon_fur(file_a2l,
                                                                                 file_geskon,
                                                                                 file_dcm,
                                                                                 file_mech_table,
                                                                                 variable_name,
                                                                                 dict_mech_parameter[variable_name][0],
                                                                                 [dict_mech_parameter[variable_name][1],
                                                                                 dict_mech_parameter[variable_name][2],
                                                                                 dict_mech_parameter[variable_name][3]],
                                                                                 dict_mech_parameter[variable_name][4])
    elif variable_name in variable_name_list:
        print(f"需特殊计算: {variable_name}")
        logger.info(f"需特殊计算: {variable_name}")
        if variable_name == variable_name_list[0]:
            print(f"需计算数据名为：{variable_name_list[0]}")
            logger.info(f"需计算数据名为：{variable_name_list[0]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_0(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[1]:
            print(f"需计算数据名为：{variable_name_list[1]}")
            logger.info(f"需计算数据名为：{variable_name_list[1]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_1(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[2]:
            print(f"需计算数据名为：{variable_name_list[2]}")
            logger.info(f"需计算数据名为：{variable_name_list[2]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_2(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[3]:
            print(f"需计算数据名为：{variable_name_list[3]}")
            logger.info(f"需计算数据名为：{variable_name_list[3]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_3(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[4]:
            print(f"需计算数据名为：{variable_name_list[4]}")
            logger.info(f"需计算数据名为：{variable_name_list[4]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_4(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[5]:
            print(f"需计算数据名为：{variable_name_list[5]}")
            logger.info(f"需计算数据名为：{variable_name_list[5]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_5(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[6]:
            print(f"需计算数据名为：{variable_name_list[6]}")
            logger.info(f"需计算数据名为：{variable_name_list[6]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_6(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[7]:
            print(f"需计算数据名为：{variable_name_list[7]}")
            logger.info(f"需计算数据名为：{variable_name_list[7]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_7(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[8]:
            print(f"需计算数据名为：{variable_name_list[8]}")
            logger.info(f"需计算数据名为：{variable_name_list[8]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_8(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[9]:
            print(f"需计算数据名为：{variable_name_list[9]}")
            logger.info(f"需计算数据名为：{variable_name_list[9]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_9(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[10]:
            print(f"需计算数据名为：{variable_name_list[10]}")
            logger.info(f"需计算数据名为：{variable_name_list[10]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_10(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[11]:
            print(f"需计算数据名为：{variable_name_list[11]}")
            logger.info(f"需计算数据名为：{variable_name_list[11]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_11(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[12]:
            print(f"需计算数据名为：{variable_name_list[12]}")
            logger.info(f"需计算数据名为：{variable_name_list[12]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_12(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[13]:
            print(f"需计算数据名为：{variable_name_list[13]}")
            logger.info(f"需计算数据名为：{variable_name_list[13]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_13(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[14]:
            print(f"需计算数据名为：{variable_name_list[14]}")
            logger.info(f"需计算数据名为：{variable_name_list[14]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_14(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[15]:
            print(f"需计算数据名为：{variable_name_list[15]}")
            logger.info(f"需计算数据名为：{variable_name_list[15]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_15(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[16]:
            print(f"需计算数据名为：{variable_name_list[16]}")
            logger.info(f"需计算数据名为：{variable_name_list[16]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_16(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[17]:
            print(f"需计算数据名为：{variable_name_list[17]}")
            logger.info(f"需计算数据名为：{variable_name_list[17]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_17(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[18]:
            print(f"需计算数据名为：{variable_name_list[18]}")
            logger.info(f"需计算数据名为：{variable_name_list[18]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_18(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[19]:
            print(f"需计算数据名为：{variable_name_list[19]}")
            logger.info(f"需计算数据名为：{variable_name_list[19]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_19(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[20]:
            print(f"需计算数据名为：{variable_name_list[20]}")
            logger.info(f"需计算数据名为：{variable_name_list[20]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_20(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[21]:
            print(f"需计算数据名为：{variable_name_list[21]}")
            logger.info(f"需计算数据名为：{variable_name_list[21]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_21(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[22]:
            print(f"需计算数据名为：{variable_name_list[22]}")
            logger.info(f"需计算数据名为：{variable_name_list[22]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_22(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[23]:
            print(f"需计算数据名为：{variable_name_list[23]}")
            logger.info(f"需计算数据名为：{variable_name_list[23]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_23(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[24]:
            print(f"需计算数据名为：{variable_name_list[24]}")
            logger.info(f"需计算数据名为：{variable_name_list[24]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_24(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[25]:
            print(f"需计算数据名为：{variable_name_list[25]}")
            logger.info(f"需计算数据名为：{variable_name_list[25]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_25(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[26]:
            print(f"需计算数据名为：{variable_name_list[26]}")
            logger.info(f"需计算数据名为：{variable_name_list[26]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_26(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[27]:
            print(f"需计算数据名为：{variable_name_list[27]}")
            logger.info(f"需计算数据名为：{variable_name_list[27]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_27(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[28]:
            print(f"需计算数据名为：{variable_name_list[28]}")
            logger.info(f"需计算数据名为：{variable_name_list[28]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_28(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[29]:
            print(f"需计算数据名为：{variable_name_list[29]}")
            logger.info(f"需计算数据名为：{variable_name_list[29]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_29(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[30]:
            print(f"需计算数据名为：{variable_name_list[30]}")
            logger.info(f"需计算数据名为：{variable_name_list[30]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_30(file_a2l,file_geskon,file_dcm,file_mech_table)
        if variable_name == variable_name_list[31]:
            print(f"需计算数据名为：{variable_name_list[31]}")
            logger.info(f"需计算数据名为：{variable_name_list[30]}")
            fun_find_result, fun_find_para = spec_fun_find_variable_31(file_a2l,file_geskon,file_dcm,file_mech_table)

    else:
        print(f"不需特殊计算: {variable_name}")
        logger.info(f"不需特殊计算: {variable_name}")
        fun_find_result, fun_find_para = fun_find_text(variable, file_geskon, file_dcm)

    print(f"<Function: fun_find_para>\nfun_find_result = {fun_find_result}\nfun_find_para = \n{fun_find_para}")
    print(f"-----该参数查找结束-----\n")
    logger.info(f"<Function: fun_find_para>\n查询结果 = {fun_find_result}\n查询参数 = \n{fun_find_para}")
    logger.info(f"-----该参数查找结束-----\n")
    return fun_find_result, fun_find_para

'''调试用函数'''
# fun_find_para("", "xSteerCtrl_ChatterReduction_XAU16")

# for parameter in parameter_list:
#     fun_find_para("Ratio_RackForce2MotorTrq", parameter)


print("\n---find end---")

# find_result, paragraph_find, = fun_find_text(self.variable, file_geskon, file_dcm)
