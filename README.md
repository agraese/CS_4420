# CS 4420 SEMESTER PROJECT

## File Descriptions

    - Lost_found_adoptable_pets.csv
        - cleaned and adapted dataset from King County, WA (data.gov)
    - Lost_found_adoptable_pets_new.csv
        - csv file mentioned above including indexed references
    - Record_Type_Index.csv
        - Generated index for whether the record is for a lost, found, or adoptable pet.
    - Animal_Breed_Index.csv
        - Generated index for the animal breed the record is for.
    - boostrap.sql
        - initializes database
    > FlaskApp
        - app.py
            - runs the flask app.
        > Templates
            - index.html
                - Template for the home page

## Run Instructions

    In order to run this application, you will need to have flask installed, on a mac, it can be installed by running:
    ```
    pip install flask
    ```
    You must be in the **Flask App** directory.  When you are here, you can run the command:
    ```
    python app.py
    ```
    This should begin running the application on your local host.  The terminal window will tell you the address where it is running.

### Run on  Cloud9

    > FlaskApp
	    - Change app.py to be app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))