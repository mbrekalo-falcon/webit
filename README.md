# Webit
# Django Envdir settings
- *Files in envdir*:
    - DATABASE -> file name (uppercase):
        - file settings
        ```    
            {
                "host": "",
                "port": 5432,
                "name": "",
                "password": ""
            }
        ```
    - DJANGO SETTINGS -> file name (uppercase):
        - file settings
         ```    
            {
                "security_key": "RANDOM HASH",
                "debug": true,
                "allowed_hosts": ["*"]
            }
         ```
      
# Create Extra folders:
- log/
- .envdir/
- staticfiles/
- static/
- media/

# Install dependency:
- ```make install-packages```

# Migrate models:
- ```make migrate```
    
# Run application:
- ```make run```

