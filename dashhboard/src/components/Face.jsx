import { useEffect, useRef } from 'react';

const Face = () => {
  const videoRef = useRef(null);

  useEffect(() => {

    navigator.mediaDevices.getUserMedia({ video: true })
      .then((stream) => {
        videoRef.current.srcObject = stream;
      })
      .catch((error) => {
        console.error('Error accessing camera:', error);
      });

    return () => {
      // Stop recording the face when the component is unmounted
      if (videoRef.current && videoRef.current.srcObject) {
        // eslint-disable-next-line react-hooks/exhaustive-deps
        const stream = videoRef.current.srcObject;
        const tracks = stream.getTracks();

        tracks.forEach((track) => {
          track.stop();
        });
      }
    };
  }, []);

  return (
    <div>
      <video ref={videoRef} autoPlay />
    </div>
  );
};

export default Face;
