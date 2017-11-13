CREATE DATABASE lost_found_adoptable_animals;
USE lost_found_adoptable_animals;
CREATE TABLE animals
(
    Animal_ID INT NOT NULL PRIMARY KEY,
    Record_Type INT,
    Current_location VARCHAR(32),
    Animal_Name VARCHAR(32),
    animal_type VARCHAR(32),
    Animal_Gender VARCHAR(32),
    Animal_Breed INT,
    Animal_Color VARCHAR(32),
    Date VARCHAR(32),
    Date_Type VARCHAR(32),
    Obfuscated_Address VARCHAR(32),
    City VARCHAR(32),
    State VARCHAR(32),
    Zip INT,
    jurisdiction VARCHAR(32),
    Image VARCHAR(32),
    location_for_map VARCHAR(32),
    Memo VARCHAR
);
CREATE TABLE record_type
(
    Record_type_ID INT NOT NULL PRIMARY KEY,
    Record_type VARCHAR(32)
);
CREATE TABLE Animal_Breed
(
    Animal_Breed_ID INT NOT NULL PRIMARY KEY,
    Animal_Breed VARCHAR(32)
)