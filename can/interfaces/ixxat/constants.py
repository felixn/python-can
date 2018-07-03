#!/usr/bin/env python
# coding: utf-8

"""
Ctypes wrapper module for IXXAT Virtual CAN Interface V3 on win32 systems

Copyright (C) 2016 Giuseppe Corbelli <giuseppe.corbelli@weightpack.com>
"""

FALSE           = 0
TRUE            = 1

INFINITE        = 0xFFFFFFFF

VCI_MAX_ERRSTRLEN = 256

# Bitrates
CAN_BT0_10KB    = 0x31
CAN_BT1_10KB    = 0x1C
CAN_BT0_20KB    = 0x18
CAN_BT1_20KB    = 0x1C
CAN_BT0_50KB    = 0x09
CAN_BT1_50KB    = 0x1C
CAN_BT0_100KB   = 0x04
CAN_BT1_100KB   = 0x1C
CAN_BT0_125KB   = 0x03
CAN_BT1_125KB   = 0x1C
CAN_BT0_250KB   = 0x01
CAN_BT1_250KB   = 0x1C
CAN_BT0_500KB   = 0x00
CAN_BT1_500KB   = 0x1C
CAN_BT0_800KB   = 0x00
CAN_BT1_800KB   = 0x16
CAN_BT0_1000KB  = 0x00
CAN_BT1_1000KB  = 0x14

# Facilities/severities
SEV_INFO        = 0x40000000
SEV_WARN        = 0x80000000
SEV_ERROR       = 0xC0000000
SEV_MASK        = 0xC0000000
SEV_SUCCESS     = 0x00000000

RESERVED_FLAG   = 0x10000000
CUSTOMER_FLAG   = 0x20000000

STATUS_MASK     = 0x0000FFFF
FACILITY_MASK   = 0x0FFF0000

# Or so I hope
FACILITY_STD = 0

SEV_STD_INFO    = SEV_INFO |CUSTOMER_FLAG|FACILITY_STD
SEV_STD_WARN    = SEV_WARN |CUSTOMER_FLAG|FACILITY_STD
SEV_STD_ERROR   = SEV_ERROR|CUSTOMER_FLAG|FACILITY_STD

FACILITY_VCI    = 0x00010000
SEV_VCI_INFO    = SEV_INFO |CUSTOMER_FLAG|FACILITY_VCI
SEV_VCI_WARN    = SEV_WARN |CUSTOMER_FLAG|FACILITY_VCI
SEV_VCI_ERROR   = SEV_ERROR|CUSTOMER_FLAG|FACILITY_VCI

FACILITY_DAL    = 0x00020000
SEV_DAL_INFO    = SEV_INFO |CUSTOMER_FLAG|FACILITY_DAL
SEV_DAL_WARN    = SEV_WARN |CUSTOMER_FLAG|FACILITY_DAL
SEV_DAL_ERROR   = SEV_ERROR|CUSTOMER_FLAG|FACILITY_DAL

FACILITY_CCL    = 0x00030000
SEV_CCL_INFO    = SEV_INFO |CUSTOMER_FLAG|FACILITY_CCL
SEV_CCL_WARN    = SEV_WARN |CUSTOMER_FLAG|FACILITY_CCL
SEV_CCL_ERROR   = SEV_ERROR|CUSTOMER_FLAG|FACILITY_CCL

FACILITY_BAL    = 0x00040000
SEV_BAL_INFO    = SEV_INFO |CUSTOMER_FLAG|FACILITY_BAL
SEV_BAL_WARN    = SEV_WARN |CUSTOMER_FLAG|FACILITY_BAL
SEV_BAL_ERROR   = SEV_ERROR|CUSTOMER_FLAG|FACILITY_BAL

