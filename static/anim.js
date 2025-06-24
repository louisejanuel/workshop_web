const bg = document.getElementById('background');

// Position initiale aléatoire
let x = Math.random() * window.innerWidth;
let y = Math.random() * window.innerHeight;
let angle = 0;

// Vitesse de déplacement aléatoire
let speedX = (Math.random() - 0.5) * 10; // entre -2 et 2 px/frame
let speedY = (Math.random() - 0.5) * 10;
let rotationSpeed = (Math.random() - 0.5) * 4; // entre -1 et 1 deg/frame

function animate() {
    // Met à jour position
    x += speedX;
    y += speedY;
    angle += rotationSpeed;

    // Rebonds sur les bords
    if (x < 0 || x > window.innerWidth) speedX *= -1;
    if (y < 0 || y > window.innerHeight) speedY *= -1;

    // Applique les styles
    bg.style.transform = `translate(${x}px, ${y}px) rotate(${angle}deg)`;

    requestAnimationFrame(animate);
}

// Démarre l'animation quand la page est prête
window.onload = animate;
