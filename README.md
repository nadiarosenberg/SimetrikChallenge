# __Endpoints__
- [GET - tables](#get---tables)
- [GET - tables/name](#get---tables/name)
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
        {
            "message": "Something wrong happened"
        }


# GET - tables/name
Returns the table content corresponding to the name, paginated. Also allows filter (only one property at the time) and order by one column, DESC. If the table does not exist, returns error. 

- ## Method
GET

- ## Url
categories/name

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
        {
            "message": "Something wrong happened"
        }
            
- ### Case 2
        Table not found
    
    #### Code
        404
    
    #### Content
        {
            "message": "Table does not exist"
        }

# POST - tables/create/
Creates a table based on a .csv file.

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
        {
            "message": "Table created"
        }

- ## Error responses

- ### Case 1
        url is not provided
    
    #### Code:
        400
    
    #### Content
        {
            "message": ".csv file url is required"
        }

- ### Case 2
        Invalid url
    
    #### Code:
        400
    
    #### Content
        {
            "message": "Invalid url"
        }
        
- ### Case 3
        Table already exist
    
    #### Code:
        200
    
    #### Content
        {
            "message": "Table already exist"
        }
        
- ### Case 4
        Internal server error
    
    #### Code
        500
    
    #### Content
        {
            "message": "Something wrong happened"
        }

