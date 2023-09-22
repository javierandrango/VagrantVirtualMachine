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
    const $loginFlashMsg = $('#loginStatusMsgs'); //to add flash messages
    const username_or_email = document.getElementById('username_or_email').value;
    fetch('/login/verify_username_or_email/',{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'Origin': window.location.origin,
        },
        body: JSON.stringify({ username_or_email }),
    })
    .then(response => response.json())
    .then(data=>{
        if(data.username){
            loginUserDialog.close();
            localStorage.setItem('openPswdDialogFlag', 'true');
            $username.val(data.username);
            loginPswdDialogOpen(loginPswdDialog);
        }
        else{
            document.getElementById('username_or_email').value = "";
            localStorage.setItem('openDialogFlag', 'true');
            $loginFlashMsg.text(data.message);
            $loginFlashMsg.show();
            setTimeout(function(){
                $loginFlashMsg.hide();
            },1500);
        }
    })
};
//pswd hashing
/*async function pswdHash(pswd){
    console.log("hashing pswd here")
    let salt = bcrypt.gen
    return pswd_hash
};*/
// pswd verification
document.getElementById('loginBtn').addEventListener('click', verifyPswd);
function verifyPswd(){
    const inputPswd = document.getElementById('pswd').value;
    console.log("inptu Pswd: ",inputPswd);
    const $loginFlashMsg = $('#loginStatusMsgs'); //to add flash messages
    bcrypt.genSalt(10, function(err,salt){
        if (err){
            console.log("error generating salt:",err);
        };

        bcrypt.hash(inputPswd,salt,function(err,hash){
        
            if(err){
                console.log("error hashong password: ",err)
            };

            console.log("salt: ",salt);
            console.log("hash: ",hash);
        });
    });
};