# Errors
VCI_SUCCESS             = 0x00
VCI_OK                  = 0x00
VCI_E_UNEXPECTED        = SEV_VCI_ERROR | 0x0001
VCI_E_NOT_IMPLEMENTED   = SEV_VCI_ERROR | 0x0002
VCI_E_OUTOFMEMORY       = SEV_VCI_ERROR | 0x0003
VCI_E_INVALIDARG        = SEV_VCI_ERROR | 0x0004
VCI_E_NOINTERFACE       = SEV_VCI_ERROR | 0x0005
VCI_E_INVPOINTER        = SEV_VCI_ERROR | 0x0006
VCI_E_INVHANDLE         = SEV_VCI_ERROR | 0x0007
VCI_E_ABORT             = SEV_VCI_ERROR | 0x0008
VCI_E_FAIL              = SEV_VCI_ERROR | 0x0009
VCI_E_ACCESSDENIED      = SEV_VCI_ERROR | 0x000A
VCI_E_TIMEOUT           = SEV_VCI_ERROR | 0x000B
VCI_E_BUSY              = SEV_VCI_ERROR | 0x000C
VCI_E_PENDING           = SEV_VCI_ERROR | 0x000D
VCI_E_NO_DATA           = SEV_VCI_ERROR | 0x000E
VCI_E_NO_MORE_ITEMS     = SEV_VCI_ERROR | 0x000F
VCI_E_NOT_INITIALIZED   = SEV_VCI_ERROR | 0x0010
VCI_E_ALREADY_INITIALIZED = SEV_VCI_ERROR | 0x00011
VCI_E_RXQUEUE_EMPTY     = SEV_VCI_ERROR | 0x00012
VCI_E_TXQUEUE_FULL      = SEV_VCI_ERROR | 0x0013
VCI_E_BUFFER_OVERFLOW   = SEV_VCI_ERROR | 0x0014
VCI_E_INVALID_STATE     = SEV_VCI_ERROR | 0x0015
VCI_E_OBJECT_ALREADY_EXISTS = SEV_VCI_ERROR | 0x0016
VCI_E_INVALID_INDEX     = SEV_VCI_ERROR | 0x0017
VCI_E_END_OF_FILE       = SEV_VCI_ERROR | 0x0018
VCI_E_DISCONNECTED      = SEV_VCI_ERROR | 0x0019
VCI_E_WRONG_FLASHFWVERSION = SEV_VCI_ERROR | 0x001A

# Controller status
CAN_STATUS_TXPEND   = 0x01
CAN_STATUS_OVRRUN   = 0x02
CAN_STATUS_ERRLIM   = 0x04
CAN_STATUS_BUSOFF   = 0x08
CAN_STATUS_ININIT   = 0x10
CAN_STATUS_BUSCERR  = 0x20

# Controller operating modes
CAN_OPMODE_UNDEFINED = 0x00
CAN_OPMODE_STANDARD  = 0x01
CAN_OPMODE_EXTENDED  = 0x02
CAN_OPMODE_ERRFRAME  = 0x04
CAN_OPMODE_LISTONLY  = 0x08
CAN_OPMODE_LOWSPEED  = 0x10

# Message types
CAN_MSGTYPE_DATA    = 0
CAN_MSGTYPE_INFO    = 1
CAN_MSGTYPE_ERROR   = 2
CAN_MSGTYPE_STATUS  = 3
CAN_MSGTYPE_WAKEUP  = 4
CAN_MSGTYPE_TIMEOVR = 5
CAN_MSGTYPE_TIMERST = 6

# Information supplied in the abData[0] field of info frames
# (CANMSGINFO.Bytes.bType = CAN_MSGTYPE_INFO).
CAN_INFO_START      = 1
CAN_INFO_STOP       = 2
CAN_INFO_RESET      = 3

# Information supplied in the abData[0] field of info frames
# (CANMSGINFO.Bytes.bType = CAN_MSGTYPE_ERROR).
CAN_ERROR_STUFF     = 1 # stuff error
CAN_ERROR_FORM      = 2 # form error
CAN_ERROR_ACK       = 3 # acknowledgment error
CAN_ERROR_BIT       = 4 # bit error
CAN_ERROR_CRC       = 6 # CRC error
CAN_ERROR_OTHER     = 7 # other (unspecified) error

# acceptance code and mask to reject all CAN IDs
CAN_ACC_MASK_NONE   = 0xFFFFFFFF
CAN_ACC_CODE_NONE   = 0x80000000
