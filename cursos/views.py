from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Curso, Modulo, Aula
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def home (request):
          return render(request, 'cursos/home.html')

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})

def detalhes_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    modulos = Modulo.objects.filter(curso=curso).order_by('ordem')
    return render(request, 'cursos/detalhes_curso.html', {'curso': curso, 'modulos': modulos})

def aula(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    return render(request, 'cursos/aula.html', {'aula': aula})

def gerar_certificado(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificado_{curso.titulo}.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 750, f"Certificado de Conclusão")
    p.drawString(100, 730, f"Curso: {curso.titulo}")
    p.drawString(100, 710, f"Aluno: {request.user.username}")
    p.drawString(100, 690, f"Data: {datetime.now().strftime('%d/%m/%Y')}")
    p.save()

    return response
