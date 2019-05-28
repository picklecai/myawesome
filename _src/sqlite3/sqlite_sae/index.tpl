% if savetxt == False:
    <h1>打印历史记录</h1>
    <a href='/history'>点击这里</a>
    <form action='/' method="post">
        <h1>输入新记录</h1>
        <input name="record" type="text" />
        <p></p>
        <input value="save" type="submit" />
    </form>

% else:
    <h1>打印历史记录</h1>
    <a href='/history'>点击这里</a>
    <form action='/' method="post">
        <p>保存成功，继续输入：</p>
        <h1>输入新记录</h1>
        <input name="record" type="text" />
        <p></p>
        <input value="save" type="submit" />
    </form>