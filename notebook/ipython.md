## 1. 自动缩进

无意中发现，在ipython中，如果函数写了return，则回车就不会缩进。

```
def getText(filename):
    doc = docx.Document(os.path.dirname(os.getcwd()) + '/files/word/' + filename)
    for para in doc.paragraphs:
        for run in para.runs:
            print(run.text)
    return None
getText('demo.docx')
```
写完`None`，回车，光标在get的g位置。

写完`text)`回车，默认为函数没有写完，光标在`print`的p下方

## 2. 更新conda造成的事故

早上来用jupyter，发现不能用了：

```
caimeijuandeMacBook-Air:~ caimeijuan$ jupyter notebook
Traceback (most recent call last):
  File "/Users/caimeijuan/anaconda/bin/jupyter", line 4, in <module>
    from jupyter_core.command import main
ModuleNotFoundError: No module named 'jupyter_core'
```

换ipython notebook 也一样。只有ipython可以进去。

想了半天，是昨天晚上更新conda引起的，但是那条命令我却记不得了，是系统提示更新我就更新了。

今天运行这个：

```
conda update conda
```

输出中提到：

```
PackagesNotFoundError: The following packages are not available from current channels:

  - pkgs/free/osx-64::sockjs-tornado==1.0.1=py27_0 -> tornado==4.0.1
  - pkgs/free/osx-64::sphinx==1.3.1=py27_0 -> alabaster==0.7.3
  - pkgs/free/osx-64::sphinx==1.3.1=py27_0 -> babel==1.3
  - pkgs/free/osx-64::nbconvert==4.0.0=py27_0 -> jupyter_core==4.0.2
  - pkgs/free/osx-64::nbconvert==4.0.0=py27_0 -> nbformat==4.0.0
  - pkgs/free/osx-64::pickleshare==0.5=py27_0 -> path.py==7.6

Current channels:

  - https://repo.anaconda.com/pkgs/main/osx-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/osx-64
  - https://repo.anaconda.com/pkgs/r/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


```

所以现在不能用ipython了。

真是飞来横祸啊。

