const gameListContainer = document.getElementById('game-list');
const emulatorCard = document.getElementById('emulator-card');
const gameTitle = document.getElementById('game-title');
const loginPage = document.getElementById('login-page');
const gamePage = document.getElementById('game-page');
const loginForm = document.getElementById('login-form');
const loginError = document.getElementById('login-error');
const logoutButton = document.getElementById('logout-button');

let loggedIn = false;


loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch(`/api/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    if (response.ok) {
        loggedIn = true;
        loginPage.style.display = 'none';
        gamePage.style.display = 'block';
        logoutButton.style.display = 'block'; // Show logout button
        fetchGames();
    } else {
        loginError.textContent = "Invalid username or password!";
    }
});

logoutButton.addEventListener('click', async () => {
    await fetch(`/api/logout`, { method: 'POST' });
    loggedIn = false;
    loginPage.style.display = 'block';
    gamePage.style.display = 'none';
    logoutButton.style.display = 'none'; // Hide logout button
});

async function fetchGames() {
    try {
        const response = await fetch(`/api/games`);
        const games = await response.json();
        displayGameList(games);
    } catch (error) {
        console.error('Error fetching games:', error);
        gameListContainer.innerHTML = '<p>Error loading games. Please try again later.</p>';
    }
}

function displayGameList(games) {
    gameListContainer.innerHTML = '';
    games.forEach(game => {
        const button = document.createElement('button');
        button.textContent = game.name;
        button.onclick = () => startGame(game);
        gameListContainer.appendChild(button);
    });
}

async function startGame(game) {
    try {
        const response = await fetch(`/api/games/${game.id}/download`);
        if (!response.ok) throw new Error('Error fetching game file');

        const blob = await response.blob();
        const url = URL.createObjectURL(blob);

        gameTitle.textContent = game.name;
        emulatorCard.style.display = 'block';

        window.EJS_player = "#game";
        window.EJS_gameName = game.name;
        window.EJS_biosUrl = "";
        window.EJS_gameUrl = url;
        window.EJS_core = game.core;
        window.EJS_pathtodata = "data/";
        window.EJS_startOnLoaded = true;

        const script = document.createElement('script');
        script.src = "data/loader.js";
        document.body.appendChild(script);
    } catch (error) {
        console.error('Error starting game:', error);
        alert('Error starting game. Please try again.');
    }
}
