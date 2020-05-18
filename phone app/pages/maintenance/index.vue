<template>
	<view class="content" v-if="EquipData.length > 0">
		<checkbox-group v-for="(item, index) in EquipData" :key="index" value="item.Id" @change="checkboxChange(item.Id)">
			<view class="flex-row flex-y-center">
				<label>
					<view>
						<checkbox color="#000" :checked="item.is_select" value="item.Id" />
					</view>
				</label>
				<view class="img-list-item">
					<view class="flex-row">
						<!-- <view class="flex-col flex-grow-1"> -->
						<view class="flex-grow-1 flex-left" style="width:50%" >
							<view class="fs-sm item-p">
								<!-- 显示SN -->
								<view class="flex-row">
									<view>SN:</view>
									<view>{{item.SN}}</view>
								</view>
								<!-- 显示保养周期 -->
								<view class="flex-row">
									<view>保养周期(按次数):</view>
									<view>{{item.CheckCycleCount}}</view>
								</view>
								<!-- 显示已使用次数 -->
								<view class="flex-row">
									<view>已使用次数:</view>
									<view>{{item.UsedTimes}}</view>
								</view>
								<!-- 显示保养人 -->
								<view class="flex-row">
									<view>保养人:</view>
									<view>{{item.Maintainer}}</view>
								</view>
							</view>
						</view>
						<!-- <view class="flex-col flex-grow-1 flex-left"> -->
						<view class="flex-grow-1 flex-left" style="width:50%" >
							<view class="fs-sm item-p">
								<!-- 显示品名 -->
								<view class="flex-row">
									<view>品名:</view>
									<view>{{item.PartName}}</view>
								</view>
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
				</view>
			</view>
		</checkbox-group>
		<view class="cart-bottom">
			<view class="flex-row">
				<view class = "flex-grow-1">
					<checkbox-group class="" @change="checkboxAllButton">
						<view class="cart-checkbox-c">
							<checkbox :checked="checkboxAll" color="#10B2AA"/>
							全选
						</view>
					</checkbox-group>
				</view>
				<view class = "flex-grow-0">
					<button class="btn btn-square btn-b" @click="maintain" hover-class="btn-hover2">保养</button>
				</view>
			</view>
		</view>
		<!-- 保养页面 -->
		<!-- <lvv-popup position="bottom" ref="lvvpopref">
			<view  style="width: 100%;max-height: 804upx;background: #FFFFFF;position: absolute;left:0;bottom: 0;">
				<view class="pop-b">
					<view class="flex-col flex-x-center">
						<view class="cell-item flex-row flex-y-center">
							<view class="flex-row flex-grow-1">
								<view class='cell-hd-title flex-grow-0'>保养时间</view>
								<view class="hd-title mdate-padding flex-grow-1">
									<picker mode="date" style="z-index:50" :value="date" :start="startDate" :end="endDate" @change="bindDate">
										<view class="uni-input">{{mDate}}</view>
									</picker>
								</view>
							</view>
							<view class="close-padding flex-grow-0">
								<image class="icon" src="../../static/img/close.png" mode="aspectFill"  @click="toclose()"></image>
							</view>
						</view>
						<view class="cell-item flex-row flex-y-center">
							<view class='cell-hd-title'>保养人</view>
							<input class='cell-hd-title p-padding' placeholder='请输入保养人' v-model="operator" type="inputType"></input>
						</view>
						<view class="cell-item flex-row flex-y-center">
							<view class='cell-hd-title'>保养状态</view>
							<view class="cell-hd-title status-padding flex-grow-1">
								<picker @change="bindPickerChange" :value="status" :range="objectStatus">
											<view class="uni-input">{{objectStatus[status]}}</view>
								</picker>
							</view>
						</view>
					</view>
					<view class="cell-item flex-row flex-y-center">
						<view class='cell-hd-title'>保养内容</view>
						<input class='cell-hd-title mdate-padding' placeholder='请输入保养内容' v-model="maintainContent" type="inputType"></input>
					</view>
					<view class="cell-item flex-row flex-y-center">
						<view class='cell-hd-title'>备注</view>
						<input class='cell-hd-title beizhu-padding' placeholder='请输入备注' v-model="remark" type="inputType"></input>
					</view>
				</view>
				<button class='btn btn-square btn-b btn-all' hover-class="btn-hover2" @click="clickHandle">确定</button>
			</view>
		</lvv-popup> -->
		
	</view>
	<!-- 未筛选设备清单页面 -->
	<view class='content' v-else>
		<view class='cart-none'>
			<view class="flex-col flex-y-center">
				<image class="cart-none-img" src="../../static/img/cart.png" mode=""></image>
				<view class='cart-none-t'>设备清单为空 T.T</view>
				<view class='cart-none-m'>快点进行筛选吧</view>
			</view>
		</view>
	</view>
	
