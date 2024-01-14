![image Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240114%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240114T080250Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ec4d765f24f5eef4a103030f20f68373cd8e0fc86c259721e58759cb723190f3)

# AirBnB_Clone , The Console

AirBnB clone is the first phase of creating a complete web application cloning the real AirBnB website


### Project Description
This pojects involves handling the backend of the web application by:
* Creating the main objects including all the attributes and methods
* Creating a command line interpreter that can handle and manage all objects operations                                              
### CLI Description

* How to start :
    ```bash
    python3 console.py
    ```
* How to use:
    Simply by printing the built-in commands to manage the objects
    ```bash
    (hbnb) create BasModel
    123
    (hbnb) show BaseModel 123
    [BaseModel] (123) {attributes dictionary}
    (hbnb) destroy BaseModel 123
    ```
* Available commands:
    
    ```bash
    1- quit #quit the console
    2- EOF #quit the console
    3- all #print all objects available
    4- create <object_class> #create object
    5- show <object_class> <object_id> OR object_class.show("<object_id>") #show object data
    6- destroy <object_class> <object_id> OR object_class.destroy("<object_id>") #delete object
    7- update <object_class> <object_id> <new_attr_name> <attr_value> #update object
    8- object_class.update("<object_id>", "new_attr", "new_value") #update object
    9- object_class.update("<object_id>", "{attributes_dictionary}") #update object
    
### Example

```bash
(hbnb) create BaseModel
1a90d9fd-dbcd-4da4-8c16-5576ddc3b0ab
(hbnb) create User
4b119721-8e5e-4091-b1bc-1716b5f96ec2
(hbnb) show User 4b119721-8e5e-4091-b1bc-1716b5f96ec2
[User] (4b119721-8e5e-4091-b1bc-1716b5f96ec2) {'id': '4b119721-8e5e-4091-b1bc-1716b5f96ec2', ... }
(hbnb) destroy User 4b119721-8e5e-4091-b1bc-1716b5f96ec2
(hbnb) show User 4b119721-8e5e-4091-b1bc-1716b5f96ec2
** no instance found **
```
### Contributers

* Nour Eldean Mohamed <nour98nour@gmail.com>
* Mohamed Raafat <mraafat.elsayed@gmail.com>
