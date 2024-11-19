function startGame(gameName) {
  alert(`Starting the ${gameName} game!`);

  if (gameName === "clicker") {
    loadClickerGame();
  } else if (gameName === "ticTacToe") {
    loadTicTacToe();
  } else if (gameName === "memory") {
    loadMemoryGame();
  }
}

function loadClickerGame() {
  document.body.innerHTML = `
    <div style="text-align: center; margin-top: 50px;">
      <h2>Clicker Game</h2>
      <p>Click as fast as you can!</p>
      <button id="clickButton">Click Me!</button>
      <p>Clicks: <span id="clickCount">0</span></p>
      <button onclick="location.reload()">Back to Menu</button>
    </div>
  `;

  let count = 0;
  document.getElementById("clickButton").addEventListener("click", () => {
    count++;
    document.getElementById("clickCount").textContent = count;
  });
}

function loadTicTacToe() {
  document.body.innerHTML = `
    <div style="text-align: center; margin-top: 50px;">
      <h2>Tic-Tac-Toe</h2>
      <p>Coming soon...</p>
      <button onclick="location.reload()">Back to Menu</button>
    </div>
  `;
}

function loadMemoryGame() {
  document.body.innerHTML = `
    <div style="text-align: center; margin-top: 50px;">
      <h2>Memory Game</h2>
      <p>Coming soon...</p>
      <button onclick="location.reload()">Back to Menu</button>
    </div>
  `;
}
