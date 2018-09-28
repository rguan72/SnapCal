// Camera function; used to be in camera_cp.html
const player = document.getElementById('player');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const captureButton = document.getElementById('capture');

const constraints = {
  video: true,
};

captureButton.addEventListener('click', () => {
  context.drawImage(player, 0, 0, canvas.width, canvas.height);

// Stops video functionality after capture
//player.srcObject.getVideoTracks().forEach(track => track.stop());
});
// Send captured image to a backend for image parsing

navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {
    player.srcObject = stream;
  });
