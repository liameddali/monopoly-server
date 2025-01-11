# Monopoly Server

<img src="https://github.com/user-attachments/assets/9e17919b-de3f-4d07-80cc-afb2277a8795" alt="Page de connexion" height="450px">
*Page de connexion*

<img src="https://github.com/user-attachments/assets/613aa667-d11f-448a-b377-42605af19274" alt="Page d'inscription" height="450px">
*Page d'inscription*

<img src="https://github.com/user-attachments/assets/b6c056dc-8d85-4c53-a0e7-a1761297431e" alt="Jeu en cours ou nouveau jeu" height="450px">
*Jeu en cours ou nouveau jeu*

<img src="https://github.com/user-attachments/assets/9eb9793a-0375-4082-a4c0-fb63e6427ddf" alt="Rejoindre une partie" height="450px">
*Rejoindre une partie*

<img src="https://github.com/user-attachments/assets/dd533d74-c521-499e-afa7-bc6b9172cf63" alt="Nouvelle partie" height="450px">
*Nouvelle partie*

<img src="https://github.com/user-attachments/assets/dff69b88-239a-4810-8421-359785f1a375" alt="Tableau de bord - Portefeuille" height="450px">
*Tableau de bord - Portefeuille*

---

## À propos

Monopoly Server est une application serveur permettant de jouer au jeu de société Monopoly en ligne. Elle offre une interface utilisateur pour gérer les parties, les joueurs et les transactions, tout en respectant les règles classiques du Monopoly.

---

## Fonctionnalités

- **Gestion des utilisateurs** : Inscription, connexion et gestion des profils des joueurs.
- **Création de parties** : Créez de nouvelles parties de Monopoly et invitez des joueurs à rejoindre.
- **Rejoindre des parties** : Rejoignez des parties existantes avec un code d'invitation.
- **Interface de jeu interactive** : Jouez au Monopoly avec une interface utilisateur intuitive.
- **Tableau de bord** : Visualisez votre portefeuille et vos propriétés en temps réel.

---

## Captures d'écran

*Les captures d'écran sont présentées en haut de ce document pour illustrer les différentes fonctionnalités de l'application.*

---

## Installation

Pour installer et exécuter le serveur Monopoly localement, suivez les étapes ci-dessous :

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/liameddali/monopoly-server.git
   cd monopoly-server
   ```

2. **Installer les dépendances** :

   Assurez-vous d'avoir Python installé sur votre machine. Ensuite, installez les dépendances requises :

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer la base de données** :

   Configurez votre base de données selon les paramètres définis dans le fichier de configuration. Assurez-vous que les migrations sont effectuées correctement.

4. **Lancer le serveur** :

   ```bash
   python src/main.py
   ```

   Le serveur sera accessible à l'adresse `http://localhost:8000`.

---

## Utilisation

Une fois le serveur en cours d'exécution, vous pouvez accéder à l'interface utilisateur via votre navigateur web. Depuis le tableau de bord, vous pouvez :

- **Créer une nouvelle partie** : Définissez les paramètres de la partie et invitez des joueurs.
- **Rejoindre une partie existante** : Entrez le code d'invitation fourni par l'hôte.
- **Gérer votre portefeuille** : Consultez vos propriétés, votre argent et vos transactions en cours.

---

## Contributions

Les contributions sont les bienvenues ! Pour contribuer :

1. **Forkez** le projet.
2. **Créez une branche** pour votre fonctionnalité (`git checkout -b ma-nouvelle-fonctionnalité`).
3. **Commitez** vos modifications (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4. **Poussez** vers la branche (`git push origin ma-nouvelle-fonctionnalité`).
5. **Ouvrez une Pull Request**.

---

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](https://github.com/liameddali/monopoly-server/blob/main/LICENSE) pour plus de détails.

---

## Crédits

Développé par [Liam Eddali](https://github.com/liameddali).

---
