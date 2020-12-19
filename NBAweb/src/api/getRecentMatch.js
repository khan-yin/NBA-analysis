import {request} from '@/utils/myrequest'

// http://duing.site:8888/getRecentMatch?startTime=2020-12-18&endTime=2020-12-25

export function getRecentMatch(startTime,endTime) {
    return request({
      url: '/getRecentMatch',
      method: 'get',
      params:{
        startTime,
        endTime
      }
    })
}