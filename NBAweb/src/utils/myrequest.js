import axios from 'axios'

export function request(config){
    //1.创建axios实例
    const instance = axios.create({
        baseURL:"http://duing.site:8888",
        timeout:5000
    })

    //2.axios拦截器
    //请求拦截器
    instance.interceptors.request.use(config=>{
        // console.log(config);//成功拦截config
        //使用情形
        //1.拦截监测config中的信息是否符合服务器的要求
        //2.发送请求时，希望在界面显示一些请求的图标
        //3.某些网络请求比如登录，用于监测该请求是否携带了jwt的token令牌
        return config 
        //如果拦截下来以后不把config返回出去的话，那么这个请求就无法请求到
        //必须返回才能使得下面的请求得以执行,否则这个config就会出现error,在request函数外执行promise的catch
    },err=>{
        // console.log(err);//失败拦截
    })


    //响应拦截器
    instance.interceptors.response.use(res=>{
        // console.log(res)
        return res.data //结果需要返回
    },err=>{
        // console.log(err)
    })
    return instance(config)
}