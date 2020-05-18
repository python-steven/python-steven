<template>
	<view class="content" style="padding-top: 10upx;">
		<view class="flex-col flex-x-center">
			<view class="fs-26">
				<!-- 工号显示 -->
				<view class="flex-row cell-item">
					<view class="cell-m flex-grow-1">账号：</view>
					<view class="cell-m flex-grow-0">{{user}}</view>
				</view>
				<!-- 退出登录显示 -->
				<view class="flex-row cell-item " @click="logOff">
					<view class="cell-m flex-grow-1">退出</view>
					<image class="cell-m flex-grow-0 icon" src="../../static/img/right.png" mode="aspectFill"></image>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import { get } from '@/config/db.js';
	export default {
		data() {
			return {
				user:this.$db.get("login"),
			}
		},
		onLoad: function(options) {
		},
		methods: {
			// 退出登录
			logOff () {
				this.$common.modelShow('退出', '确认退出登录吗?', () => {
					this.$db.del('login');
					var app = getApp().globalData;
					app.type = '0';
					app.maintainType = '0';
					app.recordType = '0';
					uni.reLaunch({
						url: '/pages/login/login'
					})
				})
			}
		}
	}
</script>

<style>
.content{
	background:#FFFFFF;
	height:100%;
	width:100%;
}
.choose-c{
	width: 80%;
	margin-left: 10%;
	top: 5%;
}
.cell-m{
	padding: 25upx 0;
}
.icon{
  width: 50upx;
  height: 50upx;
  /* #ifdef MP-ALIPAY */
  background-size: 100% 100%;
  /* #endif */
}
</style>
