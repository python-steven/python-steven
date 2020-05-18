import { baseUrl } from './config.js';
import * as common from './common.js' //引入common
import * as db from './db.js' //引入common
// 需要登陆的，都写到这里，否则就是不需要登陆的接口
const methodsToken = [
	'PartItem',
	'MaintenanceLog',
	'ListFiltrate',
	'Filtrate',
	'MaintainFiltrate',
	'MaintainCommit',
	'MaintainList'
];

const post = (method, data, callback) => {
	uni.showLoading({
		title: '加载中'
	});

	// 判断token是否存在
	if (methodsToken.indexOf(method) >= 0) {
		// 获取用户token
		let userToken = db.get("login");
		if (!userToken) {
			 uni.showToast({
			  title: '请登录...',
			  icon: 'success',
			  duration: 2000,
			  success: function (res) {
			  // #ifdef H5 || APP-PLUS
			  uni.reLaunch({
						url: '/pages/login/login'
			  })
			  // #endif
			  // #ifdef MP-WEIXIN || MP-ALIPAY	
				uni.reLaunch({
						url: '/pages/login/login',
						animationType: 'pop-in',
						animationDuration: 200
				});
			  // #endif
			  }
			})
			return false;
		} 
	}
	
	uni.request({
		url: baseUrl+'/webapp/'+ method + '/',
		data: data,
		header: {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			// 'Content-Type': 'application/x-www-form-urlencoded', //自定义请求头信息
		},
		method: 'POST',
		success: (response) => {
			uni.hideLoading();
			const result = response.data
			// console.log(result)
			callback(result);
		},
		fail: (error) => {
			uni.hideLoading();
			if (error && error.response) {
				showError(error.response);
			}
		},
	});
	
}

const get = (method,url, callback) => {
	
	// 判断token是否存在
	if (methodsToken.indexOf(method) >= 0) {
		// 获取用户token
		let userToken = db.get("login");
		if (!userToken) {
			uni.showToast({
			  title: '请登录...',
			  icon: 'success',
			  duration: 2000,
			  success: function (res) {
			  // #ifdef H5 || APP-PLUS
			  uni.reLaunch({
						url: '/pages/login/login'
			  })
			  // #endif
			  // #ifdef MP-WEIXIN || MP-ALIPAY	
				uni.reLaunch({
						url: '/pages/login/login',
						animationType: 'pop-in',
						animationDuration: 200
				});
			  // #endif
			  }
			})
			return false;
		} 
	}
	uni.showLoading({
		title: '加载中'
	});
	uni.request({
		url: url,
		header: {
			'Accept': 'application/json',
			'Content-Type': 'application/x-www-form-urlencoded', //自定义请求头信息
		},
		method: 'GET',
		success: (response) => {
			callback(response.data);
		},
		fail: (error) => {
			if (error && error.response) {
				showError(error.response);
			}
		},
		complete: () => {
			setTimeout(function () {
				uni.hideLoading();
			}, 250);
		}
	});
}

const showError = error => {
	let errorMsg = ''
	switch (error.status) {
		case 400:
			errorMsg = '请求参数错误'
			break
		case 401:
			errorMsg = '未授权，请登录'
			break
		case 403:
			errorMsg = '跨域拒绝访问'
			break
		case 404:
			errorMsg = `请求地址出错: ${error.config.url}`
			break
		case 408:
			errorMsg = '请求超时'
			break
		case 500:
			errorMsg = '服务器内部错误'
			break
		case 501:
			errorMsg = '服务未实现'
			break
		case 502:
			errorMsg = '网关错误'
			break
		case 503:
			errorMsg = '服务不可用'
			break
		case 504:
			errorMsg = '网关超时'
			break
		case 505:
			errorMsg = 'HTTP版本不受支持'
			break
		default:
			errorMsg = error.msg
			break
	}

	uni.showToast({
		title: errorMsg,
		icon: 'none',
		duration: 2000
	});
}

// 文件上传
export const uploadFiles = (callback) => {
	uni.chooseImage({
		success: (chooseImageRes) => {
			uni.showLoading({
				title: '上传中...'
			});
			const tempFilePaths = chooseImageRes.tempFilePaths;
			const uploadTask = uni.uploadFile({
				url: baseUrl + 'api.html', //仅为示例，非真实的接口地址
				filePath: tempFilePaths[0],
				fileType: 'image',
				name: 'file',
				headers: {
					'Accept': 'application/json',
					'Content-Type': 'multipart/form-data',
				},
				formData: {
						'method': 'images.upload',
						'upfile': tempFilePaths[0]
				},
				success: (uploadFileRes) => {
						callback(JSON.parse(uploadFileRes.data));
				},
				fail: (error) => {
					if (error && error.response) {
						showError(error.response);
					}
				},
				complete: () => {
					setTimeout(function () {
						uni.hideLoading();
					}, 250);
				}
			});
// 					uploadTask.onProgressUpdate((res) => {
//             console.log('上传进度' + res.progress);
//             console.log('已经上传的数据长度' + res.totalBytesSent);
//             console.log('预期需要上传的数据总长度' + res.totalBytesExpectedToSend);
//
//             // 测试条件，取消上传任务。
//             if (res.progress > 50) {
//                 uploadTask.abort();
//             }
// 					});
		}
	});
}

// 上传图片
export const uploadImage = (num, callback) => {
	uni.chooseImage({
		count:num,
		success: (res) => {
			uni.showLoading({
				title: '上传中...'
			});
			let tempFilePaths = res.tempFilePaths
			for (var i = 0; i < tempFilePaths.length; i++) {
				uni.uploadFile({
					url: baseUrl + 'api.html',
					filePath: tempFilePaths[i],
					fileType: 'image',
					name: 'file',
					headers: {
						'Accept': 'application/json',
						'Content-Type': 'multipart/form-data',
					},
					formData: {
						'method': 'images.upload',
						'upfile': tempFilePaths[i]
					},
					success: (uploadFileRes) => {
						callback(JSON.parse(uploadFileRes.data));
					},
					fail: (error) => {
						if (error && error.response) {
							showError(error.response);
						}
					},
					complete: () => {
						setTimeout(function () {
							uni.hideLoading();
						}, 250);
					},
				});
			}
		}
	});
}

// 设置登录
export const Login = (data, callback) => post('login', data, callback);


//设备列表 获取
export const getEqu = (callback) => get('PartItem',baseUrl + '/webapp/PartItem/', callback);
//设备列表筛选
export const ListFiltrate = (data, callback) => post('ListFiltrate', data, callback);



//设备保养列表默认获取当前用户的数据的列表
export const MaintainList = (data, callback) => post('MaintainList', data, callback);
//设备保养筛选 出来的数据
export const Filtrate = (data, callback) => post('Filtrate', data, callback);
//设备保养动作
export const MaintainCommit = (data, callback) => post('MaintainCommit', data, callback);




// 保养记录的获取
// export const MaintenanceLog = (callback) => get('MaintenanceLog',baseUrl + '/webapp/MaintenanceLog/', callback);




// //设备保养记录
export const MaintainFiltrate = (data, callback) => post('MaintainFiltrate', data, callback);