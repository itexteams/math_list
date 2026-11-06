import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang9_p4_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lis=[50,100,150,200,250,300,350,400,450,500]
                a=random.choice(lis)
                g=30
                h1=a*2/3   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Người ta treo một chiếc đèn trang trí có trọng lượng $%s$ N lên trần nhà bằng ba sợi dây không dãn, bằng nhau tại ba điểm $A, B, C$ tạo thành một tam giác đều. Mỗi sợi dây tạo với mặt phẳng trần nhà một góc $%s^\\circ$, đèn được giữ ở trạng thái cân bằng (tham khảo hình vẽ). Tính Lực căng trong mỗi sợi dây. \n'
                                '}{' 
                                '''\\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                                \\definecolor{qqffff}{rgb}{0.,1.,1.}
                                \\definecolor{ffxfqq}{rgb}{1.,0.4980392156862745,0.}
                                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                                        \\clip(-0.5676155802111174,-0.0240223386699104) rectangle (4.525139097663924,4.30952220912614);
                                        \\fill[line width=1.pt,color=qqffff,fill=qqffff,fill opacity=1.0] (0.,4.) -- (2.4596629026337564,3.5080674194732486) -- (4.,4.) -- cycle;
                                        \\draw [line width=1.pt,dash pattern=on 1pt off 1pt] (0.,4.)-- (4.,4.);
                                        \\draw [line width=1.pt] (0.,4.)-- (2.5,3.5);
                                        \\draw [line width=1.pt] (2.5,3.5)-- (4.,4.);
                                        \\draw [line width=1.pt] (4.,4.)-- (2.,2.);
                                        \\draw [line width=1.pt] (2.5,3.5)-- (2.,2.);
                                        \\draw [line width=1.pt] (2.,2.)-- (0.,4.);
                                        \\draw [line width=1.pt] (2.,2.)-- (2.,1.5);
                                        \\draw [line width=1.pt,color=ffxfqq] (2.,1.) circle (0.5cm);
                                        \\draw [line width=1.pt,color=ffxfqq] (2.,1.) circle (0.4590489298976475cm);
                                        \\draw [line width=1.pt,color=ffxfqq] (2.,1.2) circle (0.25905147883184787cm);
                                        \\draw [line width=1.pt,color=ffxfqq] (2.,1.2) circle (0.22584036764887794cm);
                                        \\draw [shift={(1.9807422221962652,0.22046755871916318)},line width=1.pt,color=ffxfqq]  plot[domain=0.9378067845566908:2.1543873820969166,variable=\\t]({1.*0.5296448392825023*cos(\\t r)+0.*0.5296448392825023*sin(\\t r)},{0.*0.5296448392825023*cos(\\t r)+1.*0.5296448392825023*sin(\\t r)});
                                        \\draw [shift={(1.981358697295039,0.18209363895545708)},line width=1.pt,color=ffxfqq]  plot[domain=0.9972188242440226:2.0987987443608267,variable=\\t]({1.*0.5316125575889296*cos(\\t r)+0.*0.5316125575889296*sin(\\t r)},{0.*0.5316125575889296*cos(\\t r)+1.*0.5316125575889296*sin(\\t r)});
                                        \\draw [line width=1.pt,color=ffxfqq] (1.6681949928453852,0.6259606474886285)-- (1.6,0.6);
                                        \\draw [shift={(1.4930934991370188,0.28118196039424936)},line width=1.pt,color=ffxfqq]  plot[domain=1.247257610488415:2.192856523073215,variable=\\t]({1.*0.33626469083866145*cos(\\t r)+0.*0.33626469083866145*sin(\\t r)},{0.*0.33626469083866145*cos(\\t r)+1.*0.33626469083866145*sin(\\t r)});
                                        \\draw [shift={(1.7787396449836466,-0.5000385109048507)},line width=1.pt,color=ffxfqq]  plot[domain=1.7318735175974873:2.0281116391881047,variable=\\t]({1.*1.114465156998029*cos(\\t r)+0.*1.114465156998029*sin(\\t r)},{0.*1.114465156998029*cos(\\t r)+1.*1.114465156998029*sin(\\t r)});
                                        \\draw [shift={(1.241301017376162,0.9674165147754537)},line width=1.pt,color=ffxfqq]  plot[domain=4.86671158730798:5.485782010467679,variable=\\t]({1.*0.5134781937581357*cos(\\t r)+0.*0.5134781937581357*sin(\\t r)},{0.*0.5134781937581357*cos(\\t r)+1.*0.5134781937581357*sin(\\t r)});
                                        \\draw [shift={(1.3996223341995184,0.6338457408939661)},line width=1.pt,color=ffxfqq]  plot[domain=4.693389979850406:6.1158549699628,variable=\\t]({1.*0.20321600116209107*cos(\\t r)+0.*0.20321600116209107*sin(\\t r)},{0.*0.20321600116209107*cos(\\t r)+1.*0.20321600116209107*sin(\\t r)});
                                        \\draw [line width=1.pt,color=ffxfqq] (1.805206817306056,0.6836735693380331)-- (1.8690993907934186,0.5600102835866261);
                                        \\draw [shift={(2.11035955631147,0.3784014782046752)},line width=1.pt,color=ffxfqq]  plot[domain=2.6054467210931094:3.857177030962328,variable=\\t]({1.*0.2657317469523881*cos(\\t r)+0.*0.2657317469523881*sin(\\t r)},{0.*0.2657317469523881*cos(\\t r)+1.*0.2657317469523881*sin(\\t r)});
                                        \\draw [shift={(2.733808013306758,0.5707712459106181)},line width=1.pt,color=ffxfqq]  plot[domain=3.207966851735604:3.6435231126396066,variable=\\t]({1.*0.8537737149149713*cos(\\t r)+0.*0.8537737149149713*sin(\\t r)},{0.*0.8537737149149713*cos(\\t r)+1.*0.8537737149149713*sin(\\t r)});
                                        \\draw [shift={(1.735176729818725,0.24418610215918446)},line width=1.pt,color=ffxfqq]  plot[domain=0.05382362795534824:1.0729135696270504,variable=\\t]({1.*0.3072610212666954*cos(\\t r)+0.*0.3072610212666954*sin(\\t r)},{0.*0.3072610212666954*cos(\\t r)+1.*0.3072610212666954*sin(\\t r)});
                                        \\draw [shift={(1.8394577193833366,0.22178794968333995)},line width=1.pt,color=ffxfqq]  plot[domain=0.2995822872113971:1.426582552491198,variable=\\t]({1.*0.2954230773308371*cos(\\t r)+0.*0.2954230773308371*sin(\\t r)},{0.*0.2954230773308371*cos(\\t r)+1.*0.2954230773308371*sin(\\t r)});
                                        \\draw [line width=1.pt,color=ffxfqq] (2.3130881807697956,0.6101592747515213)-- (2.3874808697579226,0.5491563060732313);
                                        \\draw [shift={(2.5739477639314448,0.5218167667095505)},line width=1.pt,color=ffxfqq]  plot[domain=2.99601119974935:4.431379874299508,variable=\\t]({1.*0.18846048136237412*cos(\\t r)+0.*0.18846048136237412*sin(\\t r)},{0.*0.18846048136237412*cos(\\t r)+1.*0.18846048136237412*sin(\\t r)});
                                        \\draw [shift={(2.651573465550806,0.6324587256889299)},line width=1.pt,color=ffxfqq]  plot[domain=3.44714355439609:4.538941349370676,variable=\\t]({1.*0.2769191078030787*cos(\\t r)+0.*0.2769191078030787*sin(\\t r)},{0.*0.2769191078030787*cos(\\t r)+1.*0.2769191078030787*sin(\\t r)});
                                        \\draw [shift={(2.313838914441896,0.153429474214216)},line width=1.pt,color=ffxfqq]  plot[domain=0.5843504323584873:1.3868080303681856,variable=\\t]({1.*0.4025206367826885*cos(\\t r)+0.*0.4025206367826885*sin(\\t r)},{0.*0.4025206367826885*cos(\\t r)+1.*0.4025206367826885*sin(\\t r)});
                                        \\draw [shift={(2.455976003972779,0.2873408643763912)},line width=1.pt,color=ffxfqq]  plot[domain=0.6580362620566105:1.8266775558325508,variable=\\t]({1.*0.2706268813736409*cos(\\t r)+0.*0.2706268813736409*sin(\\t r)},{0.*0.2706268813736409*cos(\\t r)+1.*0.2706268813736409*sin(\\t r)});
                                        \\draw [shift={(1.8887286978332107,1.2980361116208985)},line width=1.pt,color=ffxfqq]  plot[domain=3.82987437114675:5.560936329200472,variable=\\t]({1.*0.1482982867994035*cos(\\t r)+0.*0.1482982867994035*sin(\\t r)},{0.*0.1482982867994035*cos(\\t r)+1.*0.1482982867994035*sin(\\t r)});
                                        \\draw [shift={(2.1120810297741888,1.0661411794798872)},line width=1.pt,color=ffxfqq]  plot[domain=0.8611460048037902:2.2678755888865507,variable=\\t]({1.*0.17458619952985502*cos(\\t r)+0.*0.17458619952985502*sin(\\t r)},{0.*0.17458619952985502*cos(\\t r)+1.*0.17458619952985502*sin(\\t r)});
                                        \\draw [shift={(2.0356226369870023,1.3117278198691478)},line width=1.pt,color=ffxfqq]  plot[domain=1.8085411120537564:4.403744010576648,variable=\\t]({1.*0.11726925427673066*cos(\\t r)+0.*0.11726925427673066*sin(\\t r)},{0.*0.11726925427673066*cos(\\t r)+1.*0.11726925427673066*sin(\\t r)});
                                        \\draw [shift={(1.9600606992570209,1.1)},line width=1.pt,color=ffxfqq]  plot[domain=-1.190813328639118:1.1908133286391185,variable=\\t]({1.*0.10768076775282645*cos(\\t r)+0.*0.10768076775282645*sin(\\t r)},{0.*0.10768076775282645*cos(\\t r)+1.*0.10768076775282645*sin(\\t r)});
                                        \\draw [shift={(1.95,1.293105235902315)},line width=1.pt,color=ffxfqq]  plot[domain=3.362206566516665:5.205217374336273,variable=\\t]({1.*0.10568152606972389*cos(\\t r)+0.*0.10568152606972389*sin(\\t r)},{0.*0.10568152606972389*cos(\\t r)+1.*0.10568152606972389*sin(\\t r)});
                                        \\draw [shift={(2.0711257065228366,1.2501166326411837)},line width=1.pt,color=ffxfqq]  plot[domain=1.723777459142673:3.7554129144497694,variable=\\t]({1.*0.08700886733927776*cos(\\t r)+0.*0.08700886733927776*sin(\\t r)},{0.*0.08700886733927776*cos(\\t r)+1.*0.08700886733927776*sin(\\t r)});
                                        \\draw [shift={(2.0311772599303715,1.077646655050621)},line width=1.pt,color=ffxfqq]  plot[domain=0.2540269971459088:1.8203000015414974,variable=\\t]({1.*0.12626306885652538*cos(\\t r)+0.*0.12626306885652538*sin(\\t r)},{0.*0.12626306885652538*cos(\\t r)+1.*0.12626306885652538*sin(\\t r)});
                                        \\draw [shift={(1.9022463766999511,1.168885400182832)},line width=1.pt,color=ffxfqq]  plot[domain=-1.5988954853768034:0.3081565788425725,variable=\\t]({1.*0.1025860087442258*cos(\\t r)+0.*0.1025860087442258*sin(\\t r)},{0.*0.1025860087442258*cos(\\t r)+1.*0.1025860087442258*sin(\\t r)});
                                        \\draw [line width=1.pt,color=qqffff] (0.,4.)-- (2.4596629026337564,3.5080674194732486);
                                        \\draw [line width=1.pt,color=qqffff] (2.4596629026337564,3.5080674194732486)-- (4.,4.);
                                        \\draw [line width=1.pt,color=qqffff] (4.,4.)-- (0.,4.);
                                        \\draw [line width=1.pt,color=ffqqqq] (1.992830973337101,0.8825189011586119) circle (0.05893492611356297cm);
                                        \\draw [line width=1.pt,color=ffqqqq] (1.992830973337101,0.8825189011586119) circle (0.044015742298720247cm);
                                        \\draw [line width=1.pt,color=ffqqqq] (1.8838292394414524,0.9132191458825291) circle (0.049410850283208595cm);
                                        \\draw [line width=1.pt,color=ffqqqq] (1.8838292394414524,0.9132191458825291) circle (0.03532645464726261cm);
                                        \\draw [line width=1.pt,color=ffqqqq] (1.7873025721287574,0.9672452656470971) circle (0.05270370362665958cm);
                                        \\draw [line width=1.pt,color=ffqqqq] (1.7873025721287574,0.9672452656470971) circle (0.04278650392432937cm);
                                        \\draw [line width=1.pt,color=ffqqqq] (2.1056965046079457,0.9139394941460566) circle (0.04286526144953047cm);
                                        \\draw [line width=1.pt,color=ffqqqq] (2.1056965046079457,0.9139394941460566) circle (0.0319967638640794cm);
                                        \\draw [line width=1.pt,color=ffqqqq] (2.1892569031771445,0.9614824795388766) circle (0.04286526144953087cm);
                                        \\draw [line width=1.pt,color=ffqqqq] (2.1892569031771445,0.9614824795388766) circle (0.03157229819784687cm);
                                        \\draw (-0.6,4.228898124515982) node[anchor=north west] {$A$};
                                        \\draw (2.3,3.5839054476347085) node[anchor=north west] {$B$};
                                        \\draw (3.9,4.195304755928415) node[anchor=north west] {$C$};
                                        \\draw (1.3,2.1864213143919513) node[anchor=north west] {$O$};
                                        \\draw [line width=1.pt] (0.,4.)-- (2.5,3.5);
                                        \\draw [line width=1.pt] (2.5,3.5)-- (4.,4.);
                                        \\draw [line width=1.pt] (4.,4.)-- (0.,4.);
                                        \\begin{scriptsize}
                                            \\draw [fill=ffqqqq] (0.,4.) circle (1.0pt);
                                            \\draw [fill=ffqqqq] (2.5,3.5) circle (1.0pt);
                                            \\draw [fill=ffqqqq] (4.,4.) circle (1.0pt);
                                            \\draw [fill=ffqqqq] (2.,2.) circle (1.0pt);
                                        \\end{scriptsize} 
                                \\end{tikzpicture}'''
                                '}'
                                %(latex(a),latex(g)
                                ))

                # Nội dung lời giải
                loigiai = (
                            'Lực căng trong ba sợi dây tạo thành một tam giác lực, và do tam giác $ABC$ là tam giác đều, ba sợi dây bằng nhau tạo với mặt phẳng trần nhà góc $%s^\\circ$ nên lực căng trong mỗi dây sẽ bằng nhau. \\\\ \n'
                            'Gọi lực căng trong mỗi dây là $\\vec{T}_A, \\vec{T}_B, \\vec{T}_C$. Do đèn ở trạng thái cân bằng, các lực căng phải tạo ra một hợp lực bằng với trọng lượng của đèn, hướng thẳng lên trên. \\\\ \n'
                            'Các lực căng $\\vec{T}_A, \\vec{T}_B, \\vec{T}_C$ đều phân tích được thành tổng hai thành phần phần lực thành phần ngang và thành phần đứng. Thành phần đứng của lực căng sẽ giúp cân bằng trọng lượng của đèn, và thành phần ngang sẽ triệt tiêu lẫn nhau do tam giác đều đối xứng. \\\\ \n'
                            'Mỗi dây tạo với mặt phẳng trần nhà một góc $%s^\\circ$, do đó thành phần đứng của lực căng trong mỗi dây là \\\\ \n'
                            '$$\\left| \\vec{OA\'} \\right|=\\left| \\vec{OA} \\right| \\cdot \\cos %s^\\circ =\\dfrac{1}{2}OA=\\dfrac{1}{2}T.$$ \n'
                            'Tổng của ba thành phần đứng của lực căng phải cân bằng với trọng lượng của đèn nên suy ra \\\\ \n'
                            '$$3T \\cdot \\dfrac{1}{2} =%s \\Rightarrow T=\\dfrac{%s}{\\dfrac{3}{2}} = %s.$$'
                        %(latex(g),latex(g),latex(90-g),
                            latex(a),latex(a),latex(Rational(2*a,3))
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

