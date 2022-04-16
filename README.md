# PTerdemux

## 主要功能

无需写eac3to代码，自动分离原盘中的视频、音频、章节、字幕轨道，其中音频部分涉及转换格式。所有转换均参照猫站PTer压制组标准

## 用法：

(1) CMD进入到pterdemux.py所在的目录下

(2) 运行'python pterdemux.py'

(3) 拖动原盘目录到cmd窗口（支持将NAS中的原盘拖进来），或者直接输入原盘目录的地址，回车。


## 简单的说明：

* 需要安装eac3to软件，并将其加入环境变量。
* 章节、视频、字幕均为无损提取。
  * 提取的章节后缀名为.txt
  * 提取的视频后缀名保持原格式，为.h264或.h265
  * 提取的字幕后缀名保持原格式，一般为.sup
* 音频提取按照猫站PTer压制组720p的标准进行（1080p与720p的区别在于5.1ch和7.1ch是否为DDP）。
  * 1.0及2.0声道转为FLAC格式，如果是24bits，则降为16bits
  * 5.1及7.1声道转为AC3，码率为640kbps

## TO-DO

* 将评论音轨统一转为AAC格式
* 增加5.1及7.1ch转换为DDP格式
