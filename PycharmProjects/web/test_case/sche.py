#encoding:utf-8
import time,sched,os
# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数
# 第二个参数以某种人为的方式衡量时间
#先说sched模块，准确的说，它是一个调度（延时处理机制），每次想要定时执行某任务都必须写入一个调度
schedule = sched.scheduler(time.time,time.sleep)
def a():
    print 'now time:',time.time()
    #fi = os.popen('/Users/xiaoxiao/PycharmProjects/web/test_case/runner_report_sengmail.py')
    #f = fi.read()
    os.system('python /Users/xiaoxiao/PycharmProjects/web/test_case/runner_report_sengmail.py')
print time.time()
#设置调度
#schedule.enter(30,0,a,())
while True:
#while true代表的是无限循环
    current_time = time.localtime(time.time())
    if ((current_time.tm_hour == 16) and (current_time.tm_min == 39) and (current_time.tm_sec == 0)):
        schedule.enter(0, 0, a, ())
#参数的意义：30代表时间秒，第二个代表参数优先级，0代表最高，第三个参数是要执行的函数，第四个参数为函数所需要的参数，必须用括号括起来 多个参数最有一个参数后加逗号
        schedule.run()