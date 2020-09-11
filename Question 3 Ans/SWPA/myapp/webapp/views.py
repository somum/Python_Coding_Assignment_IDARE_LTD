from django.shortcuts import render
import math
from django.http import HttpResponse

def index(request):
    return render(request,'webapp/index.html')

def calculate(request):
    if request.POST:
        OD = float(request.POST['OD'])
        WT = float(request.POST['WT'])
        PD = float(request.POST['PD'])
        CA = float(request.POST['CA'])
        thinkness = float(request.POST['thinkness'])
        density = float(request.POST['density'])
        IE = float(request.POST['IE'])
        flooded = float(request.POST['flooded'])
        hydrotest = float(request.POST['hydrotest'])

        # Pipe Inside Radius - r1
        PIR = ((OD - 2 * WT) / 2)

        # Pipe Outside Radius - r2
        POR = (OD / 2)

        # Outer Radius of Coating 1 - r3
        ORC = (POR + thinkness / 2)

        # Total Pipeline Outside Diameter
        TPOD = ORC * 2

        # Pipe Weight per Unit Length in Air (lb/ft)
        PWULA = math.pi * (POR ** 2 - PIR ** 2) / 144 * PD

        # Coating 1 Wt. per Unit Length in Air (lb/ft)
        CULA = math.pi * (ORC ** 2 - POR ** 2) / 144 * density

        # Contents Wt. Per Unit Length in Air (lb/ft)
        ConULA = math.pi * PIR ** 2 / 144 * IE

        # Total Weight per Unit Length in Air (lb/ft)
        TWULA = PWULA + CULA + ConULA

        # Buoyant Force per Unit Length (lb/ft)
        Buoyant = math.pi * ORC ** 2 / 144 * hydrotest

        # Submerged Weight/Unit Length (lb/ft)
        SWUL = TWULA - Buoyant

        # Subm. Specific Gravity with respect to S.W.
        SSGRSW = TWULA / Buoyant

        params = {
            'PIR': PIR, 'POR': POR, 'ORC': ORC, 'TPOD': TPOD, 'PWULA': PWULA, 'CULA': CULA,
            'ConULA': ConULA, 'TWULA': TWULA, 'Buoyant': Buoyant, 'SWUL': SWUL, 'SSGRSW': SSGRSW
        }

    return render(request,'webapp/calculate.html',params)

