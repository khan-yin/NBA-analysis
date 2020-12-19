import {request} from '@/utils/myrequest'

// http://duing.site:8888/getScrollImg

export function getScrollImg() {
    return request({
      url: '/getScrollImg',
      method: 'get'
    })
}