// first login dialog variables
const loginButton = document.getElementById('loginButton');
const loginDialog = document.getElementById('loginDialog');
const closeButton = document.getElementById('closeButton');

// login variables
//let $loginMsgs = $('#loginStatusMsgs');


//string format function
String.prototype.format = function () {
    var i = 0, args = arguments;
    return this.replace(/{}/g, function () {
      return typeof args[i] != 'undefined' ? args[i++] : '';
    });
  };


//check dialog status
function checkDialog(loginDialog){
    if(loginDialog.open){
        console.log("login Dialog Open")
    }
    else{
        console.log("login Dialog closed")
    }
};
//open login dialog (username verification)
if (loginButton){
    loginButton.addEventListener("click",()=>{
        localStorage.setItem('openDialogFlag', 'true');
    });
}
//keep dialog open
function loginDialogOpen(){
    let status = localStorage.getItem('openDialogFlag');
    if (status ==='true'){
        loginDialog.showModal();
        checkDialog(loginDialog);
        localStorage.setItem('openDialogFlag','false');
    }
};
// open login dialog with button 
loginDialogOpen();

//close the login dialog
if (closeButton){
    closeButton.addEventListener("click",()=>{
        localStorage.setItem('openDialogFlag','false');
        loginDialog.close();
        checkDialog(loginDialog);
    });
}

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
            console.log("good")
            loginDialog.close()
        }
        else{
            document.getElementById('username_or_email').value = "";
            localStorage.setItem('openDialogFlag', 'true');
            console.log(data.message)
            $('#loginStatusMsgs').append('<div class="alert">{}</div>'.format(data.message))
            setTimeout(()=>{
                $('#loginStatusMsgs').remove();
            },2000);

        }
    })
}

