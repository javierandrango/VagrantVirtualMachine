# Usage
1. Download the `newsdata.sql` database from : https://drive.google.com/file/d/1L7yx9MBTK3Y_0dBFVGaD_ewtOnSva5hz/view?usp=sharing
2. Save the `newsdata.sql` file inside the `/vagrant/newsdata` directory
3. Open a new bash comman line in the `/vagrant` directory:
    ```bash 
    vagrant up # optional if the virtual machine was power off
    vagrant ssh 
    ```
4. The database `newsdata` was already set up inside the `VagrantFile` by now is empty, to check the DB run:
    ```bash
    psql newsdata
    \dt+
    \q
    ```
5. change directory to `/vagrant/newsdata` and `ls` to show the files 
6. Load the data into the DB:
    ```bash
    cd .. # return to /vagrant directory
    psql -d newsdata -f newsdata.sql
    psql newsdata
    ```
7. Usefull comands to explote the DB:
    >`\d` and `\dt`, shows list of relations and tables respectively
