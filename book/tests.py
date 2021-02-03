import json

from django.test import TestCase, Client


from my_settings import SECRET_KEY

from user.models import User, UserType,Subscribe
from book.models import (
    Book, 
    Review, 
    ReviewLike, 
    Author,
    Publisher,
    Category)

class BookDetailTest(TestCase):
    def setUpTestData(self):
        client = Client()
        Category.objects.create(id=1, name='일반소설')
        UserType.objects.create(id=1, name='모바일')
        User.objects.create(
            id                = 1, 
            social_id         = "01058974859",
            nickname          = "nickname",
            mobile            = "01058974859",
            password          = "password",
            birth             = 900922,
            gender            = 1,
            email             = "hyeseong43@gmail.com",
            profile_image_url = "profile_image_url",
            library_image_url = "library_image_url",
            usertype          = 1,
            subscribe         = "",
            category          = "1",
            review            = "",
             )
        Author.objects.create(id=1, name='name', description='description', profile_image_url='profile_image_url')
        Publisher.objects.create(id=1, name='name', description='description')
        Library.objects.create(id=1, name='나의서재')
        Shelf.objects.create(id=1, name='나의책장', library=1)
        Book.objects.create(
            id               = '1',
            title            = 'title',
            summary          = 'summary',
            translator       = 'translator',
            sub_title        = 'sub_title',
            description      = 'description     ',
            page             = 400,
            capacity         = 300,
            pub_date         = 210101,
            launched_date    = 210110,
            contents         = 'contents        ',
            publisher_review = 'publisher_review',
            image_url        = 'image_url       ',
            purchase_url     = 'purchase_url    ',
            author           = 1,
            category         = 1,
            publisher        = 1,
            shelf            = 1
        )
    def tearDown(self):
        
