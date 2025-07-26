function selectBestGenre (genres, plays) {
  const genreHash = new Map();
  genres.forEach((genre, i) => {
    genreHash.set(genre, (genreHash.get(genre) || 0) + plays[i])
  })

  return [...genreHash].sort((a, b) => b[1] - a[1]);
}

function getSongHash (genres, plays) {
  const songHash = new Map();
  
  genres.forEach((genre, i) => {
    if (!songHash.has(genre)) {
      songHash.set(genre, []);
    }
    songHash.get(genre).push([i, plays[i]])
  })
  return songHash;
}

function getBestAlbum (bestGenreHash, songHash) {
  const bestAlbum = [];
  for (let [genre] of bestGenreHash) {
    const songs = songHash.get(genre);
    songs.sort((a, b) => {
      if (b[1] !== a[1]) return b[1] - a[1];
      return a[0] - b[0];
    });
    bestAlbum.push(...songs.slice(0, 2).map(song => song[0]))
  }

  return bestAlbum;
}

function solution(genres, plays) {
    const bestGenreHash = selectBestGenre(genres, plays);
    const songHash = getSongHash(genres, plays);
    const bestAlbum = getBestAlbum(bestGenreHash, songHash);
    return bestAlbum;
}