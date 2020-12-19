import {request} from '@/utils/myrequest'

// http://duing.site:8888/getScrollImg

export function getMVPPlayerVS() {
    return request({
      url: '/getMVPRecentVS',
      method: 'get'
    })
}