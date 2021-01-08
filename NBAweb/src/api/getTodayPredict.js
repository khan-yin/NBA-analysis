import {request} from '@/utils/myrequest'

// http://duing.site:8888/getEastAndWest?part=west

export function getTodayPredict() {
    return request({
      url: '/getTodayMatch',
      method: 'get',
    })
}
// http://duing.site:8888/getTodayMatch
