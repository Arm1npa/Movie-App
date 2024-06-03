import { createContext, useEffect, useState } from "react";
import axios from "axios";

export const MovieContext = createContext({});

export const MovieContextProvider = ({ children }) => {
  const [trendings, setTrendings] = useState([]);
  const [movies, setMovies] = useState([]);
  const [tvShows, setTvShows] = useState([]);
  const [movieGenres, setMovieGenres] = useState([]);
  const [tvGenres, setTvGenres] = useState([]);
  const [trendingTotalPages, setTrendingTotalPages] = useState();
  const [latestTotalPages, setLatestTotalPages] = useState();
  const [tvTotalPages, setTvTotalPages] = useState();
  const [currentPage, setCurrentPage] = useState(1);
  const [movieSearchResults, setMovieSearchResults] = useState([]);
  const [query, setQuery] = useState("");
  const [searchResultsTotalPages, setSearchResultsTotalPages] = useState();

  const fetchTrendings = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/trending-movies/?page=${currentPage}`
      );
      const movies = response.data;

      // Ensure the data structure is correct
      if (Array.isArray(movies.results)) {
        setTrendings(movies.results);
        setTrendingTotalPages(250);
      } else {
        console.error("Invalid data structure", movies);
      }
    } catch (error) {
      console.error("Failed to fetch trending movies", error);
    }
  };

  const fetchLatest = async () => {
    try {
      const { data: movies } = await axios.get(
        `http://localhost:8000/api/latest-movies/?page=${currentPage}`
      );
      setMovies(movies.results);
      setLatestTotalPages(300);
    } catch (error) {
      console.error("Failed to fetch latest movies", error);
    }
  };

  const fetchMovieGenres = async () => {
    try {
      const { data } = await axios.get(
        `http://localhost:8000/api/movie-genres/?page=${currentPage}`
      );
      setMovieGenres(data);
    } catch (error) {
      console.error("Failed to fetch movie genres", error);
    }
  };

  const fetchTvGenres = async () => {
    try {
      const { data } = await axios.get(
        `http://localhost:8000/api/tv-genres/?page=${currentPage}`
      );
      setTvGenres(data);
    } catch (error) {
      console.error("Failed to fetch TV genres", error);
    }
  };

  const fetchTvShows = async () => {
    try {
      const { data } = await axios.get(
        `http://localhost:8000/api/tvshows?page=${currentPage}`
      );
      setTvShows(data.results);
      setTvTotalPages(data.total_pages);
    } catch (error) {
      console.error("Failed to fetch TV shows", error);
    }
  };

  const SearchMovies = async () => {
    if (!query) return;
    try {
      const { data } = await axios.get(
        `http://localhost:8000/api/movies/search?query=${query}&page=${currentPage}`
      );
      setMovieSearchResults(data.results);
      setSearchResultsTotalPages(data.total_pages);
    } catch (error) {
      console.error("Failed to search movies", error);
    }
  };

  useEffect(() => {
    fetchTrendings();
    fetchLatest();
    fetchMovieGenres();
    fetchTvShows();
    fetchTvGenres();
    SearchMovies();
  }, [currentPage]);

  const handleGenres = async (id) => {
    setMovieGenres(
      movieGenres.map((genre) =>
        genre.id === id
          ? { ...genre, active: !genre.active }
          : { ...genre, active: false }
      )
    );

    try {
      const { data } = await axios.get(
        `http://localhost:8000/api/movies/genres/${id}?page=${currentPage}`
      );
      setMovies(data.results);
    } catch (error) {
      console.error("Failed to fetch movies by genre", error);
    }
  };

  const handleTvGenres = async (id) => {
    setTvGenres(
      tvGenres.map((genre) =>
        genre.id === id
          ? { ...genre, active: !genre.active }
          : { ...genre, active: false }
      )
    );

    try {
      const { data } = await axios.get(
        `http://localhost:8000/api/tvshows/genres/${id}?page=${currentPage}`
      );
      setTvShows(data.results);
    } catch (error) {
      console.error("Failed to fetch TV shows by genre", error);
    }
  };

  return (
    <MovieContext.Provider
      value={{
        trendings,
        movies,
        movieGenres,
        tvShows,
        tvGenres,
        handleGenres,
        handleTvGenres,
        setMovies,
        trendingTotalPages,
        currentPage,
        setCurrentPage,
        setLatestTotalPages,
        latestTotalPages,
        tvTotalPages,
        searchResultsTotalPages,
        setQuery,
        SearchMovies,
        movieSearchResults,
        query,
      }}
    >
      {children}
    </MovieContext.Provider>
  );
};
