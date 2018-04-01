#!/usr/bin/env python
#coding: utf-8

def Display(Message, Redirection):
	redirect="5;URL="+Redirection
        print'Content-type: text/html'
        print''

        print'''<!DOCTYPE html>
                        <html>
				<head>
 					<meta charset="UTF-8">
					<meta http-equiv="refresh" content='''+redirect+'''>
					<link href="bootstrap-3.3.7/css/bootstrap.min.css" rel="stylesheet">
    					<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    					<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    					<!--[if lt IE 9]>
      						<script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      						<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    					<![endif]-->
                                </head>
				<body>
					<div class="container">
    						<div class="row">
        						<div class="col-lg-6 col-lg-offset-3">
								<div class="jumbotron text-center">'''
	print '<h3 class="text-danger">'+Message+'</h1>'+'''<br>Vous allez être redirigé d'içi 5 secondes
								</div>                					
							</div> 
            					</div>
                                        </body>
                        </html>'''

