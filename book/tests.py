import json

from django.test  import TestCase, Client


from my_settings    import SECRET_KEY

from library.models import Library, Shelf
from users.models   import User, UserType,Subscribe
from book.models    import (
    Book, 
    Review, 
    ReviewLike, 
    Author,
    Publisher,
    Category)

class BookListTest(TestCase):
    def setUp(self):
        client = Client()
        Category.objects.create(id=1, name='일반소설')
        usertype = UserType.objects.create(id=1, name='모바일')
        Subscribe.objects.create(id=1, price=1)
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
            usertype          = usertype,
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
            description      = 'description',
            page             = 1,
            capacity         = 1,
            pub_date         = 900922,
            launched_date    = 900922,
            contents         = 'contents',
            publisher_review = 'publisher_review',
            image_url        = 'image_url',
            purchase_url     = 'purchase_url',
            author           = 1,
            category         = 1,
            publisher        = 1,
            shelf            = 1
        )
    
    def tearDown(self):
        User.objects.all().delete()
        Usertype.objects.all().delete()
        Book.objects.all().delete()
        Publisher.objects.all().delete()
        Subcategory.objects.all().delete()
        Category.objects.all().delete()
        Author.objects.all().delete()
        Library.objects.all().delete()
        Review.objects.all().delete()
        ReviewLike.objects.all().delete()
        Author.objects.all().delete()

    def test_booklist_get_success(self):
        client = Client()
        response = client.get('/book?category_id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'bookData': {
                                              "slider"            : 
                                                                    [{
                                                                    'id'           :idx,
                                                                    'book_id'      :book.id,
                                                                    'bookTitle'    :book.title,
                                                                    'bookCoverImg' :book.image_url,
                                                                    'bookAuthor'   :book.author.name,
                                                                }],
                                              "recent_books"      : 
                                                                    [{
                                                                    'id'           :idx,
                                                                    'book_id'      :book.id,
                                                                    'bookTitle'    :book.title,
                                                                    'bookCoverImg' :book.image_url,
                                                                    'bookAuthor'   :book.author.name,
                                                                }],
                                              "favorite_books"    : 
                                                                    [ {
                                                                    'id'           :idx,
                                                                    'book_id'      :book.id,
                                                                    'bookTitle'    :book.title,
                                                                    'bookCoverImg' :book.image_url,
                                                                    'bookAuthor'   :book.author.name,
                                                                }],
                                              "subcategory_list1" : 
                                                                    [{
                                                                    'id'           :idx,
                                                                    'book_id'      :book.id,
                                                                    'bookTitle'    :book.title,
                                                                    'bookCoverImg' :book.image_url,
                                                                    'bookAuthor'   :book.author.name,
                                                                }],
                                              "subcategory_list2" : 
                                                                    [{
                                                                    'id'           :idx,
                                                                    'book_id'      :book.id,
                                                                    'bookTitle'    :book.title,
                                                                    'bookCoverImg' :book.image_url,
                                                                    'bookAuthor'   :book.author.name,
                                                                }] }})
    def test_booklist_get_fail(self):
        client = Client()
        response = client.get('/book/cateogory_id')
        self.assertEqual(response.status_code, 404)