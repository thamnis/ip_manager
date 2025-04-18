# IP Manager

[![fr](https://img.shields.io/badge/lang-fr-blue.svg)](/README.fr.md) [![en](https://img.shields.io/badge/lang-en-red.svg)](/README.md)

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](/LICENSE)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Repo Size](https://img.shields.io/github/repo-size/thamnis/ip_manager)](https://github.com/thamnis/ip_manager)
[![Issues](https://img.shields.io/github/issues/thamnis/ip_manager)](https://github.com/thamnis/ip_manager/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/thamnis/ip_manager)](https://github.com/thamnis/ip_manager/pulls)
[![Contributors](https://img.shields.io/github/contributors/thamnis/ip_manager)](https://github.com/thamnis/ip_manager/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/thamnis/ip_manager)](https://github.com/thamnis/ip_manager/commits/main)

## 📌 Vue d'ensemble

**IP Manager** est une bibliothèque Python qui fournit des opérations avancées sur les adresses IP :

- ✅ **Validation des adresses IP et CIDR**.
- 🔄 **Conversion entre la notation binaire et décimale**.
- 🛠 **Calcul du masque de sous-réseau**.
- 📍 **Détermination de la plage d'adresses réseau**.
- 🚀 **Optimisation du réseau pour un nombre donné d'hôtes**.

## 🚀 Installation

Assurez-vous que **Python 3.x** est installé sur votre machine, puis clonez le dépôt :

```bash
git clone https://github.com/thamnis/ip_manager.git
cd ip_manager
```

## 📖 Utilisation

Exemple d'utilisation de la classe Ip :

``` Python
from ip_manager import Ip
 
# Création d'une instance avec une adresse IP
 
ip_instance = Ip("192.168.1.0/24")
 
print(f "Adresse IP : {ip_instance.ip}")
print(f "CIDR : {ip_instance.cidr}")
print(f "Masque décimal : {ip_instance.mask_dec}")
print(f "Plage d'adresses : {ip_instance.ip_range}")
```

Exécutez un exemple :

```Bash
python main.py
```

## 🌍 Optimisation du réseau

Si vous voulez optimiser votre réseau pour un nombre donné d'hôtes :

``` Python
reseau_optimise = ip_instance.optimize_network(50)
print(reseau_optimise)
```

## 🛠 Dépendances

Aucune dépendance externe n'est nécessaire. Le script fonctionne avec les modules standards de Python.

C'est du 100% bio.

## 🧪 Tests unitaires

Un fichier de test [test.py](/test.py) est disponible pour valider les fonctionnalités.

### 🔹 Exécution des tests

``` Bash
python -m unittest test.py
```

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](/LICENSE) pour plus de détails.

## ✨ Auteur

Écrit par [@thamnis](https://www.github.com/thamnis).
