import random
import PySimpleGUI as sg
from math import sqrt, pi, degrees, radians, sin, cos, tan, asin, acos, atan, atan2
sptypedata = {
'O0V' : [-7.0, 200],   'O1V' : [-6.5, 150],
'O2V' : [-6.0, 100],   'O3V' : [-5.7, 75],
'O4V' : [-5.5, 50],   'O5V' : [-5.4, 40],
'O6V' : [-5.1, 30],   'O7V' : [-4.8, 28],
'O8V' : [-4.5, 22.9], 'O9V' : [-4.2, 19.7],
'B0V' : [-4.0, 17.5], 'B1V' : [-3.1, 11],
'B2V' : [-1.7, 7.3],  'B3V' : [-1.1, 5.4],
'B4V' : [-1.0, 5.0],  'B5V' : [-0.9, 4.6],
'B6V' : [-0.5, 4.0],  'B7V' : [-0.4, 3.9],
'B8V' : [-0.2, 3.4],  'B9V' : [0.7, 2.8],
'A0V' : [1.11, 2.3],  'A1V' : [1.34, 2.15],
'A2V' : [1.48, 2.05], 'A3V' : [1.55, 2.00],
'A4V' : [1.76, 1.90], 'A5V' : [1.84, 1.85],
'A6V' : [1.89, 1.83], 'A7V' : [2.07, 1.76],
'A8V' : [2.29, 1.67], 'A9V' : [2.30, 1.67],
'F0V' : [2.51, 1.59], 'F1V' : [2.79, 1.50],
'F2V' : [2.99, 1.44], 'F3V' : [3.08, 1.43],
'F4V' : [3.23, 1.39], 'F5V' : [3.40, 1.33],
'F6V' : [3.70, 1.25], 'F7V' : [3.87, 1.21],
'F8V' : [4.01, 1.18], 'F9V' : [4.15, 1.14],
'G0V' : [4.45, 1.08], 'G1V' : [4.50, 1.07],
'G2V' : [4.79, 1.02], 'G3V' : [4.86, 1.00],
'G4V' : [4.94, 0.99], 'G5V' : [4.98, 0.98],
'G6V' : [5.13, 0.97], 'G7V' : [5.18, 0.96],
'G8V' : [5.32, 0.94], 'G9V' : [5.55, 0.90],
'K0V' : [5.76, 0.87], 'K1V' : [5.89, 0.85],
'K2V' : [6.19, 0.78], 'K3V' : [6.57, 0.75],
'K4V' : [6.98, 0.72], 'K5V' : [7.36, 0.68],
'K6V' : [7.80, 0.65], 'K7V' : [8.15, 0.63],
'K8V' : [8.47, 0.59], 'K9V' : [8.69, 0.56],
'M0V' : [8.91, 0.55], 'M1V' : [9.69, 0.49],
'M2V' : [10.30, 0.44], 'M3V' : [11.14, 0.36],
'M4V' : [12.80, 0.22], 'M5V' : [14.30, 0.16],
'M6V' : [16.62, 0.10], 'M7V' : [17.81, 0.090],
'M8V' : [18.84, 0.082], 'M9V' : [19.36, 0.079],
'L0V' : [13.6914380431009, 0.07], 'L1V' : [14.2910702768754, 0.069],
'L2V' : [14.6907025106498, 0.068], 'L3V' : [15.1887523269103, 0.067],
'L4V' : [15.7087740104318, 0.066], 'L5V' : [16.4992919810101, 0.065],
'L6V' : [16.9814005400918, 0.064], 'L7V' : [17.8210720976608, 0.063],
'L8V' : [18.7099255392645, 0.062], 'L9V' : [19.6738297011462, 0.061],
'T0V' : [20.5095577730389, 0.06], 'T1V' : [21.3142121098206, 0.059],
'T2V' : [22.6214507637383, 0.058], 'T3V' : [23.8686833319454, 0.057],
'T4V' : [25.2210829975127, 0.056], 'T5V' : [26.8013702335152, 0.054],
'T6V' : [28.8905508938189, 0.052], 'T7V' : [31.2704703635957, 0.05],
'T8V' : [33.762282824072, 0.048], 'T9V' : [37.0705045282067, 0.046],
'Y0V' : [40.2807703202356, 0.043], 'Y1V' : [43.3725827807118, 0.04],
'Y2V' : [47.4338631374942, 0.037], 'Y3V' : [51.1029632675748, 0.034],
'Y4V' : [55.3523506336577, 0.031], 'Y5V' : [60.2132632242146, 0.028],
'Y6V' : [66.6235631808544, 0.025], 'Y7V' : [73.2338631374942, 0.022],
'Y8V' : [86.2420506770179, 0.019], 'Y9V' : [90.3420506770179, 0.016],
}
def genstar(avg_age, age_range):
    # determine spectral type
    sp1 = random.choices(['O', 'B', 'A', 'F', 'G', 'K', 'M', 'L', 'T', 'Y'], weights=[0.01, 0.12, 0.61, 3.03, 7.64, 12.13, 76.46, 40, 10, 5])[0]
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
            if mass < 1.4: # Chandrasekhar limit
                sp1 = random.choice(['DA', 'DB', 'DC', 'DO', 'DQ', 'DZ', 'DX', 'sdO', 'sdB'])
                lum = ''
                absmag = 15
            elif mass < 2.16: # Oppenheimer-Volkoff limit
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
