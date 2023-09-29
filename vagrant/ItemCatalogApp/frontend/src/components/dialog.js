/**
 * MODULES
 */
import $ from 'jquery';
let bcrypt = require('bcryptjs');

/**
 * VARIABLES
 */
// login dialog variables
const loginButton = document.getElementById('loginButton');
const loginUserDialog = document.getElementById('loginUserDialog');
const loginPswdDialog = document.getElementById('loginPswdDialog');
const closeBtn1 = document.getElementById('closeBtn1');
const closeBtn2 = document.getElementById('closeBtn2');
const nextBtn = document.getElementById('nextBtn');
const loginBtn = document.getElementById('loginBtn');

/**
 * HANDLING EVENTS
 */
//open login dialog (username verification)
if (loginButton){
loginButton.addEventListener("click",()=>{
    localStorage.setItem('openDialogFlag', 'true');
});
};
// keep login dialog open when button click
if(loginUserDialog || loginPswdDialog){
    loginUserDialogOpen();
    loginPswdDialogOpen();
}; 

//close dialogs
if (closeBtn1){
    closeBtn1.addEventListener("click", ()=>{
        closeDialogWithBttn1();
    });
};
if (closeBtn2){
    closeBtn2.addEventListener("click", ()=>{
        closeDialogWithBttn2();
    });
};
//username or email validation
if (nextBtn){
    nextBtn.addEventListener("click", ()=>{
        verifyUsername();
    });
};
//password validation
if(loginBtn){
    loginBtn.addEventListener("click",()=>{
        verifyPswd();
    })
};

/**
 * ----- USER DEFINED FUNCTIONS -----
 */
//check dialog status
/*function checkDialog(dialog){
    if(dialog.open){
        console.log("login Dialog Open")
    }
    else{
        console.log("login Dialog closed")
    }
};*/
//keep username dialog open
function loginUserDialogOpen(){
    let status = localStorage.getItem('openDialogFlag');
    if (status ==='true'){
        loginUserDialog.showModal();
        //checkDialog(loginUserDialog);
        localStorage.setItem('openDialogFlag','false');
    }
};
//keep pswd dialog open
function loginPswdDialogOpen(){
    let status = localStorage.getItem('openPswdDialogFlag');
    if (status ==='true'){
        loginPswdDialog.showModal();
        localStorage.setItem('openPswdDialogFlag','false');
    }
};
//close the login dialog
function closeDialogWithBttn1(){
    localStorage.setItem('openDialogFlag','false');
    loginUserDialog.close();
};
function closeDialogWithBttn2(){
    localStorage.setItem('openPswdDialogFlag','false');
    loginPswdDialog.close();
};
// username or email validation
function verifyUsername(){
    const $username = $('#username'); //to add the username in disabled input
    const $salt = $('#salt'); //to add salt value in hidden div
    const $loginFlashMsg = $('#loginStatusMsgs'); //to add flash messages
    const username_or_email = document.getElementById('username_or_email').value;
    fetch('/login/verify_username_or_email/',{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            //'Origin': window.location.origin,
        },
        body: JSON.stringify({ username_or_email }),
    })
    .then(response => response.json())
    .then(data=>{
        if(data.username){
            //close username dialog
            loginUserDialog.close();
            //open password dialog
            localStorage.setItem('openPswdDialogFlag', 'true');
            //set values into tag html
            $username.val(data.username);
            $salt.val(data.salt);
            //open password dialog
            loginPswdDialogOpen();
        }
        else{
            // open a clean username dialog
            document.getElementById('username_or_email').value = "";
            localStorage.setItem('openDialogFlag', 'true');
            // show flash message
            $loginFlashMsg.text(data.message);
            $loginFlashMsg.show();
            setTimeout(function(){
                $loginFlashMsg.hide();
            },1500);
        }
    })
};

//hash password
function generateHash(password,salt){
    return new Promise((resolve,reject)=>{
        bcrypt.hash(password,salt,function(error,hash){
            if(error){
                reject(error);
            }else{
                resolve(hash);
            }
        })
    });
};

// pswd verification
function verifyPswd(){
    const username = document.getElementById('username').value; //get username value from html tag
    const salt = document.getElementById('salt').value; //get salt value from html tag
    const inputPswd = document.getElementById('pswd').value; //get password for input tag
    const $loginFlashMsg = $('#loginStatusMsgs'); //to add flash messages
    
    //generate hash
    generateHash(inputPswd,salt)
    .then((hash)=>{
        //console.log(hash);
        const pswd_hash = hash;
        fetch('/login/verify_pswd/',{
            method: 'POST',
            credentials:'include',
            headers:{
                'Content-Type': 'application/json',
                //'Origin': window.location.origin,
                'Authorization': 'Basic '+ btoa(username+":"+pswd_hash)
            },
            body: JSON.stringify({username,pswd_hash})
        })
        .then(response =>{
            if(response.status==200){
                return response.json();
            }else{
                // clean password input
                document.getElementById('pswd').value = "";
                // open a clean password dialog
                localStorage.setItem('openPswdDialogFlag', 'true');
                //show flask message
                $loginFlashMsg.text("Wrong Password");
                $loginFlashMsg.show();
                setTimeout(function(){
                    $loginFlashMsg.hide();
                },1500);
            }
        })
        .then(data=>{
            if(data){
                console.log("data:",data)
                //close username dialog
                loginPswdDialog.close();
            }
        })
    })
    .catch((error)=>{
        console.log("error:",error)
        $loginFlashMsg.text("There was a problem with the login process");
        $loginFlashMsg.show();
        setTimeout(function(){
        $loginFlashMsg.hide();
        },1500);
    })
};

