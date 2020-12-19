import {request} from '@/utils/myrequest'

// http://duing.site:8888/getMVPData?types=normal&order=gaimao



export function getMVPCareer() {
    return request({
      url: '/getMVPCareer',
      method: 'get',
      params:{
        types:"normal"
      }
    })
}