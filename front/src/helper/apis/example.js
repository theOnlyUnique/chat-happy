import $ajax from '../ajax'

/**
 * @desc 在实际开发中，您可以将 baseUrl 替换为您的请求地址前缀；
 * 备注：如果您不需要发起请求，删除 apis 目录，以及 app.ux 中引用即可；
 */
const baseUrl = 'https://api.exampel.com/'

export function getApi(data) {
  return $ajax.get(`${baseUrl}your-project-api`, data)
} 

export function postOtherApi(data) {
  return $ajax.post(`${baseUrl}your-project-api`, data)
}