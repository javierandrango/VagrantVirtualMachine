/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/components/dialog.js":
/*!**********************************!*\
  !*** ./src/components/dialog.js ***!
  \**********************************/
/***/ (() => {

eval("// first login dialog variables\r\nconst loginButton = document.getElementById('loginButton');\r\nconst loginUserDialog = document.getElementById('loginUserDialog');\r\nconst loginPswdDialog = document.getElementById('loginPswdDialog');\r\n//input text id username\r\nconst $username = $('#username');\r\n//div container for flash message\r\nconst $loginFlashMsg = $('#loginStatusMsgs');\r\n\r\n\r\n//string format function\r\nString.prototype.format = function () {\r\n    var i = 0, args = arguments;\r\n    return this.replace(/{}/g, function () {\r\n      return typeof args[i] != 'undefined' ? args[i++] : '';\r\n    });\r\n  };\r\n\r\n\r\n//check dialog status\r\n/*\r\nfunction checkDialog(dialog){\r\n    if(dialog.open){\r\n        console.log(\"login Dialog Open\")\r\n    }\r\n    else{\r\n        console.log(\"login Dialog closed\")\r\n    }\r\n};\r\n*/\r\n//open login dialog (username verification)\r\nif (loginButton){\r\n    loginButton.addEventListener(\"click\",()=>{\r\n        localStorage.setItem('openDialogFlag', 'true');\r\n    });\r\n}\r\n//keep dialog open\r\nfunction loginUserDialogOpen(){\r\n    let status = localStorage.getItem('openDialogFlag');\r\n    if (status ==='true'){\r\n        loginUserDialog.showModal();\r\n        //checkDialog(loginUserDialog);\r\n        localStorage.setItem('openDialogFlag','false');\r\n    }\r\n};\r\nfunction loginPswdDialogOpen(){\r\n    let status = localStorage.getItem('openPswdDialogFlag');\r\n    if (status ==='true'){\r\n        loginPswdDialog.showModal();\r\n        localStorage.setItem('openPswdDialogFlag','false');\r\n    }\r\n};\r\n// open login dialog with button \r\nloginUserDialogOpen();\r\n\r\n//close the login dialog\r\nfunction closeDialogWithBttn(){\r\n    localStorage.setItem('openDialogFlag','false');\r\n    localStorage.setItem('openPswdDialogFlag','false');\r\n    loginUserDialog.close();\r\n    loginPswdDialog.close();\r\n};\r\n\r\n// username or email validation\r\nfunction verifyUsername(){\r\n    const username_or_email = document.getElementById('username_or_email').value;\r\n    fetch('/login/verify_username_or_email/',{\r\n        method: 'POST',\r\n        headers:{\r\n            'Content-Type': 'application/json',\r\n            'Origin': window.location.origin,\r\n        },\r\n        body: JSON.stringify({ username_or_email }),\r\n    })\r\n    .then(response => response.json())\r\n    .then(data=>{\r\n        if(data.username){\r\n            loginUserDialog.close()\r\n            localStorage.setItem('openPswdDialogFlag', 'true');\r\n            $username.val(data.username);\r\n            loginPswdDialogOpen();\r\n        }\r\n        else{\r\n            document.getElementById('username_or_email').value = \"\";\r\n            localStorage.setItem('openDialogFlag', 'true');\r\n            $loginFlashMsg.text(data.message);\r\n            $loginFlashMsg.show();\r\n            setTimeout(function(){\r\n                $loginFlashMsg.hide();\r\n            },1500);\r\n        }\r\n    })\r\n};\r\n\r\n//pswd hashing\r\nasync function pswdHash(pswd){\r\n    \r\n};\r\n// pswd verification\r\nfunction verifyPswd(){\r\n\r\n};\n\n//# sourceURL=webpack://frontend/./src/components/dialog.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/components/dialog.js"]();
/******/ 	
/******/ })()
;