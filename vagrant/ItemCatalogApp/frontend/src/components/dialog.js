// first login dialog variables
const loginButton = document.getElementById('loginButton');
const loginUserDialog = document.getElementById('loginUserDialog');
const loginPswdDialog = document.getElementById('loginPswdDialog');
//input text id username
const $username = $('#username');
//div container for flash message
const $loginFlashMsg = $('#loginStatusMsgs');


//string format function
String.prototype.format = function () {
    var i = 0, args = arguments;
    return this.replace(/{}/g, function () {
      return typeof args[i] != 'undefined' ? args[i++] : '';
    });
  };


//check dialog status
/*
function checkDialog(dialog){
    if(dialog.open){
        console.log("login Dialog Open")
    }
    else{
        console.log("login Dialog closed")
    }
};
*/
//open login dialog (username verification)
if (loginButton){
    loginButton.addEventListener("click",()=>{
        localStorage.setItem('openDialogFlag', 'true');
    });
}
//keep dialog open
function loginUserDialogOpen(){
    let status = localStorage.getItem('openDialogFlag');
    if (status ==='true'){
        loginUserDialog.showModal();
        //checkDialog(loginUserDialog);
        localStorage.setItem('openDialogFlag','false');
    }
};
function loginPswdDialogOpen(){
    let status = localStorage.getItem('openPswdDialogFlag');
    if (status ==='true'){
        loginPswdDialog.showModal();
        localStorage.setItem('openPswdDialogFlag','false');
    }
};
// open login dialog with button 
loginUserDialogOpen();

//close the login dialog
function closeDialogWithBttn(){
    localStorage.setItem('openDialogFlag','false');
    localStorage.setItem('openPswdDialogFlag','false');
    loginUserDialog.close();
    loginPswdDialog.close();
};

// username or email validation
function verifyUsername(){
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
            loginUserDialog.close()
            localStorage.setItem('openPswdDialogFlag', 'true');
            $username.val(data.username);
            loginPswdDialogOpen();
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
async function pswdHash(pswd){
    
};
// pswd verification
function verifyPswd(){

};