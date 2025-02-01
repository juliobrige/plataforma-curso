// static/js/script.js
document.addEventListener('DOMContentLoaded', function () {
    const video = document.getElementById('videoPlayer');
    const progressBar = document.getElementById('progressBar');

    // Play/Pause
    function togglePlay() {
        video.paused ? video.play() : video.pause();
    }

    // Atualizar barra de progresso
    video.addEventListener('timeupdate', () => {
        const progress = (video.currentTime / video.duration) * 100;
        progressBar.value = progress;
    });

    // Pular para um ponto do vídeo
    progressBar.addEventListener('input', () => {
        const time = (progressBar.value / 100) * video.duration;
        video.currentTime = time;
    });
});