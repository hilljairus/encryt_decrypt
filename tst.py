import string
from encrypt import *
from decrypt import *

message = "MACHINE LEARNING IS THE STUDY OF COMPUTER ALGORITHMS THAT IMPROVE AUTOMATICALLY "\
"THROUGH EXPERIENCE AND BY THE USE OF DATA. IT IS SEEN AS A PART OF ARTIFICIAL "\
"INTELLIGENCE. MACHINE LEARNING ALGORITHMS BUILD A MODEL BASED ON SAMPLE DATA KNOWN "\
"AS TRAINING DATA IN ORDER TO MAKE PREDICTIONS OR DECISIONS WITHOUT BEING EXPLICITLY "\
"PROGRAMMED TO DO SO."\
 
expected = "QGLRI PIVRRK MW XLI WXH] SJ GQTXV EPKVXLQW XLX MQTVZI EXQXGPP] XLVSKL I\TVMRGI ERH "\
"F] XLI YWI SJ HXE2 MX MW WIR EW E TVX SJ EVXJGMP MRXPPKRGI2 QGLRI PIVRRK EPKVXLQW "\
"FYPH E QHP FWH SR WQTPI HXE OR[R EW XVERRK HXE MR SVHV XS QOI TVHGXMRW SV HGWMRW "\
"[XLSX FIRK I\TPGXP] TVKVQQH XS HS WS2"
test_encrypt= Encrypt(message)
test_decrypt = Decrypt(expected)

if __name__=='__main__':
    if (test_encrypt.encrypt_message()==expected):
        print("ENCRYPT PASSED")
    else:
        print("ENCRYPT FAILED")
    if (test_decrypt.decrypt_message()==message):
        print("DECRYPT PASSED")
    else:
        print("DECRYPT FAILED")
#brk = 0
# for i in range(len(expected)):

#     if(expected[i]!=test_encrypt.encrypt_message()[i]):
#         brk += i
#         break
# print(i)
# print(expected[i: ])
# print(test_encrypt.encrypt_message()[i: ])
# print(expected[i]==test_encrypt.encrypt_message()[i])
