import React, { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { postUserComment } from "../../store/songs";

const CommentForm = ({userId, newComment, setNewComment, sessionUser}) => {
  const { songId } = useParams();
  const dispatch = useDispatch();
  const [comment, setComment] = useState("");
  const history = useHistory()
  // const sessionUser = useSelector((state) => state.user);

  const commentSubmit = async (e) => {
    e.preventDefault();

    if(!sessionUser?.user) history.push("/login")

    const userComment = {
      user_id: userId,
      content: comment,
    };
    console.log(songId, userComment);
    await dispatch(postUserComment(userComment, songId));
   
  };

  useEffect(() => {
    setComment("")
  }, [newComment])

  const newCommentSubmit = () => {
    return setTimeout(() => {
      console.log("hello")
      setNewComment(true)
    }, 10)
  }

  return (
    <div id="comment-form-div">
      <form id="comment-form" onSubmit={commentSubmit}>
        <textarea
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          id="comment-text"
          placeholder="Comment"
        ></textarea>
        <button onClick={newCommentSubmit} id="comment-submit-button" type="submit">
          Submit
        </button>
      </form>
    </div>
  );
};

export default CommentForm;
