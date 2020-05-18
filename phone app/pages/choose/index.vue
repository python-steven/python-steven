<template>
	<view class="content" style="padding-top: 10upx;">
		<view class="choose-c">
			<view class="flex-col flex-x-center fs-26">
				<!-- 开始时间选择 -->
				<view class="flex-row mb-10">
					<view class="cell-m">开始时间</view>
					<view class="cell-m cell-w">
						<picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindStartDateChange">
							<view class="uni-input">{{starttime}}</view>
						</picker>
					</view>
				</view>
				<!-- 截止时间选择 -->
				<view class="flex-row mb-10">
					<view class="cell-m">截止时间</view>
					<view class="cell-m cell-w">
						<picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindEndDateChange">
							<view class="uni-input">{{endtime}}</view>
						</picker>
					</view>
				</view>
				<!-- SN输入 -->
				<view class="flex-row mb-10 flex-y-center">
					<view class="cell-m">SN</view>
					<input class="input-c1" type="inputType" v-model="sn"></input>
					<!-- #ifndef H5 -->
					<image src="../../static/img/ewm.png" class="icon" mode="aspectFill" @click="scanCode"></image>
					<!-- #endif -->
				</view>
				<!-- 品名输入 -->
				<view class="flex-row mb-10 flex-y-center">
					<view class="cell-m flex-grow-0">品名</view>
					<input class="input-c" type="inputType" v-model="pn"></input>
				</view>
				<!-- 保养人输入 -->
				<view class="flex-row flex-y-center">
					<view class="cell-m">保养人</view>
					<input class="input-c2" type="inputType" v-model="maintainer"></input>
				</view>
			</view>
		</view>
		<view class="cart-bottom">
			<view class="flex-row">
				<button class="btn btn-square btn-b btn-half flex-grow-1" @click="chooseOK">确定</button>
				<button class="btn btn-square btn-b btn-half flex-grow-1" @click="chooseCancel">取消</button>
			</view>
		</view>
	</view>
</template>

<script>
import lvvPopup from '@/components/lvv-popup/lvv-popup.vue'
export default {
	data() {
		return {
			starttime: '请选择',
			endtime: '请选择',
			sn: '',
			pn: '',
			maintainer: '',
			date:'',
		};
	},
	components: {lvvPopup},
	computed: {
        startDate() {
            return this.getDate('start');
        },
        endDate() {
            return this.getDate('end');
        }
    },
	onLoad: function(options) {
	},
	onShow: function() {
	},
	
	methods: {
		// 获取开始时间
		bindStartDateChange: function(e) {
			this.starttime = e.target.value;
		},
		// 获取截止时间
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
		// 确定
		chooseOK(){
			if(this.starttime=='请选择'){
				this.starttime = ''
			}
			if(this.endtime=='请选择'){
				this.endtime=''
			}
			getApp().globalData.type = 1;
			getApp().globalData.chooseString = this.starttime + ',' + this.endtime + ',' + this.sn + ',' + this.pn + ',' + this.maintainer;
			uni.switchTab({
				url:'/pages/list/index'
			})
		},
		// 	取消
		chooseCancel(){
			uni.navigateBack({
				delta: 1,
			});
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
};


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
.input-c{
	/* background: #ffffff; */
	/* #ifdef APP-PLUS */
	width: 60%;
	/*  #endif  */
	/*  #ifdef  H5  */
	width: 70%;
	/*  #endif  */
	margin:20upx 20upx 20upx 55upx;
	border: 1upx solid #10B2AA;
	padding-left: 8upx;
	border-radius: 5upx;
	
}
.input-c1{
	/* background: #ffffff; */
	/* #ifdef APP-PLUS */
	width: 60%;
	/*  #endif  */
	/*  #ifdef  H5  */
	width: 70%;
	/*  #endif  */
	margin:20upx 20upx 20upx 70upx;
	border: 1upx solid #10B2AA;
	padding-left: 8upx;
	border-radius: 5upx;
}
.input-c2{
	/* background: #ffffff; */
	/* #ifdef APP-PLUS */
	width: 60%;
	/*  #endif  */
	/*  #ifdef  H5  */
	width: 70%;
	/*  #endif  */
	margin:20upx 20upx 20upx 30upx;
	border: 1upx solid #10B2AA;
	padding-left: 8upx;
	border-radius: 5upx;
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
.cell-w{
	margin-left: 5%;
	width: 60%;
}
.cell-ft-next{
  float: right;  
}
.icon{
  padding: 18upx 0;
  width: 50upx;
  height: 50upx;
  /* #ifdef MP-ALIPAY */
  background-size: 100% 100%;
  /* #endif */
}
.btn-ok-c{
	position: relative;
	text-align: center;
	height: 100%;
	width: 45%;
	float: left;
}
.cart-bottom {
	/*  #ifdef  H5  */
	bottom: 0px;
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
.btn-cancel-c{
	text-align: center;
	float:left;
	left:50%;
	height: 100%;
	width: 50%;
}
.btn-half{
	width:50%;
}
.icon{
  width: 50upx;
  height: 50upx;
  /* #ifdef MP-ALIPAY */
  background-size: 100% 100%;
  /* #endif */
}

</style>
