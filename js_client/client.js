const loginForm = document.getElementById('login-form');
const searchForm = document.getElementById('search-form');

const baseEndpoint = 'http://localhost:8000/api/'
const contentContainer = document.getElementById('content-container');
if (loginForm){
    loginForm.addEventListener('submit', handleLogin)
}

if (searchForm){
    searchForm.addEventListener('submit', handleSearch)
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

function handleSearch(event){
    event.preventDefault();
    let FormData = new FormData(searchForm)
    let Data = Object.fromEntries(FormData)
    let searchParams = new URLSearchParams(Data)

    const Endpoint = '${baseEndpoint}/search/?${searchParams}'
        const authToken = localStorage.getItem('access')
        if (authToken){
            options.headers['Authorization'] = 'Bearer ' + authToken  
        }
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
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