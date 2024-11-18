Thank you chris-ritsen for creating network-audio-controller -> (https://github.com/chris-ritsen/network-audio-controller)

This fork focuses on using network-audio-controller as part of a wider control system ecosystem.
Emphasis has been given to reintroducing ability to narrow down command focus, and stipping down the terminal out some what meaning easier parsing of the interformation.

Example reintroducing te ability to quiery te subscription status of a single device or channel;



```python
class SubscriptionListCommand(Command):
    name = "list"
    description = "List subscriptions"

    options = [
        option("json", None, "Output as JSON", flag=True),
        option("rx-channel-name", None, "Filter by Rx channel name", flag=False),
        option("rx-channel-number", None, "Filter by Rx channel number", flag=False),
        option("rx-device-host", None, "Filter by Rx device host", flag=False),
        option("rx-device-name", None, "Filter by Rx device name", flag=False),
        option("tx-channel-name", None, "Filter by Tx channel name", flag=False),
        option("tx-channel-number", None, "Filter by Tx channel number", flag=False),
        option("tx-device-host", None, "Filter by Tx device host", flag=False),
        option("tx-device-name", None, "Filter by Tx device name", flag=False),
    ]
```


Also attention has been made to reduce cli output, making it easier and quicker to parse information for systems using netaudio;
Bellow chnages to dante/browser.py
```python
@contextlib.contextmanager
def suppress_stderr():
    """Temporarily suppress stderr output"""
    stderr = sys.stderr
    sys.stderr = StringIO()
    try:
        yield
    finally:
        sys.stderr = stderr
```

Output of subscriptions can now be a bit more precice;
```cmd
C:\Users\Admin>netaudio subscription list --rx-device-name="A32"
01_VO1_AUX_Input@A32 <- VO1 Aux-1@Artist-Artist-64-2-Bay-5
02_VO2_AUX_Input@A32 <- VO2 Aux-1@Artist-Artist-64-2-Bay-5
03_VO3_AUX_Input@A32 <- VO3 Aux-1@Artist-Artist-64-2-Bay-5
04_VO4_AUX_Input@A32 <- VO4 Aux-1@Artist-Artist-64-2-Bay-5
05_VO5_AUX_Input@A32 <- VO5 Aux-1@Artist-Artist-64-2-Bay-5
11 STD3_FB1@A32 <- STD3_FB@Artist-Artist-64-2-Bay-5
12 STD3_FB2@A32 <- STD3_FB@Artist-Artist-64-2-Bay-5
13 STD3_IEM1@A32 <- Port5@Artist-Artist-64-2-Bay-6
14 STD3_IEM2@A32 <- Port6@Artist-Artist-64-2-Bay-6
15 STD3_IEM3@A32 <- Port6@Artist-Artist-64-2-Bay-6
16 STD3_IEM4@A32 <- Port6@Artist-Artist-64-2-Bay-6
17_STD3_Wallbox7@A32 <- STD3Wallbox1-11@A32
18_STD3_Wallbox8@A32 <- STD3Wallbox2-12@A32
25 Studio3_to_Lawo1@A32 <- Mic 01@Studio-3-Mic-1-2
26 Studio3_to_Lawo2@A32 <- Mic 02@Studio-3-Mic-1-2
27 Studio3_to_Lawo3@A32 <- Mic 03@Studio-3-Mic-3-4
28 Studio3_to_Lawo4@A32 <- Mic 04@Studio-3-Mic-3-4
29 Studio3_to_Lawo5@A32 <- STD3Wallbox5-15@A32
30 Studio3_to_Lawo6@A32 <- STD3Wallbox6-16@A32
31 Studio3_to_Lawo7@A32 <- STD3Wallbox7-17@A32
32 Studio3_to_Lawo8@A32 <- STD3Wallbox8-18@A32

C:\Users\Admin>netaudio subscription list --rx-device-name="A32" --rx-channel-name="01_VO1_AUX_Input"
01_VO1_AUX_Input@A32 <- VO1 Aux-1@Artist-Artist-64-2-Bay-5
```



#Normal list of commands unaffected;

```cmd
netaudio device list = list all devices on network
netaudio channel list = list all devices on network with channels showing
netaudio subscription list = list all subscriptions on network, now wil options available '--rx-device-name=' '--rx-channel-name='
netaudio subscription remove = remove a subscription (netaudio subscription remove --rx-channel-name=10 --rx-device-name="A32")
netaudio subscription add = add a subscription (netaudio subscription add --tx-device-name="Artist-Artist-64-2-Bay-5" --tx-channel-name="02" --rx-channel-name="01" --rx-device-name="A32"
```
