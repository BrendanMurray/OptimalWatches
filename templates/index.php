{% extends "NavBar.php" %}
{% block bodycontent %}
<html>
 <head>
     <title>Home</title>
     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
 </head>
	 <body class="bg">
	 	<div class="container text-center"></br></br>
	 		<h2 style='text-align:center; vertical-align: middle; color:black;'>Optimal watch list under construction.</h2>
            <ul class="products">
                <li>
                    <a href="#">
                        <img src="/static/images/SNK809.jpg" width=200px>
                        <h4>Seiko SNK809</h4>
                        <p>$58.65</p>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <img src="/static/images/SNZF15J.jpg" width=200px>
                        <h4>Seiko SNZF15J</h4>
                        <p>$225.00</p>
                    </a>
                </li>
                <li>
                    <a href="http://www.amazon.com/Seiko-Mechaical-Alpinist-Automatic-Sarb017/dp/B000KG93BQ/">
                        <img src="/static/images/SARB017.jpg" width=200px>
                        <h4>Seiko SARB017</h4>
                        <p>$375.00</p>
                    </a>
                </li>
            </ul>
	 	</div>
	 </body>
 </html>

{% endblock %}
