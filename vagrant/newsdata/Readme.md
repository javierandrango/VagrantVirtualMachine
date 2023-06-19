# Prerequisites
1. Download the `newsdata.sql` database from : https://drive.google.com/file/d/1L7yx9MBTK3Y_0dBFVGaD_ewtOnSva5hz/view?usp=sharing
2. Download extra Python packages to generate a better report:
    ```bash
    pip install pandas --user
    ```
    `pip <command> --user` changes the scope of the current pip command to work on the current user account's local python package install location, rather than the system-wide package install location, which is the default.

# Usage

1. Save the `newsdata.sql` file inside the `/vagrant/newsdata` directory
2. Open a new bash comman line and type:
    ```bash
    cd .. # IMPORTANT return or go to /vagrant directory
    vagrant up # optional if the virtual machine was power off
    vagrant ssh # SSH sesion into the VM to give shell access
    ```
3. The database `newsdata` was already set up inside the `VagrantFile` by now is empty, to check the DB run:
    ```bash
    psql newsdata # explore the DB
    ```
    ```sql 
    -- single line comment
    
    /*
    * block comments
    */

    -- shows list of relations inside DB (by now is empty):
    \dt+
    -- exit the DB (return to VM):
    \q
    ``` 
4. Load the data into the DB:
    ```bash
    cd /vagrant/newsdata
    psql -d newsdata -f newsdata.sql # add downloaded data inside DB
    psql newsdata
    ```
    ```sql
    \dt+ 
    select * from log limit 2; -- explote info inside a table
    ```
5. Run the python script:
```bash
python3 python3 newsreport.py
```

