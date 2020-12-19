import {request} from '@/utils/myrequest'

// http://duing.site:8888/getScrollImg

export function getTopChart(types,order) {
    return request({
      url: '/getChartTop10',
      method: 'get',
      params:{
        types,
        order,
      }
    })
}

// yearData:{
//     year: ['16-17', '17-18', '18-19', '19-20'],
//     getScore:[1111,1,1,1,,1],
//     totalHit:[1,1,21,2,1]
//     threeHit:[11,1,2,12,1],
// }