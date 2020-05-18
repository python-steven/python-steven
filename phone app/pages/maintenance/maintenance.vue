<template>
	<view class="content">
		<view class="flex-col flex-x-center">
			<view class="cell-item flex-row  flex-y-center">
				<view class='cell-hd-title flex-grow-0'>保养时间</view>
				<view class="cell-hd-title mdate-padding flex-grow-1">
					<picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindDate">
						<view class="uni-input">{{mDate}}</view>
					</picker>
				</view>
			</view>
			<view class="cell-item flex-row flex-y-center">
				<view class='cell-hd-title flex-grow-0'>保养人</view>
				<input class='cell-hd-title operator-padding flex-grow-1' placeholder='请输入保养人' v-model="operator" type="inputType"></input>
			</view>
			<view class="cell-item flex-row flex-y-center">
				<view class='cell-hd-title flex-grow-0'>保养状态</view>
				<view class="cell-hd-title status-padding flex-grow-1">
					<picker @change="bindStatusChange" :value="status" :range="objectStatus">
								<view class="uni-input">{{objectStatus[status]}}</view>
					</picker>
				</view>
			</view>
			<view class="cell-item flex-row flex-y-center">
				<view class='cell-hd-title flex-grow-0'>保养内容</view>
				<input class='cell-hd-title mdate-padding flex-grow-1' placeholder='请输入保养内容' v-model="maintainContent" type="inputType"></input>
			</view>
			<view class="cell-item flex-row flex-y-center">
				<view class='cell-hd-title flex-grow-0'>备注</view>
				<input class='cell-hd-title beizhu-padding flex-grow-1' placeholder='请输入备注' v-model="remark" type="inputType"></input>
			</view>
			<view class="cart-bottom">
				<button class='btn btn-square btn-b btn-all' hover-class="btn-hover2" @click="maintaince()">保养</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				date:'',
				mDate:'请选择',
				operator:'',
				status:0,
				objectStatus: ['PASS', 'NG'],
				maintainContent:'',
				remark:'',
				options:''
				
			}
		},
		onLoad: function (option){
			this.options = option.SN;
			console.log(this.options);
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
			bindStatusChange: function(e) {
				if (this.status !== e.target.value) {
					this.status = e.target.value;
				}
			},
			maintaince(){
				if(this.mDate == '请选择'){
					uni.showToast({
					    icon: 'none',
					    title: '请选择保养时间'
					});
					return;
				}
				if(this.operator == ''){
					uni.showToast({
					    icon: 'none',
					    title: '请选择保养人'
					});
					return;
				}
				if(this.maintainContent == ''){
					uni.showToast({
					    icon: 'none',
					    title: '请输入保养内容'
					});
					return;
				}
				var maintainStatus=''
				if(this.status==0){
					maintainStatus='PASS'
				}else{
					maintainStatus='NG'
				}
				
				
				 const data = {
				    maintian_date: this.mDate,
				    maintainer: this.operator,
					status: maintainStatus,
					content: this.maintainContent,
					remark: this.remark,
					select_sn: this.options
				};
				console.log(this.mDate+this.operator+maintainStatus+this.maintainContent+this.remark+this.options);
				this.$api.MaintainCommit(data, res => {
					console.log(res.data);
					if (res.data=='ok'){
						console.log(res.message);
						uni.switchTab({
							url:'/pages/maintenance_List/index'
						});
					}else{
						console.log(res.message);
						uni.showToast({
						    icon: 'none',
						    title: res.message
						});
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
	background-color: #FFFFFF;
}
.hd-title{
	margin-top:20upx; 
	margin-left:10upx;
	font-size: 26upx;
}
.mdate-padding{
	padding-left:8%;
}
.cell-hd-title{
	margin:18upx 0; 
	margin-left:10upx;
	font-size: 26upx;
}
.operator-padding{
	padding-left:11.5%;
}
.status-padding{
	padding-left:8.5%;
}
.beizhu-padding{
	padding-left:15%;
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
</style>
