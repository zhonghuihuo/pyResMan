'''
Created on 2017/3/19

@author: JavaCardOS
'''

from pyResMan.MifareTLV import MifareCommandTLV, MifareResponseTLV,\
    COMMAND_TAG_DECREMENT
from pyResMan.MifareTLV import COMMAND_TAG_AUTHENTICATION, COMMAND_TAG_READ_BLOCK, COMMAND_TAG_WRITE_BLOCK, COMMAND_TAG_INCREMENT\
                               , COMMAND_TAG_DECREMENT, COMMAND_TAG_RESTORE, COMMAND_TAG_TRANSFER, COMMAND_TAG_SETUP

class LibSC(object):
    '''
    Library for smartcard functions;
    '''


    def __init__(self, interface):
        self.__interface = interface
    
    def M1_authentication(self, block_number, key_type, key, uid):
        command_tlv = MifareCommandTLV(COMMAND_TAG_AUTHENTICATION)
        command_tlv.set_block_number(block_number)
        command_tlv.set_key_type(key_type)
        command_tlv.set_key_value(key)
        command_tlv.set_uid(uid)
        command = command_tlv.serialize()
        response = self.__interface.transmit_sc_command(command)
        response_tlv = MifareResponseTLV(response)
        return response_tlv.get_error()

    def M1_read_block(self, block_number):
        command_tlv = MifareCommandTLV(COMMAND_TAG_READ_BLOCK)
        command_tlv.set_block_number(block_number)
        command_tlv.set_rw_len(0x10)
        command = command_tlv.serialize()
        response = self.__interface.transmit_sc_command(command)
        response_tlv = MifareResponseTLV(response)
        return response_tlv.get_error(), response_tlv.get_block_data()
    
    def M1_write_block(self, block_number, block_data):
        print(block_number)
        print(len(block_data))
        for i in range(len(block_data)):
            print('%02X' %(ord(block_data[i]))),
        command_tlv = MifareCommandTLV(COMMAND_TAG_WRITE_BLOCK)
        command_tlv.set_block_number(block_number)
        command_tlv.set_block_data(block_data)
        command_tlv.set_rw_len(len(block_data))
        command = command_tlv.serialize()
        response = self.__interface.transmit_sc_command(command)
        response_tlv = MifareResponseTLV(response)
        return response_tlv.get_error()
    
    def M1_increment(self, block_number, inc_operand):
        command_tlv = MifareCommandTLV(COMMAND_TAG_INCREMENT)
        command_tlv.set_block_number(block_number)
        command_tlv.set_incdec_operand(inc_operand)
        command = command_tlv.serialize()
        response = self.__interface.transmit_sc_command(command)
        response_tlv = MifareResponseTLV(response)
        return response_tlv.get_error()
    
    def M1_decrement(self, block_number, dec_operand):
        command_tlv = MifareCommandTLV(COMMAND_TAG_DECREMENT)
        command_tlv.set_block_number(block_number)
        command_tlv.set_incdec_operand(dec_operand)
        command = command_tlv.serialize()
        response = self.__interface.transmit_sc_command(command)
        response_tlv = MifareResponseTLV(response)
        return response_tlv.get_error()
    
    def M1_restore(self, block_number):
        command_tlv = MifareCommandTLV(COMMAND_TAG_RESTORE)
        command_tlv.set_block_number(block_number)
        command = command_tlv.serialize()
        response = self.__interface.transmit_sc_command(command)
        response_tlv = MifareResponseTLV(response)
        return response_tlv.get_error()
    
    def M1_transfer(self, block_number):
        command_tlv = MifareCommandTLV(COMMAND_TAG_TRANSFER)
        command_tlv.set_block_number(block_number)
        command = command_tlv.serialize()
        response = self.__interface.transmit_sc_command(command)
        response_tlv = MifareResponseTLV(response)
        return response_tlv.get_error()
        
    def M1_setup(self):
        command_tlv = MifareCommandTLV(COMMAND_TAG_SETUP)
        command = command_tlv.serialize()
        response = self.__interface.transmit_sc_command(command)
        response_tlv = MifareResponseTLV(response)
        return response_tlv.get_error()
    