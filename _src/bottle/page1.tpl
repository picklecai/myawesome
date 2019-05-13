<html>
    <head>
        <title>Static File</title>
    </head>
    <body>
        % if False:
            <h1>It's Pickle.</h1>
        % else:
            <h1>It's Ahcai</h1>
        % end

        % for i in range(2):
            <p>This is loop index: {{i}} </p>
        % end

        <p>Hello, {{name}}. Welcome </p>

        <img src='/static/emoj.png' />

    </body>
</html>