[install - PackagesNotFoundError: The following packages are not available from current channels: - Stack Overflow](https://stackoverflow.com/questions/48493505/packagesnotfounderror-the-following-packages-are-not-available-from-current-cha)

重新安装jupyter：

```
conda install jupyter
```

再运行`jupyter notebook`出来的是：

```
Traceback (most recent call last):
  File "/Users/caimeijuan/anaconda/bin/jupyter-notebook", line 4, in <module>
    from notebook.notebookapp import main
ModuleNotFoundError: No module named 'notebook'

```
可奇怪了。

如果运行` ipython notebook`，则输出：

```
Traceback (most recent call last):
  File "/Users/caimeijuan/anaconda/bin/ipython", line 4, in <module>
    from IPython import start_ipython
ImportError: No module named IPython
```

## 3. conda

昨天用的哪条命令已经找不到了。mac终端下本来有`history`这一条可以用的，但是不知道为什么几百条下来也找不到哪条动的是conda。

查看conda版本：

```
conda -V
```
输出为：`conda 4.7.5`

更新所有包：

```
conda update --all
```

更新情况：

```
The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    cffi-1.12.3                |   py37hb5b8e2f_0         212 KB
    cryptography-2.7           |   py37ha12b0ac_0         518 KB
    jdcal-1.4.1                |             py_0          11 KB
    libpng-1.6.37              |       ha441bb4_0         262 KB
    libxml2-2.9.9              |       hf6e021a_1         1.3 MB
    lxml-4.3.4                 |   py37hef8c89e_0         1.1 MB
    openpyxl-2.6.2             |             py_0         157 KB
    pip-19.1.1                 |           py37_0         1.6 MB
    pysocks-1.7.0              |           py37_0          30 KB
    python-3.7.3               |       h359304d_0        18.0 MB
    requests-2.22.0            |           py37_0          91 KB
    setuptools-41.0.1          |           py37_0         506 KB
    soupsieve-1.8              |           py37_0         105 KB
    sqlite-3.28.0              |       ha441bb4_0         1.2 MB
    urllib3-1.24.2             |           py37_0         158 KB
    wheel-0.33.4               |           py37_0          41 KB
    ------------------------------------------------------------
                                           Total:        25.3 MB

The following packages will be UPDATED:

  cffi                                1.12.1-py37hb5b8e2f_0 --> 1.12.3-py37hb5b8e2f_0
  cryptography                           2.5-py37ha12b0ac_0 --> 2.7-py37ha12b0ac_0
  jdcal                  pkgs/main/osx-64::jdcal-1.4-py37_0 --> pkgs/main/noarch::jdcal-1.4.1-py_0
  libpng                                  1.6.36-ha441bb4_0 --> 1.6.37-ha441bb4_0
  libxml2                                  2.9.9-hab757c2_0 --> 2.9.9-hf6e021a_1
  lxml                                 4.3.1-py37hef8c89e_0 --> 4.3.4-py37hef8c89e_0
  openpyxl           pkgs/main/osx-64::openpyxl-2.6.1-py37~ --> pkgs/main/noarch::openpyxl-2.6.2-py_0
  pip                                         19.0.3-py37_0 --> 19.1.1-py37_0
  pysocks                                      1.6.8-py37_0 --> 1.7.0-py37_0
  python                                   3.7.2-haf84260_0 --> 3.7.3-h359304d_0
  requests                                    2.21.0-py37_0 --> 2.22.0-py37_0
  setuptools                                  41.0.0-py37_0 --> 41.0.1-py37_0
  soupsieve                                    1.7.1-py37_0 --> 1.8-py37_0
  sqlite                                  3.26.0-ha441bb4_0 --> 3.28.0-ha441bb4_0
  urllib3                                     1.24.1-py37_0 --> 1.24.2-py37_0
  wheel                                       0.33.1-py37_0 --> 0.33.4-py37_0


```

查看conda情况：

```
conda info
```

输出：

```
     active environment : python35
    active env location : /Users/caimeijuan/anaconda/envs/python35
            shell level : 1
       user config file : /Users/caimeijuan/.condarc
 populated config files : /Users/caimeijuan/.condarc
          conda version : 4.7.5
    conda-build version : not installed
         python version : 3.6.8.final.0
       virtual packages : 
       base environment : /Users/caimeijuan/anaconda  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/osx-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/osx-64
                          https://repo.anaconda.com/pkgs/r/noarch
                          https://conda.anaconda.org/conda-forge/osx-64
                          https://conda.anaconda.org/conda-forge/noarch
          package cache : /Users/caimeijuan/anaconda/pkgs
                          /Users/caimeijuan/.conda/pkgs
       envs directories : /Users/caimeijuan/anaconda/envs
                          /Users/caimeijuan/.conda/envs
               platform : osx-64
             user-agent : conda/4.7.5 requests/2.22.0 CPython/3.6.8 Darwin/18.6.0 OSX/10.14.5
                UID:GID : 501:20
             netrc file : None
           offline mode : False
```

使用命令`conda install --only-deps anaconda`，等待情况。看样子好几个库都是回滚的。不知道全部完成后什么效果。

没想到，这句执行成功后，`jupyter notebook`得到的居然是退回去这样的了：

```
Traceback (most recent call last):
  File "/Users/caimeijuan/anaconda/bin/jupyter", line 4, in <module>
    from jupyter_core.command import main
ModuleNotFoundError: No module named 'jupyter_core'
```

检查conda版本，仍然是`4.7.5`。那就只是把安装的jupyter卸了吧？


[install - PackagesNotFoundError：当前通道不提供以下软件包： - Stack Overflow](https://stackoverflow.com/questions/48493505/packagesnotfounderror-the-following-packages-are-not-available-from-current-cha)

遵照这里的做法，先运行这个：

```
conda config --append channels conda-forge

```
> 它告诉conda 在搜索包时也会查看conda-forge通道。

如果再次运行这一句，系统就会提示：

```
Warning: 'conda-forge' already in 'channels' list, moving to the bottom
```

此时如果运行它说到的`conda install slycot control`（我并不是要安装这两个），会输出：  

```
Collecting package metadata (current_repodata.json): done
Solving environment: failed
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - pkgs/free/osx-64::sockjs-tornado==1.0.1=py27_0 -> tornado==4.0.1
  - pkgs/free/osx-64::sphinx==1.3.1=py27_0 -> alabaster==0.7.3
  - pkgs/free/osx-64::sphinx==1.3.1=py27_0 -> babel==1.3
  - pkgs/free/osx-64::nbconvert==4.0.0=py27_0 -> jupyter_core==4.0.2
  - pkgs/free/osx-64::nbconvert==4.0.0=py27_0 -> nbformat==4.0.0
  - pkgs/free/osx-64::pickleshare==0.5=py27_0 -> path.py==7.6

Current channels:

  - https://repo.anaconda.com/pkgs/main/osx-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/osx-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://conda.anaconda.org/conda-forge/osx-64
  - https://conda.anaconda.org/conda-forge/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.

```
会发现notfound的还是那几个，current channel则多了两行，这是上面一条命令起作用的原因。

[PackagesNotFoundError: The following packages are not available from current channels: · Issue #174 · abinit/abipy](https://github.com/abinit/abipy/issues/174)

又增加两条运行：

```
conda config --add channels matsci
conda config --add channels abinit

```
还试那个安装语句：

```
(base) caimeijuandeMacBook-Air:~ caimeijuan$ conda install slycot control
Collecting package metadata (current_repodata.json): done
Solving environment: failed
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - pkgs/free/osx-64::sockjs-tornado==1.0.1=py27_0 -> tornado==4.0.1
  - pkgs/free/osx-64::sphinx==1.3.1=py27_0 -> alabaster==0.7.3
  - pkgs/free/osx-64::sphinx==1.3.1=py27_0 -> babel==1.3
  - pkgs/free/osx-64::nbconvert==4.0.0=py27_0 -> jupyter_core==4.0.2
  - pkgs/free/osx-64::nbconvert==4.0.0=py27_0 -> nbformat==4.0.0
  - pkgs/free/osx-64::pickleshare==0.5=py27_0 -> path.py==7.6

Current channels:

  - https://conda.anaconda.org/abinit/osx-64
  - https://conda.anaconda.org/abinit/noarch
  - https://conda.anaconda.org/matsci/osx-64
  - https://conda.anaconda.org/matsci/noarch
  - https://conda.anaconda.org/conda-forge/osx-64
  - https://conda.anaconda.org/conda-forge/noarch
  - https://repo.anaconda.com/pkgs/main/osx-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/osx-64
  - https://repo.anaconda.com/pkgs/r/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.

```

进入python3环境运行刚才这个安装，顺利安装了。决定继续试试`conda install jupyter`

安装好之后，仍然运行不了`jupyter notebook`：  

```
(python35) caimeijuandeMacBook-Air:~ caimeijuan$ jupyter notebook
Traceback (most recent call last):
  File "/Users/caimeijuan/anaconda/bin/jupyter", line 4, in <module>
    from jupyter_core.command import main
ModuleNotFoundError: No module named 'jupyter_core'
```
[No module named 'jupyter_core' · Issue #153 · dunovank/jupyter-themes](https://github.com/dunovank/jupyter-themes/issues/153)

又运行了一下这个： 

```
pip3 install --upgrade notebook
```

更新所有包：

```
conda update --all
```


时隔多日（已经7月16号了），又回来试。`pip3 install jupyter`，仍然失败：

```
WARNING: No metadata found in ./anaconda/envs/python35/lib/python3.7/site-packages
ERROR: Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/bleach-3.1.0.dist-info/METADATA'
```

不知道哪里看来的，先`pip3 install pync`，成功。

```
Installing collected packages: pync
Successfully installed pync-2.0.3
```
然而无济于事

看到说`conda-build version : not installed`，于是运行`conda install conda-build`安装，不料安装完竟然还是`conda-build version : not installed`.


根据这里的说法[No module named 'jupyter_core' · Issue #153 · dunovank/jupyter-themes](https://github.com/dunovank/jupyter-themes/issues/153)，开始运行`pip3 install lesscpy`，成功是成功了，不知道有啥用。

又一次时隔多日（7月30日），仍然先`pip3 install jupyter`，这次最后的警告信息是：

```
WARNING: No metadata found in ./anaconda/envs/python35/lib/python3.7/site-packages
ERROR: Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/mistune-0.8.4.dist-info/METADATA'


```
metadata前的目录换了一下。

到实际位置去看，这两个上级目录都是在的，但metadata却不是目录，而是一个json文件。


[python - Pip cannot find metadata file - EnvironmentError - Stack Overflow](https://stackoverflow.com/questions/54552367/pip-cannot-find-metadata-file-environmenterror)

这一页所说的三个命令似乎没有用：

```
cd ~/.local/lib/python3.7/site-packages/pip-19.0.1.dist-info/
cp -r ./pip-19.0.1.dist-info/* ./
rm -r ./pip-19.0.1.dist-info

```

```
FileNotFoundError: [Errno 2] No such file or directory: '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/pyparsing-2.3.1.dist-info/METADATA'

FileNotFoundError: [Errno 2] No such file or directory: '/Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages/pandas-0.24.2.dist-info/METADATA'
```
在以上几个目录里依次塞上pip-19.0.3.dist-info文件夹里的metadata。。。

[No module named 'jupyter_core' · Issue #153 · dunovank/jupyter-themes · GitHub](https://github.com/dunovank/jupyter-themes/issues/153)
使用这个命令：

```
pip3 install --upgrade notebook
```
提示无权限，建议加上`--user`，于是生生地改成：  

```
pip3 install --upgrade notebook --user

```
反馈：  

```
  WARNING: The scripts jupyter-kernel, jupyter-kernelspec and jupyter-run are installed in '/Users/caimeijuan/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed jupyter-client-5.3.1

```

如法炮制：  

```
 pip3 install jupyter --user
 
 pip3 install --upgrade jupyterthemes
 
 conda update --all

 pip3 install --upgrade jupyter
```

## 4. 重装anaconda

这么多天无果，决定壮士断腕，来个大手术。卸载已有的，重新安装。

### 4.1 第1步，下载anaconda安装包。

[Anaconda Python/R Distribution - Free Download](https://www.anaconda.com/distribution/#download-section)

这次是在这里下载的。安装包还不小，653M。早知道这么大就在家里下载了。

### 4.2 第2步，检查anaconda里现在安装了哪些包。

已经用过的命令如下：  

```
conda install lxml
conda install beautifulsoup4
conda install requests
conda install openpyxl
conda install pillow
```

查看：

```
conda list
```

结果：  

```
# packages in environment at /Users/caimeijuan/anaconda:
#
# Name                    Version                   Build  Channel
_license                  1.1                      py27_1    https://repo.continuum.io/pkgs/free
abstract-rendering        0.5.1               np110py27_0    https://repo.continuum.io/pkgs/free
alabaster                 0.7.6                    py27_0    https://repo.continuum.io/pkgs/free
anaconda                  custom           py27h2cfa9e9_0  
anaconda-client           1.2.1                    py27_0    https://repo.continuum.io/pkgs/free
appnope                   0.1.0                    py27_0    https://repo.continuum.io/pkgs/free
appscript                 1.0.1                    py27_0    https://repo.continuum.io/pkgs/free
argcomplete               1.0.0                    py27_1    https://repo.continuum.io/pkgs/free
asn1crypto                0.24.0                   py36_0  
astropy                   1.0.6               np110py27_0    https://repo.continuum.io/pkgs/free
babel                     2.1.1                    py27_0    https://repo.continuum.io/pkgs/free
backports                 1.0                      py27_1  
backports.functools_lru_cache 1.5                      py27_1  
backports_abc             0.4                      py27_0    https://repo.continuum.io/pkgs/free
beautifulsoup4            4.7.1                    py27_1  
bitarray                  0.8.1                    py27_0    https://repo.continuum.io/pkgs/free
blaze-core                0.8.3                    py27_0    https://repo.continuum.io/pkgs/free
bokeh                     0.10.0                   py27_0    https://repo.continuum.io/pkgs/free
boto                      2.38.0                   py27_0    https://repo.continuum.io/pkgs/free
bottleneck                1.0.0               np110py27_0    https://repo.continuum.io/pkgs/free
bzip2                     1.0.7                h1de35cc_0  
ca-certificates           2019.5.15                     0  
cdecimal                  2.3                      py27_0    https://repo.continuum.io/pkgs/free
certifi                   2019.6.16                py36_0  
cffi                      1.12.3           py36hb5b8e2f_0  
chardet                   3.0.4                    py36_1  
clyent                    1.2.0                    py27_0    https://repo.continuum.io/pkgs/free
colorama                  0.3.3                    py27_0    https://repo.continuum.io/pkgs/free
conda                     4.7.5                    py36_0  
conda-build               1.18.2                   py27_0    https://repo.continuum.io/pkgs/free
conda-env                 2.6.0                         1  
conda-package-handling    1.3.10                   py36_0  
configobj                 5.0.6                    py27_0    https://repo.continuum.io/pkgs/free
cryptography              2.7              py36ha12b0ac_0  
curl                      7.63.0            ha441bb4_1000  
cycler                    0.9.0                    py27_0    https://repo.continuum.io/pkgs/free
cython                    0.23.4                   py27_1    https://repo.continuum.io/pkgs/free
cytoolz                   0.9.0.1          py27h1de35cc_1  
datashape                 0.4.7               np110py27_1    https://repo.continuum.io/pkgs/free
decorator                 4.0.4                    py27_0    https://repo.continuum.io/pkgs/free
docutils                  0.12                     py27_0    https://repo.continuum.io/pkgs/free
dynd-python               0.7.0                    py27_0    https://repo.continuum.io/pkgs/free
enum34                    1.1.6                    py27_0    https://repo.continuum.io/pkgs/free
fastcache                 1.0.2                    py27_0    https://repo.continuum.io/pkgs/free
flask                     0.10.1                   py27_1    https://repo.continuum.io/pkgs/free
freetype                  2.5.5                         0    https://repo.continuum.io/pkgs/free
funcsigs                  0.4                      py27_0    https://repo.continuum.io/pkgs/free
futures                   3.2.0                    py27_0  
gevent                    1.0.1                    py27_0    https://repo.continuum.io/pkgs/free
gevent-websocket          0.9.3                    py27_0    https://repo.continuum.io/pkgs/free
greenlet                  0.4.9                    py27_0    https://repo.continuum.io/pkgs/free
grin                      1.2.1                    py27_1    https://repo.continuum.io/pkgs/free
h5py                      2.5.0               np110py27_4    https://repo.continuum.io/pkgs/free
hdf5                      1.8.15.1                      2    https://repo.continuum.io/pkgs/free
icu                       58.2                 h4b95b61_1  
idna                      2.8                      py36_0  
ipaddress                 1.0.18                   py27_0    https://repo.continuum.io/pkgs/free
ipykernel                 4.1.1                    py27_0    https://repo.continuum.io/pkgs/free
ipython                   4.0.1                    py27_0    https://repo.continuum.io/pkgs/free
ipython-notebook          4.0.4                    py27_0    https://repo.continuum.io/pkgs/free
ipython-qtconsole         4.0.1                    py27_0    https://repo.continuum.io/pkgs/free
ipython_genutils          0.1.0                    py27_0    https://repo.continuum.io/pkgs/free
ipywidgets                4.1.0                    py27_0    https://repo.continuum.io/pkgs/free
itsdangerous              0.24                     py27_0    https://repo.continuum.io/pkgs/free
jbig                      2.1                           0    https://repo.continuum.io/pkgs/free
jdcal                     1.0                      py27_0    https://repo.continuum.io/pkgs/free
jedi                      0.9.0                    py27_0    https://repo.continuum.io/pkgs/free
jinja2                    2.8                      py27_0    https://repo.continuum.io/pkgs/free
jpeg                      8d                            1    https://repo.continuum.io/pkgs/free
jsonschema                2.4.0                    py27_0    https://repo.continuum.io/pkgs/free
jupyter                   1.0.0                    py27_1    https://repo.continuum.io/pkgs/free
jupyter_client            4.1.1                    py27_0    https://repo.continuum.io/pkgs/free
jupyter_console           4.0.3                    py27_0    https://repo.continuum.io/pkgs/free
jupyter_core              4.0.6                    py27_0    https://repo.continuum.io/pkgs/free
krb5                      1.16.1               hddcf347_7  
launcher                  1.0.0                         3    https://repo.continuum.io/pkgs/free
libarchive                3.3.3                h786848e_5  
libcurl                   7.63.0            h051b688_1000  
libcxx                    4.0.1                hcfea43d_1  
libcxxabi                 4.0.1                hcfea43d_1  
libdynd                   0.7.0                         0    https://repo.continuum.io/pkgs/free
libedit                   3.1.20181209         hb402a30_0  
libffi                    3.2.1                h475c297_4  
libiconv                  1.15                 hdd342a3_7  
libpng                    1.6.17                        0    https://repo.continuum.io/pkgs/free
libssh2                   1.8.0                ha12b0ac_4  
libtiff                   4.0.6                         2    https://repo.anaconda.com/pkgs/free
libxml2                   2.9.9                hab757c2_0  
libxslt                   1.1.33               h33a18ac_0  
llvmlite                  0.8.0                    py27_0    https://repo.continuum.io/pkgs/free
lxml                      4.3.1            py27hef8c89e_0  
lz4-c                     1.8.1.2              h1de35cc_0  
lzo                       2.10                 h362108e_2  
markupsafe                0.23                     py27_0    https://repo.continuum.io/pkgs/free
matplotlib                1.5.0               np110py27_0    https://repo.continuum.io/pkgs/free
mistune                   0.7.1                    py27_0    https://repo.continuum.io/pkgs/free
multipledispatch          0.4.8                    py27_0    https://repo.continuum.io/pkgs/free
nbconvert                 4.0.0                    py27_0    https://repo.continuum.io/pkgs/free
nbformat                  4.0.1                    py27_0    https://repo.continuum.io/pkgs/free
ncurses                   6.1                  h0a44026_1  
networkx                  1.10                     py27_0    https://repo.continuum.io/pkgs/free
node-webkit               0.10.1                        0    https://repo.continuum.io/pkgs/free
nose                      1.3.7                    py27_0    https://repo.continuum.io/pkgs/free
notebook                  4.0.6                    py27_0    https://repo.continuum.io/pkgs/free
numba                     0.22.1              np110py27_0    https://repo.continuum.io/pkgs/free
numexpr                   2.4.4               np110py27_0    https://repo.continuum.io/pkgs/free
numpy                     1.10.1                   py27_0    https://repo.continuum.io/pkgs/free
odo                       0.3.4                    py27_0    https://repo.continuum.io/pkgs/free
openpyxl                  2.2.6                    py27_0    https://repo.continuum.io/pkgs/free
openssl                   1.1.1c               h1de35cc_1  
packaging                 16.8                     py27_0    https://repo.continuum.io/pkgs/free
pandas                    0.17.1              np110py27_0    https://repo.continuum.io/pkgs/free
path.py                   8.1.2                    py27_1    https://repo.continuum.io/pkgs/free
patsy                     0.4.0               np110py27_0    https://repo.continuum.io/pkgs/free
pep8                      1.6.2                    py27_0    https://repo.continuum.io/pkgs/free
pexpect                   3.3                      py27_0    https://repo.continuum.io/pkgs/free
pickleshare               0.5                      py27_0    https://repo.continuum.io/pkgs/free
pillow                    3.0.0                    py27_1    https://repo.continuum.io/pkgs/free
pip                       19.1.1                   py36_0  
ply                       3.8                      py27_0    https://repo.continuum.io/pkgs/free
psutil                    3.3.0                    py27_0    https://repo.continuum.io/pkgs/free
ptyprocess                0.5                      py27_0    https://repo.continuum.io/pkgs/free
py                        1.4.30                   py27_0    https://repo.continuum.io/pkgs/free
pyasn1                    0.1.9                    py27_0    https://repo.continuum.io/pkgs/free
pyaudio                   0.2.7                    py27_0    https://repo.continuum.io/pkgs/free
pycosat                   0.6.3            py36h1de35cc_0  
pycparser                 2.19                     py36_0  
pycrypto                  2.6.1                    py27_0    https://repo.continuum.io/pkgs/free
pycurl                    7.43.0.2         py27ha12b0ac_0  
pyflakes                  1.0.0                    py27_0    https://repo.continuum.io/pkgs/free
pygments                  2.0.2                    py27_0    https://repo.continuum.io/pkgs/free
pyopenssl                 19.0.0                   py36_0  
pyparsing                 2.2.0                    py27_0    https://repo.continuum.io/pkgs/free
pyqt                      4.11.4                   py27_1    https://repo.continuum.io/pkgs/free
pysocks                   1.7.0                    py36_0  
pytables                  3.2.2               np110py27_0    https://repo.continuum.io/pkgs/free
pytest                    2.8.1                    py27_0    https://repo.continuum.io/pkgs/free
python                    3.6.8                haf84260_0  
python-dateutil           2.4.2                    py27_0    https://repo.continuum.io/pkgs/free
python-libarchive-c       2.8                     py36_10  
python.app                1.2                      py27_4    https://repo.continuum.io/pkgs/free
pytz                      2015.7                   py27_0    https://repo.continuum.io/pkgs/free
pyyaml                    3.11                     py27_1    https://repo.continuum.io/pkgs/free
pyzmq                     14.7.0                   py27_1    https://repo.continuum.io/pkgs/free
qt                        4.8.7                         1    https://repo.continuum.io/pkgs/free
qtconsole                 4.1.1                    py27_0    https://repo.continuum.io/pkgs/free
readline                  7.0                  h1de35cc_5  
redis                     2.6.9                         0    https://repo.continuum.io/pkgs/free
redis-py                  2.10.3                   py27_0    https://repo.continuum.io/pkgs/free
requests                  2.22.0                   py36_0  
rope                      0.9.4                    py27_1    https://repo.continuum.io/pkgs/free
ruamel_yaml               0.11.14          py36h9d7ade0_2  
scikit-image              0.11.3              np110py27_0    https://repo.continuum.io/pkgs/free
scikit-learn              0.17                np110py27_1    https://repo.continuum.io/pkgs/free
scipy                     0.16.0              np110py27_1    https://repo.continuum.io/pkgs/free
setuptools                41.0.1                   py36_0  
simplegeneric             0.8.1                    py27_0    https://repo.continuum.io/pkgs/free
singledispatch            3.4.0.3                  py27_0    https://repo.continuum.io/pkgs/free
sip                       4.16.9                   py27_0    https://repo.continuum.io/pkgs/free
six                       1.12.0                   py36_0  
snowballstemmer           1.2.0                    py27_0    https://repo.continuum.io/pkgs/free
sockjs-tornado            1.0.1                    py27_0    https://repo.continuum.io/pkgs/free
soupsieve                 1.7.1                    py27_0  
sphinx                    1.3.1                    py27_0    https://repo.continuum.io/pkgs/free
sphinx_rtd_theme          0.1.7                    py27_0    https://repo.continuum.io/pkgs/free
spyder                    2.3.8                    py27_0    https://repo.continuum.io/pkgs/free
spyder-app                2.3.8                    py27_0    https://repo.continuum.io/pkgs/free
sqlalchemy                1.0.9                    py27_0    https://repo.continuum.io/pkgs/free
sqlite                    3.26.0               ha441bb4_0  
ssl_match_hostname        3.4.0.2                  py27_0    https://repo.continuum.io/pkgs/free
statsmodels               0.6.1               np110py27_0    https://repo.continuum.io/pkgs/free
sympy                     0.7.6.1                  py27_0    https://repo.continuum.io/pkgs/free
terminado                 0.5                      py27_1    https://repo.continuum.io/pkgs/free
tk                        8.6.8                ha441bb4_0  
toolz                     0.9.0                    py27_0  
tornado                   4.3                      py27_0    https://repo.continuum.io/pkgs/free
tqdm                      4.32.1                     py_0  
traitlets                 4.0.0                    py27_0    https://repo.continuum.io/pkgs/free
ujson                     1.33                     py27_0    https://repo.continuum.io/pkgs/free
unicodecsv                0.14.1                   py27_0    https://repo.continuum.io/pkgs/free
urllib3                   1.24.2                   py36_0  
werkzeug                  0.11.2                   py27_0    https://repo.continuum.io/pkgs/free
wheel                     0.33.4                   py36_0  
xlrd                      0.9.4                    py27_0    https://repo.continuum.io/pkgs/free
xlsxwriter                0.7.7                    py27_0    https://repo.continuum.io/pkgs/free
xlwings                   0.5.0                    py27_0    https://repo.continuum.io/pkgs/free
xlwt                      1.0.0                    py27_0    https://repo.continuum.io/pkgs/free
xz                        5.2.4                h1de35cc_4  
yaml                      0.1.6                         0    https://repo.continuum.io/pkgs/free
zeromq                    4.1.3                         0    https://repo.continuum.io/pkgs/free
zlib                      1.2.11                        0    https://repo.continuum.io/pkgs/free
zstd                      1.3.7                h5bba6e5_0  
```
在python3环境下再运行一次`conda list`，结果：  

```
WARNING conda.core.prefix_data:_load_site_packages(285): Problem reading non-conda package record at lib/python3.7/site-packages/jupyterlab-0.35.4-py3.7.egg-info/PKG-INFO. Please verify that you still need this, and if so, that this is still installed correctly. Reinstalling this package may help.
WARNING conda.core.prefix_data:_load_site_packages(285): Problem reading non-conda package record at lib/python3.7/site-packages/widgetsnbextension-3.4.2-py3.7.egg-info/PKG-INFO. Please verify that you still need this, and if so, that this is still installed correctly. Reinstalling this package may help.
# packages in environment at /Users/caimeijuan/anaconda/envs/python35:
#
# Name                    Version                   Build  Channel
antiorm                   1.2.1                    pypi_0    pypi
appdirs                   1.4.3                    pypi_0    pypi
appnope                   0.1.0                    pypi_0    pypi
asn1crypto                0.24.0                py37_1003    conda-forge
attrs                     19.1.0                   pypi_0    pypi
backcall                  0.1.0                    pypi_0    pypi
beautifulsoup4            4.8.0                    py37_0    conda-forge
bottle                    0.12.16                  pypi_0    pypi
buildozer                 0.39                     pypi_0    pypi
builtwith                 1.3.3                    pypi_0    pypi
bzip2                     1.0.8                h01d97ff_0    conda-forge
ca-certificates           2019.6.16            hecc5488_0    conda-forge
certifi                   2019.6.16                py37_1    conda-forge
cffi                      1.12.3           py37hccf1714_0    conda-forge
chardet                   3.0.4                 py37_1003    conda-forge
colorama                  0.4.1                    pypi_0    pypi
conda                     4.7.10                   py37_0    conda-forge
conda-build               3.18.9                   py37_0    conda-forge
conda-package-handling    1.3.11                   py37_0    conda-forge
cryptography              2.7              py37h212c5bf_0    conda-forge
cycler                    0.10.0                   pypi_0    pypi
cython                    0.29.7                   pypi_0    pypi
db                        0.1.1                    pypi_0    pypi
decorator                 4.3.2                    pypi_0    pypi
defusedxml                0.6.0                    pypi_0    pypi
django                    2.2.2                    pypi_0    pypi
docutils                  0.14                     pypi_0    pypi
entrypoints               0.3                      pypi_0    pypi
et_xmlfile                1.0.1                   py_1001    conda-forge
filelock                  3.0.10                     py_0    conda-forge
freetype                  2.10.0               h24853df_0    conda-forge
future                    0.17.1                   pypi_0    pypi
glob2                     0.7                        py_0    conda-forge
graphics-py               5.0.1.post1              pypi_0    pypi
html5lib                  1.0.1                      py_0    conda-forge
icu                       64.2                 h6de7cb9_0    conda-forge
idna                      2.8                   py37_1000    conda-forge
ipykernel                 5.1.0                    pypi_0    pypi
ipython                   7.3.0                    pypi_0    pypi
ipython-genutils          0.2.0                    pypi_0    pypi
ipywidgets                7.5.1                    pypi_0    pypi
jdcal                     1.4.1                      py_0    conda-forge
jedi                      0.13.3                   pypi_0    pypi
jinja2                    2.10.1                     py_0    conda-forge
jpeg                      9c                h1de35cc_1001    conda-forge
jsonschema                3.0.1                    pypi_0    pypi
jupyter                   1.0.0                    pypi_0    pypi
jupyter-client            5.2.4                    pypi_0    pypi
jupyter-console           6.0.0                    pypi_0    pypi
jupyter-core              4.4.0                    pypi_0    pypi
jupyterthemes             0.20.0                   pypi_0    pypi
kivy                      1.10.1                   pypi_0    pypi
kivy-garden               0.1.4                    pypi_0    pypi
kiwisolver                1.0.1                    pypi_0    pypi
kvdb                      3.5                      pypi_0    pypi
lesscpy                   0.13.0                   pypi_0    pypi
libarchive                3.3.3             h5c473cc_1006    conda-forge
libcxx                    8.0.0                         4    conda-forge
libcxxabi                 8.0.0                         4    conda-forge
libffi                    3.2.1             h6de7cb9_1006    conda-forge
libiconv                  1.15              h01d97ff_1005    conda-forge
liblief                   0.9.0                h2a1bed3_1    conda-forge
libpng                    1.6.37               h2573ce8_0    conda-forge
libtiff                   4.0.10            hd08fb8f_1003    conda-forge
libxml2                   2.9.9                h12c6b28_2    conda-forge
libxslt                   1.1.32            h320ff13_1004    conda-forge
lxml                      4.4.0            py37h08abf6f_0    conda-forge
lz4-c                     1.8.3             h6de7cb9_1001    conda-forge
lzo                       2.10              h1de35cc_1000    conda-forge
markupsafe                1.1.1            py37h1de35cc_0    conda-forge
matplotlib                3.0.3                    pypi_0    pypi
nbconvert                 5.5.0                    pypi_0    pypi
nbformat                  4.4.0                    pypi_0    pypi
ncurses                   6.1               h0a44026_1002    conda-forge
notebook                  6.0.0                    pypi_0    pypi
numpy                     1.16.2                   pypi_0    pypi
olefile                   0.46                       py_0    conda-forge
opencv-python             4.1.0.25                 pypi_0    pypi
openpyxl                  2.6.2                      py_0    conda-forge
openssl                   1.1.1c               h01d97ff_0    conda-forge
pandocfilters             1.4.2                    pypi_0    pypi
parso                     0.3.4                    pypi_0    pypi
pexpect                   4.6.0                    pypi_0    pypi
pickleshare               0.7.5                    pypi_0    pypi
pillow                    5.4.1           py37hbddbef0_1000    conda-forge
pip                       19.0.3                   pypi_0    pypi
pkginfo                   1.5.0.1                    py_0    conda-forge
ply                       3.11                     pypi_0    pypi
prometheus-client         0.7.1                    pypi_0    pypi
prompt-toolkit            2.0.9                    pypi_0    pypi
psutil                    5.6.3            py37h01d97ff_0    conda-forge
ptyprocess                0.6.0                    pypi_0    pypi
py-lief                   0.9.0            py37h6d6d4d2_1    conda-forge
pyautogui                 0.9.44                   pypi_0    pypi
pycosat                   0.6.3           py37h1de35cc_1001    conda-forge
pycparser                 2.19                     py37_1    conda-forge
pygetwindow               0.0.5                    pypi_0    pypi
pygments                  2.3.1                    pypi_0    pypi
pyjwt                     1.7.1                    pypi_0    pypi
pymsgbox                  1.0.6                    pypi_0    pypi
pymysql                   0.9.3                    pypi_0    pypi
pync                      2.0.3                    pypi_0    pypi
pyobjc                    5.2                      pypi_0    pypi
pyobjc-core               5.2                      pypi_0    pypi
pyobjc-framework-accounts 5.2                      pypi_0    pypi
pyobjc-framework-addressbook 5.2                      pypi_0    pypi
pyobjc-framework-adsupport 5.2                      pypi_0    pypi
pyobjc-framework-applescriptkit 5.2                      pypi_0    pypi
pyobjc-framework-applescriptobjc 5.2                      pypi_0    pypi
pyobjc-framework-applicationservices 5.2                      pypi_0    pypi
pyobjc-framework-automator 5.2                      pypi_0    pypi
pyobjc-framework-avfoundation 5.2                      pypi_0    pypi
pyobjc-framework-avkit    5.2                      pypi_0    pypi
pyobjc-framework-businesschat 5.2                      pypi_0    pypi
pyobjc-framework-calendarstore 5.2                      pypi_0    pypi
pyobjc-framework-cfnetwork 5.2                      pypi_0    pypi
pyobjc-framework-cloudkit 5.2                      pypi_0    pypi
pyobjc-framework-cocoa    5.2                      pypi_0    pypi
pyobjc-framework-collaboration 5.2                      pypi_0    pypi
pyobjc-framework-colorsync 5.2                      pypi_0    pypi
pyobjc-framework-contacts 5.2                      pypi_0    pypi
pyobjc-framework-contactsui 5.2                      pypi_0    pypi
pyobjc-framework-coreaudio 5.2                      pypi_0    pypi
pyobjc-framework-coreaudiokit 5.2                      pypi_0    pypi
pyobjc-framework-corebluetooth 5.2                      pypi_0    pypi
pyobjc-framework-coredata 5.2                      pypi_0    pypi
pyobjc-framework-corelocation 5.2                      pypi_0    pypi
pyobjc-framework-coremedia 5.2                      pypi_0    pypi
pyobjc-framework-coremediaio 5.2                      pypi_0    pypi
pyobjc-framework-coreml   5.2                      pypi_0    pypi
pyobjc-framework-coreservices 5.2                      pypi_0    pypi
pyobjc-framework-corespotlight 5.2                      pypi_0    pypi
pyobjc-framework-coretext 5.2                      pypi_0    pypi
pyobjc-framework-corewlan 5.2                      pypi_0    pypi
pyobjc-framework-cryptotokenkit 5.2                      pypi_0    pypi
pyobjc-framework-dictionaryservices 5.2                      pypi_0    pypi
pyobjc-framework-discrecording 5.2                      pypi_0    pypi
pyobjc-framework-discrecordingui 5.2                      pypi_0    pypi
pyobjc-framework-diskarbitration 5.2                      pypi_0    pypi
pyobjc-framework-dvdplayback 5.2                      pypi_0    pypi
pyobjc-framework-eventkit 5.2                      pypi_0    pypi
pyobjc-framework-exceptionhandling 5.2                      pypi_0    pypi
pyobjc-framework-externalaccessory 5.2                      pypi_0    pypi
pyobjc-framework-findersync 5.2                      pypi_0    pypi
pyobjc-framework-fsevents 5.2                      pypi_0    pypi
pyobjc-framework-gamecenter 5.2                      pypi_0    pypi
pyobjc-framework-gamecontroller 5.2                      pypi_0    pypi
pyobjc-framework-gamekit  5.2                      pypi_0    pypi
pyobjc-framework-gameplaykit 5.2                      pypi_0    pypi
pyobjc-framework-imagecapturecore 5.2                      pypi_0    pypi
pyobjc-framework-imserviceplugin 5.2                      pypi_0    pypi
pyobjc-framework-inputmethodkit 5.2                      pypi_0    pypi
pyobjc-framework-installerplugins 5.2                      pypi_0    pypi
pyobjc-framework-instantmessage 5.2                      pypi_0    pypi
pyobjc-framework-intents  5.2                      pypi_0    pypi
pyobjc-framework-iosurface 5.2                      pypi_0    pypi
pyobjc-framework-ituneslibrary 5.2                      pypi_0    pypi
pyobjc-framework-latentsemanticmapping 5.2                      pypi_0    pypi
pyobjc-framework-launchservices 5.2                      pypi_0    pypi
pyobjc-framework-libdispatch 5.2                      pypi_0    pypi
pyobjc-framework-localauthentication 5.2                      pypi_0    pypi
pyobjc-framework-mapkit   5.2                      pypi_0    pypi
pyobjc-framework-mediaaccessibility 5.2                      pypi_0    pypi
pyobjc-framework-medialibrary 5.2                      pypi_0    pypi
pyobjc-framework-mediaplayer 5.2                      pypi_0    pypi
pyobjc-framework-mediatoolbox 5.2                      pypi_0    pypi
pyobjc-framework-modelio  5.2                      pypi_0    pypi
pyobjc-framework-multipeerconnectivity 5.2                      pypi_0    pypi
pyobjc-framework-naturallanguage 5.2                      pypi_0    pypi
pyobjc-framework-netfs    5.2                      pypi_0    pypi
pyobjc-framework-network  5.2                      pypi_0    pypi
pyobjc-framework-networkextension 5.2                      pypi_0    pypi
pyobjc-framework-notificationcenter 5.2                      pypi_0    pypi
pyobjc-framework-opendirectory 5.2                      pypi_0    pypi
pyobjc-framework-osakit   5.2                      pypi_0    pypi
pyobjc-framework-photos   5.2                      pypi_0    pypi
pyobjc-framework-photosui 5.2                      pypi_0    pypi
pyobjc-framework-preferencepanes 5.2                      pypi_0    pypi
pyobjc-framework-pubsub   5.2                      pypi_0    pypi
pyobjc-framework-qtkit    5.2                      pypi_0    pypi
pyobjc-framework-quartz   5.2                      pypi_0    pypi
pyobjc-framework-safariservices 5.2                      pypi_0    pypi
pyobjc-framework-scenekit 5.2                      pypi_0    pypi
pyobjc-framework-screensaver 5.2                      pypi_0    pypi
pyobjc-framework-scriptingbridge 5.2                      pypi_0    pypi
pyobjc-framework-searchkit 5.2                      pypi_0    pypi
pyobjc-framework-security 5.2                      pypi_0    pypi
pyobjc-framework-securityfoundation 5.2                      pypi_0    pypi
pyobjc-framework-securityinterface 5.2                      pypi_0    pypi
pyobjc-framework-servicemanagement 5.2                      pypi_0    pypi
pyobjc-framework-social   5.2                      pypi_0    pypi
pyobjc-framework-spritekit 5.2                      pypi_0    pypi
pyobjc-framework-storekit 5.2                      pypi_0    pypi
pyobjc-framework-syncservices 5.2                      pypi_0    pypi
pyobjc-framework-systemconfiguration 5.2                      pypi_0    pypi
pyobjc-framework-usernotifications 5.2                      pypi_0    pypi
pyobjc-framework-videosubscriberaccount 5.2                      pypi_0    pypi
pyobjc-framework-videotoolbox 5.2                      pypi_0    pypi
pyobjc-framework-vision   5.2                      pypi_0    pypi
pyobjc-framework-webkit   5.2                      pypi_0    pypi
pyopenssl                 19.0.0                   py37_0    conda-forge
pypdf2                    1.26.0                   pypi_0    pypi
pyperclip                 1.7.0                    pypi_0    pypi
pyrect                    0.1.4                    pypi_0    pypi
pyrsistent                0.15.4                   pypi_0    pypi
pyscreeze                 0.1.21                   pypi_0    pypi
pysocks                   1.7.0                    py37_0    conda-forge
python                    3.7.3                h93065d6_1    conda-forge
python-dateutil           2.8.0                    pypi_0    pypi
python-docx               0.8.10                   pypi_0    pypi
python-for-android        0.7.0                    pypi_0    pypi
python-libarchive-c       2.8                   py37_1004    conda-forge
python-whois              0.7.1                    pypi_0    pypi
pytweening                1.0.3                    pypi_0    pypi
pytz                      2019.1                     py_0    conda-forge
pyyaml                    5.1.1            py37h01d97ff_0    conda-forge
pyzmq                     18.0.0                   pypi_0    pypi
qtconsole                 4.5.2                    pypi_0    pypi
readline                  8.0                  hcfe32e1_0    conda-forge
requests                  2.22.0                   py37_1    conda-forge
ruamel_yaml               0.15.71         py37h1de35cc_1000    conda-forge
selenium                  3.141.0                  pypi_0    pypi
send2trash                1.5.0                    pypi_0    pypi
setuptools                41.0.1                   py37_0    conda-forge
sh                        1.12.14                  pypi_0    pypi
six                       1.12.0                   pypi_0    pypi
soupsieve                 1.9.2                    py37_0    conda-forge
sqlite                    3.29.0               hb7d70f7_0    conda-forge
sqlparse                  0.3.0                    pypi_0    pypi
terminado                 0.8.2                    pypi_0    pypi
testpath                  0.4.2                    pypi_0    pypi
tk                        8.6.9             h2573ce8_1002    conda-forge
tornado                   5.1.1                    pypi_0    pypi
tqdm                      4.24.0                   py37_1    matsci
traitlets                 4.3.2                    pypi_0    pypi
twilio                    6.27.0                   pypi_0    pypi
urllib3                   1.25.3                   py37_0    conda-forge
utils                     0.9.0                    pypi_0    pypi
virtualenv                16.6.0                   pypi_0    pypi
wcwidth                   0.1.7                    pypi_0    pypi
web-py                    0.40.dev0                pypi_0    pypi
webencodings              0.5.1                    pypi_0    pypi
wheel                     0.33.4                   py37_0    conda-forge
widgetsnbextension        3.5.1                    pypi_0    pypi
xz                        5.2.4             h1de35cc_1001    conda-forge
yaml                      0.1.7             h1de35cc_1001    conda-forge
zlib                      1.2.11            h01d97ff_1005    conda-forge
zstd                      1.4.0                ha9f0a20_0    conda-forge
```

### 4.3 第3步，卸载anaconda

[Mac OSX上卸载Anaconda - ''竹先森゜ - 博客园](https://www.cnblogs.com/zhuminghui/p/9281895.html)

在python3的环境下，

```
conda install anaconda-clean
anaconda-clean --yes
rm -rf ~/anaconda
```

第三个命令，由于有python3环境的python35文件夹不空，没有自动删除，于是手动删除了。

重启电脑。

### 4.4 第4步，重装

上面下载的安装包点击安装。

这次直接成功了。得到的文件夹是anaconda3。所以新安装的文件只有python3。

### 4.5 第5步，补之前安装的各个库。

`conda list`的结果：  

```
# packages in environment at /Users/caimeijuan/anaconda3:
#
# Name                    Version                   Build  Channel
_ipyw_jlab_nb_ext_conf    0.1.0                    py37_0  
alabaster                 0.7.12                   py37_0  
anaconda                  2019.07                  py37_0  
anaconda-client           1.7.2                    py37_0  
anaconda-navigator        1.9.7                    py37_0  
anaconda-project          0.8.3                      py_0  
appnope                   0.1.0                    py37_0  
appscript                 1.1.0            py37h1de35cc_0  
asn1crypto                0.24.0                   py37_0  
astroid                   2.2.5                    py37_0  
astropy                   3.2.1            py37h1de35cc_0  
atomicwrites              1.3.0                    py37_1  
attrs                     19.1.0                   py37_1  
babel                     2.7.0                      py_0  
backcall                  0.1.0                    py37_0  
backports                 1.0                        py_2  
backports.functools_lru_cache 1.5                        py_2  
backports.os              0.1.1                    py37_0  
backports.shutil_get_terminal_size 1.0.0                    py37_2  
backports.tempfile        1.0                        py_1  
backports.weakref         1.0.post1                  py_1  
beautifulsoup4            4.7.1                    py37_1  
bitarray                  0.9.3            py37h1de35cc_0  
bkcharts                  0.2                      py37_0  
blas                      1.0                         mkl  
bleach                    3.1.0                    py37_0  
blosc                     1.16.3               hd9629dc_0  
bokeh                     1.2.0                    py37_0  
boto                      2.49.0                   py37_0  
bottleneck                1.2.1            py37h1d22016_1  
bzip2                     1.0.8                h1de35cc_0  
ca-certificates           2019.5.15                     0  
certifi                   2019.6.16                py37_0  
cffi                      1.12.3           py37hb5b8e2f_0  
chardet                   3.0.4                    py37_1  
click                     7.0                      py37_0  
cloudpickle               1.2.1                      py_0  
clyent                    1.2.2                    py37_1  
colorama                  0.4.1                    py37_0  
conda                     4.7.10                   py37_0  
conda-build               3.18.8                   py37_0  
conda-env                 2.6.0                         1  
conda-package-handling    1.3.11                   py37_0  
conda-verify              3.4.2                      py_1  
contextlib2               0.5.5                    py37_0  
cryptography              2.7              py37ha12b0ac_0  
curl                      7.65.2               ha441bb4_0  
cycler                    0.10.0                   py37_0  
cython                    0.29.12          py37h0a44026_0  
cytoolz                   0.10.0           py37h1de35cc_0  
dask                      2.1.0                      py_0  
dask-core                 2.1.0                      py_0  
dbus                      1.13.6               h90a0687_0  
decorator                 4.4.0                    py37_1  
defusedxml                0.6.0                      py_0  
distributed               2.1.0                      py_0  
docutils                  0.14                     py37_0  
entrypoints               0.3                      py37_0  
et_xmlfile                1.0.1                    py37_0  
expat                     2.2.6                h0a44026_0  
fastcache                 1.1.0            py37h1de35cc_0  
filelock                  3.0.12                     py_0  
flask                     1.1.1                      py_0  
freetype                  2.9.1                hb4e5f40_0  
future                    0.17.1                   py37_0  
get_terminal_size         1.0.0                h7520d66_0  
gettext                   0.19.8.1             h15daf44_3  
gevent                    1.4.0            py37h1de35cc_0  
glib                      2.56.2               hd9629dc_0  
glob2                     0.7                        py_0  
gmp                       6.1.2                hb37e062_1  
gmpy2                     2.0.8            py37h6ef4df4_2  
greenlet                  0.4.15           py37h1de35cc_0  
h5py                      2.9.0            py37h3134771_0  
hdf5                      1.10.4               hfa1e0ec_0  
heapdict                  1.0.0                    py37_2  
html5lib                  1.0.1                    py37_0  
icu                       58.2                 h4b95b61_1  
idna                      2.8                      py37_0  
imageio                   2.5.0                    py37_0  
imagesize                 1.1.0                    py37_0  
importlib_metadata        0.17                     py37_1  
intel-openmp              2019.4                      233  
ipykernel                 5.1.1            py37h39e3cac_0  
ipython                   7.6.1            py37h39e3cac_0  
ipython_genutils          0.2.0                    py37_0  
ipywidgets                7.5.0                      py_0  
isort                     4.3.21                   py37_0  
itsdangerous              1.1.0                    py37_0  
jbig                      2.1                  h4d881f8_0  
jdcal                     1.4.1                      py_0  
jedi                      0.13.3                   py37_0  
jinja2                    2.10.1                   py37_0  
joblib                    0.13.2                   py37_0  
jpeg                      9b                   he5867d9_2  
json5                     0.8.4                      py_0  
jsonschema                3.0.1                    py37_0  
jupyter                   1.0.0                    py37_7  
jupyter_client            5.3.1                      py_0  
jupyter_console           6.0.0                    py37_0  
jupyter_core              4.5.0                      py_0  
jupyterlab                1.0.2            py37hf63ae98_0  
jupyterlab_server         1.0.0                      py_0  
keyring                   18.0.0                   py37_0  
kiwisolver                1.1.0            py37h0a44026_0  
krb5                      1.16.1               hddcf347_7  
lazy-object-proxy         1.4.1            py37h1de35cc_0  
libarchive                3.3.3                h786848e_5  
libcurl                   7.65.2               h051b688_0  
libcxx                    4.0.1                hcfea43d_1  
libcxxabi                 4.0.1                hcfea43d_1  
libedit                   3.1.20181209         hb402a30_0  
libffi                    3.2.1                h475c297_4  
libgfortran               3.0.1                h93005f0_2  
libiconv                  1.15                 hdd342a3_7  
liblief                   0.9.0                h2a1bed3_2  
libpng                    1.6.37               ha441bb4_0  
libsodium                 1.0.16               h3efe00b_0  
libssh2                   1.8.2                ha12b0ac_0  
libtiff                   4.0.10               hcb84e12_2  
libxml2                   2.9.9                hf6e021a_1  
libxslt                   1.1.33               h33a18ac_0  
llvm-openmp               4.0.1                hcfea43d_1  
llvmlite                  0.29.0           py37h98b8051_0  
locket                    0.2.0                    py37_1  
lxml                      4.3.4            py37hef8c89e_0  
lz4-c                     1.8.1.2              h1de35cc_0  
lzo                       2.10                 h362108e_2  
markupsafe                1.1.1            py37h1de35cc_0  
matplotlib                3.1.0            py37h54f8f79_0  
mccabe                    0.6.1                    py37_1  
mistune                   0.8.4            py37h1de35cc_0  
mkl                       2019.4                      233  
mkl-service               2.0.2            py37h1de35cc_0  
mkl_fft                   1.0.12           py37h5e564d8_0  
mkl_random                1.0.2            py37h27c97d8_0  
mock                      3.0.5                    py37_0  
more-itertools            7.0.0                    py37_0  
mpc                       1.1.0                h6ef4df4_1  
mpfr                      4.0.1                h3018a27_3  
mpmath                    1.1.0                    py37_0  
msgpack-python            0.6.1            py37h04f5b5a_1  
multipledispatch          0.6.0                    py37_0  
navigator-updater         0.2.1                    py37_0  
nbconvert                 5.5.0                      py_0  
nbformat                  4.4.0                    py37_0  
ncurses                   6.1                  h0a44026_1  
networkx                  2.3                        py_0  
nltk                      3.4.4                    py37_0  
nose                      1.3.7                    py37_2  
notebook                  6.0.0                    py37_0  
numba                     0.44.1           py37h6440ff4_0  
numexpr                   2.6.9            py37h7413580_0  
numpy                     1.16.4           py37hacdab7b_0  
numpy-base                1.16.4           py37h6575580_0  
numpydoc                  0.9.1                      py_0  
olefile                   0.46                     py37_0  
openpyxl                  2.6.2                      py_0  
openssl                   1.1.1c               h1de35cc_1  
packaging                 19.0                     py37_0  
pandas                    0.24.2           py37h0a44026_0  
pandoc                    2.2.3.2                       0  
pandocfilters             1.4.2                    py37_1  
parso                     0.5.0                      py_0  
partd                     1.0.0                      py_0  
path.py                   12.0.1                     py_0  
pathlib2                  2.3.4                    py37_0  
patsy                     0.5.1                    py37_0  
pcre                      8.43                 h0a44026_0  
pep8                      1.7.1                    py37_0  
pexpect                   4.7.0                    py37_0  
pickleshare               0.7.5                    py37_0  
pillow                    6.1.0            py37hb68e598_0  
pip                       19.1.1                   py37_0  
pkginfo                   1.5.0.1                  py37_0  
pluggy                    0.12.0                     py_0  
ply                       3.11                     py37_0  
prometheus_client         0.7.1                      py_0  
prompt_toolkit            2.0.9                    py37_0  
psutil                    5.6.3            py37h1de35cc_0  
ptyprocess                0.6.0                    py37_0  
py                        1.8.0                    py37_0  
py-lief                   0.9.0            py37h1413db1_2  
pycodestyle               2.5.0                    py37_0  
pycosat                   0.6.3            py37h1de35cc_0  
pycparser                 2.19                     py37_0  
pycrypto                  2.6.1            py37h1de35cc_9  
pycurl                    7.43.0.3         py37ha12b0ac_0  
pyflakes                  2.1.1                    py37_0  
pygments                  2.4.2                      py_0  
pylint                    2.3.1                    py37_0  
pyodbc                    4.0.26           py37h0a44026_0  
pyopenssl                 19.0.0                   py37_0  
pyparsing                 2.4.0                      py_0  
pyqt                      5.9.2            py37h655552a_2  
pyrsistent                0.14.11          py37h1de35cc_0  
pysocks                   1.7.0                    py37_0  
pytables                  3.5.2            py37h5bccee9_1  
pytest                    5.0.1                    py37_0  
pytest-arraydiff          0.3              py37h39e3cac_0  
pytest-astropy            0.5.0                    py37_0  
pytest-doctestplus        0.3.0                    py37_0  
pytest-openfiles          0.3.2                    py37_0  
pytest-remotedata         0.3.1                    py37_0  
python                    3.7.3                h359304d_0  
python-dateutil           2.8.0                    py37_0  
python-libarchive-c       2.8                     py37_11  
python.app                2                        py37_9  
pytz                      2019.1                     py_0  
pywavelets                1.0.3            py37h1d22016_1  
pyyaml                    5.1.1            py37h1de35cc_0  
pyzmq                     18.0.0           py37h0a44026_0  
qt                        5.9.7                h468cd18_1  
qtawesome                 0.5.7                    py37_1  
qtconsole                 4.5.1                      py_0  
qtpy                      1.8.0                      py_0  
readline                  7.0                  h1de35cc_5  
requests                  2.22.0                   py37_0  
rope                      0.14.0                     py_0  
ruamel_yaml               0.15.46          py37h1de35cc_0  
scikit-image              0.15.0           py37h0a44026_0  
scikit-learn              0.21.2           py37h27c97d8_0  
scipy                     1.3.0            py37h1410ff5_0  
seaborn                   0.9.0                    py37_0  
send2trash                1.5.0                    py37_0  
setuptools                41.0.1                   py37_0  
simplegeneric             0.8.1                    py37_2  
singledispatch            3.4.0.3                  py37_0  
sip                       4.19.8           py37h0a44026_0  
six                       1.12.0                   py37_0  
snappy                    1.1.7                he62c110_3  
snowballstemmer           1.9.0                      py_0  
sortedcollections         1.1.2                    py37_0  
sortedcontainers          2.1.0                    py37_0  
soupsieve                 1.8                      py37_0  
sphinx                    2.1.2                      py_0  
sphinxcontrib             1.0                      py37_1  
sphinxcontrib-applehelp   1.0.1                      py_0  
sphinxcontrib-devhelp     1.0.1                      py_0  
sphinxcontrib-htmlhelp    1.0.2                      py_0  
sphinxcontrib-jsmath      1.0.1                      py_0  
sphinxcontrib-qthelp      1.0.2                      py_0  
sphinxcontrib-serializinghtml 1.1.3                      py_0  
sphinxcontrib-websupport  1.1.2                      py_0  
spyder                    3.3.6                    py37_0  
spyder-kernels            0.5.1                    py37_0  
sqlalchemy                1.3.5            py37h1de35cc_0  
sqlite                    3.29.0               ha441bb4_0  
statsmodels               0.10.0           py37h1d22016_0  
sympy                     1.4                      py37_0  
tblib                     1.4.0                      py_0  
terminado                 0.8.2                    py37_0  
testpath                  0.4.2                    py37_0  
tk                        8.6.8                ha441bb4_0  
toolz                     0.10.0                     py_0  
tornado                   6.0.3            py37h1de35cc_0  
tqdm                      4.32.1                     py_0  
traitlets                 4.3.2                    py37_0  
unicodecsv                0.14.1                   py37_0  
unixodbc                  2.3.7                h1de35cc_0  
urllib3                   1.24.2                   py37_0  
wcwidth                   0.1.7                    py37_0  
webencodings              0.5.1                    py37_1  
werkzeug                  0.15.4                     py_0  
wheel                     0.33.4                   py37_0  
widgetsnbextension        3.5.0                    py37_0  
wrapt                     1.11.2           py37h1de35cc_0  
wurlitzer                 1.0.2                    py37_0  
xlrd                      1.2.0                    py37_0  
xlsxwriter                1.1.8                      py_0  
xlwings                   0.15.8                   py37_0  
xlwt                      1.3.0                    py37_0  
xz                        5.2.4                h1de35cc_4  
yaml                      0.1.7                hc338f04_2  
zeromq                    4.3.1                h0a44026_3  
zict                      1.0.0                      py_0  
zipp                      0.5.1                      py_0  
zlib                      1.2.11               h1de35cc_3  
zstd                      1.3.7                h5bba6e5_0  
```

发现已经安装的里面有：

```
beautifulsoup4
chardet
flask
html5lib
jinja2
lxml
nltk
numpy
openpyxl
pandas
pillow
pip
requests
scipy
six
sqlite
tornado
urllib3
```
以上import都试了一下，都没有问题。其中特殊的有两个： 

```
from bs4 import BeautifulSoup

from PIL import Image（或其他）
```

之前用过的需要安装的库，一共两大类安装方式，一是conda，一是pip。

#### 4.5.1 conda安装

```
conda install selenium
conda install Django
```

#### 4.5.2 pip安装

```
pip install builtwith
pip install kivy
pip install opencv-python(使用：import cv2)
pip install pyautogui
pip install PyPDF2
pip install pyperclip
pip install python-docx(使用：import docx)
pip install python-whois (使用：import whois)
pip install twilio
```

#### 4.5.3 无需特别安装就能使用的库

通过以上检查，发现不少库都无需安装，就能直接使用。这也分两类；一类是anaconda里带的，一类是python标准库。以下不区分，只是让自己知道一下到底是哪些库被我反复使用。

```
import bs4
import chardet
import csv
import datetime
import decimal
import email
import filecmp
import getpass
import itertools
import json
import logging
import lxml
import math
import numpy
import openpyxl
import os
import pandas
import pickle
import PIL
import pprint
import pylab
import random
import re
import requests
import shelve
import shutil
import smtplib
import subprocess
import sys
import threading
import time
import timeit
import tkinter
import tkinter
import traceback
import webbrowser
```

#### 4.5.4 自动化一书中笔记所用的所有import

```
from cencus2010 import allData
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from openpyxl.styles import Alignment
from openpyxl.styles import Font
from openpyxl.styles import NamedStyle
from openpyxl.styles import PatternFill
from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
from PIL import ImageFont
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client
import bs4
import chardet
import csv
import datetime
import docx
import getpass
import json
import logging
import lxml
import openpyxl
import os
import pprint
import pyautogui
import PyPDF2
import pyperclip
import random
import re
import requests
import shelve
import shutil
import smtplib
import subprocess
import sys
import threading
import time
import tkinter
import traceback
import webbrowser
```

### 4.6 第6步，更新库。

``` 
conda info 
conda update conda
conda update python

```
运行结果表明无需更新。

由于现在python直接是3.7.3，所以base环境就是python3。在base下运行python进去，python版本也是python3。看上去以后基本用不上source那句了。

试试pip安装：

之前的记录pyperclip这个库是用pip安装的。 

```
(base) caimeijuandeMacBook-Air:~ caimeijuan$ pip install pyperclip
Collecting pyperclip
Installing collected packages: pyperclip
Successfully installed pyperclip-1.7.0

(base) caimeijuandeMacBook-Air:~ caimeijuan$ pip3 install pyperclip
-bash: /usr/local/bin/pip3: /usr/local/opt/python3/bin/python3.5: bad interpreter: No such file or directory

```
结果base环境无法用pip3。

检查pip版本：  

```
pip show pip

Name: pip
Version: 19.1.1
Summary: The PyPA recommended tool for installing Python packages.
Home-page: https://pip.pypa.io/
Author: The pip developers
Author-email: pypa-dev@groups.google.com
License: MIT
Location: /Users/caimeijuan/anaconda3/lib/python3.7/site-packages
Requires: 
Required-by: 

```

更新pip版本：  

```
pip install --upgrade pip
```
升级成了pip19.2.1。


