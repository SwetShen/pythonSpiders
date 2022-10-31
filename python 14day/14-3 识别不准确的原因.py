
# 1、训练次数不够（增加训练次数）
# 2、样本不够多（？）

# 关于图像增强的方法

# rotation_range : 旋转 正数（顺时针旋转）负数（逆时针旋转） 度数
# width_shift_range : 平移 正数（右平移） 负数（左平移） 宽度比例 0~1
# height_shift_range ：平移 正数（上平移） 负数（下平移） 高度比例 0~1
# zoom_range : > 1 放大  < 1 缩小
# channel_shift_range ：改变颜色通道 正整数（0~255）
# horizontal_flip ：True 水平翻转
# rescale=1./255 将色彩像素压缩到0~1
# fill_mode 填充方式
#填充方法
# constant kkkkkkkk\abcdk\kkkkkkkk
# nearest aaaaaaaaaa\abcd\ddddddddd
# reflect abcddcba|abcd|dcbaabcd
# wrap abcdabcd\abcd\abcdabcd