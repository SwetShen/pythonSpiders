import datetime

data = [
"坚持下去不是因为我很坚强，而是因为我别无选择",
"含泪播种的人一定能笑着收获",
"做对的事情比把事情做对重要",
"命运给予我们的不是失望之酒，而是机会之杯",
"明日永远新鲜如初，纤尘不染",
"求知若饥，虚心若愚",
"成功将属于那些从不说“不可能”的人"]

weekday = datetime.datetime.now().weekday()
print(data[weekday])