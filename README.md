# Monopoly Server

![Page de connexion](https://github.com/liameddali/monopoly-server/blob/main/images/login.png)
*Page de connexion*

![Page d'inscription](https://github.com/liameddali/monopoly-server/blob/main/images/sign-up.png)
*Page d'inscription*

![Jeu en cours ou nouveau jeu](https://github.com/liameddali/monopoly-server/blob/main/images/current-or-new-game.png)
*Jeu en cours ou nouveau jeu*

![Rejoindre une partie](https://github.com/liameddali/monopoly-server/blob/main/images/join-a-game.png)
*Rejoindre une partie*

![Nouvelle partie](https://github.com/liameddali/monopoly-server/blob/main/images/new-game.png)
*Nouvelle partie*

![Tableau de bord - Portefeuille](https://github.com/liameddali/monopoly-server/blob/main/images/dashboard-wallet.png)
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
