from array import array
from django.shortcuts import redirect, render
from Prestamo.models import Prestamo
from datetime import date
import json
# Create your views here.
            
def multas(request): 
    multas = [] 
    hoy = date.today()
    datos = Prestamo.objects.all()
    datos = Prestamo.objects.select_related("Fdispositivo")
    for a in datos:
        fechaFin = a.fechafin
        fechaEntrega = a.fechaentrega
        if (a.fechafin == a.fechaentrega) or (a.Estado == 'Prestado' and hoy<a.fechafin):
            multas.append(0)
        elif(a.Estado == 'Devuelto' and fechaEntrega < fechaFin):
            multas.append(0)
        elif (a.Estado == 'Devuelto'):
            multas.append((fechaEntrega-fechaFin).days*5) 
        elif (a.Estado == 'Prestado' and hoy > fechaFin):
            multas.append((hoy-fechaFin).days * 5) 
    count = 0
    datatosend = []
    for dato in datos:
        datatosend.append({'Usuario': dato.Usuario, 'Dispositivo': dato.Fdispositivo.dispositivo, 'Fecha_inicio': dato.fechainicio, 'Fecha_fin': dato.fechafin, 'Fecha_entrega': dato.fechaentrega, 'Multa': multas[count] })
        if count < len(multas):
            count += 1 
    
    contexto= {
        'datos':datatosend
    }          
    return render(request,'Multas.html', contexto)

