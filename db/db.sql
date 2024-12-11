CREATE DATABASE wardrobio;

USE wardrobio;

CREATE TABLE Seasons (
    season_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE ClothingTypes (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE ClothingPieces (
    piece_id INT AUTO_INCREMENT PRIMARY KEY,
    type_id INT,
    name VARCHAR(100) NOT NULL,
    color VARCHAR(50),
    size VARCHAR(10),
    FOREIGN KEY (type_id) REFERENCES ClothingTypes(type_id)
);

CREATE TABLE Outfits (
    outfit_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    season_id INT,
    FOREIGN KEY (season_id) REFERENCES Seasons(season_id)
);

CREATE TABLE OutfitClothing (
    outfit_id INT,
    piece_id INT,
    PRIMARY KEY (outfit_id, piece_id),
    FOREIGN KEY (outfit_id) REFERENCES Outfits(outfit_id),
    FOREIGN KEY (piece_id) REFERENCES ClothingPieces(piece_id)
);