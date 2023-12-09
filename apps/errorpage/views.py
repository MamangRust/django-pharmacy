from django.shortcuts import render


def error_500_view(request):
    return render(request, "500.html", status=500)


def error_403_view(request, exception):
    return render(request, "errors/403.html", status=403)


def error_404_view(request, exception):
    return render(request, "errors/404.html", status=404)
