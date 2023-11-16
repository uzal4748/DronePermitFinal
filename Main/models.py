from django.db import models
#from Authentication.models import User

class Owner(models.Model):
    #oid = models.ForeignKey(User, on_delete= models.CASCADE, default='user',primary_key=True)
    fname = models.CharField(max_length=30,verbose_name="First Name")
    lname = models.CharField(max_length=30,verbose_name="Last Name")
    email = models.EmailField(max_length=254,unique=True,verbose_name="Email")
    tele_no = models.CharField(max_length=10, unique=True,verbose_name="Phone No.")
    pilot_fname = models.CharField(max_length=30,verbose_name="Pilot First Name")
    pilot_lname = models.CharField(max_length=30,verbose_name="Pilot Last Name")
    pilot_email = models.EmailField(max_length=254,verbose_name="Pilot Email")
    pilot_tele_no = models.CharField(max_length=10,verbose_name="Pilot Phone No.")

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname) 

class Drone(models.Model):
    CATEGORIES = [
        ("A","A"),("B","B"),("C","C"),("D","D"),
    ]

    TYPES = [
        ('1',"Multi-Rotor"),('2',"Fixed-Wing"),('3',"Single-Rotor"),('4',"Fixed-Wing Hybrid VTOL"),
    ]
    owners = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='drones', db_column='owners_id', null=True)
    modelno = models.CharField(max_length=30, null=False, blank=False,verbose_name="Model No.")
    category = models.CharField(max_length=1,choices=CATEGORIES,verbose_name="Category")
    types = models.CharField(max_length=10,choices=TYPES,verbose_name="Type")
    weight = models.DecimalField(max_digits=4, decimal_places=2,verbose_name="Weight")
    max_takeoff = models.CharField(max_length=30, null = False , blank = False,verbose_name="Maximum TakeOff")
    manufacturer = models.CharField(max_length=100, verbose_name="Manufacturer Name")
    reg_id = models.CharField(max_length=10, unique=True, null = True, blank = False, verbose_name="Drone Registration No.")

    def __str__ (self):
        return self.modelno
    
class Area(models.Model):
    DISTRICTS = [
        ('Achham', 'Achham'), ('Arghakhanchi', 'Arghakhanchi'), ('Baglung', 'Baglung'), ('Baitadi', 'Baitadi'), ('Bajhang', 'Bajhang'),
        ('Bajura', 'Bajura'), ('Banke', 'Banke'), ('Bara', 'Bara'), ('Bardiya', 'Bardiya'), ('Bhaktapur', 'Bhaktapur'),
        ('Bhojpur', 'Bhojpur'), ('Chitwan', 'Chitwan'), ('Dadeldhura', 'Dadeldhura'), ('Dailekh', 'Dailekh'), ('Dang', 'Dang'),
        ('Darchula', 'Darchula'), ('Dhading', 'Dhading'), ('Dhankuta', 'Dhankuta'), ('Dhanusa', 'Dhanusa'), ('Dolakha', 'Dolakha'),
        ('Dolpa', 'Dolpa'), ('Doti', 'Doti'), ('Eastern Rukum', 'Eastern Rukum'), ('Gorkha', 'Gorkha'), ('Gulmi', 'Gulmi'),
        ('Humla', 'Humla'), ('Ilam', 'Ilam'), ('Jajarkot', 'Jajarkot'), ('Jhapa', 'Jhapa'), ('Jumla', 'Jumla'),
        ('Kailali', 'Kailali'), ('Kalikot', 'Kalikot'), ('Kanchanpur', 'Kanchanpur'), ('Kapilvastu', 'Kapilvastu'), ('Kaski', 'Kaski'),
        ('Kathmandu', 'Kathmandu'), ('Kavrepalanchok', 'Kavrepalanchok'), ('Khotang', 'Khotang'), ('Lalitpur', 'Lalitpur'), ('Lamjung', 'Lamjung'),
        ('Mahottari', 'Mahottari'), ('Makwanpur', 'Makwanpur'), ('Manang', 'Manang'), ('Morang', 'Morang'), ('Mugu', 'Mugu'),
        ('Mustang', 'Mustang'), ('Myagdi', 'Myagdi'), ('Nawalpur', 'Nawalpur'), ('Nuwakot', 'Nuwakot'), ('Okhaldhunga', 'Okhaldhunga'),
        ('Palpa', 'Palpa'), ('Panchthar', 'Panchthar'), ('Parbat', 'Parbat'), ('Parsa', 'Parsa'), ('Pyuthan', 'Pyuthan'),
        ('Ramechhap', 'Ramechhap'), ('Rasuwa', 'Rasuwa'), ('Rautahat', 'Rautahat'), ('Rolpa', 'Rolpa'), ('Rukum West', 'Rukum West'),
        ('Rupandehi', 'Rupandehi'), ('Salyan', 'Salyan'), ('Sankhuwasabha', 'Sankhuwasabha'), ('Saptari', 'Saptari'), ('Sarlahi', 'Sarlahi'),
        ('Sindhuli', 'Sindhuli'), ('Sindhupalchok', 'Sindhupalchok'), ('Siraha', 'Siraha'), ('Solukhumbu', 'Solukhumbu'), ('Sunsari', 'Sunsari'),
        ('Surkhet', 'Surkhet'), ('Syangja', 'Syangja'), ('Tanahun', 'Tanahun'), ('Taplejung', 'Taplejung'), ('Terhathum', 'Terhathum'),
        ('Udayapur', 'Udayapur'), ('Western Rukum', 'Western Rukum')
    ]

    district = models.CharField(max_length = 255, choices = DISTRICTS,verbose_name="District")
    municipality = models.CharField(max_length=255,verbose_name="Municipality")
    wardno = models.PositiveIntegerField(null=True,verbose_name="Ward No.")
    areainsqm = models.CharField(max_length=10, null=False, blank=False, verbose_name="Area in Square Meter")

    def __str__(self):
        return self.municipality
    
class DronePermit(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, related_name= "drone_permits")
    drone = models.ForeignKey(Drone,on_delete=models.SET_NULL,null=True, related_name="owner")
    area = models.ForeignKey(Area,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    purpose = models.CharField(max_length=255,verbose_name="Purpose of Flight")
    status = models.CharField(max_length=10, choices = STATUS, default='pending')

    def __str__(self):
        return str(self.owner) + '--'+ str(self.drone)