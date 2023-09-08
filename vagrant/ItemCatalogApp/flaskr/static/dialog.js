const loginButton = document.getElementById('loginButton');
const loginDialog = document.getElementById('loginDialog');
const closeButton = document.getElementById('closeButton');

//check dialog status
function checkDialog(loginDialog){
    if(loginDialog.open){
        console.log("login Dialog Open")
    }
    else{
        console.log("login Dialog closed")
    }
};

//
if (loginButton){
    loginButton.addEventListener("click",()=>{
        localStorage.setItem('openDialogFlag', 'true');
        window.location.href = '/login';
    });
}


var openDialogFlag = localStorage.getItem('openDialogFlag');
if (openDialogFlag === 'true') {
    loginDialog.showModal();
    checkDialog(loginDialog);
    localStorage.setItem('openDialogFlag', 'false');
};
//show the login dialog
//loginButton.addEventListener("click",()=>{
//    loginDialog.showModal();
//    checkDialog(loginDialog)
//});

//close the login dialog
if (closeButton){
    closeButton.addEventListener("click",()=>{
        loginDialog.close();
        checkDialog(loginDialog);
    });
}


