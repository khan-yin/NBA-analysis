// http://duing.site:8888/getNews
import {request} from '@/utils/myrequest'

// http://duing.site:8888/getScrollImg

export function getNews() {
    return request({
      url: '/getNews',
      method: 'get'
    })
}