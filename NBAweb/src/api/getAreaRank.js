import {request} from '@/utils/myrequest'

// http://duing.site:8888/getEastAndWest?part=west

export function getAreaRank(part) {
    return request({
      url: '/getEastAndWest',
      method: 'get',
      params: { 
        part
      }
    })
}

