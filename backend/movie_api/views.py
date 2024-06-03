import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dotenv import load_dotenv
import os

load_dotenv()


@api_view(['GET'])
def get_trending_movies(request):
    api_key = os.getenv('API_KEY')
    if not api_key:
        return Response({"error": "API Key is missing"}, status=400)

    base_url = "https://api.themoviedb.org/3/trending/movie/week"
    page = request.GET.get('page', 1)  # دریافت شماره صفحه از درخواست
    url = f"{base_url}?api_key={api_key}&language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{api_key}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        trending_movies = []
        for movie in data['results']:
            trending_movies.append({
                'id': movie['id'],
                'title': movie['title'],
                'rating': f"{movie['vote_average']:.1f}",
                'overview': movie.get('overview', ''),
                'release_date': movie.get('release_date', ''),
                'poster_path': movie.get('poster_path', ''),
                'backdrop_path': movie.get('backdrop_path', ''),
            })
        return Response({
            "results": trending_movies,
            "total_pages": data.get('total_pages', 1),
            "page": data.get('page', 1)
        })
    else:
        return Response({"error": "Failed to fetch data from API"}, status=response.status_code)


@api_view(['GET'])
def get_tv_shows(request):
    api_key = os.getenv('API_KEY')
    page = request.GET.get('page', 1)  # دریافت شماره صفحه از درخواست
    base_url = "https://api.themoviedb.org/3/discover/tv"
    url = f"{base_url}?include_adult=false&include_video=false&language=en-US&page={
        page}&sort_by=popularity.desc&api_key={api_key}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{api_key}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return Response({
            "results": data.get('results', []),
            "total_pages": data.get('total_pages', 1),
            "page": data.get('page', 1)
        })
    else:
        return Response({"error": "Failed to fetch data from API"}, status=response.status_code)


@api_view(['GET'])
def get_latest_movies(request):
    api_key = os.getenv('API_KEY')
    page = request.GET.get('page', 1)  # دریافت شماره صفحه از درخواست
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={
        api_key}&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{api_key}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        movies = data.get('results', [])
        return Response({
            "results": movies,
            "total_pages": data.get('total_pages', 1),
            "page": data.get('page', 1)
        })
    else:
        return Response({"error": "Failed to fetch latest movies"}, status=response.status_code)


@api_view(['GET'])
def get_tv_genres(request):
    api_key = os.getenv('API_KEY')
    url = f"https://api.themoviedb.org/3/genre/tv/list?api_key={api_key}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{api_key}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        genres = data.get('genres', [])
        return Response(genres)
    else:
        return Response({"error": "Failed to fetch TV genres"}, status=response.status_code)


@api_view(['GET'])
def get_tv_series_by_genre(request, genre_id):
    api_key = os.getenv('API_KEY')
    page = request.GET.get('page', 1)  # Get page number from request
    base_url = "https://api.themoviedb.org/3/discover/tv"
    url = f"{base_url}?api_key={api_key}&with_genres={genre_id}&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{api_key}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return Response({
            "results": data.get('results', []),
            "total_pages": data.get('total_pages', 1),
            "page": data.get('page', 1)
        })
    else:
        return Response({"error": "Failed to fetch TV series by genre"}, status=response.status_code)


@api_view(['GET'])
def get_movie_genres(request):
    api_key = os.getenv('API_KEY')
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{api_key}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        genres = data.get('genres', [])
        return Response(genres)
    else:
        return Response({"error": "Failed to fetch movie genres"}, status=response.status_code)


@api_view(['GET'])
def get_movies_by_genre(request, genre_id):
    api_key = os.getenv('API_KEY')
    page = request.GET.get('page', 1)  # دریافت شماره صفحه از درخواست
    base_url = "https://api.themoviedb.org/3/discover/movie"
    url = f"{base_url}?api_key={api_key}&with_genres={genre_id}&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": f"{api_key}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return Response({
            "results": data.get('results', []),
            "total_pages": data.get('total_pages', 1),
            "page": data.get('page', 1)
        })
    else:
        return Response({"error": "Failed to fetch movies by genre"}, status=response.status_code)


