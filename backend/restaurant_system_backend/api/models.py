from django.db import models

class Contact(models.Model):
    """
    Contact entity of a restaurant entity.
    """
    # phone number
    phone = models.CharField(max_length=15)
    # email
    email = models.EmailField()

    def __str__(self):
        """
        The dundle function str overwrited.
        
        Returns:
            str: Contact email.
        """
        return self.email

class Restaurant(models.Model):
    """
    Restaurant entity.
    """
    # restaurant id
    id = models.IntegerField(primary_key=True)
    # restaurant name
    name = models.CharField(max_length=100, null=False, unique=True)
    # restaurant location
    location = models.CharField(max_length=30, null=False)
    # cuisine type
    cuisine = models.CharField(max_length=30)
    # rating from customers
    rating = models.FloatField()
    # conatct of the restaurant
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, related_name='restaurant', null=True, blank=True)

    def __str__(self):
        """
        The dundle function str overwrited.
        
        Returns:
            str: Restaurant name.
        """
        return self.name