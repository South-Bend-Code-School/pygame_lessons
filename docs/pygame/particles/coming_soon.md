# Particle Effects Mini Lesson Coming Soon

In the meantime, play our game.

**Tap or Press Spacebar to Play**

<div>
   <canvas id="gameCanvas" width="400" height="200"></canvas>
    
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        
        const ORANGE = "rgb(255, 155, 32)";
        const PURPLE = "rgb(179, 55, 255)";
        const BLACK = "rgb(19, 22, 25)";
        
        let dino, obstacles, gameOver, score, playing;
        
        function resetGame() {
            dino = { x: 50, y: 150, width: 30, height: 30, vy: 0, gravity: 0.6, jumping: false };
            obstacles = [];
            gameOver = false;
            score = 0;
            playing = false;
            update();
        }
        
        function drawDino() {
            ctx.fillStyle = ORANGE;
            ctx.fillRect(dino.x, dino.y, dino.width, dino.height);
        }
        
        function drawObstacles() {
            ctx.fillStyle = PURPLE;
            obstacles.forEach(obstacle => ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height));
        }
        
        function drawGround() {
            ctx.fillStyle = BLACK;
            ctx.fillRect(0, 180, canvas.width, 20);
        }
        
        function update() {
            if (gameOver) return;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawGround();
            
            if (playing) {
                dino.y += dino.vy;
                dino.vy += dino.gravity;
                if (dino.y >= 150) {
                    dino.y = 150;
                    dino.jumping = false;
                }
                
                obstacles.forEach(obstacle => {
                    obstacle.x -= 5;
                    if (obstacle.x + obstacle.width < 0) {
                        obstacles.shift();
                        score++;
                    }
                    if (dino.x < obstacle.x + obstacle.width && dino.x + dino.width > obstacle.x && dino.y < obstacle.y + obstacle.height && dino.y + dino.height > obstacle.y) {
                        gameOver = true;
                        playing = false;
                        return;
                    }
                });
                
                if (Math.random() < 0.02 && obstacles.length < 3) {
                    obstacles.push({ x: canvas.width, y: 160, width: 20, height: 40 });
                }
            }
            
            drawDino();
            drawObstacles();
            ctx.fillStyle = "black";
            ctx.font = "20px Arial";
            ctx.fillText(`Score: ${score}`, 10, 30);
            requestAnimationFrame(update);
        }
        
        function jump() {
            if (gameOver) {
                resetGame();
                gameOver = false;
                playing = true;
            }
            if (!playing) {
                playing = true;
            }
            if (!dino.jumping) {
                dino.vy = -10;
                dino.jumping = true;
            }
        }
        
        document.addEventListener("keydown", (event) => {
            if (event.code === "Space") {
                jump();
            }
        });
        
        canvas.addEventListener("click", () => {
            jump();
        });
        
        resetGame();
    </script>
</div>
