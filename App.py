import jetson.inference
import jetson.utils
from twilio.rest import client
import time

# Defining veriables
receiving_number = input("where would you send to? ")
subj='Person detected!'
date='7/6/23'
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
            try:
                account_sid = 'ACc0d1ff6103e8328835a0dcb1cd7a3fbc'
                auth_token = '0907f6474bc1107becd2dc62f55c7ee8'
                client = client(account_sid, auth_token)
                message = client.messages.create(
                from_='+18446070094',
                body= message_text,
                to='+' + receiving_number
                )
                print(message.sid)
                time(300)
            except:
                print("Sorry, somthing went wrong...") #fallback message
			
 
