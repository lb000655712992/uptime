import threading
import time
from database.CRUD import config_table_backend, data_table_backend
import get_uptime

threadLock = threading.Lock()


class update_uptime(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(update_uptime, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用於暫停執行緒的標識
        self.__flag.set()  # 設定為True
        self.__running = threading.Event()  # 用於停止執行緒的標識
        self.__running.set()  # 將running設定為True
        self.vms_config = {}
        self.duration = 0
        self.flag_change = True

    def run(self):
        while self.__running.isSet():
            times_duration = 1
            for vm in self.vms_config:
                self.__flag.wait()
                time.sleep(1)
                try:
                    print(vm)
                    username = vm["Username"]
                    password = vm["Password"]
                    IP = vm["IP"]
                    port = vm["Port"]
                    vm["Uptime"] = get_uptime.uptime(username, password, IP, port)
                    data_table_backend.update(vm)
                except Exception as e:
                    vm["Status"] = str(e)
                    data_table_backend.update(vm)

            while times_duration <= self.duration:
                print(times_duration)
                self.__flag.wait()
                if self.flag_change:
                    times_duration += 1
                    time.sleep(1)
                else:
                    self.flag_change = True
                    break

    def pause(self):
        self.__flag.clear()  # 設定為False, 讓執行緒阻塞

    def resume(self):
        self.__flag.set()  # 設定為True, 讓執行緒停止阻塞

    def stop(self):
        self.__flag.set()  # 將執行緒從暫停狀態恢復, 如何已經暫停的話
        self.__running.clear()  # 設定為False

    def change(self, duration, vms):
        self.duration = duration
        self.vms_config = vms
        self.flag_change = False

if __name__ == '__main__':
    """
    程式開始
    """
    try:
        if not config_table_backend.get_count():
            config_table_backend.create({
                "ID": 1,
                "Change": "0",
                "Threshold": "30",
                "Duration": "30"
            })
        vms = data_table_backend.read()
        config = config_table_backend.read(1)
        duration = int(config[0]["Duration"])  # 從data_table獲取duration
        work = update_uptime()  # 建立實例
        work.change(duration, vms)  # 將data_table的duration帶入到實例
        work.start()  # 實例開始
        while True:
            config = config_table_backend.read(1)
            duration = int(config[0]["Duration"])  # 從data_table獲取duration
            if bool(int(config[0]["Change"])):
                print("Cnange")
                vms = data_table_backend.read()
                config[0]["Change"] = "0"
                config_table_backend.update(config[0])
                work.pause()  # 實例暫停
                work.change(duration, vms)  # 將data_table的新duration帶入到實例
                time.sleep(3)
                work.resume()  # 實例繼續
            time.sleep(1)
    except KeyboardInterrupt:
        work.change(0, {})
        work.stop()
