
    //Appクラス
    class App {
      constructor() {
        //stopwatctクラスのインスタンスの作成
        this.stopwatch = new Stopwatch();
      }

      mount() {
          const startStopElement = document.querySelector('.start-stop');
          const StopElement = document.querySelector('.stop')
        const resetElement = document.querySelector('.reset');
        //startStopボタンを押したとき
        startStopElement.addEventListener("click", () => {
          //ストップウォッチが止まっているとき
          if(this.stopwatch.isStop) {
            //ストップウォッチを動かす
            this.stopwatch.start();
          //ストップウォッチが動いているとき
          } else {
            //ストップウォッチを止める
            this.stopwatch.stop();
            //ボタン表示をスタートに
            startStopElement.textContent = "スタート";
          }
        });
        stopElement.addEventListener("click", () => {
            if(this.stopwatch.isStop) {
                this.stopwatch.start();
                }
             else {
              this.stopwatch.stop();
            }
        });
        //resetボタンを押したとき
        resetElement.addEventListener("click", () => {
          //ストップウォッチが止まっているとき
          if(this.stopwatch.isStop){
            //ストップウォッチをリセット
            this.stopwatch.reset();
          }
        });
      }
    }

    //画面の時間表示
    const view = (value) => {
      let min = Math.floor(value / (60 * 1000));
      let sec = Math.floor(value % (60 * 1000) / 1000);
      let minSec = value % 1000;
      //2桁表示に
      if(min < 10) {
        min = ("0" + min).slice(-2);
      }
      sec = ("0" + sec).slice(-2);
      minSec = ("00" + minSec).slice(-3);

      //timerの表示を書き換え
      const timerElement = document.querySelector('.timer');
      timerElement.textContent = `${min}:${sec}.${minSec}`;
    };

    //stopwatchクラス
    class Stopwatch {
      constructor() {
        //リセットメソッドを実行
        this.reset();
      }
      //ストップウォッチをリセット
      reset() {
        this.isStop = true;
        this.id = 0;
        this.elapsedTime = 0;
        view(0);
      }
      //ストップウォッチをスタート
      start() {
        this.isStop = false;
        this.startTime = Date.now();
        this.id = setInterval(() => {
          view((Date.now() - this.startTime) + this.elapsedTime);
        }, 5);
      }
      //ストップウォッチをストップ
      stop() {
        this.isStop = true;
        this.elapsedTime += Date.now() - this.startTime;
        clearInterval(this.id);
      }
    }

    //Appクラスのインスタンスを作成
    const app = new App();
    //マウントメソッドの実行
    app.mount();

