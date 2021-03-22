import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { useState, useEffect } from "react";
import { getAllSongs } from "../../store/songs";
import { restoreUser } from "../../store/session";

const Home = () => {
  const dispatch = useDispatch();
  const songs = useSelector((state) => Object.values(state.songs));
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    if (songs) {
      // dispatch(restoreUser());
      dispatch(getAllSongs()).then((req) => setIsLoaded(true));
    }
  }, [dispatch]);

  return (
    isLoaded && (
      <>
        <h1>My Home </h1>
        {songs.map((song, idx) => (
          <li key={idx}>{song.title}</li>
        ))}
      </>
    )
  );
};

export default Home;
