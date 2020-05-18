<template>
	<view class="content cell-group">
		<view class="flex-col">
			<!-- 开始时间选择 -->
			<view class="cell-item flex-row flex-y-center">
				<view class="flex-grow-0">
					<view class='cell-left-title'>开始时间</view>
				</view>
				<view class="flex-grow-1">
					<view class="cell-left-title cell-padding">
						<picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindStartDateChange">
							<view class="uni-input">{{starttime}}</view>
						</picker>
					</view>
				</view>
			</view>
			<!-- 截止时间选择 -->
			<view class="cell-item flex-row flex-y-center">
				<view class="flex-grow-0">
					<view class='cell-left-title'>截止时间</view>
				</view>
				<view class="flex-grow-1">
					<view class="cell-left-title cell-padding">
						<picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindEndDateChange">
							<view class="uni-input">{{endtime}}</view>
						</picker>
					</view>
				</view>
			</view>
			<!-- SN输入 -->
			<view class="cell-item flex-row flex-y-center">
				<!-- #ifdef H5 -->
				<view class="flex-grow-0">
					<view class='cell-left-title'>SN</view>
				</view>
				<view class="flex-grow-1">
					<input class='cell-left-title cell-sn-space' placeholder='请输入SN' v-model="sn" type="inputType"></input>
				</view>
				<!-- #endif -->
				<!-- #ifndef H5 -->
				<view class="flex-grow-0">
					<view class='cell-left-title'>SN</view>
				</view>
				<view class="flex-grow-1">
					<view class="flex-row">
						<input class='cell-left-title cell-sn-space' placeholder='请输入SN' v-model="sn" type="inputType"></input>
						<image src="../../static/img/ewm.png" class="icon" mode="aspectFill" @click="scanCode"></image>
					</view>
				</view>
				<!-- #endif -->
			</view>
			<!-- PN输入 -->
			<view class="cell-item flex-row flex-y-center">
				<view class="flex-grow-0">
					<view class='cell-left-title'>PN</view>
				</view>
				<view class="flex-grow-1">
					<input class='cell-left-title cell-sn-space' placeholder='请输入PN' v-model="pn" type="inputType"></input>
				</view>
			</view>
			<!-- 输入品名 -->
			<view class="cell-item flex-row flex-y-center">
				<view class="flex-grow-0">
					<view class='cell-left-title'>品名</view>
				</view>
				<view class="flex-grow-1">
					<input class='cell-left-title cell-pm-space' placeholder='请输入品名' v-model="pm" type="inputType"></input>
				</view>
			</view>
			<!-- 输入保养人 -->
			<view class="cell-item flex-row flex-y-center">
				<view class="flex-grow-0">
					<view class='cell-left-title'>保养人</view>
				</view>
				<view class="flex-grow-1">
					<input class='cell-left-title cell-maintainer-space' placeholder='请输入保养人' v-model="maintainer" type="inputType"></input>
				</view>
			</view>
		</view>
		<view class="cart-bottom">
			<button class='btn btn-square btn-b btn-all' hover-class="btn-hover2" @click="chooseOK()">筛选</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				date:'',
				starttime:'请选择',
				endtime:'请选择',
				sn:'',
				pn:'',
				pm:'',
				maintainer:''
			}
		},
		computed: {
		    startDate() {
		       return this.getDate('start');
		    },
		    endDate() {
		       return this.getDate('end');
		    }
		},
		methods: {
			//获取开始时间
			bindStartDateChange: function(e) {
				this.starttime = e.target.value;
			},
			//获取截止时间
			bindEndDateChange: function(e) {
				this.endtime = e.target.value;
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
			//筛选
			chooseOK(){
				if(this.starttime == '请选择'){
					this.starttime =''
				}
				if(this.endtime == '请选择'){
					this.endtime =''
				}
				getApp().globalData.recordType = '1';
				getApp().globalData.recordString = this.starttime + ',' + this.endtime + ',' + this.sn + ',' + this.pn + ',' + this.pm + ',' + this.maintainer;
				uni.switchTab({
					url: '/pages/maintenance_List/index'
				})
			},
			scanCode() {
				uni.scanCode({
					success(res) {
						this.sn = res.result;
					},
					// complete(res){
					// 	console.log(3);
					// 	console.log(res)
					// },
					fail(res) {
						uni.showToast({
						    icon: 'none',
						    title: res
						});
						console.log(res)
					}
				});
			}
		}
	}
</script>

<style>
.content{
	height:100%;
	width:100%;
}
.cell-group{
  background-color: #fff;
}
.cell-left-title{
	margin:18upx 0; 
	margin-left:5upx;
	font-size: 26upx;
}
.cell-padding{
	padding-left:15%;
}
.cell-sn-space{
	padding-left:23%;
}
.cell-pm-space{
	padding-left:21%;
}
.cell-maintainer-space{
	padding-left:17.5%;
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
	left:0;
	/* box-shadow: 0 0 20upx #ccc; */
}
.icon{
  padding-top: 18upx;
  padding-left:8%;
  width: 50upx;
  height: 50upx;
  /* #ifdef MP-ALIPAY */
  background-size: 100% 100%;
  /* #endif */
}
</style>
