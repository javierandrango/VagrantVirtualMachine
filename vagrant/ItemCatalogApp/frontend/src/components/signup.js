/**
 * ----- MODULES -----
 */
import $ from 'jquery';
let bcrypt = require('bcryptjs');

/**
 * ----- VARIABLES -----
 */
//create account dialog
let signUpHeaderBtn = document.getElementById('signUpButton');
let closeDialogBtn = document.getElementById('closeDialogBtn');
let nextDialogBtn1 = document.getElementById('nextDialogBtn1');
//agree terms dialog
let returnBtn1 = document.getElementById('returnBtn1');
let signUpBtn = document.getElementById('signUpBtn');
//email code dialog
let returnBtn2 = document.getElementById('returnBtn2');
let nextDialogBtn2 = document.getElementById('nextDialogBtn2');
//new password dialog
let nextDialogBtn3 = document.getElementById('nextDialogBtn3');
//new user image dialog
let skipBtn = document.getElementById('skipBtn')
//dialog dictionary
let dialog = {
    1:'createAccountDialog',
    2:'agreeTermsDialog',
    3:'emailCodeDialog',
    4:'newPasswordDialog',
    5:'newUserImageDialog',
};
/**
 * ----- HANDLING EVENTS -----
 */
//open create account dialog
if(signUpHeaderBtn){
    signUpHeaderBtn.addEventListener("click",()=>{
        localStorage.setItem(`${dialog[1]}Flag`,'true');
    });
};
if(document.getElementById(dialog[1])){
    dialogOpen(dialog[1]);
};
// close create account dialog
if(closeDialogBtn){
    closeDialogBtn.addEventListener("click",()=>{
        dialogClose(dialog[1]);
    });
};
//open agree terms dialog dialog
if(nextDialogBtn1){
    nextDialogBtn1.addEventListener("click",()=>{
        //localStorage.setItem(`${dialog[2]}Flag`,'true');
        //dialogClose(dialog[1]);
        //dialogOpen(dialog[2]);
        checkNewUser();
    });
};
//return to create account dialog
if(returnBtn1){
    returnBtn1.addEventListener("click",()=>{
        localStorage.setItem(`${dialog[1]}Flag`,'true');
        dialogClose(dialog[2]);
        dialogOpen(dialog[1]);
    });
};
//open email code dialog
if (signUpBtn){
    signUpBtn.addEventListener("click",()=>{
        //localStorage.setItem(`${dialog[3]}Flag`,'true');
        //dialogClose(dialog[2]);
        //dialogOpen(dialog[3]);
        saveNewUser();
    });
};
//return to agree terms dialog
if (returnBtn2){
    returnBtn2.addEventListener("click",()=>{
        localStorage.setItem(`${dialog[2]}Flag`,'true');
        dialogClose(dialog[3]);
        dialogOpen(dialog[2]);
    });
};
//open new password dialog
if(nextDialogBtn2){
    nextDialogBtn2.addEventListener("click",()=>{
        localStorage.setItem(`${dialog[4]}Flag`,'true');
        dialogClose(dialog[3]);
        dialogOpen(dialog[4]);
    });
};
//open new user image dialog
if (nextDialogBtn3){
    nextDialogBtn3.addEventListener("click",()=>{
        localStorage.setItem(`${dialog[5]}Flag`,'true');
        dialogClose(dialog[4]);
        dialogOpen(dialog[5]);
    });
}
//close new user image dialog
if (skipBtn){
    skipBtn.addEventListener("click",()=>{
        dialogClose(dialog[5]);
    });
}
/**
 * ----- USER DEFINED FUNCTIONS -----
 */
//keep dialog open
function dialogOpen(dialogName){
    console.log("dialog open:",dialogName);
    const dialog = document.getElementById(dialogName);
    var status = localStorage.getItem(`${dialogName}Flag`);
    if (status === 'true'){
        dialog.showModal();
        localStorage.setItem(`${dialogName}Flag`,'false');
    }
};
//close dialog
function dialogClose(dialogName){
    console.log("dialog close:",dialogName);
    const dialog = document.getElementById(dialogName);
    dialog.close();
};
//handling new username and password
function checkNewUser(){
    const $newUsername = $('#inputUsername'); //input username in create account dialog
    const $newEmail = $('#inputEmail'); //input email in create account dialog
    const $checkedUsername = $('#checkedUsername') //to show the new registered username
    const $checkedEmail = $('#checkedEmail')//to show the new  registered email
    const $signUpStatusMsgs = $('#signUpStatusMsgs'); //to add flash messages

    fetch('/signup/verify-new-user/',{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'Origin': window.location.origin,
        },
        body: JSON.stringify({email:$newEmail.val(),}),
    })
    .then(response => response.json())
    .then(data=>{
        //console.log("data from response:",data);
        if(!data.email_msg){
            $checkedUsername.val($newUsername.val());
            $checkedEmail.val($newEmail.val());
            localStorage.setItem(`${dialog[2]}Flag`,'true');
            dialogClose(dialog[1]);
            dialogOpen(dialog[2]);
        }else{
            // clear email input
            //document.getElementById('inputEmail').value = "";
            $newEmail.val("");
            // open a clean create account dialog
            localStorage.setItem(`${dialog[1]}Flag`,'true');
            //show flask message
            $signUpStatusMsgs.text(data.email_msg);
            $signUpStatusMsgs.show();
            setTimeout(function(){
                $signUpStatusMsgs.hide();
            },1500);
        }
    })
    .catch((error)=>{
        console.log("error:",error);
        $signUpStatusMsgs.text("There was a problem with the sign-up process");
        $signUpStatusMsgs.show();
        setTimeout(function(){
            $signUpStatusMsgs.hide();
        },1500);
    })
}
//save new user in database
function saveNewUser(){
    const $checkedUsername = $('#checkedUsername') //to show the new registered username
    const $checkedEmail = $('#checkedEmail')//to show the new  registered email
    const $signUpStatusMsgs = $('#signUpStatusMsgs'); //to add flash messages
    var data={
        'completed_form': false,
        'new_username': $checkedUsername.val(),
        'new_email': $checkedEmail.val(),
    }
    fetch('/signup/newuser',{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'Origin': window.location.origin,
        },
        body: JSON.stringify(data),
    })
    .then(response=>{
        if(response.status==200){
            localStorage.setItem(`${dialog[3]}Flag`,'true');
            dialogClose(dialog[2]);
            dialogOpen(dialog[3]);
        }
        else{
            console.log("error:",error);
            $signUpStatusMsgs.text("There was a problem with the sign-up process");
            $signUpStatusMsgs.show();
            setTimeout(function(){
                $signUpStatusMsgs.hide();
            },1500);    
        }
    })
    .catch((error)=>{
        console.log("error:",error);
        $signUpStatusMsgs.text("There was a problem with the sign-up process");
        $signUpStatusMsgs.show();
        setTimeout(function(){
            $signUpStatusMsgs.hide();
        },1500);
    })
}