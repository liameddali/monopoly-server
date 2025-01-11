function copyGameId() {
  const copyText = document.getElementById("game_id");

  // Copier le texte dans le presse-papiers
  navigator.clipboard.writeText(copyText.textContent || copyText.innerText)
      .then(() => {
          // Afficher le message de confirmation dans la liste dynamique
          displayDynamicMessage('info', "Game ID copied!");
      })
      .catch(err => {
          console.error("Failed to copy text: ", err);
      });
}
