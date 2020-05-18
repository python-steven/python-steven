<template>
	<view class="content" style="padding-top: 10upx;">
		<view v-if="EqumList.length>0">
			<view v-for="(item, index) in EqumList" :key="index" >
				<view class="img-list-item">
					<view class="flex-col">
						<view class="flex-row">
							<!-- <view class="flex-col flex-grow-1 flex-left"> -->
							<view class="flex-grow-1 flex-left" style="width:50%" >
								<view class="fs-sm item-p">
									<!-- 显示SN信息 -->
									<view class="flex-row">
										<view>SN:</view>
										<view>{{item.SN}}</view>
									</view>
									<!-- 显示保养周期（按次数） -->
									<view class="flex-row">
										<view>保养周期(按次数):</view>
										<view>{{item.CheckCycleCount}}</view>
									</view>
									<!-- 显示已使用次数 -->
									<view class="flex-row">
										<view>已使用次数:</view>
										<view>{{item.UsedTimes}}</view>
									</view>
									<!-- 显示保养人信息 -->
									<view class="flex-row">
										<view>保养人:</view>
										<view>{{item.Maintainer}}</view>
									</view>
								</view>
							</view>
							<!-- <view class="flex-col flex-grow-1 flex-left"> -->
							<view class="flex-grow-1 flex-left" style="width:50%" >
								<view class="fs-sm item-p">
									<!-- 显示PN -->
									<view class="flex-row">
										<view>PN:</view>
										<view>{{item.PN}}</view>
									</view>
									<!-- 显示品名 -->
									<!-- <view class="flex-row">
										<view>品名:</view>
										<view>{{item.PartName}}</view>
									</view> -->
									<!-- 显示保养周期(按时间) -->
									<view class="flex-row">
										<view>保养周期(按时间):</view>
										<view>{{item.CheckCycle}}</view>
									</view>
									<!-- 显示下次保养时间 -->
									<view class="flex-row">
										<view>下次保养时间:</view>
										<view>{{item.NextCheckDate}}</view>	
									</view>
									<!-- 显示设备状态 -->
									<view class="flex-row">
										<view>状态:</view>
										<!-- <view>{{item.Status}}</view> -->
										<view v-if="item.status===0" class="status-border-green">{{item.Status}}</view>
										<view v-else-if="item.status===1" class="status-border-yellow">{{item.Status}}</view>
										<view v-else-if="item.status===2" class="status-border-red">{{item.Status}}</view>
										<view v-else-if="item.status===3" class="status-border-info">{{item.Status}}</view>
									</view>
								</view>
							</view>
						</view>
						<view class="fs-sm item-partname">
							<!-- 显示品名 -->
							<view class="flex-row">
								<view>PartName:</view>
								<view>{{item.PartName}}</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import Vue from 'vue' 
	import uniSegmentedControl from "@/components/uni-segmented-control/uni-segmented-control.vue"
	export default {
		components: {uniSegmentedControl},
		data() {
			return {
				starttime: '请选择',
				endtime: '请选择',
				EqumList:[],
				status:0,
			}
		},
		//切换到筛选页面
		onNavigationBarButtonTap(e) {
			uni.navigateTo({
				url: '/pages/choose/index',
				animationType: 'pop-in',
			});
		},
		computed: {
		    startDate() {
		        return this.getDate('start');
		    },
		    endDate() {
		        return this.getDate('end');
		    }
		},
		onLoad: function (option) {	
			
		},
		onShow: function () {
			const app = getApp().globalData;
			if(app.type =='1'){
				this.GetSelectEquData();
			}
			if(app.type =='0'){
				console.log("debug1");
				this.GetAllEquData();
			}
		},
		mounted() {
			// #ifdef H5 
			window.addEventListener('scroll', this.handleScroll)
			// #endif
		},
		methods: {
			//显示符合筛选条件的设备数据
			GetSelectEquData(){
				const _app = getApp().globalData;
				var str = _app.chooseString.split(',');
				const data = {
					start_time: str[0],
					end_time: str[1],
					sn:str[2],
					part_name: str[3],
					maintainer: str[4]
				};
				console.log(str[0]+str[1]+str[2]+str[3]+str[4]);
				this.$api.ListFiltrate(data,res => {
					this.EqumList = res.data;
					console.log(res.data);
					this.EqumList.forEach(item => {
						console.log(item.Status);
						Vue.set(item,'status',0); 
						if(item.Status == 'WARNING'){
							item.Status = '预警';
							item.status = 1;
						}
						else if(item.Status == 'NORMAL'){
							item.Status = '正常';
							item.status = 0;
						}
						else if(item.Status == 'OVERPROOF'){
							item.Status = '超标';
							item.status = 2;
						}
						else if(item.Status == 'none'){
							item.Status = '未设定';
							item.status = 3;
						}
					});
				});
			},
			//显示一周内所有的设备数据
			GetAllEquData() {
				this.$api.getEqu(res => {
					this.EqumList = res.data;
					console.log(res.data);
					this.EqumList.forEach(item => {
						// console.log(item.Status);
						Vue.set(item,'status',0); 
						if(item.Status == 'WARNING'){
							item.Status = '预警';
							item.status = 1;
						}
						else if(item.Status == 'NORMAL'){
							item.Status = '正常';
							item.status = 0;
						}
						else if(item.Status == 'OVERPROOF'){
							item.Status = '超标';
							item.status = 2;
						}
						else if(item.Status == 'none'){
							item.Status = '未设定';
							item.status = 3;
						}
					});
				});
				
			},
			getDate(type) {
			    const date = new Date();
			    let year = date.getFullYear();
			    let month = date.getMonth() + 1;
			    let day = date.getDate();
			
			    if (type === 'start') {
			        year = year - 60;
			    } else if (type === 'end') {
			        year = year + 2;
			    }
			    month = month > 9 ? month : '0' + month;;
			    day = day > 9 ? day : '0' + day;
			    return `${year}-${month}-${day}`;
			},
			
			handleScroll() {
				var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
				// console.log(scrollTop)
				// var offsetTop = document.querySelector('#searchBar').offsetTop
				scrollTop > 50 ? this.searchBarOpacity = true : this.searchBarOpacity = false
			},
			destroyed() {
				window.removeEventListener('scroll', this.handleScroll)
			},
			onPullDownRefresh() {
				this.initData();
				//this.$db.del('all_cat');
				uni.stopPullDownRefresh();
			},

		}
	}
