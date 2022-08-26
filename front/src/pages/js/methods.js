export var BASE_URL = 'http://127.0.0.1:8000/'
export var headers =  {
              Authorization: `Token ${sessionStorage.getItem('token')}`
            }