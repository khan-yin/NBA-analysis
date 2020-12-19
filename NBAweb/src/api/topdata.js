import {request} from '@/utils/myrequest'

// request({
//   url:"/home/multidata"
// }).then(res =>{
//   console.log(res);
// }).catch(err =>{
//   console.log(err);
// })

export function getTopRank(type,order) {
    return request({
      url: '/getTeamData',
      method: 'get',
      params: { 
        type,
        order
      }
    })
}