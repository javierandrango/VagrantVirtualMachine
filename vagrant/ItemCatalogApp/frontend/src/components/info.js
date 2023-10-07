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
    const baseUrl = window.location.origin; // get the base URL (https://localhost:80000)
    $(function () {
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
                console.log("response ok")
                window.location.href = `${baseUrl}/`
                
            }
            else{
                console.log("request failed with status:", response.status)
            }
        })
        .catch(error=>{
            console.log("error:",error)
        })
    });
    
};