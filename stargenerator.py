import random
import PySimpleGUI as sg
from math import *
sptypedata = {
'O2V' : [-5.80, 59],    'O3V' : [-5.80, 59],
'O4V' : [-5.50, 48],    'O5V' : [-5.35, 43],
'O6V' : [-5.10, 35],    'O7V' : [-4.80, 28],
'O8V' : [-4.50, 23.6],  'O9V' : [-4.20, 20.2],
'B0V' : [-3.90, 17.7],  'B1V' : [-3.00, 11.8],
'B2V' : [-1.80, 7.3],   'B3V' : [-1.20, 5.4],
'B4V' : [-1.00, 5.1],   'B5V' : [-0.85, 4.7],
'B6V' : [-0.55, 4.3],   'B7V' : [-0.40, 3.92],
'B8V' : [0.00, 3.38],   'B9V' : [0.50, 2.75],
'A0V' : [0.99, 2.18],   'A1V' : [1.16, 2.05],
'A2V' : [1.35, 1.98],   'A3V' : [1.70, 1.86],
'A4V' : [1.94, 1.93],   'A5V' : [2.01, 1.88],
'A6V' : [2.12, 1.83],   'A7V' : [2.23, 1.77],
'A8V' : [2.32, 1.81],   'A9V' : [2.43, 1.75],
'F0V' : [2.57, 1.61],   'F1V' : [2.76, 1.50],
'F2V' : [2.97, 1.46],   'F3V' : [3.08, 1.44],
'F4V' : [3.20, 1.38],   'F5V' : [3.37, 1.33],
'F6V' : [3.69, 1.25],   'F7V' : [3.80, 1.21],
'F8V' : [4.05, 1.18],   'F9V' : [4.25, 1.13],
'G0V' : [4.48, 1.06],   'G1V' : [4.62, 1.03],
'G2V' : [4.80, 1.00],   'G3V' : [4.87, 0.99],
'G4V' : [4.93, 0.985],  'G5V' : [4.98, 0.98],
'G6V' : [5.10, 0.97],   'G7V' : [5.20, 0.95],
'G8V' : [5.30, 0.94],   'G9V' : [5.55, 0.90],
'K0V' : [5.78, 0.88],   'K1V' : [5.95, 0.86],
'K2V' : [6.07, 0.82],   'K3V' : [6.50, 0.78],
'K4V' : [6.98, 0.73],   'K5V' : [7.28, 0.70],
'K6V' : [7.64, 0.69],   'K7V' : [8.16, 0.64],
'K8V' : [8.43, 0.62],   'K9V' : [8.56, 0.59],
'M0V' : [8.80, 0.57],   'M1V' : [9.64, 0.50],
'M2V' : [10.21, 0.44],  'M3V' : [11.15, 0.37],
'M4V' : [12.61, 0.23],  'M5V' : [14.15, 0.162],
'M6V' : [16.32, 0.102], 'M7V' : [17.70, 0.090],
'M8V' : [18.60, 0.085], 'M9V' : [19.40, 0.079],
}
def genstar(avg_age, age_range):
    # determine spectral type
    sp1 = random.choices(['O', 'B', 'A', 'F', 'G', 'K', 'M'], weights=[0.01, 0.12, 0.61, 3.03, 7.64, 12.13, 76.46])[0]
    sp2 = random.randint(0, 9)
    if sp1 == 'O' and sp2 < 2:
        sp2 = 2
    lum = 'V'
    sptype = '%s%s%s' % (sp1, sp2, lum)
    mass = sptypedata[sptype][1]
    mass = round(mass+random.uniform(-(mass/10), mass/10), 3)
    absmag = round(sptypedata[sptype][0]+random.uniform(-0.1, 0.1), 2)
    # non-main sequence stars, partially based on TTarrants' code
    if sp1 in 'FGKM' and random.uniform(0, 1) < 0.01: # subdwarfs
        lum = 'VI'
    if sp1 == 'O' and random.uniform(0, 1) < 0.01: # Wolf-Rayet stars
        sp1 = random.choice(['WN', random.choice(['WC', 'WO'])])
        lum = ''
    texture = ''
    age = random.uniform(avg_age-age_range, avg_age+age_range)
    luminosity = mass**3.5
    ms_life = 10.9 * mass / luminosity
    if age > ms_life:
        postms_age = age - ms_life
        if postms_age < (ms_life * 0.1):
            lum = 'IV'
            if mass < 2:
                sp1 = 'K'
                absmag = round(random.uniform(3.0, 3.5), 2)
            elif mass > 5:
                sp1 = 'B'
                absmag = round(random.uniform(-4.5, -0.1), 2)
            else:
                absmag = round(random.uniform(0.3, 2.0), 2)
        elif postms_age < (ms_life * 0.15):
            lum = 'III'
            if mass < 2:
                sp1 = 'M'
                texture = 'Red-Giant'
                absmag = round(random.uniform(-0.7, 0.0), 2)
                if random.uniform(0, 1) < 0.01: # carbon stars
                    sp1 = random.choice(['C', 'S'])
            elif mass > 5:
                sp1 = 'O'
                absmag = round(random.uniform(-6.5, -5.1), 2)
            else:
                absmag = round(random.uniform(-4.9, 1.3), 2)
        elif postms_age < (ms_life * 0.17):
            lum = 'II'
            sp1 = 'M'
            texture = 'RBG'
            absmag = round(random.uniform(-3.0, -2.6), 2)
            if random.uniform(0, 1) < 0.01: # carbon stars
                sp1 = random.choice(['C', 'S'])
        elif postms_age < (ms_life * 0.18):
            lum = random.choice(['Ia', 'Ib'])
            sp1 = 'M'
            texture = 'RSG'
            #absmag = round(random.uniform(-7.2, -5.0), 2)
            absmag = round(random.uniform(-3.0, -2.6), 2)
            if random.uniform(0, 1) < 0.01: # carbon stars
                sp1 = random.choice(['C', 'S'])
        else:
            if mass < 9:
                sp1 = random.choice(['DA', 'DB', 'DC', 'DO', 'DQ', 'DZ', 'DX', 'sdO', 'sdB'])
                lum = ''
                mass = round(random.uniform(0.109 - 0.007, 0.109 + 0.007)*mass + random.uniform(0.394 - 0.025, 0.394 + 0.025), 3)
                absmag = 15
            elif mass < 15:
                sp1 = 'Q'
                sp2 = ''
                lum = ''
                absmag = 25
            else: # black hole
                sp1 = 'X'
                sp2 = ''
                lum = ''
                absmag = 50
    sptype = '%s%s%s' % (sp1, sp2, lum)
    return [sptype, absmag, mass, texture]

