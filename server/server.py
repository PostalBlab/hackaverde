import asyncio
from aioconsole import ainput
import hexdump
import binascii
import sys
from bvmessage import *

LOGFILE_LOCATION = "dump.log"
LOGFILE = open(LOGFILE_LOCATION, 'a')
loop = None

def logfile(logmessage):
    LOGFILE.write(logmessage)
    LOGFILE.write("\n")
    LOGFILE.flush()

class EchoServerProtocol(asyncio.Protocol):

    identified = None

    def connection_made(self, transport):
        global loop
        loop.create_task(self.menu())
        peername = transport.get_extra_info('peername')
        self.transport = transport

    def data_received(self, data):
        while True:
            logfile(" < < < Received from machine:")
            logfile(hexdump.hexdump(data, 'return'))
            package_length = data[0] * 256 + data[1]
            #logfile("Length: " + str(package_length))
            payload = data[2:package_length + 2]
            #logfile("Payload: ")
            if len(payload) > 0:
                #0 means no data packet but stuff like ACK packages
                if payload[0] == 0:
                    #REQ
                    if payload[1] & 0xf0 == 0x00:
                        logfile("REQ received, implement me")
                    #ACK, sending to the machine for ACK the package
                    elif payload[1] & 0xf0 == 0x10:
                        logfile("ACK received, implement me")
                    #SPO
                    elif payload[1] & 0xf0 == 0x20:
                        logfile("SPO received, implement me")
                    #CCL, looks like sensor registering and machine registering
                    elif payload[1] & 0xf0 == 0x40:
                        logfile("CCL with RID != 1 received, implement me")
                    #SML, seems like state change stuff
                    elif payload[1] == 0x50:
                        #received event like register sensors
                        if payload[2] % 0xf0 == 0x40:
                            logfile("Event received")
                        #self.write_with_log(build_package(b'\x00' + (0x10 | (payload[1] & 0x0f)).to_bytes(1, byteorder="big") + b'\x00\x01'))
                
                    #this looks like a "give sensor infos plz" stub.class onFnCall for more infos
                    #self.write_with_log(build_package(b'\x00\x50\x20\x00\x00 \x00\x02 \x00'))

                #it is the identify package
                elif payload[0] == 0x41:
                    self.write_with_log(build_package(b"AsensorLogic"))
                else:
                    logfile("Data packet received")
            else:
                #empty ping message received, answer with "pong"
                self.write_with_log(build_package(b''))
            #iterate trough multiple message
            if len(data) > package_length + 2:
                #print("multiple messages found")
                data = data[package_length + 2:]
            else:
                break


    def write_with_log(self, data):
        logfile(" > > > Sending to machine:")
        logfile(hexdump.hexdump(data, 'return'))
        self.transport.write(data)

    async def menu(self):
        print("Hackaverde Menu")
        print("")
        while True:
            print("1. Send machine state on")
            print("2. Send DEBUG_NFC_TAG package")
            print("3. Send GRIND_AND_BREW_NFC_TAG package")
            print("4. Send ROAST_ONLY_NFC_TAG package")
            print("5. Send COFFEE_CHANGER_BADGE_NFC_TAG package")
            print("6. Send AIRFILTER_MULTI_USE_NFC_TAG package")
            print("7. Send ADVENTURE_14_SLOW_NFC_TAG package")
            print("8. Send ADVENTURE_4_QUICKIE_NFC_TAG package")
            line = await ainput(">>> ")
            if line == "1":
                #set machine state to start
                self.write_with_log(b'\x00\x0C\x00\x50\x20\x00\x0c\x00\x02\x22\x01\x00\x00\x00')
                
            elif line == "2":
                self.write_with_log(get_full_nfc_tag_package(DEBUG_NFC_TAG))
            elif line == "3":
                self.write_with_log(get_full_nfc_tag_package(GRIND_AND_BREW_NFC_TAG))
            elif line == "4":
                self.write_with_log(get_full_nfc_tag_package(ROAST_ONLY_NFC_TAG))
            elif line == "5":
                self.write_with_log(get_full_nfc_tag_package(COFFEE_CHANGER_BADGE_NFC_TAG))
            elif line == "6":
                self.write_with_log(get_full_nfc_tag_package(AIRFILTER_MULTI_USE_NFC_TAG))
            elif line == "7":
                self.write_with_log(get_full_nfc_tag_package(ADVENTURE_14_SLOW_NFC_TAG))
            elif line == "8":
                self.write_with_log(get_full_nfc_tag_package(ADVENTURE_4_QUICKIE_NFC_TAG))

            else:
                print("Command not found")

async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    global loop
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '0.0.0.0', 17198)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())