# practise-project
#####flask-lab resfulAPI


pip install -r requirements.txt


gunicorn -w 4 -b 127.0.0.1:5000 my_app:app


ML model for mnist using postman to post

http://127.0.0.1:5000/mnist

with json body
  {
	"base64_image":"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/wAALCAAcABwBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/AP5/6/S7/gmR/wAGx/7Wn7ePwuP7Rnxw8f2fwM+GcunG+03xH4r0V7i71C08kTLeRWjzW4FoYyGFxJKisvzKHXmvCf2pP+CJX/BQP9mnwd4s+O8fwJ1vxL8IPD2q3Cab8UNLhhNrq2lrKwg1ZLdJpJ47SaLZKJipiCyA+YRhj8j0+3aBJQ1zEzpg5VH2k8cc4Pf2r+ln4L/CvT/+DhX/AIIefBn4J/swftZ6/wDCrWPhPHovhb4i6SjSNDdmxsobSaO5jhZGnR4FF3bjf5ZZgkgDAtF4H/wcQ/8ABUbxL+w38C7D/ghP+zNaeK4rfQPBGmaP44+I3iuUTza1pMlgM2NsZVbejxyRiSZCoTa0EaqFNfg/Wt4D0rQNd8c6LonizVjYaVeatbQalfBwv2a3eVVkkywIG1STkgjiv6wv2oP2Df2gvhV+xv4B/Zq/4JJftW/DH9nL4F6XpQ1Dxn8TrrUZW1i7DNFJFdQXSIIXWb78tw08bSb1RSI/lb8wv+Dnr/goL+xb+0R8A/hB+y38NPjLoHxo+LngOWBvGfxi8O6bHFbSolm8M8KSxl0f7ROy3DRRSPHEYwMknA/GSiiiiv/Z"
  }

mongoDB Create
post http://127.0.0.1:5000/employee
with json body
{
	"key":8,
	"name":"UlllU",
	"age":99,
	"birthDate":"2012/01/09"
}

mongoDB Read
get http://127.0.0.1:5000/findAll

mongoDB Update
post http://127.0.0.1:5000/update
{
	"key":4,
	"age":28	
}
mongoDB Delete
post http://127.0.0.1:4000/delete

mongoDB Helthcheck and log
get http://127.0.0.1:5000/healthCheck


