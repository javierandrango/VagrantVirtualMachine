/**
 * MODULES
 */
import $ from 'jquery';

/**
 * VARIABLES
 */


/**
 * HANDLING EVENTS
 */

/**
 * USER DEFINED FUNCTIONS
 */

export function user_info(token){
    //active account header tags
    const $img = $('.img-blank-user'); //to update the user image
    const $username = $('#active-username'); //to update active username
    const $email = $('#active-email'); //to update active email

    fetch('/login/user_info/',{
        method: 'GET',
        credentials:'include',
        headers:{
            'Content-Type': 'application/json',
            "Authorization": "Bearer "+token
        },
    })
    .then(response=>{
        if(response.status==200){
            return response.json();
        }
    })
    .then(data=>{
        //console.log("user_info:",data)
        //update user photo
        $img.attr("src",data.picture);
        //update user username
        $username.text(data.username);
        //update user email
        $email.text(data.email);
    })
    .catch(error=>{
        console.log("error:",error)
    })
};