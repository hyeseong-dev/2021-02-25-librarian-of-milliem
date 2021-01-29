for i in Book.objects.all():
    # i.title =random.choice(seed_info.book_title)
    i.book_sub_title = random.choice(seed_info.book_sub_title)
    i.summary = random.choice(seed_info.book_summary)
    i.publisher_review = random.choice(seed_info.publisher_reviews)
    i.save()

<<<<<<< HEAD

for i in Book.objects.all():
    # i.title =random.choice(seed_info.book_title)
    print(i.book_sub_title)
    print(i.summary)
    print(i.publisher_review)


for i in Book.objects.all():
    # i.title =random.choice(seed_info.book_title)
    print("=" * 30)
    print("서브타이틀", i.sub_title)
    print("섬머리", i.summary)
    print("출판사 리뷰", i.publisher_review)


## 최신 업데이트 OK 8개 데이터
for i in Book.objects.all():
    print("=" * 30)
    print("서브타이틀", i.sub_title)
    print("섬머리", i.summary)
    print("출판사 리뷰", i.publisher_review)

## 카테고리(일반소설, 무협/만화, 로맨스/BL, 만화)별 랜덤하게 20개 데이터 넘기기
for i in Book.objects.prefetch_related("subcategory", "publisher", "series").filter(
    subcategory__category_id=1
).order_by('?'):
    print(i.id)
    print(i.title)
    print(i.sub_title)
    print(i.image_url)

## Most Review book 일주일간 가장 많이 읽힌 책 10개 데이터
for i in Review.objects.prefetch_related("subcategory", "publisher", "series").filter(
    subcategory__category_id=1
):

## 서브카테고리=2 8개 전해주기


## 서브카테고리=3 8개 전해주기


## 일반 소설 추천 작가
#작가이름 : 
#작품 : 


## 서브카테고리=5 8개 전해주기

## 커밍순 놓치기 아쉬운 책 

# 현재일보다 앞선 출시일의 책(pub_date)



# 메인 페이지(story page의 json 데이터 전달 모형도)
{
    "category_id"
    # 20개 각 카테고리별 랜덤하게 전달함
  'slider':{
      'image_url':
      'title':
      'author_name':

  },

 #최신 업데이트 OK 8개 데이터
 'recent_books':{
     'image_url':
     'title':
     'author_name':
 },
 
 # 가장 많이 읽힌 책( 리뷰가 가장 많이 달린책으로 대체함  10개 데이터)

 # subcategory_id=1  ('우리들은 자란다, 2시간으로 그 시절 나를 돌아봐요') 8개
 'sub_cate_1':{
     'image_url':
     'title':
     'author_name':
 },

 # subcategory_id=2  ('3시간 넘도록 독서를 멈출 수 없는 추리 스릴러')
 'sub_cate_2':{
    'image_url':
     'title':
     'author_name':
 },

#  작가, 작품 4개 데이터.(작품이 가장 많은 4명)
#  'author_info':{
#      'author_name':
#      'book_name'
#  }

# 가장 가까운 날로 발매될 책(오늘 기준으로 오름차순 정렬)
    'comming_soon':{
        'image_url':
        'title':
        'author_name':
    }
}
=======
print(seed_info.book_title)hello world
1차 커밋
2차 커밋
16:40 commit
>>>>>>> b7a113262ca6f1cef05d86b14f10c7e329458a9d
