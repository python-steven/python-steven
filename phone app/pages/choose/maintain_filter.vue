<template>
	<view class="content cell-group">
		<view class="flex-col flex-x-center">
			<!-- SN输入 -->
			<view class="cell-item flex-row flex-y-center">
				<view class='cell-hd-title'>SN</view>
				<input class='cell-hd-title cell-padding' placeholder='请输入SN' v-model="sn" type="inputType"></input>
				<!-- #ifndef H5 -->
				<view class="mdate-padding">
					<image src="../../static/img/ewm.png" class="icon" mode="aspectFill" @click="scanCode"></image>
				</view>
				<!-- #endif -->
			</view>
			<!-- PN输入 -->
			<view class="cell-item flex-row flex-y-center">
				<view class='PN-hd-title'>PN</view>
				<input class='PN-hd-title cell-padding' placeholder='请输入PN' v-model="pn" type="inputType"></input>
			</view>
			<!-- 状态选择 -->
			<view class="cell-item flex-row">
				<view class="hd-title">状态</view>
				<view class="hd-title status-padding flex-grow-1">
					<picker @change="bindStatusChange" :value="status" :range="objectStatus">
								<view class="uni-input">{{objectStatus[status]}}</view>
					</picker>
				</view>
			</view>
			<!-- 选择下次保养时间 -->
			<view class="cell-item flex-row">
				<view class="hd-title">下次保养时间</view>
				<view class="hd-title mdate-padding flex-grow-1">
					<picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindDate">
						<view class="uni-input">{{mDate}}</view>
					</picker>
				</view>
			</view>
		</view>
		<view class="cart-bottom">
			<button class='btn btn-square btn-b btn-all' hover-class="btn-hover2" @click="chooseOK()">筛选</button>
		</view>
		<!-- <view class="pop-b">
			<button class='btn btn-square btn-b btn-all' hover-class="btn-hover2" @click="chooseOK()">筛选</button>
		</view> -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				status: 0,
				objectStatus: ['超期', '预警', '正常'],
				mDate: '请选择',
				sn:'',
				pn:'',
				date:'',
			
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
			//获取设备状态
			bindStatusChange: function(e) {
				if (this.status !== e.target.value) {
					this.status = e.target.value;
				}
			},
			//获取下次保养时间
			bindDate: function(e) {
				this.mDate = e.target.value;
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
				var EquipStatus;
				if(this.objectStatus[this.status] == '超期'){
					EquipStatus = 'OVERPROOF'
				}else if(this.objectStatus[this.status] == '预警'){
					EquipStatus = 'WARNING'
				}else if(this.objectStatus[this.status] == '正常'){
					EquipStatus = 'NORMAL'
				}
				if(this.mDate == '请选择'){
					this.mDate =''
				}
				console.log('test');
				console.log(EquipStatus);
				getApp().globalData.maintainType = '1';
				getApp().globalData.maintainChoose = this.sn + ','  + this.pn  + ',' + this.mDate + ',' + EquipStatus;
				uni.switchTab({
					url: '/pages/maintenance/index'
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
		},
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
.margin-cell-group{
	/* margin: 5upx 0 0 0; */
}
.cell-hd-title{
	margin:18upx 0; 
	margin-left:5upx;
	font-size: 26upx;
}
.cell-padding{
	padding-left:25%;
}
.PN-hd-title{
	margin:23upx 0; 
	margin-left:5upx;
	font-size: 26upx;
}
.hd-title{
	margin-top:20upx; 
	margin-left:5upx;
	font-size: 26upx;
}
.status-padding{
	padding-left:23%;
}
.mdate-padding{
	padding-left:8%;
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
.btn-select{
	display: inline-block;
	position: relative;
	text-align: center;
	height: 100%;
	width: 100%;
	float: left;
}
.icon{
  padding-top: 18upx;
  width: 50upx;
  height: 50upx;
  /* #ifdef MP-ALIPAY */
  background-size: 100% 100%;
  /* #endif */
}
</style>
