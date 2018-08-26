import os, sys, traceback, time

sys.path.insert(0, (os.path.dirname(os.path.abspath(__file__).replace('SampleScripts', 'Modules'))))
from IxNetRestApi import *
from IxNetRestApiProtocol import Protocol
from IxNetRestApiTraffic import Traffic
from IxNetRestApiFileMgmt import FileMgmt
from IxNetRestApiPortMgmt import PortMgmt
from IxNetRestApiStatistics import Statistics
from IxNetRestApiPacketCapture import PacketCapture

# Default the API server to either windows or linux.
osPlatform = 'windows'

if len(sys.argv) > 1:
    if sys.argv[1] not in ['windows', 'windowsConnectionMgr', 'linux']:
        sys.exit("\nError: %s is not a known option. Choices are 'windows' or 'linux'." % sys.argv[1])
    osPlatform = sys.argv[1]

try:
    #---------- Preference Settings --------------

    forceTakePortOwnership = True
    releasePortsWhenDone = False
    enableDebugTracing = True
    deleteSessionAfterTest = False ;# For Windows Connection Mgr and Linux API server only

    # If the licenses are activated in the Linux based XGS chassis or if the licenses are configured 
    # in the Windows IxNetwork GUI API server in preferences, then you won't need to config license.
    configLicense = True
    licenseServerIp = '192.168.70.3'
    licenseModel = 'subscription'
    licenseTier = 'tier3'

    ixChassisIp = '192.168.70.11'
    # [chassisIp, cardNumber, slotNumber]
    portList = [[ixChassisIp, '1', '1'],
                [ixChassisIp, '2', '1']]

    if osPlatform == 'linux':
        mainObj = Connect(apiServerIp='192.168.70.121',
                          serverIpPort='443',
                          username='admin',
                          password='admin',
                          deleteSessionAfterTest=deleteSessionAfterTest,
                          verifySslCert=False,
                          serverOs=osPlatform,
                          apiKey='9277fc8fe92047f6a126f54481ba07fc',
                          sessionId=1
                          )

    if osPlatform in ['windows', 'windowsConnectionMgr']:
        mainObj = Connect(apiServerIp='192.168.70.3',
                          serverIpPort='11009',
                          serverOs=osPlatform,
                          deleteSessionAfterTest=deleteSessionAfterTest
                          )
    
    trafficObj = Traffic(mainObj)
    statObj = Statistics(mainObj)
    protocolObj = Protocol(mainObj)

    #protocolObj.verifyProtocolSessionsUp('BGP Peer Per Port')

    #statObj.takeSnapshot(viewName='Flow Statistics', isLinux=True, localLinuxPath='/home/hgee')
    statObj.takeSnapshot(viewName='Flow Statistics', windowsPath='c:\\Results', localLinuxPath='/home/hgee')

    '''
    #trafficObj.startTraffic(regenerateTraffic=False, applyTraffic=True)
    stats = statObj.getStats(viewName='Flow Statistics')
    #stats = statObj.getStats(viewName='Protocols Summary')
    #print(type(stats))

    for key,value in stats.items():
        print('\n{0: {1}\n'.format(key, value))
        #print(key)
    '''

except (IxNetRestApiException, Exception, KeyboardInterrupt) as errMsg:
    print('\nTest failed! {0}\n'.format(traceback.print_exc()))
    print(errMsg)
    if osPlatform == 'linux':
        mainObj.linuxServerStopAndDeleteSession()
