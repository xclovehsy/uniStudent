<!-- <template>
	<view>


		</u-cell-group>
		<u-popup
			:safeAreaInsetBottom="true"
			:safeAreaInsetTop="true"
			:mode="popupData.mode"
			:show="popShow"
			:round="popupData.round"
			:overlay="popupData.overlay"
			:borderRadius="popupData.borderRadius"
			:closeable="popupData.closeable"
			:closeOnClickOverlay="popupData.closeOnClickOverlay"
			@close="popClose"
			@open="popOpen"
		>
			<view
				class="u-popup-slot"
				:style="{
					width: ['bottom', 'top'].includes(popupData.mode) ? '750rpx' : '200px',
					marginTop: ['left', 'right'].includes(popupData.mode) ? '480rpx' : '0',
				}"
			>	
				<u--text :text="popMsg" v-show="msgShow"></u--text>
				<u-button v-show="returnShow" @click="popClose()" type="primary" icon="checkmark" :plain="false" shape="circle" text="返回填写信息" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button>
				<u-button v-show="uploadShow" @click="popClose()" type="primary" icon="checkmark" :plain="false" shape="circle" text="上传个人信息" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button>
				<u-button v-show="CapReportShow" @click="popClose()" type="primary" icon="checkmark" :plain="false" shape="circle" text="能力测试" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button>
			
			</view>
		</u-popup>
		
		<u-button @click="openPopup()"> test</u-button>
		
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// buShow: true,
				popShow: false,
				msgShow: true,
				returnShow:false,
				uploadShow: true,
				CapReportShow: false,
				popupData: {
					overlay: true,
					mode: 'center',
					round: 10,
					closeOnClickOverlay: true
				},
				popMsg: "您所提交的信息有误",
				
				
			}
		},
		methods: {
			openPopup() {
				this.popupData = {
					overlay: true,
					mode: 'center',
					round: 10,
					closeOnClickOverlay: true
				}
				
				uni.$u.sleep().then(() => {
					this.popShow = !this.popShow
				})
			},
			navigateBack() {
				uni.navigateBack()
			},
			popOpen() {
				// console.log('open');
			},
			popClose() {
				this.popShow = false
				// console.log('close');
			}
		}
	}
</script>

<style lang="scss">
	.u-popup-slot {
		width: 200px;
		height: 150px;
		// @include flex;
		justify-content: center;
		align-items: center;
	}
	.custom-style {
		margin-top: 10px;
		color: #ffffff;
		width: 200rpx;
		font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
	}
</style> -->

<template>
	<view>
		<u-cell-group>
			<u-cell
				:titleStyle="{fontWeight: 500}"
				@click="openPopup(item.popupData)"
				:title="item.title"
				v-for="(item, index) in list"
				:key="index"
				isLink
			>
			</u-cell>
		</u-cell-group>
		<u-popup
			:safeAreaInsetBottom="true"
			:safeAreaInsetTop="true"
			:mode="popupData.mode"
			:show="show"
			:round="popupData.round"
			:overlay="popupData.overlay"
			:borderRadius="popupData.borderRadius"
			:closeable="popupData.closeable"
			:closeOnClickOverlay="popupData.closeOnClickOverlay"
			@close="close"
			@open="open"
		>
			<view
				class="u-popup-slot"
				:style="{
					width: ['bottom', 'top'].includes(popupData.mode) ? '750rpx' : '200px',
					marginTop: ['left', 'right'].includes(popupData.mode) ? '480rpx' : '0',
				}"
			>
				<u-button
					type="success"
					text="点我关闭"
					customStyle="width: 200rpx"
					@click="show = !show"
				></u-button>
			</view>
			
			<!-- <u-button @click="show = !show  ">test</u-button> -->
		</u-popup>
		<button @click="show =!show">test</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				show: false,
				popupData: {
					overlay: true,
					mode: 'bottom',
					borderRadius: '',
					closeable: true,
					closeOnClickOverlay: true
				},
				list: [
					{
						popupData: {
							overlay: true,
							mode: 'center',
							round: 10,
							closeOnClickOverlay: true
						},
						title: '居中弹出',
						iconUrl: 'https://cdn.uviewui.com/uview/demo/popup/modeCenter.png'
					}
				]
			}
		},
		methods: {
			openPopup(popupData) {
				this.popupData = popupData
				uni.$u.sleep().then(() => {
					this.show = !this.show
				})
			},
			navigateBack() {
				uni.navigateBack()
			},
			open() {
				// console.log('open');
			},
			close() {
				this.show = false
				// console.log('close');
			}
		}
	}
</script>

<style lang="scss">
	.u-popup-slot {
		width: 200px;
		height: 150px;
		@include flex;
		justify-content: center;
		align-items: center;
	}
</style>