import { FilmIcon } from "@heroicons/react/24/outline";
import React, { useContext, useEffect, useState } from "react";
import { Col, Container, Row } from "react-bootstrap";
import { Genre } from "../components/Genre";
import NavComp from "../components/Navbar";
import { useParams } from "react-router-dom";
import axios from "axios";
import { LazyLoadImage } from "react-lazy-load-image-component";
import { VideoPlayerModal } from "../components/VideoPlayerModal";
import { MovieContext } from "../context/MovieContext";

const IMAGE_UNAVAILABLE_PLACEHOLDER =
  "https://via.placeholder.com/350x500?text=Image+Unavailable";

export default function ShowInfo() {
  const { isTvShow } = useContext(MovieContext);
  const [modalShow, setModalShow] = useState(false);
  const [movieInfo, setMovieInfo] = useState();
  const [movieCast, setMovieCast] = useState([]);
  const [movieVideoId, setMovieVideoId] = useState("");
  const params = useParams();
  const { id: movieId } = params;

  const fetchMovieDetails = async () => {
    try {
      const { data } = await axios.get(
        `http://127.0.0.1:8000/api/tv-show/${movieId}/`
      );
      setMovieInfo(data.details);
      setMovieCast(data.cast);
      setMovieVideoId(data.video_id);
    } catch (error) {
      console.error("Failed to fetch movie details", error);
    }
  };

  useEffect(() => {
    fetchMovieDetails();
  }, [movieId]);

  return (
    <>
      <NavComp />
      <Container>
        <div className="wrapper mt-4">
          <div id="movie-info" className="d-flex gap-5">
            <img
              style={{
                borderRadius: 5,
                boxShadow: "rgb(46 255 14 / 10%) -1px -1px 57px 1px",
                width: 350,
                height: 500,
                objectFit: "cover",
              }}
              src={
                movieInfo?.backdrop_path
                  ? `http://image.tmdb.org/t/p/w500${movieInfo.backdrop_path}`
                  : IMAGE_UNAVAILABLE_PLACEHOLDER
              }
              alt="movie thumbnail"
            />
            <div className="mt-5">
              <h3 style={{ fontSize: 33, color: "white" }}>
                {movieInfo?.title}
              </h3>
              <div className="d-flex gap-2 mt-3">
                {movieInfo?.genres?.map((genre) => (
                  <Genre key={genre.id} name={genre.name} />
                ))}
              </div>
              <p style={{ color: "#a5a5a5", marginTop: 15, lineHeight: 1.8 }}>
                {movieInfo?.overview}
              </p>
              <p style={{ color: "#a5a5a5", fontWeight: "bold" }}>
                Release Date: {movieInfo?.first_air_date}
              </p>
              <button
                onClick={() => setModalShow(true)}
                style={{
                  background: "#00CE79",
                  border: "none",
                  color: "black",
                  fontSize: 18,
                  fontWeight: 500,
                  marginTop: 12,
                  display: "flex",
                  alignItems: "center",
                  gap: 5,
                }}
                className="btn btn-primary"
              >
                <FilmIcon style={{ width: 20, height: 20 }} />
                Play Trailer
              </button>
            </div>
          </div>
          <div className="mt-5">
            <h2 style={{ color: "white" }}>Cast</h2>
            <div className="d-flex flex-wrap gap-5 mt-5">
              {movieCast?.map((cast) => (
                <div
                  key={cast.id}
                  style={{ display: "grid", placeItems: "center" }}
                >
                  <LazyLoadImage
                    width={100}
                    height={100}
                    style={{
                      objectFit: "cover",
                      borderRadius: "100%",
                    }}
                    src={
                      cast.profile_path
                        ? `https://image.tmdb.org/t/p/w500${cast.profile_path}`
                        : IMAGE_UNAVAILABLE_PLACEHOLDER
                    }
                    alt="user"
                  />
                  <p
                    className="m-0 mt-2 mb-1 "
                    style={{ color: "white", textAlign: "center" }}
                  >
                    {cast.name}
                  </p>
                  <p style={{ color: "white", textAlign: "center" }}>
                    {cast.character}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </Container>
      <VideoPlayerModal
        videoid={movieVideoId && movieVideoId}
        title={movieInfo?.title}
        show={modalShow}
        onHide={() => setModalShow(false)}
      />
    </>
  );
}
