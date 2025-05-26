import smbus

# none CF registers
# read_block_data - not work

class LTC2975:
    # LTC2975 (integrated to LTM4673) Register Addresses
    REG_PAGE = 0x00
    REG_OPERATION = 0x01
    REG_ON_OFF_CONFIG = 0x02
    REG_CLEAR_FAULTS = 0x03
    REG_WRITE_PROTECT = 0x10
    REG_STORE_USER_ALL = 0x15
    REG_RESTORE_USER_ALL = 0x16
    REG_CAPABILITY = 0x19
    REG_VOUT_MODE = 0x20
    REG_VOUT_COMMAND = 0x21
    REG_VOUT_MAX = 0x24
    REG_VOUT_MARGIN_HIGH = 0x25
    REG_VOUT_MARGIN_LOW = 0x26
    REG_VIN_ON = 0x35
    REG_VIN_OFF = 0x36
    REG_IOUT_CAL_GAIN = 0x38
    REG_VOUT_OV_FAULT_LIMIT = 0x40
    REG_VOUT_OV_FAULT_RESPONSE = 0x41
    REG_VOUT_OV_WARN_LIMIT = 0x42
    REG_VOUT_UV_WARN_LIMIT = 0x43
    REG_VOUT_UV_FAULT_LIMIT = 0x43
    REG_VOUT_UV_FAULT_RESPONSE = 0x45
    REG_IOUT_OC_FAULT_LIMIT = 0x46
    REG_IOUT_OC_FAULT_RESPONSE = 0x47
    REG_IOUT_OC_WARN_LIMIT = 0x4A
    REG_IOUT_UC_FAULT_LIMIT = 0x4B
    REG_IOUT_UC_FAULT_RESPONSE = 0x4C
    REG_OT_FAULT_LIMIT = 0x4F
    REG_OT_FAULT_RESPONSE = 0x50
    REG_OT_WARN_LIMIT = 0x51
    REG_UT_WARN_LIMIT = 0x52
    REG_UT_FAULT_LIMIT = 0x53
    REG_UT_FAULT_RESPONSE = 0x54
    REG_VIN_OV_FAULT_LIMIT = 0x55
    REG_VIN_OV_FAULT_RESPONSE = 0x56
    REG_VIN_OV_WARN_LIMIT = 0x57
    REG_VIN_UV_WARN_LIMIT = 0x58
    REG_VIN_UV_FAULT_LIMIT = 0x59
    REG_VIN_UV_FAULT_RESPONSE = 0x5A
    REG_POWER_GOOD_ON = 0x5E
    REG_POWER_GOOD_OFF = 0x5F
    REG_TON_DELAY = 0x60
    REG_TON_RISE = 0x61
    REG_TON_MAX_FAULT_LIMIT = 0x62
    REG_TON_MAX_FAULT_RESPONSE = 0x63
    REG_TOFF_DELAY = 0x64
    REG_STATUS_BYTE = 0x78
    REG_STATUS_WORD = 0x79
    REG_STATUS_VOUT = 0x7A
    REG_STATUS_IOUT = 0x7B
    REG_STATUS_INPUT = 0x7C
    REG_STATUS_TEMPERATURE = 0x7D
    REG_STATUS_CML = 0x7E
    REG_STATUS_MFR_SPECIFIC = 0x80
    REG_READ_VIN = 0x88
    REG_READ_IIN = 0x89
    REG_READ_VOUT = 0x8B
    REG_READ_IOUT = 0x8C
    REG_READ_TEMPERATURE_1 = 0x8D
    REG_READ_TEMPERATURE_2 = 0x8E
    REG_READ_POUT = 0x96
    REG_READ_PIN = 0x97
    REG_PMBUS_REVISION = 0x98
    REG_USER_DATA_00 = 0xB0
    REG_USER_DATA_01 = 0xB1
    REG_USER_DATA_02 = 0xB2
    REG_USER_DATA_03 = 0xB3
    REG_USER_DATA_04 = 0xB4
    REG_MFR_LTC_RESERVED_1 = 0xB5
    REG_MFR_T_SELF_HEAT = 0xB8
    REG_MFR_IOUT_CAL_GAIN_TAU__INV = 0xB9
    REG_MFR_IOUT_CAL_GAIN_THETA = 0xBA
    REG_MFR_READ_IOUT = 0xBB
    REG_MFR_LTC_RESERVED_2 = 0xBC
    REG_MFR_EE_UNLOCK = 0xBD
    REG_MFR_EE_ERASE = 0xBE
    REG_MFR_EIN = 0xC0
    REG_MFR_EIN_CONFIG = 0xC1
    REG_MFR_IIN_CAL_GAIN = 0xE8
    REG_MFR_IIN_CAL_GAIN_TC = 0xC3
    REG_MFR_IIN_PEAK = 0xC4
    REG_MFR_IIN_MIN = 0xC5
    REG_MFR_PIN_PEAK = 0xC6
    REG_MFR_PIN_MIN = 0xC7
    REG_MFR_COMMAND_PLUS = 0xC8
    REG_MFR_DATA_PLUS0 = 0xC9
    REG_MFR_DATA_PLUS1 = 0xCA
    REG_MFR_CONFIG_LTM4673 = 0xD0
    REG_MFR_CONFIG_ALL_LTM4673 = 0xD1
    REG_MFR_FAULTB0_PROPAGATE = 0xD2
    REG_MFR_FAULTB1_PROPAGATE = 0xD3
    REG_MFR_PWRGD_EN = 0xD4
    REG_MFR_FAULTB0_RESPONSE = 0xD5
    REG_MFR_FAULTB1_RESPONSE = 0xD6
    REG_MFR_IOUT_PEAK = 0xD7
    REG_MFR_IOUT_MIN = 0xD8
    REG_MFR_CONFIG2_LTM4673 = 0xD9
    REG_MFR_CONFIG3_LTM4673 = 0xDA
    REG_MFR_RETRY_DELAY = 0xDB
    REG_MFR_RESTART_DELAY = 0xDC
    REG_MFR_VOUT_PEAK = 0xDD
    REG_MFR_VIN_PEAK = 0xDE
    REG_MFR_TEMPERATURE_1_PEAK = 0xDF
    REG_MFR_DAC = 0xE0
    REG_MFR_POWERGOOD_ASSERTION_DELAY = 0xE1
    REG_MFR_WATCHDOG_T_FIRST = 0xE2
    REG_MFR_WATCHDOG_T = 0xE3
    REG_MFR_PAGE_FF_MASK = 0xE4
    REG_MFR_PADS = 0xE5
    REG_MFR_I2C_BASE_ADDRESS = 0xE6
    REG_MFR_SPECIAL_ID = 0xE7                       # Manufacturer code for identifying the LTM4673. 0x448X
    REG_MFR_SPECIAL_LOT = 0xC2
    REG_MFR_VOUT_DISCHARGE_THRESHOLD = 0xE9
    REG_MFR_FAULT_LOG_STORE = 0xEA
    REG_MFR_FAULT_LOG_RESTORE = 0xEB
    REG_MFR_FAULT_LOG_CLEAR = 0xEC
    REG_MFR_FAULT_LOG_STATUS = 0xED
    REG_MFR_FAULT_LOG = 0xEE
    REG_MFR_COMMON = 0xEF
    REG_MFR_IOUT_CAL_GAIN_TC = 0xF6
    REG_MFR_RETRY_COUNT = 0xF7
    REG_MFR_TEMP_1_GAIN = 0xF9
    REG_MFR_TEMP_1_OFFSET = 0xF9
    REG_MFR_IOUT_SENSE_VOLTAGE = 0xFA
    REG_MFR_VOUT_MIN = 0xFB
    REG_MFR_VIN_MIN = 0xFC
    REG_MFR_TEMPERATURE_1_MIN = 0xFD

    # Default I2C bus number
    DEFAULT_BUS = 1
    N = 2**-13

    def hex_to_signed(self, hex_value, bits=5):
        value = int(hex_value, 16)
        if value & (1 << (bits - 1)):
            value -= 1 << bits
        return value

    def __init__(self, bus_num=DEFAULT_BUS, addr=0x40):
        self.bus = smbus.SMBus(bus_num)
        self.addr = addr
        
    def write_register(self, reg, value):
        self.bus.write_word_data(self.addr, reg, value)

    def read_register(self, reg):
        value = self.bus.read_word_data(self.addr, reg)
        return value

    def read_register_block(self, reg):
        value = self.bus.read_block_data(self.addr, reg)
        return value

    def write_register_byte(self, reg, value):
        self.bus.write_byte_data(self.addr, reg, value)

    def read_register_byte(self, reg):
        value = self.bus.read_byte_data(self.addr, reg)
        return value

    def page(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_PAGE, value)
        else:
            return  self.read_register_byte(self.REG_PAGE)
        
    def operation(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_OPERATION, value)
        else:
            return self.read_register_byte(self.REG_OPERATION)
            
    def on_off_config(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_ON_OFF_CONFIG, value)
        else:
            return self.read_register_byte(self.REG_ON_OFF_CONFIG)
            
    def clear_faults(self, value):
            self.write_register_byte(self.REG_CLEAR_FAULTS, value)

    def write_protect(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_WRITE_PROTECT, value)
        else:
            return self.read_register_byte(self.REG_WRITE_PROTECT)

    def store_user_all(self, value):
            self.write_register_byte(self.REG_STORE_USER_ALL, value)

    def restore_user_all(self, value):
            self.write_register_byte(self.REG_RESTORE_USER_ALL, value)

    def capability(self):
        return self.read_register_byte(self.REG_CAPABILITY)

    def vout_mode(self, value = None):
        return self.read_register_byte(self.REG_VOUT_MODE)

    def vout_command(self, value = None):
        if value is not None:
            self.write_register(self.REG_VOUT_COMMAND, value/N)
        else:
            return self.read_register(self.REG_VOUT_COMMAND) * N
            
    def vout_max(self, value = None):
        if value is not None:
            self.write_register(self.REG_VOUT_MAX, value/N)
        else:
            return self.read_register(self.REG_VOUT_MAX) * N
            
    def vout_margin_high(self, value = None):
        if value is not None:
            self.write_register(self.REG_VOUT_MARGIN_HIGH, value/N)
        else:
            return self.read_register(self.REG_VOUT_MARGIN_HIGH) * N

    def vout_margin_low(self, value = None):
        if value is not None:
            self.write_register(self.REG_VOUT_MARGIN_LOW, value/N)
        else:
            return self.read_register(self.REG_VOUT_LOW) * N

    def vin_on(self, value = None):
        if value is not None:
            self.write_register(self.REG_VIN_ON, value)
        else:
            raw_vin_on = self.read_register(self.REG_VIN_ON)
            vin_on_value = int((hex(raw_vin_on & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_vin_on & 0xF800) >> 11 ))
            return  vin_on_value

    def vin_off(self, value = None):
        if value is not None:
            self.write_register(self.REG_VIN_OFF, value)
        else:
            raw_vin_off = self.read_register(self.REG_VIN_OFF)
            vin_off_value = int((hex(raw_vin_off & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_vin_off & 0xF800) >> 11 ))
            return  vin_off_value

    def iout_cal_gain(self):
        raw_iout_cal_gain = self.read_register(self.REG_IOUT_CAL_GAIN)
        iout_cal_gain_value = int((hex(raw_iout_cal_gain & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_iout_cal_gain & 0xF800) >> 11 ))
        return iout_cal_gain_value

    def vout_ov_fault_limit(self, value = None):
        if value is not None:
            self.write_register(self.VOUT_OV_FAULT_LIMIT, value/N)
        else:
            return self.read_register(self.VOUT_OV_FAULT_LIMIT) * N

    def vout_ov_fault_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_VOUT_OV_FAULT_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_VOUT_OV_FAULT_RESPONSE)

    def vout_ov_warn_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_VOUT_OV_WARN_LIMIT, value/N)
        else:
            return self.read_register(self.REG_VOUT_OV_WARN_LIMIT) * N

    def vout_uv_warn_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_VOUT_UV_WARN_LIMIT, value/N)
        else:
            return self.read_register(self.REG_VOUT_UV_WARN_LIMIT) * N

    def vout_uv_fault_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_VOUT_UV_FAULT_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_VOUT_UV_FAULT_RESPONSE)

    def iout_oc_fault_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_IOUT_OC_FAULT_LIMIT, value)
        else:
            raw_iout_oc_fault_limit = self.read_register(self.REG_IOUT_OC_FAULT_LIMIT)
            iout_oc_fault_limit_value = int((hex(raw_iout_oc_fault_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_iout_oc_fault_limit & 0xF800) >> 11 ))
            return  iout_oc_fault_limit_value

    def iout_oc_fault_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_IOUT_OC_FAULT_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_IOUT_OC_FAULT_RESPONSE)

    def iout_oc_warn_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_IOUT_OC_WARN_LIMIT, value)
        else:
            raw_iout_oc_warn_limit = self.read_register(self.REG_IOUT_OC_WARN_LIMIT)
            iout_oc_warn_limit_value = int((hex(raw_iout_oc_warn_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_iout_oc_warn_limit & 0xF800) >> 11 ))
            return  iout_oc_warn_limit_value

    def iout_uc_fault_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_IOUT_UC_FAUILT_LIMIT, value)
        else:
            raw_iout_uc_fault_limit = self.read_register(self.REG_IOUT_UC_FAUILT_LIMIT)
            raw_iout_uc_fault_limitvalue = int((hex(raw_iout_uc_fault_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_iout_uc_fault_limit & 0xF800) >> 11 ))
            return  raw_iout_uc_fault_limitvalue

    def iout_uc_fault_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_IOUT_UC_FAULT_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_IOUT_UC_FAULT_RESPONSE)

    def ot_fault_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_OT_FAULT_LIMIT, value)
        else:
            raw_ot_fault_limit = self.read_register(self.REG_OT_FAULT_LIMIT)
            ot_fault_limitvalue = int((hex(raw_ot_fault_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_ot_fault_limit & 0xF800) >> 11 ))
            return  ot_fault_limitvalue

    def ot_fault_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_OT_FAULT_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_OT_FAULT_RESPONSE)

    def ot_warn_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_OT_WARN_LIMIT, value)
        else:
            raw_ot_warn_limit = self.read_register(self.REG_OT_WARN_LIMIT)
            ot_warn_limit_value = int((hex(raw_ot_warn_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_ot_warn_limit & 0xF800) >> 11 ))
            return  ot_warn_limit_value

    def ut_warn_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_UT_WARN_LIMIT, value)
        else:
            raw_ut_warn_limit = self.read_register(self.REG_OT_WARN_LIMIT)
            ut_warn_limit_value = int((hex(raw_ut_warn_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_ut_warn_limit & 0xF800) >> 11 ))
            return  ut_warn_limit_value

    def ut_fault_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_UT_FAULT_LIMIT, value)
        else:
            raw_ut_fault_limit = self.read_register(self.REG_UT_FAULT_LIMIT)
            ut_fault_limit_value = int((hex(raw_ut_fault_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_ut_fault_limit & 0xF800) >> 11 ))
            return  ut_fault_limit_value

    def vin_ov_fault_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_VIN_OV_FAULT_LIMIT, value)
        else:
            raw_vin_ov_fault_limit = self.read_register(self.REG_VIN_OV_FAULT_LIMIT)
            vin_ov_fault_limit_value = int((hex(raw_vin_ov_fault_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_vin_ov_fault_limit & 0xF800) >> 11 ))
            return  vin_ov_fault_limit_value

    def vin_ov_fault_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_VIN_OV_FAULT_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_VIN_OV_FAULT_RESPONSE)

    def vin_ov_warn_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_VIN_OV_WARN_LIMIT, value)
        else:
            raw_vin_ov_warn_limit = self.read_register(self.REG_VIN_OV_WARN_LIMIT)
            vin_ov_warn_limit_value = int((hex(raw_vin_ov_warn_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_vin_ov_warn_limit & 0xF800) >> 11 ))
            return  vin_ov_warn_limit_value

    def vin_uv_warn_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_VIN_UV_WARN_LIMIT, value)
        else:
            raw_vin_uv_warn_limit = self.read_register(self.REG_VIN_UV_WARN_LIMIT)
            vin_uv_warn_limit_value = int((hex(raw_vin_uv_warn_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_vin_uv_warn_limit & 0xF800) >> 11 ))
            return  vin_uv_warn_limit_value

    def vin_uv_fault_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_VIN_UV_FAULT_LIMIT, value)
        else:
            raw_vin_uv_fault_limit = self.read_register(self.REG_VIN_UV_FAULT_LIMIT)
            vin_uv_fault_limit_value = int((hex(raw_vin_uv_fault_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_vin_uv_fault_limit & 0xF800) >> 11 ))
            return  vin_uv_fault_limit_value

    def vin_uv_fault_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_VIN_UV_FAULT_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_VIN_UV_FAULT_RESPONSE)

    def power_good_on(self, value = None):
        if value is not None:
            self.write_register(self.REG_POWER_GOOD_ON, value/N)
        else:
            return self.read_register(self.REG_POWER_GOOD_ON) * N

    def power_good_off(self, value = None):
        if value is not None:
            self.write_register(self.REG_POWER_GOOD_OFF, value/N)
        else:
            return self.read_register(self.REG_POWER_GOOD_OFF) * N

    def ton_delay(self, value = None):
        if value is not None:
            self.write_register(self.REG_TON_DELAY, value)
        else:
            raw_ton_delay = self.read_register(self.REG_TON_DELAY)
            ton_delay_value = int((hex(raw_ton_delay & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_ton_delay & 0xF800) >> 11 ))
            return  ton_delay_value

    def ton_rise(self, value = None):
        if value is not None:
            self.write_register(self.REG_TON_RISE, value)
        else:
            raw_ton_rise = self.read_register(self.REG_TON_RISE)
            ton_rise_value = int((hex(raw_ton_rise & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_ton_rise & 0xF800) >> 11 ))
            return  ton_rise_value

    def ton_max_fault_limit(self, value = None):
        if value is not None:
            self.write_register(self.REG_TON_MAX_FAULT_LIMIT, value)
        else:
            raw_ton_max_fault_limit = self.read_register(self.REG_TON_MAX_FAULT_LIMIT)
            ton_max_fault_limit_value = int((hex(raw_ton_max_fault_limit & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_ton_max_fault_limit & 0xF800) >> 11 ))
            return  ton_max_fault_limit_value

    def ton_max_fault_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_TON_MAX_FAULT_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_TON_MAX_FAULT_RESPONSE)

    def toff_delay(self, value = None):
        if value is not None:
            self.write_register(self.REG_TOFF_DELAY, value)
        else:
            raw_toff_delay = self.read_register(self.REG_TOFF_DELAY)
            toff_delay_value = int((hex(raw_toff_delay & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_toff_delay & 0xF800) >> 11 ))
            return  toff_delay_value

    def status_byte(self):
        return self.read_register_byte(self.REG_STATUS_BYTE)

    def status_word(self):
        return self.read_register(self.REG_STATUS_WORD)

    def status_vout(self):
        return self.read_register_byte(self.REG_STATUS_VOUT)

    def status_iout(self):
        return self.read_register_byte(self.REG_STATUS_IOUT)

    def status_input(self):
        return self.read_register_byte(self.REG_STATUS_INPUT)

    def status_temperature(self):
        return self.read_register_byte(self.REG_STATUS_TEMPERATURE)

    def status_cml(self):
        return self.read_register_byte(self.REG_STATUS_CML)

    def status_mfr_specific(self):
        return self.read_register_byte(self.REG_STATUS_MFR_SPECIFIC)

    def read_vin(self):
        raw_read_vin = self.read_register(self.REG_READ_VIN)
        read_vin_value = int((hex(raw_read_vin & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_read_vin & 0xF800) >> 11 ))
        return  read_vin_value

    def read_iin(self):
        raw_read_iin = self.read_register(self.REG_READ_IIN)
        read_iin_value = int((hex(raw_read_iin & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_read_iin & 0xF800) >> 11 ))
        return  read_iin_value

    def read_vout(self):
        return self.read_register(self.REG_READ_VOUT) * N

    def read_iout(self):
        raw_read_iout = self.read_register(self.REG_READ_IIN)
        read_iout_value = int((hex(raw_read_iout & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_read_iout & 0xF800) >> 11 ))
        return  read_iout_value

    def read_temperature_1(self):
        raw_read_temperature = self.read_register(self.REG_READ_TEMPERATURE_1)
        read_temperature_value = int((hex(raw_read_temperature & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_read_temperature & 0xF800) >> 11 ))
        return read_temperature_value

    def read_temperature_2(self):
        raw_read_temperature = self.read_register(self.REG_READ_TEMPERATURE_2)
        read_temperature_value = int((hex(raw_read_temperature & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_read_temperature & 0xF800) >> 11 ))
        return read_temperature_value

    def read_pout(self):
        raw_read_pout = self.read_register(self.REG_READ_IIN)
        read_pout_value = int((hex(raw_read_pout & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_read_pout & 0xF800) >> 11 ))
        return  read_pout_value

    def read_pin(self):
        raw_read_pin = self.read_register(self.REG_READ_IIN)
        read_pin_value = int((hex(raw_read_pin & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_read_pin & 0xF800) >> 11 ))
        return read_pin_value

    def pm_bus_revision(self):
        return self.read_register_byte(self.REG_PMBUS_REVISION)

    def user_data_00(self, value = None):
        if value is not None:
            self.write_register(self.REG_USER_DATA_00, value)
        else:
            return self.read_register(self.REG_USER_DATA_00)

    def user_data_01(self, value = None):
        if value is not None:
            self.write_register(self.REG_USER_DATA_01, value)
        else:
            return self.read_register(self.REG_USER_DATA_01)

    def user_data_02(self, value = None):
        if value is not None:
            self.write_register(self.REG_USER_DATA_02, value)
        else:
            return self.read_register(self.REG_USER_DATA_02)

    def user_data_03(self, value = None):
        if value is not None:
            self.write_register(self.REG_USER_DATA_03, value)
        else:
            return self.read_register(self.REG_USER_DATA_03)

    def user_data_04(self, value = None):
        if value is not None:
            self.write_register(self.REG_USER_DATA_04, value)
        else:
            return self.read_register(self.REG_USER_DATA_04)

    def mfr_ltc_reserved_1(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_LTC_RESERVED_1, value)
        else:
            return self.read_register(self.REG_MFR_LTC_RESERVED_1)

    def mfr_t_self_heat(self):
         return self.read_register(self.REG_MFR_T_SELF_HEAT)

    def mfr_iou_cal_gain_tau_inv(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_IOUT_CAL_GAIN_TAU_INV, value)
        else:
            raw_mfr_iou_cal_gain_tau_inv = self.read_register(self.REG_MFR_IOUT_CAL_GAIN_TAU_INV)
            mfr_iou_cal_gain_tau_invself_value = int((hex(raw_mfr_iou_cal_gain_tau_inv & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_iou_cal_gain_tau_inv & 0xF800) >> 11 ))
            return mfr_iou_cal_gain_tau_invself_value

    def mfr_iout_cal_gain_theta(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_IOUT_CAL_GAIN_THETA, value)
        else:
            raw_mfr_iout_cal_gain_theta = self.read_register(self.REG_MFR_IOUT_CAL_GAIN_THETA)
            mfr_iout_cal_gain_theta_value = int((hex(raw_mfr_iout_cal_gain_theta & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_iout_cal_gain_theta & 0xF800) >> 11 ))
            return mfr_iout_cal_gain_theta_value

    def mfr_read_iout(self):
        return self.read_register(self.REG_MFR_READ_IOUT)

    def mfr_ltc_reserved_2(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_LTC_RESERVED_2, value)
        else:
            return self.read_register(self.REG_MFR_LTC_RESERVED_2)

    def mfr_ee_unlock(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_EE_UNLOCK, value)
        else:
            return self.read_register_byte(self.REG_MFR_EE_UNLOCK)

    def mfr_ee_erase(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_EE_ERASE, value)
        else:
            return self.read_register_byte(self.REG_MFR_EE_ERASE)

    def mfr_ee_data(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_EE_DATA, value)
        else:
            return self.read_register(self.REG_MFR_EE_DATA)

    def mfr_ein(self):
         return self.read_register_block(self.REG_MFR_EIN)

    def mfr_ein_config(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_EIN_CONFIG, value)
        else:
            return self.read_register_byte(self.REG_MFR_EIN_CONFIG)

    def mfr_special_lot(self):
         return self.read_register_byte(self.REG_MFR_SPECIAL_LOT)

    def mfr_iin_cal_gain_tc(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_IIN_CAL_GAIN_TC, value)
        else:
            return self.read_register(self.REG_MFR_IIN_CAL_GAIN_TC)

    def mfr_iin_peak(self):
        raw_mfr_iin_peak = self.read_register(self.REG_MFR_IIN_PEAK)
        mfr_iin_peak_value = int((hex(raw_mfr_iin_peak & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_iin_peak & 0xF800) >> 11 ))
        return mfr_iin_peak_value

    def mfr_iin_min(self):
        raw_mfr_iin_min = self.read_register(self.REG_MFR_IIN_MIN)
        mfr_iin_min_value = int((hex(raw_mfr_iin_min & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_iin_min & 0xF800) >> 11 ))
        return mfr_iin_min_value

    def mfr_pin_peak(self):
        raw_mfr_pin_peak = self.read_register(self.REG_MFR_PIN_PEAK)
        raw_mfr_pin_peak_value = int((hex(raw_mfr_pin_peak & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_pin_peak & 0xF800) >> 11 ))
        return raw_mfr_pin_peak_value

    def mfr_pin_min(self):
        raw_mfr_pin_min = self.read_register(self.REG_MFR_PIN_MIN)
        mfr_pin_min_value = int((hex(raw_mfr_pin_min & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_pin_min & 0xF800) >> 11 ))
        return mfr_pin_min_value

    def mfr_command_plus(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_COMMAND_PLUS, value)
        else:
            return self.read_register(self.REG_MFR_COMMAND_PLUS)

    def mfr_data_plus0(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_DATA_PLUS0, value)
        else:
            return self.read_register(self.REG_MFR_DATA_PLUS0)

    def mfr_data_plus1(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_DATA_PLUS1, value)
        else:
            return self.read_register(self.REG_MFR_DATA_PLUS1)

    def mfr_config_ltm4673(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_CONFIG_LTM4673, value)
        else:
            return self.read_register(self.REG_MFR_CONFIG_LTM4673)

    def mfr_config_all_ltm4673(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_CONFIG_ALL_LTM4673, value)
        else:
            return self.read_register(self.REG_MFR_CONFIG_ALL_LTM4673)

    def mfr_faultb0_propagate(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_FAULTB0_PROPAGATE, value)
        else:
            return self.read_register_byte(self.REG_MFR_FAULTB0_PROPAGATE)

    def mfr_faultb1_propagate(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_FAULTB1_PROPAGATE, value)
        else:
            return self.read_register_byte(self.REG_MFR_FAULTB1_PROPAGATE)

    def mfr_pwrgd_en(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_PWRGD_EN, value)
        else:
            return self.read_register(self.REG_MFR_PWRGD_EN)

    def mfr_faultb0_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_FAULTB0_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_MFR_FAULTB0_RESPONSE)

    def mfr_faultb1_response(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_FAULTB1_RESPONSE, value)
        else:
            return self.read_register_byte(self.REG_MFR_FAULTB1_RESPONSE)

    def mfr_iout_peak(self):
        raw_mfr_iout_peak = self.read_register(self.REG_MFR_IOUT_PEAK)
        mfr_iout_peak_value = int((hex(raw_mfr_iout_peak & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_iout_peak & 0xF800) >> 11 ))
        return mfr_iout_peak_value

    def mfr_iout_min(self):
        raw_mfr_iout_min = self.read_register(self.REG_MFR_IOUT_PEAK)
        mfr_iout_min_value = int((hex(raw_mfr_iout_min & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_iout_min & 0xF800) >> 11 ))
        return mfr_iout_min_value

    def mfr_config2_ltm4673(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_CONFIG2_LTM4673, value)
        else:
            return self.read_register_byte(self.REG_MFR_CONFIG2_LTM4673)

    def mfr_config3_ltm4673(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_CONFIG3_LTM4673, value)
        else:
            return self.read_register_byte(self.REG_MFR_CONFIG3_LTM4673)

    def mfr_retry_delay(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_RETRY_DELAY, value)
        else:
            raw_mfr_retry_delay = self.read_register(self.REG_MFR_RETRY_DELAY)
            mfr_retry_delay_value = int((hex(raw_mfr_retry_delay & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_retry_delay & 0xF800) >> 11 ))
            return mfr_retry_delay_value

    def mfr_restart_delay(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_RESTART_DELAY, value)
        else:
            raw_mfr_restart_delay = self.read_register(self.REG_MFR_RESTART_DELAY)
            mfr_restart_delay_value = int((hex(raw_mfr_restart_delay & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_restart_delay & 0xF800) >> 11 ))
            return mfr_restart_delay_value

    def mfr_vout_peak(self):
        return self.read_register(self.REG_MFR_VOUT_PEAK) * N

    def mfr_vin_peak(self):
        return self.read_register(self.REG_MFR_VIN_PEAK) * N

    def mfr_temperature_1_peak(self):
        return self.read_register(self.REG_MFR_TEMPERATURE_1_PEAK) * N

    def mfr_dac(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_DAC, value)
        else:
            return self.read_register(self.REG_MFR_DAC)

    def mfr_powergood_assertion_delay(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_POWERGOOD_ASSERTION_DELAY, value)
        else:
            raw_mfr_powergood_assertion_delay = self.read_register(self.REG_MFR_POWERGOOD_ASSERTION_DELAY)
            mfr_powergood_assertion_delay_value = int((hex(raw_mfr_powergood_assertion_delay & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_powergood_assertion_delay & 0xF800) >> 11 ))
            return mfr_powergood_assertion_delay_value

    def mfr_watchdog_t_first(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_WATCHDOG_T_FIRST, value)
        else:
            raw_mfr_watchdog_t_first = self.read_register(self.REG_MFR_WATCHDOG_T_FIRST)
            mfr_watchdog_t_first_value = int((hex(raw_mfr_watchdog_t_first & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_watchdog_t_first & 0xF800) >> 11 ))
            return mfr_watchdog_t_first_value

    def mfr_watchdog_t_first(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_WATCHDOG_T, value)
        else:
            raw_mfr_watchdog_t = self.read_register(self.REG_MFR_WATCHDOG_T)
            mfr_watchdog_t_value = int((hex(raw_mfr_watchdog_t & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_watchdog_t & 0xF800) >> 11 ))
            return mfr_watchdog_t_value

    def mfr_page_ff_mask(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_PAGE_FF_MASK, value)
        else:
            return self.read_register_byte(self.REG_MFR_PAGE_FF_MASK)

    def mfr_pads(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_PADS, value)
        else:
            return self.read_register(self.REG_MFR_PADS)

    def mfr_i2c_bade_address(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_I2C_BASE_ADDRESS, value)
        else:
            return self.read_register_byte(self.REG_MFR_I2C_BASE_ADDRESS_MASK)

    def mfr_special_id(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_SPECIAL_ID, value)
        else:
            return self.read_register(self.REG_MFR_SPECIAL_ID)

    def mfr_iin_cal_gain(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_IIN_CAL_GAIN, value)
        else:
            raw_mfr_iin_cal_gain= self.read_register(self.REG_MFR_IIN_CAL_GAIN)
            mfr_iin_cal_gain_value = int((hex(raw_mfr_iin_cal_gain & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_iin_cal_gain & 0xF800) >> 11 ))
            return mfr_iin_cal_gain_value

    def mfr_vout_discharge_threshold(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_VOUT_DISCHARGE_THRESHOLD, value)
        else:
            raw_mfr_vout_discharge_threshold= self.read_register(self.REG_MFR_VOUT_DISCHARGE_THRESHOLD)
            mfr_vout_discharge_threshold_value = int((hex(raw_mfr_vout_discharge_threshold & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_vout_discharge_threshold & 0xF800) >> 11 ))
            return mfr_vout_discharge_threshold_value

    def mfr_fault_log_store(self, value):
        self.write_register_byte(self.REG_MFR_FAULT_LOG_STORE, value)

    def mfr_fault_log_restore(self, value):
        self.write_register_byte(self.REG_MFR_FAULT_LOG_RESTORE, value)

    def mfr_fault_log_clear(self, value):
        self.write_register_byte(self.REG_MFR_FAULT_LOG_CLEAR, value)

    def mfr_fault_log_status(self):
        return self.read_register_byte(self.REG_MFR_FAULT_LOG_STATUS)

    def mfr_fault_log(self):
        return self.read_register_block(self.REG_MFR_FAULT_LOG)

    def mfr_common(self):
        return self.read_register_byte(self.REG_MFR_COMMON)

    def mfr_special_id(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_SPECIAL_ID, value)
        else:
            return self.read_register(self.REG_MFR_SPECIAL_ID)

    def mfr_retry_count(self, value = None):
        if value is not None:
            self.write_register_byte(self.REG_MFR_RETRY_COUNT, value)
        else:
            return self.read_register_byte(self.REG_MFR_RETRY_COUNT)

    def mfr_temp_1_offset(self, value = None):
        if value is not None:
            self.write_register(self.REG_MFR_TEMP_1_OFFSET, value)
        else:
            raw_mfr_temp_1_offset = self.read_register(self.REG_MFR_TEMP_1_OFFSET)
            mfr_temp_1_offset_value = int((hex(raw_mfr_temp_1_offset & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_temp_1_offset & 0xF800) >> 11 ))
            return mfr_temp_1_offset_value

    def mfr_vout_min(self):
        return self.read_register(self.REG_MFR_VOUT_MIN) * N

    def mfr_vin_min(self):
        raw_mfr_vin_min = self.read_register(self.REG_MFR_VIN_MIN)
        mfr_vin_min_value = int((hex(raw_mfr_vin_min & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_vin_min & 0xF800) >> 11 ))
        return mfr_vin_min_value

    def mfr_temperature_1_min(self):
        raw_mfr_temperature_1_min = self.read_register(self.REG_MFR_TEMPERATURE_1_MIN)
        mfr_temperature_1_min_value = int((hex(raw_mfr_temperature_1_min & 0x7FF)),16)*2**self.hex_to_signed( hex((raw_mfr_temperature_1_min & 0xF800) >> 11 ))
        return mfr_temperature_1_min_value
