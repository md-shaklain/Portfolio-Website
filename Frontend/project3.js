console.log("Welcome to Spotify");

// Initialize variables
let songIndex = 0;
let audioElement = new Audio('audio/audio.MP3');
let masterPlay = document.getElementById('masterPlay');
let myProgressBar = document.getElementById('myProgressBar');
let gif = document.getElementById('gif');
let masterSongName = document.getElementById('masterSongName');
let songItems = Array.from(document.getElementsByClassName('songItem'));

// Songs array
let songs = [
  { songName: "Aap Nazar Aaye", filePath: "audio/1.mp3.MP3", coverPath: "image/cover1.jpg" },
  { songName: "Deewaniyat", filePath: "audio/2.mp3.MP3", coverPath: "image/cover2.jpg" },
  { songName: "Dhurandhar Title Track", filePath: "audio/3.mp3.MP3", coverPath: "image/cover3.jpg" },
  { songName: "Guzaara", filePath: "audio/4.mp3.MP3", coverPath: "image/cover4.jpg" },
  { songName: "Khudaya Ishq", filePath: "audio/5.mp3.MP3", coverPath: "image/cover5.jpg" },
  { songName: "Mera Hua", filePath: "audio/6.mp3.MP3", coverPath: "image/cover6.jpg" },
  { songName: "Raat Bhar", filePath: "audio/7.mp3.MP3", coverPath: "image/cover7.jpg" },
  { songName: "Tere Ishk Mein", filePath: "audio/8.mp3.MP3", coverPath: "image/cover8.jpg" },
  { songName: "Tu Pehli Tu Aakhri", filePath: "audio/10.mp3.MP3", coverPath: "image/cover9.jpg" }
];

// Update song items in UI
songItems.forEach((element, i) => {
  let imgTag = element.getElementsByTagName("img")[0];
  let nameTag = element.getElementsByClassName("songName")[0];

  if (imgTag) imgTag.src = songs[i].coverPath;
  if (nameTag) nameTag.innerText = songs[i].songName;
});

// Handle play/pause click
masterPlay.addEventListener('click', () => {
  if (audioElement.paused || audioElement.currentTime <= 0) {
    audioElement.play();
    masterPlay.classList.remove('fa-play-circle');
    masterPlay.classList.add('fa-pause-circle');
    gif.style.opacity = 1;
  } else {
    audioElement.pause();
    masterPlay.classList.remove('fa-pause-circle');
    masterPlay.classList.add('fa-play-circle');
    gif.style.opacity = 1;
  }
});

// Listen to timeupdate event
  audioElement.addEventListener('timeupdate', () => {
  let progress = parseInt((audioElement.currentTime / audioElement.duration) * 100);
  myProgressBar.value = progress;
});

// Seekbar change event
  myProgressBar.addEventListener('change', () => {
  audioElement.currentTime = myProgressBar.value * audioElement.duration / 100;
});

// Reset all play buttons
const makeAllPlays = () => {
  Array.from(document.getElementsByClassName('songItemplay')).forEach((element) => {
    element.classList.remove('fa-pause-circle');
    element.classList.add('fa-play-circle');
  });
};

// Handle individual song play
Array.from(document.getElementsByClassName('songItemplay')).forEach((element) => {
  element.addEventListener('click', (e) => {
    makeAllPlays();
    songIndex = parseInt(e.target.id);
    e.target.classList.remove('fa-play-circle');
    e.target.classList.add('fa-pause-circle');
    audioElement.src = songs[songIndex].filePath;
    masterSongName.innerText = songs[songIndex].songName;
    audioElement.currentTime = 0;
    audioElement.play();
     gif.style.opacity = 1;
    masterPlay.classList.remove('fa-play-circle');
    masterPlay.classList.add('fa-pause-circle');
  });
});

// Handle next button
document.getElementById('next').addEventListener('click', () => {
  songIndex = (songIndex + 1) % songs.length;
  audioElement.src = songs[songIndex].filePath;
  masterSongName.innerText = songs[songIndex].songName;
  audioElement.currentTime = 0;
  audioElement.play();
  masterPlay.classList.remove('fa-play-circle');
  masterPlay.classList.add('fa-pause-circle');
});

// Handle previous button
document.getElementById('previous').addEventListener('click', () => {
  songIndex = (songIndex - 1 + songs.length) % songs.length;
  audioElement.src = songs[songIndex].filePath;
  masterSongName.innerText = songs[songIndex].songName;
  audioElement.currentTime = 0;
  audioElement.play();
  masterPlay.classList.remove('fa-play-circle');
  masterPlay.classList.add('fa-pause-circle');
});
