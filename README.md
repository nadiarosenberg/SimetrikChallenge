# Start
Python version: Python 3.8.10

1. Create environment

For windows:

        > python -m venv env
        > .\env\Scripts\activate

2. Install dependencies

        > cd ./SimetrikChallenge
        > pip install -r requirements.txt

3. Create .env file with your database and amazon credentials:

        DB_NAME=your_dbname
        DB_USER=your_user
        DB_PASSWORD=your_password
        DB_PORT=your_port
        DB_HOST=your_host
        DB_URL=mysql+pymysql://your_user:your_password@your_host:your_port/your_dbname
        AWS_ACCESS_KEY_ID = your_id
        AWS_SECRET_ACCESS_KEY = your_key
        AWS_REGION = your_region
        BUCKET_NAME = your_bucketname

3. Run app

        > cd ./SimetrikChallenge
        > python manage.py runserver
    
    **Do not run migrations**

4. Run tests

        > python manage.py test 

# __Endpoints__
- [GET - tables](#get---tables)
- [GET - tables/name](#get---tables/:name)
- [POST - tables/create/](#post---tables/create)

# GET - tables
Returns all existing tables. If there are no tables, returns an empty array.

- ## Method
GET

- ## Url
/tables

- ## Success response
    ### Code
        200 
    ### Content 
        [
            {
                "Tables_in_database: "table"
            }
        ]

- ## Example
For a database with 2 tables:

        [
            {
                "Tables_in_database: "table1"
            },
            {
                "Tables_in_database: "table2"
            }
        ]       


- ## Error response: 

    ### Case: 
        Internal server error
    ### Code 
        500
        
    ### Content
            
             "Something wrong happened"

# GET - tables/:name
Returns the table content corresponding to the name, paginated. Also allows filter (only one property at the time) and order by one column, DESC. If the table does not exist, returns error. 

- ## Method
GET

- ## Url
categories/:name

- ## Url params

Required:

        name = str

- ## Query string (optional):

        page = numeric str | Default value = 1
        pageSize = numeric str | Default value = 10
        prop = str 
        where = str
        equals = str 


- ## Success response
    ### Code
        200 
    ### Content     
        {
            "pagination": {
                "current": "url"
                "prev": "url or null"
                "next": "url or null"
            },
            "result": [
                {
                    "table column 1": "value",
                    "table column 2": "value"
                }
            ]
        }
        
    previous and next depend on the pagination performed. 

    ### Example
    
    For a table named table1, prop = 'propertyA', where = 'propertyB' and equals = 'value1' (total 10 registers), page = 1 and pageSize = 2:

        {
            "pagination": {
                "current": "/table1?page=1&pageSize=2",
                "prev": null,
                "next": "/table1?page=2&pageSize=2"
            },
            "result": [
                {
                    "propertyA": "property value 10",
                    "propertyB" : "value1"
                },
                {
                    "propertyA": "property value 9"
                    "propertyB" : "value1"
                }
                
            ]
        }

- ## Error responses

- ### Case 1
        Internal server error
    
    #### Code: 
        500
    
    #### Content:
        
        "Something wrong happened"
           
- ### Case 2
        Table not found
    
    #### Code
        404
    
    #### Content
        
        "Table does not exist"
        

# POST - tables/create/
Creates a table based on a .csv file url. 

- ## Method
POST

- ## Url
tables/create/

- ## Url params

Required:

        url = string

- ## Success response
    ### Code
        201 
    ### Content 
        
        "Table created"
        
- ## Error responses

- ### Case 1
        url is not provided
    
    #### Code:
        400
    
    #### Content
        
        ".csv file url is required"

- ### Case 2
        Invalid url
    
    #### Code:
        400
    
    #### Content
        
        "Invalid url"
        
- ### Case 3
        Table already exist
    
    #### Code:
        200
    
    #### Content
        
        "Table already exist"
        
- ### Case 4
        Internal server error
    
    #### Code
        500
    
    #### Content
        
        "Something wrong happened"

