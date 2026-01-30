import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('imagea1.jpg','Abhay Raj Gupta'),
      ('imagea2.jpg','Abhay Raj Gupta'),
      ('imagea3.jpg','Abhay Raj Gupta'),
      ('imagea4.jpg','Abhay Raj Gupta'),
      ('imagea5.jpg','Abhay Raj Gupta'),
      ('imagea6.jpg','Abhay Raj Gupta'),
      ('imaged1.jpg','Devesh Chauhan'),
      ('imaged2.jpg','Devesh Chauhan'),
      ('imaged3.jpg','Devesh Chauhan'),
      ('imaged4.jpg','Devesh Chauhan'),
      ('imaged5.jpg','Devesh Chauhan'),
      ('imaged6.jpg','Devesh Chauhan'),
      ('imagek1.jpg','Kush Patal'),
      ('imagek2.jpg','Kush Patal'),
      ('imagek3.jpg','Kush Patal'),
      ('imagek4.jpg','Kush Patal'),
      ('imagek5.jpg','Kush Patal'),
      ('imagek6.jpg','Kush Patal'),
      
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('student-smvdu','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
