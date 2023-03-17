#!/usr/bin/python
# -*- coding: utf-8 -*-

from logging_maker import logger

def get_file_path():
    file_a2l = ""
    file_geskon = ""
    file_dcm = ""
    file_data_mytable = ""
    file_mech_table = ""
    #
    # file_a2l = "DF0D01C0100_RG3_X_SCU3_B3_VAR_01.a2l"
    # file_geskon = "XP1100D0100_RG3_X_SCU3_B3_VAR_01_geskon.kon"
    # file_dcm = "DCM_ALL_XIAO PENG_F30_First Tuning(Normal mode_01+Comfortable_06+Sport_11)_Based on XP1100B0100_20220705.DCM"
    # file_data_mytable = "data.xlsx"
    # file_mech_table = "MechanicalDataSheet -机械参数表 Voyah_H97C_20220902.xlsm"
    #
    #     # file_a2l = "D:\MyPython\Bosch_myProjects\DataQuery\DF0D01C0100_RG3_X_SCU3_B3_VAR_01.a2l"
    #     # file_geskon = "D:\MyPython\Bosch_myProjects\DataQuery\XP1100D0100_RG3_X_SCU3_B3_VAR_01_geskon.kon"
    #     # file_dcm = "D:\MyPython\Bosch_myProjects\DataQuery\DCM_ALL_XIAO PENG_F30_First Tuning(Normal mode_01+Comfortable_06+Sport_11)_Based on XP1100B0100_20220705.DCM"
    #     # file_data_mytable = "D:\MyPython\Bosch_myProjects\DataQuery\data.xlsx"
    #     # file_mech_table = "D:\MyPython\Bosch_myProjects\DataQuery\MechanicalDataSheet -机械参数表 Voyah_H97C_20220902.xlsm"
    #
    file_a2l = input("Input a2l: \n").replace('"', '')
    file_geskon = input("Input geskon:\n").replace('"', '')
    file_dcm = input("Input Dcm:\n").replace('"', '')
    file_mech_table = input("Input MechanicalDataSheet:\n").replace('"', '')
    file_data_mytable = input("Input DataTable:\n").replace('"', '')

    # global file_a2l
    # global file_geskon
    # global file_dcm
    # global file_data_mytable
    # global file_mech_table
    # file_a2l = file_a2l
    #
    logger.info(f'A2L文件为:{file_a2l}')
    logger.info(f'Geskon文件为:{file_geskon}')
    logger.info(f'DCM文件为:{file_dcm}')
    logger.info(f'机械参数表文件为:{file_mech_table}')
    logger.info(f'Data文件为:{file_data_mytable}')

    return file_a2l, file_geskon, file_dcm, file_data_mytable, file_mech_table


#
file_a2l, file_geskon, file_dcm, file_data_mytable, file_mech_table = get_file_path()
#

# file_a2l = file_a2l
# file_geskon = file_geskon
# file_dcm = file_dcm
# file_data_mytable = file_data_mytable
# file_mech_table = file_mech_table
