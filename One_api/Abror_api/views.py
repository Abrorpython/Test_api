from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article,Author
from .serializers import ArticleSerializer,AuthorSerializer
from django.shortcuts import get_object_or_404

class ArticleView(APIView):

    def get(self,request,article_id=None):
        if article_id:
            article = Article.objects.get(pk=article_id)
            serializers = ArticleSerializer(article, many=False)
        else:
            articles = Article.objects.all()
            serializers = ArticleSerializer(articles,many=True)

        return Response(serializers.data)

    def post(self,request):
        article = request.data
        serialzer = ArticleSerializer(data=article)
        if serialzer.is_valid(raise_exception=True):
            article_saved = serialzer.save()
        return Response({"success": "Article '{}' created succesfuly".format(article_saved.title)})

    def put(self,request,article_id):
        saved_article = get_object_or_404(Article.objects.all(),pk=article_id)
        data = request.data
        serializer = ArticleSerializer(instance=saved_article,data=data,partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved= serializer.save()
        return Response({"success":"Article '{}' updated successfully".format(article_saved.title)})

class AuthorView(APIView):

    def get(self,request,id=None):
        if id:
            a = Author.objects.get(pk=id)
            b = AuthorSerializer(a,many=False)
        else:
            a = Author.objects.all()
            b = AuthorSerializer(a,many=True)
            return Response(b.data)

    def post(self,request):
        a = request.data
        b = AuthorSerializer(data=a)
        if b.is_valid(raise_exception=True):
            c = b.save()
        return Response(f"success: Author {c.name} created succesfuly")
    def put(self,request,id):
        aOne = get_object_or_404(Author.objects.all(),pk=id)
        data = request.data
        seri = AuthorSerializer(instance=aOne,data = data,partial=True)
        if seri.is_valid(raise_exception=True):
            d = seri.save()
            return Response(f" succes: Author {d.name} created succesfuly")
