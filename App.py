import jetson.inference
import jetson.utils
from twilio.rest import Client
import time

# Defining veriables
receiving_number = input("where would you send to? ")
subj='Person detected!'
date='7/7/23'
message_text='Alert! there has been someone snooping around, you should check on this...'
print("message setup complete!\nstarting detectmodel...")

# Start detectnet model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0") # 'csi://0' for MIPI CSI camera
display = jetson.utils.videoOutput("display://0")     # 'my_video.mp4' for file

# Show live cam feed
while display.IsStreaming():
    img = camera.Capture()
    detections = net.Detect(img)
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

    for detection in detections:
        class_name = "reset" # Resets veriable to prevent false alarms
        class_name = net.GetClassDesc(detection.ClassID)
        print(f"Detected '{class_name}'")
        if (class_name == "person"):
            print("Person detected!")
            try: #this is to send the message
                account_sid = 'ACc0d1ff6103e8328835a0dcb1cd7a3fbc' 
                auth_token = '[AuthToken]' #Go to twilio and get your auth_token
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                from_='+18446070094',
                body= message_text,
                to= '+1' + receiving_number
                )
                print(message.sid)
                time.sleep(300)
            except:
                print("Sorry, somthing went wrong...") #fallback message
			