</template>

<script>
	import Vue from 'vue'
	import { get } from '@/config/db.js'
	import lvvPopup from '@/components/lvv-popup/lvv-popup.vue'
	import {
	    mapState,
	    mapMutations
	} from 'vuex'
	export default {
		components: {
			lvvPopup,
		},
		data() {
			return {
				EquipData: {}, //设备数据
				isLoad: true,
				// showState: false,
				// mDate: '2019-07-04',
				// date:'',
				// status: 0,
				// objectStatus: ['PASS', 'NG'],
				checkboxAll: false, //全选按钮
				SelectEquip:{},
				// operator:'',
				index: 0,
				// maintainContent:'',
				// remark:'',
				SelectEquipSN:[],
				user:this.$db.get("login"),
				
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
		onLoad: function() {
			// this.initData();
		},
		onShow: function () {
			const app = getApp().globalData;
			if(app.maintainType =='0'){
				console.log(this.user);
				this.GetUserMaintainData();
			}else{
				this.GetEquData();
			}
			this.checkboxAll = false;
		},
		//跳转到筛选页面
		onNavigationBarButtonTap(e) {
			console.log("debug");
			uni.navigateTo({
				url: '/pages/choose/maintain_filter',
				animationType: 'pop-in',
			});
		},
		methods: {
			GetUserMaintainData(){
				const data = {
					maintain_operator: this.user
				}
				this.$api.MaintainList(data,res => {
					this.EquipData = res.data;
					console.log(res.data);
					this.EquipData.forEach(item => {
						console.log(item.Status);
						Vue.set(item,'is_select',false);
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
			//获取符合筛选条件的设备数据
			GetEquData(){
				const app = getApp().globalData;
				var str = app.maintainChoose.split(',');
				const data = {
					sn: str[0],
					pn: str[1],
					date:str[2],
					status: str[3],
				};
				console.log(str[0]+str[1]+str[2]+str[3]);
				this.$api.Filtrate(data,res => {
					this.EquipData = res.data;
					console.log(res.data);
					this.EquipData.forEach(item => {
						// console.log(item.Status);
						Vue.set(item,'is_select',false);
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
			//变更选择状态
			checkboxChange: function(e) {
				let _this = this;
				let Id = e;
				let EquipData = _this.EquipData;
				EquipData.forEach(item => {
					if (item.Id == Id){
						if (item.is_select == true) {
							item.is_select = false;
						} else {
							item.is_select = true;
						}
					}
				});
				_this.EquipData = EquipData;
			},
			//显示保养页面
			maintain:function(e) {
				this.SelectEquipSN=[];
				console.log("debug");
				this.EquipData.forEach(item => {
					console.log("debug2");
					if(item.is_select==true){
						console.log("debug1");
						console.log(item.SN);
						this.SelectEquipSN.push(item.SN);
					}
				});
				console.log(this.SelectEquipSN[0]);
				var string = '/pages/maintenance/maintenance?SN=' + JSON.stringify(this.SelectEquipSN)
				uni.navigateTo({
					url: string,
					animationType: 'pop-in',
				});
				// this.$refs.lvvpopref.show();
				// this.showState = true; 
				
			},
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
			bindPickerChange: function(e) {
				this.status = e.target.value;
			},
			// 关闭modal弹出框
			toclose(){
				this.$refs.lvvpopref.close();
			},
			//全选操作
			checkboxAllButton: function(e) {
				if (this.checkboxAll == true) {
					this.checkboxAll = false;
					this.setAllCheckbox(false);
				} else {
					this.checkboxAll = true;
					this.setAllCheckbox(true);
				}
			},
			//全选设置
			setAllCheckbox: function(e) {
				let _this = this;
				let EquipData = _this.EquipData;
				if (e) {
				//全选
					EquipData.forEach(item => {
						item.is_select = true;
					});
				}else{
					EquipData.forEach(item => {
						item.is_select = false;
					});
				}
				_this.EquipData = EquipData;
			},
			// clickHandle: function(e){
			// 	console.log("click");
			// 	if (this.mDate == '请选择') {
			// 	    uni.showToast({
			// 	        icon: 'none',
			// 	        title: '请选择保养日期'
			// 	    });
			// 	    return;
			// 	}
			// 	if (this.operator.length < 1) {
			// 	    uni.showToast({
			// 	        icon: 'none',
			// 	        title: '请输入保养人'
			// 	    });
			// 	    return;
			// 	}
			// 	if(this.maintainContent.length < 1){
			// 		 uni.showToast({
			// 		    icon: 'none',
			// 		    title: '请输入保养内容'
			// 		});
			// 		return;
			// 	}
			// 	this.EquipData.forEach(item => {
			// 		if(item.is_select==true){
			// 			this.SelectEquipData.push(item);
			// 		}
			// 	});
				// console.log(this.SelectEquipData[0].SN);
				// const data = {
				//     maintian_date: this.mDate,
				//     maintainer: this.operator,
				// 	status:this.objectStatus[this.status],
				// 	content: this.maintainContent,
				// 	remark: this.remark,
				// 	select_sn: SelectEquipData
				// };
			// }
		}
	}
</script>

<style>
.content{
	height:100%;
	width:100%;
	background-color: #FFFFFF;
}
.cart-none{
	height:100%;
	width:100%;
	background-color: #FFFFFF;
	padding: 200upx 0;
}
.cart-none-img{
	width: 252upx;
	height: 228upx;
	margin-bottom: 40upx;
}
.cart-none-t{
	color: #666;
	font-size: 28upx;
}
.cart-none-m{
	color: #666;
	font-size: 28upx;
	margin-bottom: 40upx;
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
	background-color: #fff;
	position: fixed;
	
	overflow: hidden;
	/* box-shadow: 0 0 20upx #ccc; */
}
.cart-bottom .cart-checkbox-c {
	color: #333;
	font-size: 30upx;
}
.cart-checkbox{
	position: relative;
	height: 100%;
}
.cart-checkbox-c{
	display: inline-block;
	position: absolute;
	top: 50%;
	left: 26upx;
	transform: translateY(-50%);
	z-index: 99;
}
.cart-bottom-right {
	height: 90upx;
	float: right;
	overflow: hidden;
}
.pop-b{
	margin-bottom: 90upx;
}
.cell-hd-title{
	margin:18upx 0; 
	margin-left:10upx;
	font-size: 26upx;
}
.close-padding{
	margin:18upx 0; 
}
.hd-title{
	margin-top:20upx; 
	margin-left:10upx;
	font-size: 26upx;
}

.mdate-padding{
	padding-left:8%;
}
.p-padding{
	padding-left:11.5%;
}
.status-padding{
	padding-left:8.5%;
}
.beizhu-padding{
	padding-left:15%;
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
.pop-t{
	position: relative;
	padding:30upx 26upx;
	/* border-bottom:2upx solid #f3f3f3; */
	/* box-shadow: 0 0 20upx #ccc; */
}

.pop-c{
	width:100%;
}
.icon{
  width: 40upx;
  height: 40upx;
  /* #ifdef MP-ALIPAY */
  background-size: 100% 100%;
  /* #endif */
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
</style>