layout = [
    [sg.Text('RA (degrees):'), sg.Input(size=(15,1), key='RA', default_text='15.984'),
    sg.Text('Dec (degrees:)'), sg.Input(size=(15,1), key='Dec', default_text='21.8947')],
    [sg.Text('Distance (light-years):'), sg.Input(size=(30,1), key='Distance', default_text='2022000')],
    [sg.Text('Radius (light-years):'), sg.Input(size=(30,1), key='Radius', default_text='100')],
    [sg.Text('Number of stars:'), sg.Input(size=(30,1), key='NStars', default_text='10000', disabled_readonly_background_color='#bbbbbb')],
    [sg.Checkbox('Calculate number of stars from radius', key='CalcNStars', default=False, enable_events=True)],
    [sg.Text('Clustering (1-3, smaller = denser):'), sg.Input(size=(20,1), key='Density', default_text='2')],
    [sg.Text('Age (Gyr:)'), sg.Input(size=(15,1), key='AvgAge', default_text='5'), sg.Text('+/-'), sg.Input(size=(15,1), key='AgeRange', default_text='5')],
    [sg.Text('Seed:'), sg.Input(size=(20,1), key='Seed', default_text=str(random.randint(1, 1000000000))),
    sg.Text('Prefix:'), sg.Input(size=(15,1), key='Prefix', default_text='RS-')],
    [sg.Text('Number to start at:'), sg.Input(size=(25,1), key='FirstN', default_text='1')],
    [sg.Text('File name:'), sg.Input(key='Filename', default_text='randomstars')],
    [sg.Button('Generate'), sg.Button('Reset'), sg.Button('Exit'), sg.Text(size=(25,1), key='Output')],
]
window = sg.Window('Celestia Star Generator', layout, icon='sgicon.ico')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Reset':
        window['RA'].update('15.984')
        window['Dec'].update('21.8947')
        window['Distance'].update('2022000')
        window['Radius'].update('100')
        window['NStars'].update('10000')
        window['Density'].update('2')
        window['AvgAge'].update('5')
        window['AgeRange'].update('5')
        window['Prefix'].update('RS-')
        window['FirstN'].update('1')
        window['Seed'].update(str(random.randint(1, 1000000000)))
        window['Filename'].update('randomstars')
        window['Output'].update('All fields reset!')
    if event.startswith('CalcNStars'):
        if values['CalcNStars'] == True:
            window['NStars'].update(disabled=True, text_color='#444444')
        if values['CalcNStars'] == False:
            window['NStars'].update(disabled=False, text_color='#000000')
    if event == 'Generate':
        window['Output'].update('Generating stars...')
        if values['RA'] == '' or values['Dec'] == '' or values['Distance'] == '':
            window['Output'].update('Error: missing coordinates!')
        elif values['Radius'] == '':
            window['Output'].update('Error: missing radius!')
        elif values['CalcNStars'] == False and values['NStars'] == '':
            window['Output'].update('Error: missing number of stars!')
        elif values['Density'] == '':
            window['Output'].update('Error: missing density!')
        elif values['AvgAge'] == '' or values['AgeRange'] == '':
            window['Output'].update('Error: missing average age!')
        elif values['Prefix'] == '':
            window['Output'].update('Error: missing prefix!')
        elif values['FirstN'] == '':
            window['Output'].update('Error: missing first number!')
        else:
            outfile = open('%s.stc' % values['Filename'], 'w')
            catalog = values['Prefix']
            firstn = eval(values['FirstN'])
            basera = eval(values['RA']) # phi
            basedec = eval(values['Dec']) # theta
            basedist = eval(values['Distance']) # rho
            basex = basedist * cos(radians(basedec)) * cos(radians(basera))
            basey = basedist * cos(radians(basedec)) * sin(radians(basera))
            basez = basedist * sin(radians(basedec))
            radius = eval(values['Radius'])
            if values['CalcNStars'] == True:
                nstars = int((radius**3) * 0.01) # from projectrho.com; may be inaccurate
            if values['CalcNStars'] == False:
                nstars = eval(values['NStars'])
            density = eval(values['Density'])
            avg_age = eval(values['AvgAge'])
            age_range = eval(values['AgeRange'])
            if values['Seed'] == '':
                seed = random.randint(1, 1000000000)
            else:
                seed = eval(values['Seed'])
            random.seed(seed)
            for i in range(nstars):
                theta = random.uniform(0, 2*pi)
                v = random.uniform(0, 1)
                phi = acos((2 * v) - 1)
                r = random.uniform(0, radius**density)**(1/density)
                x = r * sin(phi) * cos(theta)
                y = r * sin(phi) * sin(theta)
                z = r * cos(phi)
                x += basex
                y += basey
                z += basez
                dist = sqrt((x**2)+(y**2)+(z**2)) # rho
                ra = degrees(atan2(y, x)) # phi
                if ra < 0:
                    ra += 360
                dec = degrees(asin(z/dist)) # theta
                # orientation of system's ecliptic
                inc = round(random.uniform(0, 360), 3)
                node = round(random.uniform(0, 360), 3)
                if random.uniform(0, 1) < 0.2: # 20% chance of binary
                    stardata1 = genstar(avg_age, age_range)
                    stardata2 = genstar(avg_age, age_range)
                    sptype1 = stardata1[0]
                    sptype2 = stardata2[0]
                    absmag1 = stardata1[1]
                    absmag2 = stardata2[1]
                    mass1 = stardata1[2]
                    mass2 = stardata2[2]
                    texture1 = stardata1[3]
                    texture2 = stardata2[3]
                    sptypes = [[mass1, sptype1, absmag1, texture1], [mass2, sptype2, absmag2, texture2]]
                    sptypes.sort()
                    sptype1 = sptypes[1][1]
                    sptype2 = sptypes[0][1]
                    absmag1 = sptypes[1][2]
                    absmag2 = sptypes[0][2]
                    mass1 = sptypes[1][0]
                    mass2 = sptypes[0][0]
                    texture1 = sptypes[1][3]
                    texture2 = sptypes[0][3]
                    sma = random.uniform(0.5, 50)
                    period = sqrt((sma**3) * (1/(mass1+mass2)))
                    ecc = random.uniform(0.0, 0.9)
                    outfile.write('Barycenter "%s%s"\n' % (catalog, i+firstn))
                    outfile.write('{\n')
                    outfile.write('\tRA %s\n' % round(ra, 8))
                    outfile.write('\tDec %s\n' % round(dec, 8))
                    outfile.write('\tDistance %s\n' % round(dist, 4))
                    outfile.write('}\n\n')
                    outfile.write('"%s%s A"\n' % (catalog, i+firstn))
                    outfile.write('{\t# Mass %s M_Sun\n' % mass1)
                    outfile.write('\tOrbitBarycenter "%s%s"\n' % (catalog, i+firstn))
                    outfile.write('\tSpectralType "%s"\n' % sptype1)
                    outfile.write('\tAbsMag %s\n' % absmag1)
                    outfile.write('\tEllipticalOrbit {\n')
                    outfile.write('\t\tPeriod %s\n' % round(period, 3))
                    outfile.write('\t\tSemiMajorAxis %s\n' % round((sma/(mass1+mass2) * mass2), 3))
                    outfile.write('\t\tEccentricity %s\n' % round(ecc, 3))
                    outfile.write('\t\tInclination %s\n' % inc)
                    outfile.write('\t\tAscendingNode %s\n' % node)
                    outfile.write('\t}\n')
                    if sptype1 == 'X':
                        outfile.write('\tRadius %s\n' % round(mass1*2.95))
                    if texture1 == 'RBG':
                        outfile.write('\tMesh "RBG.cmod"\n')
                    if texture1 == 'RSG':
                        outfile.write('\tMesh "RSG.cmod"\n')
                    if texture1 != '':
                        outfile.write('\tTexture "%s.*"\n' % texture1)
                    outfile.write('}\n\n')
                    outfile.write('"%s%s B"\n' % (catalog, i+firstn))
                    outfile.write('{\t# Mass %s M_Sun\n' % mass2)
                    outfile.write('\tOrbitBarycenter "%s%s"\n' % (catalog, i+firstn))
                    outfile.write('\tSpectralType "%s"\n' % sptype2)
                    outfile.write('\tAbsMag %s\n' % absmag2)
                    outfile.write('\tEllipticalOrbit {\n')
                    outfile.write('\t\tPeriod %s\n' % round(period, 3))
                    outfile.write('\t\tSemiMajorAxis %s\n' % round((sma/(mass1+mass2) * mass1), 3))
                    outfile.write('\t\tEccentricity %s\n' % round(ecc, 3))
                    outfile.write('\t\tInclination %s\n' % inc)
                    outfile.write('\t\tAscendingNode %s\n' % node)
                    outfile.write('\t\tArgOfPericenter 180\n')
                    if sptype2 == 'X':
                        outfile.write('\tRadius %s\n' % round(mass2*2.95))
                    if texture2 == 'RBG':
                        outfile.write('\tMesh "RBG.cmod"\n')
                    if texture2 == 'RSG':
                        outfile.write('\tMesh "RSG.cmod"\n')
                    if texture2 != '':
                        outfile.write('\tTexture "%s.*"\n' % texture2)
                    outfile.write('\t}\n')
                    outfile.write('}\n\n')
                else:
                    stardata = genstar(avg_age, age_range)
                    sptype = stardata[0]
                    absmag = stardata[1]
                    mass = stardata[2]
                    texture = stardata[3]
                    outfile.write('"%s%s"\n' % (catalog, i+firstn))
                    outfile.write('{\t# Mass %s M_Sun\n' % mass)
                    outfile.write('\tRA %s\n' % round(ra, 8))
                    outfile.write('\tDec %s\n' % round(dec, 8))
                    outfile.write('\tDistance %s\n' % round(dist, 4))
                    outfile.write('\tSpectralType "%s"\n' % sptype)
                    outfile.write('\tAbsMag %s\n' % absmag)
                    if sptype == 'X':
                        outfile.write('\tRadius %s\n' % round(mass*2.95))
                    if texture == 'RBG':
                        outfile.write('\tMesh "RBG.cmod"\n')
                    if texture == 'RSG':
                        outfile.write('\tMesh "RSG.cmod"\n')
                    if texture != '':
                        outfile.write('\tTexture "%s.*"\n' % texture)
                    outfile.write('}\n\n')
            outfile.close()
            window['Output'].update('Stars generated!')
window.close()