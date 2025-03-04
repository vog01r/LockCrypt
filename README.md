# LockCrypt

## Description

**LockCrypt** est une solution open source de test de cybersécurité, conçue pour offrir une plateforme de chiffrement robuste et flexible. Inspirée par les standards de l'industrie, LockCrypt permet aux développeurs et aux professionnels de la sécurité de tester et d'évaluer les fonctionnalités de défense de leurs systèmes. En utilisant la bibliothèque `cryptography`, LockCrypt offre un chiffrement de type industriel qui peut être intégré dans des environnements de test pour simuler des scénarios de sécurité réels.

Cette solution est idéale pour les entreprises et les chercheurs en cybersécurité qui souhaitent explorer et renforcer les capacités de défense de leurs infrastructures numériques. LockCrypt est conçu pour être facilement extensible, permettant aux utilisateurs d'adapter et d'améliorer les fonctionnalités selon leurs besoins spécifiques.

## Fonctionnalités

- **Chiffrement partiel** : Chiffre uniquement les 2048 premiers octets de chaque fichier pour une performance optimale.
- **Gestion des clés** : Génération, stockage et chargement sécurisés des clés de chiffrement.
- **Support des répertoires critiques** : Chiffrement et déchiffrement des répertoires utilisateurs et des lecteurs réseau sous Windows.
- **Chiffrement et déchiffrement individuels** : Scripts dédiés pour le traitement de fichiers spécifiques.
- **Extensibilité** : Conçu pour être facilement extensible avec des fonctionnalités supplémentaires.

## Installation

Pour installer et configurer LockCrypt, suivez les étapes ci-dessous :

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/vogeaux/LockCrypt.git
   cd LockCrypt
   ```

2. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Génération de la clé

Avant de chiffrer ou de déchiffrer des fichiers, vous devez générer une clé de chiffrement. Utilisez le script `keygen.py` pour cela :

```bash
python LockCrypt/keygen.py
```

### Chiffrement

Pour chiffrer les fichiers dans un répertoire ou des répertoires critiques :

- **Répertoire spécifique** :
  ```bash
  python LockCrypt/encryption.py
  ```

- **Fichier individuel** :
  Modifiez le chemin du fichier dans `standalone_encryption.py` et exécutez :
  ```bash
  python LockCrypt/standalone_encryption.py
  ```

### Déchiffrement

Pour déchiffrer les fichiers dans un répertoire ou des répertoires critiques :

- **Répertoire spécifique** :
  ```bash
  python LockCrypt/decryption.py
  ```

- **Fichier individuel** :
  Modifiez le chemin du fichier dans `standalone_decrypt.py` et exécutez :
  ```bash
  python LockCrypt/standalone_decrypt.py
  ```

## Architecture du Projet

- **LockCrypt/encryption.py** : Gère le chiffrement des fichiers dans un répertoire.
- **LockCrypt/decryption.py** : Gère le déchiffrement des fichiers dans un répertoire.
- **LockCrypt/standalone_encryption.py** : Chiffre un fichier spécifique.
- **LockCrypt/standalone_decrypt.py** : Déchiffre un fichier spécifique.
- **LockCrypt/keygen.py** : Génère et gère les clés de chiffrement.
- **LockCrypt/utils.py** : Fournit des utilitaires pour le chargement des clés.

## Sécurité

LockCrypt utilise l'algorithme de chiffrement symétrique `Fernet` de la bibliothèque `cryptography`, garantissant que vos données sont protégées par un chiffrement fort et sécurisé. Assurez-vous de stocker votre fichier de clé en lieu sûr, car il est essentiel pour le déchiffrement des données.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer LockCrypt, veuillez suivre ces étapes :

1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. Commitez vos modifications (`git commit -m 'Add some AmazingFeature'`).
4. Poussez votre branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence Apache 2.0. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

Merci à la communauté open-source et aux contributeurs de la bibliothèque `cryptography` pour leur travail exceptionnel qui a rendu ce projet possible.
