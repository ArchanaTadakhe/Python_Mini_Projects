import qrcode

# Taking input from user

upi_id= input("Enter your upi id = ")

#Payemt URL making
#upi://pay?pa=UPI_ID&apn=Name$am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and payemnt app
#u can update URL's based on payment app u want to support

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url) #create function to create url
paytm_qr = qrcode.make(paytm_url) #create function to create url
google_pay_qr = qrcode.make(google_pay_url) #create function to create url

#save QR code

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#dispaly QE code u need to install PIL/Pillow library
phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()
