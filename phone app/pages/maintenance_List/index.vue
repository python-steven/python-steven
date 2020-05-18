<template>
	<view class="content" style="padding-top: 10upx;">
		<view v-if="maintenanceList.length>0">
			<view v-for="(item, index) in maintenanceList" :key="index" >
				<view class="img-list-item">
					<view class="flex-col">
						<view class="flex-row">
							<!-- <view class="flex-col flex-grow-1"> -->
							<view class="flex-grow-1 flex-left" style="width:50%" >
								<view class="fs-sf item-p">
									<view class="flex-row">
										<view>SN:</view>
										<view>{{item.SN}}</view>
									</view>
									<view class="flex-row">
										<view>STATUS:</view>
										<view>{{item.Status}}</view>
									</view>
									<view class="flex-row">
										<view>CONTENT:</view>
										<view>{{item.Content}}</view>
									</view>
								</view>
							</view>
							
							<!-- <view class="flex-col flex-grow-1 flex-left"> -->
							<view class="flex-grow-1 flex-left" style="width:50%" >
								<view class="fs-sf item-p">
									<view class="flex-row">
										<view>PN:</view>
										<view>{{item.PN}}</view>
									</view>
									<view class="flex-row">
										<view>保养人:</view>
										<view>{{item.Operator}}</view>
									</view>
									<view class="flex-row">
										<view>DATE:</view>
										<view>{{item.MaintenanceDate}}</view>
									</view>
								</view>
							</view>
						</view>
						<view class="flex-row fs-sf item-p">
							<view>SPEC:</view>
							<view>{{item.Spec}}</view>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				maintenanceList:[],
			}
		},
		onShow: function () {
			const app = getApp().globalData;
			if(app.recordType == '1'){
				this.SelectRecordData()
			}else{
				this.GetRecordData()
			}
		
		},
		onLoad: function(options) {
		},
		//筛选页面跳转
		onNavigationBarButtonTap(e) {
			console.log("debug");
			uni.navigateTo({
				url: '/pages/choose/record',
				animationType: 'pop-in',
			});
		},
		methods: {
			//获取所有设备保养记录
			GetRecordData() {
				const data = {
					start_time: '',
					end_time: '',
					sn:'',
					pn: '',
					part_name: '',
					operator: ''
				}
				this.$api.MaintainFiltrate(data,res => {
					if(res.data == 'error'){
						console.log(res.message);
						uni.showToast({
						    icon: 'none',
						    title: res.message
						});
					}else{
						this.maintenanceList = res.data;
						}
					
				});
			},
			//获取筛选后符合条件的设备保养记录
			SelectRecordData(){
				const _app = getApp().globalData;
				var str = _app.recordString.split(',');
				const data = {
					start_time: str[0],
					end_time: str[1],
					sn:str[2],
					pn: str[3],
					part_name: str[4],
					operator: str[5]
				}
				console.log(str[0]+str[1]+str[2]+str[3]+str[4]+str[5]);
				this.$api.MaintainFiltrate(data,res => {
					if(res.data == 'error'){
						console.log(res.message);
						uni.showToast({
						    icon: 'none',
						    title: res.message
						});
					}
					else{
						this.maintenanceList = res.data;
						console.log(res.data)
					}
						
					
				});
			}
		},
		
	}
</script>

<style>
.row-space-1{
	padding-left:135upx;
}
.img-list-item{ 
	width:100%;
	margin: 10upx 2upx;
	border-radius: 10upx;
	box-shadow: 2px 2px 5px #000000;
}
.item-p{
	padding: 3upx 10upx 3upx 10upx;
}
</style>
