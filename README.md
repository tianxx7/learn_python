# learn_python
python学习
代码运行在jupyter环境下

### 1.jupyter环境

1.下载python或者Anaconda3,我用的anaconda,建议使用anaconda

```
pip install jupyter
```

### 2.虚拟环境的安装

#### 2.1 新建一个用于python学习的虚拟环境

后便会更新这个环境的,目前这个写的不清楚

```
#安装的是python的话,需要
pip install virtualenv
#测试
virtualenv --version
#为工程搭建虚拟环境
virtualenv my-project-env
#激活虚拟环境
source my-project-env/bin/activate
#停用虚拟环境
deactivate
```

```
另一个工具:virtualenvwrapper
需要安装好virtualenv

pip install virtualenvwrapper
#创建虚拟环境目录
mkdir -p $work_home
mkvirtualenv ai

pip install -r requirements.txt
```



#### 2.2 查看当前的虚拟环境

```
conda env list
```

编辑需要的库文件requirements.txt

```
matplotlib==2.2.2
numpy==1.14.2
pandas==0.20.3
tables==3.4.2
jupyter==1.0.0
#可以不指明版本
```

```
pip install -r requirements.txt
```



```
#进入虚拟环境
workon ai
#输入命令
jupyter notebook
```

