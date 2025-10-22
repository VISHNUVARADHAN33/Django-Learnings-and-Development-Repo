const loginForm = document.getElementById('login-form');
const baseEndpoint = 'http://localhost:8000/api/'
const contentContainer = document.getElementById('content-container');
if (loginForm){
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event){
    console.log(event)
    event.preventDefault();
    const loginEndpoint = '${baseEndpoint}/token/'
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodystr = JSON.stringify(loginObjectData)
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: bodystr                            //nothing is post yet
    }
fetch(loginEndpoint, options)      
}

function handleAuthData(authData){ 
    localStorage.setItem('access', authData.access)   
    localStorage.setItem('refresh', authData.refresh) 
}

function writeToContainter(data){
    if (contentContainer){
        contentContainer.innerHTML = '<pre>' + JSON.stringify(data) + '</pre>'
}}

function getFetchaOptions(method){
    return{
        method: method === null ? 'GET' : method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('access')
        },
        body: body? body : null 
    }
}
function getProtectedList(){
    const endpoint = '${baseEndpoint}/products/'
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    }
fetch(endpoint, options)
.then(response => response.json())
.then(data => {
    writeToContainter(data)
    console.log(data)
})
}