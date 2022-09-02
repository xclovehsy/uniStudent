<template>
  <view>
    <canvas canvas-id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" class="charts" @touchend="tap"/>
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
			  url: "http://121.4.95.22:10085/api/plane/getCountOfMWS", //仅为示例，并非真实接口地址。
			   method: 'GET',
				   data: {
				   },
			   //dataType:'json',
			   success: (res) => {
						console.log(res.data)
						this.data = {
							series: [
							  {
							    data: [{"name":"男生人数","value":res.data.countM},{"name":"女生人数","value":res.data.countW},]
							  }
							]
						}
						console.log(this.data)
						this.drawCharts('GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL', this.data);
				   } 
			   })
			   
      //模拟从服务器获取数据时的延时
      // setTimeout(() => {
      //   //模拟服务器返回数据，如果数据格式和标准格式不同，需自行按下面的格式拼接
      //   let res = {
      //       series: [
      //         {
      //           data: [{"name":"一班","value":50},{"name":"二班","value":30},{"name":"三班","value":20},{"name":"四班","value":18},{"name":"五班","value":8}]
      //         }
      //       ]
      //     };
      //   this.drawCharts('GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL', res);
      // }, 500);
    },
    drawCharts(id,data){
      const ctx = uni.createCanvasContext(id, this);
      uChartsInstance[id] = new uCharts({
        type: "ring",
        context: ctx,
        width: this.cWidth,
        height: this.cHeight,
        series: data.series,
        animation: true,
        timing: "easeOut",
        duration: 1000,
        rotate: false,
        rotateLock: false,
        background: "#FFFFFF",
        color: ["#1890FF","#91CB74","#FAC858","#EE6666","#73C0DE","#3CA272","#FC8452","#9A60B4","#ea7ccc"],
        padding: [5,5,5,5],
        fontSize: 13,
        fontColor: "#666666",
        dataLabel: true,
        dataPointShape: true,
        dataPointShapeType: "solid",
        touchMoveLimit: 60,
        enableScroll: false,
        enableMarkLine: false,
        legend: {
          show: true,
          position: "right",
          lineHeight: 25,
          float: "center",
          padding: 5,
          margin: 5,
          backgroundColor: "rgba(0,0,0,0)",
          borderColor: "rgba(0,0,0,0)",
          borderWidth: 0,
          fontSize: 13,
          fontColor: "#666666",
          hiddenColor: "#CECECE",
          itemGap: 10
        },
        title: {
          name: "男女比例",
          fontSize: 15,
          color: "#666666",
          offsetX: 0,
          offsetY: 0
        },
        subtitle: {
          name: "happy",
          fontSize: 25,
          color: "#7cb5ec",
          offsetX: 0,
          offsetY: 0
        },
        extra: {
          ring: {
            ringWidth: 30,
            activeOpacity: 0.5,
            activeRadius: 10,
            offsetAngle: 0,
            labelWidth: 15,
            border: true,
            borderWidth: 3,
            borderColor: "#FFFFFF",
            centerColor: "#FFFFFF",
            customRadius: 0,
            linearType: "none"
          },
          tooltip: {
            showBox: true,
            showArrow: true,
            showCategory: false,
            borderWidth: 0,
            borderRadius: 0,
            borderColor: "#000000",
            borderOpacity: 0.7,
            bgColor: "#000000",
            bgOpacity: 0.7,
            gridType: "solid",
            dashLength: 4,
            gridColor: "#CCCCCC",
            fontColor: "#FFFFFF",
            splitLine: true,
            horizentalLine: false,
            xAxisLabel: false,
            yAxisLabel: false,
            labelBgColor: "#FFFFFF",
            labelBgOpacity: 0.7,
            labelFontColor: "#666666"
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