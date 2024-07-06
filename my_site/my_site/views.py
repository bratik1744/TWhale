from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return HttpResponse('''<!DOCTYPE html>
<html lang="ru">
<head>
  <title>Рекомендательная инвестиционная платформа</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <style>
    .navbar-custom {
      background-color: #131F2B;
    }
    .navbar-custom .navbar-brand,
    .navbar-custom .nav-link {
      color: white;
    }
    .content-box {
      border: 2px solid black;
      border-radius: 15px;
      padding: 20px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>

<!-- Navigation bar -->
<nav class="navbar navbar-expand-lg navbar-custom">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">TWhale</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <a class="nav-link" href="#">О НАС</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">УСЛУГИ</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">НОВОСТИ</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<!-- Main content -->
<div class="container">
  <div class="content-box">
    <h1>Рекомендательная инвестиционная платформа</h1>
    <h3>Зарабатывайте на акциях, облигациях и ЦФА российских эмитентов</h3> 
  </div>

  <div class="row mt-5">
    <div class="col-sm-4">
      <h3>Column 1</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
    <div class="col-sm-4">
      <h3>Column 2</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
    <div class="col-sm-4">
      <h3>Column 3</h3>        
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
  </div>
</div>

</body>
</html>''')
 
# def about(request):
# 	return HttpResponse('<h1>Рекомендации</h1>')
