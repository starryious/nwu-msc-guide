# MATLAB实现文档编码的转换

* 读取给定的文档，并打开一个新的文档

* 判断文档的编码格式

* 转换文档的编码格式

* 将转换后的写入新的文档中

  代码如下：

```matlab
fileid1=fopen('GBK2UTF8_1.txt','r');%读取目录下文本的二进制数据
[filename,~,~,encoding]=fopen(fileid1);%获取文件名以及编码方式
fileid_1=fopen('GBK2UTF8_1_save.txt','w','n','utf-8');%保存文件的名字,以utf-8编码打开文件
[filename,~,~,encoding]=fopen(fileid_1);%获取保存文件的文件名和编码方式
while 1 %通过循环来输出文本
    tline=fgetl(fileid1);
    if ~ischar(tline) %若到末尾跳出循环
        break
    end
    fprintf(fileid_1,'%s\n',tline);%将获取的文字保存为对应的utf-8编码格式文件
    disp(tline)
end
fclose(fileid1);%关闭文本
fclose(fileid_1)

fileid2=fopen('GBK2UTF8_2.txt','r');
[filename,~,~,encoding]=fopen(fileid2);
fileid_2=fopen('GBK2UTF8_2_save.txt','w','n','utf-8');
[filename,~,~,encoding]=fopen(fileid_2);
while 1 
    tline=fgetl(fileid2);
    if ~ischar(tline)
        break
    end
    fprintf(fileid_2,'%s\n',tline);
    disp(tline)
end
fclose(fileid2);
fclose(fileid_2)

fileid3=fopen('GBK2UTF8_3.txt','r');
[filename,~,~,encoding]=fopen(fileid3);
fileid_3=fopen('GBK2UTF8_3_save.txt','w','n','utf-8');
[filename,~,~,encoding]=fopen(fileid_3);
while 1 
    tline=fgetl(fileid3);
    if ~ischar(tline)
        break
    end
    fprintf(fileid_3,'%s\n',tline);
    disp(tline)
end
fclose(fileid3);
fclose(fileid_3)
```

