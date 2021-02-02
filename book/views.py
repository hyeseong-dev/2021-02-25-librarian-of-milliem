import random
import json

from django.http        import JsonResponse
from django.views       import View
from django.db.models   import Q, Count

from book.utils         import validate_value, query_debugger
from book.models        import Book, Author, Publisher, Category, Review, ReviewLike


class CategoryListView(View):
    def get(self, request,category_id):
        try:
            # 메인 페이지, 섹션별 아이템 10개 뿌리기
            # category_id = int(request.GET.get(category_id,1))

            OFFSET = 0 
            LIMIT  = 10

            books = Book.objects.prefetch_related("author", "publisher", )\
                                .filter(category__id=category_id)\
                                .order_by('?')[OFFSET:LIMIT]


            # 슬라이더 부분
            slider = []
            for idx,book in enumerate(books,1):
                    
                    slider.append(
                         {
                            'id'           :idx,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        }
                    )
                

            # 최신 책
            recent_book_list = []
            books = Book.objects.prefetch_related("author", "publisher", )\
                                .filter(category__id=category_id)\
                                .order_by('-pub_date')[OFFSET:LIMIT]

            for idx,book in enumerate(books,1):
                    recent_book_list.append(
                         {
                            'id'           :idx,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        }
                    )
                

            # 가장 좋아하는 책(== 리뷰가 가장 많이 달린 책)
            favorite_books = []
             
            books = Book.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')
            
            for idx,book in enumerate(books,1):
                    favorite_books.append(
                         {
                            'id'           :idx,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        }
                    )
                    

            # 특정한 카테고리에서 랜덤하게 서브카테고리를 정하고 10개 책을 가져옴 - sub_cate1
            sub1 = Book.objects.prefetch_related("author", "publisher", )\
                                .filter(category__id=category_id).order_by('?')[OFFSET:LIMIT]
            sub_list_1 = []
            for idx,book in enumerate(sub1,1):
                    sub_list_1.append(
                         {
                            'id'           :idx,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        }
                    )
                    
            sub2 = Book.objects.prefetch_related("author", "publisher", )\
                               .filter(category__id=category_id)\
                               .order_by('?')[OFFSET:LIMIT]
            sub_list_2 = []
            for idx,book in enumerate(sub2,1):
                    sub_list_2.append(
                         {
                            'id'           :idx,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        }
                    )

            return JsonResponse(
                                {'bookData':[
                                            {"slider"                       : slider},
                                            {"recent_books"                 : recent_book_list},
                                            {"favorite_books"               : favorite_books},
                                            {"sub_category_name1" : sub_list_1},
                                            {"sub_category_name2" : sub_list_2}
                                            ]
                                
                                },
                                status=200)
        
        except Book.DoesNotExist:
            return JsonResponse({'MESSAGE':'BOOK DOES NOT EXISTS!'},status=400)

 
