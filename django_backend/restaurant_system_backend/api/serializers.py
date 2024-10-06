from rest_framework import serializers
from .models import Restaurant, Contact

class ContactSerializer(serializers.ModelSerializer):
    """Serializer of the contact model

    Args:
        serializers (serializers.ModelSerializer): Basic model serializer.
    """
    class Meta:
        # related model
        model = Contact
        # related fields of the model
        fields = ['phone', 'email']

class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer of the restaurant model

    Args:
        serializers (serializers.ModelSerializer): Basic model serializer.
    """

    # contact serializer
    contact = ContactSerializer()

    class Meta:
        # related model
        model = Restaurant
        # related fields of the model
        fields = ['id', 'name', 'location', 'cuisine', 'rating', 'contact']

    def create(self, validated_data):
        """Overwrited create function to execute when a instance is to be created.

        Args:
            validated_data (Restaurant): Instance to be created.

        Returns:
            Restaurant: Instance to be created.
        """
        # create a contact record
        contact_data = validated_data.pop('contact')
        contact = Contact.objects.create(**contact_data)

        # create the restaurant record
        restaurant = Restaurant.objects.create(contact=contact, **validated_data)

        # return the restaurant record
        return restaurant

    def update(self, instance, validated_data):
        """Overwrited create function to execute when a instance is to be updated.

        Args:
            instance (Restaurant): Old instance to be updated by.
            validated_data (Restaurant): New instance to be updated.

        Returns:
            Restaurant: New instance to be updated.
        """
        # get the contact instance
        contact_data = validated_data.pop('contact')
        contact = instance.contact

        # update the old instance values to the new instance values
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.cuisine = validated_data.get('cuisine', instance.cuisine)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()

        # contact: update the old instance values to the new instance values
        contact.phone = contact_data.get('phone', contact.phone)
        contact.email = contact_data.get('email', contact.email)
        contact.save()

        # return the restaurant record
        return instance
    
class RestaurantNameSerializer(serializers.ModelSerializer):
    """Serializer of the restaurant model that only relates its name.

    Args:
        serializers (Restaurant): Basic model serializer.
    """
    class Meta:
        # related model
        model = Restaurant
        # related fields of the model
        fields = ['name']
