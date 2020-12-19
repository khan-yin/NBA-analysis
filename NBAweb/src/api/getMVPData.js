import {request} from '@/utils/myrequest'

// http://duing.site:8888/getMVPData?types=normal&order=gaimao



export function getMVPData(types,order) {
    return request({
      url: '/getMVPData',
      method: 'get',
      params: { 
        types,
        order
      }
    })
}