</script>

<style>
	.content{
		background:#FFFFFF;
		width:100%;
		height:100%;
	}
	.item-p{
		padding: 5upx 20upx 5upx 20upx;
	}
	.top{
		margin: 10upx 0upx 0 0upx;
	}
	.img-list-item{ 
		width:100%;
		margin: 10upx 2upx;
		border-radius: 10upx;
		box-shadow: 2px 2px 5px #000000;
	}
	.cell-m{
		padding: 25upx 0;
	}
	.border-m{
		border-bottom: 2upx solid #ffffff;
	}
	.cell-item-ft{
	  display: inline-block;
	  position: relative;
	  /* top: 5%; */
	  right: 26upx;
	  transform: translateY(-50%);
	  overflow: hidden;
	}
	.btn{
		width: 100%;
		height:100upx;
	}
	.btn-s{
		width:45%;
	}
	.btn-ok-c{
		margin:0;
		padding:0;
		display: inline-block;
		position: relative;
		text-align: center;
		height: 100%;
		width: 45%;
		float: left;
		font-size: 22upx;
		color: #666;
	}
	.cart-bottom {
		/*  #ifdef  H5  */
		bottom: 50px;
		/*  #endif  */
		/*  #ifndef  H5  */
		bottom: 0;
		/*  #endif  */
		z-index: 99;
		height: 90upx;
		width: 100%;
		/* background-color: #fff; */
		position: fixed;
		
		overflow: hidden;
	/* box-shadow: 0 0 20upx #ccc; */
	}
	.btn-cancel-c{
		display: inline-block;
		position: relative;
		text-align: center;
		float:left;
		left:50%;
		height: 100%;
		width: 45%;
		font-size: 22upx;
		color: #666;
	}
	.status-border-green{
		border: 2upx solid #28a745;
		background:#28a745;
		color:#FFFFFF;
	}
	.status-border-yellow{
		border: 2upx solid #FFFF00;
		background:#FFFF00;
		color:#000;
	}
	.status-border-red{
		border: 2upx solid #FF0000;
		background:#FF0000;
		color:#FFFFFF;
	}
	.status-border-info{
		border: 2upx solid #17a2b8;
		background:#17a2b8;
		color:#FFFFFF;
	}
	.item-partname{
		padding: 0upx 20upx;
	}
</style>