@api_view(['GET'])
def fetch_movie_data(request, movie_id):
    api_key = os.getenv("API_KEY")
    base_url = 'https://api.themoviedb.org/3/movie'

    headers = {
        'Authorization': f'{api_key}',
        'Content-Type': 'application/json;charset=utf-8'
    }

    # Fetch movie details
    movie_details_url = f'{base_url}/{movie_id}'
    movie_details_response = requests.get(movie_details_url, headers=headers)
    if movie_details_response.status_code != 200:
        return Response({'error': 'Failed to fetch movie details'}, status=movie_details_response.status_code)
    movie_details = movie_details_response.json()

    # Fetch movie cast
    movie_cast_url = f'{base_url}/{movie_id}/credits'
    movie_cast_response = requests.get(movie_cast_url, headers=headers)
    if movie_cast_response.status_code != 200:
        return Response({'error': 'Failed to fetch movie cast'}, status=movie_cast_response.status_code)
    movie_cast = movie_cast_response.json().get('cast', [])

    # Fetch movie video ID
    movie_videos_url = f'{base_url}/{movie_id}/videos'
    movie_videos_response = requests.get(movie_videos_url, headers=headers)
    if movie_videos_response.status_code != 200:
        return Response({'error': 'Failed to fetch movie video ID'}, status=movie_videos_response.status_code)
    movie_videos = movie_videos_response.json().get('results', [])
    movie_video_id = movie_videos[0].get('key') if movie_videos else None

    data = {
        'details': movie_details,
        'cast': movie_cast,
        'video_id': movie_video_id,
    }

    return Response(data)


@api_view(['GET'])
def fetch_tv_show_data(request, tv_show_id):
    api_key = os.getenv("API_KEY")
    base_url = 'https://api.themoviedb.org/3/tv'

    headers = {
        'Authorization': f'{api_key}',
        'Content-Type': 'application/json;charset=utf-8'
    }

    # Fetch TV show details
    tv_show_details_url = f'{base_url}/{tv_show_id}'
    tv_show_details_response = requests.get(
        tv_show_details_url, headers=headers)
    if tv_show_details_response.status_code != 200:
        return Response({'error': 'Failed to fetch TV show details'}, status=tv_show_details_response.status_code)
    tv_show_details = tv_show_details_response.json()

    # Fetch TV show cast
    tv_show_cast_url = f'{base_url}/{tv_show_id}/credits'
    tv_show_cast_response = requests.get(tv_show_cast_url, headers=headers)
    if tv_show_cast_response.status_code != 200:
        return Response({'error': 'Failed to fetch TV show cast'}, status=tv_show_cast_response.status_code)
    tv_show_cast = tv_show_cast_response.json().get('cast', [])

    # Fetch TV show video ID
    tv_show_videos_url = f'{base_url}/{tv_show_id}/videos'
    tv_show_videos_response = requests.get(tv_show_videos_url, headers=headers)
    if tv_show_videos_response.status_code != 200:
        return Response({'error': 'Failed to fetch TV show video ID'}, status=tv_show_videos_response.status_code)
    tv_show_videos = tv_show_videos_response.json().get('results', [])
    tv_show_video_id = tv_show_videos[0].get('key') if tv_show_videos else None

    data = {
        'details': tv_show_details,
        'cast': tv_show_cast,
        'video_id': tv_show_video_id,
    }

    return Response(data)


@api_view(['GET'])
def search_movies(request):
    query = request.GET.get('query')
    page = request.GET.get('page', 1)  # Default to page 1 if not provided
    if not query:
        return Response({'error': 'Query parameter is required'}, status=400)

    api_key = os.getenv("API_KEY")
    base_url = 'https://api.themoviedb.org/3/search/movie'

    headers = {
        'Authorization': f'{api_key}',
        'Content-Type': 'application/json;charset=utf-8'
    }

    params = {
        'query': query,
        'page': page,
    }

    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code != 200:
        return Response({'error': 'Failed to fetch movies'}, status=response.status_code)

    data = response.json()
    return Response({
        'results': data.get('results', []),
        'total_pages': data.get('total_pages', 1)
    })
