
<template>
  <view>
    <canvas canvas-id="UcgsrwojWzgflwgxVeXCpQnXpqLcLvWh" id="UcgsrwojWzgflwgxVeXCpQnXpqLcLvWh" class="charts" @touchend="tap"/>
  </view>
</template>

<script>
import uCharts from '@/js_sdk/u-charts/u-charts.js';
var uChartsInstance = {};
export default {
  data() {
    return {
      cWidth: 750,
      cHeight: 500
    };
  },
  onReady() {
    //这里的 750 对应 css .charts 的 width
    this.cWidth = uni.upx2px(750);
    //这里的 500 对应 css .charts 的 height
    this.cHeight = uni.upx2px(500);
    this.getServerData();
  },
  methods: {
    getServerData() {
		uni.request({
			  header: {
						'Content-Type': 'application/x-www-form-urlencoded'
				   }, 
			  url: "http://121.4.95.22:10085/api/plane/isResCount", //仅为示例，并非真实接口地址。
			   method: 'GET',
				   data: {
				   },
			   success: (res) => {
						this.data = {
							series: [
							  {
							    data: [{"name":"男生人数","value":res.data.countRes},{"name":"女生人数","value":res.data.countNoRes},]
							  }
							]
						}

						this.drawCharts('UcgsrwojWzgflwgxVeXCpQnXpqLcLvWh', this.data);
					
				   } 
			   })

    },
    drawCharts(id,data){
      const ctx = uni.createCanvasContext(id, this);
      uChartsInstance[id] = new uCharts({
        type: "pie",
        context: ctx,
        width: this.cWidth,
        height: this.cHeight,
        series: data.series,
        animation: true,
        background: "#FFFFFF",
        color: ["#1890FF","#91CB74","#FAC858","#EE6666","#73C0DE","#3CA272","#FC8452","#9A60B4","#ea7ccc"],
        padding: [5,5,5,5],
        extra: {
          pie: {
            activeOpacity: 0.5,
            activeRadius: 10,
            offsetAngle: 0,
            labelWidth: 15,
            border: false,
            borderWidth: 3,
            borderColor: "#FFFFFF"
          }
        }
      });
    },
    tap(e){
      uChartsInstance[e.target.id].touchLegend(e);
      uChartsInstance[e.target.id].showToolTip(e);
    }
  }
};
</script>

<style scoped>
  .charts{
    width: 750rpx;
    height: 500rpx;
  }
</style>