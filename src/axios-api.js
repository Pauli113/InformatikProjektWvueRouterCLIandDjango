import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://192.168.68.101:8000',
    timeout: 1000
})

export {
    getAPI
}