![image Alt text](https://camo.githubusercontent.com/dd07bdb5f1d850f43898037ed8f72e1d53af03841b08cabf09303f5902c3509f/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67)

# AirBnB_Clone , The Console 💻

AirBnB clone is the first phase of creating a complete web application cloning the real AirBnB website


### Project Description 📣

This pojects involves handling the backend of the web application by:
* Creating the main objects including all the attributes and methods
* Creating a command line interpreter that can handle and manage all objects operations                                              

### CLI Description 🔧

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

### Class Diagram 🔩

![image Alt text](https://camo.githubusercontent.com/eb174d0a8e35b695634e3ac3eb61f686a1e1e020b3c55aceac60bc9d92a34699/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f45526a5644316b585941455f554f2d3f666f726d61743d6a7067266e616d653d6d656469756d)
    
### Example 👀

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
### Contributers 👷

* Nour Eldean Mohamed <nour98nour@gmail.com>
* Mohamed Raafat <mraafat.elsayed@gmail.com>
