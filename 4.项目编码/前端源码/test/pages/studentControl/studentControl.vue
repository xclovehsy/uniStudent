<template>
	<view>
		<text>学校信息界面</text>
		<u-swiper
		            :list="list3"
		            indicator
		            indicatorMode="line"
		            circular
		    ></u-swiper>
		
		
		<u-button type="primary" text="校园概况"></u-button>
		<u-button type="primary" text="专业介绍"></u-button>
		
		<!-- <u-button type="primary" text="返回信息收集界面"></u-button> -->
		<navigator url="/pages/plane/plane" open-type="navigate" hover-class="navigator-hover">
			<u-button type="primary" text="数据总览"></u-button>
		</navigator>
		
		<u-button type="primary" text="新闻咨询"></u-button>

		
		<u-button type="primary" text="机构设置"></u-button>
		<u-button type="primary" text="校园风采"></u-button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list3: [
					'https://xc-figure.oss-cn-hangzhou.aliyuncs.com/img/202208171439435.png',
					'https://xc-figure.oss-cn-hangzhou.aliyuncs.com/img/202208171439434.png',
					'https://xc-figure.oss-cn-hangzhou.aliyuncs.com/img/202208171439432.jpg',
				],
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
