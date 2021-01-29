import random
import datetime
import json

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django_seed import Seed

from users.models import *
from book.models import *
from library.models import *

from faker import Faker

from data import seed_info


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", default=1000, type=int, help="몇개 생성 하실거에요?")

    def handle(self, *args, **options):

        number = options.get("number")
        fake = Faker(["ko_KR"])
        seeder = Seed.seeder()

        start_date = datetime.date(1980, 1, 1)
        end_date = datetime.date(2020, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        # seeder.add_entity(
        #     Book,
        #     number,
        #     {
        #         "title": lambda x: random.choice(seed_info.book_title),
        #         "summary": lambda x: random.choice(seed_info.book_summary),
        #         "translator": lambda x: fake.name(),
        #         "sub_title": lambda x: random.choice(seed_info.book_sub_title),
        #         "description": lambda x: random.choice(seed_info.book_summary),
        #         "page": lambda x: random.randint(300, 1000),
        #         "capacity": lambda x: random.randint(25, 1000),
        #         "pub_date": lambda x: fake.date(),
        #         "launched_date": lambda x: fake.date(),
        #         "contents": lambda x: random.choice(seed_info.book_contents),
        #         "publisher_review": lambda x: fake.text(seed_info.publisher_summary),
        #         "image_url": lambda x: random.choice(seed_info.book_image),
        #         "purchase_url": lambda x: fake.,
        #         "author": lambda x: random.choice(seed_info.book_sub_title),
        #         "sub_category": lambda x: Subcategory.objects.all(),
        #         "publisher": lambda x: random.choice(seed_info.book_sub_title),
        #         "series": lambda x: random.choice(Series.objects.all()),
        #         #  'shelf'            : lambda x: fake.name(),
        #     },
        # )
        # Author
        # seeder.add_entity(
        #     Author,
        #     number,
        #     {
        #         "name": lambda x: fake.name(),
        #         "'description'": lambda x: random.choice(seed_info.author_desc),
        #         "profile_image_url": lambda x: random.choice(seed_info.profile_images),
        #     },
        # )

        # Publisher 30개 작성 완료 !
        # seeder.add_entity(
        #     Publisher,
        #     number,
        #     {
        #         "name": lambda x: fake.company(),
        #         "description": lambda x: random.choice(seed_info.publisher_summary),
        #     },
        # )

        #         # # Subcategory ! 이미 40개 작성 완료
        #         # seeder.add_entity(
        #         #     Subcategory,
        #         #     number,
        #         #     {
        #         #         "name": lambda x: fake.name(),
        #         #         "description": lambda x: fake.text(),
        #         #     },
        #         # )

        #         # #Category # 이미 디비 4개 있음!
        #         # seeder.add_entity(
        #         #     Category,
        #         #     number,
        #         #     {
        #         #         "name": lambda x: fake.name(),
        #         #         "description": lambda x: fake.text(),
        #         #     },
        #         # )

        #         # # Review # 관계 작성 필요
        #         # seeder.add_entity(
        #         #     Author,
        #         #     number,
        #         #     {
        #         #         "name": lambda x: fake.name(),
        #         #         "description": lambda x: fake.text(),
        #         #     },
        #         # )

        #         # # ReviewLike
        #         # seeder.add_entity(
        #         #     Author,
        #         #     number,
        #         #     {
        #         #         "name": lambda x: fake.name(),
        #         #         "description": lambda x: fake.text(),
        #         #     },
        #         # )

        #         # seeder.add_entity(
        #         #     Author,
        #         #     number,
        #         #     {
        #         #         "name": lambda x: fake.name(),
        #         #         "description": lambda x: fake.text(),
        #         #     },
        #         # )

        # UserType 완료!
        # seeder.add_entity(
        #     UserType,
        #     number,
        #     {
        #         "name": lambda x:for x in ["카카오톡", "구글", "모바일"],
        #     },
        # )

        # Library 완료!
        seeder.add_entity(
            Library,
            number,
            {"name": lambda x: fake.word()},
        )

        # User

        # seeder.add_entity(
        #     User,
        #     number,
        #     {
        #         # social_id         =
        #         "nickname": lambda x: fake.name(),
        #         "mobile": lambda x: fake.phone_number(),
        #         "password": lambda x: fake.password(),
        #         "birth": lambda x: random.choice([i for i in range(900920, 900950)]),
        #         "gender": lambda x: random.choice([1, 2]),
        #         "email": lambda x: fake.ascii_free_email(),
        #         "profile_image_url": lambda x: random.choice(seed_info.profile_images),
        #         # 'library_image_url' : lambda x: "https://images.unsplash.com/photo-1507842217343-583bb7270b66"
        #         "usertype": lambda x: UserType.objects.filter(),
        #         # 'subscribe'         :
        #         # 'review'            :
        #         "library": lambda x: Library.objects.filter(),
        #     },
        # )

        seeder.execute()
        self.stdout.write(
            self.style.SUCCESS("Successfully Finished to Create Model's Data")
        )
